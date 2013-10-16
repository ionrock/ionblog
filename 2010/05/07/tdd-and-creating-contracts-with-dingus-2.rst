========================================
 TDD and Creating Contracts with Dingus
========================================

In my quest to become a better tester and generally write better code,
I've started looking at TDD. One of the things about TDD is that has
always stumped me is you manage to make sure that some piece of code
with work when it is not isolated. Seeing as Dingus has played a
critical role with my interest in testing, the concept of isolation has
felt important before I even understood what it really meant.

One ideal in TDD (and this is an assumption based on what little I've
read) is that tests should be really fast. This is simply a user
interface kind of feature that makes testing more usable. If you know
you can run 500+ tests in less than a second, then you are more likely
to run those tests. In fact, I'd say it is critical to TDD that test run
quickly. It is no fun to write a test first that takes a few seconds to
run before writing any working code. You can trust me on this one as
I've experienced it first hand.

With that in mind, how do you speed up the tests? From my perspective,
it is critical to remove I/O. Specifically, you need to remove real
connections to real sources of data. That means any RESTful web service,
file system reads/writes and databases. You can do this with Dingus and
I'd say it really what Dingus excels at. The problem you generally feel
is that you will write the wrong interface or API when mocking these
services. This is where a contract comes into play.

Lets say we have a small session library. We're talking a really simple
key/value kind of store using MongoDB for storing session information in
a web application. Here is the object:

::

    class Session(object):
        def __init__(self, conn):
            self.conn = conn

I'm leaving out any methods because we're TDD'ing here!
So, the basic thing we want to do is test that sessions can be saved.
What does that mean? Well it means that we take some dictionary and
store it in MongoDB in a way we can get it back. I'm not going to go
into details about things like IDs or how to make sure your session keys
are unique. The point here is to show how to provide a contract for
saving and retrieving the data.

So here are two tests:

::

    class TestSession(object):
        def test_saving_session(self):
            mock_conn = Dingus()
            sess = Session(mock_conn)
            sess.save(ID, {'foo': 'bar', 'ts': now()})
            expected_data = {
                'sess_id': ID, 
                'data': {'foo': 'bar', 'ts': now()}
            }
            assert mock_conn.calls('insert', expected_data)
            assert mock_conn.calls('find_one', {'sess_id': ID})

        def test_loading_session(self):
            mock_conn = Dingus()
            sess = Session(mock_conn)
            sess.load(ID)
            assert mock_conn.calls('find_one', {'sess_id': ID})

So, what you see is that we are testing that when the session object
tries to save a session it will do some series of operations using the
fake MongoDB connection.

Here is another way you could test it with a live MongoDB connection.

::

    def test_saving_session(self):
        test_conn = get_test_conn()
        sess = Session(test_conn)
        sess.save(ID, {'foo': 'bar'})
        loaded = sess.load(ID)
        assert loaded['foo'] == 'bar'

This seems pretty rock solid. One problem though is that your test
needs to run a MongoDB instance. That is a pain, although nothing major.
More importantly though, what happens when the MongoDB API changes or
you need to change how you do inserts. MongoDB, for example, supports
things called upserts where if the object doesn't exist, it will create
it, or else it updates the objects that it finds. That might be a better
way to go about it, but the live connection doesn't reveal that subtlety
which is actually a really important distinction.

When I first started looking at this, the idea of mapping out the API
calls on the Dingus object seemed fragile and daunting. But, as I
started to think about it, the idea of mocking a service is to create
that contract. Contracts in this situation are between an external
library and your code, but they can very well go deeper. In the above
example, I might have a SessionStore abstraction that works like a file
like object. In that case, I'd want to verify that doing something like
"session.save()" ends up doing an open, write and close call. Likewise,
if that still ended up using MongoDB on the back end, I'd then test the
SessionStore for calls similar to the above. In doing so, I'm making
contracts all the way down.

Likewise, it is important to understand that we are using TDD. When
there is a bug, we write a test first. In our session example, if we
needed to test whether a session is expired then, we can effectively add
that to the contract of calls on the mock connection object to verify
that we check for a expire date. We run the fast tests, see things are
broken, and go about fixing it. Writing the code first wouldn't enforce
the same outcome because we haven't established that a certain set of
operations describe what it means to be "saved". Instead, by recording
the operations performed, we've created that description. Likewise it
provides metrics for complexity. If you have a single test that has tons
of assertions, it might be time to try and refactor.

The key here really is practicing the process. At work it is clear that
the project I'm working is ready for a rather large restructuring. I've
started that restructuring through tests and it seems to be a rather
reasonable way to go about it. It seems obvious that with practice the
process will only become easier as well as more effective.



.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
