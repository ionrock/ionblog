Forcing a Refresh
#################

Web applications are interesting because it is exceptionally challenging
to maintain state. The client and the server act independently and there
very little a web application developer can do to reliably keep the
client and server in perfect sync. Yet, there are times where you need
to sync your client with the server.

When a server API changes it means your client code needs change. When
the update to the server involves multiple processes, there is even more
chance for the client and server to get out of sync. One way to make
sure our client and server processes are in sync is to force the client
to reload its resources. This involves downloading the new versions of
static resources such as JavaScript, CSS and images.

In order to force our client to refresh, we need a couple pieces in
place. First we need to be sure our client communicates what version it
is running. Second we need our client to understand when the response
from the server is indicating we need to refresh. There are other pieces
that can be developed such as a UI explaining to the user what is
happening, but to start this is all we need.

To start we should make sure our client has access to some version
number. The version number is defined by the server and can be evaluated
however you want. An easy way to do add the version is via hidden
element in the HTML. If you wanted to do something clever you could
limit a refresh when there is a major version bump. For simplicity sake,
I'd recommend using the application version and only do simple equality
comparisons when deciding whether to return a refresh error.

Whatever version number is in the HTML needs to be sent to the server on
each request. How you send that data is totally up to you. I've used a
'\_\_version\_\_' named value submitted as a form value. You could have
a \_\_version\_\_ key in a JSON document you post, make it part of the
URL, use a header or use a cookie value. Whatever it is needs to be
understood by the server API.

Once you have a version number being sent by your client, the server
then needs to test whether or not the versions match before returning a
response. If they don't match, then you should send an error message.
For example, you could return a 400 status along with a JSON message
that says to reload the page. It is important that you return an error
to the client rather than simply return a redirect because the client
needs to refresh the page and make sure to avoid cached resources on the
refresh. When the client gets the error message, the JavaScript can call
'window.location.reload(true)' in order to reload the page, avoiding the
cache.

It should be noted that this doesn't avoid using things like timestamps
in the paths to static resources. Making the URL paths reflect the age
of the file is still very helpful as it makes sure that subsequent
reloads will reference completely different resources that are not
cached. The system I've described is focused on reloading the initial
page vs. performing some operation to clear the cache or determine what
resources need to be reloaded. By keeping these concerns separate, we
can keep the implementation simple.

I don't think any of this is extremely difficult, but I think it is a
critical part of any distributed web app. When you release new software
to a cluster of applications, you want to slowly roll it out. This
methodology ensures that as a roll out occurs, your client code can be
upgraded at the same time as well as client code that has become stale.


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
