A Serious TDD Attempt
#####################

Designing a public API is very different than designing a language level
API. The former involves a language agnostic view of a problem. There
are broad assumptions that are made to help with interoperability, but
you don't have to contend with language specific features. At the
language level, things are much different. You are thinking in terms of
language features and available constructs alongside best practices that
could very well define how useful a library is. While I can say I've
designed quite a few public-type APIs, designing language level systems
is still pretty new.

At my job, I've recently been rather frustrated because there is a ton
of code that has become tough to maintain, yet refactoring and testing
has been really difficult. Part of the difficulty has been my lack of
design skills when it comes to language level APIs. What better way to
refactor and improve the testability of the code than to try writing a
more usable API on top of the existing code? Here is where TDD is coming
in handy.

It seems like a really helpful exercise to consider how I'd like to
work with the code and write tests in order to figure out a good plan
for refactoring. TDD fits the bill nicely because by forcing myself to
write (and rewrite) the ideal code. The biggest confusion now is not
necessarily the API, but rather how it integrates with the underlying
systems and existing code. TDD examples are all pretty primitive and
don't necessarily make it clear how to consider integration testing and
more complicated scenarios. My theory is that there are some good
techniques out there already. One thing that seems to be consistent is
that tests should be fast, so figuring out how to test functionality
without actually requiring services to be running might be key. We'll
see how it turns out!


.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
