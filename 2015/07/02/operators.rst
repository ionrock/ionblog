===========
 Operators
===========

Someone mentioned to me a little while back a disinterest in going to
`PyCon <https://us.pycon.org/>`_ because it felt directed towards
operators more than programmers. Basically, there have become more
talks about integrations using Python than discussions regarding
language features, libraries or development techniques. I think this
trend is natural because Python has proven itself as a main stream
language that has solved many common programming problems. Therefore,
when people talk about it, it is a matter of how Python was used
rather than describing how to apply some programming technique using
the language.

With that in mind, it got me thinking about "Operators" and what that
means.

Where I `work <https://rackspace.com>`_ there are two types of
operators. The first is the somewhat traditional system
administrator. This role is focused on knowledge about the particular
system being administered. There is still a good deal of automation
work that happens at this level, but it is typically focused on
administering a particular suite of applications. For example,
managing apache httpd or bind9 via config files and rolling out
updates using the specific package manager. There is typically more
nuance to this sort of role than can be expressed in a paragraph, so
needless to say, these are domain experts that understand the common
and extreme corner cases for the applications and systems they
administer.

The second type of operator is closer to the operations included
devops. These operators are responsible for building the systems that
run application software. These folks are responsible for designing
the systems and infrastructure to run the custom applications. While
more traditional sysadmins use configuration management, these
operators master it. Ops must have a huge breadth of knowledge that
spans everything. File systems, networking, databases, services, *nix,
shell, version control and everything in between are all topics that
Ops are familiar with.

As a software developer, we think about abstract designs, while ops
makes the abstract concrete.

After working with Ops for a while, I have a huge amount of respect
due to the complexity that must be managed. There is no way to simply
`import cloud` and `cloud.start()`. The tools available to Ops for
enacapsulating concepts is rudimentary by necessity. The configuration
management tools are still very new and the terminology hasn't
coalesced towards design patterns due to the fact that everyone's
starting point is different. Ops is where linux distros, databases,
load balancers, firewalls, user management and apps come together to
actually have working products.

It is this complexity that makes DevOps such an interesting place for
software development. Amidst the myriad of programs and systems, there
needs to be established concepts that can be reused as best practices,
and eventually, as programs. Just as C revolutionized programming by
allowing a way to build for different architectures, DevOps is
creating the language, frameworks, and concepts to deploy large scale
systems.

The current state of the art is using configuration manangement /
orchestration tools to configure a system. While in many ways this is
very high level, I'd argue that it is closer to assembly in the grand
scheme of things. There is still room to encapsulate these tools and
provide higher level abstractions that simplify and make safe the
processes of working with systems.


.. author:: default
.. categories:: code
.. tags:: devops, python, chef, ansible
.. comments::
