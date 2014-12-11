Ugly Attributes
===============

At some point in my programming career I recognized that Object
Oriented Programming is not all it's cracked up to be. It can be a
powerful tool, especially in a statically typed language, but in the
grand scheme of managing complexity, it often falls short of the
design ideals that we were taught in school. One area where this
becomes evident is object attributes.

Attributes are just variables that are "attached" to an object. This
simplicity, unfortunately, makes attributes require a good deal more
complexity to manage in a system. The reason being is that languages
do not provide any tools to respect the perceived boundaries that an
attribute appears to provide.

Let's look at a simple example. ::

  class Person(object):

      def __init__(self, age):
          self. age = age

We have a simple `Person` object. We want to be able to access the
person's `age` by way of an attribute. The first change we'll want to
make is to make this attribute a property. ::

  class Person(object):
      def __init__(self, year, month, day):
          self.year = year
          self.month = date
          self.day = day

      @property
      def age(self):
          age = datetime.now() - datetime(self.year, self.month, self.day)
          return age.days / 365

So far, this feels pretty simple. But lets get a little more realistic
and presume that this `Person` is not a naive object but one that
talks to a RESTful service in order to get is values.

A Quick Side Note
-----------------

Most of the time you'd see a database and an ORM for this sort of
code. If you are using Django or SQLAlchemy (and I'm sure other ORMs
are the same) you'd see something like. ::

  user = User.query.get(id)

You might have a nifty function on your model that calculates the
age. That is, until you realize you stored your data in a non-timezone
aware date field and now that you're company has started supporting
Europe, some folks are complaining that they are turning 30 a day
earlier than they expected...

The point being is that ORMs do an interesting thing that is your only
logical choice if you want to ensure your attribute access is
consistent with the database. ORMs *MUST* create new instances for
each query and provide a *SYNC* method or function to ensure they are
updated. Sure, they might have an `eagercommit` mode or something, but
`Stack Overflow <https://stackoverflow.com>`_ will most likely provide
plenty of examples where this falls down.

I'd like to keep this reality in mind moving forward as it presents a
fact of life when working with objects that is important to understand
as your program gets more complex.

Back to Our Person
------------------

So, we want to make this `Person` object use a RESTful service as our
database. Lets change how we load the data. ::

  class Person(ServiceModel):
      # We inherit from some ServiceModel that has the machinery to
      # grab our data form our service.

      @classmethod
      def by_id(cls, id):
          doc = conn.get('people', id=id).pop()
          return cls(**doc)

      @property
      def age(self):
          age = datetime.now() - datetime(self.year, self.month, self.day)
          return age.days / 365

      # This would probably be implemented in the ServiceModel, but
      # I'll add it hear for clarity.
      def __getattr__(self, name):
          if name in self.doc:
              return self.doc[name]
          raise AttributeError('%s is not in the resource.' % name)


Now assuming we get a document that has a `year`, `month`, `day`, our
age function would still work.

So far, this all feels pretty reasonable. But what happens when things
change? Fortunately in the `age` use case, people rarely change their
birth date. But, unfortunately, we do have pesky time zones that we
didn't want to think about when we had 100 users and everyone lived on
the west coast. The "least viable product" typically doesn't afford
thinking ahead that far, so these are issues you'll need to deal with
after you have a lot of code.

Also, the whole point of all this work has been to support an
attribute on an object. We haven't sped anything up. These are not new
features. We haven't even done some clever with meta classes or
generators! The reality is that you've refactored your code 4 or 5
five times to support a single call in a template. ::

   {{ person.age }}

Let's take a step back for a bit.


Taking a Step Back
------------------

Do not feel guilty for going down this rabbit hole. I've taken the
trip hundreds of times! But maybe it is time to reconsider how we
think about object oriented design.

When we think back to when we were just learning OO there was a
zoo. In this zoo we had the mythical `Animal` class. We'd have new
animals show up at the zoo. We'd get a `Lion`, `Tiger` and `Bear` they
would all need to `eat`. This modeling feels so right it can't be
wrong! An in many ways it isn't.

If we take a step back, there *might* be a better way.

Let's first acknowledge that that our `Animal` does need to `eat`. But
lets really think about what it means to our zoo. The Animals will
eat, but so will the Visitors. I'm sure the Employee would like to
have some food now and then as well. The reason we want to know about
all this sustenance is because we need to Order food and track it's
cost. If we reconsider this in the code, what if, and this is a big
what if, we didn't make `eat` a method on some class. What if we
passed our object to our `eat` method. ::

  eat(Person)

While that looks cannibalistic at first, we can reconsider our
original `age` method as well. ::

  age(Person)

And how about our Animals? ::

  age(Lion)

Looking back at our issues with time zones, because our `zoo has grown
<http://zoo.sandiegozoo.org/>`_ and people come from all over the
world, we can even update our code without much trouble.  ::

  age(adjust_for_timezones(Person))

Assuming we're using imports, here is a more realistic refactoring. ::

  from myapp.time import age

  age(Lion)

Rather than rewriting all our `age` calls for timezone awareness, we
can change our `myapp/time.py`. ::


  def age(obj):
     age = utc.now() - adjust_for_timezones(obj.birthday())
     return age / 365

In this idealized world, we haven't thrown out objects
completely. We've simply adjusted how we use them. Our age depends on
a `birthday` method. This might be a Mixin class we use with our
Models. We also could still have our classic `Animal` base
class. `Age` might even be relative where you'd want to know how old
an `Animal` is in "person years". We might create a `time.animal.age`
function that has slightly different requirements.

In any case, by reconsidering our object oriented design, we can
remove quite a bit of code related to ugly attributes.


The Real World Conclusions
--------------------------

While it might seem obvious now how to implement a system using these
ideas, it requires a different set of skills. Naming things is one of
the `two hard things in computer science
<http://martinfowler.com/bliki/TwoHardThings.html>`_. We don't have
obvious design patterns for grouping functions in dynamic languages
where it becomes clear the expectations. Our `age` function above
likely would need some check to ensure that the object has a
`birthday` method. You wouldn't want every `age` call to be wrapped in
a try/except.

You also wouldn't want to be too limiting on type, especially in a
dynamic language like Python (or Ruby, JavaScript, etc.). Even though
there has been `some rumbling
<http://www.infoq.com/news/2014/08/python-type-annotation-proposal>`_
for type hints in Python that seem reasonable, right now you have to
make some decisions on how you want to handle the communication that
some function `foo` expects some object of type of `Bar` or has a
method `baz`. These are trivial problems at a technical level, but
socially, they are difficult to enforce without formal language
support.

There are also some technical issues to consider. In Python, function
calls can be expensive. Each function call requires its own lexical
stack such that many small nested functions, while designed well, can
become slow. There are `tools
<http://ionrock.org/2014/10/25/functional_programming_in_python.html>`_
to help with this, but again, it is difficult to make this style
obvious over time.

There is never a panacea, but it seems that there is still room for OO
design to grow and change. Functional programming, while elegant, is
pretty tough to grok, especially when you have a dynamic language code
sitting in your editor, allowing you to mutate everything under the
sun. Still, there are some powerful themes in Functional Programming
that can make your Object Oriented code more helpful in managing
complexity.


Finally
-------

Programming is really about layering complexity. It is taking concepts
and modeling them to a language that computers can take and,
eventually, consider in terms of voltage. As we model our systems we
need to consider the data vs. the functionality, which means avoiding
ugly attributes (and methods) in favor of orthogonal functionality
that respects the design inherit in the objects.

It is not easy by any stretch, but I believe by adopting the
techniques mentioned above, we can move past the kludgy parts of OO
(and functional programming) into better designed and more
maintainable software.



.. author:: default
.. categories:: code
.. tags:: python, functional programming, object oriented
.. comments::
