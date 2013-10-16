Emacs, Email and Mu
###################

I've once again ventured into the world of using Emacs as my email
client. The problem with email is that is a messaging and event
platform. You have actual messages you are sent from real people and
then there are the host of services that use your inbox as a user
interface. When email becomes out of control and you are a programmer
with a powerful editor like Emacs, it makes you consider a world where
you don't have to don't have to leave your editor and you can use all
the slick tricks you have for editing text for managing the massive
amount of email.

In the past I was a reasonably happy `Wanderlust`_ user. I've given
`Gnus`_ plenty of tries, but never have felt comfortable using it. Tools
like VM, RMail and Mew all have not made the cut, primarily because
installation is painful. This time around I'm giving something new and
different a try, `mu4e`_.

Mu4e is built on the email indexing tool `Mu`_. I've used Mu in the past
for searching through archives when Wanderlust wasn't really up to the
task. At the time I was using Linux for my desktop and it came with a
simple GUI that made it really easy to find what I was looking for. When
I `found out about mu4e`_ and that it was being worked on by
`emacs-fu`_, it seemed like it could be what I was looking for.

Mu4e is based on searching for your mail. Mu it is a simple `Xapian`_
index for your mail messages. It's really fast and handles tons of email
really quickly. It uses `Maildir`_ directories for reading mail, which
means it is well suited for use with `Offlineimap`_. The mu4e package
allows you to call a command prior to reindexing your maildir. Mu4e will
also refresh the index every so often to keep your messages up to date.

For sending messages I opted to use `msmtp`_, which was easier to
configure with multiple servers. After moving my work email over, it
seemed like it'd be a good idea to have my personal email in Emacs as
well.

Here is what my config looks like. I'm still tweaking things, but
overall, I'm pretty happy and things feel rather natural.

::

    (require 'mu4e)
    (setq mu4e-debug t)
    (setq mu4e-mu-binary "/usr/local/bin/mu")
    (setq mu4e-maildir "~/Mail") ;; top-level Maildir
    (setq mu4e-sent-folder "/Sent") ;; where do i keep sent mail?
    (setq mu4e-drafts-folder "/Drafts") ;; where do i keep half-written mail?
    (setq mu4e-trash-folder "/Deleted") ;; where do i move deleted mail?
    (setq mu4e-get-mail-command "offlineimap")
    (setq mu4e-update-interval 900) ;; update every X seconds
    (setq mu4e-html2text-command "w3m -dump -T text/html")
    (setq mu4e-view-prefer-html t)
    (setq mu4e-maildir-shortcuts
             '(("/YouGov/INBOX"     . ?i)
               ("/GMail/INBOX"   . ?g)
               ("/YouGov/archive" . ?a)
               ("/YouGov/error emails" . ?e)))

    (setq mu4e-bookmarks
          '( ("flag:unread AND NOT flag:trashed" "Unread messages"      ?u)
             ("date:today..now"                  "Today's messages"     ?t)
             ("date:7d..now"                     "Last 7 days"          ?w)
             ("mime:image/*"                     "Messages with images" ?i)
             ("\"maildir:/YouGov/error emails\" subject:paix" "PAIX Errors" ?p)
             ("\"maildir:/YouGov/error emails\" subject:ldc" "LDC Errors" ?l)))


    (setq w3m-command "/usr/local/bin/w3m")

    ;; sending mail
    (setq message-send-mail-function 'message-send-mail-with-sendmail
          sendmail-program "/usr/local/bin/msmtp"
          user-full-name "Eric Larson")

    ;; Choose account label to feed msmtp -a option based on From header
    ;; in Message buffer; This function must be added to
    ;; message-send-mail-hook for on-the-fly change of From address before
    ;; sending message since message-send-mail-hook is processed right
    ;; before sending message.
    (defun choose-msmtp-account ()
      (if (message-mail-p)
          (save-excursion
            (let* 
                ((from (save-restriction
                         (message-narrow-to-headers)
                         (message-fetch-field "from")))
                 (account 
                  (cond 
                   ((string-match "eric.larson@yougov.com" from) "yougov")
                   ((string-match "eric@ionrock.org" from) "gmail")
                   ((string-match "ionrock@gmail.com" from) "gmail"))))
              (setq message-sendmail-extra-arguments (list '"-a" account))))))
    (setq message-sendmail-envelope-from 'header)
    (add-hook 'message-send-mail-hook 'choose-msmtp-account)

What I like most is the speed at which I can load up messages and find
what I'm looking for. Offlineimap has been a bit flaky at times, but I'm
hoping I can continue to tweak my settings there to be sure I'm getting
my mail in a timely fashion. If you don't use Emacs but you have a lot
of mail you want to analyze programatically, I encourage you to take a
look at mu.

.. _Wanderlust: http://www.gohome.org/wl/
.. _Gnus: http://gnus.org
.. _mu4e: http://www.djcbsoftware.nl/code/mu/mu4e/index.html
.. _Mu: http://www.djcbsoftware.nl/code/mu/
.. _found out about mu4e: http://emacs-fu.blogspot.com/2012/02/regular-emacs-fu-programming-will.html
.. _emacs-fu: http://emacs-fu.blogspot.com/
.. _Xapian: http://xapian.org/
.. _Maildir: https://en.wikipedia.org/wiki/Maildir
.. _Offlineimap: http://offlineimap.org/
.. _msmtp: http://msmtp.sourceforge.net/


.. author:: default
.. categories:: code
.. tags:: emacs, programming
.. comments::
