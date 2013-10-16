=================
 Coding Comments
=================

I've heard plenty of times from coders that comments are pointless. Some
folks are even avidly against them. In the past my own thoughts most
definitely tended towards code telling the algorithmic story. Lately
though, my perceptions have changed. My recent goals have been to
understand what really makes code maintainable in the real world. There
are plenty of blogs out there that can offer small examples of how
something could be made more readable and assume that it negates the
need for comments, but I don't believe them at this point. It is not
that the refactoring and naming isn't important, but rather it is not
enough in the real world. A blog post will get a few paragraphs to
explain the context, give you the small snippet and walk you through the
changes. At then end you feel like the code is so obvious it hurts.

Unfortunately, the difference is that in the real world, that snippet is
wrapped by a few hundred lines on either side. And, in python, you have
no clue what some arguments type possibly is, so looking at the original
object just doesn't cut it. It just isn't that easy.

What is ironic then is that those folks trying to make code more
readable are also making a strong case for commenting. The blog usually
does a really good job of explaining the context and then how that
context applies to the actual code. Unfortunately we've all see the
massively commented code complete with paragraphs for getters and
setters and found it extremely difficult to gain anything from the
extreme verbosity that is probably incorrect anyway. Still, there is a
need to provide context.

Lately my code has drawn me into the `CherryPy`_ internals a bit to see
how things work. CherryPy has always been a framework (or library
really) that just gets out of the way. It has done such a good job at
this that I've been trying to use more of it! In looking at the code,
there are some really consistent practices that have made understanding
what is going on much easier. Here are my summations.

1. All code should be in chunks.

If you look at the CherryPy code you quickly notice that each piece of
structure is actually created from smaller bits of structure defined by
spaces and short comments. Most I would say are between 4 and 8 lines
long. They also have a really short one line comment describing what is
happening. This leads me to my next point.

2. All comments length should be relative to the size of the code.

If you have most of your code in 4 to 8 line segments, a one line
comment is perfect. If you have something that takes up most of the page
in your editor, the comments should either be a single larger before the
algorithm/section or should follow the logic as it goes through the
code.

I should mention that when I say "segments" these are not language
constructs. This is simply putting a blank line between things.

Commenting in generally is one of those thing that is tough to do
right. It is easy to skirt the issue, but I'm going to go ahead an say
if you're not commenting your code, you're really doing it wrong.

Comments share the context of your well written clean code. It is not
your fault that code is mean for machine not people, so don't feel bad
that your code is easier to read because you added a little comment.

Likewise, when you commit your code, it is really publishing it. Someone
else will read it at some point, so consider your audience.

I'd encourage anyone to take a look at the CherryPy source and try to
understand it. It is surprisingly simple to follow along. It doesn't
make you fluent in the code, but it does let you see what is happening
in a way that diving deeper is easier.

I should also mention these suggestions are somewhat limited to
languages like Python and Ruby where the types are dynamic. In C#/Java
for example you usually have an very clear picture of what is happening
and I'd say in rare cases to comments really help. Python doesn't have
this so adding a comment or two here and there allows the reader a
context for digging deeper.


.. _CherryPy: http://cherrypy.org


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
