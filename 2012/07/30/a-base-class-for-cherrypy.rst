A Base Class for CherryPy
#########################

I'm a fan of `CherryPy`_. It is a great framework that hits a sweet spot
in terms of features and flexibility. My biggest struggle though in
learning CP was always based on dispatchers.

When I first started learning CP, my perspective was to use something
like `Routes`_. The problem is the routes dispatcher provided by CP
doesn't support other helpful aspects such as Tools. This disconnect was
always frustrating until I understood how the handlers work. In CP, a
handler is passed a set of arguments and keyword arguments that are the
path segments and form values respectively. Understanding this aspect
makes it much clearer how to use the framework effectively in addition
to using Python (as opposed to framework specific libraries) for writing
apps.

Fast forward to today and things are even better. CP allows you to
define a \_cp\_dispatch method that can be used to pick another handler.
Here is an example:

::

    class Bar(object):

        def __init__(self, name):
            self.name = name

        def index(self, baz=None):
            return 'I am %s. baz == %s' % (self.name, baz)

    class Foo(object):

        def index(self):
            return 'I am foo'

        def _cp_dispatch(self, vpath):
            if vpath:
                bar = Bar(vpath.pop(0)
                return bar

In this example, the Foo class is able to see that it gets an extra path
segment and returns the Bar object instead. This allows you to
intelligently dispatch without having to depend on attribute names like
the traditional dispatcher.

Seeing as this is extremely simple, lets improve this pattern with a
simple base class. I'd also like to point out that I copied this from a
local project that was written by `Tabo`_ and `Fumanchu`_.

::

    class BaseHandler(object):

        exposed = True

        def _cp_dispatch(self, vpath):
            try:
                dispatcher = self.dispatch
            except AttributeError:
                return
            try:
                return dispatcher(vpath)
            except cherrypy.HTTPRedirect:
                # pass redirections as usual
                raise

And here is an example using the Base class.

::

    class MyData(BaseHandler):
        def __init__(self, id):
            self.id = id

        @cherrypy.tools.json_out()
        def GET(self):
            return db.get(self.id)


    class MyAPI(BaseHandler):
        def dispatch(self, vpath):
            if vpath:
                id = vpath.pop(0)
                return MyData(id)
            return False

        @cherrypy.tools.json_out()
        def GET(self):
            return db.listing()

In this example suppose we had our app mounted at '/api' and were using
the MethodDispatcher. When a GET request was made to '/api', we return
some listing of IDs. A GET can be made to '/api/1234' in order to get ID
1234 and we dispatch to a new instance of MyData which handles the GET
request providing the specific object's data.

You can also see how I'm using the json\_out tool to return JSON to the
client.

Hopefully this example is helpful in understanding the simplicity and
power of CP's dispatching model. You can use the above base class to
implement any logic you might need, such as transforming the segment to
the proper type, all without having to pollute your actual handler
method or contend with a specialized syntax. Obviously this is not a
perfect solution for every use case, but CP is more than happy to allow
you to configure different dispatching paradigms at different paths.

.. _CherryPy: http://cherrypy.org
.. _Routes: http://routes.readthedocs.org/en/latest/index.html
.. _Tabo: https://tabo.pe
.. _Fumanchu: http://aminus.org/blogs/index.php/fumanchu


.. author:: default
.. categories:: code
.. tags:: cherrypy, programming, python
.. comments::
