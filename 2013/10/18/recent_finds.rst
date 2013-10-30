==============
 Recent Finds
==============

For the past few years I've been more or less happily developing on
OS X. Thanks to Emacs_, I have a nice text base interface to work with
that allows me to manage most of my core applications (text editor,
IRC, email, terminal, etc.) in a keyboard centered environment. At the
same time, I missed the stripped down environment of my tiling window
manager choice, StumpWM_. A recent associate moved on to "googlier"
pastures and left behind a X1 Carbon that was up for grabs. Seeing as
my MacBook Pro always had problems running VMs and the disk was always
almost full, it seemed like a good time to switch.

When switching environments, it usually is a time you are forced
reinvestigate the current tools available. Here are some tools that
I've found interesting.

Emacs
=====

Helm
----

Helm_ is the reinvention of anything.el. Many people compare it to
Spotlight, Alfred and Quicksilver on the Mac in that it helps you
configure smart look ups to find things. People use it for everything
from autocomplete to a `nice interface to spotify`_. The spotify video
inspired me to write some code to browse the files in my recently
converted blog. It was really easy to do and puts a pretty face along
side a usable UI for very little time.

Expand Region
-------------

Anyone who follows Emacsrocks_ probably already has seen `Expand
Region`_. It is a really simple package that helps you to semantically
expand what is selected. Here is a `short video
<http://emacsrocks.com/e09.html>`_ showing how it works. The nice
thing is that if you are refactoring code, this makes it easy to
select the current expression, function or class and cut/copy it where
you need it to go. Likewise, you needed to search/replace in a
semantic block, it is trivial to do without having to move around to
make the selection.

S and Dash
----------

S_ is a string library for elisp and Dash_ is a library for working
with lists in elisp. Neither are arguably that helpful if you already
know elisp and/or common lisp, but for someone like me that doesn't
have a strong lisp background, these are really helpful libs.

Python
======

Tinkerer
--------

I recently migrated my blog to Tinkerer_. The nice thing about it is
that it uses Sphinx_ for generating the static pages.

Toolz
-----

Toolz_ extends itertools, functools and operator modules in order to
provide a more robust functional programming pattern in Python. After
playing with it a bit, it was clear how helpful a tool it can be in a
distributed processing model. It is trivial to construct a complext
pipeline of transforms and pass it to a multiprocessing pool to
quickly crank through some data.

Python Daemon
-------------

There are tons of tutorials and libraries out there for creating
proper unix daemon. `PEP 3143`_ proposed a module in the standard
library since it is something that hasn't changed in a *long*
time. The result was python-daemon_. The python-deamon module is
really easy to use and makes doing helpful bits like changing working
directory and capturing stoud/stderr trivial.

Invoke
------

Invoke_ is a python build tool that is similar to Paver_. What is
interesting about it is that it has a mechanism for including other
source files as extensions. It has a focus on calling multiple tasks
at the same time and handing each task's arguments correctly. I
haven't had a chance to mess with it very much, but my cursory
overview has been positive. It cleans up a couple annoyances I had
with Paver regarding task arguments. It also comes from the folks that
wrote Fabric_.


This process of setting up my dev environment has been fun. It has
been much simpler to get my emacs up and running thanks to keeping my
config files in source control and package listings up to date. My
fingers remembered how to use StumpWM. It is as though I never
switched! Hope you enjoy my recent finds!


.. _Emacs: http://www.gnu.org/software/emacs/
.. _StumpWM: http://www.nongnu.org/stumpwm/
.. _nice interface to spotify: http://www.youtube.com/watch?v=XjKtkEMUYGc
.. _Emacsrocks: http://emacsrocks.com
.. _Sphinx: http://sphinx-doc.org/
.. _PEP 3143: http://www.python.org/dev/peps/pep-3143/
.. _python-daemon: https://pypi.python.org/pypi/python-daemon/
.. _Expand Region: https://github.com/magnars/expand-region.el
.. _S: https://github.com/magnars/s.el
.. _Dash: https://github.com/magnars/dash.el
.. _Toolz: http://toolz.readthedocs.org/
.. _Invoke: http://docs.pyinvoke.org/
.. _Paver: http://paver.github.io/paver/
.. _Fabric: http://fabfile.org

.. author:: default
.. categories:: code
.. tags:: emacs, python, programming, linux, stumpwm
.. comments::
