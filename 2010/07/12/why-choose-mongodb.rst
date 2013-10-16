====================
 Why Choose MongoDB
====================

A co-worker will occasionally send along recent `blog posts`_ that place
into question our decision to use `MongoDB`_. These are small reminders
that technical decisions are never black and white and that no matter
how careful you are, there are going to be trade offs. Usually the
complaints I hear about MongoDB have to do with durability.

Specifically, people have a problem with `10gen`_ (the folks who make
MongoDB) `suggesting`_ that you run at least two MongoDB instances to
provide some level of reliability in the face of one system going down.
The fact is we have been bitten by a bug that required a good deal of
downtime. This kind of thing totally stinks. I'd say it is unacceptable,
but the reality is that at some point you have to trust that a system
will do its job. In other words, it is not enough to prevent problems,
you must also have a means of recovering from problems. In our case,
that recovery plan was the problem. Shame on us.

This has since been remedied and there is probably more to do. I'm sure
other organizations might have considered the hiccup a worthy reason to
abandon MongoDB for another more durable system. The problem is that
while MongoDB's durability did prove to be a major problem, that isn't
the whole story. There are other reasons to choose MongoDB, but
durability is not one of them.

In our situation, the biggest benefit we get from MongoDB is the
ability to query. This seems like such a basic tenant of databases that
you'd be hard pressed to find someone who didn't believe running queries
on your data isn't the killer feature of a database. With that in mind,
I'd point out that many NoSQL systems do not provide the same level of
support for queries. `CouchDB`_ (which I'm personally a fan of) is in
fact really bad at ad-hoc queries. Once you save a view in CouchDB,
you're in pretty good shape, but randomly querying the DB is considered
bad form. Likewise, generating a new view on a massive dataset is time
consuming as well. That is the trade off CouchDB made. In return you get
excellent durability, a fantastic HTTP based interface and the ability
to utilize pure JSON as a document format. Totally reasonable trade offs
if you ask me. The only problem is, the ability to query the dataset in
real time is an order of magnitude more important to us than the other
features. We can run a slave (for reads even), deal with BSON, and use
the socket based Python driver that MongoDB provides, yet if we couldn't
do realtime queries in a reasonable about of time, then what is the
point?
By the way, I don't mean to pick on CouchDB or any other system. The
fact of the matter the discussion is not over what system to use as much
as weighting what features are important. For us, the ability to query
very quickly and under load trumps the other features such as single
machine durability. We've paid the price of that trade off once, so
we're aiming not to do so again. Thanks to my cautious and objective
thinking co-worker, we also consistently consider other data stores.

That said, I think we made a good choice to go with MongoDB. It is not
perfect, but nothing is. MongoDB has been meeting needs very
successfully and I have no problem recommending it.


.. _blog posts: http://www.mikealrogers.com/2010/07/mongodb-performance-durability/
.. _MongoDB: http://mongodb.org
.. _10gen: http://www.10gen.com/
.. _suggesting: http://blog.mongodb.org/post/381927266/what-about-durability
.. _CouchDB: http://couchdb.org


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
