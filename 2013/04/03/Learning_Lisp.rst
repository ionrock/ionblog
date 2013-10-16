===============
 Learning Lisp
===============


Programming is often an iterative process. When learning new
technology it is often the case the first attempt doesn't work
out. After a little time away, a second look might get you a bit
further in the process. Eventually, the technology stops being
something you are learning and becomes something you are using. This
has been my experience with Lisp.

My first foray was via Emacs of course! I remember the first time I
set out to write a small function to help me paste some code and
managed to make it work. A python script did much of the heavy
lifting, but it was still a breakthrough to be able to select some
text, send it to a process and write the output to a buffer. When I
finally managed to refactor that code to do what the python script
did, it was when I first used Lisp and wasn't strictly learning it.

My most recent Lisping came from trying out elnode_. Elnode is named
after node.js and provides a similar service, an async web server
written in Emacs Lisp. My task was to make a small web UI for some
services that I typically start to work locally. I use a package
called dizzee_ to start services in a similar way as you'd use
foreman_ to start services for development.

I was able to get some HTML returned to the browser and handle some
requests to start up services, which felt pretty good. I also wrote
some advice for dizzee to help keep a data structure with all my
services. Dizzee provides macros that create new functions, so there
isn't a listing you can simply query. Where things fell apart for me
was trying to stream the output of the service. I wanted to be able to
tail the service to my browser, but that proved more difficult than I
hoped.

After hitting a wall, yet appreciating the elegance of writing
application code in lisp, it seemed like a good time to give clojure_
another try. My first attempt at clojure was short lived, primarily
due to my lack of experience in Java. Thankfully, there is leiningen_
to help those without much Java experience use clojure
successfully. In this case I was able to get through a tutorial for
noir_, a clojure web framework. My hope is that I can get some more
time with clojure and noir to create a more involved web app.

What is interesting is that when I returned to Python, my primary
language, it became clear that it feels very comfortable to me. I
rarely need to look things up in documentation. Solving environment
issues such as dependency resolution doesn't require much thought. The
process of coding in Python has become natural. My hope is that
someday I can say the same of lisp.


.. _elnode: http://elnode.org
.. _dizzee: https://github.com/davidmiller/dizzee
.. _foreman: http://blog.daviddollar.org/2011/05/06/introducing-foreman.html
.. _clojure: http://clojure.org
.. _leiningen: http://leiningen.org/
.. _noir: http://www.webnoir.org/


.. author:: default
.. categories:: code
.. tags:: programming, python, lisp, emacs
.. comments::
