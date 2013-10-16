Emacs Reset
###########

I've had a pretty stable `Emacs`_ configuration for a while, but it also
has been somewhat unruly at times. The big issue is that I really needed
some package management. One option is to simply stick with the distro
version of Emacs and apt for my package needs, but that would preclude
me from trying new features and modes that have been developed recently.
For this reason, I build my own Emacs and have traditionally tried to
keep my environment tidy myself.
As much as I thought I had things under control, whenever I set things
up on a new machine it became apparent that my system for keeping track
of things was less than ideal. Depending on what sort of development I
had been doing recently, my environment would be at different levels of
portability and rarely was it a lossless process moving around from
machine to machine. Fortunately, it didn't happen much, but it is enough
pain to make me consider being a little more proactive with my Emacs
config.
I read a post about the `Emacs Starter Kit getting a reboot`_ and while
I knew it was a little to customized for my taste, the use `ELPA`_ and
`Marmalade`_ were intriguing. These are package repositories for Emacs
using `package.el`_. After upgrading to the dev version of Emacs from
git, I went ahead and started getting my packages in line, so I no
longer had to keep my own /emacs.d/vendor/ directory in line.
Overall the process was actually pretty quick. I know I lost some
custom functions, but I made a decision to bite the bullet and create
some actual Emacs packages for those specialized functions and even
found some new helpers. For example, I found `dizzee`_ which is a
service starter that I used to replace all my customized functions. I
also found `nose.el`_ for running `nose`_ on files and am in the process
of rewriting it for `pytest`_. This also exposed a project called `Eco`_
that looked like a nice middleground between the shell focused nature of
`virtualenv`_ and a more explicit python setup.
This whole reboot might have also helped in diving into to rooting my
phone too ;)

.. _Emacs: http://www.gnu.org/s/emacs/
.. _Emacs Starter Kit getting a reboot: http://technomancy.us/153
.. _ELPA: http://tromey.com/elpa/
.. _Marmalade: http://marmalade-repo.org/
.. _package.el: http://repo.or.cz/w/emacs.git/blob_plain/1a0a666f941c99882093d7bd08ced15033bc3f0c:/lisp/emacs-lisp/package.el
.. _dizzee: http://blog.deadpansincerity.com/2011/09/announcing-dizzee/
.. _nose.el: https://bitbucket.org/durin42/nosemacs/src/9302529e68be/nose.el
.. _nose: http://readthedocs.org/docs/nose/en/latest/
.. _pytest: http://pytest.org
.. _Eco: https://bitbucket.org/kumar303/eco
.. _virtualenv: http://pypi.python.org/pypi/virtualenv


.. author:: default
.. categories:: code
.. tags:: emacs, programming, python, testing
.. comments::
