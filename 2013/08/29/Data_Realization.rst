================
Data Realization
================


17 hours and 35 seconds. That is the amount of time I've been running
an Elastic Map Reduce job. The file is a 16 GB compressed. I'm using
10 small EC2 instances.

It is my first EMR experience and it wouldn't surprise me in the least
if I was doing something wrong.

The thing that is interesting about this process is that all this time
has been spent moving data around. My understanding (and the
monitoring tool mrjob_ provides confirms) is we must first take all
our data and make it available to our EC2 instances. I'm supposing
this process means copying it from s3 and putting it in a hadoop
filesystem for processing. My guess is that the actual processing
won't take nearly as long... At least I hope not.

It just goes to show that data has a price. In theory, digital content
can be moved all over the world in an instant. In reality our networks
are insanely limited, our hard drives are slow and the more moving
pieces the slower things become. It doesn't come a surprise, but it is
something to think about when you have a lot of data you want to work
with.

When I started working on this project, I questioned the decision of
putting the data in S3. I wondered if uploading it directly to an HDFS
cluster would be a better tact. Seeing as we hadn't settled on a
processing system, it felt like a premature optimization. Yet, in the
back of my mind, I wondered how Amazon could conceivably take huge
files, put them on an HDFS cluster for processing, run a job and clean
things up faster than I could dump a database to a decent sized
machine and run my processing locally. It appears that my intuition
might have been right after all.

More data, more problems I suppose.


.. _mrjob: http://pythonhosted.org/mrjob/index.html


.. author:: default
.. categories:: code
.. tags:: python, cloud, big data
.. comments::
