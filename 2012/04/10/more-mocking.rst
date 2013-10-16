More Mocking
############

Recently the codebase I've been working on has gone through a major
change that has brought about an opportunity to make some major changes
in our test suite. My perspective has been that it is generally a good
thing. Our goal is to simplify the code, remove complexity and create a
test suite that helps improve our code. This last bit is really
important because in the past our test suite, while relatively
comprehensive, did not always help make our code better.

Specifically, the tests were brittle. There was a lot of code necessary
to make the tests work correctly. This either involved complicated
mocking or starting/stubbing a lot of services. The result was that the
tests were extremely slow and were easy to break.

Since the reboot of the code, we've got a new test suite that has around
400 tests. Some are still really slow, but we've start organizing tests
into different categories, unit, functional and integration. Obviously
the integration tests are slower. The functional tests are a mix bag.
Some are slow where others are relatively quick. Many could be faster
with some mocks, which leads me to the unit tests. These are meant to be
extremely fast and isolate the code under test as much possible.

The unit tests are the newest and test the newest code. I realized
relatively quickly that I would need to use mocks to make these test
fast since they all interact with HTTP services heavily. If I didn't
mock the responses then the tests were extremely slow and interacted
with a large part of the system. The positive aspect of using the mocks
was the the tests were really fast. This is a really great feature! I
can run all the unit tests in less than half a second.

The downside is that sometimes these tests seem to replicate the code in
the method. This is not terrible, but it doesn't help test what the
method should really achieve. Instead it focuses on the steps taken to
presumably achieve the correct end goal. This indirection is not always
entirely opaque and I can see that at times it is really effective. It
also raises issues in the code that reflect a method is trying to do too
much.

Also, each test ended up following a similar pattern. The initial steps
built the state you required. Sometimes this was trivial, but many times
it could be a pain in the neck. My suspicion is that dealing with state
for a complex document oriented system intrinsically is difficult to
test functionally because the system must always be adjusting state
instead of performing operations. For example, if you had a method that
adds two numbers, there is a limited set of input that confirms the
output is going to be correct. But, when you have a document that needs
to be mutated, the input and the output becomes less obvious.

The next step of the pattern was doing the action. This traditionally
involved instantiating the object and calling the method. This was
generally extremely simple and as expected.

After the method was called it was then time to assert the results.
Where ever possible my goal was to assert a value returned by the
method. Often times though, I had to make sure specific API calls were
made to the backend service using the correct data. This didn't bother
me as a tactic because the APIs were mocked and by confirming the
behavior, in theory, we confirm we are using the API correctly. If we
were having to mock more of the system, then I'd presume that could be
considered evidence the system design is not as good as it could be.

In the past I had tried to use mocks for tests and came away with a
feeling that my tests weren't really very effective. When you isolate
the functionality by fooling your code, you are not really asserting the
code functions correctly. That said, it is clear that you cannot expect
to build a large system and always test all components. In my new
testing environment, I'm loving mocking in my isolated unit tests. I'm
also mocking lightly in my functional tests to help speed them up where
possible. In taking a layered approach I'm able to cover the code
without hiding when errors actually happen. At the same time, I'm
finding that every test I write now feels like it needs a ton of setup
in order to run. Part of that is code smell, but at the same time I also
think it is a negative attribute of using mocks.

Time will tell if the tactics I'm using are best. I do feel I'm using
the mocks more effectively than I have in the past. The type of code
that uses mocks also feels more natural than the code I tried to mock in
the past. Finally, I also switched to using `Mock`_, which I'm pretty
happy with.

.. _Mock: http://www.voidspace.org.uk/python/mock/


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
