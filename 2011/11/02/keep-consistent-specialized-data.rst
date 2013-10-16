Keep Consistent Specialized Data
################################

First off, I have to mention that I'm still rather sick. This thing has
been going strong for 3 days now, which really rare. I don't believe I'm
getting fevers as consistently, but it doesn't change the fact I feel
really weak and thinking has been a challenge. Hopefully I'll start
feeling better today as I've made a decision to let up on the rest and
make sure I get more work done. Being sick sucks.
Speaking of work, we recently put in a good deal of work testing
specialized solution for analyzing data. The initial tests were
promising, but in the end I think there were some limitations in the
actual implementation tools that kept it from seriously flying. This has
me thinking about how you can make specialized processes for data in
order to get the speed you need while still keeping some element of
consistency across the different data sources.
The problem that comes up is that if you do work to get the data to
some specialized format in order to do some special processing, that has
a rather expensive cost. This expense is traditionally in the form of
extra time. One solution is to make sure you write in the specialized
format initially instead of pulling it from some other database. The
problem then is that original database which might have been good for
something then has to jump hoops to get it to a format it requires. This
leads the solution that you might write it twice. Disk is cheap
afterall, so when you save your data, write it to the database and also
write it to the specialized format. The potential problem here is that
the transaction to write the data is rather lengthy and failures might
be hard to handle. It really isn't an easy problem.
One solution is to rethink the flow of data. Instead of the data being
something that sits in a database until you query it, the data could
instead be part of a workflow of transformations. This doesn't mean that
you don't put your data in a database, but it does mean that you don't
always have to. If some portion of the workflow doesn't require updating
the data, a flat file might be a great way to handle the data. The goal
is that by providing a workflow with the data, you change the
expectations and expose the real qualities of the data at each step in
such a way that you can capitalize on them.
This idea is extremely vague because even though I've been thinking
about it for a while, an actual implementation hasn't come up that makes
obvious sense. Hopefully someone reading might have some ideas on how
this design could work and what tools would be helpful.


.. author:: default
.. categories:: code
.. tags:: design, mongodb, programming
.. comments::
