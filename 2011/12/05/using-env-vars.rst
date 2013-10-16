Using Env Vars
##############

Someone at work mentioned `The Twelve Factor App`_ in our IRC topic. It
is a great read as it simply and concisely states the current general
best practices for writing a distributed app.

One thing that did confuse though was the mention of Environment
Variables for configuration. Here is what it said:

    **The twelve-factor app stores config in environment variables**
     (often shortened to env vars or env). Env vars are easy to change
     between deploys without changing any code; unlike config files,
     there is little chance of them being checked into the code repo
     accidentally; and unlike custom config files, or other config
     mechanisms such as Java System Properties, they are a language- and
     OS-agnostic standard.

The idea of using env vars as a means of passing configuration
information makes sense in a general case. But, if you application has
more complicated configuration, it seems like it could be somewhat
daunting.

That is just my initial impression coming from a YAML based
configuration system. After taking a look at our production
configuration I could see how most details could be reflected as
traditional env vars. Where things do become more complicated it seems
reasonable to consider moving that information to a service.

As a though experiment, I'm going to consider moving some of our
configuration to env vars to see if it feels reasonable. Starting off,
the vast majority of values seem like they could easily be migrated to
prefixed variable names. As we do use YAML, we have some dictionary and
list structures. The lists seem easy enough to parse as strings. For
example:

::

    # set the env var as JSON
    import os
    os.environ['APP_HOSTS'] = '["123.45.22.3", "123.45.22.8", "123.45.22.10"]'

    # load the env var
    import json
    hosts = json.loads(os.environ['APP_HOSTS'])

While JSON seems like it might be somewhat heavy handed, it is important
to have some standard otherwise you'd end up seeing lots of code that
looks like:

::

    hosts = os.environ['APP_HOSTS'].split()

Maybe this paradigm is totally fine. I would imagine it could break down
though depending on the values and if they needed spaces.

For dictionaries it seems looking at our config that most could, and
probably should, be moved to some service. It is still possible to use
something like JSON, but again, I think that might prove cumbersome in
some situations. Writing raw JSON in a BASH script might be rough. I'm
also noticing that many times a dictionary really is more of a visual
organizing tool. It is possible to flatten the dictionary using an
obvious delimiter that could be used to expand things later if need be.

Here is an example:

::

    conf = {
        'csv': {'extra': {'repair': True, 'delimiter': '|'},
                'type': 'text/csv'},
        'xml': {'extra': {'xsl': 'http://host/path/to/foo.xsl'},
                'type': 'text/xml'}
    }

This might be flattened in the env vars as the following:

::

    APP_CSV_EXTRA_REPAIR = True
    APP_CSV_EXTRA_DELIMITER = "|"
    APP_CSV_TYPE = "text/csv"

    APP_XML_EXTRA_XSL = "http://host/path/to/foo.xsl"
    APP_XML_TYPE = "text/xml"

What we need to do is take this kind of configuration and use it via env
vars to configure a download service. Here is one option:

::

    class DownloadService(object):
        @classmethod
        def from_env(cls, type):
            kwargs = {}

            vkey = ('app_%s' % type).upper()
            for key, value in os.environ.iteritems():
                if key.startswith(vkey + '_EXTRA'):
                    kwargs[key.split('_', 3).lower()] = value

            kwargs['headers'] = {'Content-Type': os.environ['APP_%s_TYPE' % type.upper()]}

            return cls(**kwargs)

Offhand it feels a little bit kludgy, but I think the reality is that it
is not that complicated. The fact I wrote this method inline in a minute
or two suggests that wasting any more time to something cleaner is
probably just a waste of time.

In summary, it seems pretty reasonable to define configuration via
environment variables. One concern is that keeping the configuration for
development and testing might be cumbersome at times. But with that in
mind, there is no reason one couldn't keep them in a YAML or JSON or
even Python and simply generate them on the fly when you run the
application. I've also found at times using environment variables can be
tricky with scripts where I preferred to use command line flags. My gut
tells me that the real issue is that I'm not doing the right thing
wrapping some script or configuring how it is run.

I hope this exercise has been somewhat helpful. Obviously a complex
configuration is going to end up with pretty massive set of environment
variables. The gut reaction might be that it seems sloppy or that it
will become too complex. This might very well be true, but I have a
feeling it can be pretty easily managed. Writing a simple YAML to env
var script would be pretty trivial. Maintaining a global namespace of
env var names is effectively what Emacs does and I can say from
experience that while the namespace has become huge over the years, I've
never hit a collision.

.. _The Twelve Factor App: http://twelve-factor.herokuapp.com/


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
