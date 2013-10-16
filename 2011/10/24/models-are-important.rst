Models are Important
####################

Models are a critical part of any large system because they define what
can and cannot be expected. The NoSQL set of databases are praised
because they are "schemaless" but I believe that benefit is really a
hindrance. If you do not have a schema, then you can never truly know
whether or not some data exists. It is possible to fake this knowledge
for a time by just assuming some attribute will exist with a usable
value, but that practice quickly begins to fail when you have to make
any changes to these sorts of assumed values. The better thing to do is
define the schema using models.
By "model" I do mean the "M" in MVC. Most people associate them with
ORMs, which makes it especially easy to drop them when creating a system
that doesn't require mapping to a relational paradigm. The "model" is
the data and that is all you need. This is completely false. The data
can have "extra" information a model might not use, but the model still
provides the contract that others can depend on. In fact the model can
give the appearance of data existing, when in fact it is a calculated
value using a business defined algorithm. This is the power of a model.
Where this realization became especially important recently was in a
central concept in our code called a "context". The context provides a
singleton that, based on configuration, calls specific methods according
to the "context" defined in the configuration. This sounds pretty slick,
so lets see an example:

::


    config = {'env': 'devel'}



    from database.dev import save as devsave

    from database.prod import save as prodsave



    class Context(object):

        def __init__(self, conf):

            self.conf = conf



        def save(self, key, value):

            if self.conf['env'] == 'devel':

                devsave(key, value)

            else:

                prodsave(key, value)

This is a contrived example, but hopefully the point is clear. Instead
of always checking the config everywhere, you keep that test in your
"context" and provide a single function to call. This is a clever way to
get around constantly checking your configuration and polluting your
logic with redundant if statements.
By why are you doing this in the first place!!! Just pass the
configuration details to your models and let them deal with the
connection. If the configuration is pointing at a development database,
then you are good to go. You never need the if statement in the first
place.
Going the other way, if you need to get data out, you can just ask your
model to do it for you. The model will pull it from the database and
validate the contract is correct. You never will have to see code that
checks different values to understand the current state. For example:

::


    if doc.get('name') and not doc['name'].startswith('/implicit'):

        create_element(doc['element'])

    elif not doc['name'] and len(doc.get('children', [])) > 0:

        name = doc['children'][0].get('name', gen_name())

        create_element(doc['element'], name=name)

    else:

        create_element(doc['element'])

This kind of code is terrible to debug later because you never really
know what concept you're enforcing. Why does it matter that the name
starts with '/implicit'? Is that a URL or a path? What scenario would
there not be a 'name'? Is that a fix for an old bug that introduced bad
data? Why are you calling "gen\_name"? What does that really do? Models
can help with all these issues.
A model can encapsulate not only data but a business concept. The above
code can become as simple as:

::


    element = Element.create_from_doc(doc)

This works because the information for what is optional is defined in
the model. For example, the name attribute we tested above can be
generated immediately if it isn't present:

::


    class Element(Model):

        @property

        def name():

            if not self.name:

                self.name = gen_name()

            return self.name

The concept of "implicit" that was mentioned above can also be
encapsulated in a property or method. Not to mention, it can be tested
easily and in isolation instead of having to construct complex state in
order to traverse a particular code path.
I remember when I first learned about MVC and Rails and it seemed like
a handy way to organize code. You had fewer questions to answer such as
where to put files and which files were for working with the database
vs. filling in a page template. I was naive to the problems MVC was
truly addressing. The goal of a model is to encapsulate concepts in
order to minimize confusion. This happens by making sure your models
provide expectations via the contract within their API.


.. author:: default
.. categories:: code
.. tags:: design, mongodb, programming, python, testing, Uncategorized
.. comments::
