Broken Python Packaging
#######################

Over the weekend I took some time to take a project at work and try to
build a set of binary packages. My goal was to be able to untar a
package into a virtualenv and it work correctly. This isn't that
different from distributing egg packages or a RPM, so I figured it would
be pretty easy.

My first step was to determine all its requirements. To do this, I
created a blank virtualenv and installed my app. I then used pip freeze
to record all the eventual requirements. Again, my goal was to have a
set of package like files that can be untarred (or something similar)
that will install the files in the virtualenv correctly such that I
don't need to perform some sort of build (compile C extensions for
example) or get other requirements.

Having my requirements in place, I then starting downloading their
packages from our local cheeseshop using pip's "–no-install" flag.
Again, this was very convenient and felt promising.

Once everything was downloaded, my script would then visit each package
and try to build a binary package. I tried quite a few options here but
none seemed to work correctly. The biggest problem was that each package
had some inconsistencies that made using the same command for all of
them fail. One package gave an odd character error when trying to create
a tar.gz. Another didn't recognize different bdist formats. Trying an
RPM format on a whim was useless. Taking a step back I tried doing a
"build" of each package and manually putting them together in a tar, but
that was non-trivial and different per-package.

I'm going ahead and giving up for the time being as it is clear that
Python packaging currently has a requirement to use source vs. pre-built
packages. This is really too bad because often times distributing source
and forcing your end-user system to have the necessary tools makes a
package unusable. In my case it means that releasing a new deployment
requires running the through the entire setuptools process for each
package that gets installed. The benefit of avoiding this process is
that you reduce the number of variables present when deploying. This
makes a deployment much faster, which becomes more and more important in
a distributed environment.

Hopefully with distutils2 and Python 3 the community can find some
better solutions for packaging. I understand that the source based
installation makes a lot of sense in development and even in many
production environments, but that shouldn't make a consistent binary
package system impossible.


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
