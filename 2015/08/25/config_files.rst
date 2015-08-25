Config Files
============

In `Chef <https://www.chef.io/>`_, you can use `attributes
<https://docs.chef.io/attributes.html>`_ to set up values that you can
later use in your recipes. I suspect a majority of these attributes
end up in config files. For example, at `work
<https://rackspace.com>`_, we have added pretty much every value
necessary in our config files. The result is that we duplicate our
configuration (more or less) as a Ruby hash that gets serialized using
ERB templates into the necessary config, which, in this case, is a
conf file format. The other thing that happens is that we also set
many of these values via environment variables using `withenv
<https://github.com/ionrock/withenv>`_, which describes this data as
YAML.

Essentially, we go from YAML to Ruby to a template to a config file in
a known parsable format. The problem is that each time you transition
between data formats there is a chance for mistakes. As we all know,
`humans can make mistakes writing config files
<http://danluu.com/postmortem-lessons/>`_. It is worth considering how
we could improve the situation.

I imagine a tool that accepts YAML and spits out different config file
formats. YAML seems like a good option because it is arguably
ubiquitous and provides data structures that programmers like. The
tool to spit out a config file would use consistent patterns to output
formats like conf files and plugins would need to be written for
common tools like databases, web servers, queues, etc.

For example:

.. code-block:: bash

   $ ymlconf --format rsyslog rsyslog_conf.yml > /etc/rsyslog.conf

I'm sure there would be some weirdness for some apps archaic and silly
configuration file formats, but I'd hope that 1) the people using
these apps understand the archaic file format well enough that 2)
translating it to a YAML format wouldn't be that terrible. For apps
that do understand simple conf files, or even better, YAML or JSON or
environment variables, things can be a matter of simply writing the
files.

What's more, YAML is resonably programmatic. If you have a list of
nodes that need to repeat the same sections over a list of IPs you get
when you start up cloud servers, it is trivial to do in a chef
recipe. Rather than adding it to a data structure, only to decompose
and pass that data to a template, you just append them to a list in a
data structure read from YAML.

After using withenv, I think this is another way to greatly reduce the
cognitive mapping that is required to constantly go from some driving
data (like environment variables) to configuration management system
data structures (chef attributes) that are passed to a template
languages in order to write config files. Instead it would simply be a
matter of running some command and pass it the path or YAML as stdin
and be done with it.

.. author:: default
.. categories:: code
.. tags:: devops, ruby, python, chef, ansible, yaml, configuration management
.. comments::
