My First Cojure Experience
==========================

Clojure_ is a LISP_ built on top of the JVM_. As a huge fan of Emacs,
it shouldn't be suprising that there is a soft spot in my heart for
LISP as well functional programming. The problem is lisp is a rather
lonely language. There are few easily googable tutorials and a rather
fractured community. You have a ton of options (Guile, Scheme, Racket,
CL, etc.) with none of them providing much proof that a strong, long lasting
community exists. It can be rather daunting to spend time trying to
learn a language based on a limited set of docs knowing that it is
unlikely you will have many chances to actually use it.

Of course, learning a lisp (and functional programming) does make you
a better programmer. Learning a lisp is definitely time well
spent. That said, this reality of actually using lisp in the real
world has always been a deterrent for me personally.

Clojure, on the other hand, is a little different.

Clojure, being built on the JVM, manages to provide a lisp that is
contextualized by Java. Clojure doesn't try to completely hide the JVM
and instead provides clear points of interoperability and communicates
its features in terms of Java. Rich Hickey does a great job explaining
his perspective on Clojure, and more importantly, `what the goal
is`_. This all happens using Java colored glasses. The result is a
creator that is able to present a practical lisp built from lessons
learned programming in typical object oriented paradigms.

Idealism aside, what is programming in Clojure really like?

Well, as a python programmer with limited Java experience, it is a
little rough to get started. The most difficult part of learning a
lisp is how to *correctly* access data. In Python (and any OO
language) it is extremely easy to create a data structure and get what
you need. For example, if you have a nested dictionary of data, you
can always provide a couple keys and go directly to the data you
want. Lisp does not take the same approach.

It would be really great if I were to tell you how best to map data in
python data structures into Clojure data structures, but I really
don't know. And that is really frustrating! But, it is frustrating
because I can see how effective the platform and constructs would be
if only I could wrap my head around dealing with data.

Fortunately, Rich gives us some tips by way of `Hammock Driven
Development`_, that seem promising. A common concept within the world
of lisp is that your program is really just data. Cascalog_, a popular
hadoop map reduce framework, provides a practical example of this
through its logic engine. `Here is a decent video
<http://www.youtube.com/watch?v=uuJW3EaN_3Q>`_ that reflects how a
declarative form, where you program really is just data used by a
logic engine. Eventually, I'm sure my brain will figure out how to
effectively use data in Clojure.

Another thing that is commonly frustrating with a JVM for a Python
programmer is dealing with the overwhelming ecosystem. Clojure manages
to make this aspect almost trivial thanks to Leiningen_. Imagine
virtualenv/pip merged with manage.py in Django and you start to see
how powerful a tool it is.

Finally, Clojure development is really nice in Emacs. The key is the
inferior lisp process. If you've ever wanted a Python IDE you'll find that
the only way to reliably get features like autocomplete to work with
knowledge of the project is to make sure the project is configured
with the specific virtualenv. Emacs makes this sort of interaction
trivial in Clojure because of tools like Cider_ that jack into the
inferior lisp process to compile a specific function, run tests or
play around in a repl.

I highly recommend checking out Clojure. Like a musical instrument,
`parens may take a little practice
<http://www.infoq.com/presentations/Design-Composition-Performance>`_. But,
once you get used to them, the language becomes really elegant. At a
practical level you get a similar dynamism as you see in Python. You
also get the benefits of a platform that is fast and takes advantages
of multiple cores. Most importantly, there is a vibrant and helpful
community.

Even if you don't give Clojure a try, I encourage you to watch some of
Rich Hickey's talks online. They are easy to watch and take an
interesting perspective on OO based languages. I've become a fan.



.. _Clojure: http://clojure.org/
.. _LISP: http://en.wikipedia.org/wiki/Lisp_%28programming_language%29
.. _JVM: http://en.wikipedia.org/wiki/Java_virtual_machine
.. _what the goal is: http://www.infoq.com/presentations/Value-Identity-State-Rich-Hickey
.. _Cider: https://github.com/clojure-emacs/cider
.. _Hammock Driven Development: http://www.youtube.com/watch?v=f84n5oFoZBc
.. _Leiningen: http://leiningen.org/
.. _Cascalog: http://cascalog.org/


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
