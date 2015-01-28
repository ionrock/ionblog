DevOps
======

I finally realized why DevOps is an idea. Up until this point, I felt
DevOps was a term for a developer that was also responsible for the
infrastructure. In other words, I never associated DevOps with an
actual strategy or idea, and instead, it was simply something that
happened. Well no more!

DevOps is providing developers keys [#f1]_ to operations. In a small
organization these keys never have a chance to leave the hands of the
small team of developers that have nothing to concern themselves
except getting things done. As an organization grows, there becomes a
dedicated person (and soon after group of people) dedicated to
maintaining the infrastructure. The thing that happens is that the
keys developers had to log into any server or install a new database
are taken away and given to operations to manage. DevOps is a trend
where operations and developers share the keys.

Because developers and operations both have access to change the
infrastructure, there is a meeting of the minds that has to
happen. Developers and Ops are forced to communicate the what, where,
when, why and how of changes to the infrastructure. Since folks in
DevOps are familiar with code, version control becomes a place of
communication and cohesion.

The reason I now understand this paradigm more clearly is because when
a developer doesn't have access to the infrastructure, it is a huge
waste of time. When code doesn't work we need to be able to debug
it. It important to come up with theories why things don't work and
iteratively test the theories until we find the reason for the
failure. While it is possible to debug bugs that only show up in
production, it can be slow, frustrating and difficult, when access to
the infrastructure isn't available.

I say all this with a huge grain of salt. I'm not a sysadmin and I've
never been a true sysadmin. While I understand the hand wavy idea that
if all developers have ssh keys to the hosts in a datacenter, there
are more vectors for attack. What I don't understand is why a
developer with ssh keys is any more dangerous than a sysadmin
having ssh keys. Obviously, a sysadmin may have a more stringent
outlook on what is acceptable, but at the same time, anyone can be
duped. After all, if you trust your developers to write code that
writes to your database millions (or billions!) of times a day, I'm
sure you can trust them to keep an ssh key safe or avoid exposing
services that are meant to remain private.

I'm now a full on fan of DevOps. Developers and Ops working together
and applying software engineering techniques to everything they work
with seems like a great idea. Providing Developers keys to the
infrastructure and pushing Ops to communicate the important security
and/or hardware concerns is only a good thing. The more cohesion
between Ops and Dev, the better.


.. [#f1] I'm not talking about ssh keys, but rather the idea of having
	 "keys to the castle". One facet of this could be making sure
	 developer keys and accounts are available on the servers, but
	 that is not the only way to give devs access to the
	 infrastructure.

.. author:: default
.. categories:: code
.. tags:: devops, sysadmin, cloud
.. comments::
