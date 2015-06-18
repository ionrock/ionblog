Announcing: Withenv
===================

I wrote a tool to help sanely manage environment
variables. Environment Variables (env vars) are a great way to pass
data to programs because it works practically everywhere with no set
up. It is a lowest common denominator that almost all systems support
all the way from dev to production.

The problem with env vars is that they can be sticky. You are in a
shell (zsh, bash, fish, etc...) and you set an environment
variable. It exists and is available to every command from then
on. If an env var contains an important secret such as a cloud account
key, you could silently delete production nodes by mistake. Someone
else could use your computer and do the same thing, with or without
malicious intent.

Another difficulty with env vars is that they are a global key value
store. Writing small shell scripts to export environment variables can
be error prone. Copying and pasting or commenting out env vars in
order to configure a script is easy to screw up. The fact these env
vars are long lasting only makes it more difficult to automate
reliably.

`Withenv <http://github.com/ionrock/withenv>`_ tries to improve this
situation by providing some helpful features:

 - Setup the environment for each command without it leaking into your
   shell
 - Organization of your environment via YAML files
 - Cascading of your environment files in order to override
   specific values
 - Debugging the environment variables

Here is how it works.

Lets say we have a script that starts up some servers. It uses some
environment variables to choose how many servers to spin, what cloud
account to use and what role to configure them with (via
Chef or Ansible or Salt, etc.). The script isn't important, so we'll
just assume `make create` does all the work.

Lets organize our environment YAML files. We'll create a `envs` folder
that we can use to populate our environment. It will have some
directories to help build up an environment.

.. code-block:: bash

   envs
   ├─ env
   │  ├─ dev
   │  └─ prod
   └─ roles
      ├─ app-foo
      └─ app-bar

Now we'll add some YAML files. For example, lets create a YAML file
in the `envs/env/dev` that connects to a development account.

.. code-block:: yaml

   # envs/env/dev/rax_creds.yml
   ---
   - RACKSPACE:
     - USERNAME: eric
     - API_KEY: 02aloksjdfp;aoidjf;aosdijf

You'll notice that we used a nested data structure as well as
lists. Using lists ensure we get an explicit ordering. We could have
used a normal dictionary as well if the order doesn't matter. The
nesting ensures that each child entry will use the correct prefix. For
example, the YAML above is equivalent to the following bash script.

.. code-block:: bash

   export RACKSPACE_USERNAME=eric
   export RACKSPACE_API_KEY=02aloksjdfp;aoidjf;aosdijf


Now, lets create another file for defining some object storage info.

.. code-block:: yaml

   # envs/env/dev/cloud_storage.yml
   ---
   - STORAGE_BUCKET: devstore
   - STORAGE_PREFIX: $STORAGE_BUCKET/dev


You'll notice that the `STORAGE_PREFIX` uses the value of the
`STORAGE_BUCKET`. You can do normal dollar prefixed replacements like
you would do normally in an shell. This includes any variables
currently defined in your environment such as `$HOME` or `$USER` that
are typically set. Also, by using a list (as defined by the `-`), we
ensure that we apply the variables in order and the `STORAGE_BUCKET`
exists for use within the `STORAGE_PREFIX` value.

With our environment YAML in place, we can now use the `we` command
`withenv` provides in order to set up the environment before calling a
command.

.. code-block:: bash

   $ we -e envs/common.yml -d envs/env/dev -d envs/role/app-foo make create

The `-e` flag lets you point to a specific YAML file, while the `-d`
flag points to a directory of YAML files. The ordering of the flags is
important because the last entry will take precedence. In the command
above, we might have configured `common.yml` with a personal dev
account along with our defaults. The `envs/env/dev/` folder contains a
`rax_creds.yml` file that overrides the default cloud account with
shared development account, leaving the other defaults alone.

The one limitation is that you cannot use the output from commands as
a value to an env var. For example, the following wouldn't work to set
a directory path.

.. code-block:: yaml

   CONFIG_PATH: `pwd`/etc/foo/

This might be fixed in the future, but at the moment it is not
supported.

If you don't pass any argument to the `we` command it will output he
environment as a bash script using `export` to set variables.

`Withenv <https://github.com/ionrock/withenv` is available on `pypi
<https://pypi.python.org/pypi/withenv>`_. Please let me know if you
give it a try.

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
