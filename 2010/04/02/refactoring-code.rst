==================
 Refactoring Code
==================

I've spent the last few days updating a rather large Javascript code
base. There are a couple issues I'd like to solve. The first is settling
on one Javascript library, `jQuery`_ in this case. It is currently a mix
of jQuery and Mochikit, where most of the oldest functionality uses
`Mochikit`_ and the newer features, jQuery. The second issue is to write
a new feature to lazy load some of the data it uses in hopes of making
things feel a bit snappier. The big picture though is to get the entire
code base up to a more modern version of jQuery so as to take advantage
of more plugins and the widget features. Once I get thing decoupled from
Mochikit, I'm hoping to do a refactoring to get the code more organized.
Refactoring is a great way to learn a code base. If you force yourself
to go over every line and change things, you often break them. This is a
good thing because for every bug you create, you are given the
opportunity to understand something about the code. It is pretty obvious
that you'll have to see why a certain change broke something. But beyond
that you also end up seeing tons of mundane decisions that were made.
Little things like whether or not to include braces for one line if/else
statements. You see where spaces are added or not added within the
context things like function definitions and variable declarations.

While a lot of these sorts of things are pretty inconsequential things
to pay attention to, they are still important.

The little details help by describing the dialect of the code. Every
author will develop a style. There will be a cadence and rhythm to the
tone of the text. Refactoring helps you to see the style of the code,
which in turn helps in more quickly understanding the code. Knowing an
author's style doesn't help make the message clearer, but it does make
it more palatable. When you start a book you might need to reread small
portions to remember something about characters or situations, but by
the end, assuming you're enjoying yourself, reading becomes a guide for
your imagination. The characters have faces and feelings. The same goes
for code. Refactoring is how you gain the intimate understanding of the
ideas and characteristics of the code, no matter how small.

The other thing I've realized working on this code is that it is better
to refactor earlier. I realize there are time constraints, especially in
a startup scenario, but if possible effort should be spent simply
organizing the code. For the author, it keeps the code fresh and
relevant. For the developers that haven't looked at the code, they get
the benefit of more iterations and potentially seeing the progression of
where the code is going. Using this codebase as an example, the initial
code was pretty much a large set of functions. As things have progressed
in other areas though, jQuery became more pervasive. The most current
code adopts jQuery conventions more thoroughly and uses the $.widget
tools for making that jQuery interactions more convenient. Refactoring
helps to share this story and signifies where new code should be. It
also makes it clear that there is still work to do on the code to bring
everything to a more unified model.

Unfortunately, as helpful as refactoring can be, it is also somewhat
dangerous. There are personal opinions on code quality that are rarely
universal. "If it ain't broke, don't fix it" really does make sense in
the real world of software development. That said, I think the risk is
eventually worth it. Testing, which is a good thing, is one great way to
prevent breaking things through refactoring. Sometimes refactoring can
even be beneficial in finding new bugs or use cases that were not
considered before.

The important thing about refactoring is that you get to know the code
better. Even if you try and fail, you've learned more about the code.
The intent might be clearer and you've started to see the author's
cadence and style. When learning a code base, failing at refactoring is
going to be common, but still helpful. And when you've been working on
some code for years, refactoring can help reinvigorate a stale codebase.

.. _jQuery: http://jquery.com
.. _Mochikit: http://mochikit.com


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
