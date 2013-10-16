Better CherryPy Tools
#####################

`CherryPy`_ allows creating extensions to the request level
functionality by means of Tools. There are a standard set of tools that
provide extra functionality such as gzipping responses, HTTP auth, and
sessions. You can also create your own tools to provide specialized
functionality as needed for your application.

From a design perspective, Tools are exceptionally powerful. Like WSGI
middleware, they provide a way to layer features on top of request
application handlers without adding extra complexity. The only problem
is that writing your own custom tools can be a little tricky, depending
on what you want to accomplish.

What makes them a little tricky is that they can be used in many
different scenarios. You can attach them to hook points in the request
cycle and they can be used as decorators. A Tool also requires that you
attach a callable to a specific hook point, which is convenient when
only one hook point is necessary for some functionality. When you need a
tool to attach to more than one hook point, it requires a somewhat
awkward extra method that can be a little confusing. None of this is
impossible to understand, but it can be less than obvious when you are
first working on writing Tools.

In order to make this process easier, I wrote an alternative Tool base
class to make writing tools a little easier. Lets start with a simple
tool that logs when a request starts and ends.

::

    import cherrypy


    class BeforeAndAfterTool(cherrypy.Tool):

        def __init__(self):
            # Attach the initial handler. This is also the method that
            # would be used with a decorator.
            super(BeforeAndAfterTool, self).__init__('before_handler',
                                                     self.log_start)

        def _setup(self):
            # CherryPy will call this function when the tools is turned
            # "on" in the config. 
            super(BeforeAndAfterTool, self)._setup()

            # The cherrypy.Tool._setup method compiles the configuration
            # and adds it to the hooks.attach call so it gets passed to the
            # attached function.
            conf = self._merged_args()
            cherrypy.request.hooks.attach('before_finalize', 
                                          self.log_end, **conf)

        def log_start(self, **conf):
            cherrypy.log('before_handler called')

        def log_end(self, **conf):
            cherrypy.log('before_finalize called')


    cherrypy.tools.before_and_after = BeforeAndAfterTool()

If you've never written a tool the above is a decent example to explain
the process of attaching more than one hook. It should also make it
clear why this API is not exactly obvious. Why do you attach the
'before\_handler' in the \_\_init\_\_ call? There is really no reason.
The Tool API has to accept an initial callable in order to allow using
it as a decorator. Similarly, we could have used the log\_start method
to attach our 'before\_finalize' and avoid using the \_setup at all.
What methodology is correct? There isn't a right or wrong way.

It would be nice if we had a slightly more straightforward way of
creating tools that was clearer in how they worked. This was my goal in
writing the SimpleTool base class. SimpleTool provides a very simple
wrapper around the above pattern to make creating a tool a bit more
straightforward.

Here is the code for the actual base class.

::

    from cherrypy import Tool
    from cherrypy._cprequest import hookpoints


    class SimpleTool(Tool):

        def __init__(self, point=None, callable=None):
            self._point = point
            self._name = None
            self._priority = 50
            self._setargs()

        def _setup(self):
            conf = self._merged_args()
            hooks = cherrypy.request.hooks
            for hookpoint in hookpoints:
                if hasattr(self, hookpoint):
                    func = getattr(self, hookpoint)
                    p = getattr(func, 'priority', self._priority)
                    hooks.attach(hookpoint, func, priority=p, **conf)

Here is the example tool above, using this new base class.

::

    class BeforeAndAfterTool(SimpleTool):

        def before_handler(self, **conf):
            cherrypy.log('before_handler called')
        callable = before_handler

        def before_finalize(self, **conf):
            cherrypy.log('before_finalize called')

How does that look? Is it a little more obvious to see what is going on?
I think so.

There are still some features we haven't covered yet. When hook points
are attached, they are ordered according by a priority. There are two
ways to set the priority. The first is by setting a priority value on
the method itself.

::

    class HighPriorityTool(SimpleTool):

        def before_handler(self, **conf):
            cherrypy.log('this is high priority!')
        before_handler.priority = 10

The second way to set the priority is via the \_priority attribute. This
will be the default priority for any hook functions. Here is an example
using the \_priority attribute.

::

    class PriorityTwentyTool(SimpleTool):

      _priority = 20

      def on_start_resource(self, **conf):
          prep_db_connections()

The last aspect of tools we haven't covered yet is how to use these
tools as decorators. As I mentioned earlier, the initial callable passed
to the Tool is used for the decorator functionality. Using the
SimpleTool base class it is simply a matter of setting the callable
attribute.

CherryPy is pretty much voodoo free, so implementing the default tool
behavior where the initial callable is applied when the tool is used as
a decorator is straight forward.

::

    class DefaultTool(SimpleTool):
        def on_start_resource(self, **conf):
            cherrypy.log('starting a resource')
        callable = on_start_resource

Pretty simple right?

If you use CherryPy and give this base class a try, let me know how it
works out. Likewise, if you think the API could be improved I love to
hear any suggestions.

As an aside, if you are curious what Tools bring to the table over WSGI
middleware, there is an important distinction. WSGI ends up nesting
function calls where tools are called directly. The result is that if
you utilize a lot of tools, the cumulative effect is much smaller
compared to WSGI middleware. Most of the time this doesn't make a huge
difference, but it is good to know that if you use Tools in your
application design, you be insured against the tools eventually becoming
a bottleneck. The other benefit of tools is that they are much simpler
to write and can be easily applied to content consistently via the
CherryPy framework (ie via the config) rather than a simple decorator.
These are not huge gains, but as complexity grows over time, Tools are a
great way to keep the code simple.

.. _CherryPy: http://cherrypy.org


.. author:: default
.. categories:: code
.. tags:: cherrypy, programming, python
.. comments::
