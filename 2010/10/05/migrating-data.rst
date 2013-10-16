Migrating Data
##############

At work we have something of a problem. We keep a ton of data, but most
of that data is read only. In the spirit of avoiding optimizations,
we've just kept all that data in one MongoDB process. This has been
working pretty well, but recently we realized we're hitting some
performance limits that happen because our use cases for the data is
different and the DB isn't really equipped to handle each use case
efficiently at the same time. The idea is to migrate the data out of
that database to a read only archive database.

This feels like a pretty simple problem, but since it deals with our
data, it is really important to get it right. A co-worker recommended
`Celery`_, which looks promising. I really want to make sure I have
accurate logs on this project. It should be really easy to monitor and
find interesting information from the constant stream of data.
Obviously, some might be asking why not just use more hardware and that
is a valid question. It is interesting because that was the initial
plan, but when we starting thinking about the amount of hardware and
space we'd need, it became rather clear that creating a MongoDB cluster
wouldn't be trivial or cheap. If we used EC2 it wouldn't be a big deal,
but, we also would have hit performance issues much sooner since the
issues stem from reading old data off the disk.

The other reason for the design change is that the data usage really is
different. The vast majority of the data is read-only. What happens then
is that a read would be expensive and lock the DB. This automatically
should raise red flags since MongoDB doesn't lock on reads. The problem
was actually that the query used enough resources to effectively lock
the DB. The connections and queries would pile up and then finally
stampede. This would interrupt our writing systems and generally just
cause a lot errors, not to mention a poor user experience.

If the migration tool seems helpful, I'll try to post it. It is
interesting in that it reveals the power in customization and how
generic solutions, while seemingly effective, usually end up falling
down over the long haul.

.. _Celery: http://celeryproject.org


.. author:: default
.. categories:: code
.. tags:: mongodb, python
.. comments::
