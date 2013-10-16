===========================
 Making Code More Testable
===========================

Lately I've been really making efforts to become a better tester. I've
heard that tests make code better just about as much as I've heard that
there isn't really a difference. After working on a large code base for
a while, my conclusion is that tests do help isolate code, which is a
definite positive for maintainability.

The issue though is a catch 22 when you have a code base that managed
to get a little out of control. This tendency is entirely normal of
course. If you can stop a user from hurting with a few lines of code
then that is a big win. Users are important and in the end then code is
not.

That said, at some point there becomes the requirement to start really
nailing down corner cases. This is where bugs occur in really sneaky
parts of the code that you may never have considered or because of slow
changes in use cases. It challenges you to reconsider seemingly stable
code, in which case your tests are really the only way to have some
confidence things are working correctly. If you originally wrote the
code you probably feel more assured things can work, but when the code
is foreign, you need the tests to verify in real terms what is
happening.

The question then is how the heck to tear apart the old code to improve
the testability? To be perfectly frank, I have no idea. Part of the
problem is simply finding an easy to way to iterate on the problem. It
is easy to bite off more than you can chew, so there needs to be ways to
roll things back. Likewise, it is also difficult to know your making
improvements since you don't have tests there to reassure yourself
things didn't get way worse in some unknown manner.

There is obviously not a single answer to this, but I would like to
find some resources that define some techniques or at the very least
ideas. For example, DVCS does help because in theory breaking off a
"cleanup" branch is trivial. Unfortunately, that is only the beginning
since you also have to consider any sort of environment that needs to be
setup.

No matter what techniques are out there it can't hurt to dive in. If
you fail, remove the branch and try again. Eventually you'll hit on
something. There have been many times where I started learning some
language or library only to become extremely frustrated. Eventually when
I revisit it, things are clearer and it all makes sense. This is the
same kind of thing, so step one is just doing it even if you fail.



.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
