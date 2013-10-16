Writing and Testing Code
########################

Throughout the years my methodology for writing code has changed quite a
bit. I've tried tons of editors and IDEs and jumped back and forth from
gui tools to the command line many times over. Since settling on
`Emacs`_ and learning some of its features it has become clearer the
common thread that flows between all the different tools.

The most obvious thread is compiling code. Since we use Python at work,
we don't actually "compile" things, but we do test them which happens to
produce errors very similar to compilation. Fortunately, Emacs has a
very handy compilation mode that helps to make the process very fluid.

When I'm writing code my basic iterative process is to create a test
that is re-run each time the code changes. Using `Pytest`_ I'm able to
do just that. This pytest process runs in a compilation mode buffer and
allows me to jump between the different exception / error file points
and immediately open that file to the line where the error occurred.

The key is making these tests run quickly as possible. In order to do
this, I use what I call a `Dev Server`_ that keeps the test instances of
any services up and running. It makes sure my databases are started
along side any service that I might be testing. This way my test suite
doesn't shut down a database and reinstall any stub data for running a
single test that might not need the service in the first place.
Likewise, for the tests that need a good deal of orchestration, all the
services are already up and running.

The whole process is pretty well integrated. If want to paste a
traceback or some code, I have some lisp code to paste to our internal
pastebin. I can then paste it in IRC which is also running in Emacs via
`ERC`_. I can even use a tool like `pdb`_ to debug directly in Emacs,
opening the current file where the execution was paused.

Before finding the compilation mode I ran tests in a shell buffer or in
a terminal. The problem with this was that it was never trivial to find
initial test error or see what failed. I would search around to find the
error but sometimes tracebacks were extremely long and even include a
"pretty" version that added to the visual clutter.

There is still more I can probably do help make my testing experience
more helpful, but for now I'm relatively happy. One thing that I've
noticed is that many times my quest to write tests is partially used as
a means to avoid switching to a web browser. While in theory this is a
good optimization, I've found myself needlessly avoiding firing up the
application and dependencies even though my dev server handles that for
me just fine.

.. _Emacs: http://www.gnu.org/s/emacs/
.. _Pytest: http://pytest.org/
.. _Dev Server: http://ionrock.org/blog/2011/10/11/The_Development_Server_and_Porting_A_Test_Suite_to_Nose
.. _ERC: http://www.emacswiki.org/emacs/ERC
.. _pdb: http://docs.python.org/library/pdb.html


.. author:: default
.. categories:: code
.. tags:: emacs, programming, python
.. comments::
