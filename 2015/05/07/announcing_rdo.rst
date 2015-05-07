Announcing rdo
==============

At `work <https://rackspace.com>`_ I've been using `Vagrant
<https://vagrantup.com>`_ for development. The thing that bothers me
most about using Vagrant or any remote development machine is the
disconnect it presents with local tools. You are forced to either
login into the machine and run command or jump through hoops to run
the commands from the local machine, most often times losing the file
system context that make the local tools possible.


Local Tools
-----------

What I mean by local tools are things like IDEs or build code that
performs tasks on your repository. IDEs assume you are developing
locally and expect a local executable for certain tasks in order to
work. Build code can be platform specific, which is likely why you are
using Vagrant in the first place.

My answer to this is `rdo <https://github.com/ionrock/rdo>`_.


Why `rdo`
---------

I have a similar project called `xe` that you can configure to sort
out your path when in a specific project. For example, if I have a
`virtualenv <https://virtualenv.pypa.io/en/latest/>`_ `venv`, in my
cloned repo, I can use `xe python` to run the correct python without
having to activate the virtualenv or manually include the path to the
python executable.

`rdo` works in a similar way, the difference being that instead of
adjust the path, it configures the command to run on a remote machine,
such as a Vagrant VM.


Using `rdo`
-----------

For example, lets assume you have a `Makefile`
in your project repo. You've written a `bootstrap` task that will
download any system dependencies for your app.

.. code-block:: Makefile

   bootstrap:
   	sudo apt-get install -y python-pip python-lxml

Obviously if you are on OS X or RHEL, you don't use `apt` for package
management, and therefore use a Vagrant VM. Rather than having to
`ssh` into the VM, you can use `rdo`.

The first step is to create a config file in your repo.

.. code-block:: ini

   [default]
   driver = vagrant
   directory = /vagrant

That assumes you're `Vagrantfile` is mounting your repo at
`/vagrant`. You can change it as needed.

From there you can use `rdo` to run commands.

.. code-block:: bash

   $ rdo make bootstrap

That will compose a command to connect to the vagrant VM, `cd` to the
correct directory and run your command.


Conclusion
----------

I hope you give it a try and report back any issues. At the moment it
extremely basic in that it doesn't do anything terribly smart as far
as escaping goes. I hope to remedy that as well as support generic ssh
connections as well.


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
