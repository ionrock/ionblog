===================================
 Adding &quot;like&quot; to Dingus
===================================

In making serious efforts to become a better tester I've tried to get
better acquainted with testing tools. Mocking specifically is one
technique that seems extremely helpful, especially when you have an
application built upon many other systems that you'd want to test
without having a huge test setup stage. The library I settled on was
`Dingus`_ thanks to `Gary's`_ `screencasts`_ and seeing first how how
flexible it is in terms its ability to almost magically replace
everything except that which is tested.

At the moment the Dingus docs are rather sparse, but the basic idea is
you use a Dingus object and then assert different things happened to the
object. This primarily done by using a method called "calls". Here is an
example:

::

    from dingus import Dingus

    d = Dingus()
    d.foo('bar')

    assert d.calls('foo', ('bar'))

Pretty easy so far.

Dingus can also be used to replace all the objects in a test using a
DingusTestCase. So, for example, you can do something like this:

::

    class TestSomeModel(DingusTestCase(MyModel)):

        def test_getting_a_thing(self):
            m = MyModel()
            m.get('foo')

            assert m.db.calls('query', (), {'name': 'foo'})

This makes sure the "db" object in the MyModel class calls its "query"
function with the query argument "name" equal to "foo". Again this is
pretty simple and is really helpful because you verify that you are
using an API correctly without having to spin up some external service.
This all works really well when you're looking at mocking something one
level deep, but often times it would be beneficial to go a little
deeper. In my specific situation, I'm using a MongoDB connection, so I
want to verify that specific things happened when I created the object
and when I query something. To do this, I have to go a bit deeper with
the calls. Here is an example:

::

    from dragoman.testing import DingusTestCase
    from dragoman import storage

    class TestLanguageList(DingusTestCase(storage.LanguageList)):

        def test_get(self):
            result = storage.LanguageList.get('foo')
            db = storage.get_db.calls('()').one().return_value
            collection = db.calls('__getitem__', ('config.languages')).one().return_value
            assert collection.calls('find_one', ({'abbrev': 'foo'}))

My project is a `gettext-like service`_ and the test is for testing
getting a language. You can see in the above code I have to go into the
calls list and pull out the return value of the "get\_db" function and
continue to traverse the graph of calls to make sure the query was
correct.

What I'd like to do is to describe what it should have looked like.

Something like this:

::

    def test_get(self):
        result = storage.LanguageList.get('foo')
        expected = Dingus()
        expected()['config.languages'].find({'abbrev': 'foo'}).count()
        assert expected.like(storage.get_db)

Instead of manually traversing I can just utilize a Dingus and compare
it with the one that was called previously. This is really helpful for
defining protocols of sorts. Often times applications have a set of
business rules that go along with certain actions and it can be
difficult to test that sort of thing. The idea here is that those sort
of protocols can be defined clearly in the tests and there is a simple
way to test them.

Here is another example. Say you have a User object that when saved
needs to create or update a datastore. Here is what the test might look
like:

::

    class TestUser(DingusTestCase(User)):
       def test_create(self):
           u = User('eric')
           mock_db = Dingus()
           mock_db.find('user')
           mock_db.create('user_%s' % eric)
           mock_db.commit({'username': 'eric', 'type': 'user'})
           assert mock_db.like(u.db)

Based on the tests we verify that the create method will be using a
"user\_" prefix in its create method. If we assume the database is a
document store like CouchDB, then we can glean from the tests that there
is a "username" field that is needed for documents of that type.

Likewise, it is clear that the protocol for adding a user involves
checking if the user there, creating the user then committing the
transaction.

Here is the implementation along with a few tests:

::

    from dingus import Dingus

    class LikeDingus(dingus.Dingus):
        def _flatten_calls(self, d):
            calls = d.calls()
            def flattener(cl):
                calls = []
                for call in cl:
                    if call.return_value:
                        calls.append((call.name,
                                      call.args,
                                      call.kwargs,
                                      flattener(call.return_value.calls())))
                    else:
                        calls.append((call.name, call.args, call.kwarg))
                return calls
            return flattener(calls)
                                    
        
        def like(self, other_dingus):
            return self._flatten_calls(self) == self._flatten_calls(other_dingus)

    ## tests

    class TestDingusLikeStmt(object):

        def test_singular(self):
            tested = LikeDingus()
            tested('foo')['bar'].find({'name': 'baz'})

            expected = Dingus()
            expected('foo')['bar'].find({'name': 'baz'})

            assert tested.like(expected)

        def test_multiple(self):
            tested = LikeDingus()
            tested('foo')
            tested('bar')

            expected = Dingus()
            expected('foo')
            expected('bar')
            assert tested.like(expected)

        def test_the_order(self):
            tested = LikeDingus()
            tested('foo')
            tested('bar')

            expected = Dingus()
            expected('bar')
            expected('foo')
            
            assert not tested.like(expected)

Seeing as I'm still learning to be a more effective tester, I can't say
whether these kinds of assertions are extremely helpful or not. I do
think that defining the expected assertions in terms of some other
Dingus seems helpful in that you get to keep on mental model. Also I
think the definition feels more natural than focusing entirely on the
calls method of a Dingus.

What do you think?

.. _Dingus: http://bitbucket.org/garyberhardt/dingus
.. _Gary's: http://blog.extracheese.org
.. _screencasts: http://vimeo.com/garybernhardt
.. _gettext-like service: http://bitbucket.org/elarson/dragoman


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
