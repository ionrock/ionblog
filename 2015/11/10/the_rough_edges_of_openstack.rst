==============================
 The Rough Edges of Openstack
==============================

I'm thankful `Rackspace <http://rackspace.com>`_ sent me to Tokyo for
the `OpenStack Summit <http://openstack.org/summit>`_. Besides the
experience of visiting Tokyo, the conference and design summit proved
to be a great experience. Going into the summit, I had become a little
frustrated with the `OpenStack <https://openstack.org>`_ development
ecosystem. There seemed to be a lot of decisions that separated it
from more main stream Python development with little actual reason for
the diverting from the norm. Fortunately, the summit contextualized
the oddities of developing OpenStack code, which made the things more
palatable as a developer familiar with the larger Python ecosystem.

One thing that hit me at the summit was that OpenStack is really just
5 years old. This may not seem like a big deal, but when you consider
the number of projects, amount of code, infrastructure and
contributors that have made all this happen it is really
impressive. It is a huge community of paid developers that have
managed to get amazing amounts of work done making OpenStack a
functioning and reasonably robust platform. So, while OpenStack is an
impressive feat of software development, it still has a ton of rough
edges, which should be expected!

As a developer, it can be easy to come to a project, see how things
are different and feel as though the code and/or project is of poor
quality. While this is a bad habit, we are all human and fear things
we don't understand! The best way to combat this silliness is to try
and educate those coming to a new project on what can be
improved. In addition to helping recognize ways to improve a project,
it helps new developers feel confident when they hit rough edges to
dig deeper and fix the problems.

With that in mind, here are some rough edges of OpenStack that
developers can expect to run into, and hopefully, we can fix!


OpenStack Doesn't Mean Stable
=============================

You'll quickly find that "OpenStack" as a suite of projects is
HUGE. Each of these projects is at different stages of
stability. Documentation may be lacking, but the code is well tested
and reliable, while other projects may have docs and nothing else. It
critical to keep this in mind when developing for an OpenStack project
that the other OpenStack requirements, and there will be **TONS**, may
not be entirely stable.

What this means is that it is OK to dig deep when trying to figure out
why something doesn't work as expected. Don't be afraid to checkout
the latest version of the library and dive into the source to see what
is going on. Add some temporary print / log messages to get some
visibility into what's happening. Write a small test script to get
some context. All these tactics you'd use with your own internal
libraries are the same you should use with **ANY** OpenStack project.

This is not to say that OpenStack libraries aren't stable. You can't
assume that just because it has gotten the label "oslo" or
"OpenStack", that it has been tested and considered working. The
inclusion of libraries or applications into OpenStack, from a
development standpoint, has more to do with answering the question of
"Does the community need this". Inclusion means that the community has
identified a **need**, not a fully fleshed out solution.


Not Invented Here
=================

OpenStack is an interesting project because the essence of what it
provides is an interface to existing software. `Nova
<http://docs.openstack.org/developer/nova/>`_, for example, provides
an interface to start VMs. Nova doesn't actually do the work to act as
a hypervisor, instead, it leaves that to pluggable backends that work
with things like `Xen <http://www.xenproject.org/>`_ or `KVM
<http://www.linux-kvm.org/page/Main_Page>`_. Right off the bat, this
should make it clear that when a project is labeled as the OpenStack
solution for X, it most likely means it provides an interface for
managing some other software that implements the actual functionality.

`Designate <http://docs.openstack.org/developer/designate/>`_ and
`Octavia <http://docs.openstack.org/developer/octavia/>`_ are two
examples of this. Designate manages DNS servers. You get a REST
interface that can can update different DNS servers like bind or
PowerDNS (or both!). Designate handles things like multi-tenancy,
validation and storing data in order to provide a reliable
system. Octavia does a similar task, but specifically for `haproxy
<http://haproxy.org>`_.

It doesn't stop there though. OpenStack aims to be as flexible as
possible in order to cater to the needs / preferences of operators. If
one organization prefers `Postgres <http://www.postgresql.org/>`_ over
`MySQL <https://www.mysql.com/>`_ that should be supported because an
operator will need to manage that database. The result is that many
libraries tend to provide the same sort of wrapping. `Tooz
<http://docs.openstack.org/developer/tooz/>`_ and `oslo.messaging
<http://docs.openstack.org/developer/oslo.messaging/>`_, for example,
provide access to distributed locking and queues
respectively. Abstractions are created to consistently support
different backends, so projects can not only provide flexibility for
core functionality, but also the services that support the
application.

In the cases where there really was a decision to reimplement some
library, it is often due to an in compatibility with another
library. A good example of this is oslo.messaging. It supports
building apps with an async or background worker pattern, much like
celery. This makes one wonder, why not just `celery
<http://www.celeryproject.org/>`_! My understanding is that celery has
been tried in many different projects and it wasn't a good fit within
the community at large.

By the way, my vague answer of "it wasn't a good fit" is
intentional. There are so many projects in OpenStack that often times
these questions are bought up again and again. A new project is
started and the developers try out other libs, like celery, because it
is a good solution that is well supported. Sometimes the technical
challenges of integration with other services is a problem, while
other times, the dependencies of the library aren't compatible with
something in OpenStack, making it impossible to resolve
dependencies. I'm sure there are cases where someone just doesn't like
the library in question. No matter what the reasons are, OpenStack has
a huge plane of software that makes it hard for new libraries to be a
"good fit", so sometimes it is easier to rewrite something
specifically for OpenStack.


Dependencies
============

OpenStack is committed to providing software that can be
deployed via distro packages. In other words, OpenStack wants to make
`yum install openstack` or `apt-get install openstack` work. It is a
noble goal, especially for a suite of applications written in python,
moving at radically different rates of change.

You see, distro package managers have different priorities than most
Python authors may have when it comes to packaging. A distro is
something of an editor, ensuring that all the pieces for all the use
cases work reliably. This is how Red Hat provides general "linux"
support, by knowing that all the pieces work together. Python REST
services (like OpenStack), on the other hand, typically assume that
the person running it uses some best practices such as a separate
virtualenv for each application. This design pattern means that at the
application level, the dependencies are isolated from the rest of the
system.

Even though the vast majority of OpenStack operators don't rely on
system packages in a way that requires all projects use the same
versions, it is an implementation detail OpenStack has adopted. As
a developer, you have to be ready to deal with this limitation, and
more importantly, the impact it has on your ability to introduce new
code. I believe that this restriction is most likely to blame for the
Not Invented Here nature of many OpenStack tooling, which leads
reimplementations that are not very stable.


Why Develop for OpenStack?
==========================

If OpenStack has such a rough development experience, why should you
commit to learning it and developing on OpenStack software?

You'll remember, I began all this with a recognition that OpenStack
is only 5 years old. Things will continue to change, and I believe,
improve. Many of the rough edges of OpenStack have been caused by
growing pains. There is a crazy amount of code happening and it takes
time and effort to improve development patterns. Even though it can be
rough at first to develop in OpenStack, it gets better.

Another reason to develop OpenStack code is that it is a exciting
work. OpenStack includes everything from low level, high performance
systems to distributed CPU intensive tasks to containers and
micro-services. If you enjoy scaling backend applications, OpenStack is
a great place to be. The community is huge with loads of great
people. OpenStack also makes for a very healthy career path.

No project is perfect, and OpenStack is no different. Fortunately,
even though there are rough edges, OpenStack is a great project to
write code. If you are new to OpenStack development and need a hand,
please don't hesitate to reach out!


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
