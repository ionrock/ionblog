Automate Everything
===================

I've found that it has become increasingly difficult to simply hack
something together without formally automating the process. Something
inside me just can't handle the idea of repeating steps that could be
automated. My solution has been to become faster at the process of
formal automation. Most of the steps are small, easy to do and don't
take much time. Rather than feeling guilty that I'm wasting time by
writing small a library or script, I work to make the process faster
and am able to re-use these scripts and snippets in the future.

A nice side effect is that writing code has become much more fluid. I
get more practice using essential libraries and tools where over time
they've become second nature. It also can be helpful getting in the
flow because taking the extra steps of writing to files and setting up
a small package feels like a warm up of sorts.

One thing that has been difficult is navigating the wealth of
options. For example, I've gone back to OS X for development. I've had
to use VMs for running processes and tests. I've been playing with
Vagrant and Docker. These can be configured with chef, ansible, or
puppet in addition to writing a `Vagrantfile` or `Dockerfile`. Does chef set
up a docker container? Do you call `chef-apply` in your `Dockerfile`?
On OS X you have to use `boot2docker <http://boot2docker.io>`_, which
seems to be a wrapper around `docker machine
<https://github.com/docker/machine>`_. Even though I **know** the
process can be configured to be completely automated, it is tough to
feel as though you're doing it right.

Obviously, there is a balance. It can be easy to become caught in a
quagmire of automation, especially when you're trying to automate
something that was never intended to be driven programaticaly. At some
point, even though it hurts, I have to just bear down and type the
commands or click the mouse over and over again.

That is until I break down and start writing soem elisp to do it for
me ;)


.. author:: default
.. categories:: code
.. tags:: python, make, docker, vagrant chef, automation
.. comments::
