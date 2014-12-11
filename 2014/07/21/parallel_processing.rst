Parallel Processing
===================

It can be really hard to work with data programmatically. There is
some moment when working with a large dataset where you realize you
need to process the data in parallel. As a programmer, this sounds
like it could be a fun problem, and in many cases it is fun to get all
your cores working hard crunching data.

The problem is parallel processing never is purely a matter of
distributing your work across CPUs. The hard part ends up being
getting the data organized before sending it to your workers and doing
something with the results. Tools like Hadoop boast processing
terabytes of data, but it's a little misleading because there is most
likely a ton of code on either end of that processing.

The input and output code (I/O) can also have big impact on the
processing itself. The input often needs to consider what the atomic
unit is as well as what the "chunk" of data needs to be. For example,
if you have 10 million tiny messages to process, you probably want to
chunk up the million messages into 5000 messages when sending it to
your worker nodes, yet the workers will need to know it is getting a
chunk of messages vs. 1 message. Similarly, for some applications the
message:chunk ratio needs to be tweaked.

In hadoop this sort of detail can be dealt with via HDFS, but hadoop
is not trivial to set up. Not to mention if you have a bunch of data
that doesn't live in HDFS. The same goes for the output. When you are
done, where does it go?

The point being is that "data" always tends towards spcificity. You
can't abstract away data. Data always ends up being physical at its
core. Even if the processing happens in parallel, the I/O will always
be a challenging constraint.


.. author:: default
.. categories:: code
.. tags:: python, mapreduce, hadoop, multiprocessing
.. comments::
