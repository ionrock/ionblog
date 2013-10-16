=====================
 Testing Terminology
=====================


There are some common terms in testing that are often
misunderstood. We have unit tests, functional test, integration tests,
smoke tests, etc. I'm going to try and give each a definition in
hopes of clarifying how to think about each type of test and how it
fits within the scope of a test suite.

We'll start with unit tests.

Unit Tests
==========

A unit test typically will be a mirror of some class where each method
of the class has a test method that asserts the functionality. Unit
tests are great for testing classes that actually do things and have
methods that perform specific actions. A unit test is pointless for
a container class. Unit tests can also be really difficult for classes
that defines operations on a lot of other classes.

Let me explain.

You often will have classes that serve as glue amidst your more
traditional "object" classes. Your object classes are things like
models or anything that maps really obviously to a real world
thing. These are your "User" or "EnemyNinja" classes that are meant to
provide an actual "thing" in your application.

You glue classes are the ones that take all these objects and do stuff
with them. The glue classes often are containers of functions that are
used to organized complex algorithms and maintain state. They usually
will have one major "function" that will incorporate many
methods. These kinds of classes are not the ones you need unit tests
for because they really don't provide a "unit" in your
application. The glue really is providing some "functionality", which
means they really need a different kind of test.


Functional Tests
================

Functional tests are often confused as tests for functions. If you use
this definition, it becomes unclear why you would have "functional"
tests and "unit" tests since "unit" tests really just test things like
methods. And lets face it, methods really are functions when it gets
down to it.

A functional test is meant to test functionality. Functions are
conceptually where you keep your algorithms. Therefore functional
tests should effectively assert that your algorithm or operation is
correct.

Often your functional tests are where you will be testing your glue
classes that don't fit the traditional "object" classes mentioned
above. Your functional tests will confirm the interaction between
objects and make sure that you are getting the right output based on
some set of inputs. Functional tests should make sure your application
functions as expected.

There is a difference though between the functionality of an
application and how it functions when it is deployed. Functional
testing is meant to assert at the algorithmic level, things are
working as expected.


Integration Tests
=================

Applications never run within a vacuum. Any software must run on
actual hardware and the vast majority of cases, software must interact
with other software. Integration tests are meant to test these
interactions between different pieces of software and hardware.

An integration tests should verify that when an application interacts
with some other system outside of itself, that it is doing the right
thing. The "right thing" is going to depend on what the application is
interacting with. An integration test asserts the APIs are used
correctly.

This definition doesn't meant that integration tests need to fully
test any API the program interacts with. For example, if you read a
file, you don't need to test that your language is properly creating
file handle, reading the bytes and converting them to the right
string.

An integration test will assert that the parts of the API that are
used work correctly. An integration test will also assert that when
the output is not as expected, your application has a specified means
of handling the problem.

Just to be clear, when I say API, this includes internal application
APIs. Most applications define tons of APIs that are meant to be
followed in the future. Whether they are a specific base class or some
IPC protocol used between worker processes, integration tests should
assert that things work as expected and that things fail as expected.


Smoke Tests
===========

Smoke tests take the concepts of an integration test to the next
level. A smoke test is meant to make sure that actual users experience
the application as intended.

Smoke tests are difficult to maintain and perform because often times
they are really boring. This makes it hard to find people to take the
time to run the tests and report findings. It can also be difficult to
communicate when things break.

Difficulties aside, smoke tests provide a sanity check. Smoke tests
will allow you to be confident you didn't introduce new issues that
prevent users from doing whatever it is they need to do with your
software.


How About Code Coverage
=======================

Code coverage is meant to see if you have tests that execute all the
code in the code base. Looking at a higher level, unit, functional,
integration and smoke tests are all tools to help make sure your code
is fully tested without sacrificing efficiency or accuracy. Each type
of test layers on top each other in order to create provide a stable
base.

It is sort of like a pyramid.

The bottom of the pyramid is the guarantees of your platform. You have
an operating system, hardware and a programming language that acts to
provide you reliable answers. When you add 1 + 1 in your language, you
will always get 2. When your user types a Q on the keyboard, you will
get a Q in your application.

The next layer of the pyramid are your essential functions and
objects. These are small "units" of work that can be accomplished
atomically using the stable layer of your platform. Unit tests cover
these functions and make sure that everything else that depends on
these units of work receive the same stability the platform offers.

The next layer is the algorithmic layer. You combine your objects and
functions into more complex algorithms and operations. These
operations assume simple use cases only need to deal with seemingly
atomic operations. Your functional tests make sure this level of code
works as expected.

The next layer is your interaction layer. This is where you consider
what happens when you have threads and processes using the same
resources. The code here talks to services and maintains state in such
a way that your algorithms can function atomically and reliably. Your
integration tests cover this class of code.

Finally, you have your completed application where you see it not as
individual pieces of code, but a single tool. Smoke tests consider the
software as a whole and reflect this completed perspective.

These layers work together to provide guarantees and stability. The
result is that the code usage becomes "covered".


Testing Distribution
====================

Up until this point I've tried to give each type of testing a somewhat
equal standing in the grand scheme of things. The truth is that each
application is very different. If your application does nothing but
crunches numbers, then your integration tests will most likely be very
minimal since you do not need to interact with different systems. If
your application acts as an middleman between many different systems,
you might have very few unit tests and no smoke tests because your
users are other systems that do most of the actual work.

Instead of looking at testing as something that you do to code you've
written, testing as a whole should assert a quality design. The
layering of tests should align with the layering of your application
functionality. Like a pyramid, the goal is to create stable layers of
functionality. If it is easy to organize your tests and cover all your
code with your unit, functional and integration tests, then you can
also be confident you've designed a quality piece of software. Your
smoke tests can then confirm that the internal quality of the code is
reflected to the users.


.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
