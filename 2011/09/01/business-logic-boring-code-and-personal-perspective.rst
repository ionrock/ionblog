Business Logic, Boring Code and Personal Perspective
####################################################

Today we had a code review of some code. We do this in hopes of exposing
some code someone else is working and getting a better vision of what
others apps do, their design patterns and specifics that would help us
contribute if (when) the need arises. One theme I've noticed is that
most comments that are offered have little to do with the business
logic. Not many folks care about some algorithm or function. This is
most likely because you are not going to gain a deep enough
understanding within the course of an hour to have a strong opinion on
some algorithm being used for a project. The result is that business
logic is boring.
I wouldn't say that it is intrinsically boring, but rather that unless
you are invested it is boring. Art and music can both have similar
effects. You hear a song or see a painting and think it is simple and
anyone could do it. Yet, to those well versed in the genre or style can
quickly attest that the artist has in fact introduced a new revolution
within the scene.
It applies to other areas as well. Take the car you drive. If you are a
car person you might really like charger over a camero, but to a
mechanic, who has a deeper understanding of the engines, they are just
two shades of the same thing. Hopefully this example is not completely
lost behind my massive lack of knowledge in cars.
Going back to the code review though, it is interesting to see what
portions of the code did prompt comments. It was almost always opinions
on things like library choice and code patterns. More generally, I might
categorize these as framework-type opinions. This is interesting because
many projects at my job to use different frameworks that traditionally
are dependent on the preference of the author. The result being that
these code reviews often end up being an exercise in a personal
perspective on code rather than an exploration into the business logic
and the project's meat.
If this sounds like something is broken, then I agree. If it doesn't
then let me tell you why it is an indicator that something is broken.
When a team of developers all use their personal perspective to code a
few different things happen. The first is that emotions become tied to
the code. Code is not emotional. It is logical through and through. The
second thing that happens with personal perspectives is a lack of
instinct. When you approach another project to fix something or run the
tests and it is an exercise in teasing apart config files and debugging,
then you're coding with personal perspectives instead of a standard.
Your goal should be to have a code base where anyone familiar with one
application can automatically do things like run tests, start
servers/daemons, add logging (print statements) and deploy to production
any other application. This kind of familiarity and standard allows for
instincts to develop. Instead of wrestling with understanding the meta
data (testing, deployment, debugging), people working on the code can
focus on the purpose of the application. They have a bug report and it
is a matter of grepping the source, adding some logging to do some
introspection and fixing the bug instead of understanding the different
test runner or build script that is used to create a package.
I'm not saying that people should code like robots or anything else
that sounds extreme and stale. Rather, I'm pointing out that your
personal preferences should take a back seat to the goals of the code.
If an application is going to be thrown away, then sure, rigging up your
own test harness to do something is totally fine. The start up with two
developers shouldn't feel bad they haven't settled on a test framework
or deployment strategy that considers applications written outside of
their core language. But if you are debugging code someone else wrote,
then you have hit the point where you should have some standards that
help move the code to a higher level among developers. We use langauges
like Python and Ruby (and even Java) because it hides a lot of
complexity that doesn't help us get the job done, yet when we consider
testing, deployment and debugging, our opinions matter most. Adding
standards for the common development practices is like adding memory
management and garbage collection, it lets you stop focusing on the
lower level details so you put your focus higher up the conceptual
ladder. The result is better code.
By the way, regarding my critique of our recent code review and it
revealing a symptom of a problem, it is something we're in the process
of fixing. Hindsight is 20/20 and we realize we could have made some
better decisions earlier on that would have helped avoid the
discrepancies between projects, but we didn't at the time. Fortunately,
it is never too late to change and change is exactly what we're doing!


.. author:: default
.. categories:: code
.. tags:: programming, testing
.. comments::
