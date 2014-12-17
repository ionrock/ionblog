Watching a Log in CherryPy
##########################

Last night I realized that I'm slow switching hats. When there is a
sysadmin type problem, it can be tough for me to immediately know where
to start looking. It is not that I can't figure it out, but rather it
seems to be a difficult transition. My theory on why this can be hard is
because I don't do it very often. My development environment is meant to
be free from sysadmin tasks wherever possible. I've made an effort to
automate as much as I can away, so I can focus on the task at hand. The
downside of this is that I then lose some practice being a sysadmin.

Because of this mental jump that always seems to trip me up, I started
writing a really simple sysadmin server for myself. The idea is that
when the need to switch to the sysadmin world arises, I can run a
command and be off and running watching logs and checking our metrics.

With that in min, I wanted to be able have a link and tail a log file.

My server/framework of choice being CherryPy means that I'm inherently
threaded and streaming responses like this are not well suited to the
model. My resolution then was to find a work around to this problem.

The first thing I did was create a monitoring script. It was easy to
add commands for the logs I'd want to watch, the hard part was starting
up a CherryPy server that served the responses and closed when I stopped
watching them in my browser. Here is what I came up with:

::


    #!/usr/env python
    '''
    A monitor is a web server that handles one request. That one
    request though is one that will return the output of a command and
    stream it as long as the command is running.

    For example, streaming a log to a web browser.

    The script expects an environ variable called PERVIEW_PROC_PORT to
    contain an integer for the port to run the server on.
    '''

    import os
    import sys
    import time

    from subprocess import Popen, PIPE, STDOUT

    import cherrypy

    from cherrypy.process import plugins


    class MonitoredProcessPlugin(plugins.SimplePlugin):

        def __init__(self, bus):
            super(MonitoredProcessPlugin, self).__init__(bus)
            self.bus.subscribe('start_process', self.run_command)
            self.proc = None

        def run_command(self, cmd):
            if not self.proc:
                self.proc = Popen(cmd, stdout=PIPE, stderr=STDOUT)

            def gen():
                while self.proc.poll() == None:
                    yield self.proc.stdout.readline()
            return gen

        def stop(self):
            if self.proc:
                try:
                    self.proc.kill()
                except OSError:
                    pass


    class MonitorServer(object):

        def __init__(self, cmd):
            self.cmd = cmd

        def index(self):
            cherrypy.response.headers['Content-Type'] = 'text/plain'
            p = cherrypy.engine.publish('start_process', self.cmd).pop()
            return p()

        index.exposed = True
        index._cp_config = {'response.stream': True}


    class StopServerTool(cherrypy.Tool):

        def __init__(self):
            super(StopServerTool, self).__init__('on_end_request',
                                                 self.kill_server,
                                                 priority=1)

        def kill_server(self):
            cherrypy.engine.stop()
            cherrypy.engine.exit()


    cherrypy.tools.single_request = StopServerTool()


    def run():

        args = sys.argv[1:]

        if not args:
            sys.exit(1)

        cherrypy.config.update({
            'server.socket_port': int(os.environ['PERVIEW_PROC_PORT'])
        })

        config = {'/': {'tools.single_request.on': True}}
        cherrypy.tree.mount(MonitorServer(args), '/', config)

        # add our process plugin
        engine = cherrypy.engine
        engine.proc_plugin = MonitoredProcessPlugin(engine)
        engine.proc_plugin.subscribe()

        cherrypy.engine.start()
        cherrypy.engine.block()


    if __name__ == '__main__':
        run()


You can run the server with a command like this:

::

    PERVIEW_PROC_PORT=9999 python monitor.py ssh you@server.org tail -F /var/log/myapp.log

I called my app "Perview" for my own "personal view" of some systems.

It is not something I plan on releasing or anything but it is always
good to have a somewhat descriptive directory name.

One thing to note is that I had to create the generator that I would
return in the index method in the same scope as the Popen call. I
suspect the reason being is that when it goes out of scope, the handle
to stdout is released. I used a plugin for creating my process because I
can easily tie it in with the main CherryPy process. By using the
SimplePlugin as a base class and defining the "exit" method, it will
kill the process when the server is asked to stop and exit. The stop and
exit calls happen in a simple tool that waits for the end of a request.

The "on\_end\_request" hook is called after \*everything\* is done in
the request/response cycle so it is safe to do any cleanup there. In the
case where a user just closes the page, the socket eventually times out
and the on\_end\_request hook is called. That takes a little while
unfortunately, so when I do start working on a better UI, part of that
will be to recognize when a user wants to kill the process.

Eventually, it'd be nice to have a more user friendly HTML page that
will make the streamed content a little easier to watch. For example,
making sure it scrolls up and follows the new content coming in.

Hopefully there are already some nice libraries for this sort of thing.

Hopefully this is example shows off some nifty features of CherryPy. I
think the plugin makes a great model for wrapping these kinds of
operations where you have some other processes you need hooked into your
CherryPy server. The hook model is also nice because it allows your
handlers to focus on providing a response. Had I not had the tool and/or
plugin, getting a reliable way to stop the process or know when it
stopped producing output would need a good deal more code.


.. author:: default
.. categories:: code
.. tags:: cherrypy, programming, python
.. comments::
