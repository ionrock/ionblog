Quality Libraries
#################

Have you ever read about a slick library that someone just released and
thought how awesome it is, yet you don't immediately start using it?

This happens to me all the time. People are constantly releasing
interesting code that seem applicable to the projects I work on. Yet,
even though it seems like a decent solution to problems I'm having, I'll
rarely try it out.

The reason is pretty simple. It takes time to learn some library and it
takes experience to understand it well enough to make a qualified
decision. If I tried all the libraries that I saw, nothing would get
done! The converse to this is that I'm missing out on some packages that
actually would be a good fit.

This issue came up when I read about `Obviel`_, a JavaScript
view/template library. We are currently in the process of migrating many
services from being a mix of RPCs and HTML base Ajax to a more RESTful
platform. Obviel seemed like a pretty slick solution. The blog post I
read about it also mentioned `Fantastic`_, which seemed like another
slick tool to help with static resources. Even though both seem like
interesting solutions, the doubt comes up in my head that they will
continue to be maintained or that I will choose these packages only find
a killer bug sometime down the line that causes us to switch.

The reality is I have a classic case of NIH syndrome. When code is open
source/free software my level of comfort should be high. I can always
try to fix my own bugs. I can always take bits and pieces if need be to
make something customized. If we have to switch 6 months or a year down
the line, that is OK. That is 6 months to a year of time that we got for
free because we didn't have to write or maintain some code.

I'm going to try and make an effort to try out the packages that look
interesting to me. I did spend some time with `Backbone.js`_ and
`Underscore.js`_, both of which were very nice. The packages mentioned
above seem really interesting and might fit extremely well in our
homogenous environment built on CherryPy. Instead of being worried about
the bad things happening, it seems much better to just give things a
try.

.. _Obviel: http://www.obviel.org/en/latest/index.html
.. _Fantastic: http://fantastic.org
.. _Backbone.js: http://documentcloud.github.com/backbone/
.. _Underscore.js: http://documentcloud.github.com/underscore/


.. author:: default
.. categories:: code
.. tags:: cherrypy, javascript, programming, python
.. comments::
