================================
 Configuration and Environments
================================

I've found myself increasinly frustrated with configuration when
programming. It is not a difficult problem, but it gets complicated
quickly when the intent is typically for simplicity.

Lets consider a simple command line client that starts a server and
needs some info such as a database connection, some file paths,
etc. On the surface it seems pretty simple:

.. code-block:: bash

   $ myservice --config service.conf

But, an operator might want to override values in the config via
command line flags.

.. code-block:: bash

   $ myservice --config service.conf --port 9001

This is all well and good, but what if you need to override something
that more sensitive you don't want showing up in the process table
such as the database connection URL. Instead the operator uses an
environment variable.

.. code-block:: bash

   $ export DBURL=mysql://appuser:secret@dbserver
   $ myservice --config service.conf --port 9001

By the way, we haven't talked about things like handling `stdin` so
you can use pipes with your app.

Now, in your code you have to support all these sorts of input and
make the configuration available to the code. This typically happens
as a singleton of sorts that you import all over the place in your
code and tests. This code needs to deal with command line arguments,
reading config files, providing overrides in flags and the
environment, etc.

There are tons of frameworks to make these problems easier, but they
get pretty complicated. What's more, if you've already made some
design decisions about how you want to pass around configuration in
your application, there is a really good chance that library you chose
won't work with that model and you'll need to adjust for that. If you
have a lot of code, this can be a pretty difficult refactoring,
especially if you realize the framework has a bug or doesn't actually
do what it says it does.


Is there a better way?
======================

Maybe? Lately, I've been focusing on only using environment variables
for configuration. This solves some issues in the code. I don't have
to think about parsing command line flags or dealing with override
operations. I also don't have to create some sort of global singleton
because languages provide access to the environment directly. This
doesn't answer things like type conversion, but generally, it is much
simpler.

The reason it is simpler is because of `withenv
<https://github.com/ionrock/withenv>`_. Using `we` I get config files
via YAML and JSON, use the environment and layer overrides as needed
as well as codify that layering on the filesystem. I even have a good
way to load dynamic values to avoid storing secrets on the file
system. The downside is that `we` becomes a dependency, so this isn't
a reasonable solution for some command line tool you distribute
broadly. But, if you're running network services and driving an
operational code base, depending on `we` is a great way to reduce
friction between different systems and have an extremely cross
platform means of communicating configuration to your applications.

The larger philosophy that is at play here is the division between
delcaring configuration and communicating that configuration to the
application. These two aspects are often tightly coupled resulting in
a non-trivial amount of code that is tightly coupled throughout an
application's code base. It also leaks into the operational code as
configuration files need to be written and rewritten, adding an
unnecessary layer of abstraction in order to meet the needs of the
application.

Environment variables can be tricky though. While it is non-trivial to
inspect the environment of a running process, it may be easy for an
attacker to replace the application that is meant to run and capture
sensitive data. If you start processes via shell, that can also lend
itself to executing dangerous code. With that said, there are many
tools to aid in keeping a production filesystem secure such that these
sorts of attacks can be avoided for the most part, leaving only rare
attack vectors available.


But my app doesn't use environment variables
============================================

The on gotcha about a system such as this is that all apps may not be
using environment variables. I've tried to deal with this in `withenv`
by allowing writing a config file before starting the app based on a
template. Until then, the best I can offer to is write something
similar yourself.


Conclusion
==========

I've discussed this topic with some folks and have seen a somewhat
wide spectrum of positive and negative comments. The folks that have
tried `withenv` and see how to extend it, `withenv` becomes a critical
tool. This makes me believe that it is a good method for constructing
an environment and providing it to a process. But, you never know
until you try, so please give it a go the next time you find yourself
exporting environment variables for some code and see if `withenv`
improves anything for you.

.. author:: default
.. categories:: code
.. tags:: devops, chef, ansible, golang, python
.. comments::
