=============
 CherryFlask
=============


Today I noticed a core, albeit simple, application we wrote uses
flask_. This seemed odd since typically we_ would consider ourselves a
CherryPy_ and Django_ shop. Since the app is so small with no actual
UI, it doesn't make sense to use Django. But, why not use CherryPy?
The author is typically a Django dev, so I'd assume it seemed easier
(and possibly more fun) to give another micro-framework a try.

Seeing as I believe CherryPy is more than capable enough to make life
easier in these situations, I was curious if I could replicate (more
or less) flask's API using a minimal amount of CherryPy.

Without further adieu, CherryFlask:

.. code-block:: python

  import cherrypy


  class CherryFlask(object):

      def __init__(self):
          self.dispatcher = cherrypy.dispatch.RoutesDispatcher()

      def route(self, path):
          def handler(f):
              self.dispatcher.connect(path, path, f)
              return f
          return handler

      def run(self):
          conf = {
              'global': {'script_name': '/'},
              '/': {'request.dispatch': self.dispatcher}
          }
          cherrypy.quickstart(None, '/', config=conf)


  app = CherryFlask()


  @app.route('/')
  @cherrypy.tools.json_out()  # cool, I can use cherrypy tools as decorators!
  def hello():
      return {'message': 'hello world'}


  if __name__ == '__main__':
      app.run()

Obviously this is just a proof of concept, but it doesn't seem that
difficult to continue to build on the idea to construct the same sort
of micro-framework with a minimal amount of code. Also, it shows that
CherryPy could be used to create other, more specialized, APIs.

.. _flask: http://flask.pocoo.org/
.. _we: http://yougov.com
.. _CherryPy: http://cherrypy.org
.. _Django: https://www.djangoproject.com/


.. author:: default
.. categories:: code
.. tags:: programming, python, cherrypy
.. comments::
