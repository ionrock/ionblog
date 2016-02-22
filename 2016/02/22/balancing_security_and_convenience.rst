Balancing Security and Convenience
==================================

There is always a question of whether to use a hosted service or
manage a service yourself. It is a tough question because the answer
changes over time depending on your business needs. A startup might be
totally fine using github and slack, but the size of google means
rolling your own solution. The arguments regarding hosted services
revolve around security, and more specifically, the sensitive data you
make available by using these services.

There are many that would argue that owning a service is more
secure. While it is true that you *may* send fewer bits to a third
party, it really says nothing of security. A hosted service such as
`github <https://github.com>`_ or `slack <https://slack.com>`_ is
already targeted by hackers. While I'm sure there are vulnerabilities,
popular hosted services have been vetted by huge amounts of usage. It
is in the providers interest to provide a secure and reliable service,
constantly improving infrastructure and security over time. Running a
service at scale shakes loose quite a few bugs that contain difficult
to find attack vectors.

Even if a service is reasonably secure, there is still a risk of
trusting your data to another company. Unless you have clients that
specifically disallow this, I'd argue that this is not worth the
cost. Successful hosted services generally have a community of
supporters that have done the work of integrating with the
platform. That makes hooking up your bug tracker with your build
system, chat and monitoring is trivial. Sorting out all the bits to
make this work in an internal environment means writing, debugging and
maintaining code along side operating each dependent system. That is
far from impossible, but it is certainly expensive when you need
developers and operators working on more pressing issues. The irony
here is that by avoiding the hosted service, you've essentially made
local development more difficult and reduced the ability of your
development pipeline to improve the code.

To put this in financial terms, lets say you have a team of 5 people
and lets say the average salary is $100k, or $48 / hour. If each
person spends 10 hours a week on the CI/CD system and operating tools
like chat, it would cost $480 / week, or ~$25k per year. That doesn't
seem too bad, but that doesn't include the extra cost of an effective
build system catching bugs and the initial development time to get
these systems up and running and talking to each other. You might need
to get hardware within the network, setup firewalls, configure secure
routes via VPNs to allow remote developers to use the system. At this
point you might have included the time of another 15 people and spent
at least 3+ months of your team's time getting the initial system up
and running, noting, that it is all code you'll need to maintain. Also
note, that this says nothing about problems that come up.

The fact is, it is really expensive to design, build and operate a
suite of services simply to avoid having some bits on another person's
computer. It seems better to focus on making your team more productive
by providing helpful tools they don't have to manage and prepare
mitigation plans for how to recover from a security breach or service
failure. Obviously, there are dangers, but mitigating them is less
work than rebuilding a service along with its integrations from
scratch.

I'm curious what others have experienced when choosing an external
service over a DIY solution. Did you feel the DIY solution was full
featured? Did you get burned choosing a hosted solution? Let me know!


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
