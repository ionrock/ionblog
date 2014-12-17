Thinking About ETLs
===================

My primary focus for the last year or so has been writing ETLs at
work. It is an interesting problem because on some level it feels
extremely easy, while in reality, it is a problem that is very
difficult to abstract.


Queries
-------

The essence of an ETL, beyond the obvious "extract, transform, load",
is the query. In the case of a database, the query is typically the
`SELECT` statement, but it usually is more than that. It often
includes the format of the results. You might need to chunk the data
using multiple queries. There might be columns you skip or columns you
create.

In non-database ETLs, it still ends up being very similar to
query. You often still need to find boundaries for what you are
extracting. For example, if you had a bunch of date stamped log files,
doing a `find /var/logs -name 2014*.log.gz` could still be considered
a query.

A query is important because ETLs are inherently fragile. ETLs are
required because the standard interface to some data is not available
due to some constraints. By bypassing standard, and more importantly
supported, interfaces, you are on your own when it comes to ensuring
the ETL runs. The database dump you are running might timeout. The
machine you are reading files from may reboot. The REST API node you
are hitting gets a new version and restarts. There are always good
reasons for your ETL process to fail. The query makes it possible to
go back and try things again, limiting them to the specific subset of
data you are missing.


Transforms
----------

ETLs often are considered part of some analytics pipeline. The goal
of an ETL is typically to take some data from some system and transform
it to a format that can be loaded into another system for analysis. A
better principle is to consider storing the intermediaries such that
transformation is focused on a specific generalized format, rather
than a specific system such as a database.

This is *much* harder than it sounds.

The key to providing generic access to data is a standard schema for
the data. The "shape" of the data needs to be described in a fashion
that is actionable by the transformation process that loads the data
into the analytics system.

The schema is more than a type system. Some data is heavy with
metadata while other data is extremely consistent. The schema should
provide notation for both extremes.

The schema also should provide hints on how to convert the data. The
most important aspect of the schema is to communicate to the loading
system how to transform and / or import the data. One system might
happily accept a string with `2014-02-15` as a date if you specify it
is a date, while others may need something more explicit. The schema
should communicate that the data is date string with a specific format
that the loading system can use accordingly.

The schema can be difficult to create. Metadata might need a suite of
queries to other systems in order to fill in the data. There might
need to be calculations that have to happen that the querying system
doesn't support. In these cases you are not just transforming the
data, but processing it.

I admit I just made an arbitrary distinction and definition of
"processing", so let me explain.


Processing Data
~~~~~~~~~~~~~~~

In a transformation you take the data you have and change it. If I
have a URL, I might transform it into JSON that looks like `{'url':
$URL}`. Processing, on the other hand, uses the data to create new
data. For example, if I have a RESTful resource, I might crawl it to
create a single view of some tree of objects. The important difference
is that we are creating new information by using other resources not
found in the original query data.

The processing of data can be expensive. You might have to make many
requests for every row of output in a database table. The
calculations, while small, might be on a huge dataset. Whatever the
processing that needs happen in order to get your data to a
generically usable state, it is a difficult problem to abstract over a
wide breadth of data.

While there is no silver bullet to processing data, there are tactics
that can be used to process data reliably and reasonably fast. The key
to abstracting processing is defining the unit of work.


A Unit of Work
~~~~~~~~~~~~~~

"Unit of Work" is probably a loaded term, so once again, I'll define
what I mean here.

When processing data in an ETL, the Unit of Work is the combination
of:

 - an atomic record

 - an atomic algorithm

 - the ability to run the implementation

If all this sounds very map/reducey it is because it is! The
difference is that in an ETL you don't have the same reliability you'd
have with something like Hadoop. There is no magical distributed
file system that has your data ready to go on a cluster designed to run
code explicitly written to support your map/reduce platform.

The key difference with processing data in ETLs vs. some system like
Hadoop is the implementation and execution of the algorithm. The
implementation includes:

 - some command to run on the atomic record

 - the information necessary to setup an environment for that script
   to run

 - an automated to input the atomic record to the command

 - a guarantee of reliable execution (or failure)


If we look at a system like Hadoop, and this applies to most
map/reduce platforms that I've seen, there is an explicit step that
takes data from some system and adds it to the HDFS store. There is
another step that installs code, specifically written for Hadoop, onto
the cluster. This code could be using Hadoop streaming or actual Java,
but in either case, the installation is done via some deployment.

In other words, there is an unsaid step that **Extracts** data from
some system, **Transforms** it for Hadoop and **Loads** it into
HDFS. The processing in this case is getting the data from whatever
the source system is into the analytics system, therefore, the
requirements are slightly different.

We start off with a command. The command is simply an executable
script like you would see in Hadoop streaming. No real difference
here. Each line passed to the command contains the atomic record as
usual.

Before we can run that command, we need to have an environment
configured. In Hadoop, you've configured your cluster and deployed
your code to the nodes. In an ETL system, due to the fragility and
simpler processing requirements (no one should write a SQL-like system
on top of an ETL framework), we want to set up an environment every
time the command runs. By setting up this environment every time the
command runs you allow a clear path for development of your ETL
steps. Making the environment creation part of the development process
it means that you ensure the deployment is tested along side the
actual command(s) your ETL uses.

Once we have the command and an environment to run it in we need a way
to get our atomic record to the command for actual processing. In
Hadoop streaming, we use everyone's favorite file handle, `stdin`. In
an ETL system, while the command may still use `stdin`, the way the
data enters the ETL system doesn't necessarily have a distributed
file system to use. Data might be downloaded from S3, some RESTful
service, and / or some queue system. It important that you have a
clear automated way to get data to an ETL processing node.

Finally, this processing must be reliable. ETLs are low priority. An
ETL should not lock your production database for an hour in order to
dump the data. Instead ETLs must quietly grab the data in a way that
doesn't add contention to the running systems. After all, you are
extracting the data because a query on the production server will bog
it down when it needs to be serving real time requests. An ETL system
needs to reliably stop and start as necessary to get the data
necessary and avoid adding more contention to an already resource
intensive service.


Loading Data
------------

Loading data from an ETL system requires analyzing the schema in order
to construct the understanding between the analytics system and the
data. In order to make this as flexible as possible, it is important
that the schema use the source of data to add as much metadata as
possible. If the data pulls from a Postgres table, the schema should
idealling include most of the schema information. If that data must
be loaded into some other RDBMS, you have all you need to safely read
the data into the system.


Development and Maintenance
---------------------------

ETLs are always going to be changing. New analytics systems will be
used and new source of data will be created. As the source system
constraints change so do the constraints of an ETL system, again, with
the ETL system being the lowest priority.

Since we can rely on ETLs changing and breaking, it is critical to
raise awareness of maintenance within the system.

The key to creating a maintainable system is to build up from small
tools. The reason being is that as you create small abstractions at a
low level, you can reuse these easily. The trade off is that in the
short term, more code is needed to accomplish common tasks. Over time,
you find patterns specific to your organizations requirements that
allow repetitive tasks to be abstracted into tools.

The converse to building up an ETL system based on small tools is to
use a pre-built execution system. Unfortunately, pre-built ETL
systems have been generalized for common tasks. As we've said earlier,
ETLs are often changing and require more attention than a typical
distributed system. The result is that using a pre-built ETL
environment often means creating ETLs that allow the pre-built ETL
system to do its work!


Testing
~~~~~~~

Our goal for our ETLs is to make them extremely easy to test. There
are many facets to testing ETLs such as unit testing within an actual
package. The testing that is most critical for development and
maintenance is simply being able to quickly run and test a single step
of an ETL.

For example, lets say we have an ETL that dumps a table, reformats
some rows and creates a 10GB gzipped CSV file. I only mention the size
here as it implies that it takes too long to run over the entire set
of data every time while testing. The file will then be uploaded to S3
and notify a central data warehouse system. Here are some steps that
the ETL might perform:

 1. Dumping the table
 2. Create a schema
 3. Processing the rows
 4. Gzipping the output
 5. Uploading the data
 6. Update the warehouse

Each of these steps should be runnable:

 - locally on a fake or testing datbase
 - locally, using a production database
 - remotely using a production database and testing system (test
   bucket and test warehouse)
 - remotely using the production database and production systems

By "runnable", I mean that an ETL developer can run a command with a
specific config and watch the output for issues.

These steps are all pretty basic, but the goal with an ETL system is
to abstract the pieces that can be used across all ETLs in a way that
is optimal for your system. For example, if your system is
consistently streaming, your ETL framework might allow you to chain
file handles together. For example ::

  $ dump table | process rows | gzip | upload

Another option might be that each step produces a file that is used by
the next step.

Both tactics are valid and can be optimized for over time to help
distill ETLs to the minimal, changing requirements. In the above
example, the database table dump could be abstracted to take the
schema and some database settings to dump any table in your
databases. The gzip, upload and data warehouse interactions can be
broken out into a library and/or command line apps. Each of these
optimizations are simple enough to be included in an ETL development
framework without forcing a user to jump through a ton of hoops when a
new data store needs to be considered.


An ETL Framework
~~~~~~~~~~~~~~~~

Making it easy to develop ETLs means a framework. We want to create a
Ruby on Rails for writing ETLs that makes it easy enough to get the
easy stuff done and powerful enough to do deal with the corner
cases. The framework revolves around the schema and the APIs to the
different systems and libraries that provide language specific APIs.

At some level the framework needs to allow the introduction of other
languages. My only suggestion here is that other languages are
abstracted through a command line layer. The ETL framework can
eventually call a command that could be written in whatever language
the developer wants to use. ETLs are typically used to export data for
to a system that is reasonably technical. Someone using this data most
likely has some knowledge of some language such as R, Julia or maybe
JavaScript. It is these technically savvy data wranglers we want to
empower with the ETL framework in order to allow them to solve small
ETL issues themselves and provide reliability where the system can be
flaky.


Open Questions
--------------

The system I've described is what I'm working on. While I'm confident
the design goals are reasonable, the implementation is going to be
difficult. Specifically, the task of generically supporting many
languages is challenging because each language has its own ecosystem
and environment. Python is an easy language for this task b/c it is
trivial to connect to a Ubuntu host have a good deal of the ecosystem
in place. Other languages, such as R, probably require some coordination
with the cluster provisioning system to make sure base requirements
are available. That said, it is unclear if other languages provide
small environments like virtualenvs do. Obviously typical scripting
languages like Ruby and JavaScript have support for an application
local environment, but I'm doubtful R or Julia would have the same
facilities.

Another option would be to use a formal build / deployment pattern
where a container is built. This answers many of the platform
questions, but it brings up other questions such as how to make this
available in the ETL Framework. It is ideal if an ETL author can
simply call a command to test. If the author needs to build a
container locally then I suspect that might be too large a requirement
as each platform is going to be different. Obviously, we could
introduce a build host to handle the build steps, but that makes it
much harder for someone to feel confident the script they wrote will
run in production.

The challenge is because our hope is to empower semi-technical ETL
authors. If we compare this goal to people who can write HTML/CSS
vs. programmers, it clarifies the requirements. A user learning to
write HTML/CSS only has to open the file in a web browser to test
it. If the page looks correct, they can be confident when they deploy
it will work. The goal with the ETL framework and APIs is that the
system can provide a similar work flow and ease of use.


Wrapping Up
-----------

I've written a **LOT** of ETL code over the past year. Much of what I
propose above reflects my experiences. It also reflects the server
environment in which these ETLs run as well as the organizational
environment. ETLs are low priority code, by nature, that can be used
to build first class products. Systems that require a lot of sysadmin
time, server resources or have too specific an API may still be
helpful moving data around, but they will fall short as systems
evolve. My goal has been to create a system that evolves with the data
in the organization and empowers a large number of users to distribute
the task of developing and maintaining ETLs.



.. author:: default
.. categories:: code
.. tags:: python, map reduce, hadoop, data processing, etl
.. comments::
