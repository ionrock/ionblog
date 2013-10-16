Emacs and Doing One Thing Well
##############################

I read a bit of `this thread`_ about how Emacs fits in with the Unix
idea that you have small programs that do one thing well. Two responses
I thought were very poignant.

The first was that `Emacs does one thing well, evaluate elisp`_. When
you really think about what Emacs does, this is right on the money.
Elisp is just a specialized lisp dialect that contains a ton of tools
for working with and editing text.

The other comment effectively pointed out `Emacs is for working with
code`_. This is another important distinction to make. People usually
point out things like the shell and pipes when they talk about what
makes Unix and small programs doing one thing well. In the case of
Emacs, it allows a developer to easily participate in the craft of
programming. If you needed to talk on a mailing list about some feature,
trade code snippets, chat on IRC and commit code into your version
control system, you can do it all within Emacs.

Both of these answers helped to clarify how a general purpose text
editor that has a mode for everything under the sun still adhered to the
Unix Philosophy. And even if the old school \*nix hackers didn't think
Emacs fit in, it doesn't suprise me that it was the editor of choice for
many authors of \*nix operating systems.

I don't know about you, but can you imagine needing to copy and paste
code into an email? I suspect it could look something like this:

::

    head -34 some_source.c | tail -15 &> message && send somelist@gnu.org message

Ugh…

Emacs on the other hand spawned a lot of modes helping programmers
participate in programming and working with code. Just because that
"thing" is rather large and complex, I'd argue that Emacs does a pretty
good job of doing it well.

.. _this thread: http://www.reddit.com/r/emacs/comments/w3ip3/doesnt_emacs_do_too_much/
.. _Emacs does one thing well, evaluate elisp: http://www.reddit.com/r/emacs/comments/w3ip3/doesnt_emacs_do_too_much/c59wo1e
.. _Emacs is for working with code: http://www.reddit.com/r/emacs/comments/w3ip3/doesnt_emacs_do_too_much/c59x38u


.. author:: default
.. categories:: code
.. tags:: emacs, programming
.. comments::
