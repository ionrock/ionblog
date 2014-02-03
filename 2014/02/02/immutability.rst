Immutability
============

One thing about functional programming languages that is source of
frustration is immutable data structures. In Clojure there are a host
of data structures that allow you change the data in place. This is
possible because the operation is wrapped in a transaction of sorts
that will guarantee it will work or everything will be reverted.

One description that might be helpful is that Clojure uses locks by
default. Any data you store is immutable and therefore locked. You can
always make a copy efficiently and you are provided some tools_ to
unlock the data when necessary.

I'm definitely not used this model by any stretch, but it seems the
transactional paradigm along with efficient copies makes for a good
balance of functional values along side practical requirements.


.. _tools: http://clojure.org/refs


.. author:: default
.. categories:: code
.. tags:: clojure, lisp, python, programming
.. comments::
