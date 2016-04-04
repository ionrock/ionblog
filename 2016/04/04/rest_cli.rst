REST Command Line Interface
===========================

At `work <https://rackspace.com>`_ we have a support rotation where
we're responsible for handling ticket escalations. Typically, this is
somewhat rare event that requires the team to get involved, thanks to
the excellent and knowledgable support folks. But, when there is an
issue, it can be a rough road to finding the answers you need.

The biggest challenge is simply being out of practice. We have a few
different APIs to use, both internal and external that use different
authentication mechanisms. Using something like `cURL
<https://curl.haxx.se/>`_ definitely works, but gets rather difficult
over time. It doesn't help that I'm not a `bash
<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_ expert that can
bend and shape the world to my will. There are other tools, like
`httpie <https://github.com/jkbrzt/httpie>`_, that I'd like to spend
some more time with. Unfortunately,I never seem to remember about in
the heat of the moment. Some coworkers delved into this idea for a bit
and wrote `some tools <https://github.com/pglbutt/noodles>`_, but my
understanding is that it was still very difficult to get around the
verbosity in a generic enough way for the approach to really pay off.

Looking at things from a different perspective, what if you had a
shell of sorts? Specifically, it doesn't take much to configure
something like `ipython <http://ipython.org/>`_ with some builtins for
reading auth from known files and including some helpful functions to
make things easier. You could also progressively improve the support
over time. For example, I can imagine writing small helpers to follow
links, dealing with pagination, or finding data in a specific
document. Lastly, I can also imagine it would be beneficial to store
some state inbetween sessions in order to bounce back and forth
between your HTTP shell and some other shell.

Seeing as this doesn't seem too revolutionary, I'm curious if others
have investigated this already. I'm also curious how others balance a
generic command line interface, API specific tooling and reusability
over time, without adding a million flags and more to learn than just
using cURL!


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
