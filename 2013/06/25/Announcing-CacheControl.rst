=========================
 Announcing CacheControl
=========================



A while back I took the time to make the httplib2_ caching libraries
available in requests_. I called the project HTTPCache_.

Recently, there were some changes to requests that Ian_ submitted some
patches for. I also found out there was `another httpcache`_ project! It
made sense to take a minute a revisit the project to see if there were
some improvements. Specifically, I wanted to see if there was a better
way to integrate with requests and httpcache had provided a great
example.

With that said, I introduce to you CacheControl_! There are few
important differences that I wanted to point out.


The httplib2 Cache Logic as a Library
=====================================

You can import a class that will accept a minimum set of requirements
to handle caching. Here is a quick example of how to use it. ::


  import requests

  from cachecontrol import CacheController

  controller = CacheController()

  resp = requests.get('http://ionrock.org')

  # See if a request has been cached
  controller.cached_request(resp.request.url, resp.request.headers)

  # cache our response
  controller.cache_response(resp)

This still assumes a requests response for caching, which I might end
up refactoring out, but for now it seems like a reasonable API. For an
in-depth example of how it is use in CacheControl's actual adapter,
take a look `at the code`_.


Use the Requests Transport Adapter
==================================

Thanks to Lakasa_ for telling me about `Transport Adapters`_. Requests
implements much of its functionality via the default HTTPAdapter,
which means you can subclass it in order to make more customized
clients.

For example, if you had a service at `http://api.ionrock.org` that you
wanted to create a custom client for, you could do something like
this: ::

  from requests import Session
  from ionrock.client import IonAdapter

  sess = Session()
  sess.mount('http://api.ionrock.org', IonAdapter())

The adapter then can do things like peek at the request prior to
sending it, as well as take a look at the response. This is really
handy if you needed to do things like include application specific
headers or implement something that non-trivial in a general HTTP
client such as Etags.

In the case of CacheControl, it allows the ability to change what is
cached before the response is constructed. The nice thing about this
flexibility is that you could considering storing a more optimal
version of the response information. While CacheControl doesn't do
anything special, now we can if the default behavior is too slow or
the cache store requires a specific format.


Project Changes
===============

I actually released an package_ for CacheControl and plan on
keeping it up to date. In addition to a new package, I've moved
development to github, most importantly, because I've moved most of my
packages to git.

The test suite has also been revamped to use webtest_ rather than the
custom CherryPy_ test server I used. You can run the tests and get up
and running for development by using the pavement.py and paver_.

Take a look at the PyPI page or the README_ for help on how to use
CacheControl. At this point I believe it is reasonably stable. My next
steps are to provide better documentation and work on making sure the
cache implementation has a reasonable performance when compared to a
similar threadsafe cache I've used with httplib2.

Please let me know of any comments / questions!


.. _Lakasa: https://github.com/Lukasa/
.. _Ian: https://github.com/sigmavirus24/
.. _README: https://github.com/ionrock/cachecontrol/blob/master/README.rst
.. _CherryPy: http://cherrypy.org
.. _paver: http://paver.github.io/paver/
.. _webtest: http://webtest.pythonpaste.org/en/latest/
.. _Transport Adapters: http://docs.python-requests.org/en/latest/user/advanced/#transport-adapters
.. _CacheControl: https://github.com/ionrock/cachecontrol
.. _HTTPCache: https://bitbucket.org/elarson/httpcache/
.. _another httpcache: https://github.com/Lukasa/httpcache
.. _httplib2: http://code.google.com/p/httplib2/
.. _requests: http://docs.python-requests.org/
.. _at the code: https://github.com/ionrock/cachecontrol/blob/master/cachecontrol/adapter.py
.. _package: https://pypi.python.org/pypi/CacheControl/0.6


.. author:: default
.. categories:: code
.. tags:: python
.. comments::
