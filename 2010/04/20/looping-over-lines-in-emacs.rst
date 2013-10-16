=============================
 Looping Over Lines in Emacs
=============================

I can't tell you how many times I've wanted to take some selection of
text and just do some operation over every line. If this desire gets
strong enough, I'll save the text as a file and crack open my `ipython`_
shell. Eventually things devolve into writing a short script. In reality
none of this is a big deal, but it is obviously something that could be
optimized. This is especially true when a vast majority of the
operations are simply analyzing a line for bit of information.

As I am an avid `Emacs`_ user, there is a pretty serious voice in the
front of my head screaming at me to figure out how to do this in my
editor of choice. This kind of monotony has in fact driven me to learn
how to make keyboard macros and get familiar with Emacs regex. My most
recent foray, I realized that I needed to take yet another step and
learn some lisp.

The hardest part of figuring things out was simply finding the
documentation and learning how to read it. Emacs contains quite an
unbelievable amount of help available to the curious user, but
unfortunately, I'm pretty bad at finding what I need. That is another
skill I've been working on brushing up slowly but surely. Once I found
some helpful bits, the process was really simple.

Here is the code:

::

    (defun regex-keep-lines ( )
      "Keeps a line in a region if the regex matches"
      (interactive)
      (setq msg (read-string "regex: "))
      (setq num-lines (count-lines (mark) (point)))
      (setq line-direction nil)
      (if ( num-lines 0)
        (if (not (string-match msg (buffer-substring (line-beginning-position) (line-end-position))))
        (kill-line 1))
        (forward-line line-direction)
        (setq num-lines (1- num-lines))))

What this function does is takes in a regex string and if a line
doesn't match, it gets yanked. The lines it goes over are the lines in
some selection.

The reason I messed with this in the first place was because I needed
to transplant a large number of changesets in mercurial. With a little
hg log filtering and reading, I narrowed down the output to the
changesets I needed. It would have been pretty easy to just move around
in my buffer and clean things up, but curiosity got the best of me and I
wrote the above function (as well as a inverse of it, removing lines if
they contain the regex).

I'm always pleasantly surprised with how trivial little functions like
these end up. It is never very difficult and the output works really
well in more cases than I would have expected. For example, I wondered
if I would need to settle on having to start the selection at the top
and move down since that provides an obvious path for traversing the
selection. That ended up being really easy to get around.

I'm sure this sort of thing has been done before. I'm pretty sure there
is an "occur" function that effectively does the same sort of thing.

That said, it is pleasing to realize that with a little work I can learn
to customize my editor while learning a rather innovative language.


.. _ipython: http://ipython.scipy.org/
.. _Emacs: http://www.gnu.org/software/emacs/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
