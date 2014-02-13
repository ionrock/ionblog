Queues
======

`Ian Bicking has said goodbye
<http://www.ianbicking.org/blog/2014/02/saying-goodbye-to-python.html>`_. Paste_
and WSGI_ played a huge part of my journey as a Python
programmer. After reading Ian's post, I can definitely relate. Web
frameworks are becoming more and more stripped down as we move to
better JS frameworks like AngularJS_. Databases have become rather
boring as Postgres seems to do practically anything and MongoDB
finally feels slightly stable. Where I think there is still room to
grow is in actual data, which is where queues come in.

Recently I've been dragged into the wild world of Django_. If you plan
on doing anything outside of typical request / response cycle, you
will quickly run into Celery_. Celery defines itself as a distributed
task queue. The way it works is that you run celery workers processes
that use the same code as your application. These workers listen to a
queue (like RabbitMQ for example) for task events that a worker will
execute. There are some other pieces that are provided such as
scheduling, but generally, this is the model.

The powerful abstraction here is the queue. We've recently seen the
acceptance of async models in programming. On the database front,
eventual consistency has become more and more accepted as fact for big
data systems. Browsers have adopted data storage models to help
protect user data while that consistency gets replicated to a central
system. Mobile devices with flaky connectivity provide the obvious use
case for storing data temporarily on the client. All these
technologies present a queue-like architecture where data is sent
through a series of queues where workers are waiting to act on the
data.

The model is similar to functional programming. In a functional
programming language you use functions to describe a set of operations
that will happen on a specific type or set of data. Here is simple
example in Clojure ::

  (defn handle-event [evt]
    (add-to-index (map split-by-id (parse (:data evt)))))

Here we are handling some `evt` data structure that has a `data`
key. The `data` might be a string that gets parsed by the `parse`
function. The result of the parsing is passed to a `map` operation
that also returns an iterable that is consumed by the `add-to-index`
function.

Now, say we wanted to implement something similar using queues in
Python. ::

  def parse(data, output):
      # some parsing...
      for part in parts:
          output.push(split_by_id(part))


  def add_to_index(input):
      while True:
          doc = input.get()
          db.write(doc)


  def POST(doc):
      id = gen_id()
      indexing_queue.push((id, doc))
      return {'message': 'added to index queue',
              'redirect': '/indexed/%s' % id}


Even though this is a bit more verbose, it presents a similar model as
the functional paradigm. Each step happens on a immutable value. Once
the function receives the value from the queue, it doesn't have to be
concerned with it changing as it does its operation. What's more, the
processing can be on the same machine or across a cluster of
machines, mitigating the effect of the GIL.

This isn't a new idea. It is very similar to the actor model and other
concurrency paradigms. Async programming effectively does the same
thing in that the main loop is waiting for I/O, at which time it sends
the I/O to the respective listener. In theory, a celery worker could
queue up a task on another celery queue in order to get a similar
effect.

What is interesting is that we don't currently have a good way to do
this sort of programming. There is a lot of infrastructure and tooling
that would be helpful. There are questions as to how to deploy new
nodes, keep code up to date and what happens when the queue gets
backed up? Also, what happens when Python isn't fast enough? How do
you utilize a faster system? How do you do backfills of the data? Can
you just re-queue old data?

I obviously don't have all the answers, but I believe the model could
work to make processing streamable data more powerful. What makes the
queue model possible is an API and document format for using the
queue. If all users of the queue understood the content on the queue,
then it is possible for any system that connect to the queue to
participate in the application.

Again, I'm sure others have built systems like this, but as there is
no framework available for python, I suspect it is not a popular
paradigm. One example of the pattern (sans a typical queue) is
Mongrel2_ with its use of ZeroMQ_. Unfortunately, with the web
providing things like streaming responses and the like, I don't
believe this model is very helpful for a generic web server.

Where I believe it could excel is when you have a lot of data coming
that requires flexible analysis by many different systems, such that a
single data store cannot provide the flexibility required. For
example, if you wanted to process all facebook likes based on the
URLs, users and times, it would require a rather robust database that
could effectively query each facet and establish a reasonably fast
means of calculating results. Often this is not possible. Using queues
and a streaming model, you could listen to each like as it happens and
have different workers process the data and create their own data
sources customized for the specific queries.

I still enjoy writing python and at this point I feel I know the
language reasonably well. At the same time I can relate to the feeling
that it isn't as exciting as it used to be. While JavaScript could be
a lot of fun, I think there is still something to be done with big
data that makes sense for Python. Furthermore, I'd hope the queue
model I mentioned above could help leave room to integrate more
languages and systems such that if another platform does make sense,
it is trivial to switch where needed.

Have other written similar systems? Are there problems that I'm
missing?


.. _WSGI: http://wsgi.readthedocs.org/
.. _Paste: http://pythonpaste.org/
.. _AngularJS: http://angularjs.org/
.. _Celery: http://www.celeryproject.org/
.. _Django: https://www.djangoproject.com/
.. _Mongre2: http://mongrel2.org/
.. _ZeroMQ: http://zeromq.org/


.. author:: default
.. categories:: code
.. tags:: python, clojure, programming, cloud
.. comments::
