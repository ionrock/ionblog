Announcing MgoQuery
###################

If you remember not long ago I wrote a post about `caution writing
DSLs`_. Despite my own advice and reluctance towards DSLs, I wrote one
for creating MongoDB queries.

The big question should be why. After all, MongoDB just uses simple
dictionaries for queries. What could be easier than that? Surprisingly,
a lot.

Where MongoDB queries get complicated is when you are combining AND and
OR operations along side range operations that may use non-standard
types such as dates or timestamps. It is for this reason I wrote
`MgoQuery`_ (which stands for Mongo Query if that wasn't obvious).

Here is a really simple example:

::

    from pprint import pprint
    from mgoquery import Parser, Query


    p = Parser()
    result = p.parse('"x:1,y:2"|"x:3,y:4"')
    pprint(Query(result).as_dict())

    # print something like
    # 
    # {'$or': [{'$and': [{'x': '1'}, {'y': '2'}]},
    #          {'$and': [{'x': '3'}, {'y': '4'}]}]}

As you can see, we get a pretty concise language for expressing a rather
complex query. You can also pass in a conversion function that will help
to convert the values to their proper type in the query.

Feel free to take a look at my first stab at this. I'm using
`PyParsing`_ to create the gammar and parser. Not having a ton of
experience with it, my initial impressions are very good. Please feel
free to send along comments or recommendations.

.. _caution writing DSLs: http://ionrock.org/blog/2012/08/07/Be_Careful_Designing_DSLs
.. _MgoQuery: http://bitbucket.org/elarson/mgoquery
.. _PyParsing: http://pyparsing.wikispaces.com/


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
