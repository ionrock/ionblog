Build Tools
===========

I've recently been creating more new projects for small libraries /
apps and its got me thinking about build tools. First off, "build
tools" is probably a somewhat misleading name, yet I think it is most
often associated with type of tools I'm thinking of. Make is the big
one, but there are a whole host of tools like Make on almost every
platform.

One of the `apps <https://github.com/ionrock/dadd>`_ I've been working
on is a `Flask <http://flask.poocoo.org>`_ application. For the past
year or so, I've been working on a `Django
<http://djangoproject.org>`_ app along side some `CherryPy
<http://cherrypy.org>`_ apps. The interesting thing about these
different frameworks is the built in integration with some sort of
build tool.

CherryPy essentially has no integration. If you unfamiliar with
CherryPy, I'd argue it is the un-opinionated web framework, so it
shouldn't be surprising that there are no tools to stub out some
directories, provide helpers for connecting to the DB and starting a
shell with the framework code loaded.

Flask is similar to CherryPy in that it is a microframework, but the
community has been much more active providing plugins (Blueprints in
Flask terms) that provide more advance functionality. `One such plugin
<http://flask-script.readthedocs.org/en/latest/>`_, mimics Django's
manage.py file, which provides typical build tool and project
helpers.

Django, as I just mentioned, provides manage.py file that adds some
project helpers and, arguably, functions as a generic build tool.

I've become convince that every project should have some sort of build
tool in place that codifies how to work with the project. The build
tool should automate how to build and release the software, along with
how that process interacts with the source control system. The build
tool should provide helpers, where applicable, to aid in development
and debugging. Finally, the build tool should help in running the apps
processes, and/or supporting processes (ie make sure a database is up
and running).

Yet, many projects don't include these sorts of features. Frameworks,
as we've already seen, don't always provide it by default, which is a
shame.

I certainly understand why programmers avoid build tools, especially
in our current world where many programs don't need an actual
"build". As programmers, we hope to create generalized solutions,
while we are constantly pelted with proposed productivity gains in the
form of personal automations. The result is that while we create
simple programs that guide our users toward success, when it comes to
writing code, we avoid prescribing how to develop on a project as if
its a plague that will ruin free thinking.

The irony here is that Django, the framework with a built in build
tool, is an order of magnitude more popular. I'm confident the reason
for its popularity lies in the integrated build tool, that helps
developers find success.

At some point, we need to consider how other developers work with our
code. As authors of a codebase, we should consider our users, our
fellow developer, and provide them with build tools that aid in
working on the code. The goal is not to force everyone into the same
workflow. The goal is to make our codebases usable.



.. author:: default
.. categories:: code
.. tags:: python, make, build tools, paver, invoke
.. comments::
