TDD
===

I watched `DHH's keynote at Railsconf 2014
<https://www.youtube.com/watch?v=9LfmrkyP81M>`_. A large part of his
talk discusses the misassociation of TDD on metrics and making code
"testable" rather than stepping back an focusing on clarity, as an
author would when writing.

If you've ever tried to do true TDD, you might have a similar feeling
that you're doing it wrong. I know I have. Yet, I've also seen the
benefit of iterating on code via writing tests. The faster the code /
test cycle, the easier it is to experiment and write the
code. Similarly, I've noticed more bugs show up in code that is not as
well covered by tests. It might not be clear how DHH's perspective
then fits in with the benefits of testing and facets of TDD.

What I've found is that readability and clarity in code often comes by
way of being testable. Tests and making code testable can go along way
in finding the clarity that DHH describes. It can become clear very
quickly that your class API is actually really difficult to use by
writing a test. You can easily spot odd dependencies in a class by the
number of mocks you are required to deal with in your tests. Sometimes
I find it easier to write a quick test rather than spin up a repl to
run and rerun code.

The point being is that TDD can be a helpful tool to write clear
code. As DHH points out, it is not a singular path to a well thought
out design. Unfortunately, just as people take TDD too literally,
people will feel that any sort of granular testing is a waste of
time. The irony here is that DHH says very clearly that we, as
software writers, need to practice. Writing tests and re-writing tests
are a great way to become a better writer. Just because the ideals
presented in TDD might be a bit too extreme, the mechanism of a fast
test suite and the goal for 100% coverage are still valuable in that
they force you to think about and practice writing code.

The process of thinking about code is what is truly critical in almost
all software development exercises. Writing tests first is just
another way to slow you down and force you to think about your problem
before hacking out some code. Some developers can avoid tests, most
likely because they are really good about thinking about code before
writing it. These people can likely iterate on ideas and concepts in
their head before turning to the editor for the actual
implementation. The rest of us can use the opportunity of writing
tests, taking notes, and even drawing a diagram as tools to force us
to think about our system before hacking some ugly code together.


.. author:: default
.. categories:: code
.. tags:: python, tdd, testing
.. comments::
