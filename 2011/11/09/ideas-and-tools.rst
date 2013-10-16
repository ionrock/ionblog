Ideas and Tools
###############

It is interesting to see the progression of cloud technology. Amazon has
been extremely successful selling the concept of cloud based systems and
it has had an impact on the entire software landscape. Companies like
10gen who make MongoDB have a product that assumes your datacenter lives
in the cloud and that having multiple machines to provide replication is
a given and that all your indexes can fit in memory. I don't think we'd
see things like MongoDB and the wealth of virtualization tools had it
not been for Amazon's initial push. It was a pretty powerful idea.

What has developed since then is a suite of tools that consider the
machine the unit of deployment. Instead of pushing code to a server
directory, you spin up new image and reinstate some application code.
Instead of having constraints like a single directory to keep files you
have no filesystem whatsoever. The data must be kept outside the
application at all times because when the machine reboots it also means
reinstalling everything. Again, it is a powerful idea.

The machine being the unit of deployment has impacted developer tools.
Things like distributed version control can make it trivial for a script
to check out some code or configuration on a server to set things up.
Tools like `chef`_ and `puppet`_ help manage configuration across any
number of machines that have been configured in an virtual machine
image. Other tools like `fabric`_ allow the automation of running
commands on a machine. All these tools build on the assumption that you
have a set of machines that are exactly (more or less) the same that you
need to consistently configure.

The point being is that the ideas behind much of the cloud has had a
huge impact on the tools. It makes me wonder though what might have been
possible had there been a different set of ideas in place. What if EC2
was more like a chroot jail with a single directory to run processes.
Would will still see so many NoSQL databases and would they be as
focused on being distributed? Would tools like puppet and chef still be
a widely used or would we simply see more use of rsync? Would something
like Hadoop be simpler by allowing direct use of the filesystem instead
of its HDFS? It is interesting to think about.

At some point though there seems to be a moment where trying to do
things differently isn't really worth the time. Python has been a
language that has competed with typical shared hosting and has not been
very successful. I think most Python developers consider it a given that
you should use a VPS to host a Python web app. But is that really the
case? `WebFaction`_ has been successful providing Python hosting in a
shared environment, so we know it can be done. Yet, it seems that the
ship has sailed and we'd rather always configure entire machines rather
than untar a tarball in a directory.

The irony in my mind is that power behind the ideas has pushed the tools
so far that the seemingly inefficient process of setting up entire
machines has become easier than simply writing applications under the
assumption there is a filesystem and a single directory to work from. It
makes you wonder if all the presumed savings behind the cloud really is
worth it. Virtualization is a double edged sword in that it provides
flexible environments quickly while abstracting away access to efficient
hardware. All those CPU cycles we use to make sure application A doesn't
interfere with application B by providing two different machines could
have been used by both application A and B had they been written more
carefully to use a sandbox on the filesystem. Maybe it is too cheap to
matter, but it still makes me wonder.

I don't think I really have an important point here past it is important
to question the status quo every once in a while. I've always been a fan
of the cloud, NoSQL and distributed version control, while at the same
time looking back at my time with PHP and shared hosting and realizing
it was really easy back then to get an application out the door. Maybe
we are doing it wrong.

.. _chef: http://wiki.opscode.com/display/chef/Home
.. _puppet: http://puppetlabs.com/
.. _fabric: http://fabfile.org/
.. _WebFaction: http://www.webfaction.com/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
