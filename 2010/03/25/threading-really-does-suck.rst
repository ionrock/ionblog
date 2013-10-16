============================
 Threading Really Does Suck
============================

For a large portion of my programming career, I've made an effort to
avoid threads. The constant barrage of negative press and issues
associated with the concepts behind threads made me nervous about their
use and more importantly, my ability to effectively. As I've grown as a
programmer my perspective on threads has changed. They seemed less
magical and more practical. Discipline could make them viable options
and in fact a really helpful tool.

While I believe threads have their value, I'm back to thinking they
sort of suck. Recently trying to profile some code I realized that a
whole host of functionality was never getting touched. This was because
there was only one thread and one process. I've yet to actually get very
far in writing a more extensive test to utilize more threads/processes
(I need to stress the connections to the database), but I'm not looking
forward to it.

The big issue is not so much idea of threads or processes, but just the
lack of polish when it comes to working with them. Part of the problem
is your truly. I'm always forgetting to do some bit of preparation or
have screwed up some thread safety issue. But there are other times
where what I'm trying really feels like it should work, but it doesn't.
All these issues are really my own responsibility, but I do wish someone
could come along and make a really simple threading/process package that
goes beyond the constructs and doesn't do anything odd. I'm thinking of
things like the different actor implementations or possibly something
like `Kamaelia`_ without all the networking oddness. I'm sure something
will happen in this space since it is so critical with the move to
multiple cores and the need to scale horizontally. In the mean time, I'm
going to keep trying to get better at threads even though they sort of
suck.


.. _Kamaelia: http://www.kamaelia.org/Home.html


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
