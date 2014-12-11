Dadd, ErrorEmail and CacheControl Releases
==========================================

I've written a couple new bits of code that semeed like they could be
helpful to others.

Dadd
----

`Dadd <https://github.com/ionrock/dadd/>`_ (pronounced Daddy) is a
tool to help administer daemons.

Most deployment systems are based on the idea of long running
processes.  You want to release a new version of some service. You
build a package, upload it somewhere and tell your package manager to
grab it. Then you tell your process manager to restart it to get the
new code.

Dadd works differently. Dadd lets you define a short spec that
includes the process you want to run. A dadd worker then will use that
spec to download any necessary files, create a temporary directory to
run in and start the process. When the process ends, assuming
everything went well, it will clean up the temp directory. If there
was an error, it will upload the logs to the master and send an
email.

Where this sort of system comes in handy is when you have scripts that
take a while to run and that shouldn't be killed when new code is
released.  For example, at work I manage a ton of ETL processes to get
our data into a data warehouse we've written. These ETL processes are
triggered with Celery tasks, but they typically will ssh into a
specific host, create a virtaulenv, install some dependencies, and
copy files before running a deamon and disconnecting. Dadd, makes this
kind of processing more automatic where it can run these processes on
any host in our cluster. Also, because the dadd worker builds the
environment, it means we can run a custom script without having to go
through the process of a release. This is extremely helpful for
running backfills or custom updates to migrate old data.

I have some ideas for Dadd such as incorporating a more involved build
system and possibly using lxc containers to run the code. Another
inspriation for Dadd is for setting up nodes in a cluster. Often times
it would be really easy to just install a couple python packages but
most solutions are either too manual or require a specific image to
use things like chef, puppet, etc. With Dadd, you could pretty easily
write a script to install and run it on a node and then let it do the
rest regarding setting up an environment and running some code.

But, for the moment, if you have code you run by copying some files,
Dadd works really well.


ErrorEmail
----------

`ErrorEmail <https://github.com/ionrock/erroremail/>`_ was written
specifically for Dadd. When you have a script to run and you want a
nice traceback email when things fail, give ErrorEmail a try. It
doesn't do any sort rate limiting an the server config is extremely
basic, but sometimes you don't want to install a bunch of packages
just to send an email on an error.

When you can't install django or some other framework for an
application, you can still get nice error emails with ErrorEmail.


CacheControl
------------

The CacheControl 0.10.6 release includes support for calling `close`
on the cache implementation. This is helpful when you are using a
cache via some client (ie Redis) and that client needs to safely close
the connection.


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
