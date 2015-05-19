Docker vs. Provisioning
=======================

Lately, I've been playing around with `Docker <https://docker.com>`_
as I've moved back to OS X for development. At the same time, I've
been getting acquainted with `Chef <https://chef.io>`_ in a reasonably
complex production environment. As both systems have a decent level of
overlap, it might be helpful to compare and contrast the different
methodologies of these two deployment tactics.

.. note:
   You'll notice the title of this post is "Docker vs. Provisioning"
   rather than specifically comparing Chef. The reason being is you
   could substitute other provisioning tools such as Ansible,
   SaltStack, Puppet, etc. as all have the same essential difference
   to Docker.


What does Docker actually do?
-----------------------------

Docker wraps up the container functionality built into the Linux
kernel. Basically, it lets a process use the machine's hardware in a
very specific manner, using a predefined filesystem. When you use
docker, it feels like starting up a tiny VM to run a process. But,
what really happens, the container's filesystem is used along with the
hardware provided by the kernel in order to run the process in an
isolated environment.

When you use Docker, you typically start from an "image". The image is
just an initial filesystem you'll be starting from. From there, you
might install some packages and add some files in order to run some
process. When you are ready to run the process, you use docker run and
it will get the filesystem ready and run the process using the
computer's hardware.

Where this differs from VM is that you only start **one**
process. While you might create a container that has installed
Postgres, RabbitMQ and your own app, when you run `docker run myimage
myapp`, no other processes are running. The container only provides
the filesystem. It is up to the caller how the underlying hardware is
accessed and utilized. This includes everything from the disk to the
network.


What does a Provisioner do?
---------------------------

A provisioner, like Chef, configures a machine in a certain
state. Like Docker, this means getting the file system sorted out,
including installing packages, adding configuration, adding users,
etc. A provisioner also can start processes on the machine as part of
the provisioning process.

A provisioner usually starts from a known image. In this case, I'm
using "image" in the more common VM context, where it is a snapshot of
the OS. With that in mind, a provisioner doesn't require a specific
image, but rather, the set of required resources necessary to consider
the provisioned machine as complete. For example, there is no reason
you couldn't use a provisioner to create user directories across
variety of unices, including OS X and the BSDs.


Different Deployment Strategies
-------------------------------

The key difference when using Docker or a provisioner is the strategy
used for deployment. How do you take your infrastructure and configure
it to run your applications consistently?

Docker takes the approach of deploying containers. The concept of a
container is that it is self contained. The OS doesn't matter,
assuming it supports docker. Your deployment then involves getting the
container image and running the processes supported by the container.

From a development perspective, the deliverable artifact of the build
process would be a container (or set of containers) to run your
different processes. From there, you would configure your
infrastructure accordingly, configuring the resources the processes
can use at run time.

A provisioner takes a more generalized route. The provisioner
configures the machine, therefore, it can use any number of
deliverables to get your processes running. You can create system
packages, programming language environments or even containers to get
your system up and running.

The key difference from the devops perspective (the intersection of
development and sysops), is development within constraints of the
system must be coordinated with the provisioner. In other words,
developers can't simply choose some platform or application. All
dependencies must be integrated into the provisioning system. A docker
container, on the other hand, can be based on any image and use any
resource available within the image's filesystem.


What do you want to do?
-----------------------

The question of whether to use Docker or a provisioning system is not
an either or proposition. If you choose to use Docker containers as
your deployment artifact, the actual machines may still need to be
configured. There are `options
<https://coreos.com/using-coreos/clustering/>`_ that avoid the need to
use a provisioning system, but generally, you may still use something
like Chef to maintain and provision the servers that will be running
your containers.

One vector to make a decision on what strategy to use is the level of
consistency across your infrastructure. If you are fine with
developers creating containers that may use different operating
systems and tooling, docker is an excellent choice. If you have hard
requirements as to how your OS should be configured, using a
provisioning system might be better suited for you.

Another thing to consider is development resources. It can be a
blessing and a curse to provision a development system, no matter what
system you use. Your team might be more than happy to take on managing
containers efficiently, while other teams would be better off leaving
most system decisions to the provisioning system. The ecosystem
surrounding each platform is another consideration.


Conclusions
-----------

I don't imagine that docker (and containers generally) will completely
supplant provisioning services. But, I do believe the model does aid
in producing more consistent deployment artifacts over time. Testing a
container locally is a reasonably reliable means of ensuring it should
run in production. That said, containers require that many resources
must be configured (network, disk, etc.) in order to work
correctly. This is a non-trivial step and making it work in
development, especially when you consider devs using tools like
boot2docker, can be a difficult process. It can much easier to simply
spin up a Vagrant VM with the necessary processes and be done with
it. Fortunately, there tools like `docker compose
<http://docs.docker.com/compose/>`_ and `docker machine
<http://docs.docker.com/machine/>`_ that seem to be addressing this
shortcoming.


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
