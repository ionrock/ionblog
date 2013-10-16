Better Mocking
##############

Recently I've been updating a lot of tests. I've been switching out
Dingus for Mock as well as updating tests that were slow or unclear. It
has been a good experience because it has forced me to look at old tests
and mocking techniques and compare them directly with newer code that
utilized mocks more effectively. I've come up with a couple best
practices to help avoid some mistakes I made initially.
First off, avoid mocking. The ideal situation is that you've written
code in such a way that you never need to mock anything because the code
has been designed to be isolated and modular. As soon as you start to
deal with I/O this become extremely difficult, but as a general rule of
thumb, try running the code rather than mocking.
Secondly, be careful what you mock. One reason to mock is to help
isolate code under test. If you find yourself mocking a ton of objects
and asserting complex sets of methods were called, then that is a red
flag that your code could be refactored. If you think of mocking as a
means of providing a barrier between code under test and the code that
you know works, it becomes slightly clearer when to mock. Your goal
should be to mock the point at which the code under test is accessing
code that you assume is working correctly. For example, when you write
tests, you don't test things supported by Python. Your assumption is
that things like opening files or sockets work correctly. When you are
mocking, the same distinction should be made and that is the point where
a mock will be most helpful.
Finally, mock only one level deep. Specifically related to databases,
there is usually some namespaces that databases provide. MongoDB, for
example, provides a database, which contains collections, that contain
the actual documents. The API then provides access via similar nesting.
When mocking this type of connection, don't try to mock the connection.
Instead mock the point where the query is actually made. Generally, this
makes the mock much simpler and it also makes the assertion solely based
on the query rather than the setup necessary to connect to the database
and find the namespace you will be using.
Hopefully these tips help avoid some mistakes that I made when I first
started trying to use mocks. Using these simple guidelines has made
using mocks much easier. It has also helped to improve and simplify the
code, which is partially the point of writing tests. Good luck and happy
mocking!


.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
