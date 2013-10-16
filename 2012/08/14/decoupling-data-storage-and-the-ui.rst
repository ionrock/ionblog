Decoupling Data Storage and The UI
##################################

One thing that has always frustrated me about MongoDB is that it is very
difficult to assert your data has been written. Eventual consistency is
a tricky thing. You can't always be positive the next read you make
includes all the data. How do you get around this limitation?

One technique is to use a smart client. Rather than store everything in
the database and rely completely on it as your primary source of data,
your client loads the state and maintains its own state internally. This
does not work when the client needs to consider a rich hierarchy of
records, but for things like a user session's settings, it is pretty
reasonable.

For example, say you have a list of records you are displaying in your
browser. Your initial request loads the records and displays them all.
When you change the name of some record, the user interface is updated
directly from the submitted data, while it is persisted to the database
in the background. If the person managed to open another browser and
reach the same UI, the record might not yet be updated, but that is the
tradeoff you make for eventual consistency.

This technique works relatively well as long as the client is able to
take the state and directly apply it to the user interface. If the new
data impacts a wide variety of data or requires information that must be
coordinated / evaluated centrally, the result is the client becomes much
more complicated. For example, imagine if you TurboTax had to do all the
calculations for the tax code in the browser. It ceases to be a valid
tactic.

Just because you need to visit the server for some evaluation of your
data, it doesn't mean you need to store the data in your database prior
to evaluating the data. Most data driven applications use some concept
of a model in order to translate the data from the data store format to
your application format. There is no reason your application cannot
submit data that gets translated to the same model format and is
evaluated for a result.

I'll use an example from my job to explain how to implement this kind of
design.

As I mentioned numerous times, we do opinion polling. This involves
writing questionnaires in a specialized DSL. The DSL supports things
like logic blocks and flow control so authors can ask different
questions and process data based on the answers. The flow control and
logic are too complex to consider implementing them in the browser. It
would mean introducing client issues into a core element of our
processing, which is an unnecessary addition of complexity. The problem
is that we need to consider this complex logic when finding the next
question (or questions) we want to ask.

Currently we require that for each submitted answer, we have to write it
to the database before returning our next question to the UI. This
requirement is because the user might contact another node in the
cluster. Therefore, we need to be sure when there is a node change, the
new node pulls it state from our database.

What I propose then is that we decouple the data submission from the
evaluation for the next page. When a question is answered we submit our
data to a data queue that will process it and store it in the database.
Rather than waiting on an answer, we send our newly updated state and
current location in the interview to an evaluation service that will
take the state and find the next question we need to ask.

It is possible that the user could try to change clients and switch
nodes between the time the data is actually written. The worst case
scenario in this situation is they might be asked the same question
twice. It is reasonable to require that the data be written and made
available within a few seconds, which would virtually eliminate this
scenario from happening.

One thing I haven't touched on is whether or not the data is validated
before writing or when looking for the next question. I would presume
the former is a better tact as the validation should be relatively quick
and we reduce the chance of bad data being written. I should also
mention that in our scenario, our data, once written is effectively
static. This means that when requesting the data on a node change, there
is a minimum requirement that it be available in a format suitable for
interviewing. This might not be the same format we use for analysis. The
analyzed format could require more time to process, but that time need
not be considered for maintaining state during interviews.

Has anyone tried this methodology before? Any pitfalls or obvious
problems I'm missing?


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
