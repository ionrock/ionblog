Flask vs. CherryPy
==================

I've always been a fan of CherryPy_. It seems to avoid making decisions for you
that will matter over time and it helps you make good decisions where
it matters most. CherryPy is simple, pragmatic, stable fast enough and
plays nice with other processes. As much as I appreciate what CherryPy
offers, there is unfortunately not a lot of mindshare in the greater
Python community. I suspect the reason CherryPy is not seen a hip
framework is due to most users of CherryPy happily work around the
rough edges and get work done rather than make an effort market their
framework of choice. Tragic.

While there are a lot of microframeworks out there, Flask_ seems to be
the most popular. I don't say this with any sort of scientific
accuracy, just a gut feeling. So, when I set out to write a different
kind of `process manager <https://github.com/ionrock/dadd>`_ , it seemed
like a good time to see how other microframeworks work.

The best thing I can say about Flask is the community of
projects. After having worked on a Django project, I appreciate the
admin interface and how easy it is to get 80% there. Flask is
surprisingly similar in that searching google for "flask + something"
quickly provides some options to implement something you want. Also,
as Flask generally tries to avoid being too specific, the plugins
(called Blueprints... I think) seem to provide basic tools with the
opportunity to customize as necessary. `Flask-Admin
<http://flask-admin.readthedocs.org/en/v1.0.9/>`_ is extremely helpful
along side `Flask-SQLAlchemy
<http://pythonhosted.org/Flask-SQLAlchemy/>`_.

Unfortunately, while this wealth of excellent community packages is
excellent, Flask falls short when it comes to actual development. Its
lack of organization in terms of dispatching makes organizing code
feel very haphazard. It is easy to create circular dependencies due to
the use of imports for establishing what code gets called. In essence,
Flask forces you to build some patterns that are application specific
rather than prescribing some models that make sense generally.

While a lack of direction can make the organization of the code less
obvious, it does allow you to easily hook applications together. The
Blueprint model, from what I can tell, makes it reasonably easy to
compose applications within a site.

Another difficulty with Flask is configuration. Since you are using
the import mechanism to configure your app, your configuration must
also be semi-available at import time. Where this makes things
slightly difficult is when you are creating a app that starts a web
server (as opposed to an app that runs a web service). It is kind of
tricky to create `myapp --config` because by the time you've started
the app, you've already imported your application and set up some
config. Not a huge issue, but it can be kludgy.

This model is where CherryPy excels. It allows you create a stand
alone process that acts as a server. It provides a robust
configuration mechanism that allows turning on/off process and request
level features. It allows configuration per-URL as well. The result is
that if you're writing a daemon or some single app you want to run as
a command, CherryPy makes this exceptionally easy and clear.

CherryPy also helps you stay a bit more organized in the framework. It
provides some helpful dispatcher patterns that support a wide array of
functionality and provide some more obvious patterns for organizing
code. It is not a panacea. There are patterns that take some getting
used to. But, once you understand these patterns, it becomes a
powerful model to code in.

Fortuately, if you do want to use Flask as a framework and CherryPy as
a process runner / server, it couldn't be easier. It is trivial to run
a Flask app with CherryPy, getting the best of both worlds in some
ways.

While I wish CherryPy had more mindshare, I'm willing to face facts
that Flask might have "won" the microframework war. With that said, I
think there are valuable lessons to learn from CherryPy that could be
implemented for Flask. I'd personally love to see the process bus
model made available and a production web server included. Until then
though, I'm happy to use CherryPy for its server and continue to enjoy
the functionality graciously provided by the Flask community.


.. author:: default
.. categories:: code
.. tags:: python, cherrypy, flask
.. comments::

.. _CherryPy: http://cherrypy.org
.. _Flask: http://flask.pocoo.org/
