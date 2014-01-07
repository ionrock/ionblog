Hiding Complexity vs. Too Many Layers
=====================================

If you've ever tried TDD there is a decent chance you've written some
code like this: ::

  from mock import patch


  @patch('foo.uploader.upload_client')
  def test_upload_foo(upload_client):
      do_upload()

      upload_client.upload.assert_called_with(new_filename())

In this example, what is happening is we are testing some code that
uploads a file somewhere like S3. We patch the actual upload layer to
make sure we don't have to upload anything. We then are asserting that
we are uploading the file using the right filename, which is the
result of the `new_filename` function.

The code might look something like this: ::

  from mypkg.uploader import upload_client


  def new_filename():
      return some_hash() + request.path


  def do_upload():
      upload_client.upload(new_filename())

The nice thing about this code it is pretty reasonable to test. But,
in this simplified state, it doesn't reflect what happens when you
have a more complex situation with multiple layers.

For example, here is an object that creates a gzipped CSV writer
on some parameters and the current time. ::

  class Foo(object):

      basedir = '/'

      def __init__(self, bar, baz, now=None):
          self.bar = bar
          self.baz = baz
          self._now = now
          self._file_handle = None

      @property
      def now(self):
          if not self._now:
              self._now = datetime.now().strftime('%Y-%m-%d')
          return self._now

      def fname(self):
          return '%s.gz' % os.path.join(self.basedir, self.now,
                                        self.bar, self.baz)

      @property
      def file_handle(self):
          if not self._file_handle:
              self._file_handle = gzip.open(self.fname())
          return self._file_handle

      def writer(self):
          return csv.writer(self.file_handle)


The essence of this functionality could all be condensed down to a
single method: ::

  def get_writer(self):
      now = self._now
      if not now:
          now = datetimetime.now().strftime('%Y-%m-%d')

      fname = '%s.gz' % os.path.join(self.basedir, now,
                                     self.bar, self.baz)

      # NOTE: We have to keep this handle around to close it and
      #       actually save the data.
      self.file_handle = gzip.open(fname)
      return csv.writer(self.file_handle)


The single method is pretty easy to understand, but testing becomes
more difficult.

Even though the code is relatively easy to read, I believe it is
better to lean towards the more testable code and I'll tell you why.


Tests Automate Understanding
----------------------------

The goal of readable code and tests is to help those that have to work
on the code after you've moved on. This person could be you! The code
you pushed might have seemed perfectly readable when you originally
sent it upstream. Unfortunately, that readability can only measured by the
reader. The developer might be new to the project, new to the
programming language or, conversely, be an author that predates you!
In each of these cases, your perspective on what is easy to understand
is rarely going to be nearly as clear to the next developer reading
your code.

Tests on the other hand provide the next developer with confidence
because they have an automated platform on which to build. Rather than
simply reading the code in order to gain understanding, the next
developer can play with it and confirm his or her understanding
authoritatively. In this way, tests automate your understanding of the
code.


Be Cautious of Layers!
----------------------

Even though hiding complexity by way of layers makes things easier to
test and you can automate understanding, layers still present a
difficult cognitive load. Nesting objects in order to hide complexity
can often become difficult to keep track of, especially when you are
in a dynamic language such as Python. In static languages like Java,
you have the ability to create tools to help navigate the layers of
complexity. Often times in dynamic languages, similar tools are not
the norm.

Obviously, there are no hard and fast rules. The best course of action
is to try and find a balance. We have rough rules of thumb that help
us make sure our code is somewhat readable. It is a good idea to apply
similar rules to your tests. If you find that testing some code, that
may be reasonably easy to read, is difficult to confirm an isolated
detail, then it is probably worth creating a test and factoring out
that code. The same goes for writing tons of tests to cover all the
code paths.


About the Example
-----------------

I came up with the example because it was some actual code I had to
write. I found that I wanted to be able to test each bit
separately. I had a base class that would create the file handles, but
the file naming was different depending on the specific class that was
inherited. By breaking out the naming patterns I was able to easily
test the naming and fix the naming bugs I ran into easily. What's
more, it gave me confidence when I needed to use those file names
later and wanted to be sure they were correct. I didn't have rewrite
any code that created the names because there was an obvious property
that was tested.

It did make the code slightly more ugly. But, I was willing to accept
that ugliness because I had tests that made sure when someone else
needed to touch the code, they would have the same guarantees that I
found helpful.


Test are *NOT* Documentation
----------------------------

Lastly, tests are not a replacement for readable code, docs or
comments. Code is meant for computers to read and understand, not
people. Therefore it is in our best interest to take our surrounding
tools and use them to the best of our abilities in order to convey as
clearly as possible what the computer will be doing with our
text. Test offer a way to automate understanding. Test are not a
replacement for understanding.

Finally, it should be clear that my preference for tests and more
layers is because I value maintainable code. My definition of
maintainable code is defined by years (5-10) and updated by teams of
developers. In other words, my assumption is that maintenance of the
code is, by far, the largest cost. Other projects don't have the same
requirements, in which case, well commented code with less isolated
tests may work just fine.


.. author:: default
.. categories:: code
.. tags:: programming, python, testing, tdd
.. comments::
