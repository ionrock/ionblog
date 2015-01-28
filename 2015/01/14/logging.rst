Logging
=======

Yesterday I fixed an issue in `dadd
<https://github.com/ionrock/dadd>`_ where logs from processes were
being correctly sent back to the master. My solution ended up being a
rather specific process of opening the file that would contain the
logs and ensuring that any subprocesses used this file handle.

Here is the essential code annotated:

.. code-block:: python

  # This daemonizes the code. It can except stdin/stdout parameters #
  # that I had originally used to capture output. But, the file used for
  # capturing the output would not be closed or flushed and we'd get #
  # nothing. After this code finishes we do some cleanup, so my logs were
  # empty.
  with daemon.DaemonContext(**kw):

      # Just watching for errors. We pass in the path of our log file
      # so we can upload it for an error.
      with ErrorHandler(spec, env.logfile) as error_handler:
          configure_environ(spec)

	  # We open our logfile as a context manager to ensure it gets
	  # closed, and more importantly, flushed and fsync'd to the disk.
          with open(env.logfile, 'w+') as output:

	      # Pass in the file handle to our worker will starts some
	      # subprocesses that we want to know the output of.
              worker = PythonWorkerProcess(spec, output)

	      # printf => print to file... I'm sure this will get
	      # renamed in order to avoid confusion...
              printf('Setting up', output)
              worker.setup()
              printf('Starting', output)
              try:
                  worker.start()
              except:
                  import traceback

		  # Print our traceback in our logfile
                  printf(traceback.format_exc())

		  # Upload our log to our dadd master server
                  error_handler.upload_log()

		  # Raise the exception for our error handler to send
		  # me an email.
                  raise

              # Wrapping things up
              printf('Finishing', output)
              worker.finish()
              printf('Done')

Hopefully, the big question is, "Why not use the logging module?"

When I initially hacked the code, I just used `print` and had planned
on letting the daemon library capture logs. That would make it easy
for the subprocesses (scripts written by anyone) to get logs. Things
were out of order though, and by the time the logs were meant to be
sent, the code had already cleaned up the environment where the
subprocesses had run, including deleting the log file.

My next step then was to use the logging module.

Logging is Complicated!
-----------------------

I'm sure it is not the intent of the logging module to be extremely
complex, but the fact is, the management of handlers, loggers and
levels across a wide array of libraries and application code gets
unwieldy fast. I'm not sure people run into this complexity that
often, as it is easy to use the `basicConfig` and be done with it. As
an application scales, logging becomes more complicated and, in my
experience, you either explicitly log to syslog (via the syslog
module) or to stdout, where some other process manager handles the
logs.

But, in the case where you do use `logging`, it is important to
understand some essential complexity you simply can't ignore.

First off, configuring loggers needs to be done early in the
application. When I say early, I'm talking about at import time. The
reason being is that libraries, that **should** try to log
intelligently, when imported, might have already configured the
logging system.

Secondly, the propagation of the different loggers needs to be
explicit, and again, some libraries / frameworks are going to do it
wrong. By "wrong", I mean that the assumptions the library author
makes don't align with your application. In my `dadd`, I'm using
`Flask <http://flask.pocoo.org/>`_. Flask comes with a handy
`app.logger` object that you can use to write to the log. It has a
specific formatter as well, that makes messages really loud in the
logs. Unfortunately, I couldn't use this logger because I needed to
reconfigure the logs for a daemon process. The problem was this daemon
process was in the same repo as my main Flask application. If my
daemon logging code gets loaded, which is almost certain will happen,
it reconfigures the logging module, including Flasks handy
`app.logger` object. It was frustrating to test logging in my daemon
process and my Flask logs had disappeared. When I go them back, I
ended up seeing things show up multiple times because different
handlers had been attached that use the same output, which leads me to
my next gripe.

The logging module is opaque. It would be extremely helpful to be able
to inject at some point in your code a `pprint(logging.current_config)`
that will provide the current config at that point in the code. In
this way, you could intelligently make efforts to update the config
correctly with tools like `logging.config.dictConfig` by editing the
current config or using the `incremental` and
`disable_existing_loggers` correctly.

Logging is Great
----------------

I'd like to make it clear that I'm a fan of the logging module. It is
extremely helpful as it makes logging reliable and can be used in a
multithreaded / multiprocessing environment. You don't have to worry
about explicitly flushing the buffer or fsync'ing the file handle. You
have an easily way to configure the output. There are excellent
handlers that help you log intelligently such as the
`RotatatingFileHandler`, `WatchedFileHandler` and
`SysLogHandler`. Many libraries also allow turning up the log level to
see more deeply into what they are doing. `Requests
<http://docs.python-requests.org/en/latest/>`_ and `urllib3
<http://urllib3.readthedocs.org/en/latest/>`_ do a pretty decent job
of this.

The problem is that controlling output is a different problem than
controlling logging, yet they are intertwined. If you find it
difficult to add some sort of output control to your application and
the logging module seems be causing more problems than it is solving,
then don't use it! The technical debt you need to pay off for a small,
customized output control system is extremely low compared to the
hoops you might need to jump through in order to mold logging to your
needs.

With that said, learning the logging module is extremely
important. `Django <https://djangoproject.org>`_ provides a really
easy way to configure the logging and you can be certain that it gets
loaded early enough in the process that you can rely on it. Flask and
`CherryPy <http://cherrypy.org>`_ (and I'm sure others) provide hooks
into their own loggers that are extremely helpful. Finally, the
`basicConfig` is a great tool to get started logging in standalone
scripts that need to differentiate between `DEBUG` statements and
`INFO`. Just remember, if things get tough and you feel like your
battling `logging`, you might have hit the edges of its valid use
cases and it is time to consider another strategy. There is no shame
in it!

.. author:: default
.. categories:: code
.. tags:: python, logging
.. comments::
