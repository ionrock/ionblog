Mercurial Workflows
###################

I have an idea for a workflow using mercurial where you have a simple
tool hide things like merging and dealing with multiple heads. I felt
pretty good about it until I talked to my manager about it and he
mentioned the difficulties of communicating status based on the state of
the source repo. Even though I disagree, it is clear that one must be
careful not to lose the communicative nature of source control.

My idea for a workflow is based on `this video`_. It is a good idea to
go ahead and watch it first before moving on.

The biggest thing to draw from this is the idea that it is not the
facilities of your VCS that makes development work with complicated code
trees, but rather the etiquette prescribed for the team. If you have a
vision for the flow of code, it is best to create that system and use
tools instead of allowing the tool to decide your version control
strategy. There reason is because your etiquette is a protocol with
interop between each developer. In other words, it is a UI that you have
to live with for a potentially long time.

With that in mind, my specific workflow does cater to ease of use over
expertise. My goal is that you avoid running into trouble using this
system. Where does trouble come from? In a word, merges. By merges I
mean taking one code line and merging it into another. This distinction
is important because it differs greatly depending on your tools. The
point is though, most all VC systems contain the idea of a branch and
merging is taking those branches, no matter what they contain, and
merging them into another. The difference in my workflow is that you
avoid taking branches and merging them in favor of working with
changesets. Abstract thoughts aside, here is my proposal.

You have a "project". This the traditional repo for your code.

Somewhere there is a canonical version of that code that you do releases
from. In my system you have a canonical remote repo and you have a
canonical local repo. We'll call these the remote and local mainlines.

The idea is that the remote mainline must always be at a reasonable
level of stability. I'm defining "reasonable" here as a developer should
be able to clone it and "run" the package successfully on the main
branches.

The reasonable level of stability is important because it prescribes a
condition such that you shouldn't be pushing code for others that hasn't
reached a certain level of stability. That doesn't mean you will never
break the build, but it means you understand it is a serious problem
when you do. In order to keep this possible problem to a minimum, we
utilize a local mainline to stage your pushes.

Traditionally when you have a bug or feature you need to work on you
will branch. That will create a copy of your local mainline in a
directory called "branches". You then point your environment at that
branch and start working on fixing the bug. The next day you "sync" the
branch you are working on. A "sync" is a process that pulls in the
stable changes found in the public repo and immediately adds them to
your "unstable" feature branch. You are then forced to handle any issues
at that time. Likewise, the "sync" process rebases your branch to the
new stable mainline. In this way your changes are always going to be
easy to apply to mainline.

When you finish your feature or bug fix, the next step is to get the
changes into mainline. The first step is to apply those changes to the
local mainline. This intermediate step is important because it gives you
a change to have staged other code that might not be public yet. For
example, if you have a bug that requires changes to other parts of the
code, you could work on each and them as they are ready to the local
mainline. When you are all done and everything seems to be working
correctly, you can then push your changes to the remote mainline.

Doing this with mercurial, the process looks something like this.

::

    % cd $project
    % hg clone . branches/foo
    % cd branches/foo
    % python setup.py develop # point the virtualenv at the branch package

    # work on the code
    # ok we're don

    % cd ../../ # back to the project dir
    % hg pull branches/foo
    % run-tests
    % hg push ssh://mainline/repo/$project

The essential bit is that you "pull" into the mainline branch. Assuming
that the branch and the mainline are in "sync", that makes sure the
branch changesets end up on the top of the mainline stack of changesets.

The result is that you appear to have a sequence of changesets that can
be viewed atomically. You also have not "merged" anything. It is as if
you perfectly applied all your changes with the result being a very
simple stack of changes ending up on the source tree.

This simple list is advantageous because it removes the complexity of
dealing with parents and ancestors. If something has causes a
regression, the solution can be to simply pop off changesets until the
regression is gone. There is also little confusion if a merge
potentially pulled changes that were undesirable.

Going back to my original paragraph where my manager mentioned that by
not having the branch in the remote code repo you lose track of what the
developers are doing. I do see the benefit. If you want to collaborate
on something, you just switch to the branch that work is happening on.

If you don't want the changes, then don't pull or push them to your
working branch.

The problem is when you have to follow that tree of changes. This
happens when you have a break in production and you have to ask yourself
what the correct baseline is to move back to. This is when trying to
understand the parallel lines in your graphical log becomes hopeless.

Once you do get a picture of what happened, how do you back it out?

Where is the best place to apply the changes? How they propagate between
all those parallel branches? I'm not saying that my workflow is totally
correct, but I believe when it counts the most, simplicity will make
life easier.

An answer to the collaboration question is also very possible. Most
developers have a desire to pull at the beginning of the day and push at
the end. It is trivial then that you'd always push to a personal repo or
branch. Here is an example of a potential filesystem for a suite of
projects.

::

    /sourc
    ├── main
    │   ├── project1
    │   ├── project2
    │   └── project3
    └── users
        ├── eric
        │   ├── project2
        │   └── project2-feature-branch
        └── mike
            └── project1
    [googlevideo=http://video.google.com/videoplay?docid=-577744660535947210#]

If you want to see what people are working on, then using the idea of
the "local mainline" mentioned above, you could keep that copied on the
server. The point being is that the etiquette defined by the protocol is
the most important function of the version control workflow because it
is that protocol that guarantees the release process is exactly the same
and that developers can be confident in their actions using the version
control system.

This workflow does make the assumption that it is trivial to point the
environment at different branches. If that is difficult then I'd argue
that there is something wrong. If you want to make sure deployments are
simple and the same across N servers, you need to be sure you can create
that environment from scratch at the push of a button. Therefore this
workflow makes that assumption on the source code.

Lastly, I'm sure different tools would make the workflow different. My
understanding is that git gets branching right such that some of the
problems that this workflow solves might not be issues. In my mind it
doesn't matter what tool you are using. All that matters is that when
you get a source tree you can easily see the obvious path the code took
getting from point a to point b. The analogy is like publishing. You
keep drafts private, sometimes you share them with select people and
collaborate for different sections, but at some point you publish it and
at that point you can't simply change things. If you ask me, the same
technique and process applies to source control.

.. _this video: http://video.google.com/videoplay?docid=-577744660535947210#


.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
