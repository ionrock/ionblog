=========================
 Balancing Microservices
=========================

Microservices are often touted as a critical design pattern, but
really it is just a tactic for managing certain vectors of complexity
by decoupling the code from operations. For example, if you have a
large suite of APIs, each driven by a different microservice, you can
iterate and release different APIs as needed, reducing the complexity
of releasing a single monolithic API service. In this use case, the
microservices allow more concurrent work between teams by decoupling
the code and the release process.

Another use case for microservices would be to decouple resource
contention. Lets assume you have a database that is used by a few
different apps. You could remove this decoupling by using separate
services that manage their own data plane, removing contention between
the services that exists by using the same database.

From a design standpoint, it is non-trivial. The first example of a
huge API suite can be implemented primarily through load balancing
rules without much issue. The database example is more difficult
because there will need to be a middleman ensuring data is replicated
properly. Just like normalization of databases, the normalization that
occurs in microservices can be costly as it requires more work
(expense) when those services need consistency.

Another expense is designing and maintaining APIs between the
services. Refactoring becomes more complicated because you have to
consider there is old code still handling messages in addition to the
new code. Before, the interactions were isolated to the code, but when
using microservices the APIs will need some level of backwards
compatibility.

The one assumption with microservices that make them operationally
feasible is automation. Artifacts should be built and tested reliably
from your CI pipeline. Deployments need to be driven by a
configuration management system (ie chef, ansible, etc.). Monitoring
needs to be in place and communicated to everyone doing releases. The
reason all this automation is so critical is because without it, you
can't possibly keep track of everything. Imagine having 10 services
each scaled out to 10 "nodes" and you begin to see why it is difficult
to manage this sort of system without a lot of automation.

Even though it is expensive, it might be worth it. Incidents are one
area where microservices can be valuable. Microservices provide a
smaller space to search for root causes. Rather than having to examine
a large breadth of over a single codebase, you can (hopefully) review
a single service in semi-isolation and determine the problem. Assuming
your microservices are designed properly and even though the number of
services is large, the hope is that the problem areas will be limited
to small services and can be more easily debugged and fixed.

Microservices require a balance. Using microservices is a tactic, not
a design. Lot of small processes doesn't make anything easier, but
lots of small processes that divide operational concerns and decouple
systems can be really helpful. Like anything else, it is best to
measure and understand the reasoning for breaking up code into
microservices.

.. author:: default
.. categories:: code
.. tags:: microservices, devops
.. comments::
