Deep CherryPy
#############

My first experiences with Python web development was with `CherryPy`_. I
did the Hello World and that was pretty much it. It didn't strike me as
that compelling at the time so I moved on. Later I tried `Rails`_ and it
made a ton of sense. At the time I also was doing some Python for school
and really liked the language. When I finally got a job out of school,
Python was the preference of the two and I started looking more for web
frameworks like Rails. `Django`_ and `TurboGears`_ were brand spankin
new and of the two I liked TurboGears the best. What struck me though
was that most of TurboGears was really just extra fluff on CherryPy.

Once again, I started playing around with CherryPy. For whatever reason,
I still wasn't entirely satisfied. I ended up going with `web.py`_ for a
time and enjoyed it. Then I stuck to raw `WSGI`_. Of course, when I
looked for a server I ended back on CherryPy's.

Now, I work at a job where I work with CherryPy every day and honestly,
things couldn't be better. Every time I take a peak over the fence at
other frameworks and tools it never ends up having the right balance of
features to flexibility like CherryPy. I'll often hit some bug or
limitation that isn't in CherryPy. There will be some moment where the
model this framework wants to use just doesn't really fit. It has
happened every single time and now, I don't really look very often.

I did stumbled on this framework for Ruby called `Renee`_. What struck
me was that it was essentially like my transitions between TurboGears,
web.py and CherryPy. Each had a different model for how the application
should be written. CherryPy gives you flexibility to do all the above.

First you start with Rails where you define routing via a central file.

This is how Django works and how `Pylons`_ (now Pyramid) used to work.

In CherryPy you can mimic that behavior with the following:

    ::

        import cherrypy
        from my_controllers import *

        urls = cherrypy.dispatch.RoutesDispatcher()
        d.connect('main', '/', HomePage())
        d.connect('blog', '/blog/:year/:month/:day/:slug', BlogPage())

This model can be really powerful but there is also a subtle disconnect
at times. Often times you want to not only dispatch on the URL path, but
also on the HTTP method. Web.py had a similar model where you would
define your routes, and then have a class handle that request based on
the method. Here is how you can do that in CherryPy:

    ::

        import cherrypy
        from myapp import models

        class MyHandler(object):

            exposed = True

            def GET(self):
                params = {'error': cherrypy.session.last_error}
                cherrypy.session.last_error = None
                return render('myhandler.tmpl', params=params)

            def POST(self, **kw):
                '''The **kw are the submitted form arguments'''
                try:
                    models.foo.update(kw)
                except InvalidData as e:
                    cherrypy.session.last_error = e
                raise cherrypy.redirect(cherrypy.request.path_info)

        d = cherrypy.dispatch.MethodDispatcher()
        conf = {'/': {'request.dispatch': d}}
        cherrypy.tree.mount(MyHandler(), '/foo', conf)

This is nice, but what happens if you want to mix and match the models.

Here is an example:

    ::

        import cherrypy
        from myapp import controllers
        from myapp import urls

        d = cherrypy.dispatch.MethodDispatcher()

        method_conf = {'/': {'request.dispatch': d}}
        routes_conf = {'/': {'request.dispatch': urls}} # routes dispatcher
        cherrypy.tree.mount(controllers.APIHandler(), '/api', method_conf)
        cherrypy.tree.mount(None, '/app', routes_conf)

In this example, I've mixed to models in order to use the model that
works best for each scenario.

With all that said, what I've found is that the more specialized
dispatchers often are unnecessary. The CherryPy default tree dispatch is
actually really powerful and can easily be extended to support other
models. I think this is the real power of CherryPy. You have a great set
of defaults that allows customizing via plain old Python along side a
fast and stable server.

There are obviously some drawbacks in that if you application is going
to keep open many long connections, then you will use up all the
available threads since CherryPy uses a traditional thread per request
model. There is the slim chance you'll run into the GIL as well if you
are doing rather extreme processing for each request since it is using
Python threading. With that said, these limitations are really easy to
work around. You can start more than one CherryPy server and use a load
balancer quite easily. For processing intensive tasks you can obviously
fork off different processes/threads as needed. CherryPy even includes
an excellent bus implementation that makes orchestrating processes
somewhat straightforward. In fact, it is what I use for my test/dev
server implementation.

CherryPy may never be the hippest web framework around, but that is OK
by me. I use Python because it helps me to get things done. Other web
frameworks have some definite benefits, but CherryPy always seems to
help me get things done quickly using a stable foundation. If you've
never checked it out, I encourage you to take a look. The repository
just moved to `BitBucket`_ as well, so feel free to fork away and take a
closer look at the internals.

.. _CherryPy: http://cherrypy.org
.. _Rails: http://rubyonrails.com
.. _Django: https://www.djangoproject.com/
.. _TurboGears: http://turbogears.org/
.. _web.py: http://webpy.org
.. _WSGI: http://www.python.org/dev/peps/pep-0333/
.. _Renee: http://reneerb.com/
.. _Pylons: http://www.pylonsproject.org/
.. _BitBucket: https://bitbucket.org/cherrypy/cherrypy/wiki/Home


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
