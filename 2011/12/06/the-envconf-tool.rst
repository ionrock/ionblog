The Envconf Tool
################

Continuing to think about using `env vars`_, it seems like a really easy
way to start using them would be to have a way of configuring them using
a file in development. For example, in our apps at work we traditionally
have some sort of a base config YAML file that keeps all our defaults.
The YAML format is pretty helpful in keeping things organized for
development but there is really no reason you couldn't use environment
variables.

Without further adieu, I wrote `envconf`_. It is really meant for
development where you have some configuration files and you want to read
and create env vars from them. It only supports YAML files and for lists
it uses JSON to create a more universally parseable value. I'm not crazy
about this list support, but one easy work around is to explicitly use a
string and parse it yourself. Not ideal, but probably good enough.

In theory if someone actually uses this and wants to use another config
format like .ini, JSON or some other format, it should be pretty easy to
add a new type. Implementing a different configuration type is a matter
of reading a file and returning a dict, which shouldn't be terribly
hard.

I should also mention that envconf doesn't overwrite anything currently
in the environment. The result is that you could layer things if you
wanted. Here is an example of how you could do it:

::

    envconf -c dev.yaml envconf -c base.yaml run-my-server

You could also just pass it in explicitly in your shell:

::

    APP_EXAMPLE=foo envconf -c base.yaml run-my-server

Unfortunately, I haven't had a chance to try it out at my job as we have
a semi-involved configuration pattern that would need to be adjusted and
I don't have the time. But hopefully I'll get a chance to give it a go.

.. _env vars: http://ionrock.org/blog/2011/12/05/Using_Env_Vars
.. _envconf: http://bitbucket.org/elarson/envconf


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
