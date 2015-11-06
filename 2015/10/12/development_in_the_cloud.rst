Development in the Cloud
========================

I've recently made an effort to stop using local virtual
machines. This has not been by choice, but rather because OS X has
become extremely unstable as of late with VirtualBox and seems to show
similar behavior with VMWare. Rather than trying to find a version of
VirtualBox that is more stable, I'm making an effort to develop on
cloud servers instead.

First off, to aid in the transition, I've started using Emacs in a
terminal exclusively. While I miss some aspects of GUI Emacs, such as
viewing PDFs and images, it generally hasn't been a huge change. I've
had to do some fiddling as well with my `$TERM` in order to make sure
Emacs picks up a value that provides a readable color setting.

Another thing I started doing was getting more familiar with `byobu
<http://byobu.co/>`_ and `tmux <https://tmux.github.io/>`_. As Emacs
does most of my window management for me, my use is relatively
limited. That said, it is nice to keep my actually terminal (iTerm2)
tabs to a minimum and use consistent key bindings. It also makes
keeping an IRC bouncer less of a requirement because my client is up
all the time.

The one thing I haven't done yet is to provision a new dev machine
automatically. The dev machine I'm on now has been updated
manually. I started using a Vagrantfile to configure a local VM that
would get everything configured, but as is clear by my opening
paragraph, frequent crashes made that less than ideal. I'm hoping to
try and containerize some processes I run in order to make a
Vagrantfile that can spin up a cloud server reasonably simple.

What makes all this possible is Emacs. It runs well in a terminal and
makes switching between local and remote development reasonably
painless. The biggest pain is the integrations with my desktop, aka my
local web browser. When developing locally, I can automatically open
links with key bindings. While I'm sure I could figure something out
with iTerm2 to make this happen, I'm going to avoid wasting my time
and just click the link.

If you don't use Emacs, I can't recommend tmux enough for "window"
management. I can see how someone using vim could become very
proficient with minimal setup.

.. author:: default
.. categories:: code
.. tags:: cloud, emacs, vim, development
.. comments::
