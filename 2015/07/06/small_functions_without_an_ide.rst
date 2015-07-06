Small Functions without an IDE
==============================

I've been reading `Clean Code
<http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882>`_
for a book club at `work <https://rackspace.com>`_. So far, it is
really a great book as it provides attributes and techniques for
understanding what clean code really looks like. My only complaint,
which is probably the wrong word, is that the suggestions are based on
using a more verbose language such as Java that you use with an IDE.

As I said, this really isn't a complaint so much as the author
mentions how things like renaming things and creating very small
functions are painless thanks to the functionality of the IDE. In
dynamically typed languages like Python, the same level of
introspection doesn't generally exist for tooling available.

As an aside, function calls in Python can be expensive, so extracting
a single function into many, much smaller functions does have the
potential to slow things down. I saw this impact on a data export tool
that needed to perform a suite of operations on each role. It had
started as one huge function and I refactored it into a class with a
ton of smaller methods. Unfortunately, this did slow things down
somewhat, but considering the domain and expense of maintaining the
single, **huge** function, the slowdown **was** worth it.

Performance aside, I'd argue that it is definitely better to try to
keep functions small and use more when writing any code. The question
then, is how do you manage the code base when you can't reliably jump
to function references automatically?

I certainly don't have all the answers, but here are some things I've
noticed that seem to help.


Use a Single File
-----------------

While your editor *might* support refactoring tools, it most certainly
has the ability to search. When you need to pop around to different
functions, keep the number of files to a minimum so you can easily use
search to your advantage.


Use a Flat Namespace
--------------------

Using a flat namespace goes hand in hand with keeping more functions /
methods in a single file. Avoid nesting your modules to make it faster
to find files within the code. One thing to note is that the goal here
is no to keep a single folder with hundreds of files. The goal is to
limit the scope of each folder / module to include the code it will be
using.

You can think of this in the same terms as refactoring your
classes. If a file has functionality that seems out of place in the
module, move it somewhere else. One benefit of using a dynamic
language like Python is you don't have the same one class per file
requirements you see in something like Java.


Consistent Naming
-----------------

Consistent naming is pretty obvious, but it is even more important in
a dynamic language. Make absolutely sure you name the same usage of
the same objects / classes throughout your code base. If you are
diligent in how you name your variables, search and replace can be
extremely effective in refactoring.


Write Tests
-----------

Another obvious one here, but make sure you write tests. Smaller
functions means more functions. More functions should mean more
tests. Fortunately, writing the tests are much, **much** easier.

.. code-block:: python

   class TestFoo(object):

       def test_foo_default(self): ...
       def test_foo_bar(self): ...
       def test_foo_bar_and_baz(self): ...
       def test_foo_bar_and_baz_and_kw(self): ...

If you've ever written a class like this, adding more functions should
make your tests easier to understand as well. A common pattern is to
write a test for each path a function can take. You often end up with
a class that has tons of oddly named test functions with different
variables mocked in order to test the different code paths in
isolation. When a function gets refactored into many small functions
(or methods) you see something more like this:

.. code-block:: python

   class TestFoo(object):

       def setup(self):
           self.foo = Foo()

       def test_foo(self):
           self.foo.bar = Mock()

	   self.foo()

           assert self.foo.bar.called

       def test_bar(self):
           self.foo.baz = Mock()

	   self.foo.bar()

	   self.foo.baz.assert_called_with('/path/to/cfg')


In the above example, you can easily mock the functions that
**should** be called and assert the interface the function requires is
being met. Since the functions are small, you're tests end up being
easy to isolate and you can test the typically very small bit of
functionality that needs to happan in that function.


Use Good Tools
--------------

When I first started to program and found out about `find ... | xargs
grep` my life was forever changed. Hopefully your editor supports some
integration of search tools. For example, I use `Emacs
<https://www.gnu.org/software/emacs/>`_ along with `projectile
<https://github.com/bbatsov/projectile>`_, which supports searching
with `ag <http://geoff.greer.fm/ag/>`_. When I use these tools in my
editor along side the massive amount of functionality my editor
provides, it is a very powerful environment. If you write code in a
dynamic language, it is extremely important to take some time to
master the tools available.

Conclusions
-----------

I'm sure there are other best practices that help to manage well
factored code in dynamic languages. I've heard some programmers that
feel refactoring code to very small functions is "overkill" in a
language like Python, but I'd argue these people are wrong. The cost
associated with navigating the code base can be reduced a great deal
using good tools and some simple best practices. The benefits of a
clean, well tested code base far out weigh the cost of a developer
reading the code.


.. author:: default
.. categories:: code
.. tags:: python, java
.. comments::
