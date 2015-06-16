DevOps System Calls
===================

One thing I've found when looking at DevOps is the adherance to
specific tools. For example, if an organization uses chef, then it is
expected that chef be responsible for all tasks. It is understandable
to reuse knowledge gained in a system, but at the same time, all
systems have pros and cons.

More importantly, each tool adheres to its own philosophies for how a
system should be defined. Some are declarative while others are
iterative and almost all systems define their own (clever at times)
verbage for what the different elements of a system should be.

What the DevOps ecosystem really needs is a low level suite of common
primitives we can build off of. A set of DevOps System Calls, if you
will, we can use to build higher order systems. The reason is to gain
the ability to have some gaurantees we can start to assume will work.

For example, in Python, when I write tests, I assume the standard
library functions such as `open` or the `socket` module work as
expected. You don't see tests such as:

.. code-block:: python

   def test_open():
       with open('test_file.txt') as fh:
           fh.write('foo')

       assert open('test_file.txt').read() = 'foo'

We have similar expectations regarding much of the TCP/IP stack. We
assume the bits are read correctly on the network hardware and passed
to the OS, eventually landing in our program correctly. We take it for
granted that the HTTP request becomes something like
`request.headers['Content-Type']` in our language of choice.

These assumptions let us consider our program in higher level terms
that are portable across languages and systems. Every programmer
understands what it means to open file, connect to a database or make
a HTTP request within our programs because our level of abstraction is
reasonably high.

DevOps could use a similar standard and the implementation doesn't
matter. A machine might be created with Ansible, but configured via
Chef. That part doesn't matter. What matters is we can write simple
code that manages our operations.

For example, lets say I want to spin up a machine to run an app and a
DB. Here is some psuedo code that might get the job done.

.. code-block:: python

   machine = cloud.create(flavor=provider.FLAVOR_COMPUTE)
   machine.bootstrap()
   app = packages.find('my-app')
   machine.deploy(app)

This would compile to a suite of commands that trigger some DevOps
tools do the work necessary to build the machines. The configuration
of what provider, available flavors, and repository locations would
all live in OS level config like you see for your OS networking, auth
and everything else in `/etc`.

The key is that we can assume the calls will work or throw an
error. The process is ecapsulated in such a way that we don't need to
think about the provider, setting API keys in an environment,
bootstrapping the node for our configuration managment and every other
tiny detail that needs to be performed and validated in order to
consider the "recipe" or "playbook" as done.

Obviously, this is not trivial. But, if we consider where our tools
excel and begin the process of encapsulating the tools behind some
higher order concepts, we can begin to create a glossary and shared
expectations. The result is a true Cloud OS.

.. author:: default
.. categories:: code
.. tags:: python, devops, openstack
.. comments::
