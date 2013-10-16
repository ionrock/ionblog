SQL Isn&#039;t the Problem
##########################

I read this `article`_ commenting on Facebook and how their MySQL based
system must be so complex that it is hell to work with. At the end of
the article the author brings up "NewSQL" which is basically the
practice of providing ACID compliance, but without many of the other
features of a typical RDBMS. My personal take is that it is a reboot on
relational databases that recognizes potential "requirements" that can
be safely dropped and advertised in order to gain better performance.
After spending a good deal of time with MongoDB and some similar
home-grown databases, I don't believe that SQL is really the problem.
More specifically, I don't think the relational model is the problem,
but rather how we think about storing things. Just because you are using
a RDBMS it doesn't mean you have to normalize your data. It doesn't mean
you have to store all your fields in tables. Instead, when using any
data store, your main concern should be how you write and retrieve your
data in a way that it will be performant. Looking at the data storage
problem from a simpler perspective is helpful because when you take away
larger preconceived ideas of how you "should" do things, it allows you
room to consider what is both possible and realistically evaluate what
could work for your situation.
Many times NoSQL solutions are based on the idea of having a key /
value store. The need to query is often bolted on this aspect by
providing data types and recognizing JSON formatted "values" in the
store. The result being that the store is not really a hash table, but
rather it is a set of indexes on fields within your formatted document
that allow you to combine and "query" for more specificity than you
could otherwise. You could just as easily keep index tables in a RDBMS
that you update via a trigger or manually and store the document as JSON
in a blob. There are downsides to this of course, but the reality is
that an RDBMS and a NoSQL database are probably using many of the same
techniques to do the core operations of storing the document efficiently
and utilizing the indexes to find the data. Just because you are not
using SQL, it doesn't mean you magically remove the limitations of
computer hardware and the years of research that has been done on how to
effectively store data.
My point is not to tout RDBM systems as the perfect solutions because
they are not. The point here is to recognize there isn't a free lunch.
I'm sure if Facebook had a system based on MongoDB, Redis or CouchDB
there would be a massive amount of complexity there as well. Storing
massive amounts of data quickly and retrieving it is not a simple
problem. No matter what data store you choose there will need to be
similar operations done within the process of saving the data (adding
and creating indexes) and retrieving it (finding the row / document,
filtering or finding the fields requested). There are tons of options
within the work flow, but they will have to happen. NoSQL often moves
these to the application layer, so while your database system might
become simpler, you may have increased your test complexity in your
application. There really isn't a free lunch.

.. _article: http://gigaom.com/cloud/facebook-trapped-in-mysql-fate-worse-than-death/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
