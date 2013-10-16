================
 MongoDB Schema
================

Unfortunately, I can't remember where I read it, but there was a blog
post that mentioned the importance of schema in a schemaless database.
It hit me as somewhat close minded at the time. After all, they don't
call them "schemaless" for nothing. Slowly there has been a change in
how I view the issue.

Contracts have been a theme recently in my programming life. Tests
essentially create contracts. The environment you run in can be rather
limited and yet more robust thanks to contracts with the underlying
system. Contracts are what let you sleep at night because without some
guarantees you'd never get anything done. The key with contracts is that
they happen at the right time and place. Abstraction (and much of OO)
basically is a way to take some level of complexity and hide it behind a
contract. Before when you had to clean up a file name, verify it wasn't
written to the data store and replicate it to three other systems. Now,
you call the "save" method and forget about the details. The benefit
most people site is flexibility, but the reality is that the contract
behind the "save" method lets you abstract the more complicated process
down to one thing, letting you free of some mental space for new
problems.

The idea then behind a schema for something like MongoDB is that you
get to stop thinking in terms of JSON or Python dictionaries and begin
to use real objects. The reason is the same as the save method example
above. We need a contract. A schemaless database is advantageous because
it moves the verification and contracts for the data to the application
level where it belongs. The RDBMS can help by saying something is a
string or int, but past that you're working with really basic types.

You're going to need some larger concepts to keep everything in place.
ORMs are one example. In the case of MongoDB, you still need a schema
because you need the contract. The only difference is that there is a
slightly more automatic translation between a strings, ints, lists, and
dicts along side the fact MongoDB doesn't require setting everything up
front.

It is always interesting to find how some buzzword or concept really
ends up being a slightly different perspective on system design. Most
people (myself included) hear "schemaless" and think, "I can ditch my
ORM! Declare nothing! Everything is just a dict!". The reality is that
in the case of MongoDB you have a database that can understand JSON.

That is pretty much it. There are interesting outcomes to that reality,
but no where does it say you never have to verify your data. That is
what a schema does.



.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
