Testing and Design
##################

A well designed system does not always imply it is easy to test. Adding
a flexible, modular design can make testing difficult. The complexity
that hides behind a good design still exists, which means we need to be
sure the interfaces between the different layers of the design are fully
tested.

Conceptually, testing interfaces seems relatively simple, but as layers
build upon other layers, things can become more difficult. Typically a
layer of design will interact with libraries which may in turn have
similar layers. A change at one layer may have a larger impact than
expected.

Fortunately there are strategies to help manage the complexity when
managing complexity! Mocks can be a good options as long as you also
test the real interface using the same parameters. There are other tools
such as code injection, but it is something I'm personally familiar
with.

If you do have to test a complex, well designed system it may not be
easy to test, but it should still be testable. The difference lies in
the fact that testable software can be tested effectively. Even though
the process of testing a system might be difficult at times, it should
be clear that it is possible. If the code doesn't seems impossible to
test effectively (brittle tests, tons of stubs/framework for small
corner cases, extremely slow tests), then it is probably a sign of a
poor design. This is unfortunate as code that is difficult to test is
also code that is difficult to confidently refactor.


.. author:: default
.. categories:: code
.. tags:: programming, testing
.. comments::
