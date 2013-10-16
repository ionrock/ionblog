Circus and Process Management
#############################

I've been looking at `Circus`_ bit as a process or service management
tool for testing. Often when you are testing an web application, there
are a suite of services that are required in order to test different
levels of the stack. One argument is that you should mock most of these
interactions, which I simply don't agree with. It makes sense to mock
and assert how you are calling your objects that do I/O, but it is
dangerous to assume these sorts of tests truly verify your code is
working. Only when you actually touch the code can you be somewhat sure
that you are on track.

In the project I work on, we've started creating three different test
types. There are unit tests that do utilize mocking techniques and aim
for a very explicit exercising of an objects method. So far these have
been focused on our models as they typically would do I/O and they have
very focused methods. The second type of tests are functional tests.
These are tests that assert functionality is working by using a large
portion of the stack. We still mock some aspects in order to control the
output, but generally, the idea is to use stubs and let each service
handle the requests. The last set of tests are integration tests. These
include things like selenium tests or tests that are known to be long
running because they are metrics against threading or synchronization
issues.

In the last two scenarios, it is important to be able to start up
services for the tests on demand. Circus is of interest to me because in
addition to a command line interface, it also provides a library for
orchestrating services. There is one thing that I'd personally like to
see in a tool like this that I believe others would appreciate as well.

In the example Circus config there are listed a couple delay keys that I
presume are there to help processes wait until some resource is
available. A good example would be waiting for a database to be
available prior to starting a service that depends on that database.
There are two obvious problems with any sort of time delay when running
tests. The first is that you could be waiting longer than you have to.
If you start up a lot of services and have to wait a second or two for
each, then you are almost certain to have a slow test suite. The second
is that things will break inconsistantly if the delay is not long
enough. You end up working with a lowest common denominator where the
person with the slowest machine defines the delay time for everyone,
including those with powerful machines or the CI server which most
likely has a good amount of processing power.

In our test suite, we've solve this by creating a service manager that
instantiates service classes. These classes have some knowledge of how
to determine a service or resource is really up. For example, we use
`MongoDB`_. Our service class for MongoDB will start up the process and
block until a connection can be made. We also have some applications
that provide a status URL that is not available until the application is
truly ready.

In a system like Circus, it is difficult to do this because you don't
want to require each application or service to implement a specific API
in order to use it with Circus. With that in mind, I'd propose that
Circus allow using a process to define the wait time before proclaiming
the process is available. The config might look something like this:

::

    [watcher:myprogram]
    cmd = python
    args = -u myprogram.py $WID
    numprocesses = 5
    wait_for_cmd = python
    wait_for_args = check_myprogram.py -p $PORT

Circus would use this "wait\_for" process to finish before reporting the
actual process as available.

I haven't tried Circus just yet, but I plan to take a look and see if
this idea could work for it. When you try to orchestrate services as
generic processes it is very difficult to maintain a featureful API
because within the concept of a process there is such a wide breadth of
implementations that supporting anything but the typical
start/stop/restart is close to impossible. Adding this sort of
deterministic hook could allow for more advanced features such as
dependencies and priorities that would make it possible to reliably
start up a suite of services in such a way that it was always consistent
and didn't have any unnecessary waiting.

.. _Circus: http://circus.readthedocs.org/en/latest/index.html
.. _MongoDB: http://mongodb.org


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
