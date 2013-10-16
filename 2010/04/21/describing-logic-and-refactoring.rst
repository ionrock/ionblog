==================================
 Describing Logic and Refactoring
==================================

I've been staring at a rather large snippet of code trying to think of
how to refactor things so they can be easier to follow. While my
definition of "easy to follow" is going to differ from others, it is
clear that when the code is a long set of nested if/else if/else
statements, there could be a better way. The problem is I can't seem to
find it!

One of the issues is defining what the logic is really checking
against. Here is an example:

::

    if self.context.baseline != current_status and 'foo' in self.new_data:
       next_segment = self.content.next_segment()

This code is totally made up but it hopefully expresses the problem.

The test is checking a few different details in order to set some
variable that gets used in another if test later. The obvious thing to
do is to simplify the value to see if it can be made into something
like:

::

    need_segment = (self.context.baseline != current_status and 'foo' in self.new_data)
    if need_segment:
       next_segment = self.content.next_segment()

This small change helps make the if statement a little more
encapsulated, but really it doesn't help that much. It would be much
nicer to have something like:

::

    if self.need_segment(current_status):
        next_segment = self.content.next_segment()

At this point you might feel there is some progress towards a more
understandable set of logic, but in reality you're simply just masking
the massive if/else tree with syntax. There is still a deeply nested
tree and as we know, `flat is better than nested`_.


It is in these sorts of situations that I miss XSLT. XSLT had match
templates. Haskell has the facility by which you define a set of
functions and the signature of the input is used to decide what function
to actually call. XSLT used a slightly more specific version of this by
using the current context of the document. In both cases you have a
situation where you can have some set of state analyzed and a single
caller handle what needs to be done. In some ways this is just like a
big case statement, but the difference is that the language abstracts it
away to being implicit. This is not an easy thing to understand and when
I first started using XSLT it was difficult to grok what was really
happening. Only after I understood did I really appreciate the elegance
of it and saw effectiveness of the technique. My favorite example the
identity pattern in XSLT. A really common pattern there was simply
copying everything. This was done in a couple lines. You could then add
another match template to filter out specific node. Turn on the pretty
printing and you had a pretty slick way to filter massive amounts of XML
with a startling small amount of code.


In this situation, what I'd like is to have a match on the current
state of the application, like in XSLT. Then the nested if/else could be
removed for a set of functions. If the state was correct, the function
would be applied. Here is an example of what some framework might look
like:

::

    @apply([has_page, has_foo])
    def set_segment(self, *args, **kw):
        self.ctx['next_segment'] = self.content.find('segment', 1)

    def some_handler(self, *args, **kw):
        run_matches(self.context, self.page, self.some_other_necessary_state)

The apply decorator would take a list of functions that would get
applied to set of arguments. If they all returned True, then the
function gets called. The run\_matches function would run through all
the apply decorated methods and if none were called would return the
changes to the context. The "context" in this case would most likely be
something like a dict. In some ways this is similar to WSGI with the
main difference being the application of functions is always tested
before it happens where in WSGI, the middleware and application have to
decide whether or not to call the next method. Unlike functional
languages, I would presume the context could change between function
calls. In that way you could chain applied functions together by
providing "events" or "triggers" in the context dictionary. For example,
one applied function might add a 'foo.bar' key where another applied
function might look for the 'foo.bar' and use it's value to adjust some
other value in the context dictionary.


I have no idea if this sort of thing would really make life any easier
when dealing with large logic problems. While it is a pain in the neck
keeping everything in your head, there is an obvious path to follow in
the code. It really does take a lot of concentration, but that doesn't
mean it is a bad thing. Another concern would be efficiency. In theory
it would be nice to do the whole process recursively, but in practice it
would really need to be done based on looping just because Python
couldn't do the matching process infinitely. The looping would most
likely be faster anyway, but there are a lot of extra function calls
that add a good deal of overhead when compared to the if/else tree. Of
course worrying about it is probably a premature optimization.

The last thing that makes me leery of this kind of system is that
someone else would need to read it. Being someone that has spent a
non-trivial amount of time with XSLT makes me somewhat unique. I've seen
first hand how difficult it can be for people to learn and understand
the concepts behind it. This might feel more like adding complexity than
solving the problem of making the code more clear.


One upside that I should point out is you get more testable code. Even
though the methods have side effects, the fact is you would have had to
break up your entire logic into relatively composable parts. Each part
should be relatively autonomous, which means testing it should be
simple. My favorite tests to write have been for some small text parsing
or name generating code. You can make a huge list of input and call a
function on each to verify things are working as expected. This feels
advantageous in that you test the code in isolation easily.

I might give this idea a try, but I'm not holding my breath. One thing
I've learned is that functional concepts don't always map easily to
non-functional languages. While it seems easy to start using more
recursion and functional tools, the reality is languages are designed
and optimized for specific use cases. If functional patterns are not
part of that design, then you'll be swimming up hill. At the same time,
it seems there should be a more object oriented means of doing a similar
approach to defining large bits of logic. If I do find one, I'll
definitely post it here.


**UPDATE!**
Seeing as there is no point in thinking about these sorts of things
without actually trying them I decided to take a go at coming up with a
simple system. Talking to `Christian`_ a bit about it, he presented the
idea of using an iterator for the code in question. That made me realize
an iterator would be a good track for making my idea feel a bit more
pythonic.


I'm not claiming this is revolutionary or anything, but it seems like a
good start for an API or system that is more customized. Ultimately,
this kind of system really shouldn't be too generic just because it
would add a lot of extra code. I think the following is small enough and
simple enough to be helpful without making a bunch of extra
classes/objects that only obfuscate the intent. This is presented with
no real world practical usage though, so take it with a huge giant salt
lick. Here is the code:

::

    '''trying to make a match template / multi method like pattern for
    python'''


    class match(object):
        def __init__(self, paths):
            self.paths = paths

        def __get__(self, obj, type=None):
            if obj is None:
                return self
            new_func = self.__get__(obj, type)
            return self.__class__(new_func)

        def wrapper(self, ctx):
            matches = True
            for path in self.paths:
                if callable(path):
                    matches = path(ctx)
                elif not path in ctx:
                    matches = False
            if matches:
                self.func(ctx)
            return matches

        def __call__(self, f):
            self.func = f
            return self.wrapper
        

    class Applicator(object):

        def __init__(self, funcs, ctx):
            self.funcs = funcs
            self.ctx = ctx

        def apply(self):
            finished = False
            while not finished:
                go_again = False
                for f in self.funcs:
                    go_again = f(self.ctx)
                finished = go_again


    @match(['input'])
    def sums(ctx):
        ctx['sums'] = sum(ctx['input'])


    @match(['sums'])
    def sum_range(ctx):
        ctx['range'] = range(0, ctx['sums'])


    @match(['range'])
    def larger_than_ten(ctx):
        if max(ctx['range']) > 10:
            ctx['larger_than_ten'] = True


    if __name__ == '__main__':
        ctx = {
            'input': [1,2,3]
        }
        applicator = Applicator([sums, sum_range, larger_than_ten], ctx)
        applicator.apply()
        print ctx

        ctx['input'] = [4,5,6]
        applicator.apply()
        print ctx

Enjoy!

.. _flat is better than nested: http://python.org/dev/peps/pep-0020/
.. _Christian: http://blog.dowski.com/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
