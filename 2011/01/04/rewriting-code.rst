Rewriting Code
##############

We have a large project that is going to be going through a pretty large
change. There will be a new incarnation of the project that hopefully
sets the bar for the future. Seeing as that is a pretty big lofty goal
and the real world is rarely big and lofty, it seemed like a good idea
to write down some specific reasons we need to make rather major
changes.

I'm not going to deny the reason for this explanation is to help me
feel better about effectively rewriting our application. After all,
`rewriting software is a really bad idea`_. I heartily agree that a big
rewrite is rarely going to solve problems. But, in this case, the goal
is to improve the system. How is that different? When you write software
you have bugs and bugs have assumptions. Take persistence for example.

You might be getting errors every so often that happen because the
database layer is a bottleneck. Fixing the bug might be to include some
caching or simply throwing hardware at the issue. The system on the
other hand could include a completely different design of the data such
that writes can be made incrementally and later compiled into a complete
object. The difference here is that you've starting changing the
assumptions and in doing so opened up a different set of opportunity
that could be the difference between constant frustration and actually
getting new features.

Our code base, while very successful, has begun to show these sorts of
systemic issues that will prevent us from expanding far beyond where we
are currently. I say "far" beyond because that is real goal. We want to
handle 1000x the load with 1/10th the hardware and that can't happen
given the current system assumptions. Likewise, if we continue to focus
on fixing our bugs, we'll never be able to radically change the system.

The biggest systemic issue that we have is speed. We need to be faster.

Our response times need to be much lower and our ability to develop
exciting features needs to be faster as well. The current assumption is
that there is one data store. The single data store implies that you
write to one "place" and read from the same "place". The problem is that
as we've grown, the realization has come that we don't read/write to the
same place. There can be an intermediary. Along similar lines we don't
read everything in the same fashion, yet the vast majority of data is in
fact read only. Our persistence goals then are to make sure our updates
are fast and don't impact our read performance. There will be a trade
off that much of our data will be slightly more stale than before.

Another speed issue deals with development speed. There are infinite
possibilities for asking questions, but it is not simple to create
another way of asking questions very quickly. This problem become more
complex as we enter different platforms (mobile). Here the solution is
not as sweeping but simply involves producing some API to our storage
that any client can utilize. While this seems simple (GET the question
foo, POST the answer bar) in reality there is huge set of assumptions
the system makes throughout that have never been truly codified. By
codified I mean they have not been defined in a publishable manner in
addition to lacking consistency through out the code. This improvement
will mean providing a true API that we publish along with tools to make
things easier to work with. From there, our hope is that we can have a
platform for more customized questions that help us move beyond check
boxes and into rich interfaces.

Finally, we need to make our authors faster. I've mentioned before that
we have a custom language we use for writing questionnaires. These
"scripters" as we call them are in fact a mix of programmer, designer,
statistician and project manager all rolled into one. As such there is a
wide variety of skill levels that need to be supported. In this case our
goal will be to extend our scripting environment to better support our
more basic users while giving the advanced users tools that can improve
everyone's workflow.

The reality is that while we are effectively rewriting our application
there is a clear direction that we want to go. Our first iterations have
been naive as to the problems at scale. Now we have an opportunity to
take some systemic bottlenecks and hopefully improve things for the
foreseeable future. We're pretty confident that we'll see a whole new
set of problems but hopefully by that time we will have gained enough
understanding that we can make another shift to keep growing.

.. _rewriting software is a really bad idea: http://www.joelonsoftware.com/articles/fog0000000069.html


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
