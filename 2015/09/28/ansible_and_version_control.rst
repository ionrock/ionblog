Ansible and Version Control
===========================

I've become reasonbly comfortable with both `Chef <https://chef.io>`_
and `Ansible <http://www.ansible.com>`_. Both have pros and cons, but
there is one aspect of Ansible that I think deserves mention is how
it can work with version control thanks to its lack of a central
server and through defining its operations via YAML.


No Central Server
-----------------

In Chef, there is the chef server that keeps the actual scripts for
different roles, recipes, etc. It also maintains the list of nodes /
clients and environments available. The good thing about this design
is that you have a single source of truth for all aspects of the
process. The downside, is that the central server must be updated
outside of version control. This presents the situation where version
`1.1` of some recipe introduces some bug and you may need to cut a
`1.2` that is the same as `1.0` in order to fix it.

Another downside is that if a node goes down or doesn't get cleaned up
properly, it will still exist on the chef server. Other recipes may
still think the node is up even though it has become unavailable.

Ansible, at its core, runs commands via SSH. The management of nodes
happens in the inventory and is dependent on file listing or a dynamic
module. The result is that everything Ansible needs to work is the
local machine. While it is not automatic, using a `dynamic inventory
<http://docs.ansible.com/ansible/guide_rax.html>`_, Ansible can
examine the infrastructure at run time and act accordingly.

If you are not using a dynamic inventory, you can add hosts in your
invetory files and just commit them like any other change! From here
you can see when nodes come up and go down in your change history.


YAML Roles
----------

Ansible defines its actions via playbooks defined as YAML. You can
also add your own modules if need be in the same repo. What's more, if
you find a helpful role or library in `Ansible Galaxy
<https://galaxy.ansible.com/>`_, installing the library downloads its
file directly into your code tree, ready to be committed. This
vendoring makes things like version pins unnecessary. Instead, you
simply checkout the changeset or version tag and everything should be
good to go.

To compare this with Chef, you can maintain roles, environments,
etc. as JSON and sync them with the central Chef server using
Kitchen. The problem with this tactic is that a new commit in version
control may or may not be an update to the resource on the chef
server. You can get around this limitation with things like commit
hooks that automatically sync the repo with the chef server, but that
is not always feasible. For example, if you mistakenly update a role
with an incorrect version pin and your servers are updating on a
cadence, then that change will get rolled out automatically.

Again, there are known ways around these sorts of issues, but the
point being is that it is harder to maintain everything via version
control, which I'd argue is beneficial.

I'm a firm believer that keeping your config management code in
version control is the best way to manange your systems. There are
ways to make central server based systems effectively gated via
version control, but it is not always obvious, and it is certainly
not built in. Ansible, by running code from the local machine and
repository code, makes it simple to keep the repository as the single
source of truth.


.. author:: default
.. categories:: code
.. tags:: python, devops, git, ansible, chef
.. comments::
