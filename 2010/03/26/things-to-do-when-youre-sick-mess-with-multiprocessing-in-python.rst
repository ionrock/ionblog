=========================================================================
 Things to do When You&#039;re Sick: Mess with Multiprocessing in Python
=========================================================================

This morning I got my wisdom teeth out. It was full on surgery. I had my
first IV and it was the first time to go under anesthesia. I was nervous
at first, but honestly it wasn't a big deal. In some senses, it was kind
of fun to disappear for a minute and be awake with gause in your mouth
the next.

Since I was essentially supposed to be out of commission the rest of
the day, I took a sick day at work. I'm glad I did because from what my
wife says, I should not have been working on production code! That said,
I haven't been able to sleep today so I went ahead and thought about
doing a bit of coding.

In my recent `mini-rant on threading`_, I alluded to creating simpler
constructs for separating processing. I always have in my mind a system
where specific actions can be run in another process or thread. More
specifically, the only difference from this idea and normal threading is
that you utilize the thread or process via a service like interface. It
is just basic message passing, so not rocket science.

A quick glance at the `multiprocessing`_ module in Python revealed
pipes. I had heard about them before, but had never used it. My task
then was to create a simple web application that instead of handling the
request inline, it would send it to a worker process to do it using a
Pipe. So, here is the code:

::

    import cherrypy

    from multiprocessing import Process, Pipe


    class BaseHandler(Process):
        def __init__(self, conn):
            Process.__init__(self)
            self.conn = conn

    class HelloHandler(BaseHandler):
        def run(self):
            msg = self.conn.recv()
            while msg != 'close':
                self.conn.send('hello world from another process')


    class HelloPage(object):
        def __init__(self):
            self.conn, child_conn = Pipe()
            self.hello_processor = HelloHandler(child_conn)
            self.hello_processor.start()

        def index(self, *args, **kw):
            self.conn.send(args)
            return self.conn.recv()
        index.exposed = True


    def run():
        cherrypy.tree.mount(HelloPage(), '/')
        cherrypy.quickstart()


    if __name__ == '__main__':
        run()

Of course immediately after I do this I read in the docs that it is
easy to corrupt the data passing through the pipe if the same endpoint
is being used by more than one thread or process. My conclusion then is
that, while this seems pretty slick, a Pipe is probably better used for
a series of callbacks. This would be analogous to iteration through
recursion where the final step of the function calls itself with the
remaining items. In this case a process might create another child to
return and send the rest of the data to process things that way.

It should be noted that I'm taking pain killers, so this might be a
little off.

What I also found was that a Queue was going to be safe to use with
multiple threads/processes. This makes sense since a queue sort of
includes the idea of single sequence since it can't pop an item off
twice. My next step in this experiment is going to be trying to make a
threadsafe and process safe wrapper around a traditionally
non-thread/process safe store such as bsddb, `buzhug`_ or sqlite. The
queue will let me handle things in an order and I think I'll be able to
push a pipe on the queue in order to return the value to the correct
parent.

I'm also going to reserve the right to delete this post later if I look
back an realize that I was more messed up than I felt!

.. _mini-rant on threading: http://ionrock.org/blog/2010/03/25/Threading_Really_Does_Suck
.. _multiprocessing: http://docs.python.org/library/multiprocessing.html
.. _buzhug: http://buzhug.sourceforge.net/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
