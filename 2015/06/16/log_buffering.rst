Log Buffering
=============

Have you ever had code that needed to do some logging, but your
logging configuration hadn't been loaded? While it is a best practice
to set up logging as early as possible, logging is still code that
needs to be executed. The Python runtime will still do some setup (ie
import everything) that **MUST** come before **ANY** code is executed,
including your logging code.

One solution would be to jump through some hoops to make that code
evaluated more lazily. For example, say you wanted to apply a
decorator from some other package if it is installed. The first time
the function is called, you could apply the decorator. This would get
pretty complex pretty quickly.

.. code-block:: python

   class LazyDecorator(object):
       def __init__(self, entry_point):
           self.entry_point = entry_point
	   self.func = None

       def find_decorator(self):
           # find our decorator...

       def __call__(self, f):
           self.original_func = f
	   def lazy_wrapper(*args, **kw):
	       if not self.func:
	           self.func = self.find_decorator()
	       return self.func(*args, **kw)
	   return lazy_wrapper

I haven't tried the code above, but it does rub me the wrong way. The
reason being is that we're jumping through hoops just to do some
logging. Function calls are expensive in Python, which means if you
decorated a ton of functions, the result could end up as a lot of
overhead for a feature that only effects start up.

Instead, we can just buffer the log output until after we've loaded
our logging config.

.. code-block:: python

   import logging


   class LazyLogger(object):

       LVLS = dict(
           debug=logging.DEBUG,
           info=logging.INFO,
           warning=logging.WARNING,
           error=logging.ERROR,
           critical=logging.CRITICAL,
           exception=logging.ERROR,
       )

       def __init__(self):
           self.messages = []

       def replay(self, logger=None):
           logger = logging.getLogger(__name__)
           for level, msg, args, kw in self.messages:
               logger.log(level, msg, *args, **kw)

       __call__ = replay

       def capture(self, lvl, msg, *args, **kw):
           self.messages.append((lvl, msg, args, kw))

       def __getattr__(self, name):
           if name in self.LVLS:
               return functools.partial(self.capture, self.LVLS[name])


We can use this as our logging object in our code that needs to log
before logging has been configured. Then, when we can replay our log
when it is appropriate by importing the logger, and calling the
`replay` method. We could even keep a registry of lazy loggers and
call them all after configuring logging.

The benefit of this tactic is that you avoid adding runtime
complexity, while supporting the same logging patterns at startup /
import time.


.. author:: default
.. categories:: code
.. tags:: python, logging, openstack
.. comments::
