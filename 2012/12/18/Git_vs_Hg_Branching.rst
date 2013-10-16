===================
 Git vs. Mercurial
===================


I'm going to start by saying that I'm not arguing git/hg is
better. They are both great and do an excellent job. I'd also like to
point out that I've never really used git, therefore my descriptions
are based on what I've `read of git`_ and git user's `arguments against
mercurial branches`_. In any case, it is not meant to be negative to
either side and simply is here to potentially put a name on a face.

A large point of contention between the primary DVCSs is the concept
of branching. The primary difference has actually nothing to do with
either system's branching feature. Instead it has everything to do how
it stores the underlying tree of changes, merges, tags, etc.

Mercurial acts like a pack rat. When you commit, mercurial wants to
keep track of everything.

Git just cares about the patch. Everything else is just metadata.

Mercurial's model means that you always know *everything* about a
changeset. If something changes, it needs a new changeset.

Git's model means that if you want to say that branch never existed,
then just remove that metadata. It disappears.

The big difference is in the cultural impact this has.

Git has always been friendly to "commit everything and let rebase sort
it out" crowd. The workflow is to commit code (commit might be the
wrong word here...) and create the perfect patch to push. Over time,
the mentality is that your repository is not simply a collection of
changes. It is the culmination of perfectly pruned patched.

While mercurial works best with a plan, hg isn't nearly as inept as it
might seem though. While you are less likely to see the perfectly
pruned repo (ie no merges), with a bit of organization, you can have a
repo with obvious scopes of development. A well organized hg repo will
let you see a feature start its life as a branch, potentially have
some child branches for experiments, and finally find the right
solution. When the branch is merged back to default you can see the
entire perfectly pruned changeset while still being able to go back
and see how it came to be.

The git folks think this is ugly. Why create a persistent branch when
you really just need that single patch in the grand scheme of things?
Keeping your history means you can analyze it and understand it. The
big list of perfectly pruned changesets you see in a well managed git
repo is really nice when you look at 10, 20, maybe 50 changes. When
you are looking at 1k, 20k, maybe 30k changes, that single list is not
nearly as helpful. In those times it would be really nice to go back
to the original branch and see what happened. If you use named
branches in mercurial with a good naming convention
(feature/$ticket-$title works for me), that history can actually be
useful in the long run.

I should be clear that there is no reason you can't have the same
model in git that you would have in mercurial. At least that is my
impression. I'm positive there are things in git that are possible you
can't do in mercurial. I also understand the draw of a "clean" set of
changes. Personally, I think I value the pack rat mentality of
mercurial, but I plan on giving git a formal try sooner than
later. After all, the `mercurial mode`_ I use in emacs is based on a
`git mode`_!

.. _read of git: http://jhw.dreamwidth.org/1868.html
.. _arguments against mercurial branches: https://felipec.wordpress.com/2012/05/26/no-mercurial-branches-are-still-not-better-than-git-ones-response-to-jhws-more-on-mercurial-vs-git-with-graphs/

.. _mercurial mode: https://github.com/ananthakumaran/monky
.. _git mode: http://philjackson.github.com/magit/


.. author:: default
.. categories:: code
.. tags:: programming, mercurial
.. comments::
