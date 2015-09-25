Vendoring
=========

`Glyph <https://glyph.twistedmatrix.com/>`_ wrote an interesting
article on `software you can use
<https://glyph.twistedmatrix.com/2015/09/software-you-can-use.html>`_. In
the article, he argues that Python is pretty good at installing server
software, but lacks when it comes to other platforms. The key, as
Glyph mentions, is that we need an artifact that vendors all
dependencies. There are some issues regarding system packages,



As an `OpenStack
<https://openstack.org>`_ developer, this struck a chord with
me. OpenStack has a very specific list of approved packages. If you
use these packages, then there isn't a problem. Adding a new package
though means entering the package in some qualification process that
ensures the new library meets stability requirements and doesn't
conflict with other OpenStack projects.

While this commitment to quality and cross-project requirements seem
like a good idea, the restriction is actually due to the nature of
python software distribution that Glyph mentions. In order to provide
packages to Debian based systems, there can be no vendored
libraries. Therefore, as OpenStack wants to provide .debs, all
requirements across all projects must be in line with each other and
runnable from a single system Python. The benefits of this policy is
that security patches and updates can be rolled out to an entire
system rather than require updates for each application. The downside
is that development in OpenStack is plagued with NIH type decisions
because it is often easier to just re-write some library than face the
daunting process of inclusion in the global requirements list.

Looking at `Go <https://golang.org>`_, **ALL** requirements are added
at build time. After a build, you can just copy the resulting artfact
to the machine and you're done. While it does remove the ability to
roll out a systemwide patch to a bunch of Go programs, the tradeoff is
an extremely simple deployment. It would be really great if we could
include a similar vendoring in Python.


Why Deployment is Expensive
---------------------------

Deploying software is expensive. If you've ever written Chef recipes,
Ansible playbooks, Puppet classes, etc. you quickly realize the
process of taking code in a repository to a running process is
complex. Python, like many programming language dependency systems,
don't allow for installing "system" packages. Therefore, even if your
app has defined all its dependencies, there could be *implicit*
assumptions that some library already exists on the system. The result
is that deploying an app is typically a mashup of writing
configuration, installing system packages and getting everything ready
for the application's build process.

While PHP as a language gets some grief, its deployment process is
drop dead simple. Deploying new PHP code is usually as simple as
copying a file to the server. That's it. While it does make
assumptions the server is configured, in terms of the complexity of
deploying code, it doesn't get much better. Go is another example of
this simplified complexity. You can simply copy the executable to the
server and run the process. It is no wonder that Go has become such a
powerful system administration language.

The key to a painless deployment is to provide artifacts that can be
copied to the machine. On the desktop, Apple uses this model very
successfully. Java, with its jar, war and ear formats, also uses this
model on servers.


But What about Security Updates?
--------------------------------

It is Debian's policy that no software packages include any vendored
libraries. One reason is that it opens the system up to security
problems because all apps need to be updated in order to apply a
security patch to a common library. In Debian's case, I'm sure there
are other legal and copyright concerns as well, but we'll skip that
for the time being.

The problem with Debian's stance for many users is that Debian is not
the final authority for what goes on the system. If I'm deploying an
OpenStack project as an operator, I will use a system like Chef to
configure the server. While I appreciate Debian's role in ensuring a
secure system, it is my responsibility as an operator to 1) have
working software and 2) manage what software is used by the
system. When I deploy server software, the analysis of what is secure
is not always that simple, especially if my infrastructure and use
cases make assumptions that don't fall in line with Debian's idea of
what software should be on the system. As an operator, there are many
programs I'm fine letting Debian manage, but, at the end of the day,
time is spent keeping critical systems up and running for a few select
pieces of software.

Going away from the server for a minute, the situation is similar on
the desktop. If you've ever developed a desktop application that runs
on many platforms, you quickly realize that there are almost no
assumptions you can make. Updates rarely are applied consistently. If
the software is not free, the party selling the software has the
responsibility to ensure their stuff works and doesn't introduce
system instability or security issues. The result is


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
