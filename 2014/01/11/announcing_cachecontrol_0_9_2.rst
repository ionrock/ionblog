Announcing CacheControl 0.9.2
=============================

I've just released CacheControl 0.9.2! As requests_ now supports
response pickling out of the box, CacheControl won't try to patch the
Response object unless it is necessary.

Also, I've heard that CacheControl is being used successfully in
production! It has helped us replace httplib2 in our core application,
which has pretty decent traffic.

Download the release over at pypi_ and check out the docs_.


.. _requests: http://docs.python-requests.org/en/latest/
.. _docs: http://cachecontrol.readthedocs.org/en/latest/
.. _pypi: https://pypi.python.org/pypi/CacheControl/

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
