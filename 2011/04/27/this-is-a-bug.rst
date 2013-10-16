This is a Bug
#############

If you've ever programmed in Javascript, you've obviously dealt with
"this". In some ways, "this" is a pretty powerful concept because it
lets you have a dynamic context. Where the idea excels is with events
and DOM. At least that is where I think using "this" is really slick.
Where "this" falls apart though is when you use it in a similar way to
Python's "self" concept. More generally, when you have an object and you
want to reference that objects variable within a function of that
object. Here is a really simple example. ::

  var Foo = function () {
    this.bar = 'hello world';
  }

  Foo.prototype.handler = function (evt) {
    console.log(this.bar);
  }

  Foo.prototype.connect = function () {
    some_object.bind('my_event', this.handler);
  }

The idea here is that when you fire some event 'my\_event' the Foo
object's 'handler' function is called and prints the Foo objects 'bar'
value, which is 'hello world.' That is the idea anyway. What really
happens though is that when you do fire that event, the "this" ends up
referencing 'some\_0bject' instead. Unless 'some\_object' also has a
'bar' variable, it will print null.

On the one hand this is really cool. Again, it is a really effective
model for DOM events. At the same time though, it is really sort of a
pain in neck to write more organized objects because you have some hoops
to jump through in order to change what "this" references. In fact there
are plenty of examples where a library or tool tries to make this
easier.

`jQuery.proxy`_ is one example that lets you set the value of "this" in
a function. `Coffee Script`_, which is something I've been playing with
lately, has a slightly different function operator (=>) that will keep
the value of "this" as the parent object instead of using the calling
function. `Backbone.js`_ is another tool that aims to solve a similar
problem in that it provides a more typical object model where it is most
effective, defining Models. The point being is that others have hit this
same "bug" and had to work around it.

Obviously, the behavior of "this" shouldn't really change. And the fact
that there are work arounds provided by libraries just means that it
doesn't have to be too big a deal. Still, I wish that there was a simple
way to access an object's method or attribute more reliably within
Javascript. The other option is to construct more clear best practices
regarding organizing code that doesn't rely on typical objects. Not
being a Javascript guru, I'm sure others have come up with solutions to
both questions. Maybe I just need to look a little harder.

As an aside, I've been playing around with Coffee Script. It is a bang
up great idea if you ask me. They have managed to create a language that
is still Javascript in that it works with other libraries and tools, yet
it manages to add some of the most helpful macros to make things
simpler. Creating Classes is one example where it excels with things
like list comprehensions and better looping being another huge win. What
is also exciting to me is that it compiles to really basic Javascript.
The result is that you don't see code generated that is based on a
library or framework. Instead you get plain old Javascript. In this way
it becomes a simple way to abstract the structure and code while still
optimizing the code by using straight Javascript. If you've ever needed
to do things like process data in Javascript you'll find that using
something like jQuery can be slow at times compared to plain JS. Coffee
Script takes a different tact in that it is an optimization of syntax
that doesn't effect the runtime performance very much. Check it out if
you've haven't already.

.. _jQuery.proxy: http://api.jquery.com/jQuery.proxy/
.. _Coffee Script: http://jashkenas.github.com/coffee-script/
.. _Backbone.js: http://documentcloud.github.com/backbone/


.. author:: default
.. categories:: code
.. tags:: javascript, programming
.. comments::
