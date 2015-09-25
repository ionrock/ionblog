Create a CI System
==================

At `work <http://rackspace.com>`_ we're putting together a bunch of
infrastructure for running `Designate
<http://docs.openstack.org/developer/designate/index.html>`_ in
production. Part of that process is getting our CI/CD system in
place.

Jenkins
-------

We're using Jenkins for running our tests and building artifacts (aka
deliverables). I've never been a huge fan of Jenkins as it always felt
a little kludgy integrating projects. Tools like `travis
<https://travis-ci.org/>`_ and `circle ci <https://circleci.com/>`_
make it so easy to get a project up and running, the idea of writing a
bunch of XML or clicking around the Jenkins UI felt pretty
painful. What makes managing jobs so much easier is `Jenkins Job
Builder (JJB) <http://ci.openstack.org/jenkins-job-builder/>`_. JJB
allows writing jobs in YAML that feels much more manageable.

The basic workflow is:

 1. Keep your job builder YAML files in a repo
 2. Add new YAML files for projects
 3. Run jjb to update Jenkins

While it is still not as easy as travis or circle, it makes things
much easier. It also wouldn't take much to include a `.jenkins.yaml`
in a repo and write a script to pull in all the jobs from different
projects.


Artifacts
---------

When you "build" your software, there are tons of options for the
resulting artifact. You can deploy containers, python packages, rpms,
debs, and pretty much everything inbetween. We settled on using
`dh-virtualenv
<http://dh-virtualenv.readthedocs.org/en/latest/>`_. `dh-virtualenv`
will build a deb composed from a virtualenv where you app is
installed. The deb installs the virtualenv in
`/usr/local/share/<name>`, at which point you can start whatever app
you need to using the appropriate path.

Once you have an artifact there are some options as to what you do
with it. We've decided on deploying the deb to a staging apt repo. It
lands in a `test` area where it can be tested separately. From there
the CI can start moving the artifact through different `staging` and
`prod` apt repos, running different suites of tests on the artifact
along the way to ensure everything looks good.


Releasing
---------

Once our artifact is good to go and passes all the necessary tests, it
can be released to the production environment. Here we are doing a
pretty standard process of spinning up a new version of the app and
pressing a button to switch over. The old environment stays around
until the new version is considered stable, at which point the old
environment gets shut down.


Automation
----------

This entire process is built on a couple triggers. When upstream
changes land, we pull those in and start the process of testing
things. We also have to include any patches that we need applied, that
may not have been merged just yet. We then need to apply any org
specific patches. This process of merging upstream with patches and
merging again with org specific patches is pretty difficult to
automate. I don't know that we have a good answer, but we do have some
tactics we're hoping make the process more manageable. The biggest
target is to make sure org specific hooks are included via managed
interfaces provided by the upstream code.

Conclusions
-----------

There are a few big takeaways:

 1. As a contributor, you are responsible for maintaining the CI
    system
 2. Automate and encapsulate many steps in to single logical steps
 3. ...


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
