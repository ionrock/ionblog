Virtual Machine Development
===========================

I've recently started developing on OS X again on software that will
be run on Linux. The solution I've used has been to use a Vagrant VM,
but I'm not entirely happy with it. Here are a few other things I've
tried.

Docker / Fig
------------

On OS X, `boot2docker <http://boot2docker.io/>`_ makes it possible to
use `docker <http://docker.io>`_ for running processes in
containers. `Fig <http://fig.sh>`_ lets you orchestrate and connect
containers.

.. note::
   Fig is deprecated and will be replaced with `Docker Compose
   <http://docs.docker.com/compose/>`_, but I found that Docker
   Compose didn't work for me on OS X.

The idea is that you'd run MySQL, RabbitMQ, etc. in containers and
expose those processes' ports and hosts to your app container. Here is
an example:

.. code-block:: yaml

   mysql:
     image: mysql:5.5

   app:
     build: path/to/myapp/  # A Dockerfile must be here
     links:
       - mysql

The app container then can access `mysql` as a host in order to get to
the container running MySQL.

While I think this pattern could work, I found that it needs a bit too
much hand holding. For example, you explicitly need to make sure
volumes are set up for each service that needs persistence. Doing the
typical database sync ended up being problematic because it wasn't
trivial to connect. I'm sure I was doing it wrong along the way, but
it seems that you have to constantly tweak any tutorial because you
have to use boot2docker.

Docker Machine
--------------

Another tactic I used was docker-machine. This is basically how
boot2docker works. It can start a machine, configured by docker, and
provide you commands so you can run things on that machine via the
normal docker command line. This seemed promising, but in the end, it
was pretty much the same as using Vagrant, only a lot less
convenient.

I also considered using it with my Rackspace account, but, for
whatever reason, the client couldn't destroy machines, which made it
much less enticing.


Vagrant
-------

One thing that was frustrating with Vagrant is that if you use a
virtualenv that is on part of the file system that is mounted from the
host (ie OS X), doing any sort of package loading is really slow. I
have no clue why this is. I ended up just installing things as root,
but I think a better tactic might be to use virtualenvwrapper, which
should install it to the home directory, while code still lives in
`/vagrant/*`.

One thing that I did do initially was to write a `Makefile` for
working with Vagrant. Here is a snippet:

.. code-block:: make

   SRC=/vagrant/designate
   VENV=/usr/local
   SPHINX=$(VENV)/bin/sphinx-build
   VCMD=vagrant ssh -c

   bootstrap:
	$(VCMD) 'virtualenv $(VENV)'
	$(VCMD) 'cd $(SRC) && $(VENV)/bin/pip install -r requirements.txt -r test-requirements.txt'
	$(VCMD) 'cd $(SRC) && $(VENV)/bin/python setup.py develop'

   tests:
	$(VCMD) 'cd $(SRC) && $(VENV)/bin/tox'

It is kind of ugly, but it more or less works. I also tried some other
options such as using my `xe <https://github.com/ionrock/xe>`_ package
to use `paramiko <http://docs.paramiko.org/en/1.15/>`_ or `fabric
<http://fabfile.org>`_, but both tactics made it too hard to simply do
things like:

.. code-block:: bash

   $ xe tox -e py27

And make `xe` figure out what needs to happen to run the commands
correctly on the remote host. What is frustrating is that docker
managed to essentially do this aspect rather well.


Conclusions
-----------

OS X is not Linux. There are more than enough differences that make
developing locally really difficult. Also, most code is not meant to
be portable. I'm on the fence as to whether this is a real problem or
just a fact of life with more work being done on servers in the
cloud. Finally, virtualization and containers still need tons of
work. It feels a little like the wild west in that there are really no
rules and very few best practices. The potential is obvious, but the
path is far from paved. Of the two, virtualization definitely feels
like a better tactic for development. With that in mind, it would be
even better if you could simply do with Vagrant what you can do with
docker. Time will tell!

Even though I didn't manage to make major strides into a better dev
story for OS X, I did learn quite a bit about the different options
out there. Did it make me miss using Linux? Yes. But I haven't given
up yet!

.. author:: default
.. categories:: code
.. tags:: docker, vagrant, virtualization, cloud, linux, devops
.. comments::
