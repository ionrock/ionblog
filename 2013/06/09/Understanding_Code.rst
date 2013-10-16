====================
 Understanding Code
====================


Beautiful code is a myth. It is trivial to look at code and feel it is
lacking or could be written more clearly, yet it is rare that we write
code and end up with a piece of work that is well written. Seeing as
software engineering is still very much in its infancy, we can't be
too critical. While we might consider the great computer scientists
comparable to great authors, the reality is, these monuments of
software engineering are much closer to the ancient Egyptians or
Mayans. They have seen the development of language, yet they have not
mastered it to the point of art.

In light of this discovery that we lack truly beautiful code, it
becomes extremely important that we read and understand code. We start
with the basic elements of what a snippet of code is doing and start
building on that understanding. Quickly we will find that the
programming language is least of our concerns. When we are forced to
understand old code that has been used and abused for years we are
confronted with the true challenge of understanding.

If I only knew the secret to make understanding extremely complex and
mature easier, I would happily share it with the world. But I don't.

What I have found is that some code is easier to read than
others. There is the obvious style consistency that improves the
situation. `PEP 8`_ in the python world is a great example of a "good
enough" description of style that makes reading python code much less
opinionated.

Commenting is another valuable tool. The comments that make the
biggest impact to me have been the ones that reflect insecurity and
doubt. The reason being, IMHO, is working code is extremely
confident. When a programmer leaves a nugget suggesting that the code
offers opportunity for improvement, it provides a sense of relief
after following a bug to that location in the code. It is proof that
something was "good enough" at the time, but might need some changes
later. It is empowering to know when trying to understand code the
author empathized with your confusion and confirms to the reader they
are not alone.

Along side commenting, naming things (aka `one of hard things in
computer science <http://martinfowler.com/bliki/TwoHardThings.html>`_)
is another critical tool in understanding code. Where naming becomes
powerful is when we cease to critique solely based on length and
transition to truly descriptive terms. Changing the index key from `i`
to `index` is not enough. Great authors communicate intense concepts
with very few words and we should attempt the same in how we name
things. Literary authors have the theasaurus to help find words with
similar meanings. It would be pretty slick to have a theasarus for
variable and routine names. Something that examined the usage,
arguments and context to help provide feedback that you might be
naming some concept inconsistently or better yet, that there is a
larger name that communicates the encapsulated set of concepts.

Understanding code is really hard. It is not going to get radically
easier any time soon. As someone who has worked on older codebases for
a while, I'm empathetic to those who read my code after me. My hope is
that empathy yields practical benefits by saving those poor souls some
time as they are forced to unravel my mess just as I had to unravel
the mess presented to me.


.. _PEP 8: http://www.python.org/dev/peps/pep-0008/


.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
