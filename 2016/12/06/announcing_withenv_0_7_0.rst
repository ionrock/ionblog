Announcing Withenv 0.7.0
========================

I pushed a new version of `Withenv
<https://github.com/ionrock/withenv>`_ and thought it might be helpful
to discuss some new features.


No More Shells
--------------

In order to make things easy for me, I used `shell=True` when calling
commands within `Withenv`. I've removed that aspect and started
parsing the shell commands in order to avoid the shell. Replacements
should still work as expected.

This removes some security risk by explicit replacements and
avoiding the shell. Shells can be leaky with environment information,
and I'd like people to feel comfortable passing secrets via
`Withenv`.


Pipes
-----

`Withenv` allows dynamic environment variables to be injected by
calling commands and scripts. This was always a little kludgy to me. I
had hoped I could do something like `/bin/bash my.sh` and inspect the
environment afterwards in order to reuse local shell scripts people
write to manage environments.

Instead, when working on a `Go <https://golang.org>`_ version of
`Withenv <https://github.com/ionrock/we>`_, I realized I could just
load up JSON or YAML from a command. There are tons of commands that
will output JSON, so this seemed like a reaosnable plan.

With that in mind, you often want to use a piped command. For example,
lets say I'm trying to get a secret token. I might do something like
this:

.. code-block:: bash

   $ curl -X POST http://internal.auth.example.org/tokens | jq .user.token

I went ahead an implementing the piping between commands so you can
use this sort of thing your `Withenv` YAML.

.. code-block:: yaml

   ---
   - IDURL: http://internal.auth.example.org/tokens
   - TOKEN: "`curl -X $IDURL | jq .user.token`"


The Future
----------

There are two things I've been working on. The first is feature parity
with the Go version. This has been for my own practice and to provide
a lighter weight solution in that might be more palletable to a larger
audience. The second is implementing some config file templates.

I wrote a version of this in Go, but I'd like to consider one in
Python that uses a popular template language. The idea is you can
provide a template and `Withenv` will use the environment as the
context and write a file before starting the process. You could then
configure the file to be deleted when tht process exits or even after
some specified time where the upstream process should have already
loaded it into memory.

This adds a lot of complexity, so we'll see if it makes it. I
originally wrote this tooling as another tool, which might be the best
course of action. I'd also like to support the same config language in
the Go version, but, for now at least, I'm hoping I don't need to
write a `jinja2 <http://jinja.pocoo.org/>`_ parser in Go.


.. author:: default
.. categories:: code
.. tags:: devops, python, golang
.. comments::
