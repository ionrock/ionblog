Server Buffer Names in Circe
============================

`Circe <https://github.com/jorgenschaefer/circe/wiki>`_ is an IRC
client for Emacs. If you are dying to try out Emacs for your IRC-ing
needs, it already comes with two other clients, ERC and rcirc. Both
work just fine. Personally, I've found circe to be a great mix of
helpful features alongside simple configuration.

One thing that was always bugging me was that the server buffers
names. I use an IRC bouncer that keeps me connected to the different
IRC networks I use. At `work <http://rackspace.com>`_, I connect to
each network using a different username using a port forwarded by
ssh. The result being I get 3 buffers with extremely descriptive names
such as `localhost:6668<2>`. I'd love to have names like
`*irc-freenode*` instead, so here is what I came up with.

First off, I wrote a small function to connect to each network that
looks like this:

.. code-block:: lisp

   (defun my-start-ircs ()
     (interactive)
     (start-freenode-irc)
     (start-oftc-irc)
     (start-work-irc)
     ;; Tell circe not to show mode changes as they are pretty noisey
     (circe-set-display-handler "MODE" (lambda (&rest ignored) nil)))

Then for each IRC server I call the normal `circe` call. The circe
call returns the server buffer. In order to rename the buffer, I can
do the following:

.. code-block:: lisp

   (defun start-freenode-irc ()
     (interactive)
     (with-current-buffer (circe "locahost"
                                 :port 6689
                                 :nick "elarson"
                                 :user "eric_on_freenode"
                                 :password (my-irc-pw))
       (rename-buffer "*irc-freenode*"))

Bingo! I get a nice server buffer name. I suspect this could work with
ERC and rcirc, but I haven't tried it. Hope it helps someone else out!

.. author:: default
.. categories:: code
.. tags:: emacs, irc, circe
.. comments::
