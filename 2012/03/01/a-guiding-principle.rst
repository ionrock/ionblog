A Guiding Principle
###################

There was a discussion on `the Emacs Reddit`_ regarding an `inspiring
video`_ that was very relevant to editing code. The purpose of the video
though was to reflect on a larger idea. The presenter in the video makes
the point that you should be creating things out of principle.

His personal principle is things should never get in the way of an idea.
His example is an editor where small tools help to visualize instantly
the effect of changing the code. If you haven't already, go check out
the video. Besides the editor example being really slick, it really hits
home how he acts according to his guiding principle.

This got me thinking about my own guiding principle. I had never thought
about it before in these terms, but the exercise of finding ones guiding
principle is helpful to contextualize why you do the things you do. What
I came up with was:

"Always be obvious."

Seeing as this is my first attempt at naming this principle I reserve
the right to change the actual wording. The meaning shouldn't change.

When the speaker discussed how he felt it morally wrong to get in the
way of ideas, I knew exactly what he was talking about. I feel the same
way when time is wasted figuring out how to perform a simple task.

Seeing as the speaker provided an example, I'll do the same and see if
that helps.

In Unix, the shell provides the entry point to the operating system. It
provides some slick tools like files and streams to make things happen.
Once you learn the basics, new concepts and usages become available
because the constructs are obvious. The questions you ask about how to
take the output of some process and read it into another doesn't require
thought because you know immediately you can do the operation via a file
handle.

The simplicity of Unix and its constructs have been used to create
incredibly complex, yet maintainable systems. The reason for this is
that the constructs are simple and become obvious when working on larger
problems.

Taking a specific example of a simple task such as reading a log, we can
see why the Unix way is obvious and makes the entire process much
simpler. If you task is to read a log, then your first question is how
to get the content of the log into your applications code. If you chose
the route of logging to some database server then you have to answer
questions about connecting to the database, login credentials, network
partitioning and many other small issues that can get in the way. Your
log reading script then ends up dealing with traversing some network and
dealing with database connections.

If we took the obvious route and just read the log file, we could simply
program our log reader to accept stdin and read directly from the log
file. It is all very simple and direct. If this is the methodology
across an entire organization, then the question of how to read a log
file becomes obvious, log into the box where the process is running and
read its log from its log file. Do you want to collect logs from the
same app across many servers then simply loop over the hosts and get
each processes log file. It might not be ideal, but it is obvious and
you spend the majority of your time working on getting the information
you need rather than dealing with network issues, credentials, or
database cursor/threading problems.

This is my guiding principle. Always be obvious. Finding clever
solutions is great in that it helps to try new things that could
eventually become obvious. But in order to easily find new solutions it
is exceptionally helpful to have an obvious base to work from. Unix
provided this and I believe the fruits of those decisions are abundant.

So, always be obvious!

.. _the Emacs Reddit: http://www.reddit.com/r/emacs/comments/qbtou/inventing_on_principle_great_talk_my_question_is/
.. _inspiring video: http://vimeo.com/36579366


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
