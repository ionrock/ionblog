Iterative Code Cycle
====================

TDD_ prescribes a simple process for working on code.

 1. Write a failing test
 2. Write some code to get the test to pass
 3. Refactor
 4. Repeat

If we consider this cycle more generically, we see a typical cycle
every modern software developer must use when writing code.

 1. Write some code
 2. Run the code
 3. Fix any problems
 4. Repeat

In this generic cycle you might use a REPL, a stand alone script, a
debugger, etc. to quickly iterate on the code.

Personally, I've found that I *do* use a test for this iteration
because it is `integrated into my editor
<https://github.com/ionrock/pytest-el>`_. The benefit of using my test
suite is that I often have a repeatable test when I'm done that proves
(to some level of confidence) the code works as I expect it to. It may
not be entirely correct, but at least it codifies that I think it
should work. When it does break, I can take a more TDD-like approach
and fix the test, which makes it fail, and then fix the actual bug.

The essence then of any developer's work is to make this cycle as
quick as possible, no matter what tool you use to run and re-run your
code. The process should be fluid and help get you in the flow when
programming. If you do use tests for this process, it *may* be a
helpful design tool. For example, if you are writing a client library
for some service, you write an idealistic API you'd like to have
without letting the implementation drive the design.

TDD has been on my mind recently as I've written a lot of code
recently and have questioned whether or not my testing patterns have
truly been helpful. It has been helpful in fixing bugs and provides a
quick coding cycle. I'd argue the code has been improved, but at the
same time, I do wonder if by making things testable I've introduced
more abstractions than necessary. I've had to look back on some code
that used these patterns and getting up to speed was somewhat
difficult. At the same time, anytime you read code you need to put in
effort in order to understand what is happening. Often times I'll
assume if code doesn't immediately convey exactly what is happening it
is terrible code. The reality is code is complex and takes effort to
understand. It should be judged based on how reasonable it is fix once
it is understood. In this way, I believe my test based coding cycle
has proven itself to be valuable.

Obviously, the next person to look at the code will disagree, but
hopefully once they understand what is going on, it won't be too bad.

.. _TDD: http://en.wikipedia.org/wiki/Test-driven_development


.. author:: default
.. categories:: code
.. tags:: python, pytest, testing
.. comments::
