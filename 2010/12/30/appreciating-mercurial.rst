========================
 Appreciating Mercurial
========================

There is a lot of buzz around `git`_. Since I've never spent much time
with it, I can't really say whether it is warranted or not. I ended up
using `mercurial`_ and never had a reason to change.

One thing that consistently happens when using a DVCS is that you
reconsider how you work with version control. There are some larger
concepts that are largely static such as tagging releases and branching
for features or bug fixes, but past that the world is wide open. This is
a blessing and a curse. The options are never ending, so like vim or
emacs, you can always tinker with your version control. The downside is
that it can be really difficult to find a canonical method of use.

Some people might wonder why you'd want a "canonical" way to use your
version control system. After all, a DVCS lets you program on planes so
your work flow doesn't effect anyone else, right? In theory this is
true, but in practice I'd argue that isn't the case. The reality is a
DVCS is a complicated beast and in most dev environments you really
don't need the extra complications. A successful colleague of mine
expressed his appreciation for Perforce, a known target for version
control bigotry. His point was not necessarily that Perforce was such a
perfect design but rather the constraints of it were reasonable and
helped get things done efficiently. It had a very clear canonical way of
working with it that made everything from getting new employees up to
speed just as simple as pushing out new releases. Unfortunately, the git
vs. hg debates usually come from radically different environments where
this idea of a canonical use doesn't easily apply and the result is that
there seems to be a farther discrepancy between the two than there
really needs to be.

I read `this article`_ regarding how git gets branching more correct
than mercurial. Looking at the context, the author's work flow requires
accepting and reviewing patches before applying it to the project code
base. His perspective is that losing the context of where a patch came
from in terms of the branch doesn't really matter compared to the
ability to disassociate patches with branches. I might have
misunderstood his point but it doesn't really matter. The use case of
pushing forward development via the submission of patches is a very
specific use case that doesn't happen in many situations.

Most open source programmers have day jobs and I've yet to see the
situation where fixing bugs in an organization goes through some
maintainer that reviews the patches and applies them to the main branch.
It is more common that developers work on specific bugs and features
within the context of some time period. At the end of the time period,
there is a release event that tags the current stable state of the repo
and the cycle continues. One option would be to create a release manager
position that is responsible for integrating patches to make sure they
work and don't cause problems, but the smarter way to deal with this is
via automation and continuous integration.

Hopefully it is clear that the biggest difference between this
traditional organization based model and open source experiences is that
in an organization your are responsible for the code. In an open source
situation you can submit patches all day long and there is no obligation
for anyone to pay attention. The open source developer has to politic
one way or another in order to be heard where as in an organization,
your obligation is to communicate and produce code. This distinction is
critical because in addition to using a tool, an organization can
specify the "right" way to use it such that it reduces issues associated
with random features colliding. This is important because by specifying
the correct way to use the tool you open the door for other assumptions
to be made.

A really good example of this would be in a release process. If you as
a group decided to always add a "closed #{bug}" format in commit
messages, writing a script that compiles the release notes and posts
them to a wiki would be pretty trivial. In a similar fashion, you could
add flags to your commit messages that hooks in the VCS use to do things
like post back to a ticket/bug page. This is something a developer at
our company recently started working on. It would be impossible to
things like this in an open source model.

I'm not trying to argue that one system is better or worse than the
other. My goal is to simply make it clear that you can't simply read
blogs about git or hg and assume that you're finding a consensus on what
is the best tool. It is not the tool, but how you use it that really
matters most. Personally, I'd stick with mercurial because, as many git
fans have mentioned, the UI is easier to use. My perspective is that you
can work around the vast majority of subtle issues by simply specifying
the best way to use the tool.

As a side note, in this `branching model`_ post, one thing that might
help in mercurial to avoid many branches in default is to only push to
default or the production branch. If I have two features I'm working
with their own named branches and I finish one, I can choose to merge
that branch into default and push only the default branch changes. That
way you can experiment and create branches as needed without polluting
the canonical repo. Does mercurial do anything to help this work flow?
Nope, it is just something you have to tell the team to do. Some smart
folks say that `constraints can be good`_ and this is simply an example
of that concept.


.. _git: http://git-scm.com
.. _mercurial: http://mercurial.selenic.com
.. _this article: http://lucumr.pocoo.org/2010/8/17/git-and-mercurial-branching/
.. _branching model: http://nvie.com/posts/a-successful-git-branching-model/
.. _constraints can be good: http://37signals.com/svn/archives2/constraints_breed_breakthrough_creativity.php


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
