To Mock or Not
##############

The first day of `PyCon`_ is almost over and it seems my interests have
swayed towards testing. It is probably not terribly surprising as I'm
currently working on making some major changes to the tests for the
project I work on at my job.

One talk I was very interested in was `Stop Mocking, Start Testing`_.
Some developers gave an overview of conclusions they've made regarding
testing while working on Google Project Hosting. This talk, I'd argue,
was a "con" in terms of mocking. They still mocked I/O resources, but
generally, they aimed to make their classes and operations easily
testable, which in turn, removed the need for lots of isolation via
mocks.

Another talk I was interested in was `Fake It Til You Make It: Unit
Testing Patterns With Mocks and Fakes`_. This talk discussed mocking
techniques and basic Unittest best practices. This was definitely a
"pro" mocking talk and assumed that mocking was the best means of
isolating tests.

I'm hear to tell you I'm thoroughly confused as to what methodology is
better. Personally, I like the "con" argument because the result of the
tests was simple, encapsulated code that did small operations. The "pro"
argument had relatively "normal" code, but the quality seemed tied to
the fact that each component was tested in complete isolation.
Everything is tested individually and the goal is coverage of every
statement, which just means that anytime you exit some tested scope, you
have a test (ie any return and exception).

I honestly don't know that either approach is better. One aspect that I
think frames both talks is the state of the code when the tests were
written. In the "con" case, the code was old and had no real tests. The
process was taking legacy code and writing new tests and code within an
orchestra of services. The "pro" case I believe was primarily written in
the situation of new projects written from scratch. At least these were
the examples that were given. I wanted to ask about the size of the
codebase(s) that the "pro" speaker used these techniques with as well as
when the tests were written, but there wasn't enough time. I suspect
that legacy code might be kinder to refactoring for better tests without
mocks, but I could be wrong there.

It is interesting to me that these questions are not obvious. In fact it
seems that no one really has a solid answer for whether or not to mock
extensively. This is not to say there are not strong opinions, but I
suspect they are limited in experience. For example, a programmer that
does mostly contract jobs using Django is going to have a different set
of code requirements then someone picking up on a 10 year set of chatty
services providing a critical business need. Hopefully, I'll have some
conversations that might help shed a little more light on the decisions
others have made.

.. _PyCon: http://us.pycon.com/2012/
.. _Stop Mocking, Start Testing: https://us.pycon.org/2012/schedule/presentation/315/
.. _`Fake It Til You Make It: Unit Testing Patterns With Mocks and Fakes`: https://us.pycon.org/2012/schedule/presentation/336/


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
