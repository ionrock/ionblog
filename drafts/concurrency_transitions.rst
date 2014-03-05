Concurrency Transitions
=======================

`Glyph <https://glyph.twistedmatrix.com/>`_, the creator of `Twisted
<https://twistedmatrix.com>`_ wrote an interesting `article
<https://glyph.twistedmatrix.com/2014/02/unyielding.html>`_ discussing
the intrinsic flaws of using threads. The essential idea is that
unless you know explicitly when you are switching contexts, it is
extremely difficult to effectively reason about concurrency in code.

I agree that this is *one* way to handle concurrency. Glyph also
provides a clear perspective into the underlying constraints of
concurrent programming. The biggest constraint is that you need a way
to guarantee a set of statements happens atomically. He suggests an
event driven paradigm as how best to do this. In a typical async
system, the work is built up using small procedures that run
atomically, yielding back control to the main loop as they finish. The
reason the async model works so well is because you eliminate all CPU
based concurrency and allow work to happen while waiting for I/O.

There are other valid ways to achieve as similar effect. The key in
all these methods, async included, is to know when you transition from
atomic sequential operations to potentially concurrent, and often
parallel, operations.

A great example of this mindset is found in functional programming,
and specifically, in monads. A monad is essentially a guarantee that
some set of operations will happen atomically. In a functional
language, functions are considered "pure" meaning they don't introduce
any "side effects", or more specifically, they do not change any
state. Monads allow functional languages a way to interact with the
outside world by providing a logical interface that the underlying
system can use to do any necessary work to make the operation
safe. Clojure, for example, uses a Software Transactional Memory
system to safely apply changes to state. Another approach might be to
use locking and mutexes. No matter the methodology, the goal is to
provide a safe way to change state by allowing the developer an
explicit way to identify portions of code that change external state.

Here is a `classic example
<http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument>`_
in Python of where mutable state can cause problems.

In Python, and the vast majority of languages, it is assumed that a
function can act on a variable of a larger scope. This is possible
thanks to mutable data structures. In the example above, calling the
function multiple time doesn't re-initialize argument to an empty
list. It is a mutable data structure that exists as state. When the
function is called that state changes and that change of state is
considered a "side effect" in functional programming. This sort of
issue is even more difficult in threaded programming because your
state can cross threads in addition to lexical boundaries.

If we generalize the purpose of monads and Clojure's reference types,
we can establish that concurrent systems need to be able to manage the
transitions between pure functionality (no state manipulation) and
operations that effect state.

One methodology that I have found to be effective managing this
transition is to use queues. More generally, this might be called
message passing, but I don't believe message passing guarantees the
system understands when state changes. In the case of a queue, you
have an obvious entrance and exit point for the transition between
purity and side effects to take place.

The way to implement this sort of system is to consider each consumer
of a queue as a different process. By considering consumers /
producers as processes we ensure there is a clear boundary between
them that protects shared memory, and more generally shared state. The
queue then acts as bridge to cross the "physical" border. The queue
also provides the control over the transition between pure
functionality and side effects.

To relate this back to Glyph's async perspective, when state is pushed
onto the queue it is similar to yielding to the reactor in an async
system. When state is popped off the queue into a process, it can be
acted upon without worry of causing side effects that could effect
other operations.

Glyph brought up the scenario where a function might yield multiple
times in order to pass back control to the managing reactor. This
becomes less necessary in the queue and process system I describe
because there is no chance of a context switch interrupting an
operation or slowing down the reactor. In a typical async framework,
the job of the reactor is to order each bit of work. The work still
happens in series. Therefore, if one operation takes a long time, it
stops all other work from happening, assuming that work is not doing
I/O. The queue and process system doesn't have this same limitation as
it is able to yield control to the queue at the correct logical point
in the algorithm. Also, in terms of Python, the GIL is mitigated by
using processes. The result is that you can program in a sequential
manner for your algorithms, while still tackle problems concurrently.

Like anything, this queue and process model is not a panacea. If your
data is large, you often need to pass around references to the data
and where it can be retrieved. If that resource is not something that
tries to handle concurrent connections, the file system for example,
you still may run into concurrency issue accessing some resource. It
also can be difficult to reason about failures in a queue based
system. How full is too full? You can limit the queue size, but that
might cause blocking issues that may be unreasonable.

There is no silver bullet, but if you understand the significance of
transitions between pure functionality and side effects, you have a
good chance of producing a reasonable system no matter what
concurrency model you use.



.. author:: default
.. categories:: code
.. tags:: python, twisted, async, queues, multiprocessing, concurrency
.. comments::
