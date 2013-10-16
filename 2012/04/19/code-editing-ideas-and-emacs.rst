Code Editing Ideas and Emacs
############################

I saw a `Kickstarter`_ campaign for `Light Table`_ and it got me
thinking. First, I started thinking about how the code I work on is
organized.

The code is Python, which means that files must adhere to the importing
rules defined by the language. It also means there are some known
metadata files we use to help our software play nice in a packaged
environment. When I compare our Python code with something like Java or
C# in terms of files, there is a pretty stark difference. Java (and to a
lesser extent C# if I remember correctly) requires a rather strict
association of one file per class. Python, on the other side of the
spectrum, requires nothing more than one file in its most extreme case.

Thinking about this in terms of actually working on code, it makes me
wonder why you see such a stark difference that seems to be paralleled
in its community. Java and C# enjoy powerful IDEs that are able to
maintain in-depth discovery of the code and allow extreme refactoring
using nothing more than simple dialogs. Python (and other languages like
Ruby, Perl and to a lesser extent PHP) is typically coded in an all
purpose editor. Navigating the set of modules is often done by searching
be it by everyone's close friends grep and find or within the editor
itself. Refactoring is a function of search and replace vs. identifying
actual references.

Going back to the code I work on, there are files that have 30+ classes
and helper functions where others are closer to Java or C# with one
class. This inconsistency (or flexibility) requires tools that can
handle a wide array of styles, rarely becoming a master of any. Yet,
even though these general purpose editors are the tools of choice, it
makes me wonder if there isn't a better way. More importantly, it makes
me wonder if there isn't a better way using the existing tools.

Personally, I use Emacs (as I've said plenty of times). Emacs is a very
powerful editor and as I've learned to use it and started to dabble in
elisp, the possibilities have only become more evident. When I watched
the Light Table proposal video, I realized that pretty every general
purpose editor is able to understand the concept of a "block" of code.
In Emacs, the different programming modes all provide the understanding
of the syntax to the point that you can always jump to the beginning and
ending of most methods, functions and classes. Emacs also allows you to
"narrow" a view of a file to a specific region. Using these two very
simple models, it seems incredibly simple then to create editing
features like you'd see in Light Table.

Thinking in terms of Emacs specifically, it seemed totally possible to
add a feature to a mode that:

#. Finds a specific function/class/method
#. Creates a "narrowed" view of that block
#. Display it in a new frame or within a buffer arrangement

I gave this a quick try and in a few minutes I was able to select the
class, open a frame and momentarily narrow the region. It didn't quite
work as I had hoped. With that said, for someone with my very limited
elisp experience to even come close to this means two things. One, a
skilled lisper would have a larger bag of tricks to pull from in order
to control the Emacs UI. Two, our generic editors already have the
knowledge needed to help us navigate and edit our code in a more
meaningful way.

My goal here is not to proclaim that I'm starting a new project or will
be attempting to create these Light Table features. But I do plan on
playing around with the idea of viewing blocks of code as a set. I
shouldn't need to adjust the file system layout to support this model as
we've already proven that grep and find are very powerful tools with
powerful text editors gluing things together and providing the last bits
of functionality.

Outside of file and code organization, Light Table and `Bret Victor`_
also suggest creating a space where we can iteratively see our code
execute. These are really slick ideas, but I think our programming
communities are more apt to solve the iterative development problems. If
the language provides an interface to its AST and means of inspecting in
such a way as to provide standard output, conforming that output to a UI
in an editor seems very doable. Again, you're not going to see me
writing any of this code. But, things like PyPy are proof that we are
quickly coming to common conclusions regarding taking code people write
and adjusting it for machines in such a way that we can watch the
transformations happen and visualize exactly what is happening. That may
be something different than the slick demos you see where some graphics
change in real time. In fact, I'm hoping it will be even better where we
can visualize our system scaling or failing as we meet demand.

I should mention that I'm really just thinking aloud here. In encourage
you to check out the Light Table video as it has some pretty concrete
concepts that present a really interesting editing environment. My only
request is that as you watch it, consider how the ideas might be made
available in your very own editor and language of choice. And by all
means, consider donating! I'm just rambling here while the Light Table
project is trying to make reality a truly amazing coding system. I wish
them the best of luck!

Of course, secretly, I hope they end up ditching the web based backend
and just add all these features to Emacs.

.. _Kickstarter: http://kickstarter.com
.. _Light Table: http://www.kickstarter.com/projects/ibdknox/light-table
.. _Bret Victor: http://worrydream.com/


.. author:: default
.. categories:: code
.. tags:: emacs, programming
.. comments::
