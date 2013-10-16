===================
 A RESTful Gettext
===================

At work I've been thinking a lot about how we work with different
languages. One area that has been something of a pain has been
translations. There is a disconnect between what phrases are live and
those that live in the source. It seems like a better system would be a
lazy one that creates and updates translation catalogs as the different
phrases are used. For example, when a translated string comes from a
database or variable.


My idea is to create a really simple service to act as a lazy gettext.
In terms of features, the basic idea is that if the string hasn't been
translated, you get a 404. Otherwise, you get the translated string. The
URLs are really simple. The language catalog and English percent encoded
phrase identifies the resource (/es/very%20well). Any special context
can be added via query string arguments that allow similar phrases to be
translated differently.


I've started working on a simple implementation using MongoDB that I'm
calling Dragoman, which is a synonym for translator. There will also be
a HTML interface for adding translated phrases. As new phrases show up
missing (404s), they will be made available to translators to translate.
The idea is to move the application translation out of the source and
into the hands of those users that create the actual content.


**Update**

I wrapped up some basic functionality/tests and added it to my
`BitBucket account`_. It uses a library called Fab which is our internal
web framework built on CherryPy. I'm working getting the necessary
aspects available (a nice threadsafe connection pool), so others can use
that aspect easily. It also uses `Eggmonster`_.


.. _BitBucket account: http://bitbucket.org/elarson/dragoman/
.. _Eggmonster: http://bitbucket.org/yougov/eggmonster


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
