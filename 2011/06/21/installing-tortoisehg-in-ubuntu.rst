Installing TortoiseHG in Ubuntu
###############################

At work we use `Mercurial`_ for our source control needs and as such,
there is an element of complexity that can be difficult to parse when
dealing strictly with the command line. Mercurial comes with a "view"
command that brings up a dialog showing the DAG and lets see where the
flow of changesets are really going. This is a really helpful feature
but it can also be truncated where it isn't quite as valuable. Enter
`TortoiseHG`_.

Long ago at a company where I worked, we used `CVS`_. And while most
would say it is a terrible VCS, I actually felt is was a pretty decent
system. The reason being was that we all use `WinCVS`_ and `Araxis
Merge`_ in a very specific workflow. The result being, we rarely if ever
really had to deal with CVS itself. In fact, this is where I started
using Mercurial because I would keep my incremental changesets locally
in my own repo, while committing my bug fixes via CVS and our workflow.
My hope then is to see if I can get a similar workflow in TortoiseHG as
I had in WinCVS in terms of reviewing and committing bug fixes.

The first thing to do is to add some software sources to your
sources.list. You can do this in the Ubuntu Software Center, but being a
long time Debian user, it was easier to just edit /etc/apt/sources.list.
You'll need to add sources for `Mercurial PPA`_ and `TortoiseHG PPA`_. There are
instructions on each respective `Launchpad`_ page.

::

    # latest mercurial releases
    deb http://ppa.launchpad.net/mercurial-ppa/releases/ubuntu natty main 
    deb-src http://ppa.launchpad.net/mercurial-ppa/releases/ubuntu natty main



    # latest tortoisehg releases
    deb http://ppa.launchpad.net/tortoisehg-ppa/releases/ubuntu natty main 
    deb-src http://ppa.launchpad.net/tortoisehg-ppa/releases/ubuntu natty main

You also need to make sure apt can trust these sources. This is done by
adding the respective sources keys.

::

    # mercurial
    $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 323293EE


    # tortoisehg
    $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key D5056DDE

After you've added the sources, you can apt-get update to make the new
source's packages available. From there, installing TortoiseHG is as
simple as apt-get install tortoisehg.

This will install the thg command. From a terminal you can launch the
command in any repository and you will get a window showing the DAG,
uncommitted changes, etc.

I haven't spent much time with TortoiseHG yet, but so far it is a bit
more usable than the other tools I've tried. I do wish that Emacs had
better mercurial support where the graph of changes could be viewed, but
I have a feeling a dedicated app will do a better job creating the
workflow I'd eventually like to establish.

.. _Mercurial: http://mercurial.selenic.com/
.. _TortoiseHG: http://tortoisehg.bitbucket.org/
.. _CVS: http://www.cvshome.org/eng/
.. _WinCVS: http://cvsgui.sourceforge.net/
.. _Araxis Merge: http://www.araxis.com/merge/
.. _Mercurial PPA: https://launchpad.net/~mercurial-ppa/+archive/releases
.. _TortoiseHG PPA: https://launchpad.net/~tortoisehg-ppa/+archive/releases
.. _Launchpad: https://launchpad.net/


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
