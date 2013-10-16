=================================
 The Problem with Dynamic Typing
=================================

In my quest to become a better tester, I've been looking at how we use
logs and error messages to find and fix bugs. This is obviously a really
important part of systems since it is often times the primary means of
finding how a system is failing in production. The glaring detail that
seems to show up is the importance of types within a system. This might
partially be because the system I'm personally working on includes an
entire language with its own types. That said, my gut is telling me the
problem is more general.

This past year my focus has been on maintenance. It is a huge part of
programming and has been a struggle for me lately. My perception of the
issue has gone from personal doubts to blame and back again. I'm
beginning to wonder if the issue is not necessarily the actual code in
question, but the platform itself. Specifically, the idea of dynamic
typing is starting to feel somewhat dangerous. This opinion is partly
because some experience in a large C# code base. It was a big code base
that had to run on a variety of systems (browsers, .net runtime,
operating system), yet had almost no automated testing. Despite the size
and breadth of the code base, it took only a few weeks to become
relatively proficient fixing bugs and adding features. A benefit I
attribute to the impact of static typing.

While I'm sure there are plenty of proponents that would argue with me
here, I'd like to make it clear that a simple yes/no regarding dynamic
typing is not what I'm talking about. The real problem is the paradigm
that current dynamic typed systems utilize to express the code.

Let's talk about Python for a moment. Python is an object oriented
language that has some functional features, but by and large, is built
around objects. At the same time it is dynamically typed. In fact it is
considered "pythonic" to avoid using types and depend on duck typing.
For example, it is better to use something like the "in" operator when
testing whether a variable contains some value since it can be applied
to a dict's keys, a list or a set. This sort of system can feel
invigorating because you have very few limits when writing code.

As I've delved further into TDD, something smells of a cover up. The
freedom that was available with duck typing starts to feel rather
inhibiting. This is because the tests should help establish and enforce
the contract. What we've done by removing the typing and adding the
tests is established the contract within the tests instead of the type.
Some would argue this is a good thing because your contract can be more
detailed and robust since you have the full language to work with. The
problem though is that you've lost the language level constraint
provided by keeping contracts in the types.

Taking a larger look at the picture, the idea really doesn't depend on
types as much as where you keep your contracts. Programming works
because there is agreement. Code promises other code to work a certain
way and in doing so we have (mostly) working systems. Things like
objects and classes all help to enforce this idea by providing the
semantic keywords to encapsulate the ideas, thus providing more
abstraction. The problem then is that when you make a language like
Python dynamically typed, the idea of an class or object providing a
contract becomes weakened. When you can't depend on the language to
enforce the contract then other measures will have to be taken in order
to make sure things work. Writing tests is the current trend for solving
this problem. This might very well be a good thing since testing your
code is a good idea. Yet, my theory is that there really is a better
way.

That better way comes through Haskell. While I'm almost positive the
pure functional nature of Haskell is all but a death sentence in terms
of adoption and general usefulness, the thing that Haskell excels at is
its concept of types. In Haskell a type is what you use to determine a
code path. Your function doesn't get called, but instead is considered
for matching against the arguments, which are types. Because of this
reliance you immediately get well written and valuable contracts between
components. The other nice aspect of Haskell's type system is that it is
implicit. While I was able to get up to speed on a C# code base quickly,
it wasn't very fun. Typing boiler plate code all the time is cumbersome.
Yet, it allows the compiler to catch quite a few mistakes. It is this
kind of early check that helps to reduce bugs to real deal logic errors
and not simple issues where the wrong data type was used incorrectly.
While I admire Haskell's type system from a distance I've yet to really
do any large projects with it. My guess is that there is some cumbersome
aspect that I've yet to encounter that might convince me otherwise.

Still, it is clear that dynamic typing and relying on duck typing
becomes difficult when a system gets large. Likewise, relying on tests
can work, but unless you are diligent in the beginning, it is very
difficult getting a large code base to a good place in terms of tests.
In any case it is clear that in terms of concrete solutions, nothing is
a panacea.

Considering that most folks are not able to completely change
platforms, there must be strategies for overcoming the obstacles
associated with languages. Testing is one example that I personally hope
proves to be more valuable than it has been. Another idea is to consider
how to utilize types more effectively. This is somewhat analogous to
effective object oriented code with the major difference being what sort
of goals you are trying for. The Smalltalk idea of object oriented is
based around message passing, although in this case, the idea of types
feels like a better fit even though it is like adding the cruft of Java.
It is clear others have taken similar tracks. Zope interfaces are a good
example of someone handling the contract problem. While they seem
unpythonic, that might very well be a good thing. Being pythonic might
have an upper bound where being enterprisy really does make more sense.
Databases have seen NoSQL destroy normalized data for great wins, so it
wouldn't surprise me that tools to enforce types on a dynamic language
might be extremely beneficial as well in terms of reliability and a
maintainable platform.

At this point I'm pretty much just mumbling, but I do hope it is clear
there is still work to be done. I love Python and all that it makes
possible, but it has become clear that maintaining code with few limits
and a test suite that doesn't necessarily build contracts is difficult
business. Outside of any architectural concepts, one of the things that
makes the whole scenario difficult is not knowing when you're wasting
time. I've recently spent an inordinate amount of time writing and
rewriting tests according some theories about what is really beneficial.
It has been a learning experience, but at what expense? Am I headed in
the right direction or is this a wild goose chase? Hopefully some really
great mentors can come and set me straight or at least make it clear I'm
not alone in these thoughts. While a lot of this is probably just
rambling, at the very least is it rambling for a cause. Programmers
should know that when things are tough and difficult that there are
other people who have asked the same questions and looked for answers.
Likewise, those programmers who managed to successfully emerge from huge
code bases might very well see the flares asking for help and offer some
wise words. One thing is for sure, at least I'm not coding in Java ;)



.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
