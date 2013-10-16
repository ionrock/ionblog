Passing Arguments
#################

Have you ever found yourself in a programming situation where you see
your function signatures growing? Typically, this is a sign that you
need to think about refactoring. Unfortunately, sometimes a library you
are using doesn't really make that as simple as you might like.

Lately, I've been working with a parser and this ends up being a good
example of how this can happen. A parser usually will help in parsing by
providing some state tracking functionality. The problem is that it can
be difficult to fit all the functionality within the confines of the
parser's API. In my specific case, I need to support line numbers, but
the parser doesn't really function on lines.

Finding the line numbers was relatively easy. Making them available at
the right context was more difficult. The result was that I started
adding arguments that would pass the necessary info along until it
reached the right context. This added to the already somewhat long set
of arguments.

I'm positive that there is a better solution. I'm sure I'll find it
sooner or later.


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
