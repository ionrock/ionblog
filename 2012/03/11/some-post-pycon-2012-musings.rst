Some Post PyCon 2012 Musings
############################

`PyCon`_ is already over for me this. `SXSW`_ Music means that I have
obligations back in my home town to hang out, play music and have some
free beer when I can. It also means that I was unable to stick around
for the surrounding PyCon activities such as sprints, which I had hoped
there was a chance of attending. Such is life.

This year I took a different tact than in the past. Previous PyCons
brought the opportunity to hack on something. The process would involve
thinking of some technology to utilize and writing some application that
uses it. Rarely would I finish it, but usually it gave me a reason to be
on my computer during talks and generally have some goal for the weekend
of geekery. Sometimes it is really nice to spend a weekend with nothing
to think about except code.

Rather than occupy my time with a throw away project, my goal was to
listen. My laptop stayed closed in the sessions I attended. I took some
time to actually look at the schedule and pick out talks I was
interested in. When I'd go to a talk, unless it was extremely
uninteresting, I'd sit and focus on the talk. The experience was
definitely fruitful because instead of walking away from PyCon with some
toy application, my impression is that I might be walking away with some
helpful "teach a man to fish" type insights.

The first is testing. I've tried to be a student of TDD school and
probably have flunked out more times than I'd like to admit. My feeling
is that TDD is a tactic and not a goal in and of itself. TDD is really
another tactic to help a programmer slow down and think about what code
should be written. Comments, documentation and specs can all do the same
thing and none are replacements for each other.

When someone says tests are good documentation, they are not being
honest. Tests can be helpful in understanding how to use a piece of
code. Tests make terrible docs. Communication is hard enough in a robust
language like English, so don't think some DSL for testing or unittests
provide some panacea of clarity because they do not. People are not
computers in that they have the ability to make jumps. When a computer
fails, it stops and will not move forward or try again unless explicitly
told to do so. People will make a jump and assume they understand
something and act on that perceived understanding. Therefore, you should
make every effort to meet the communication needs of others and that
often means repeating the same message over different mediums.

`Tox`_ is cool! One of the things Tox does is to create a virtualenv for
installing the package under test. It installs the dependencies and runs
the tests from this env. This is what all tests should do because it
emulates not only the production environment, but it emulates on idea of
an application goes from source to deployed. Hopefully that build step
becomes configurable as I believe it is important to make that
deployment and `execution environment`_ work outside of a single
language or runtime.

The key to handling subtly complex details is to be explicit. Unicode
and dealing with date/times are examples of this. I saw a talk on each
and in both cases it was clear that the desire to avoid thinking about
all the details was a mistake. It is better to accept you need to deal
with all the nitty gritty details. Your helpers and libraries will not
be that hard to write and maintain, so go ahead and write them.

Never assume some technique is going to be correct. `Bob`_ gave a great
talk on maintaining `CherryPy`_ for many versions of Python. He assumed
the prescribed methods from the community were correct. They were wrong.
Mocking is another example where you can be leery to drink the cool-aid.
The community makes an assumption that mocking is a critical part of a
good test suite. This is simply not true. Again, it is a helpful tool,
but it is not required. Remember, what you hear from the community as
the "best" option is really the option that has the best marketing. This
is not a negative because good marketing requires you to do your
homework. But as a user, just because everyone seems to be saying they
use some tool or package, it doesn't mean you'll find success with it.

Always keep things in perspective. Being a working musician and
programmer allows me to see two radically different communities. One
thing I've noticed is that the people who come across with the attitude
that they do nothing but code or play music (no sleep, no food, power
through the pain, etc.) rarely end up making a big difference. Instead
it is clear that the people who find success are the ones working hard
in all facets of life. They work hard and play hard.

That is about it for now. I still have tons of information settling in
my brain at the moment, so I'm sure there will be more realizations. I'm
also looking forward to watching the videos on the talks I missed.
Thanks for a great PyCon!

.. _PyCon: http://us.pycon.com/2012/
.. _SXSW: http://sxsw.com
.. _Tox: http://tox.testrun.org/
.. _execution environment: http://bitbucket.org/elarson/xenv
.. _Bob: http://aminus.org/rbre/index.html
.. _CherryPy: http://cherrypy.org


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
