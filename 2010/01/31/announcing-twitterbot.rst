=======================
 Announcing TwitterBot
=======================

At `work`_ we used IRC. While I'm not sure the original purpose, we
managed to spawn an IRC bot that has become something of an icon in our
corporate culture. It does the normal things like logging for specific
channels and can remember the last time someone said something. It also
can tell you the weather for different areas, stock prices and quite a
few other web service mashup type functions. What is the most fun though
is the karma system it allows. You can motivate (!m or !motivate
$username) which will provide a nice "you're doing good work foo"
message and add to your karma. There are a whole set of karma
incrementors and decrementors that help release a little steam or
provide a nice pick up when you're doing something right. In addition to
karma, there are also quotes. Some come from websites and different
characters, but many are from our discussions.


While I wouldn't say the our bot is necessary, it honestly makes
working remotely a much nicer experience and generally is a lot of fun.
For example, I have a virtual machine that has the same name as my
username. When I would mention it in the chat room it was a little
confusing, so I made a function that would let people know if I said my
username, I actually meant my VM (elarson - The Machine!!!). It is kind
of silly, but I really enjoy it.


With that in mind, it seemed like it would be a lot of fun to have a
similar bot for `Twitter`_. An account that you could ask questions or
tell it to do things for you. Personally, I didn't have to many specific
use cases, but my hope is that others will customize it to suit their
needs. The project/library is called `TwitterBot`_ and is written in
Python.


The basic idea is that you start up the TwitterBot with a configuration
and you can add your own functions to either run periodically or
depending on the content of tweets to the twitter bot's username. It
comes with two example plugins. One is a `delicious`_ tool that lets you
tweet URLs to your TwitterBot and it will post the to delicious for you.
The format is really simple. You just tweet a message, a url and any
tags in the form of ((tags: foo bar)). I stole the tags format from
`Posterous`_, so hopefully it will be somewhat familiar. It will save
the tweet without the URL and tags as the note and make an effort to
find the title of the page. It will also expand any URLs that have
minified so things like edited RTs should be pretty easy to move from
something like a twitter favorite to delicious.


The other tool I added was a period check for new followers. It saves
your follower list in a sqlite database and if there are any new
followers, it will follow that person and send them a direct message
with a simple "Thanks for following!" message. This is really more to be
used as an example of a periodic check. For example, if you wanted to
tweet when some page gets updated or send reminders for events, this
would provide a simple format.


I haven't put it up on the PyPI just yet, but I will do so shortly.

Until then, you can check out the code on `bitbucket`_. To run it you
can do: ::

  python -m twitterbot path/to/config.yaml

The config file is just a YAML file and there is an example in the
package. I'm happy to accept any patches or extensions to help make it
more interesting. That said, if you are interested in making something
that annoys folks, it is probably best to keep it to yourself. For any
questions just leave a comment, send me a message on bitbucket or email.
Thanks!

.. _work: http://yougov.com
.. _Twitter: http://twitter.com
.. _TwitterBot: http://bitbucket.org/elarson/twitterbot/
.. _delicious: http://delicious.com
.. _Posterous: http://posterous.com
.. _bitbucket: http://bitbucket.org/elarson/twitterbot/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
