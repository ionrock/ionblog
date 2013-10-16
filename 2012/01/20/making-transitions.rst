Making Transitions
##################

I can't tell you how many times a transition has made a song work. A
riff or chorus, no matter how interesting or catchy, is only as good as
the transition that introduces it. This theme also holds true when
developing systems. APIs and tools such as databases are only as good as
the data formats used in the transitions. A well designed architecture
with a poorly designed data or storage format will quickly gain
complexity, losing the benefits of the system design.

At work I've been taking an existing internal API and transitioning it
to a service based API. The process has proven to reveal a wide arrayf
of complexity. In my efforts to manage this complexity, the best tactic
has been to focus on the data format passing between the two systems.
Defining expectations and the contract using the format, it has enabled
simplifying the service as well as making the client code manageable.

While I'm still very much in the process of making the changes, the
strategy of adjusting the data going between the systems has made other
decisions much simpler. The result is that both the service and the
client application can be implemented with elegance and simplicity.


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
