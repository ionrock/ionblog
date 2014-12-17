MongoDB Headroom
################

There is a `thread`_ on Hacker News that discusses some issues someone
had with MongoDB. The party line on MongoDB is that while it has
problems, `10gen`_ (the company behind MongoDB) is very supportive and
that is definitely true in my experience. My problem with MongoDB has
never been support, but rather that it offers no headroom.

Bass players often talk about how much headroom an amplifier offers.

What they are talking about is how loud you can turn it up before things
start to go bad. Bass is not like a guitar because the low frequencies
it can produce have the ability to break things. It shakes material and
can blow out speaker with longs wave forms, which means a speaker cone
is traveling a long way with every movement. Having headroom means you
can still turn it up and not worry things are going to break.

In our experience, it feels as if MongoDB never gives us any headroom.

The usage pattern we've had has been to release code, notice a problem
in MongoDB days or week after the code change  and try to understand
what changed knowing the code didn't change recently. There have also
been times when we did change code and saw an immediate negative effect.

I remember one instance where we added an index (we had only one at the
time) and our performance grinded to a halt. Now obviously you can't
assume that adding an index is without cost, but since we had only 1 on
the collection, you'd think that adding one more would be pretty
reasonable. This is what I mean when I talk about headroom.

At this point I'm not a fan of MongoDB. I don't understand where its
sweet spot really is. Using it as a key value store is pretty decent if
you don't have many writes. We have an gettext like service using
MongoDB and language catalogs don't get updated too terribly often.

MongoDB has been just fine for this kind of usage (although, I'll point
out that a client uses HTTP and caching to make it as fast as gettext).

We download lots of data from MongoDB and it seems reasonably fast, but
we also have had to move some processing out of queries because it was
more expensive than just doing it on the application side. We had also
had to implement an implicit external index patter where we have a
different database that keeps an index on another database's data, the
"databases" being MongoDB databases. Outside of the obvious potential
consistency issues, this pattern has worked pretty well. Yet even though
it is "working", we are constantly concerned about the next outage and
when memory will start going up for no apparent reason.

There is obviously a reason for our problems and I'm sure our code is
part of the problem. But, I also don't think we are doing anything
massively outside the realm of what MongoDB should excel at, yet it
always feels that way. We're not talking about terabytes of data we have
to crawl through all the time. The documents are all effectively atomic.

Once they are done being written, they never written to again. Yet, we
these obvious constraints that would help with performance and providing
headroom, we seem to have none.

I have a feeling that we will continue to use MongoDB, but I'd like to
figure out exactly where it excels and use it there. Otherwise, I'd be
happy with other systems picking up some of the slack to help get a
little headroom for the future and a better plan of attack to scale into
the future.

.. _thread: http://news.ycombinator.com/item?id=3202081
.. _10gen: http://10gen.com


.. author:: default
.. categories:: code
.. tags:: mongodb, programming, python
.. comments::
