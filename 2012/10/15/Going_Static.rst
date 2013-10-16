==============
 Going Static
==============


I've had a blog for a really long time although it has never been an
ultra important part of my life. Most of the time my blog is simply a
vessel for playing around with different programming languages or
technology. Once again I'm giving a new `blog technology`_ a go.

I got the itch to change a little while back when I realized that I'd
been running the same version of my blog software for a really long
time. The design was boring and I had a huge archive of old blog posts
that were not worth keeping around. I had no real interest in putting
together a better design, but I did want to reduce the amount of
memory I was using on my VPS host. Running any extra services was next
to impossible and it would be nice to try and have a IRC bouncer to
help keep track of the backlog on channels at work.

I backed up my necessary files, reinstalled the OS to start from
scratch and migrated all my blog posts from my Wordpress_ site to
reStructuredText_. I wrote a simple script to format the text files
and make sure the site generation worked as expected. I'm using nginx_
to serve the files and ZNC_ for my IRC bouncer. So far so good!

I had wanted to use o-blog_. It is a blogging system that is similar
to Pelican_ that uses org-mode_ and Emacs_ for generating a static
site. It was a bit more work to get running and required that my
entire blog be in one file. This wasn't necessarily a deal breaker,
but seeing as I didn't have a desire to go crazy customizing some blog
software, I just stuck with Pelican as I had given it a try a little
while back. At some point I'd like to try and write some essays or
more indepth documentation where I could probably use org-mode's
publishing feature.

There is still a bit of work to do making sure old feed links work,
but for now I'm pretty happy with how things are working. It didn't
take forever to set up and it should be easy to archive and start
fresh should another tool strike my fancy.

.. _blog technology: http://getpelican.com
.. _Wordpress: http://ionrock.wordpress.com
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _nginx: http://nginx.org
.. _ZNC: http://www.znc.in
.. _o-blog: http://renard.github.com/o-blog/
.. _Pelican: http://getpelican.com
.. _org-mode: http://orgmode.org
.. _Emacs: http://www.gnu.org/s/emacs/


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
