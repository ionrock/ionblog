Heat vs. Ansible
================

At `work <http://rackspace.com/>`_ we're using `Ansible
<http://ansible.com>`_ to start up servers and configure them to run
`Chef <http://chef.io>`_. While I'm sure we could do everything with
Ansible or Chef, our goal is to use the right tool for each specific
job. Ansible does a pretty decent job starting up infrastructure,
while Chef works better maintaining infrastructure once it has been
created.

With that in mind, as we've developed our Ansible plays and created
some `tooling <https://github.com/ionrock/withenv>`_, there is a sense
that `Heat
<http://docs.openstack.org/developer/heat/template_guide/hot_guide.html>`_
could be a good option to do the same things we do with Ansible.

Before getting too involved comparing these two tools, lets set the
scope. The goal is to spin up some infrastructure. It is easy enough
in either tool to run some commands to setup chef or what have
you. The harder part is how to spin everything up in such a way that
you can confirm everything is truly "up" and configured correctly. For
example, say you wanted to spin up a load balancer, some application
nodes, and some database nodes. You need to be sure when you get a
message that everything is "done" that:

 1. The load balancer is accepting traffic with the correct DNS
    hostname.
 2. There are X number of app server nodes that all can be accessed by
    ssh and any other ports services might be running on.
 3. There are X number database nodes that are accessed via the proxy
    using a private network.

I'm not going to provide examples on how to spin this infrastructure
up in each tool, but rather discuss what each tool does well and not
so well.


Ansible
-------

Anisble, for the most part, connects to servers via ssh and runs
commands. It has a bunch of handy modules for doing this, but in a
nutshell, that is what Ansible does. Since all Ansible really does is
run commands on a host, it might not be clear how you'd automate your
infrastructure. The key is the inventory.

Ansible uses a concept of an inventory that contains the set of hosts
that exist. This inventory can be dynamic as well such that "plays"
create and add hosts to the inventory. A commone pattern we use is to
create some set of hosts and pass that list on to subsequent plays
that do other tasks like configure chef.

What's Good
~~~~~~~~~~~

The nice aspect of Ansible is that you have an extremely granular
process of starting up hosts. You can run checks within the plays to
ensure that nothing continues if there is a failure. You can "rescue"
failed tasks as well in order to clean up broken resources. It is also
really simple to understand what is happening. You know Ansible is
simply running some code on a host (sometime localhost!) via ssh. This
makes it easy to reproduce and perform the same tasks manually.

What's Bad
~~~~~~~~~~

The difficulty in using Ansible is that you are responsible for
everything. There is no free lunch and the definition of what you want
your infrastructure to look like is completely up to you. This is OK
when you're talking about a few servers that all look the same.
But, when you'd need 50 small 512 mem machines along with 10
big compute machines using some shared block storage, 10 memcache
nodes with tons of ram, a load balancer and ensure this infrastructure
runs in 3 different data centers, then it starts to hurt. While there
is a dynamic inventory to maintain your infrastructure, it is not well
integrated as a concept in Ansible. The process often involves using a
template language in YAML to correctly access your infrastructure,
which is less than ideal.

.. note::
   I'm sure ansible gurus have answers to my complaints. No doubt,
   using `tower <http://www.ansible.com/tower>`_ could be
   one. Unfortunately, I haven't had the opportunity to use tower and
   since it isn't free, we haven't considered it for our relatively
   limited use case.

Heat
----

Heat comes from Cloud Formation Templates from AWS. The idea is to
define what you'd like your infrastructure to look like and pass that
definition to your orchestration system. The orchestration system will
take the template, establish a plan of attack and start performing the
operations necessary. The end result is that everything gets created
and linked together as requested and you're done!

At Rackspace, we have a product called `Cloud Orchestration
<http://www.rackspace.com/cloud/orchestration/>`_ that is responsible
for making your template a reality.

What's Good
~~~~~~~~~~~

Heat lets you define a template that outlines precisely what you want
your infrastructure to look like. Just to provide a simple example,
here is a template I wrote to spin up a `Fleet
<https://coreos.com/using-coreos/clustering/>`_ cluster.

.. code-block:: yaml

   heat_template_version: '2015-04-30'
   description: "This is a Heat template to deploy Linux servers running fleet and etcd"

   resources:
     fleet_servers:
       type: 'OS::Heat::ResourceGroup'
       properties:
         count: 3
         resource_def:
           type: 'OS::Nova::Server'
           properties:
             flavor: '512MB Standard Instance'
             image: 'CoreOS (Stable)'
             config_drive: true
             user_data: |
                 #cloud-config
                 coreos:
                   etcd2:
                     discovery: https://discovery.etcd.io/10jfoa9jsd0fjf
                     initial-advertise-peer-urls: http://$private_ipv4:2380
                     advertise-client-urls: http://$public_ipv4:2379
                     listen-client-urls: http://0.0.0.0:2379,http://0.0.0.0:4001
                     listen-peer-urls: http://$private_ipv4:2380,http://$private_ipv4:7001
                   fleet:
                     public-ip: $private_ipv4

                   units:
                     - name: etcd2.service
                       command: start

                     - name: fleet.service
                       command: start

   outputs:
     fleet_ips:
       value: { get_attr: [fleet_servers, accessIPv4] }

Heat templates allow a bunch of features to make this more
programmable such that you pass in arguments where necessary. For
example, I might make `count` a parameter in order to spin up 1
server when testing and more in production.

What we do currently in Ansible is to pass environment variables to
our plays that end up as configuration options for creating our
dynamic inventory. We use the `withenv
<https://github.com/ionrock/withenv/>`_ to make this more declarative
by writing this in YAML. Here is an example:

.. code-block:: yaml

   - RACKSPACE_SERVER_COUNT:
     - MDNS:          1
     - POOL_MGR:      1
     - CENTRAL:       1
     - API:           1
     - DB:            3
     - QUEUE:         3
     - PROXY_HAPROXY: 1
     - SYSLOG_SERVER: 1

As you can see, the process defining this sort of infrastructure is
slowly becoming closer to Heat templates.

Another benefit of using Heat is that you are not responsible for
implementing every single step of the process. Heat provides semantics
for naming a group of servers in such a way that they can be
reused. If you create 5 hosts for some pool that need to be added to a
load balancer, that is easy peasy with Heat. What's more, the
orchestration system can act with a deeper knowledge of the underlying
system. It can perform retries as needed with no manual intervention.

Heat also provides makes it easy to use `cloud-init
<http://cloudinit.readthedocs.org/en/latest/>`_. While this doesn't
provide the same flexibility as an Ansible play, it is an easy way to
get a node configured after it boots.


What's Bad
~~~~~~~~~~

Heat templates are still just templates. The result is that if you are
trying to do complex tasks, get ready to write a bunch of YAML that is
not easy to look at. Heat also doesn't provide a ton of
granularity. If one step fails, where failure is defined by the
orchestration system and the heat template, the entire stack must be
thrown away.

Heat is really meant to spin up or teardown a stack. If you have a
stack that has 5 servers and you want to add 5 more, updating that
stack with your template will teardown the entire stack and rebuild it
from scratch.


Conclusions and Closing Thoughts
--------------------------------

Heat, currently, is a great tool to spin up and tear down a complex
stack. While it seems frustrating that updates do not consider the
state of the stack, it does promote a better deployment design where
infrastructure is an orthogonal concern to how apps are actually run.

Also, Heat at Rackspace, supports `autoscaling
<http://www.rackspace.com/cloud/auto-scale/>`_, which handles the most
common use case of adding / removing nodes from a cluster.

From the user perspective, decoupling your infrastructure from your
application deployments works well when you run containers and use a
tool like Fleet to automatically start your app on the available hosts
in a cluster. When a host goes away, Fleet is responsible for running
the lost processes on the nodes still available in the cluster.

With that in mind, if your applications haven't been developed to run
on containers and that isn't part of your CI/CD pipeline, Ansible is a
great option. Ansible is simple to understand and has a vibrant
ecosystem. There are definitely mismatches when it comes to
infrastructure, but nothing is ever perfect. For example, I do think
the dynamic inventory ends up a little bit cleaner than the machine
semantics I've seen in chef.

Finally, there is no reason you can't use both! In my Heat template
example, you notice that there is an outputs section. That can be used
to create your own dynamic inventory system so you could get the
benefits of setup/teardown with Heat, while doing your initial machine
configuration with Ansible rather than fitting it all into a
cloud-init script.

I hope this overview helps. Both Heat and Ansible are excellent
tools for managing infrastructure. The big thing to rememeber is that
there no free lunch when it comes to spinning up infrastructure. It is
a good idea to consider it as separate process from managing
software. For example, it is tempting to try and install and configure
your app via a cloud-init script or immediately after spinning up a
node in ansible. Step one should be to get your infrastructure up and
tested before moving on to configuring software. By keeping the
concerns separate, you'll find the tools like, heat and ansible,
become more reliable while staying simple.

.. author:: default
.. categories:: code
.. tags:: devops, ansible, heat, openstack, python, chef
.. comments::
