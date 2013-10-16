============================================
 Getting Started with JVM Languages is Hard
============================================

I watched `this video`_ on integrating `Scala`_. Now, I'm not a Java
developer. I used it in college and had to mess with small bits of it
throughout the years, but generally, it is something I've avoided. Scala
is a language built on the JVM that is (as I naively understand) well
suited for concurrency thanks to it support of Actors and is relatively
friendly to the functional style of programming. It also is statically
typed, which is what initially got me interested in looking at it.

Seeing as I'm a web developer, my first search on a new language is
always a quick review of the web frameworks. Web frameworks usually do a
good job getting you up and running quickly, which is really beneficial
for a non-Java developer like myself. Unfortunately, this is also
usually where I end up losing steam in JVM based languages. The problem
is Java and the JVM make it difficult to get started.

Part of this evaluation is pretty unfair. I have no doubt Scala and
other JVM languages (Clojure is another I had a limited interest in) can
be really excellent. The problem is you have to understand the JVM. Am I
whining? Probably. Does it matter? Nope.

When learning a language friction is a killer. Understanding the
programming constructs and ideals of the languages is usually least of
your worries. It is when you have to find dependencies and simply get
started you have a problem. The Java classpath is a great example of
pure stopping power when learning a language. The concept makes sense.
You create a path for searching for libraries and necessary files. It is
just like the operating system's PATH only for code. Got it.

Unfortunately, it just doesn't work that way. There is almost always a
stack trace that reflects javac not being able to find some aspect of
the program to make things work. When I start hitting these kinds of
problems, my eyes glaze over, I start closing buffers in Emacs and start
doing something else. It is a pain in the neck and it doesn't make sense
why it is so hard.

This pain also goes for things like Maven, Ant and all the surrounding
Java ecosystem tools. Let's take a look at getting started with `Lift`_:

::

    mvn archetype:generate -U \
      -DarchetypeGroupId=net.liftweb \
      -DarchetypeArtifactId=lift-archetype-blank \
      -DarchetypeVersion=1.0 \
      -DremoteRepositories=http://scala-tools.org/repo-releases \
      -DgroupId=demo.helloworld \
      -DartifactId=helloworld \
      -Dversion=1.0-SNAPSHOT

Now to a Java developer this might not be a big deal. This might even
be elegant. To me, it is a huge blinking light that says I'll be doing a
ton of configuration, dealing with obtuse XML and generally wasting my
time on the unimportant details. If that is how much I have to write in
order to get a Hello World application running, then the serious
complexity of a real world application is going to be a nightmare. Even
if it is not, I've lost my will to find out. Game over.

The reason I mention it at all is that there seems to be tons of cool
stuff happening on the JVM. Scala is one language I'd like to try out.
`Clojure`_ is another I was really excited about getting my hands dirty
with. Even `Jython`_ seems like an interesting tool to have in one's
programming tool belt. Yet, even though the concept of an interesting
language on top of the production proven JVM is really promising, the
reality is the interface is a nightmare. That fact is too bad because it
means that most JVM based languages that don't make an effort to hide
the JVM-ism are somewhat limited in scope to Java friendly developers.
The one JVM based language that I've used without having much trouble
getting started was `Rhino`_. It was relatively trivial to get up and
running and I never even thought about the classpath. At a minimum, that
is what I'd hope to find from other JVM based languages, especially if
their features are based more around the language than integrating with
existing Java applications. For example, I understand that Scala is a
language that seems pride itself on how easily it integrates in a Java
application. My point is that it would be really helpful to be able to
use JVM based languages without having to know I'm using a JVM based
language.


.. _this video: http://www.infoq.com/presentations/Absorbing-Scala-in-the-Java-Ecosystem
.. _Scala: http://www.scala-lang.org/
.. _Lift: http://liftweb.net
.. _Clojure: http://clojure.org
.. _Jython: http://www.jython.org/
.. _Rhino: http://www.mozilla.org/rhino/


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
