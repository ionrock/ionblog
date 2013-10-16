=============================
 Disliking the GIL in Python
=============================

One theme that I took away from `PyCon`_ this year was how truly bad the
GIL is. For those that don't know, the GIL is the Global Interpreter
Lock. When you are programming and you want to do two things at the same
time, you usually use something like a thread. Threads can access
resources, so often times it is important to lock them while you use
them. This prevents the situation where things get overwritten or
corrupted due to two different threads accessing the same resources.

When you have one processor the result is that while things are
presumably threaded, the operating system is actually just acting as
though it can do two things at one time. So, in Python, when you are
using threads on a one processor or single core machine, your threads
are effectively just as good as any other language that uses the
operating system's threads. The problem is that when you move to more
than one core, the operating system allows you to use more than one
core, while Python's GIL continues to mimic parallel operations.

The reality is that most of time it really doesn't matter. I've avoided
using threads in my design for the majority of my programing career and
my findings are that it was a good idea to do so. But, now that machines
are getting more cores, avoiding parallel operations is in fact more
limiting.

Again, most people won't need it. Python is pretty quick and there are
instances where Python's threads really can help. The problem is not
where we are now, but where we want to be in the future. There was
definitely an asynchronous theme at PyCon as well that effectively
addresses some of the problems with threads, but it considers it in
terms of connections. When programs communicate there is a limit to how
many connections can be made. Threads are one option where each thread
is a connection, but threads have a cost in terms of memory and
operating system resources that make using 10k (for example) threads
impossible. The async model instead changes the concepts around, so
instead of having a thread constantly listening, you utilize the
operating system to notify you of events. This means having 10k
connections is trivial because each connection is truly efficient in
that it won't do any work without being notified.

While async helps with the aspect of connections, it doesn't help at
all in terms of utilization of the hardware. The current option then is
to simply use more than one process and make sure your state is not held
within your applications. This is a good practice generally with both
threads and async. Unfortunately, not all applications are focused on
connections like web applications are.

The whole issue that I personally have with the GIL is not so much the
actual implications but rather that we need new models and that even if
we get them, without the GIL issues fixed, they won't help as much as
they could. The async model is pretty tough. The libraries don't usually
work with it because they can block the main loop. This makes them
rather impractical then. Threading is becoming pretty well understood
but it is still difficult because threading implies a shared state that
is a bad idea. There are still some required changes in how we program
that are needed to make threading more scalable from a programmer
perspective. The design patterns are coming along, but again, with the
GIL, it just doesn't make that much sense when you're talking about
something like a 16 core machine.

Even though I personally don't have a specific use case that is a
problem today, it shouldn't really matter. Python is a great language
with a ton of "batteries" included along with a battery store close by.
If we can't figure out a way to make the GIL go away or work across
cores, then we really limit the gains we can get from the history in the
Python community. It limits rather deeply where Python can be used.

One solution I see is taking something like the multiprocessing module
and use that as the basis for implementing higher level concurrency
models. This already works pretty well on Linux but there are some
definite corner cases that cause problems. That said, it seems
reasonable that a higher level library could restrict the use to a
certain model in such a way that the corners cases are never hit.


.. _PyCon: http://us.pycon.org


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
