=================
 The Query Queue
=================

A really basic data structure is a queue. You put things in the queue at
one end and grab things off the queue at the other end of the line. In
terms of making highly scalable web applications, queues allow you to
set up work to be done by some other process in order to get the
response to the user faster.

I had an idea based on some slightly different use cases. The idea is
that instead of simply popping off the last item in the queue, you
instead query the queue to get the last item. The querying it allows you
to have different types of workers utilizing the queue without stepping
on each others toes. This can solve an issue of granularity. If you are
saving some set of data that gets collected in steps, there is a good
chance that step has meaning. In a survey for example, there is value in
the set of answers to all the questions, but there is also value in the
single questions as well. This is especially true if the entire survey
wasn't completed.

There might be other situations where it would be beneficial. When you
register for some service, they might need to verify an email address or
do other operations that cross communication lines (sending a sms
message). If you queue the progress in a query queue, each component
could query for the unsent emails or sms messages while the actual
registration process waits for finalized and confirmed registrations.
I obviously don't have all the details worked out. For example, what
happens when the queue gets full? What happens if not all queries are
fulfilled? Using our registration example, if the person never verifies
their account, it just sits in the queue. It should probably be expunged
from the queue some point. How should that happen?
This might be a horrible idea or it might be something someone else has
implemented or found a different solution to. Already I have considered
that you could just create more simple queues for each operation. That
would probably get around a good portion of the problems, but you
inherently lose the more natural continuation type pattern, which is the
benefit of this kind of system.

If you know of any similar systems or people who have tried this kind
of design please let me know. Part of me feels it would be worth trying
out, but at the same time I have a nagging feeling someone really smart
sees a much different and better pattern available that makes the whole
idea moot. That wouldn't bother me in the slightest because the problem
is getting solved.

Update:
I just read about `the end of Nsyght`_. This is exactly the sort of
problem that I think a query queue could support. The river of data
coming really quickly and multiple services reading off it as fast as
possible getting the information they need. Some look for images, others
links, others focus on indexing text, while others focus on the
relationships between the atomic units. Again, my idea for a query queue
could be totally off, but it is an idea.


.. _the end of Nsyght: http://blog.akash.im/kevin-smith-on-pursuing-ideas?c=1


.. author:: default
.. categories:: code
.. tags:: mongodb, programming, python
.. comments::
