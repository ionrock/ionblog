===========================
 Wanderlust Folder Filters
===========================

I've been using Wanderlust as my email client within Emacs for a while
now and it now has become pretty natural. Whenever I go back to using
the gmail interface it always feels so slow. While working in Wanderlust
is not the fastest thing, I've noticed that being able to do things like
moving mail messages and working through my inbox is much faster than
doing it on the web page. The reason is that in Wanderlust (WL) you
simply mark messages and then execute the marks. Obviously, if you have
to execute a ton of marks, it takes a while, but that is something you
can run and walk away from.

What would be nicer is if I didn't have to mark so many items. For
example, I get error emails for our applications at work. Some are
really important but many are just notices of some small user errors or
attempts to use incorrect information. There is a ton of mail that comes
in from this (even though we're trying to reduce it) and it can be a
pain to manage.

Enter virtual folders!
WL has a concept of virtual folders, which when I read about it, seemed
to be about making meta folders that included other folders. This seemed
sort of helpful, but I wanted to filter a single folder into more
specific messages without actually having to make new folders. I found
out `this kind of thing is really easy to do`_!
I've been able to now create a filter for the error emails I get from
different data centers:

::

    /subject:othapp1|subject:othapp2|!subject:thisapp/%error-emails

I can further filter on date or flags (unread/read) and get a really
concise overview without much work at all.

Now, I know this is possible in other email clients and there is
nothing revolutionary here. The thing is, most other clients that I've
tried do a horrible job with this. Evolution, for example, was always
extremely slow and would always managed to peak the CPU when using this
feature. The benefit is that I'm getting something closer to Gmail
without having to actually use Gmail. After all, most labels I use tend
to be linked to a filter based on a pretty simple search.

Again, I know none of this is revolutionary. But, when you use
alternative tools it can be eye opening. I have tried to be more
efficient with email in the past and it never really worked out. The
interfaces always caused problems and seemed to need too much attention.
I never wanted to "work" on my email. With Wanderlust, it is now a
function of my editor and more importantly my overall environment.

Checking email is the same as using the terminal, irc or writing code.
Finding virtual folders makes things more efficient as well as provides
a little excitement that once again your environment has been customized
to fit your own needs and not the other way around. Of course, it is
kind of a silly quest to always be adjusting your environment, but that
is partially why programmers are different from other folks.


.. _this kind of thing is really easy to do: http://www.gohome.org/wl/doc/wl_39.html#SEC39


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
