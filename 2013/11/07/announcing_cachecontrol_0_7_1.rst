===============================
 Announcing CacheControl 0.7.1
===============================

I've release `CacheControl 0.7.1`_. This release includes patching of
the requests Response object to make it pickleable. This allows you to
easily implement cache stores on anything that can store pickled
text. I've also added a Redis and Filesystem based cache.

The `FileCache` requires lockfile_ be installed and obviously, the
redis cache requires the redis_ module be installed.

I also added docs_!

Please give it a go and file bugs_!


.. _CacheControl 0.7.1: https://pypi.python.org/pypi/CacheControl/
.. _lockfile: https://pypi.python.org/pypi/lockfile
.. _redis: https://pypi.python.org/pypi/redis
.. _docs: http://cachecontrol.readthedocs.org/en/latest/
.. _bugs: https://github.com/ionrock/cachecontrol/issues



.. author:: default
.. categories:: none
.. tags:: none
.. comments::
