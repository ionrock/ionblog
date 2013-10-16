Learning Emacs Lisp
###################

If you use Emacs then you need to learn Emacs Lisp. Lisp as a language
has widely been considered one of those languages that will change the
way you program by opening your mind to new ways of thinking about
problems. While I think this is true, my suggestion to learn lisp is
completely practical.
One of the benefits of Vi(m) is that you can stay in the shell most of
the time. Vim can be like an advanced pager at times, batch editor or
diff tool because the workflow is to stay in the shell and open it on
demand. This means if you are a Vim user, it is important to understand
your shell and recognize it as a place to customize your environment.
Emacs, on the other hand, is really like a text based OS. You start it
up and use it to interact with the filesystem and files using the
paradigms it offers. You have a file manager, process runner, manual
reader, IRC, etc. all from within Emacs and all using a text based
paradigm. Therefore, if you want to optimize your environment, you need
lisp.
If you've ever known someone good at a GUI toolkit you'll notice they
are very quick to produce simple GUI tools. They see a UI and can
immediately start coding something up that presents them with the data
quickly. Likewise web developers can often whip up a quick HTML
interface for some server process without batting an eye. When you learn
Emacs Lisp, you are learning a similar skill in that you immediately can
see places where you'd like to optimize your system and create a UI for
it.
A really good example of where this makes a difference is in copying
and pasting. It is one of those things developers do all the time. They
paste code or URLs from things like terminals, email, browsers, etc.
When you work in Emacs, you have the tools immediately available to grab
the URL your cursor is on and open it in a browser without even having
to copy and paste. You can grep for logs and save the output in a file.
One of my personal favorites is doing bunch of thing in a shell and
saving the shell session as a file then editing it for an example. What
all these examples show is how you don't have to think about moving text
around in terms of selecting it, copying it to some clipboard, changing
applications and pasting it. Instead you can see some text and
immediately run commands on it, using the output immediately afterwards
directly in your editor.
A great example of this workflow is a paste function I wrote. We have a
local pastebin at my job (you can download your own version `here`_)
along with an IRC bot. As all the developers work remotely, the ability
to paste code quickly along with links is very powerful. Previously, I
had written a command line script in Python to accept stdin and paste
the result to our pastebin. In IRC you could use a command and the bot
would get the most recent paste by your username and print the URL in
the channel. This was slick, but not optimal. It seemed a waste to
maintain a Python script for POSTing to the pastebin. It also didn't
make sense that the bot would have to grab the URL since I should know
the URL after POSTing the code. I rewrote my code to do POST the
selected code to the pastebin, use the mode of the current buffer to
find the type of code (for highlighting), get the resulting URL and add
it to the kill ring so I can immediately copy it in IRC, which I'm
running in Emacs.
This might sound like a lot of work, but honestly it wasn't much work
at all. I'm not an Emacs Lisp guru by any stretch but by picking up a
little here and there and getting used to the docs, writing small
functions like this has become relatively easy and ended up being quite
helpful. There are obviously times when it is simpler to just use
another tool, but if you are a programmer and have dedicated yourself to
an editor, then finding this flow when customizing your tools should be
pretty natural and profitable once you get used to it. If you are using
Emacs and not learning its Lisp dialect, then you really are missing
out.

.. _here: https://bitbucket.org/chmullig/librarypaste


.. author:: default
.. categories:: code
.. tags:: emacs, programming
.. comments::
