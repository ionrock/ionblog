DiffDB
######

At work a consistent problem is that we store a single document that can
grow to be rather large. If you consider a database like MongoDB where
you store relevant information in a single atomic document, it can be
problematic to update the document. The unoptimized perspective is to
just throw everything away and update the entire document on each
change. This model is really pretty reasonable, but it does break down
eventually because databases work at a rather low level at times.
Continually writing and rewriting large documents is not an operation
many data stores are optimized for. Databases typically need to know
exactly what pages a document lives on and just as adding a page in the
middle of a book has an effect on the rest of the pages following, so
does increasing a document in a data store.
The other thing to consider is that every document you update sends
that entire document's contents over the network. Considering I/O is
almost always the bottleneck in many applications, continually sending
MBs of information when all that really changes are a few bytes, it
becomes apparent that there is a lot of extra info going over the wire
for each request. I think in the long run RESTful services have some
advantages in this space because there is caching built in, but
generally, it is a really tough problem for a database to handle, hence
most just punt and let the application logic deal with what gets stored
and how.
My idea then is to create a database that is based on updates. I
realize this is pretty much how `MVCC`_ databases work, so nothing too
novel there. The thing that seems like it can be slightly more
interesting is that the client is also part of the equation, which
allows some different assumptions to be made that can hopefully help
optimize the generic storage a bit. Perforce for example (and I'm
positive about this) allows a client to check out a file, which prevents
others. I'm not proposing this model, but rather simply that a database
client could help out at times. In all honesty, I doubt this model adds
enough value that it is worthwhile in many applications. That said, at
my job, I know the incremental nature of the data is something that does
cause problems at scale, so why not take a stab at one method of solving
it.
I'm calling my experiment DiffDB. The idea is that a client starts with
a document, and sends patches to the database, where they are then
applied. There isn't any actual storage happening, but the assumption is
that you'd store the document and query it using some other database
like MongoDB. DiffDB then really would act as a REST based API to
support incremental updates on JSON documents.
The most interesting thing in this equation is the combination of HTTP
(caching, etags, etc.) along side a known patch format for updating
dictionary / hash objects. Since the HTTP layer is a bit more obvious
(we use PATCH to send the patch and PUT to create a new document), I'll
focus on the patch format. The basic idea is to be able to update a JSON
hash with new values as well as remove values.
Fortunately, Python has a rather handy 'update' method on dictionaries
that makes much of the actual patch operation really easy. When you want
to update a dictionary with new values, you just do the following:

::


    a = {'x': 1}

    a.update({'y': 2})

    print a -> {'x': 1, 'y': 2}

Now, removing elements seems like it would be harder, but the fact is
it is really pretty simple. If you had a nested dictionary, removing an
element is the same as copying the parent, leaving out the elements you
want to drop. Here is an example:

::


    a = {'x': 1, 'y': {'z': 2}}

    # removing z

    a.update({'y': {}})

This means that the only time you actually have to explicitly remove
something is when it is at the root level.
With all that in mind, the patch format then looks like this:

::


    {

      '+': { ... }, # the dictionary you want to use in the 'update' method

      '-': [ ... ], # a list of keys you want to remove from the root dictionary

    }

Nothing terribly complicated here. To apply the format, you first loop
through the '-' keys and remove them from the original. Then, you can
call the 'update' method on the dictionary using the '+' value and that
it is.
Again, this is just a simple idea with an even simpler proof of
concept. I don't know if this would be really slow or not, but I suspect
by doing the diff and patch creation on the client side you could get
the gains of small packets on the network, with a limited amount of CPU
time. After all, it is rarely CPU bound operations that are your
bottleneck, but the I/O.
On a more grander scale, I'd hope that the idea of a dict patch model
has some legs for being helpful in other areas. There is some code
`here`_ that has a diff and patch object you can play with to see if it
could be helpful. It always seems like a good idea to put things out
there in hopes others may find inspiration, even if the original idea
doesn't work out.
If anyone does try this out and have thoughts, please let me know.

.. _MVCC: http://en.wikipedia.org/wiki/Multiversion_concurrency_control
.. _here: http://bitbucket.org/elarson/diffdb


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
