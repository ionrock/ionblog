Back to Pytest
##############

My short trip into nose has become something of an uneventful
exploration into basically the same thing as pytest. This is not a bad
thing because it means I don't feel my investment into pytest is a waste
and that there was something obviously better out there. That doesn't
meant there isn't something better, but I feel a little more confident
saying that it is not nose.
None of this is to prescribe pytest or nose the winner. In fact, both
definitely have their flaws and neither really differentiate themselves
enough to warrant zealots. We're talking about test runners here. It is
not they are editors! Did I mention Emacs rules and Vim sucks? I kid.
I did learn one pattern that I will probably try migrating over to
pytest. My issue (as I mentioned the other day) with my development
server concept is that you really end up having to start it out of band
because having one command ends up being too much of a hassle. The
development server really needs more maintenance than a simple script
can provide to start and stop. This is why we have tools like monit,
init and the whole host of other process management tools out there.
Obviously all the PHP devs out there don't have a problem running Apache
and some database, so I'm going to call YAGNI on this one and just focus
on making the tests faster.
What I can do in my test runner is check for running services and start
them via the development service if they are available. This was
actually really easy to do in the test runner and was efficient in
between test runs. There is still the issue of setup / teardown for
fixture data, but so far that hasn't been a problem. I'm assuming this
is because most tests are rather explicit in this regard. After all,
just because some database is up and running, it doesn't mean that it
also has all your test data too. You always need fresh data.
The other gap I'd like to jump is how to make the transition from a
"development" server to a "production" server. How can I take this idea
and make production ready?
My first step is to continue to focus on the tests. I don't want to
become mired in the details of how to install apps or upgrade software.
Instead, we'll stick with how I can start/restart/stop applications and
update configurations in a way that is atomic and simple. Installation
of new software is really an orthogonal problem that when you stop
conflating with configuration changes becomes much simpler.
Unfortunately, my experiences have been with systems that do both more
or less at the same time, so it has been a tough lesson to realize.
As an aside, are there other test runners out there that warrant some
exploration? Same goes for continuous integration. The fact everyone
seems to just use Jenkins really makes me think the problem could be
solved differently.


.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
