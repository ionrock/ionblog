Property Pattern
================

I've found myself doing this quite a bit lately and thought it might
be helpful to others.

Often times when I'm writing some code I want to access something as
an attribute, even though it comes from some service or database. For
example, say we want to download a bunch of files form some service
and store them on our file system for processing.

Here is what we'd like the processing code to look like: ::

  def process_files(self):
      for fn in self.downloaded_files:
          self.filter_and_store(fn)

We don't really care what the `filter_and_store` method does. What we
do care about is `downloaded_files` attribute.

Lets step back and see what the calling code might look like: ::

  processor = MyServiceProcessor(conn)
  processor.process_files()

Again, this is pretty simple, but now we have a problem. When do we
actually download the files and store them on the filesystem. One
option would be to do something like this in our `process_files`
method. ::

  def process_files(self):
      self.downloaded_files = self.download_files()
      for fn in self.downloaded_files:
          self.filter_and_store(fn)

While it may not seem like a big deal, we just created a side
effect. The `downloaded_files` attribute is getting set in the
`process_files` method. There is a good chance the `downloaded_files`
attribute is something you'd want to reuse. This creates an odd
coupling between the `process_files` method and the `downloaded_files`
method.

Another option would be to do something like this in the constructor: ::

  def __init__(self, conn):
      self.downloaded_files = self.download_files()


Obviously, this is a bad idea. Anytime you instantiate the object it
will seemingly try to reach out across some network and download a
bunch of files. We can do better!

Here are some goals:

 1. keep the API simple by using a simple attribute,
    `downloaded_files`
 2. don't download anything until it is required
 3. only download the files once per-object
 4. allow injecting downloaded values for tests

The way I've been solving this recently has been to use the following
property pattern: ::

  class MyServiceProcessor(object):

      def __init__(self, conn):
          self.conn = conn
          self._downloaded_files = None

      @property
      def downloaded_files(self):
          if not self._downloaded_files:
              self._downloaded_files = []
              tmpdir = tempfile.mkdtemp()
              for obj in self.conn.resources():
                  self._downloaded_files.append(obj.download(tmpdir))
          return self._downloaded_files

      def process_files(self):
          result = []
          for fn in self.downloaded_files:
              result.append(self.filter_and_store(fn))
          return result


Say we wanted to test our `process_files` method. It becomes much
easier. ::

   def setup(self):
       self.test_files = os.listdir(os.path.join(HERE, 'service_files'))
       self.conn = Mock()
       self.processor = MyServiceProcessor(self.conn)

   def test_process_files(self):
       # Just set the property variable to inject the values.
       self.processor._downloaded_files = self.test_files

       assert len(self.processor.process_files()) == len(self.test_files)

As you can see it was realy easy to inject our stub files. We know
that we don't perform any downloads until we have to. We also know
that the downloads are only performed once.

Here is another variation I've used that doesn't required setting up a
`_downloaded_files`. ::

  @property
  def downloaded_files(self):
      if not hasattr(self, '_downloaded_files'):
          ...
      return self._downloaded_files

Generally, I prefer the explicit `_downloaded_files` attribute in the
constructor as it allows more granularity when setting a default
value. You can set it as an empty list for example, which helps to
communicate that the property will need to return a list.

Similarly, you can set the value to `None` and ensure that when the
attribute is accessed, the value may become an empty list. This small
differentiation helps to make the API easier to use. An empty list is
still iterable while still being "falsey".

This technique is nothing technically interesting. What I hope someone
takes from this is how you can use this technique to write clearer
code and encapsulate your implementation, while exposing a clear API
between your objects. Just because you don't publish a library,
keeping your internal object APIs simple and communicative helps make
your code easier to reason about.

One caveat is that this method can add a lot of small property methods
to your classes. There is nothing wrong with this, but it might give a
reader of your code the impression the classes are complex. One method
to combat this is to use mixins. ::


  class MyWorkerMixinProperties(object):

      def __init__(self, conn):
          self.conn = conn
          self._categories = None
          self._foo_resources = None
          sef._names = None

      @property
      def categories(self):
          if not self._categories:
              self._categories = self.conn.categories()
          return self._categories

      @property
      def foo_resources(self):
          if not self._foo_resources:
              self._foo_resources = self.conn.resources(name='foo')
          return self._foo_resources

      @property
      def names(self):
          if not self._names:
              self._names = [r.meta()['name'] for r in self.resources]



  class MyWorker(MyWorkerMixinProperties):

      def __init__(self, conn):
          MyWorkerMixinProperties.__init__(self, conn)

      def run(self):
          for resource in self.foo_resources:
              if resource.category in self.categories:
                  self.put('/api/foos', {
		      'real_name': self.names[resource.name_id],
                      'values': self.process_values(resource.values),
		  })


This is a somewhat contrived example, but the point being is that
we've taken all our service based data and made it accessible via
normal attributes. Each service request is encapsulated in a
function, while our primary worker class has a reasonably
straightforward implementation of some algorithm.

The big win here is clarity. You can write an algorithm by describing
what it should do. You can then test the algorithm easily by injecting
the values you know should produce the expected results. Furthermore,
you've decoupled the algorithm from the I/O code, which is typically
where you'll see a good deal of repetition in the case of RESTful
services or optimization when talking to databases. Lastly, it
becomes trivial to inject values for testing.

Again, this isn't rocket science. It is a really simple technique that
can help make your code much clearer. I've found it really useful and
I hope you do too!


.. author:: default
.. categories:: code
.. tags:: python, testing
.. comments::
