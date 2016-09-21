=============
 Eric Larson
=============

:Address: 8510 Loralinda Dr, Austin TX 78753
:Phone Number: (512) 535-1825
:Email: eric@ionrock.org


Summary of Qualifications
=========================

I'm an expert in Python, having 10 years of experience writing Open
Source software, both as a contributor and a leader. My career has
focused on distributed computing using SOA principles utilizing cloud
technologies, taking services from local deployments to scaling across
data centers and in the cloud.


Open Source Projects
====================

 - `CacheControl <http://github.com/ionrock/cachecontrol/>`_ - A HTTP
   caching algorithm library for `requests
   <http://docs.python-requests.org/en/latest/>`_. CacheControl builds
   off of the excellent caching algorithms in httplib2 to allow for
   robust, distributed and threadsafe cache
   implementations. CacheControl is *the* recommended cache
   implementation for requests and is included in `pip
   <http://pip-installer.org>`_, the standard Python packaging tool.

 - `Withenv <https://github.com/ionrock/withenv>`_ - A tool to manage
   environment variables on a per command basis using YAML
   files. Withenv is an essential tool in our DevOps workflow for
   driving `Ansible <http://ansible.com/>`_ plays via environment
   variables. It has also been adopted by developers and operators for
   effectively managing cloud credentials in development, test and
   production.

 - `Bach <https://github.com/ionrock/bach>`_ - Bach is a set of small
   utilities written in `Go <https://golang.org>`_ to help legacy apps
   written without `12 Factor <https://12factor.net>`_ methods, bridge
   the operational gap necessary for deployment in the cloud and onn
   containers.


Work Experience
===============


Rackspace 2016-Present
----------------------

I work on the Cloud DNS team, contributing to the Openstackk DNSaaS
project `Designate
<http://docs.openstack.org/developer/designate/>`_. My role includes
upstream development, maintaining and iterating on the operational
codebase, mentoring younger developers on the team and providing
software to improve the lower level data plane as needed. Our primary
task is to release Designate as a version 2 of our Cloud DNS API,
deprecating two legacy codebases and enable billing.

 - Designed and merged a hookpoint API in upstream Designate. This
   allows applying decorators to functions via an operator's
   configuration, reducing the need to keep a separate fork of the
   codebase when changes are necessary to integrate into a specific
   environment.

 - Created, Panama, an API to enforce consistency between the legacy
   DNS control plane and Designate. Panama verifies whether a zone
   exists in either system and is able to adjust the business logic
   throughout the process of migration, giving preference to the
   relevant system over time. Panama was critical to ensuring data
   consistency across our entire DNS infrastructure.

 - Designed and co-authored a new worker model in Designate. Prior to
   this change, Designate used specialized services that were
   complicated to operate and added a huge amount of complexity in the
   codebase, including bugs that made core features broken. I
   explained the problems and a potential fix to some younger
   developers on the team and mentored them through the
   implementation, fixing the last critical bugs necessary for our
   next milestone.

 - Lead the developer side of the DevOps operational code base that
   proved to be a best practice and was implemented by many other
   teams within Rackspace. This included the use of Withenv for
   managing environment data and driving operations, the use of
   Makefiles for a standard entrypoint into projects, a documentation
   best practice to provide for pull-request based communication
   within a team and utilizing docker for consistent builds within
   development and continuous integration.

 - Within my first year, I became a Core Reviewer for Designate and
   was included in the Open Stack Leadership Team within
   Rackspace. This included presenting at the OpenStack Summit in
   Tokyo and Austin as well as attending midcycle meetups over seas.

 - Wrote Rebindr, a tool to propagate zones between two instances of
   the Bind DNS server. Rebindr provides a DNS based solution to
   ensure zones created on stealth masters are propagated to
   production masters in a timely fashion, without impacting the
   performance of the production masters. Rebindr improved propgation
   time of creates by 10x. It also allowed the rate limit for zone
   creation to go from a global limit of ~10 zones per minute to ~200.

 - Added a hilarious `dadjoke` plugin to our hubot instance to provide
   a little light hearted humor throughout the day.


YouGov 2008-2016
----------------

YouGov is a market research company providing custom statistical
analysis, survey and panel services as well as turnkey research
products. I've worked on the questionnaire and surveying system and a
data warehouse and data analytics system.

 - Introduced an effective caching mechanism for a central RESTful
   service router responsible for providing an uniform interface to
   back end services and databases. This caching layer is the essential
   means of optimization for almost all production systems.

 - Implemented a RESTful data warehouse called Pangaea using Amazon S3
   for storage and Django for the API. This system supports easy
   integration with big data analytics tools such as Amazon Redshift,
   Elastic Map Reduce, Apache Hive (via a hosted Hadoop service) and
   internal analysis using Python and R. This warehouse has allowed
   business to create a new suite of competitive, automated, high
   margin analytics products.

 - Created a declarative ETL / Data processing framework for reliably
   extracting data from existing services into our data warehouse as
   well as transforming existing data before pushing it to external
   services. These ETLs have uploaded over 1 million documents
   totaling over 1.5 terabytes of data.

 - Designed a system for ETL processes to run remotely on existing
   servers consistently without requiring ownership of the server
   OS. This allowed our data warehouse project to reduce its computing
   and space requirements by utilizing existing hosts in our
   cluster. This allowed a minimal financial and technical initial
   investment before proving its value to the company.

 - Wrote a threadsafe parser for an internal Domain Specific Language
   used for scripting surveys. This parser included support for script
   blocks using a limited subset of Python. The parser produced a JSON
   document that allowed analytics on questionnaires, but most
   importantly, it allowed us to deprecate countless custom parsers
   that had been written for other projects and for ad-hoc analysis.

 - Created Dragoman, gettext as a RESTful service that supports the
   global organizations i18n requirements across all sites and
   services. Dragoman decoupled code releases from translation updates,
   allowing the global organization to quickly update translations as
   needed at any time. This was written in my free time when I became
   tired of having to build, release and deploy a new version of the
   code in order to integrate an updated PO emailed to me by a user.


BSG Alliance 2007-2008
----------------------

BSG Alliance was a startup aimed at providing social tools such as
wikis, blogs, social networking and forums for large enterprise
customers.

 - Used Ruby on Rails to implement a REST gateway service to safely
   allow cross site communication via JavaScript. This was used to
   implement client side widgets that could safely and reliably
   communicate to our back end services on client hosts.


Amp.fm 2007-2008
----------------

Amp.fm was a short lived music startup. I met the founder and other
initial employees through blogging for O'Reilly and my work with Python
and XSLT. While there were very powerful ideas, it ended up being a good
learning experience that taught me the importance of getting things
done.

 - Utilized an utterly crazy, yet ambitious, XSLT based web framework
   to create RESTful services using AWS services during the early days
   of EC2. This was before Amazon EBS, so we used a FUSE file system
   that synced to S3!

 - Wrote an mailing list signup app in Python for a booth at the
   College Music Journal Festival in 10 minutes. This allowed us to
   collect 300+ emails over the course of the weekend.


WebWorks 2006-2007
------------------

WebWorks provides document transformation products for technical
writers. Complex technical documents can be written in word
processors such as Word or Adobe FrameMaker and exported to different
targets. The flagship product was a design and build tool called
ePublisher written in C# and utilized XSLT based pipelines for
processing documents and creating output.

 - Created a lazily evaluated object wrapper for FrameMaker documents
   in Python that utilized the low level FrameMaker C API in order to
   easily traverse documents. This library was used in both IronPython
   and CPython for custom projects as well as within ePublisher, the
   company's flagship product.

 - Implemented an extensible build tool using on IronPython that
   emulated build system features from Rails and Python (Paste, WSGI)
   in order make development with the ePublisher suite of applications
   easier. Using this build tool we were able to quickly create
   minimal templates and projects that allowed us to dogfood our build
   platform and experiment with new ideas that eventually became part
   of the product.

 - Maintained and extended ePublisher's C# codebase, build pipelines
   (XSLT) and output targets. The flagship output target was a
   customized documentation system written in HTML and JavaScript.

 - Established position as a top table tennis player in the office
   within the first week of obtaining the table.


Novell 2005 - 2006
------------------
I worked as an intern with the Product Design Team for Novell whose
function was to design and test user interfaces associated with the
GNOME desktop. Specifically, this included creating demo applications,
writing specifications and mock-ups that would be used in improving
user interfaces for the Novell Linux Desktop and its associated
applications. This included notable projects such as the Banshee Music
Player, F-Spot Photo Manager, iFolder, and desktop search integration.

 - Implemented BetterDesktop.org, an open source web site dedicated to
   improving Linux desktop usability through usability testing and
   analysis. BetterDesktop.org was released at the 2006 GNOME Summit
   in Boston.

 - Redesigned the Novell Linux Desktop 10 panel, start menu and
   applets to support a new search based paradigm for the desktop.

 - Created a usability test review system for logging usability
   test results in real time while user's were asked to complete tasks
   using a Linux desktop, mock application and even paper mock ups.

Education
=========

 - B.S. in Information Sciences and Technology from Pennsylvania State University - University Park, PA
 - B.A. in History from The University of Houston - Houston, TX
