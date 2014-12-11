Functional Programming in Python
================================

While Python doesn't natively support some essential traits of an
actual functional programming language, it is possible to use a
functional style (rather than object oriented) to write programs. What
makes it hard is that some of the constraints functional programming
requires must be followed done manually.

First off, lets talk about what Python does well that makes functional
programming possible.

Python has first class functions that allow passing a function around
the same way that you'd pass around a normal variable. First class
functions make it possible to do things like currying and complex list
processing. Fortunately, the standard library provides the excellent
`functools <https://docs.python.org/2/library/functools.html>`_
library. For example ::


  >>> from functools import partial
  >>> def add(x, y): return x + y
  >>> add_five = partial(add, 5)
  >>> map(add_five, [10, 20, 30])
  [15, 25, 35]

The next thing critical functional tool that Python provides is
iteration. More specifically, Python generators provide a tool to
process data lazily. Generators allow to you create functions that can
create data on demand rather than forcing the creation of an entire
set. Again, the standard library provides some helpful tools via the
`itertools <https://docs.python.org/2/library/itertools.html>`_
library. ::

  >>> from itertools import count, imap, islice
  >>> nums = islice(imap(add_five, count(10, 10)), 0, 3)
  >>> nums
  <itertools.islice object at 0xb7cf6dc4>
  >>> nums.next()
  15
  >>> nums.next()
  25
  >>> nums.next()
  35

In this example each of the functions only calculates and returns a
value when it is required.

Python also has other functional concepts built in such as list
comprehensions and decorators that when used with first class
functions and generators makes programming a functional style
feasible.

Where Python does not make functional programming easy is dealing with
immutable data. In Python, critical core datatypes such as lists and
dicts are mutable. In functional languages, all variables are
immutable. The result is you often create value based on some initial
immutable variable that then has functions applied to it. ::

  (defn add-markup [price]
    (+ price (* .25 price)))

  (defn add-tax [total]
    (+ total (* .087 total)))

  (defn get-total [initial-price]
    (add-tax (add-markup initial-price)))

In each of the steps above, the argument is passed in by value and
can't be changed. When you need to use the `total` described from
`get-total`, rather than storing it in a variable, you'd often times
always call the `get-total` function. Typically a functional language
will optimize these calls. In Python we can mimic this by memoizing
the result. ::

  import functools
  import operator

  def memoize(f):
      cache = {}
      @functools.wraps(f)
      def wrapper(*args, **kw):
          key = (args, sorted(kw.iteritems()))
	  if key not in cache:
	      cache[key] = f(*args, **kw)
	  return cache[key]
      return wrapper

  @memoize
  def factorial(num):
      return reduce(operator.mul, range(1, num + 1))

Now, calls to the function will re-use previous results without
having to execute the body of the function.

Another pattern seen in functional languages such as LISP is to re-use
a core data type, such as a list, as a richer object. For example,
associates lists act like dictionaries in Python, but they are
essentially still just lists that have functions to access them as a
dictionary such that you can access random keys. In other functional
languages such as haskell or clojure, you create actual types that are
similar to a struct to communicate more complex type information.

Obviously in Python we have actual objects. The problem is that
objects are mutable. In order to make sure we're using immutable types
we can use Python's immutable data type, the tuple. What's more, we
can replicate richer types by using a named tuple. ::

  from collections import namedtuple

  User = namedtuple('User', ['name', 'email', 'password'])

  def update_password(user, new_password):
      return User(user.name, user.email, new_password)

I've found that using named tuples often helps close the mental gap of
going from object oriented to a functional style.

While Python is most definitely not a functional language, it has many
tools that make using a functional paradigm possible. Functional
programming can be a powerful model to consider as there are a whole
class of bugs that disappear in an immutable world. Functional
programming is also a great change of pace from the typical object
oriented patterns you might be used to. Even if you don't refactor all
your code to a functional style, there is much to learn, and
fortunately, Python makes it easy to get started in a language you are
familiar with.


.. author:: default
.. categories:: code
.. tags:: python, functional programming
.. comments::
