=============================
 Some Recent jQuery Thoughts
=============================

After a rather long stretch I've finally got back into programming more
with Javascript, which essentially means a whole bunch of `jQuery`_.

Unfortunately, I've been stuck using a rather old version. The result is
that I do miss out on some improvements that would have been helpful.
All things considered though, jQuery is a library that I believe has
stood the test of time.

The big win with jQuery is the DOM. The DOM sucks. Imagine a world of
I/O where you could almost never be sure the file handle you're reading
from is accurate and you can begin to see some problems with the DOM.
Thank goodness though for jQuery, as it makes the vast majority of the
DOM bearable. Some things I'm specifically a fan of are:

-  `The Data API`_
-  `Selectors`_
-  Chaining

The Data API makes it possible to have a persistent store for keeping
data both globally and specific to elements. While the version of jQuery
that I was using didn't have this feature, implementing a temporary
version was trivial. This concept is insanely valuable because you have
a simple consistent way to store information that is specific to
elements. This use case is the critical one since the rest of jQuery all
focuses on elements through selectors. There is a single pattern in
jQuery that one could compare to a command line interface. If you pass
in some HTML, you'll get an element back. If you pass in a selector, you
get an element. If you want to filter a set of elements, grab a subset
or do anything else with some set of elements, just use selectors. I'm
generalizing here by "selector" to mean anything you pass to the "$"
function. Chaining, lastly, is helpful not so much because you can chain
calls, but rather because it provides a protocol for performing an
operation on one or a set of elements. The newer widget APIs abstract
this away, but the patterns have been present forever and while I've
been confused in the past with them, I've come to really appreciate how
it works and supports the rest of the framework.

The amazing thing about jQuery is not so much the set of features but
rather how it did such a great job nailing the key feature. Web
development is all about DOM manipulation and traversing. Almost every
feature helps to make one of the stickier problems of web development
easier, which is why jQuery is such a successful framework. In Python
list comprehensions have become a central optimization alongside dicts.
The choice provides a huge bang for your buck and I believe jQuery's
focus on the DOM provides the same returns.

Gushing praises aside, there are some other areas that I'd hope to see
some optimizations. As I `mentioned before`_, my recent worked involved
removing `MochiKit`_. In going through some of the code it became clear
that MochiKit had some rather interesting features. One specifically I
appreciated was the partial function. A partial was just an easy way to
return partially applied function. Mapping a usage of partial to jQuery
was pretty simple. It was just an in-line function. Here is an example:

::

    // Mochikit
    $('#foo').click(partial(handle_click, 'bar'));

    // jQuery or just not MochiKit
    $('#foo').click( function () { handle_click('bar'); });

This doesn't really reflect why the idea is powerful. In fact, I would
argue the latter is clearer in what is happening. The only thing that
really interests me about the partial function is that it provides an
optimization point. There is a good deal of overhead with using
anonymous functions because the machine/vm instructions can't be saved
by the interpreter. The result is that attaching an anonymous function
to a control that fires frequently means the interpreter spends a large
amount of time re-interpreting that function's code.

It is pretty common to extensive use of anonymous functions within
jQuery code. The common idiom for plugins is that a dict is use for
arguments and it can be really easy to just do things like:

::

    $('#foo').my_plugin('run', {
        success: function () { 
            // do other things...

        }
    });

Honestly, I like the style a lot. But, it would be nice if jQuery had a
way to cache that function reference so the interpreter could avoid
having to recompile it all the time. I'm not sure how it would be
implemented, but it seems like another effective place to optimize.

Maybe something like this that further abuses the $ function:

::

    // I can't imagine this would work effectively... but who knows
    $('#foo').my_plugin('run', {
        success: $( function () { 
            // do other things...

        })
    });

    // a terrible implementation idea?
    if ($.isFunction(selector)) {
        if (!$._cache_methods[selector]) {
            $._cached_methods[stringified(selector)] = selector;
        } 
        return $._cache_methods[selector];        
    }

Another thing MochiKit did that was interesting to me was contexts
within the DOM. You could define a block of code (usually using an
anonymous function) that let to make sure whatever operations would be
performed within that document's context. The interesting thing about
this is that it is another use case that would be helpful within the
scope of jQuery code. jQuery does a good job of utilizing "this" within
things like the $.each function. Having a way to do $.with and sets what
"this" should be within the context of the calling method would be
helpful avoiding some of the confusion that can happen using "this". The
data API helps this situation because you have the ability to use that
as a context, but at the same time constantly using
``$('#foo').data('key')`` means constantly going through the $ function,
while saving the value as a new variable might not be an appropriate
solution since it may get overwritten or changed.

I could be totally off the mark with my context idea, but I do think
providing syntax for caching anonymous functions would be kind of slick.
At the same time it doesn't take much to save the function as a
variable, so I can't imagine I'll see it. In any case, I think it is a
popular way of writing code that if optimized might help improve
performance across the board. Or not ;)

.. _jQuery: http://jquery.com
.. _The Data API: http://api.jquery.com/category/data/
.. _Selectors: http://api.jquery.com/category/selectors/
.. _mentioned before: http://ionrock.org/blog/2010/04/03/Refactoring_Code
.. _MochiKit: http://mochikit.com


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
