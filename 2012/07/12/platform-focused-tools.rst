Platform Focused Tools
######################

The more I learn as a programmer, the most I recognize why Linux is the
way the it is. There are a set of tools that devops considers for
deployments and system administration. Sometimes, as developers we avoid
learning things. It is more fun to write code and consider how this code
we write might very well be tool that finally solves some problem. The
irony is that the tool that finally solves the problem is probably
already written and you'd rather code than read how to use it!

There is a really good chance that tool already exists within the \*nix
ecosystem. You need a deployment and packaging system, try `RPM`_ or
`APT`_. You want to build things, `Make`_ (while having warts) is up to
the task once you understand it. You need to be sure your daemons are up
and running and can be controled correctly, check out `Upstart`_ or
`init`_. They may not be perfect, but they are well tested. Also, these
tools were written with \*nix in mind as opposed to your application or
programming language. While that means they are not optimized for you,
they **are** optimized for the operating system, your platform you
deploy to.

This realization came about recently because at work we use
`daemontools`_ to manage our deployment tool. The deployment tool has
two main components it uses on each node. There is a launching piece
that has a heartbeat of sorts that checks it has instances of the
applications running. If something isn't running, it will try to start
it. When it starts it, it actually starts a wrapper process that will
accept signals from our main server. If you wanted to terminate some
application process, you tell the main server, it tells the wrapper
process to term, and the launch tool realizes it is gone and starts a
new instance.

The problem with this system is daemontools knows nothng of this
hierarchy. Daemontools assumes you're working with processes that are
meant to be run as daemons (get it "daemon tools"). Our system cuts off
some of daemontools responsibility to restart processes. The result
being that if our hiearchy of processes fails for some reason (broken
network connection for example), daemontools is unaware and we have to
log into the node to get things back in shape. If we kill a node via the
master and it dies, but our lauching tool doesn't recognize it is gone,
then we need to restart the launch the launch tool. But that orphans our
other processes and we have to kill them manually before starting back
up our daemontools managed process.

Even if you didn't follow any of that, the moral of the story is to
consider the \*nix tools. If you have a long running process that should
start with the OS, use the init or upstart system. That is what it is
made for and has been doing a good job of for a **long** time. Does it
suck to write init.d scripts? Yes. Will you need to consider how your
app handles signals the like? You betcha. Once you have that in place
will you have problems restarting your app due to your tools? Nope!

As I'm still relatively new to a lot of these sorts of tools, so I'm
sure I'm paiting a prettier picture than reality. That said, the reality
is that we deploy our apps on \*nix platforms which have a specific
model in place for managing processes and the file system. Tools like
init, Make, RPM, etc. all were designed with these realities in mind.
While it may seem like a lot of work to understand and use these tools,
I want to remind you it is even more work to create your own and
maintain them.

I'm also not trying to suggest that you shouldn't use `supervisord`_ or
create your own deployment strategy based on `virtualenv`_ and `pip`_.
Many people have found success creating a Python specific release
strategy. The point is that while it may seem obvious and easier to
consider your language and application specific tools, a platform
focused deployment strategy may be a better tact in the long run.

.. _RPM: http://www.rpm.org
.. _APT: http://wiki.debian.org/Apt/
.. _Make: http://software-carpentry.org/4_0/make/intro/
.. _Upstart: http://upstart.ubuntu.com/
.. _init: http://en.wikipedia.org/wiki/Init
.. _daemontools: http://cr.yp.to/daemontools.html
.. _supervisord: http://supervisord.org/
.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org/


.. author:: default
.. categories:: code
.. tags:: devops, programming, python
.. comments::
