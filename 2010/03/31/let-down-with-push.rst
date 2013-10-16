====================
 Let Down with PuSH
====================

In the `CherryPy`_ IRC channel, I heard about an async framework called
`Circuits`_. While I'm still in the midst of getting well versed in
`Diesel`_, it occurred to me that I don't really have a go to idea for
what to implement when learning an async framework. In the past I would
often write a blogging system to learn a new language, but even that
became somewhat tired once I started learning more esoteric languages.
The benefits of functional languages and async frameworks is that they
can scale. So what is a project that has some obvious scaling issues out
of the gate.

What I came up with was PubSubHubBub (PuSH). The idea of PuSH is that
you have a server that listens to content producers and potentially
multiplies that content to a huge set of subscribers. I don't know that
a PuSH server really needs to scale, but I'd imagine that if one content
producer becomes popular, the multiplier for that content's subscribers
seems could balloon easily. With that in mind, after looking at the
spec, I'm pretty let down.

I can accept that it uses XML. Google is pretty dedicated to Atom and
while I've most definitely moved on from building systems with XML, it
has its positives. That said, the idea of PuSH is to notify subscribers
of changes to content. The content is a resource, so it seems somewhat
odd that the protocol requires that the server to do a diff of new
content in order to push the changes to the subscribers. Finding the
differences in XML, even in a known format like Atom, is very difficult.
If there was an understanding that the document should be able to be
diff'd by lines and characters, then it wouldn't really bother me. The
system could be built on patches in a way that is similar to the
distributed version control systems. But that is not how it works. The
PuSH server has to analyze the content, find the differences and send it
along to the subscriber.

From an efficiency standpoint, passing around changes is helpful in
reducing the payload, but again, differences in XML is difficult. Just
as deep object comparisons can be costly, so are finding XML
differences. Maybe in practice it is not that hard or a problem, but
personally I'd rather not find out. I suppose reducing the payload might
be more beneficial than lowering the processing time in terms of
providing realtime updates.

What I think makes a better model would be much lighter. First off, the
payload would be `JSON`_. It is easier to work with. Second, the most
important aspect of the payloads would be the URLs. The goal would be to
send a signal instead of a payload. The realtime requirement seems
difficult over the web. Sending two medium sized payloads instead of two
really small payloads and the content feels much better to me. If the
system will have a set number of subscribers that will always be
present, then yes, sending the diff'd payload makes sense. But in the
case where you are supporting many subscribers, but very few truly
require realtime updates, the extra latency would be negligible.

But back to my system idea. The payload to the signal server (I just
named it this) would be a URL to the content that changed. The
subscribers would be notified via a ping that might use the Location
header to signify where to get the update. If the signal server is meant
to be used a caching proxy, that could point back to the signal server
URL or it could point back to the original source. The subscriber,
assuming it needs the data right then and there, can fetch it.

I think the biggest benefit is that the system is so simple.

Implementing it on a small level using an intranet makes a ton of sense,
while large scale implementations would have the benefit of being able
to use something like an `nginx`_ plugin or some other simple module
written in C that piggybacks a well tested server.

I'm going to try an implement this kind of service as my example
application for async/functional languages. It should be easy enough to
do without having to get involved in library monotony while still
presenting enough problems to make it worthwhile. I'd also hope that in
fleshing out the idea, it might present another option in the world push
based systems.


.. _CherryPy: http://cherrypy.org
.. _Circuits: http://bitbucket.org/prologic/circuits/wiki/Home
.. _Diesel: http://dieselweb.org
.. _JSON: http://json.org
.. _nginx: http://nginx.net


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
