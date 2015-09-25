More Virtual Machine Development
================================

I've `written before
<http://ionrock.org/2015/04/10/virtual_machine_development.html>`_
developing on OS X using virtual machines. That was ~6 months ago and
it seemed time for an update.


Docker is Better
----------------

One thing that has improved is Docker. `Docker Compose
<https://docs.docker.com/compose/>`_ now works on OS X. `Docker
Machine <https://docs.docker.com/machine/>`_ also has become more
stable, which allows a `boot2docker <http://boot2docker.io/>`_ like
experience on any "remote" VM where "remote" includes things like
cloud servers as well as Vagrant VMs.

In terms of development, Docker Compose seems really nice in
theory. You can define a suite of services that get started and linked
together without having to manually switch configs all over the
place. Eventually, Docker Compose will also be supported on things
like `Docker Swarm <https://docs.docker.com/swarm/>`_, which means, in
theory at least, that you could deploy an entire stack.

In practice though, the linking is not as robust as one would like. If
a container doesn't start, the link doesn't get added to the host
machine's `/etc/hosts` file. It's also unclear how portable this is
across different distros. While an `/etc/hosts` file is pretty
standard, it still must be used by the OS using whatever resolution
system is in place. I've gotten the impression that things are moving
towards injecting DNS in the mix in order to avoid lower level
changes, but time will tell.

While it hasn't worked for me, I'm still planning to keep trying
docker compose as it seems like the best solution to starting up a
suite of microservices for development.


Docker and Emacs !?!
--------------------

Emacs has a package called `Prodigy
<https://github.com/rejeep/prodigy.el>`_ that lets you manage
processes. I also played around with running my dev environment in a
docker container where I just used Prodigy to run all the services I
need as subprocesses of the Emacs process. It is like a poorman's
emacs init system. Alas, this wasn't much better than working on a
cloud server. While it is clever and portable, it still is like
ssh'ing into a box to work, which get frustrating over time.


Vagrant and rdo
---------------

A while back I released a tool called `rdo
<http://ionrock.org/2015/05/07/announcing_rdo.html>`_ that lets you
remotely execute commands like they were local. This has become my
primary entry point into using Vagrant and avoiding having to use a
terminal to access my dev environment. I also integrated this into my
`xe <https://github.com/ionrock/xe>`_ tool to make things more
cohesive, but overall, it is easier to just use rdo.

Even with a reasonably efficient way to make VM development feel
local, it's still a little painful. The pain comes in the slowness of
always working through the VM. Vagrant shares (by way of VirtualBox
shared folders) are slow. I'm looking at using `NFS
<https://docs.vagrantup.com/v2/synced-folders/nfs.html>`_ instead,
which I understand should be faster, so we'll see. The fastest method
is to use rsync. This makes sense because it basically copies
everything over to the VM, making things run as "native" speeds. My
understanding is that this is a one way operation, so that doesn't
work well if you want to run a command and have the output piped to a
file so you can use it locally (ie dosomething | grep "foo" >
result_to_email.txt).


Cloud Server
------------

I also spent some time developing on a cloud server. Basically, I set
up an Ubuntu box in `our <https://rackspace.com>`_ cloud and ssh'd in
to work. From a purely development standpoint, this worked pretty
well. I used `byobu <http://byobu.co/>`_ to keep my emacs and shell
sessions around after logging out or getting disconnected. Everything
worked really fast as far as running tests, starting processes and
even IRC. The downside was the integration into my desktop.

When I work in a local Emacs, I have key bindings and tools that help
me work. I use Emacs for IRC, therefore, I have an easy key binding to
open URLs. This doesn't work on a cloud server. What's more, because
I'm using Emacs, any fancy URL recognition iTerm2 often gets screwed
up where I can't click it, and in some cases, I can't even copy
it. Another thing that was problematic was that since the cloud server
used a hypervisor, I couldn't run VirtualBox. This meant no `Chef
Kitchen <https://docs.chef.io/kitchen.html>`_, so I was forced to head
back to OS X for doing any devops work. Due to firewall restrictions,
I also couldn't access my work email on my cloud server.

Lastly, since the machine was on a public cloud, running any process
was usually available to the public! In theory, these are just dev
processes that don't matter. In practice though, spinning up a jenkins
instance to test jobs in our real environment, was dangerous to run
openly.

The result was that I had to make a rather hard switch between pure
dev work and devops work when using a cloud server. I also had to be
very aware of the security implications of using my cloud server to
access important networks.


Sidenote: Emacs in the Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Emacs through a terminal, while very usable, has some nits related to
key bindings. There are far fewer key bindings available in a terminal
due to the shell having to provide actual characters to the
process. While I tried to work around these nits, the result was more
complex key bindings that I had no hopes of establishing as habit. One
example is `C-=` (C == ctrl). In reStructuredText mode, hitting `C-=`
will allow cycling through headings and automatically add the right
text decoration. Outside `rst-mode`, I typically have `C-=` binded to
expand region. Expand region lets me hit `C-=` repeated to
semantically select more of the current section. For example, I could
expand to a word, sentence, paragraph, section, and then
document. While these seem like trivial issues, they are frustrating
to overcome as they have become ingrained in how I work. This
frustration is made more bitter by the fact that the hoops I've jumped
through are simply due to using OS X rather than Linux for
development.


Future Plans
------------

I'm not going to give up just yet and install Linux on my Macbook
Pro. I'm doing some work with `rdo` to allow using docker in addition
to Vagrant. I'm also confident that the docker compose and network
issues will be solved relatively soon. In the meantime, I'm looking at
ways to make `rdo` faster by reusing SSH connections and seeing if
there are any ways to speed up shared folders in Vagrant (`NFS
<https://docs.vagrantup.com/v2/synced-folders/nfs.html>`_, `Rsync
<https://docs.vagrantup.com/v2/synced-folders/rsync.html>`_).


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
