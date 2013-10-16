Debbugging .emacs in OS X
#########################

It is rare as an Emacs user that I'll close my editor. Every package I
want to try out can be made available without ever having to restart
Emacs. While it is extremely helpful, it can also throw you for a loop
when you do need to restart Emacs.

I recently started using `Melpa`_ and upgraded some packages.
Unfortunately my MacBook Pro has a bug where the graphic driver seems to
go south and freeze my machine, forcing a hard restart. Upon restarting
`Emacs.app`_ wasn't happy loading my .emacs. Since this is OS X and it
is an actual "app", it wasn't obvious how to use the "--debug-init" flag
when opening Emacs.

This ended up being really easy. I opened a terminal and navigated
inside the .app file. If you've never done played around with this
before, all the applications are really just directories with a known
file structure that allows OS X to keep each apps resources separate. It
works kind of like an RPM or deb package that never actually gets
expanded on the file system. At least that is how I look it.
Our goal is to find the executable in order to run it with
"--debug-init". On my system I changed to: ::

  cd /Applications/Emacs.app/Contents/MacOS

There is an "Emacs" executable and you can run it, debugging your init
file. ::

  ./Emacs --debug-init ~/.emacs

I usually open my .emacs file when I do this since you most likely will
be changing something there anyway.
There might be other ways to do this that are more Mac-like, so feel
free to leave examples in the comments.

.. _Melpa: http://melpa.milkbox.net/
.. _Emacs.app: http://emacsformacosx.com/


.. author:: default
.. categories:: code
.. tags:: emacs, programming
.. comments::
