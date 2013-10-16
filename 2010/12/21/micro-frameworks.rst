==================
 Micro Frameworks
==================

I came across `Bottle`_ today and thought it was kind of silly. Not in
the sense that the actual framework design or functionality is silly,
but rather that there are so many attempts to make stripped down
frameworks. There is really nothing wrong with making these frameworks.
I'm sure the authors learn a lot and they scratch an itch. Every time
one comes up though, I wonder about something similar built on
`CherryPy`_ and I'm reminded that CP is really the original
microframework and works even better than ever.

Even though CP has become my framework of choice, others may not
realize how it really is similar to the other micro frameworks out there
with the main difference being it has been tested in the real world for
years. Lets take a really simple example of templates and see how we can
make it easy to use `Mako`_ with CherryPy.

First off, lets write a little controller that will be our application.
I'm going to use the CP method dispatcher.


::

    import cherrypy

    class SayHello(object):
        exposed = True # the handler is exposed or else a 404 is raised. very pythonic!

        def GET(self, user, id):
            some_obj = db.find(user, id)
            return {
                'model': some_obj
            }

        def POST(self, user, id, new_foo, *args, **kw):
            updated_foo = SomeModel(user, id, new_foo)
            updated_foo.save()
            raise cherrypy.HTTPRedirect(cherrypy.request.path_info)

I've kind of stacked the deck a little bit here with my 'GET' method.
It is returning a dict because we are going to use that to pass info
into a render function that renders the template. There are many ways
you could do this, but since I like to reuse the template look up, I'll
make a subclass that includes a render function.


::

    import os
    import cherrypy
    import json

    from mako.template import Template
    from mako.lookup import TemplateLookup

    __here__ = os.path.dirname(os.path.abspath(__file__))

    class RenderTemplate(object):
        def __init__(self):
            self.directories = [
                os.path.normpath(os.path.join(__here__, 'view/'))
            ]
            self.theme = TemplateLookup(
                directories=self.directories,
                output_encoding='utf-8'
            )

            self.constants = {
                'req': cherrypy.request,
            }

        def __call__(self, template, **params):
            tmpl = self.theme.get_template(template)
            kw = self.constants.copy()
            kw.update(params)
            return tmpl.render(**kw)

    _render = RenderTemplate()


    class PageMixin(object):
        def render(self, tmpl, params=None):
            params = params or {}
            params.update(dict([
                (name, getattr(self, name))
                 for name in dir(self)
                 if not name.startswith('_')
            ]))
            return _render(tmpl, **params)


        def json(self, obj):
            cherrypy.response.headers['Content-Type'] = 'application/json'
            return json.dumps(obj)

There is a bunch of extra code here but what I'm doing is setting up a
simple wrapper around the Mako template and template look up. I could
have use pgk\_resources as well here. You'll also notice that the
handler will automatically get the cherrypy.request as a constant called
'req' for use in the template. Below our renderer is a PageMixin. I do
this b/c it is easy to add simple functions to make certain aspects
faster, for example, quickly returning JSON.

Here is how our controller class' GET method would change.


::

        def GET(self, user, id):
            some_obj = db.find(user, id)
            return self.render('foo.mako', {
                'model': some_obj
            })

Pretty simple really. I could try to get more clever by automatically
passing in our locals() or do some other tricks to make things a little
more magic, but that is really not the point. The point here is that I'm
just using Python. I don't have to use CherryPy Tools to make major
changes to the way everything works. Including a library is just an
import away. If I wanted to write my render function as a decorator that
is possible since it would just be a matter of writing the wrapper. If
we wanted to do some sort of a cascaded look up on template files, no
problem. It is all just Python.

To wrap things up, the other day I started looking into writing a
`Tool`_ for CherryPy. After messing with things a bit, I came to the
conclusion I wasn't really a huge fan of the Tool API. After thinking of
ways I could improve it and getting some good ideas from `Bob`_,
something struck me. The Tool API has been around for a long time and
yet it never has been a really important part of my writing apps with
CherryPy. The reason is really simple. I can write Python with CherryPy.
Python has decorators, itertools, functools, context managers and a
whole host of facilities for doing things like wrapping function calls.
It doesn't mean I can't write a tool, but I don't have to. The framework
is asking me to either. When I used WSGI, I would write my whole
application as bits of middleware and compose the pieces. It felt
reusable and very powerful, but it also ended up being a pain in the
neck. Frameworks have a tendency to be opinionated and while CherryPy is
seemingly rather unbiased, I'd argue the real opinion it reflects is
"quick messing with frameworks and get things done". I like that.


.. _Bottle: http://http://bottle.paws.de/
.. _CherryPy: http://cherrypy.org
.. _Mako: http://www.makotemplates.org/
.. _Tool: http://www.cherrypy.org/wiki/CustomTools
.. _Bob: http://aminus.org/blogs/index.php/fumanchu


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
