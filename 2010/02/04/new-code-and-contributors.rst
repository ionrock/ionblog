===========================
 New Code and Contributors
===========================

I read `this blog`_ from one of the `Miro`_ developers that was a
response to `this article`_ on how open source projects can find more
contributors. I `commented`_ on the latter and realized that it might
also warrant a blog post.

I've written a few times on the difficulty working on other people's
code. I read a blog the other day about the mythical 10x productive
developer that claimed that the developer was really productive because
that person had originally written the code. While I have no statistics
on the issue, I bet that guy was more or less correct. It is so much
different diving back into code you wrote versus taking a look at some
unknown bits. Recently, I've been trying to do more work public with my
`TwitterBot`_ and `Dragoman`_ (`RESTful gettext`_). Part of what I'm
realizing is that I'm not that bad a programmer. At work there are
moments where I wonder if I picked the wrong profession. Maybe my mind
just isn't bent the right way to be a programmer. What I'm realizing now
is that working on other people's code is really, **really** hard! You
may never fully understand what is happening under the hood and
sometimes you don't really even need to know.

I think this contrast between working on someone else's code and new
code has a direct relationship to how Open Source projects find
contributors. If a project allows people to write extensions or plugins
easily, it greatly increases the chances of that person eventually
contributing to the core code. A plugin gives a programmer something
that is small enough to do and in most cases, allows that person to
scratch their own itch without feeling any sort of liability or
responsibility to the community. The code works and that is all the
matters. Over time though, that person might try to make that code nicer
and eventually, the next thing you know, that person has dived into the
core code to see why his pet feature is acting odd. What's more, they
are doing so in the context of their own plugin/extension, that they
fully understand. It provides a really nice transition from specific
modular knowledge of some codebase to understanding the core.

I would argue that most successful projects manage to make writing
extensions easy. jQuery is a great example of a project that has a
massive community and a much larger plugin community than core group.
Firefox is another situation where the core C++ application is developed
by a small group, while there are a huge number of extension authors.
Eclipse, Apache, and Rails are all more examples where much of the
community actually lies in its extensions. In the Python world, WSGI
created a huge entry point for developers to write their own middleware
and framework tools. In fact, I might go so far to say that Python would
not have the community it has if it weren't for the modular aspect WSGI
brought to Python web developers.

Where this pluggability becomes difficult is when there is a user
interface. Most projects generally have someone who is a leader and
things like the UI end up being something restricted to the core group.
That said, I think the Eclipse project (along with Emacs, Vim and
TextMate) has done an excellent job exposing extensibility, even at the
UI level.

If you want to run a successful open source project, I honestly can't
tell you how to do it. But, if you make it easy to write plugins or
extensions, then you give developers a means of scratching their own
itch. Nothing motivates better than Jones own selfish desires and
extensibility speaks to this aspect of human nature. There are
definitely cases where systems can become too modular, but that is what
separates the great projects from the others. They have found that sweet
spot for letting people get involved and become effective without
sacrificing the core aspects of the application/library.


.. _this blog: http://bluesock.org/~willg/blog/dev/crowdsourcing.html
.. _Miro: http://www.getmiro.com/
.. _this article: http://hackervisions.org/?p=613
.. _commented: http://hackervisions.org/?p=613#comment-1120
.. _TwitterBot: http://bitbucket.org/elarson/twitterbot/
.. _Dragoman: http://bitbucket.org/elarson/dragoman/
.. _RESTful gettext: http://ionrock.org/blog/2010/01/23/A_RESTful_Gettext


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
