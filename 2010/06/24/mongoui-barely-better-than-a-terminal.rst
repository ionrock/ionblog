=========================================
 MongoUI - Barely Better Than a Terminal
=========================================

At `work`_ we use `MongoDB`_ for storing most of our critical data. We
started with customized key value store we called Faststore. It was
built in Python and used BsdDB. It was a pretty successful system in
that it was reliable and performed very well. The thing that killed
Faststore was that there wasn't a good way to replicate the data. We
tried considering a different key/value database in the core such as
Tokyo Cabinet, but it quickly became clear the speed wasn't there for
our critical operations. After some research, we settled on MongoDB for
our storage needs. So, far the decision has been a rather successful
one. We did hit a rather nasty bug that required some significant
downtime, but beyond that, MongoDB has been excellent. This is
especially true when you consider the amount of data.

As we've used MongoDB one theme that I've hit is that is can be a
little hard to view the data. Things like CSVs and tables in terminals
can be a little easier to read than a pretty printed dictionary. In
order to help making the perusing of data a little bit easier when
developing with MongoDB, I made a little tool called `MongoUI`_. MongoUI
is **really** simple. It is only a little better than a terminal. That
said, it makes basic browsing a little easier.

Pretty much all you have to do to use it is download it (hg clone
http://bitbucket.org/elarson/mongoui), install it (cd mongoui && python
setup install) and then run it (mongoui). Once it is running, point your
browser to `localhost, port 9000`_ and you'll see a simple list of your
databases. Clicking on a DB will show you the collections and clicking
on the collections gives you a couple fields to query. The first field
is for excluding/including fields. The second is for providing
parameters ({'foo': 'bar'}). You can include a count by clicking the
count checkbox and change the include to an exclude by clicking the
exclude checkbox.

The output is still pretty much just a pretty printed dictionary, but
the browser is a slightly easier place to scroll up and down than a
terminal. There is no writing or editing of documents, and I seriously
doubt I'd add that anytime soon. It also is not meant for huge
databases. For example, if you have 20k collections in a DB, it will
show a really big list. Same goes for large collections. I'm not paging
or anything like that. It really is meant make basic queries on local
tests databases a little bit easier.

If it seems helpful I'll try to develop the viewing of the data bit
more as well as possibly including some editing bits. That said, it is
no where on my todo list. The other thing I'd like to try and
incorporate is a good RESTful API. My biggest complaint about MongoDB is
that the protocol to the DB is not via HTTP. It was a basic design
decision, but it would be nice at times to have a basic HTTP enabled
caching proxy in front of a MongoDB for things like saving queries as
views. Likewise things like replication and load balancing might also be
interesting uses. That said, I don't really have a need for it at work,
so I don't know that I would get very far.

Feedback is always welcome!

.. _work: http://yougov.com
.. _MongoDB: http://mongodb.com
.. _MongoUI: http://bitbucket.org/elarson/mongoui
.. _localhost, port 9000: http://localhost:9000


.. author:: default
.. categories:: code
.. tags:: mongodb, programming
.. comments::
