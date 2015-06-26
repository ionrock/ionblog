=================
 Docker and Chef
=================

Chef is considered a "configuration management" tool, but really is an
environment automation tool. Chef makes an effort to peform operations
on your system according to a series of recipes. In theory, these
recipes provide a declarative means of:

 1. Defining the process of performing some operations
 2. Defining the different paths to complete an operation
 3. The completed state on the system when the recipe has finished

An obvious, configuration specific, example would be a chef recipe to
add a new httpd config file in `/etc/httpd/sites.enabled.d/` or
somewhere similar. You can use similar tactics you see in make check
if you have a newer file or not and how to apply the change.

Defining the operations that need to happen, along with handling valid
error cases, is non-trivial. When you add to that also defining what
the final state should look like between processes running, file
changes or even database updates, you have a ton of work to do with an
incredible amount of room for error.

Docker, while it is not a configuration management tool, allows you to
bundle your build with your configuration, thus separating some of the
responsibility. This doesn't preclude using chef as much as it limits
it to configuring the system in which you will run the containers.

Putting this into more concrete terms, what we want is a cascading
system that allows each level to encapsulate its responsibilities. By
doing so, a declaration that some requirement has been met can allow
the lower layer to report back a simple true/false.

In a nutshell, use chef to configure the host that will run your
processes. Use docker containers to run your process with the
production configuration bundled in the container. By doing so, you
take advantage of Chef and its community cookbooks while making
configuration of your application encapsulated in your build step and
the resulting container.

While this **should** work, there are still questions to
consider. Chef can dyanmically find configuration values when
converging while a docker container's filesystem is read only. While I
don't have a clear answer for this, my gut says it shouldn't be that
difficult to sort out in a reliable pattern. For example, chef could
check out some tagged configuration from a git repo that gets mounted
at `/etc/$appname` when running the container. Another option would be
to use `etcd <https://github.com/coreos/etcd>`_ to update the
filesystem mounted in a container. In either case, the application
uses the filesystem normally, while chef provides the dynamism when
converging.

Another concern is that in order to use docker containers, it is
important you have access to a docker registry. Fortunately, this is a
relatively simple process. One downside is that there is not a
OpenStack Swift backed v2 registry. The other option is to use docker
hub and pay for more private containers. The containers should be
registered as private because they include the production
configuration.

It seems clear that a declarative system is valuable when configuring a
host. Unfortunately, the reality is that the resources that are
typically "declared" with Chef are too complex to maintain a
completely declarative pattern. Using docker, a container can be
can be tested reliably such that a running container is enough to
consider its dependency met in the declared state.


.. author:: default
.. categories:: code
.. tags:: devops, docker, chef
.. comments::
