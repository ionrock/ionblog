Announcing AutoRebuild
######################

At work we've started using `sass`_ for our CSS. The developer actually
working on the code asked if we had a good way to rebuild the CSS when
the sass file changed. I said no, but it would be really easy to write a
CherryPy plugin for it.

`AutoRebuild`_ is that plugin.

AutoRebuild will let you configure a set of glob patterns and watch the
files for changes. If they change, it will trigger a function to be
called. It is up to you to write the function, but the README provides
an example of how you configure a function to call make.

This plugin is really simple, but that is really the point. CherryPy
makes it really easy to add integration points so working with other
services and tools is easy and automated.

.. _sass: http://sass-lang.com
.. _AutoRebuild: http://bitbucket.org/elarson/autorebuild


.. author:: default
.. categories:: code
.. tags:: cherrypy, programming, python
.. comments::
