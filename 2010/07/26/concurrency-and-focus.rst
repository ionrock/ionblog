=======================
 Concurrency and Focus
=======================

Last night as `we`_ were driving back towards the great state of Texas,
we listened to `Coast to Coast`_. If you've never listened, it is a
radio show that traditionally focuses on non-mainstream topics that can
often stretch well into the weird. It is a fun show to listen to for
freak factor as well as the interesting perspectives. The guest in this
case was the author of the book The Shallows, Nicholas Carr. The book
argues that the Internet has changed the way people think and robbed
people of focus, and personally, I have to agree.

One interesting thing he talked about was the brain's concept of
memory. He described the basic ideas of RAM vs. CPU Cache vs. the hard
drive. The idea was that we've gotten faster RAM thanks to the web, but
in doing so, we've lost the ability to save ideas and knowledge to our
long term memory storage. One argument he disagreed with was that the
web offers you a place to store information so you can think about other
things. I partially disagreed with this because as a programmer, much of
my job is finding interfaces and layers to help manage complexity,
effectively relieving my mind of the burdens associated with lower level
problems.

This quest to hide complexity has been a major theme in computing. Back
when computers were actual people, the idea was that a scientist could
let the computer do the low level work while they continued to hone
their larger level algorithms and models. The ability to abstract and
classify is critical to moving beyond what you can do by yourself. There
are so many details in the world that without tools to manage them, life
would be unbearable.

Concurrency is a very similar situation. I read `this article`_
discussing how trends in concurrency often do not fairly characterize
the problem. This got me thinking about the issues with focus. If we
consider concurrency in terms of workers that all equally do things, you
miss the obvious abstractions you get from more specific tools. Like
learning to focus, the goal is not to store information as much it is to
manage the transitions and interruptions. It is often simpler to have a
master process that handles specifically who does what than relying on a
generic solution to magically do everything correctly. Just like the
scientists in the early days of computing, we should think of
concurrency in terms of how we can create abstractions while freeing up
resources in a way that doesn't force us to pass everything through to a
intermediary. There were probably plenty of computations that early
programmers did themselves. But at some point, there was a decision made
on a set of parameters that suggested the solution be sent to a computer
to do the work. It is this kind of mindset that will make concurrency in
the future relevant in the future and reasonable to implement.


.. _we: http://umemusic.com
.. _Coast to Coast: http://www.coasttocoastam.com/
.. _this article: http://dtrace.org/blogs/bmc/2008/11/03/concurrencys-shysters/


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
