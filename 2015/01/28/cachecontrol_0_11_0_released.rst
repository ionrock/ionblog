CacheControl 0.11.0 Released
============================

Last night I released CacheControl 0.11.0. The big change this time
around is using compressed JSON to store the cache response rather
than a pickled dictionary. Using pickle caused some problems if a
cache was going to be read by both Python 3.x and Python 2.x
clients.

Another benefit is that avoiding pickle also avoid exec'ing
potentially dangerous code. It is not unreasonable that someone could
include a header that could cause problems. This hasn't happened yet,
but it wouldn't suprise me if it were feasible.

Finally, the size of the cached object should be a little
smaller. Generally responses are not going to that large, but it
should help if you use storage that keeps a hot keys in
memory. MongoDB comes to mind along with Memcached and, probably,
Redis. If you are avoiding caching large objects it could also be
valuable. For example, a large sparse CSV response might be able to
get compressed quite a bit to make caching it reasonable.

I haven't don any conclusive tests regarding the actual size impact of
compression, so these are just my theories. Take them with a grain of
salt or let me know your experiences.

Huge thanks to `Donald Stuff <https://github.com/dstufft/>`_ for
sending in the compressed JSON patches as well all the folks who have
submitted other suggestions and pull requests.


The Future
----------

I've avoided making any major changes to CacheControl as it has been
reasonably stable and flexible. There are some features that others
have requested that have been too low on my own personal priorites to
take time to implement.

One thing I've been tempted to do is add more storage
implementations. For example, I started working on a SQLite store. My
argument, to myself at least, was that the standard library supports
SQLite, which makes it a reasonable target.

I decided to stop that work as it didn't really seem very
helpful. What did seem enticing was that a cache store becoming
queryable. Unfortunately, since the cache store API only gets a key
and blob for the value, it would require any cache store author to
unpack the blog in order read any values it is interested in.

In the future I'll be adding a hook system to let a cache store author
have access to the `requests.Response` object in order to create extra
arguments for setting the value.

For example, in Redis, `you can set an expires time the DB will use to
expire the response automatically
<https://github.com/ionrock/cachecontrol/issues/15>`_. The cache store
then might have an extra method that looks like this.

.. code-block:: python

  class RedisCache(BaseCache):

      def on_cache_set(self, response):
          kwargs = {}
          if 'expires' not in response.headers:
	      return kwargs

	  return {'expires': response.headers['expires']}

      def set(self, key, value, expires=None):
          # Set the value accordingly

I'm not crazy about this API as it is a little confusing to
communicate that creating a `on_cache_set` hook is really a way to
edit the arguments sent to the `set` method. Maybe calling it a hook
is really the wrong term. Maybe it should be called `prepare` and it
explicitly calls set. If anyone has thoughts, please let me know!

The reasoning is that I'd like to remove the Redis cache and start a
new project for CacheControl stores that includes common cache store
implementations. At the very least, I'd like to find some good
implementations that I can link to from the docs to help folks find a
path from a local file cache to using a real database when the time
comes.

Lastly, there are a couple spec related details that could use some
attention that I'll be looking at in the meantime.


.. author:: default
.. categories:: code
.. tags:: python, http, cachecontrol, requests
.. comments::
