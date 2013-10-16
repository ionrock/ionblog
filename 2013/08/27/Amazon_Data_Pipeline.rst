====================
Amazon Data Pipeline
====================



`Amazon Data Pipeline`_ is a tool make running data processing jobs
easier in the AWS cloud. Essentially it tries to wrap up the process
of grabbing data, putting it on EC2 instances, and running some
processing via EMR (Hadoop). It takes care of a bunch of details like
starting up a cluster, pulling and uncompressing data from S3 or other
data sources, pushing the results back to S3 and a whole host of other
bits that you'd have to sort out yourself if you were building a
system on hadoop.

The biggest benefit of AWS data pipeline is that it automates a lot of
small details. It is non-trivial to spin up a hadoop cluster, populate
the filesystem across nodes, distribute your tasks, schedule jobs and
return the results to a known location on S3. There are a lot of balls
needing juggling and data pipeline provides a reasonably low point of
entry.

The downside is that you really need some knowledge of what is going
with data pipeline in order to use it effectively. There are a ton of
options to consider and unless you are familiar with the specific
storage medium or processing system you are working with, it can be
pretty overwhelming and confusing.

Seeing as I'm just getting started with data pipeline, I'm unclear how
big a benefit it is or where it really excels. If I didn't run large
jobs often or had a small number of them that needed to run, it seems
like a good platform. The debugging and knowledge required to do a
specific task a few times is reasonable if you are going to get
reproducible data for a year or more. It remains to be seen if it is a
good platform for when you have more robust requirements.

As an aside, it goes to show how difficult it can be process
data. There are no shortcuts taking a data source and processing
it. Computers can't really guess b/c they can't check if they were
right. People have the ability to try something, check the result and
make an assertion on how correct it is. In this way we can see
patterns that are opaque to a computer. Within the context processing
huge amounts of data, it would be extremely helpful if a query could
describe to the computer how to pull out data from some dataset in
order to push it into a processing system. If we solved this problem,
we might be able to expose data processing to the masses.

The state of social media suggests the power process massive amounts
of data would probably amount to better cat videos, but who doesn't
love cats!


.. _Amazon Data Pipeline: http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html


.. author:: default
.. categories:: code
.. tags:: cloud, data
.. comments::
