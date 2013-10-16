=======================================================
 A Cultural Observation: Git, Mercurial and Publishing
=======================================================


*Warning! I'm not an expert git user! My goal is to describe the
philosophical difference between mercurial and git as I've seen
them.*

Recently I've had the opportunity to spend some time in git. It is a
really interesting to get some first hand experience and see exactly
why people feel as though there is such a strong difference between
git and mercurial. After enjoying my time with git and going back to
mercurial, I realized that the differences, while exist, are primarily
cultural.

The essence of what differentiates the two cultures is what it means
to publish code.

DVCS defines a concept of a "push" in order to take local changes and
add them to a repo. It is reasonable to assume that pushing is
analogous to publishing, but on a cultural level it is not entirely
correct. Publishing code in a DVCS is the point at which code goes
from "development" to "mainline".

When code is in "development", it is considered outside the scope of
the source tree. It may still be in version control, but it has not be
included in the official history of the code base. When code is
"mainline" it has become part of the public lineage of the
source. Development is where you write drafts that end up being
published in mainline for consumption.

To clarify, "mainline" does not mean "master" or "default" as it does
in git and mercurial respectively. A source repo could include a wide
variety of "mainline" branches that are used to take code from
unstable changes to stable releases. In this case "mainline" means the
set of branches that are considered part of the public workflow. Once
code hits "mainline" it cannot be changed.

Mercurial culturally has taken the approach that code goes from
development to mainline by way of merging. You create a branch of some
sort (bookmark, queue, branch, anonymous head, etc.), do work and when
it is done you merge it into some mainline branch. You may push your
branch to the public repo, but if it hasn't been merged into one of
the mainline branches, then even though the branch exists publically,
it hasn't been truly published. Culturally, it is considered OK to
make your unfinished work public. It is series of merges in the
mainline branches that we strive to make sense and keep clean.

Git culturally takes the perspective that code goes from development
to mainline when it is pushed to a public repo. The reasoning is
simple. Once you push the code, you can't very well adjust the history
as it could be conflicted with others. Users of git consider it good
practice to shape and edit the history before pushing it. Locally a
repo can be as "messy" as you want, as long as the code you push has a
well written history.

These two cultures are not entirely based on technical differences,
especially today. Mercurial historically has been less forgiving of
rewriting history at a technical level. Mercurial tries to keep track
of where code is coming from (ie what branch). If you merge a branch
and push the code, the branch that was merge will be pushed as well
because the merge changeset has a link back to the original
branch. Git on the other hand is more than happy to consider things
only terms of patches. My understanding is there is still the same
sort of linkage, but editing those links is supported as a first class
function in git (via tools like rebase and the reflog). Currently,
both tools offer a very similar toolset assuming one perspective on
how code goes from development to mainline is understood.

The important thing to take from these two different perspectives on
how code gets published is that you should pick a model and create a
workflow around that model. Where things get difficult and frustrating
is when the publishing process is undefined. A mercurial repo can take
a published when pushed model and a git repo can use a publish on
merge technique. If you mix models, then things become more
frustrating because you can't rely on the consistency provided by
adhering to a clear publishing model.

To be clear here are a few example where mixing models can cause
problems. Imagine a CI system that built things based on every commit
pushed to a remote repo. Pushes of "development" branches don't fit in
that model and could break the CI build. Similarly, in a merge based
model, tools that expect branches to align with features for a release
would become incomplete.

No matter what model you subscribe to, it is critical to communicate
what it means to publish code. Whether it is an organization or open
source project, the process of taking code from development to
mainline should be a defined standard that is communicated to everyone
working on the code. It will make life easier for everyone involved
and remove much of the frustration when working with git and/or
mercurial.


.. author:: default
.. categories:: code
.. tags:: programming, mercurial
.. comments::
