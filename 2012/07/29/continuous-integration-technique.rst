Continuous Integration Technique
################################

I'm going to start off by saying I've never set up a CI system, so my
perspective might be completely naive. With that out of the way…

I took a quick look at `BuildBot`_. I didn't really have a reason
outside of seeing a link on a blog while watching some logs. At work we
use `Jenkins`_ and since it is the only tool I've used, it seems to work
just fine. Yet, I always have a nagging feeling we're missing an
important aspect of CI.

In order to use Jenkins, we've created scripts that do things like build
an environment and get things ready for testing. The part that doesn't
sit well with me is the process of installing and running the tests in
the environment is completely different than our production system.
Sure, it uses Python and a virtualenv, but that is about it.

This disconnect between CI and a production deployment isn't terrible,
but it seems to suggest other problems. Why can't you use the same
deployment pattern to set up a test environment as your production
environments? What if your production is using easy\_install and your CI
is using pip? Are you definitely using the same repositories? What about
libraries that require building modules in C? Are details like
environment variables and library going to be the same in the production
environment as the CI?

It should be a goal to have a single starting point for running tests or
creating a built and running an application in production. By providing
the single, standard process of preparing an environment, you eliminate
any questions regarding things like correct library versions,
installation paths, dependency resolution, configuration questions, etc.
This goal is not always easy, but it will make your CI server a better
test that your code is really ready for deployment to production.

.. _BuildBot: http://trac.buildbot.net/
.. _Jenkins: http://jenkins-ci.org/


.. author:: default
.. categories:: code
.. tags:: devops, programming, testing
.. comments::
