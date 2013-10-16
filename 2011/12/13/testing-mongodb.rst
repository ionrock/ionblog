Testing MongoDB
###############

We've been noticing some issues with our data in MongoDB. Seeing as
others have had less than stellar experiences, it seemed like we should
make sure that MongoDB wasn't the one causing problems.

My main goal is to see if incrementing updates by a large set of clients
can cause data to be corrupted. I'm defining corruption as anything that
diverges from the original document. Specifically, we're looking for
some keys that should have an answer but don't. My theory is that under
some conditions it's possible develop a race condition when writing the
documents.

The good news is that so far I haven't found anything suggesting my
theory is correct. The bad news is that the test takes an extremely long
time to run. This could be a function of the python client not being
very fast, but I suspect MongoDB is at least partially to blame based on
the logs. There are some long operations like moving indexes and
creating new datafiles that seem to be slower than expected, which I'm
assuming is because of the heavy write load.

The larger picture this test paints is that incrementing documents in
MongoDB is probably a bad idea for any mission critical or highly
available app. The incremental updates play into MongoDBs weaknesses
such as the global write lock and the way it uses mmap to manage how
files are created. For our application I have long thought that we
should have a two phase system. One data store for "live" data and keep
static data in another store. In an initial iteration of this design I
would picture a MongoDB instance for both and migrate data inbetween,
doing some compaction along the way. Hopefully these tests, even if they
prove MongoDB has been doing fine, will help support my design ideas.


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
