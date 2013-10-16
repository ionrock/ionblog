Dad and adding Build Steps
##########################

I've been working on the same project at work for a while so when I have
a little free time I like to work on `Dad`_. I'm not sure if I've
mentioned it before, but its a process manager application that is meant
to support a more comprehensive set of management tasks. It came from my
idea of a devserver much like `Foreman`_, with biggest difference being
that instead of simply controlling whether a process is up or down, you
can ask it to perform tasks within its own sandboxed environment.

It got me thinking about how most people in the Python community end up
looking to `virtualenv`_ for their deployment, when there might be other
tactics. Virtualenv is a great tool and use it all the time for
development. There are tons of people that find great success with it as
a deployment tool as well, so I don't play to sway the opinion away from
it. I do think there could be better ways though.

One of the reasons developers choose to write applications in languages
like Ruby or Python is because it is easy to get a large portion of the
functionality done quickly. Honestly, during this phase of development a
tool like virtualenv makes a ton of sense because it provides a similar
speed when deploying. Installing all your dependencies at deploy time is
not a huge deal because there aren't that many and most of the time they
don't change. In other words, it isn't broken so why fix it?

The reason to consider a different methodology early on is because it is
easier to do it early on. Eventually the simple Django app you wrote is
going to push the limits of what the framework offers out of the box.
You start adding functionality that doesn't have an obvious fit within
the repo. As these problems evolve the application gets complex. The
complexity moves from being a simple repository level complexity to
abstractions via services and processes. There is nothing wrong with
this, but it presents a different sort of problem to manage. You no
longer are simply refactoring code, you are orchestrating services both
in development for testing and in production. There is a lot that can
change going from dev to production and I don't believe that tools like
virtualenv really help that issue. They do too many things.

With that in mind if you start out your application with a healthy
appreciation for processes and services, there is a good chance you can
avoid much of the pain of learning to orchestrate these details
consistently. This is why I started writing Dad. It is a process manager
that you can use in development to orchestrate your services. You can
then use it to run your tests and eventually the idea is that your
development process from code to test to production is same on your
local machine as it is when you deploy to production.

The key to making this transition is to recognize the need for different
steps of deployment. In Python it is easy to just pull some code on a
server, run setup.py install in a virtualenv and fire off a command to
start it up. The problem is when you app actually needs 10 other
services, one of which is a database written in C++ and another is a
Java application. When you have more steps for deployment, you have
points in the process where you can create the necessary pieces to make
deploying as simple as untarring a tarball vs. running setup.py, finding
dependencies, downloading them, installing console scripts, etc.

The first step in a deployment process is to make a package. This is
something that makes it easy to put files in the execution environment
easy. Creating a tar.gz via setuptools is probably a good first step.
RPMs or dpkg might be another option. But in either case, you need
something you create that can be used to build the actual "thing" that
will be deployed.

Once you have a package, you then need to make a build. The difference
between a package and a build is that a build has to be able to be run
in a production-like environment without having to do anything but
copying all the files from the build. `Pip`_ supports a "freeze"
operation where it takes all the currently installed requirements and
their versions to create a requirements file that can be used to
recreate an environment. This sort of function should happen at the
package phase, prior to the build. The build stage should find all the
requirements and compile them together accordingly. The result of that
operation then is what is used to create the actual build.

After the build, it is time to actually deploy. The deployment should be
really simple. You should have an execution environment where you are
going to put the files. That is where the build is installed. This is
where Dad comes in. When you add an application to a Dad server it
creates a sandbox for you to create an execution environment. You have
your executable files and supporting files as needed and Dad is
configured to call commands in order to manage the processes.

While all the above seems like a ton of work it really is a lot easier
than you might think. It is pretty easy to write a short and simple
script or Makefile that has to run "python setup.py sdist". From there
it is pretty simple to run a command that installs it into a brand new
virtualenv and resolves dependencies. At the end you can pop the build
in your Dad sandbox and run the tests. All in all, it really should be
simple, especially if start when your application is still manageable.

Lastly, Dad is no where near finished. The design has been hashed out a
few times with different models and only now would I argue that the
model is correct. There is still a lot to do. If it interests you, feel
free to fork it and try hacking on it.

.. _Dad: http://bitbucket.org/elarson/dad/
.. _Foreman: http://blog.daviddollar.org/2011/05/06/introducing-foreman.html
.. _virtualenv: http://virtualenv.org
.. _Pip: http://pip-installer.org


.. author:: default
.. categories:: code
.. tags:: devops, programming, python, sysadmin
.. comments::
