Vendoring Dependencies
======================

All software has to deal with dependencies. It is a fact of life. No
program can execute without some supporting tools. These tools, more
often than not, are made available by some sort of dependency
management system.

There are many paths to including dependencies in your software. A
popular use case, especially in uncompiled languages like Python or
Ruby, is to resolve dependencies when installing the program. In
Python, `pip install` will look at the dependencies a program or
library needs, download and install them into the environment.

The best argument for resolving dependencies during install (or
runtime) is that you can automatically apply things like security
fixes to dependent libraries across all applications. For example, if
there is a libssl issue, you can install the new libssl, restart
your processes and the new processes should automatically be using the
newly installed library.

The biggest problem with this pattern is that it's easy to have
version conflicts. For example, if a software declares it needs
version 1.2 of a dependency and some other library requires 1.1, the
dependencies are in conflict. These conflicts are resolved by
establishing some sort of sandboxed environment where each application
can use the necessary dependencies in isolation. Unfortunately, by
creating a sandboxed environment, you often disconnect the ability for
a package to inherit system wide libraries!

The better solution is to vendor dependencies with your program. By
packaging the necessary libraries you eliminate the potential for
conflicts. The negative is that you also eliminate the potential for
automatically inheriting some library fixes, but in reality, this
relationship is not black and white.

To make this more concrete lets look at an example. Say we have a
package called "supersecret" that can sign and decrypt messages. It
uses `libcrypto` for doing the complicated work in C. Our
"supersecret" package installs a command line utility `ss` that uses
the `click <http://click.pocoo.org/4/>`_ library. The current version
of click is 4.x but we wrote this when 3.x was released. Lets assume
as well that we use some feature that breaks our code if we're using
4.x.

We'll install it with pip

.. code-block:: bash

   $ pip install supersecret

When this gets installed, it will use the system level shared libcryto
library. But, we've vendored our `click` dependency.

The benefit here is that we've eliminated the opportunity to conflict
with other packages, while still inheriting beneficial updates from
the lower level system.

The arguments against this pattern is that keeping these dependencies
up to date can be difficult. I'd argue that this is incorrect when you
consider automated testing via a continuous integration server. For
example, if we simply have `click` in our dependency list via
`setup.py` or `requirements.txt` we can assume our test suite will be
run from scratch, downloading the latest version and revealing broken
dependencies. While this requires tests that cover your library usage,
that is a good practice regardless.

To see a good example of how this vendoring pattern works in practice,
take a look at the `Go <http://golang.org/>` language. Go has
explicitly made the decision to push dependency resolution to happen
at build time. The result is that go binaries can be copied to a
machine and run without any other requirements.

One thing that would make vendoring even safer is a standard means of
providing information about what libraries are versioned. For example,
if you do use `libssl`, having a way to communicate that dependency
is vendored would allow an operator recognize what applications may
need to be updated when certain issues arise. That in mind, as we've
seen above, many critical components in languages such as Python or
Ruby make it trivial utilize the system level dependencies that
typically are considered when discussions arise regarding rotted code
due to vendoring.

Vendoring is far from a panacea, but it does put the onus on the
software author to take responsibility for dependencies. It also
promotes working software over purity from the user's
perspective. Even if you are releasing services where you are the
operator, managing your dependencies when you are working on the code
will greatly simplify the rest of the build/release process.

.. author:: default
.. categories:: code
.. tags:: python, go, containers, devops
.. comments::
