Good Enough
===========

Eric Shrock wrote a great blog on `Engineer Anti-Patterns
<http://dtrace.org/blogs/eschrock/2012/08/14/engineer-anti-patterns/>`_. I,
unfortunately, can admit I've probably been guilty of each and every
one of these patterns at one time or another. When I think back to
times these behaviors have crept in, the motivations always come back
to what is really "good enough".

For example, I've been "the talker" when I've seen a better solution
to a problem and can't let it go. The proposed solution was considered
"good enough" but not to me. My perspective of what is good enough
clashes with that of the team and I feel it necessary to argue my
point. I wouldn't say that my motives are wrong, but at some point, a
programmer must understand when and how to let an argument go.

The quest to balance "good enough" with best practices is rarely a
simple yes or no question. Financial requirements might force you to
make poor engineering decisions in favor of losing money in that
moment. There are times where a program hasn't proven its value,
therefore strong engineering practices aren't as important as simply
proving the software is worth being written. Many times, writing and
releasing something, even if it is broken, is a better political
decision in an organization.

I suspect that most of these anti-patterns are a function of fear,
specifically, the fear of failing. All of the anti-patterns reflect a
lack of confidence in a developer. It might be imposter syndrome
creeping in or the feeling of reliving a bad experience in the
past. In order to programmers to be more productive and effective, it
is critical that effort is made to reduce fear. In doing so, a
developer can try a solution that may be simply "good enough" as the
programmer knows if it falls short, it is something to learn from
rather than fear.

Our goals as software developers and as an industry should be to raise
the bar of "good enough" to the point where we truly are making educated
risk / reward decisions instead of rolling the dice that some software
is "good enough".

The first step is to reduce the fear of failure. An organization should
take steps to provide an environment where developers can easily and
incrementally release code. Having tests you run locally, then in CI,
then in a staging environment before releasing to a staging
environment and finally to production helps developers feel confident
that pushing code is safe.

Similarly, an organization should make it easy to find failures. Tests
are an obvious example here, but providing well known libraries for
easy integration into your logging infrastructure and error reporting
are critical. It should be easy for developers to poke around in the
environment where things failed to see what went wrong. Adding new
metrics and profiling to code should be documented and encouraged.

Finally, when failures do occur, they should not be a time to place
blame. There should be `blameless postmortems
<https://codeascraft.com/2012/05/22/blameless-postmortems/>`_.

Many programmers and organizations fear spending time on basic tooling
and consistent development environments. Some developers feel having
more than on step between commit and release represents a movement
towards perfection, the enemy of "good enough". We need to stop
thinking like this! Basic logging, error reporting, writing tests,
basic release strategies are all critical pieces that have been
written and rewritten over and over again at thousands of
organizations. We need to stop avoiding basic tenants of software
development under the guise being "good enough".


.. author:: default
.. categories:: code
.. tags:: python, programming, tests, deployment
.. comments::
