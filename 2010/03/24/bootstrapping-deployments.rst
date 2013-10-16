===========================
 Bootstrapping Deployments
===========================

Recently at work I've started working towards deploying `Dragoman`_, my
gettext service. The whole process has been rather frustrating because
much of the low level bootstrapping needed to happen. It doesn't bother
me that a blank box needed configuration, but it was frustrating that
there wasn't a repeatable pattern to get things to a generally workable
state.

What is necessary is some baseline level of functionality that fits
within our organization's system management tools. This is different
from something application specific such as the specific runtime
libraries. While there should be a baseline in terms of an environment,
that should be minimal and standardized.

In our case we use Python, so for bootstrapping there are a few common
items I'd personally like to see. These are in no particular order.


-  Python 2.5 (this is just our standard version)
-  Easy Install/Setuptools
-  `Egg Monster`_

Eggmonster is our deployment tool. It is a pull based system where
nodes phone home to a central server that tells each node what package
to run as well as how to satisfy its dependencies. It is all built
around setuptools/distutils and works really well.

In terms of base utilities the biggest that I know of off hand is
`daemontools`_. This was a hassle to install because the distribution
support was not there. I'm on the fence regarding what is best in terms
of whether to build from scratch or use the distros package management
tools, but in either case a decision needs to be made and stuck to.

Building your own packages also seems like a decent option as you could
then utilize your own server to provide tools reliably.

All this seems pretty simple, but time consuming. The packages are just
the beginnings. There is also the file system and where tools should be
used. There is also the question of what sort of security should be
utilized so that developers can login and debug services. I don't think
the organizational aspects on the file system need to be anything more
than decisions. The same goes with adding single sign on facilities. The
biggest problem is just getting it done reliably such that you can spin
up new machines easily as well as upgrade machines as the operating
system improves. Hopefully I'll get a minute to give it a try.


.. _Dragoman: http://bitbucket.org/elarson/dragoman
.. _Egg Monster: http://bitbucket.org/yougov/eggmonster
.. _daemontools: http://cr.yp.to/daemontools.html


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
