Modern Development
==================

My MacbookPro crashed with a gray screen 4 times yesterday and it gave
me time to think about what sort of environment to expect when
developing.

The first thing is that you can forget about developing
locally. Running OS X or Windows means your operating system is
nothing more than an inconvenient integration point that lets you use
Office and video conferencing software. Even if you use Linux, you'll
still have some level of indirection as you separate your dev
environment from your OS. At the very least, it will be language
specific like virtualenv in Python. At most you'll be running
VirtualBox / Vagrant with Docker falling somewhere in between.

Seeing as you can't really develop locally, that means you probably
don't have decent integration into an IDE. While I can already hear
the Java folks about to tell me about remote debugging, let me define
"decent". Decent integration into and IDE means running tests and code
quickly. So, even if you **can** step through remote code, it is going
to be slow. The same goes for developing for iOS or Android. You have
a VM in the mix and it is going to be slow. When developing server
software, you're probably running a Vagrant instance and sharing a
folder. Again, this gets slow and you break most slick debugging bits
your editor / IDE might have provided.

So, when given the choice, I imagine most developers choose speed over
integration. You can generally get something "good enough" working
with a terminal and maybe some grep to iterate quickly on code. That
means you work in a shell or deal with copying code over to some
machine. In both cases, it's kludgey to say the least.

For example, in my case, I've started ssh'ing into a server and
working there in Emacs. Fortunately, Emacs **is** reasonably
feature-full in a terminal. That said, there are still integration
issues. The key bindings I've used to integrate with non-code have
been lost. Copy and paste becomes tricky when you have Emacs or tmux
open on a server with split screens. Hopefully, your terminal is
reasonably smart where it can help finding links and passing through
mouse events, but that can be a painful process to configure.

OK. I'm venting. It could be worse.

That said, I don't see a major shift anytime soon. I've gone ahead and
tried to change my expectations. I'll need to shell into servers to
develop code. It is important to do a better job learning bash and
developing a decent shell work flow. Configuring tmux / screen / byobu
is a good investment. Part of me can appreciate the lean and mean text
interface 24/7, but at the same time, I do hope that we eventually
will expect a richer environment for development than a terminal.

.. author:: default
.. categories:: code
.. tags:: python, ssh, devops, vagrant, docker, virtualization, cloud
.. comments::
