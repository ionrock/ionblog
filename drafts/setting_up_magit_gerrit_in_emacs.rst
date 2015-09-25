Setting up magit-gerrit in Emacs
================================

I recently started working on `OpenStack <http://openstack.org>`_ and,
being an avid Emacs user, I hoped to find a more integrated workflow
with my editor of choice. Of the options out there, I settled on
`magit-gerrit <https://github.com/terranpro/magit-gerrit>`_.

OpenStack uses `git <http://git-scm.org>`_ for source control and
`gerrit <https://code.google.com/p/gerrit/>`_ for code review. The way
code gets merged into OpenStack is through code review and gerrit. In
a nutshell, you create a branch, write some code, submit a code review
and after that code is reviewed and approved, it is merged
upstream. The key is ensuring the code review process is thorough and
convenient.

As developers with specific environments, it is crucial to be able to
quickly download a patch and play around with the code. For example,
running the tests locally or playing around with a new endpoint is
important when approving a review. Fortunately, magit-gerrit makes
this process really easy.

First off, you need to install the `git-review` tool. This is
available via `pip <http://pip-installer.org>`_.

.. code-block:: bash

   $ pip install git-review

Next up, you can check out a repo. We'll use the `Designate
<https://github.com/openstack/designate>`_ repo because that is what
I'm working on!

.. code-block:: bash

   $ git clone https://github.com/openstack/designate.git
   $ cd designate

With a repo in place, we can start setting up magit-gerrit. Assuming
you've setup `Melpa <http://melpa.org/>`_, you can install it via `M-x
package-install RET magit-gerrit`. Add to your emacs init file:

.. code-block:: lisp

   (require 'magit-gerrit)


The `magit-gerrit` docs suggest setting two variables.

.. code-block:: lisp

   ;; if remote url is not using the default gerrit port and
   ;; ssh scheme, need to manually set this variable
   (setq-default magit-gerrit-ssh-creds "myid@gerrithost.org")

   ;; if necessary, use an alternative remote instead of 'origin'
   (setq-default magit-gerrit-remote "gerrit")

The `magit-gerrit` package can infer the `magit-gerrit-ssh-creds` from
the `magit-gerrit-remote`. This makes it easy to configure your repo
via a `.dir-locals.el` file.

.. code-block:: lisp

   ((magit-mode
     (magit-gerrit-remote . "ssh://eric@review.openstack.org:29418/openstack/designate")))

Once you have your repo configured, you open your repo in magit via
`M-x magit-status`. You should also see a message saying "Detected
magit-gerrit-ssh-creds" that shows the credentials used to login into
the gerrit server. These are simple ssh credentials, so if you can't
ssh into the gerrit server using the credentials, then you need to
adjust your settings accordingly.

If everything is configured correctly, there should be an entry in the
status page that lists any reviews for the project. The listing shows
the summary of the review. You can navigate to the review and press
`T` to get a list of options. From there, you can download the
patchset as a branch or simply view the diff. You can also browse to
the review in gerrit. From what I can tell, you can't comment on a
review, but you can give a +/- for a review.

I've just started using gerrit and magit-gerrit, so I'm sure there are
some features that I don't fully understand. For example, I've yet to
understand how to re-run git review in order to update a patch after
getting feedback. Assuming that isn't supported, I'm sure it shouldn't
be too hard to add.

Feel free to ping me if you try it and have questions or tips!


.. author:: default
.. categories:: code
.. tags:: openstack, python, gerrit, code review, git, emacs
.. comments::
