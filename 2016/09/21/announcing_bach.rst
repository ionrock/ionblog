Announcing Bach
===============

A while back I wrote a tool called `withenv
<https://github.com/ionrock/withenv>`_ to help manage environment
variables. My biggest complaint with systems that depend on
environment variables is that it is really easy for the variables to
be sticky. For example, if you use `docker-machine
<https://docs.docker.com/machine/>`_ or `docker swarm
<https://docs.docker.com/engine/swarm/>`_, you need to be very careful
that your environment variables are configured or else you could be
using the wrong connection information.

Another change for me recently has been using `Go
<https://golang.org/>`_ regularly. I've found the language to be easy
to learn (coming from Python), fast and a lot of fun on the type of
problems I've been solving at work.

So, with some existing tooling around that I'd wanted to improve upon
and with some new ideas in tow, I started writing `Bach
<https://github.com/ionrock/bach>`_.

The basic idea is that Bach helps you orchestrate your process
environment. While it is a clever name, I don't know that it really
make clear what the bach tools are meant to do, so I'll try to clarify
why I think these tools can be helpful.

Say we have an web application that we want to run on 3 nodes with a
database and load balancer. The application is pretty old, meaning it
was written with the intent to deploy the app on traditional bare
metal servers. Our goal is to take our app and run it in the cloud on
some containers without making any major changes to the application.

When you start looking at containers and the cloud, it can be very
limiting to consider a world where you can't just ssh into the box,
make a configuration change and be done. Even when you use containers,
making the assumption the target platform will provide a way to
utilize volumes is a bit tricky. These limitations can be difficult to
work around without changing the code. For example, changing code that
previously wrote the file system to instead write to some service like
Amazon S3 is non-trivial and introduces a pretty big paradigm shift to
code and operations.

Bach, is meant to help provide tooling to make these sorts of
transitions easier such that the operations code base doesn't dictate
the developer experience, and vice versa. As a secondary goal, the
bach tools should be easy to run and verify independently of each
other, while working together in unison.

Going back to our example, lets think about how we'd configure our
application to run in our container environment. Lets assume that we
can't simply mount a config directory for our application and we need
to pass environment variables for configuration to a container. Our
app used to run with the following command.

.. code-block:: bash

   $ app --config /etc/app.conf

Unfortunately, that won't work now. Here is where the Bach tools can
be helpful.

First off, our application needs a database endpoint. We'll use
withenv (`we`) to find the URL and inject it in our environment before
starting our app. Lets assume we use some DNS to expose what services
live at what endpoints. Here is little script we might write to get
our database URL.

.. code-block:: bash

   #!/bin/bash

   # The environment will provide a SERVICES environment variable that
   # is the IP of DNS server that we use for service discovery. The
   # ENV_NAME is the name of the environment (test, prod, dev,
   # branch-foo, etc...)
   DBIP=`dig @$SERVICES +short db.$ENV_NAME.service.list`
   echo "{\"DBURI\": \"$DBIP\"}"

Now that we have the script we can use `we` to inject that into our
environment before running our app.

.. code-block:: bash

   $ we -s find-db.sh env | grep DBURI

Now that we know we are able to get our `DBURI` into our environment,
we still need to add it to our application's configuration. For that
we'll use `toconfig`. We use a simple template to write the config
before running our app.

.. code-block::

   [database]
   dburi = {{ DBURI }}

We can test this template by running the following command.

.. code-block::

   $ DBURI=mysql://1.2.3.4/foo toconfig --template app.conf.tmpl

This will print the resulting template for review.

With both these pieces in place, we can start to put things together.

.. code-block:: bash

   $ we -s find-db.sh \
     toconfig --template /etc/app.conf.tmpl \
              --config /etc/app.conf \
     app --config /etc/app.conf

Now, when we switch our command in our container to run the above
command, we get to run our app in the new environment without any code
changes while still capitalizing on new features the environment
provides.

If that command is a bit too long, we can copy the arguments to a YAML
file run it with the `bach` command.

.. code-block:: yaml

   # setup.yml
   ---
   - withenv:
     - script: find-db.sh
   - toconfig:
     template: /etc/app.conf.tmpl
     config: /etc/app.conf

Then our command becomes a bit shorter.

.. code-block:: bash

   $ bach --config setup.yml app --config /etc/app.conf

At the moment these are the only released apps that come with
Bach. With that said, I have other tools to help with different tasks:

 - present: This runs a script before and after a command exits. The
   idea was to automate service discovery mechanisms by letting the
   app join some cluster on start and leave when the process exits.

 - cluster: This provides some minimal clustering functionality. When
   you start an app, it will create a cluster if none exists or join
   one if it is provided. You can then query any member of the cluster
   to get the cluster state and easily pass that result into the
   environment via `we` and a script (ie `we -s 'cluster nodes
   192.168.1.14'`).

At the moment, the `withenv docs <https://withenv.readthedocs.org>`_
should be correct for Bach's `we` command. I'm still working on
getting documentation together for `toconfig` and the other tools, so
the source is your best bet for reference.

If you try any of the tools out, please let me know!

.. author:: default
.. categories:: code
.. tags:: golang, devops, python
.. comments::
