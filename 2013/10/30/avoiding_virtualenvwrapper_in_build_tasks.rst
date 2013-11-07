===========================================
 Avoiding Virtualenvwrapper in Build Tasks
===========================================

Virtualenvwrapper_ is a really helpful tool that allows you keep your
Python virtualenv's organized in a single location. It provides some
hooks to make working with a virtualenv in a shell
simple. Unfortunately, it is not well suited to organizing automated
virtualenvs used in a project's build tasks.

First off, I should say that my goal with any build task is that it
can be run without any external requirements. No environment variables
should need setting. No virtualenv activated. No other services be up
and running (within reason). My goal with any project is to support
something like this. ::

  $ git clone $project
  $ cd $project
  $ make bootstrap
  $ make test
  $ make run
  $ make release

In this case I'm using Make_ as an example, but Paver_, Rake_,
Invoke_, SCons_, CMake_, Redo_, Ant_ or any other build tool would
work.

The problem with virtualenvwrapper is that it assumes you are using it
from a shell. It implements its functionality as shell functions. It
is necessary that it does this because it is impossible for a child
process to adjust the environment of the parent in a way that lasts
after the child process ends. Virtualenv's user interface wants to
enable a virtualenv after it has been created, so the shell functions
are the best way to do this.

None of this means that a developer cannot use virtualenvwrapper. It
simply means that using virtualenvwrapper to create and bootstrap your
environment is more complex and could be more brittle over time. It is
safer and more reliable to just create the virtualenv yourself, while
making it configurable to utilize a virtualenv previously created by
virtualenvwrapper.


.. _Make: http://www.gnu.org/software/make/
.. _Paver: http://paver.github.io/paver/
.. _Rake: http://rake.rubyforge.org/
.. _Invoke: http://pyinvoke.org
.. _Scons: http://www.scons.org/
.. _CMake: http://www.cmake.org/
.. _Redo: https://github.com/apenwarr/redo/
.. _Ant: http://ant.apache.org
.. _Virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
