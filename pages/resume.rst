=============
 Eric Larson
=============

:Address: 8510 Loralinda Dr, Austin, TX 78753
:Phone: \(512\) 535-1825
:Email: eric@ionrock.org


Open Source Projects
====================

 - `CacheControl <http://github.com/ionrock/cachecontrol/>`_ - I'm the primary author of CacheControl. It is *the* recommended cache implementation for requests and is included in `pip <http://pip-installer.org>`_, the standard Python packaging tool. CacheControl is a HTTP caching algorithm library for `requests <http://docs.python-requests.org/en/latest/>`_. CacheControl builds off of the excellent caching algorithms in httplib2 to allow for robust, distributed and threadsafe cache implementations.

 - `Withenv <https://github.com/ionrock/withenv>`_ - A tool to manage environment variables on a per command basis using YAML files. Withenv is an essential tool in our DevOps workflow for driving operations.

 - `Xe <https://github.com/ionrock/xe>`_ - The `xe` command setups an executable environment on a per-command basis, providing consistent commands, even when using different tooling in an environment. Xe allows automating things like builds and tests for CI/CD while allowing autonomy in development.

 - `Rdo <https://github.com/ionrock/rdo>`_ - Rdo allows running commands transparently on a remote machine, or more commonly, a `Vagrant <https://www.vagrantup.com/>`_ VM in order to capitalize on local tooling that processes stdout such as traceback parsing.

 - `Buildenv <https://github.com/ionrock/buildenv>`_ - We use `Jenkins <https://jenkins.io/index.html>`_ for CI/CD along with the `build flow <https://wiki.jenkins-ci.org/display/JENKINS/Build+Flow+Plugin>`_ plugin. Buildenv replicates aspects of the buildflow plugin in order to run complex deployment flows locally for testing.

 - `Bach <https://github.com/ionrock/bach>`_ - Bach is a set of small utilities written in Go to help legacy apps utilize 12 Factor techniques. Bach provides a more featureful Withenv command that my team has been using for driving deployments.

 - `Openstack Designate <http://docs.openstack.org/developer/designate/>`_ - Designate is the DNSaaS offering for Openstack. In the 2016 Openstack User Survey, Designate ranked 2nd in user interest.



Work Experience
===============


Rackspace 2015 - Present
------------------------

I work on the Cloud DNS team, contributing to the Openstack DNSaaS
project `Designate
<http://docs.openstack.org/developer/designate/>`_. My role includes
upstream development, maintaining and iterating on the operational
code base, mentoring junior developers on the team and providing
software to improve the lower level data plane as needed.

 - Led the developer side of the DevOps operational code base that
   proved to be a best practice and was implemented by many other
   teams within Rackspace. This included the use of Withenv for
   managing environment data and driving operations, the use of
   Makefiles for a standard entry point into projects, documentation
   best practices to provide for pull-request based communication
   within a team and utilizing Docker for consistent builds within
   development and continuous integration.

 - Designed and co-authored a new worker model in Designate. The
   architectural shift provided for consistent performance at scale
   and eliminated the final issues blocking our next milestone. The
   worker model also reduced the operational complexity, removing two
   distinct processes and provided for a critical component to be
   rewritten in Go, increasing performance by 4x.


 - Promoted to Core Reviewer for Designate and invited into the
   OpenStack Leadership Team within Rackspace. This included
   presenting at the OpenStack Summit in Tokyo and Austin, as well as
   attending mid-cycle meetups overseas.

 - Wrote Rebindr, a tool to propagate zones between two instances of
   the Bind DNS server. Rebindr improves propagation time of creates
   by 10x. It also allows the rate limit for zone creation to go from
   a global limit of ~10 zones per minute to ~200.

 - Designed and merged a hookpoint API in upstream Designate. This
   provides a mechanism to apply changes necessary to integrate with
   existing infrastructure without requiring a separate fork of the
   code.

 - Created Panama, an API to enforce consistency between the legacy
   DNS control plane and Designate. Panama verifies whether a zone
   exists in either system and is able to adjust the business logic
   throughout the process of migration, giving preference to the
   relevant system over time. Panama was critical to ensuring data
   consistency across our entire DNS infrastructure.


YouGov 2008 - 2016
------------------

YouGov is a market research company providing custom statistical
analysis, survey and panel services, as well as turnkey research
products. I worked on the questionnaire and surveying system and a
data warehouse and data analytics system.

 - Introduced an effective caching mechanism for a central RESTful
   service router responsible for providing a uniform interface to
   backend services and databases. This caching layer is the essential
   means of optimization for almost all production systems.

 - Implemented a RESTful data warehouse called Pangaea using Amazon S3
   for storage and Django for the API. This system supports easy
   integration with Big Data analytics tools such as Amazon Redshift,
   Elastic Map Reduce, Apache Hive (via a hosted Hadoop service) and
   internal analysis using Python and R. This warehouse has allowed
   the business to create a new suite of competitive, automated, high
   margin analytics products.

 - Created a declarative ETL / Data processing framework for reliably
   extracting data from existing services into our data warehouse and
   transforming existing data before pushing it to external
   services. These ETLs have uploaded over 1 million documents
   totaling over 1.5 terabytes of data.

 - Designed a system for ETL processes to run remotely on existing
   servers consistently without requiring ownership of the server
   OS. This allowed our data warehouse project to reduce its computing
   and space requirements by utilizing existing hosts in our
   cluster. This minimized the initial financial and technical
   investment before proving its value to the company.

 - Wrote a threadsafe parser for an internal Domain Specific Language
   used for scripting surveys. The parser produced a JSON document
   that allowed analytics on questionnaires, but most importantly,
   allowed us to deprecate countless custom parsers that had been
   written for other projects and for ad-hoc analysis.

 - Created Dragoman, gettext as a RESTful service that supports the
   global organizations i18n requirements across all sites and
   services. Dragoman decoupled code releases from translation
   updates, allowing the global organization to quickly update
   translations as needed at any time.


WebWorks 2006 - 2007
--------------------

WebWorks provides document transformation products for technical
writers. Complex technical documents can be written in word processors
such as Word or Adobe FrameMaker and exported to different
targets. The flagship product was a design and build tool called
ePublisher written in C# and utilized XSLT based pipelines for
processing documents and creating output.

 - Created a lazily evaluated object wrapper for FrameMaker documents
   in Python that utilized the low level FrameMaker C API in order to
   easily traverse documents. This library was used in both IronPython
   and CPython for custom projects as well as within ePublisher, the
   company's flagship product.

 - Implemented an extensible build tool using IronPython that emulated
   build system features from Rails and Python (Paste, WSGI) in order
   to make development with the ePublisher suite of applications
   easier. Using this build tool, we were able to quickly create
   minimal templates and projects that allowed us to dogfood our build
   platform and experiment with new ideas that eventually became part
   of the product.

 - Maintained and extended ePublisher's C# codebase, build pipelines
   (XSLT) and output targets. The flagship output target was a
   customized documentation system written in HTML and JavaScript.


Novell 2005 - 2006
------------------

I worked as an intern with the Product Design Team for Novell whose
function was to design and test user interfaces associated with the
GNOME desktop. Specifically, this included creating demo applications,
writing specifications and mock-ups that would be used in improving
user interfaces for the Novell Linux Desktop and its associated
applications. This included notable projects such as the Banshee Music
Player, F-Spot Photo Manager, iFolder, and desktop search integration.

 - Implemented BetterDesktop.org, an open source website dedicated to
   improving Linux desktop usability through usability testing and
   analysis. BetterDesktop.org was released at the 2006 GNOME Summit
   in Boston.

 - Redesigned the Novell Linux Desktop 10 panel, start menu and
   applets to support a new search based paradigm for the desktop.

 - Created a usability test review system for logging usability
   test results in real time while users were asked to complete tasks
   using a Linux desktop, mock application and even paper mockups.


Education
=========

 - B.S. in Information Sciences and Technology from Pennsylvania State University - University Park, PA
 - B.A. in History from The University of Houston - Houston, TX
