Safety First
############

It should be a design goal in software to make the systems safe. This is
different from security because instead of preventing unrequested
access, you are preventing accidental access. You keep a gun in a safe
so no one else shoots it, but you keep the safety on so you don't shoot
someone else.

The key to designing a safe system is in the data. Specifically, the
data should be immutable whenever possible. The reason being is that you
fire off a script that ends up writing the same document over and over
again, you keep your damage small. This can be partially a data design
detail, but it is also related to how the application actually works.

The canonical example of this is the decision to actually delete data.

When you first look at something like a blog and you remove some blog
post, you write some handler that deletes it from the database. Problem
solved. But at some point you recognize you just deleted something you
needed. Whoops. Instead actually deleting things from the database, you
decide to just mark the the "thing" as deleted and update your code to
check for the deleted flag. This is a great example of writing safety
into your software.

A friend at work forwarded this article on `beating the CAP theorem`_
that I think also speaks to the benefit of safe software. Immutability
and idempotency are two great features to have for certain operations
that can go a long ways making your software safer. The result is fewer
trips to your keyboard in the middle of the night looking through
backups to find the data you just screwed up royally.

.. _beating the CAP theorem: http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html


.. author:: default
.. categories:: code
.. tags:: javascript, mongodb, programming, python
.. comments::
