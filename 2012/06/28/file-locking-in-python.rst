File Locking in Python
######################

I've been working with a super simple threadsafe file based caching
mechanism. The `httplib2`_ library has a nice and simple file based
cache, but it is not threadsafe. I tried to create a version that uses a
single writer thread to write to the cache files, but that ended up
being rather complex. I then started trying to write my open simple lock
file rather than use the `fcntl`_ module. This also fell over in tests.

I started considering the fcntl module when I found out there is
`os.open`_ which seems to support the same flags.

I have tests passing and some really simple code that seems to work,
but I suspect I'm missing something. Jason wrote `yg.lockfile`_ which
uses `zc.lockfile`_. The difference being that zc.lockfile does the
dirty work of finding the lock file mechanism supported by the system
(ie fcntl or msvcrt). It also uses a separate lock file where the
locking flags get set. There is also `this lock file implementation`_
mentioned on `Stack Overflow`_. It shouldn't be surprising there is
another `file locking library`_ that might have some useful tips within
its design.

I'm not going to suggest that I have the answers for perfect file
locking. That said, after looking through the different examples, there
are a few basic use cases you need to be aware of.

#. Lock a lock file, not the file you want to work with
#. Use something to identify the process the originally locked the lock
   file
#. Locking is platform specific, so consider your use case

The first two notes deal specifically with state getting corrupted. You
need to be sure if you are locking files that you handle the case where
the process exits unexpectedly. If this happens and your lock is still
around, what do you do to take back that lock? Using a separate file
with the pid in the contents is a good way to do that without locking
the actual file you are working with.

The last point regarding the platform independence is primarily because
if you don't need to deal with a specific platform, then don't. Most of
the time you are locking a file, it is because you are dealing with a
concurrency condition. Adding more code that does a bunch of platform
checks simply can't be helpful in making the file locking check as
atomic as possible. It may not be detrimental, but you might as well
master one platform vs. handle anything available and save yourself the
trouble of understanding the low level filesystem flags. There are a lot
of articles out there on using fcntl, all of which saying that it can be
tricky. Avoid the headache of also learning the Windows specific bits if
you don't have to.

It is frustrating that this has been this difficult. I honestly
expected there to be a file locking library or function in the standard
library. That said, it is definitely possible that I'm simply missing
how different the use cases are. It might be best that people take
different strategies as a common locking mechanism similar to the basic
description above would not be beneficial to most. I also wouldn't be
surprised if this is a pretty consistent pain point when the issue comes
up as it almost never sits amidst simple single threaded/process code.

.. _httplib2: http://code.google.com/p/httplib2/
.. _fcntl: http://docs.python.org/library/fcntl.html
.. _os.open: http://docs.python.org/library/os.html#os.open
.. _yg.lockfile: https://bitbucket.org/jaraco/yg.lockfile/
.. _zc.lockfile: http://svn.zope.org/zc.lockfile/trunk/src/zc/lockfile/__init__.py?rev=121133&view=markup
.. _this lock file implementation: http://www.evanfosmark.com/2009/01/cross-platform-file-locking-support-in-python/
.. _Stack Overflow: http://stackoverflow.com/questions/489861/locking-a-file-in-python
.. _file locking library: http://packages.python.org/lockfile/lockfile.html


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
