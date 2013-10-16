================
 Starting Fresh
================

At work I work on a project that has been a project for quite a while
now. As such, we've tried to add a lot of new features, but the reality
is almost all the work is maintenance. Fortunately though, I was
informed yesterday that our next iteration was on the horizon and the
current version was going to have a strict feature freeze in the new
year! This is really exciting for me because while I've done some new
code at work, the vast majority of my responsibility is maintaining our
current system.

A theme of this maintenance was actually that often times it was better
to rewrite a feature rather than edit the code. The code isn't bad, but
it is from a different time. It started with a different Python version,
testing wasn't necessarily a top priority (I'm still personally working
this aspect), and the company was in startup mode where new features
were often more important making sure you went back and cleaned up the
code. Along similar lines, we now are a lot larger and some of the
designs have been stressed by the load. Making changes to add features
usually ends up meaning schema changes (in one way or another, even
though we are using `MongoDB`_), which are rarely cheap. Now is
definitely a good time to consider a reset to see where we can improve
our design and prepare for the future.

There is a different between starting fresh and restarting. To use a
computer term, restarting shuts down the computer and brings it back up
again. Anything left in memory is gone. Refreshing is more a process of
taking what you have now and using it a reference as you recreate it.
Consider it like a disk defrag or reindex in the database. Your goal is
not to change the function, but rather clean up the debris left behind
through years of use.

What is also interesting is that we will finally have an opportunity to
truly change how we store and accept data. This second iteration of our
application went from using a home-made storage engine based on bsddb to
using MongoDB. While MongoDB is pretty cool, it has its warts. Honestly,
I'm not sure it is the right path either. The big plus with MongoDB is
that you can query it. When there are fires to put out finding
information is critical and queries in MongoDB can be lifesavers.

Outside of that though, MongoDB feels somewhat dangerous. We added
indexes and realized that we are more write heavy than we realized. That
or we are write heavy enough to plague MongoDB. You also need a lot of
machines to really fulfill MongoDB's replication expectations. This
might be a good thing, but outside losing power and natural disasters,
there are people called users that make things called "typos" that can
end up "killing" the wrong process. MongoDB doesn't protect against this
"threat" and that makes things a little scary at times.

All this is not to say we won't use MongoDB though. What I know I'd
like to implement is a queue that also acts like a bus. My take away
from our old design is that we have different use cases for our data. We
need some layer of abstraction over our data, but at the same time, we
need to do some more setup before trusting a single DB system to just
work supporting all our use cases. The idea then is to have some
somewhere to queue data coming in, while at the same time notify the
systems that need it. As new data comes in some processes want it right
away, while others need to wait until more data in its set have
completed. We work on finding `what people think`_, so there are
multiple levels of this data. There is the overarching topic described
by the survey, individual questions and how each person's opinion fits
within the sample. The bus then should support keeping the data while
each of these use cases are supported.

There are a lot of details yet to understand, but the process should be
helpful and fun. As a developer you are always trying to improve your
skills. The goal should be to write functioning code that is easy to
maintain, but that is a difficult thing to practice if you a) never
maintain code or b) never have to write code that gets maintained by
others. This gives me personally a chance to write some new code that
others will need to maintain at some point in the future. I'm also
excited to hopefully consider using a newer version of Python, writing
tests from scratch and generally getting to try out some new-ish tools
to make life easier. It should be a great new year!

.. _MongoDB: http://mongodb.org
.. _what people think: http://yougov.com


.. author:: default
.. categories:: code
.. tags:: mongodb, programming, python, testing
.. comments::
