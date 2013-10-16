Blogging to the Bear
####################

I've been working on debugging an issue on and off for a few weeks and
at this point, I'm stumped. I'm hoping writing about it might help
dislodge whatever it is in my brain that is preventing me from new
hypotheses.

The symptom is the database data getting out of whack. We keep a
document in MongoDB that gets updated after each request. Our system has
answers that are required, but for some reason, these answers are not
being answered. There are two reasons I can think of.

The first is the user submits an answer and in the process of responding
to the request, things get confused and we skip the questions we were
supposed to ask. The second is that we ask the question but we don't
record the answer.

Essentially my theory just wraps our entire request/response process.
The problem either happens when the data comes in or when it goes out.
Not very specific.

What has been done so far is that we confirmed when we do save the data,
we do so atomically. It is not a transaction where an error would be
rolled back, but we can be relatively confident that there is not a race
condition trying to write to the database.

Thinking about it more now, here is my theory. The problem is in the
page we send out. There could be a thread safety issue with that would
allow our "next page" algorithm to be incorrect. Our state is kept in a
cursor object that I suspect might have some thread safety issues.

I don't know that I've really come up with anything new here, but in
writing this I do think I've helped to clarify my theory. The big
question is how to reproduce the issue since it doesn't seem to happen
very often, which suggests there is a synchronization issue at play.


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
