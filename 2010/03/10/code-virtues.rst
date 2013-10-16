==============
 Code Virtues
==============

I read this article about `7 virtues of good code`_. A part of me
agrees, especially because the suggestions seem very similar to the `zen
of python`_. At the same time, the virtues are a bit unclear in terms of
what the real goals are.

The first two feel like no brainers to me. The first is that code
should work. This is true on both a practical and meta counts. On a
practical note, broken code breaks builds. So, yes, working code is
important. The second is unique as opposed to duplicated. Avoiding
copy/paste is another good thing. Writing small functions to avoid side
effects and the like is another +1 in my book.

The third is simplicity. I think this is generally a good thing, but
one must be conscious of the fact that constantly moving code out can
have some side effects as well. In languages like Java or C# you get an
editor that lets you go to the class or method definition. In this case
you have almost nothing constraining you from finding a piece of code.
In Python though, the ability to immediately know where code is coming
from drops considerably. This is especially true when you are talking
about passing around functions/callables or objects that implement core
types. Duck typing can really bite you in the end, so while moving code
around to keep things simple is often a good idea, you really need to be
aware that context is important. Moving code can take it out of context,
which has dangers of its own.

The fourth is "Clear, as opposed to puzzling". I'm going to call bs on
this one. It is definitely true good code is clear. How you communicate
what code is doing is a whole other story. The article points out naming
variables and classes is the main aspect of clarity. Wrong! Just because
you name some class effectively or have a relatively easy to read bit of
code, you're not done. Here is an example:

::

    class GettextParer(object):
        def __init__(self...):

        def parse(self, ...):

    # and later

    gt = GettextParser()
    catalogs = gt.parse(some_gettext_file)

    organized_messages = dict([
        (catalog, [msg for msg in msgs if m != ''])
        for catalog, msgs in catalogs
    ])

The thing that is fishy about the code is the why and how. First off
how do you know what sort of data structure you're going to get back
from the GettextParser. How do you even know it returns something?
Secondly, why are you stripping out the empties in the msgs list?
Hopefully some context would help provide the answers, but the fact is
the naming doesn't tell the whole story. The intersection of code,
helpful comments and context all need to work together to gain the
clarity that I'd describe as a virtue.

And as for comments being unnecessary, if you've never gotten the lyric
wrong to a song you enjoy without ever looking, then I'd say you're a
prime candidate for not using comments.

The fifth virtue deals with how easy it is to update some bit of code.
Personally, I believe this is one of the most important metrics for how
well code has been written. This is what makes writing code really hard.
The sixth virtue deals with code being developed and I think that ends
up being a technique used for achieving ease. The better your internal
APIs and models are, the better adding and removing code is going to be.
The last virtue is being brief. I'm all for brevity, but it really is a
side effect. If your code is communicative, there is helpful context
that gets supplemented by meaning comments, then chances are the code
will be a reasonable size. Huge functions definitely smell, but at the
same time helpful comments might make the context and meaning clear. A
long but clear list is better than a black magic and poorly organized
sets of methods.

Overall I think the virtues in the article are more or less agreeable,
but the simplicity bothers me. I think most coders who deal with large
code bases have their personal gripes, but they are probably just that,
personal viewpoints on why something is wrong. The real issue is not so
much the quality of the code. I would argue that should be measured by
how effectively it succeeds solving the user's problem. The real issue
is communication. You need to communicate what the code does if you want
good code. At the same time, if the code works perfectly or close to it,
then it doesn't really matter because no one needs to read it.


.. _7 virtues of good code: http://agileinaflash.blogspot.com/2010/02/seven-code-virtues.html
.. _zen of python: http://www.python.org/dev/peps/pep-0020/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
