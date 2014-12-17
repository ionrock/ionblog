Python Packaging Frustrations
#############################

I'm not a fan of Python packaging. This is a new development for me
because up until now, things like easy\_install and `setuptools`_ have
felt perfectly adequate. The big reason for the change is a realization
that software should have a build step. A build step is important
because it forces you to think about distributing your application in an
environment. You build your software to some executable or package that
will be put on some other system.

Distutils has this concept, but setuptools took it and ended up making
it the norm to just install the source as an egg instead of creating a
true package. The result is that tools like `virtualenv`_ have cropped
up that focus more on recreating a dev environment than reproducing an
installation of packages. I'm not bashing virtualenv, but rather just
suggesting that there might be better ways to think about creating a dev
environment and translating that to a production environment.

I realize this is a subtle difference . But after having a nightmare
trying to install an application on OS X thanks to its dependencies, it
became clear that deploying source packages and letting dependencies be
downloaded and built is not a great model. Fortunately, I don't think it
is that hard a problem to fix. The bigger issue is how to deal with the
cultural aspects and communicating the subtleties of the two techniques
when the current status quo is really easy.

Hopefully the `distutils2`_ effort will show some improvements.

.. _setuptools: http://pypi.python.org/pypi/setuptools
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _distutils2: https://bitbucket.org/tarek/distutils2/src/tip/docs/design/wiki.rst


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
