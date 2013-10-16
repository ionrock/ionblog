=================
 Hosting Changes
=================

I've had a VPS host since 2007 in order to run Python web apps. The
reasoning is that most shared host, in addition to killing long
running processes, rarely made it easy to create your own
environment. I'll remind you, this was in the early stages of
virtualenv and there were still hairy tutorials on how to get a Python
WSGI process running on Dreamhost.

Since then the landscape has changed quite a bit. There are far more
hosts that support long running processes. There are services such as
Heroku that make deployment of Python apps a cinch. VPS hosting has
also become more common and easy to get up and running.

Beyond the technical differences, the biggest reason I switched from
`VPS Link`_ to `Digital Ocean`_ was because of the price. As anyone
who has used a VPS, ram is a fleeting resource. With only 256MB
running any LAMP stack is pushing the limits. Nevermind being able to
use something like MongoDB or some other more interesting NoSQL
store. I'm now spending $10 a month for a gig of memory where I was
spending $25 a month for 256MB. It was a no brainer.

The other change is that I've switched from Pelican_ to Tinkerer_ for
my blog. I'm not positive I'll stick with it since sometimes it is
nice to have the WordPress infrastructure in place. Now that I can
actually run a database, I wouldn't mind switching back. For the time
being though, I'm going to check out Tinkerer and write some elisp to
make using it easy in Emacs.


.. _Pelican: http://docs.getpelican.com/en/3.3.0/
.. _Tinkerer: http://tinkerer.me/
.. _VPS Link: http://vpslink.com/
.. _Digital Ocean: https://www.digitalocean.com


.. author:: default
.. categories:: code
.. tags:: programming, cloud
.. comments::
