A Rambling Multiprocessing Story
################################

At work I had a really clear example of a distributable problem. Pretty
much just queueing up some tasks and having workers process the queues.
I ran some benchmarks to see what the most effective worker was, threads
or processes. The result was that processes were the fastest in my case.
There were a couple important details that make it clear why. The first
is that the "task" is really just a dict that can be small or large. The
dict comes from MongoDB and is a MongoDB document. My initial design was
to put the entire document on the queue, but it became apparent that it
was much more efficient to just pass around the document object ids and
let each worker fetch the data. This is obvious in hindsight, but at the
time I was avoiding prematurely optimizing things and potentially making
things more complicated. Along similar lines, I found in testing that if
workers always connected, did some work and closed the connections for
each operation, it also caused some problems. These discoveries created
a couple requirements and opportunities.

-  Workers must reuse their connections across jobs
-  The smaller the job payload the faster we can go
-  A cursor from MongoDB can get all the object ids easily, but not
   entire documents

The process of starting a job then began with a thread that does the
initial query from MongoDB. This happens in a thread because the job is
kicked off from a request to a CherryPy application. The application
starts a thread to do the work and then is able to return a response to
the client immediately. The thread then queues up the results and starts
a set of worker processes. The worker processes then get items off the
queue and do the work, preserving the connection to MongoDB.

Also, in addition to the web application being able to start jobs, it
also monitors the rate at which the jobs are being processed. The idea
here is that if we see the application putting too much strain on the
database, we can ease things up.

This whole application went through a few iterations before settling on
the above design. I started with simple threads and found that it was
trivial to max out a processor. When I switched from threading to
processes I saw an increase in performance as well as all the processors
being utilized. The difficulty in switching to processes was that it was
not as simple passing objects around. This goes beyond the obvious
serialization difficulties passing objects between processes.

When I first started switching to processes I had not yet made the
decision to use the object ID and make the workers fetch the data. The
result was that I had jumped through a lot of hoops. For one, I couldn't
queue all the documents before starting the workers. This resulted in
trying to do a batch operation, while still keeping the workers
available. I would do a batch, wait for the workers to finish, find more
documents and repeat. The problem was that the workers then couldn't
effectively tell whether or not the queue was actually finished or just
empty while more cases were being readied. Looking back, it would have
been better to go ahead an let the process finish and start a new set of
workers. My experience with connections failing silently pushed me to
avoid stopping and restarting the workers.

When I took this model and tried to apply it to processes, my first
inclination was to use Pipes. I made a very simple protocol where a
worker would listen for a case and process it. This worked but it was
cumbersome to test because I couldn't easily make my workers join. When
you are testing, you add an item to the queue and let the worker process
it but how do you tell when you can check everything worked? If the
worker is broken, then it doesn't migrate the case and you've become
deadlocked. That doesn't make for a very good test because a failure
doesn't happen within the test runner, it just blocks forever.

I then began to use a queue like I had with the threads. It shouldn't
be surprising then that I ran into the same problems. With that in mind
I took a minute to start investigating what really was the best
methodology, outside the scope of the application. I tested different
models using threads, processes, queues, pipes and data. Eventually I
came to my conclusion regarding queueing the object id and letting the
worker fetch the data. My original concern that it would strain the
database was incorrect. Again, hindsight is 20/20 here.

With the better queueing strategy in place, it was trivial to test
whether it was faster to use processes or threads and see if there was
an optimum number of each. With my model in place I refactored the code
to reflect my findings and got all my tests passing.

The next step was to introduce the reporting aspects for the web
interface.

As an aside, when working on the web interface I took some time to
investigate `Backbone.js`_ (which requires \ `Underscore.js`_) and
`Head.js`_. I had heard about these libraries for a while, but hadn't
had an opportunity to see what sort of help they are. It is honestly
very exciting to see things like Backbone.js because it begins to make
it much more obvious how to organize Javascript code. Likewise, tools
like Head.js make it possible to create a more effective system of
including those files in a way that is efficient in both the browser and
for development.

Back to reporting.

Again, the way the system works is that the `CherryPy`_ application
receives the request, it processes the request and asks a manager `bus`_
to perform and operation. The bus then checks to see if it already has
done the action (there is an idea of a "team" which is a set of threads
and processes responsible for doing a "job") and tells the team to get
to work. The team then creates a thread to actually do the work. The
thread begins by creating a result tracker thread. This thread will
listen to queues the workers write to in order to provide some stats.
Next it finds the documents that need to be migrated or copies and adds
them to the queue. The worker processes are then started. Each worker
has its own result queue that it writes to that the result tracker
thread will read from. After the worker processes are started, the
thread started by the team closes the queue, signaling to the worker
processes that when the queue is empty, all the work has finished. The
queue is then joined and the report tracker thread stopped.

Something that was important was where a queue was created. Originally
I tried to create the result queue and pass it to the workers, but that
didn't work. I suspect that the queue can only have a single writer.
Similarly, I had to create the work queue in the thread that creates the
worker processes. Again, I believe this is an implementation issue in
the multiprocessing library. My understanding is the multiprocessing
library has to create a pipe for each queue and it starts its own thread
to actually handle sending things via the pipe. The impact of this is
that even though you would suspect you could pass that queue object
around, it fails when it crosses the boundary of a thread.

There were some things I didn't try that might be helpful in the
future. I avoided using an external queueing system. Part of the goal of
this project is to lower the system administration resources. Adding
something like RabbitMQ or Redis doesn't really help our sysadmins keep
track of fewer processes. Another thing I didn't really investigate as
fully was using the logging module for getting statistics. Instead I
used the `logging.statistics protocol`_, which meant that I needed to
collect the results in the main process, hence the reason for the result
tracker thread. I considered just using a log file, but decided against
it. Logging every result in a set of files would most likely end up with
a negative impact because of the file I/O via actually writing to the
disk or even simply taking up space.

With that in mind, I did add some tooling for working with logs for
future improvements. It could be a very useful feature to journal the
operations for either a replay or for importing into another system.
Again, this would need to be something the sysadmins would want to do
since it is taking compressed binary data from MongoDB and writing it in
uncompressed JSON files. That could be quite a lot of data for a large
database.

I'm hoping that when we see where this tool really fits we can
eventually open source it. I think its strength lies in being able to
move MongoDB data in a way that is tunable such that you
can inadvertently queue things. What I mean is that when you have a
system, incorporating a queue can introduce complexity. This idea lets
you avoid the explicit queue and instead consider something more akin to
smarter replication. Time will tell how valuable this is, but at the
very least I learned quite a bit and I think the result is a tool that
does one thing well.

.. _Backbone.js: http://documentcloud.github.com/backbone/
.. _Underscore.js: http://documentcloud.github.com/underscore/
.. _Head.js: http://headjs.com/
.. _CherryPy: http://cherrypy.org
.. _bus: http://www.aminus.org/blogs/index.php/2007/06/24/web_site_process_bus?blog=2
.. _logging.statistics protocol: http://www.aminus.org/blogs/index.php/2010/11/19/logging-statistics?blog=2


.. author:: default
.. categories:: code
.. tags:: javascript, mongodb, programming, python, testing
.. comments::
