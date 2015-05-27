Playing with Repose
===================

At `work <https://rackspace.com>`_ we use a proxy called `repose
<http://openrepose.org/>`_ in front of most services in order to make
common tasks such as auth, rate limiting, etc. consistent. In python,
this type of function might also be accomplished via WSGI middleware,
but by using a separate proxy, you get two benefits.

 1. The service can be written in any language that understands HTTP.
 2. The service gets to avoid many orthogonal concerns.

While the reasoning for repose makes a lot of sense, for someone not
familiar with Java, it can be a little daunting to play
with. Fortunately, the repose folks have provided some packages to
make playing with repose pretty easy.

We'll start with a `docker <https://docker.io>`_ container to
run repose. The repose docs has an `example
<https://repose.atlassian.net/wiki/display/REPOSE/Docker>`_ we can use
as a template. But first lets make a directory to play in.

.. code-block:: bash

   $ mkdir repose-playground
   $ cd repose-playground

Now lets create our `Dockerfile`:

::

   FROM ubuntu

   RUN apt-get install -y wget

   RUN wget -O - http://repo.openrepose.org/debian/pubkey.gpg | apt-key add - && echo "deb http://repo.openrepose.org/debian stable main" > /etc/apt/sources.list.d/openrepose.list

   RUN apt-get update && apt-get install -y \
     repose-valve \
     repose-filter-bundle \
     repose-extensions-filter-bundle

   CMD ["java", "-jar", "/usr/share/repose/repose-valve.jar"]


The next step will be to start up our container and grab the default
config files. This makes it much easier to experiment since we have
decent defaults.

.. code-block:: bash

   $ docker build -t repose-playground .
   $ mkdir etc
   $ docker run -it -v `pwd`/etc:/code repose-playground cp -r /etc/repose /code

Now we have our config in `./etc/respose`, we can try something
out. Lets change our default endpoint to point to a different website.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>

   <!-- To configure Repose see: http://wiki.openrepose.org/display/REPOSE/Configuration -->
   <system-model xmlns="http://docs.openrepose.org/repose/system-model/v2.0">
       <repose-cluster id="repose">
           <nodes>
               <node id="repose_node1" hostname="localhost" http-port="8080"/>
           </nodes>
           <filters></filters>
           <services></services>
           <destinations>
               <endpoint id="open_repose" protocol="http"
                         <!-- redirect to ionrock.org! -->
                         hostname="ionrock.org"
                         root-path="/" port="80"
                         default="true"/>
           </destinations>
       </repose-cluster>
   </system-model>


Now we'll run repose from our container, using our local config
instead of the config in the container.

.. code-block:: bash

   $ docker run -it -v `pwd`/etc/repose:/etc/repose -p 8080:8080


If you're using boot2docker, you can use `boot2docker ip` to find the
IP of your VM.

.. code-block:: bash

   $ export REPOSE_HOST=`boot2docker ip`
   $ curl "http://$REPOSE_HOST:8080"

You should see the homepage HTML from `ionrock.org`!

Once you have repose running, you can leave it up and change the
config as needed. Repose will periodically pick up any changes without
restarting.

I've gone ahead and automated the steps in this `repose-playground repo
<https://github.com/ionrock/repose-playground>`_. While it can be
tricky to get started with repose, especially if you're not familiar
with Java, it is worth taking a look at repose for implementing
orthogonal requirements that make the essential application code more
complex. This especially true if you're using a micro services model
where the less code the better. Just run repose on the same node,
proxying requests to your service, which only listens on `localhost`
and you're good to go.


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
