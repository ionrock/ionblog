Coupling and Cohesion in an Organization
########################################

At work we have a team that is trying to make our deployments better.
They are taking cues from the `12 Factor App`_ model. Generally, I
believe this model provides a great start for designing your
applications in terms of deployment. The one caveat is that you may be
missing out some cohesion in your organization by assuming it is
coupling.
The 12 Factor App was written by the fine folks at `Heroku`_. Heroku is
an application hosting platform that supports a variety of runtimes.
This is important because it means that Heroku's use case is more
generalized than most organizations. In order to support different
runtimes consistently, there must be a lowest common denominator that
works for all runtimes. Having this kind of generic requirement is not a
negative, but it suggests that you are avoiding coupling that may not be
necessary in an organization.
A good example of this is logging. The 12 Factor App defines that all
logging should be a stream of events that are logged to stdout.
Obviously, if you are supporting multiple runtimes, demanding a specific
logging platform is suboptimal. The language may not support the logging
platform or some libraries might be dependent on other platform specific
details. For example, supporting syslog could be done via the C library
or simply calling the local syslog command in a process. Requiring an
application log to a specific tool is an example of negative coupling
for Heroku, but that doesn't have to be the case in an organization.
A company that has control over its own deployment platform can very
easily support a more specific logging system such as syslog. Using
tools like puppet or chef, each host can meet any requirements necessary
for the specific runtimes. Similarly, you are not tasked with inventing
a system of log management as tools like syslog already have that
functionality built in. More generally, you can separate management of
logs from application development because you have a powerful tool you
can depend on to be present. In one sense you are coupling yourself to a
logging system, but in another sense, you really are finding a cohesive
tool that makes things simpler across an organization.
Often times as developers we try to make solutions that are generic in
order to meet needs now and in the future. Preparing for the future is a
good idea, but it is always important to recognize when a generic
solution is adding unnecessary complexity that doesn't help the
organization meet its needs. Coupling and cohesion are abstract concepts
that change based on context. When you can set up a simple, seemingly
highly coupled system, and it works with no problems for the next 5
years, then I'd argue that coupling was helpful in creating a cohesive
solution.

.. _12 Factor App: http://www.12factor.net/
.. _Heroku: http://heroku.com


.. author:: default
.. categories:: code
.. tags:: devops, programming, python, sysadmin
.. comments::
