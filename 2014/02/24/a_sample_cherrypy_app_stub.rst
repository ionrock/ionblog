A Sample CherryPy App Stub
==========================

In many full stack frameworks, there is a facility to create a new
application via some command. In django for example, you use
`django-admin.py startproject foo`. The `startproject` command will
create some directories and files to help you get started.

CherryPy tries very hard to avoid making decisions for you. Instead
CherryPy allows you to setup and configure the layout of your code
however you wish. Unfortunately, if you are unfamiliar with CherryPy,
it can feel a bit daunting setting up a new application.

Here is how I would set up a CherryPy application that is meant to
serve basic site with static resources and some handlers.

The File System
---------------

Here is what the file system looks like. ::

  ├── myproj
  │   ├── __init__.py
  │   ├── config.py *
  │   ├── controllers.py
  │   ├── models.py
  │   ├── server.py
  │   ├── static
  │   ├── lib *
  │   └── views
  │       └── base.tmpl
  ├── setup.py
  └── tests

First off, it is a python package with a `setup.py`. If you've never
created a python package before, `here is a good tutorial
<http://www.scotttorborg.com/python-packaging/>`_.

Next up is the project directory. This is where all you code
lives. Inside this directory we have a few files and directories.

 - `config.py` : Practically every application is going to need some
   configuration and a way to load it. I put that code in `config.py`
   and typically import it when necessary. You can leave this out
   until you need it.
 - `controllers.py` : MVC is a pretty good design pattern to
   follow. The `controllers.py` is where you put your objects that
   will be mounted on the `cherrypy.tree`.
 - `models.py` : Applications typically need to talk to a database or
   some other service for storing persistent data. I highly recommend
   `SQLAlchemy <http://www.sqlalchemy.org/>`_ for this. You can
   configure the models referred to in the SQLAlchemy docs here, in
   the `models.py` file.
 - `server.py` : CherryPy comes with a production ready web server
   that works really well behind a load balancing proxy such as
   Nginx. This web server should be used for development as well. I'll
   provide a simple example what might go in your `server.py` file.
 - `static` : This is where your css, images, etc. will go.
 - `lib` : CherryPy does a good job allowing you to write plain
   python. Once the controllers start becoming more complex, I try to
   move some of that functionality to well organized classes /
   function in the `lib` directory.
 - `views` : Here is where you keep your template files. `Jinja2
   <http://jinja.pocoo.org/docs/>`_ is a popular choice if you don't
   already have a preference.

Lastly, I added a `tests` directory for adding unit and functional
tests. If you've never done any testing in Python, I highly recommend
looking at `pytest <http://pytest.org>`_ to get started.


Hooking Things Together
-----------------------

Now that we have a bunch of files and directories, we can start to
write our app. We'll start with the Hello World example on the
CherryPy homepage.

In our `controllers.py` we'll add our `HelloWorld` class ::

  # controllers.py
  import cherrypy


  class HelloWorld(object):
      def index(self):
          return 'Hello World!'
      index.exposed = True


Our `server.py` is where we will hook up our controller with the
webserver. The `server.py` is also how we'll run our code in
development and potentially in production

.. code-block:: python

  import cherrypy

  # if you have a config, import it here
  # from myproj import config

  from myproj.controllers import HelloWorld

  HERE = os.path.dirname(os.path.abspath(__file__))


  def get_app_config():
      return {
          '/static': {
              'tools.staticdir.on': True,
              'tools.staticdir.dir': os.path.join(HERE, 'static'),
          }


  def get_app(config=None):
      config = config or get_config()
      cherrypy.tree.mount(HelloWorld(), '/', config=config)
      return cherrypy.tree


  def start():
      get_app()
      cherrypy.engine.signals.subscribe()
      cherrypy.engine.start()
      cherrypy.engine.block()

  if __name__ == '__main__':
      start()


Obviously, this looks more complicated than the example on the
cherrypy homepage. I'll walk you through it to let you know why it is
a little more complex.

First off, if you have a `config.py` that sets up any configuration
object or anything we import that first. Feel free to leave that out
until you have a specific need.

Next up we import our controller from our `controllers.py` file.

After our imports we setup a variable `HERE` that will be used to
configure any paths. The static resources is the obvious example.

At this point we start defining a few functions. The `get_app_config`
function returns a configuration for the application. In the config,
we set up the `staticdir` tool to point to our `static` folder. The
default configuration is to expose these files via `/static`.

This default configuration is defined in a function to make it easier
to test. As you application grows, you will end up needing to merge
different configuration details together depending on configuration
passed into the application. Starting off by making your config come
from a function will help to make your application easier to test
because it makes changing your config for tests much easier.

In the same way we've constructed our config behind a function, we
also have our application available behind a function. When you call
`get_app` it has the side effect of mounting the `HelloWorld`
controller the `cherrypy.tree`, making it available when the server
starts. The `get_app` function also returns the `cherrypy.tree`. The
reason for this is, once again, to allow easier testing for tools such
as `webtest <http://webtest.readthedocs.org/en/latest/>`_. Webtest
allows you to take a WSGI application and make requests against it,
asserting against the response. It does this without requiring you
start up a server. I'll provide an example in a moment.

Finally we have our `start` function. It calls `get_app` to mount our
application and then calls the necessary functions to start the
server. The `quickstart` method used in the homepage tutorial does
this under the hood with the exception of also doing the mounting and
adding the config. The `quickstart` can become less helpful as your
application grows because it assumes you are mounting a single object
at the root. If you prefer to use `quickstart` you certainly can. Just
be aware that it can be easy clobber your configuration when mixing it
with `cherrypy.tree.mount`.

One thing I haven't addressed here is the database connection. That is
outside the scope of this post, but for a good example of how to
configure SQLAlchemy and CherryPy, take a look at the example
application, Twiseless_. Specifically you can see how to setup the
`models
<https://github.com/Lawouach/Twiseless/tree/master/lib/model>`_ and
`connections
<https://github.com/Lawouach/Twiseless/blob/master/serve.py#L39>`_. I've
chosen to provide a file system organization that is a little closer
to other frameworks like Django, but please take liberally from
Twiseless to fill in the gaps I've left here.


Testing
-------

In full stack frameworks like Django, testing is part of the full
package. While many venture outside the confines of whatever the
defaults are (using pytest vs. django's unittest based test runner),
it is generally easy to test things like requests to the web
framework.

CherryPy does not take any steps to make this easier, but fortunately,
this default app configuration lends itself to relatively easy
testing.

Lets say we want to test our `HelloWorld` controller. First off,
we'll should set up an environment to develop with. For this we'll use
`virtualenv <http://virtualenv.org>`_. I like to use a directory
called `venv`. In the project directory:

.. code-block:: shell-session

  $ virtualenv venv

Virtualenv comes bundled with a `pip <http://pip-installer.org>`_. Pip
has a helpful feature where you can define requirements in a single
test file. Assuming you've already filled in your `setup.py` file with
information about your package, we'll create a `dev_requirements.txt`
to make it easy to get our environment setup. ::

  # dev_requirements.txt

  -e .  # install our package

  # test requirements
  pytest
  webtest

Then we can install these into our virtualenv by doing the following
in the shell:

.. code-block:: shell-session

  $ source venv/bin/activate
  (venv) $ pip install -r dev_requirements.txt

Once the requirements are all installed, we can add our test.

We'll create a file in `tests` called
`test_controller_hello_world.py`. Here is what it will look like:

.. code-block:: python

  import pytest
  import webtest

  from myproj.server import get_app


  @pytest.fixture(scope='module')
  def http():
      return webtest.WebTest(get_app())


  class TestHelloWorld(object):

      def test_hello_world_request(self, http):
          resp = http.get('/')
          assert resp.status_int == 200
          assert 'Hello World!' in resp


In the example, we are using a `pytest fixture
<https://pytest.org/latest/fixture.html>`_ to inject webtest into our
test. WebTest allows you to perform requests against a WSGI
application without having to start up a server. The `request.get`
call in our test then is the same as if we had started up the server
and made the request in our web browser. The resulting response from
the request can be used to make assertions.

We can run the tests via the `py.test` command:

.. code-block:: shell-session

  (venv) $ py.test tests/

It should be noted that we also could test the response by simply
instantiating our `HelloWorld` class and asserting the result of the
`index` method is correct. For example

.. code-block:: python

  from myproj.controllers import HelloWorld


  def test_hello_world_index():
      controller = HelloWorld()
      assert controller.index() == 'Hello World!'

The problem with directly using the controller objects is when you use
more of CherryPy's features, you end up using more of
`cherrypy.request` and other cherrypy objects. This progression is
perfectly natural, but it makes it difficult to test the handler
methods without also patching much of the cherrypy framework using a
library like `mock <http://www.voidspace.org.uk/python/mock/>`_. Mock
is a great library and I recommend it, but when testing controllers,
using WebTest to handle assertions on responses is
preferred.

Similarly, I've found pytest fixtures to be a powerful way
to introduce external services into tests. You are free to use any
other method you'd like to utilize WebTest in your tests.


Conclusions
-----------

CherryPy is truely an unopinionated framework. The purpose of CherryPy
is to create a simple gateway between HTTP and plain Python code. The
result is that there are often many questions of how to do common
tasks as there are few constraints. Hopefully the above folder layout
along side the excellent Twiseless_ example provides a good jumping
off point for getting the job done.

Also, if you don't like the layout mentioned above, you are free to
change it however you like! That is the beauty of cherrypy. It allows
you to organize and structure your application the way you want it
structured. You can feel free to be creative and customize your app to
your own needs without fear of working against the framework.


.. _Twiseless: https://github.com/Lawouach/Twiseless

.. author:: default
.. categories:: code
.. tags:: python, cherrypy, django
.. comments::
