Emacs and Strings
=================

If you've ever programmed any elisp (emacs lisp) you might have been
frustrated and surprised by the lack of string handling functions. In
Python, it is trivial to do things like:

.. code-block:: python

   print('Hello World!'.split().lower())

The lack of string functions in elisp has been improved greatly by
`s.el <https://github.com/magnars/s.el>`_, but why haven't these
sorts functions existed in Emacs in the first place? Obviously, I
don't know the answer, but I do have a theory.

Elisp is (obviously) a LISP and LISPs are functional! One tenant of
functional languages is the use of immutable data. While many would
argue immutability is not something elisp is known for, when acting on
a buffer, it is effectively immutable. So, rather than load some
string into memory, mutate it and use it somewhere, my hunch is early
emacs authors saw things differently. Instead, they considered the
buffer the place to act on strings. When you call an elisp function it
acts like a monad or a transaction where the underlying text is
effectively locked. Rather than loading it into some data structure,
you instead are given access to the editor primitives to literally
"edit" the text as necessary. When the function exits, the buffer is
then returned to the UI and user in its new state.

The benefits here are:

 1. You use the same actions the user uses to manipulate text
 2. You re-use the same memory and content the editor is using

While, it feels confusing coming from other languages, if you think of
all the tools available to edit text in Emacs, one could argue that
string manipulation is not necessary.

Of course, my theory could be totally wrong, so who
knows. Fortunately, there is s.el to help bridge the gap between
editing buffers and manipulating text.


.. author:: default
.. categories:: code
.. tags:: emacs, lisp, functional programming
.. comments::
