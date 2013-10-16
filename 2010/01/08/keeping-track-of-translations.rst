===============================
 Keeping Track of Translations
===============================

At work we have a rather globally focused set of applications thanks to
our very international company. The requirement for i18n is an
absolutely critical one. The problem is that we haven't yet taken the
steps to handle the issue more elegantly. We've been using `GNU
gettext`_ with some success, but it is becoming apparent that our usage
could be better.


The biggest question in my mind is where and when translations get
built. The way gettext works in a nutshell is you have a .po file that
gets updated with the different translations. That .po file ends up
being used to generate a .mo file. The .mo file is a binary
representation of the translation that gets used when calling gettext
functions. Right now we have a folder in our python module that has a
template .po file for updating the different language .po files. When we
have a new string, we add it to the global .po and run a script to add
it to the language specific ones. The translators then translate the
strings in the file and we generate the .mo files. Both the .po and .mo
files end up in the python module so that it is simpler in deployment.
There are some problems with this system.


First the translators often edit the file more liberally than strictly
adding in the strings. Small things like changing line endings and
adding extra spaces makes for minimal changes, but ruins merges. Second,
patching the files is difficult since things like line number comments
change. This is easy to rectify manually, but using mercurial it ends up
becoming more difficult because the patch is slightly off. Finally, the
generation of the .mo files is anything but automatic. It takes about 5
steps to add a new translation and 3 for updating a translation, all of
which involve manual running of scripts. While it is a pretty minimal
set of steps, it is still something that feels like it's in the wrong
place.


Personally, I'd like to extract the translations from the module. This
would help break the reliance on a specific version of the code and
instead provide a more decoupled way for dealing with the translations.
I'd also like to only keep external .po files in version control and
instead rely on a build or deployment to handle constructing the .mo
files. Doing this means there is no question regarding changes in .mo
files as they don't exist in a repository. Currently, when the .mo file
changes it is unclear whether that was from a merge or compilation. If
you merge the files and see the .mo files as changed, it can be
difficult to know whether that change came from the merge or if you
still need to compile them again against any possible .po file changes.
Forcing the .mo to be something that must always be built reduces the
chance for confusion and issues involving .mo files that aren't actually
in sync with their respective .po files.


While my ideas on the matter seem pretty reasonable, I'd love to see
what others do. Hopefully the lazyweb can help me out in finding some of
the pros/cons with my ideas as well as systems others have used.


.. _GNU gettext: http://www.gnu.org/software/hello/manual/gettext/index.html


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
