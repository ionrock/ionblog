=================
 Learning Golang
=================

Lately I've had the opportunity to spend some time with Go. I've been
interested in the language for a while now, but I've only done a
couple toy projects. The best way to get a feel for a language is to
write spend some consecutive time writing a real program that others
will be using. Having a real project makes it possible to get a really
good picture of what software development is like using a language.


First Impressions
=================

When I first started going beyond toy projects, the most difficult
aspect was the package (or module in Python terms) system. In Python,
you have an abstraction of modules that uses the filesystem, but
requires extra tooling to include other code. Other languages, like
Ruby (if I remember it correctly!) can use a more direct include type
of module system where you include the code you want. PHP is a great
example of this simple module pattern where you truly just include
other code as if it were written within your own. Go does something
different where a package is really a directory and the import
statement includes everything in that directory that has the same
package declaration. I'm sure there is more to it, but this crude
understanding has been enough to be dangerous.

One aspect that drew me to go was the simplified deployment. Go,
aseems to be focused on producing extremely flexible binaries that can
be used on a wide array of systems. The result is that a Go binary
that you built with linux typically can be copied to any other linux
without having any issues. While I'm the sure the same is possible
with C/C++ or any other compiled language, it has been an early
feature to produce all inclusive binaries that don't have a dependency
on anything on the target machine. As I'm coming from Python, I'm not
an expert in these sorts of things, so this is really just my
impression, validated by my limited experience.

Finally, Go is reasonably fast without being incredibly complex. I
don't have to manage memory, but I do get to play with
pointers. Concurrency is a core feature of the language that helps
implement the fun features of Python like generators. Go routines are
poised to do the things that I always wished Python did and that is to
take care of work no matter whether it is async I/O or CPU
bound. Lastly, it doesn't have a warm up period like you'd see in a
JVM language, which makes it suitable for small scripts.


But What About Python?
======================

I still enjoy Python, but the enjoyment comes from feeling fluent in
the language more than enjoying any set of features. The thing I like
most about programming in Python is that I feel very comfortable
banging out code and knowing that it is reasonably well written with
tests and can function well within the larger Python ecosystem. This
fluency in Python is not something I'm willing to drop due to some
hype in another language. There are some frustrating aspects of
programming in Python that make me want to try something new.

The first is the packaging landscape. I don't mean to suggest that pip
is terrible or wheels are a huge mistake. Instead, it is the more
general pattern of shipping source code to an environment in order to
run the code. There are *TONS* of great tools to make this
manageable and containers only make it even easier, so again, I'm not
condemning the future of Python deployments. But I am tired of it.

In Python, I need to make a ton of decisions (some that have been
chosen for me) such as whether or not to use the system packages or a
virtualenv. I have to consider how to test a release before releasing
it. I have to establish how I can be sure that what I tested is the
same as what I'm releasing. All these questions can become subtlely
complex over time and it gets tiring.

The second aspect of Python that is frustrating is the
performance. Generally, it is fast enough, except when it isn't. It is
when things need to be faster that Python becomes painful. If you are
CPU bound then get ready to scale out those processes! If I/O is where
you are lacking there are a plethora of async I/O libraries to help
efficiently accessing I/O. But, dealing with both CPU and I/O bound
issues is complicated, especially when you are using libraries that
may not be compatible with the async I/O framework you are using. It
is definitely possible to write fast Python code, but there is a lot
of work to do, none of which makes deployment easier, hence it is a
little tiring.

When all else fails you can write a C module, use Cython or try
another interpreter. Again, all interesting ideas, but the cost shows
up in complexity and in the deployment.

There is no easy fix to these problems and it isn't as fun as it used
to be to think about solving it.


So Why Go Then?
===============

The question then is why Go is a contender to unseat my most fluent
language Python? The simple answer is that I'm tired of the
complexity. The nice thing about Go is that takes care of some
essential aspects I don't care to delve into, specifically, memory
management and concurrency. Go is also fast enough that I should not
have to be terribly concerned about adopting new programming paradigms
in order to work around some critical bottleneck. While I'm confident
that I could make Python work for almost anything, at some point it feels
like it has become a hammer and I'd like to start doing other things
than hitting nails.

Now, even though I'm learning Go and have been excited about the
possibilities, it doesn't change the fact most of my day to day work
is in Python. Maybe that will change at some point, but for the
foreseeable future, I don't see it changing anytime soon, which is
totally fine by me.

I'm sure there are issues with Go that I haven't run into yet. Static
typing has been challenging to use after having massive freedom in
Python. What is appealing is that less than perfect Go code has been
good enough in quality for production uses. That is exciting because
it means while I learn more about the langauge and community, it
doesn't preclude me from being productive and learning new things.


.. author:: default
.. categories:: code
.. tags:: golang, python
.. comments::
