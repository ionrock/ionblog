Announcing (the poorly named) HTTPCache
#######################################

I've been a fan of `httplib2`_ for a long time. It does caching right
and has support for authentication via HTTP Basic and Digest. The
problem with httplib2 is that it is not threadsafe. There are some data
structures used within the code that make unsafe for reuse with threads.
One thing to do to improve this situation is to use a different caching
mechanism, but it still means that you need a thread specific instance
in order to avoid issues using it with threads.
The new hotness in HTTP client libs is `requests`_. The API is
reminiscent of httplib2 and has support for many of the same
authentication schemes. More importantly though, it is threadsafe and
even provides a session construct that helps to make using requests
similar to using any other data resource connection. These are all great
features, but the one thing it lacks is HTTP caching support.
Enter `HTTPCache`_.
HTTPCache is a really simple wrapper that ports httplib2's caching for
use with requests. Here is a simple example: ::

  import requests    
  from httpcache import CacheControl    
   
  sess = CacheControl(requests.session())  
  resp = sess.get('http://mywebresource.com/some/cached/resource')

There is still some work to do, but if you were interested in the
caching of httplib2 with everything else in requests, take a look.

.. _httplib2: http://code.google.com/p/httplib2/
.. _requests: http://docs.python-requests.org/
.. _HTTPCache: https://bitbucket.org/elarson/httpcache/overview


.. author:: default
.. categories:: code
.. tags:: programming, python, Uncategorized
.. comments::
