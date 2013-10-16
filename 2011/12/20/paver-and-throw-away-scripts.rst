Paver and Throw Away Scripts
############################

I've been making an effort to automate as much as I can recently. Part
of this effort has been to utilize more Unix tools, but as a Python
programmer, it isn't always obvious how to combine the two. `Paver`_ is
a build tool written in Python that aims to be similar to `Rake`_ for
Ruby. If you've ever tried to maintain a Makefile and have felt out of
your element, Paver is a great tool to help bridge the gap. It doesn't
have the same target based design that make does, but in terms of
keeping a collection of operations dealing with files and/or running
processes, Paver does a great job to bridge the gap between Python and
the shell.

Beyond being helpful in builds, Paver provides a great tool for writing
throw away scripts. If you've ever had a task that you needed some code
for that didn't need a full fledged module or package, then a pavement
file can help to keep things organized. Its concept of tasks helps to
keep small operations organized and allows you to keep your code
semi-modular as you hack away. Paver also provides some helpful tools to
make things like command line flags and input simple and direct. If the
throwaway code does end up becoming a module that to needs stick around,
you are one step closer to making it official as Paver provides some
tooling for setuptools.

Using the simple example of examining log messages, I'll show you how
Paver makes the process really simple and intuitive.

First off, you have a log file somewhere you want to copy to your
system. The easiest thing to do would be to copy it via scp. Here is an
example in Paver.

::

    # we'll assume the rest of these examples import this
    from paver.easy import *


    @task
    def grab_logfile():
        sh('scp eric@myhost.org:/var/log/myapp.log .')

The 'sh' function calls a command much like the Popen class. You can
capture the output as well in a variable. Another helpful aspect is that
you can add command line arguments. Here is a good example of how you
can find the package name and version in a Python package.

::

    @task
    @cmdopts([('pkg=', 'p', 'The path to the package')])
    def pkg_name_version():
        if not options.pkg_name_version.get('pkg'):
            print 'I need a package name'

        scratch_dir = path('scratch_dir')
        scratch_dir.mkdir()

        pkg = path(options.pkg_name_version.pkg)
        pkg.copy(scratch_dir)
        sh('tar zxvf %s' % (pkg.basename()), cwd=scratch_dir)
        name = sh('python setup.py --name', cwd=(scratch_dir / pkg.basename())).strip()
        version = sh('python setup.py --version, cwd=(scratch_dir / pkg.basename())).strip()
        print 'Name: %s' % name
        print 'Version: %s' % version

I'm making an assumption that you have a tar.gz package that has the
same name as the package. The code uses a '-p' or '–pkg' flag to get the
package name. It makes a scratch directory where it will copy the tar.gz
into. From there we unpack the tar.gz and ask the package's setup.py to
tell us the name and version.

You can see it is really simple to do things like run commands in
specific directories and capture input as needed. Also, Paver includes a
really handy path library that helps to make path operations more
intuitive.

I haven't really covered anything that isn't in the docs, but hopefully
you can see how some of its tools help make simple throw away scripts
easier. It should also be clear that Paver doesn't make these scripts
perfect. You can see from my example above that in order to provide a
better interface you'd probably want to use something than Paver's built
in command line options support. But for a throw away script, it is
simple and gets the job done. The same goes for the path library.
Sometimes it can be a little verbose at times because you need to be
more specific by using things like the basename or abspath method.
Again, it gets the job done adding just the right amount of framework to
make things easier, not perfect.

The big win with Paver is that you have all the benefits of a Python
environment while having easy access to the shell. Here is an example of
reading and filtering a log file with Popen vs. Paver.

::

    @task
    def read_with_popen():
        log = path('/var/log/app.log')

        p1 = Popen(['tail', '-f', log], stdout=PIPE)
        p2 = Popen(['grep', 'foo'], stdin=p1.stdout, stdout=PIPE)
        p3 = Popen(['grep', '-v', 'bar'], stdin=p2.stdout)

    @task
    def read_with_sh():
        log = path('/var/log/app.log')
        sh('tail -f %s | grep foo | grep -v bar' % log)

You can always redirect the output to some file or you could use the
'capture=True' argument in the 'sh' call to do further processing.
Either method certainly works, but for a quick script, Paver does a
great job utilizing an obvious pattern that allows quick access from
Python.

I've never been a huge advocate of Paver in the past because it didn't
seem like a critical tool, but I'm beginning to become a real fan. It is
a tool that you can live without if you've never had it, but once you
recognize where it excels and you begin to use it, it quickly becomes
indispensable.

.. _Paver: http://paver.github.com/paver/
.. _Rake: http://rake.rubyforge.org/


.. author:: default
.. categories:: code
.. tags:: paver, programming, python
.. comments::
