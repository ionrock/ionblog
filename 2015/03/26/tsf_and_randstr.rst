tsf and randstr
===============

I wrote a couple *really* small tools the other day that I packaged
up. I hope someone else finds them useful!

tsf
---

`tsf <https://github.com/ionrock/tsf>`_ directs stdin to a timestamped
file or directory. For example:

.. code-block:: bash

   $ curl http://ionrock.org | tsf homepage.html

The output from the cURL request goes into a file
`20150326123412-homepage.html`. You can also specify that a directory
should be used.

.. code-block:: bash

   $ curl http://ionrock.org | tsf -d homepage.html

That will create a `homepage.html` directory with the timestamped
files in the directory.

Why is this helpful?
~~~~~~~~~~~~~~~~~~~~

I often debug things by writing small scripts that automate repetitive
actions. It is common that I'll keep around output for this sort of
thing so I can examine it. Using `tsf`, it is a little less likely
that I'll overwrite a version that I needed to keep.

Another place it can be helpful is if you periodically run a script
and you need to keep the result in a time stamped file. It does that
too.

randstr
-------

`randstr <https://github.com/ionrock/randstr>`_ is a function creates
a random string.

.. code-block:: python

   from randstr import randstr

   print(randstr())

`randstr` provides some globals containing different sets of
characters you can pass in to the call in order to get different
varieties of random strings. You can also set the length.

Why is this helpful?
~~~~~~~~~~~~~~~~~~~~

I've written this function a ton of times so I figured it was worth
making a package out of it. It is helpful for testing b/c you can
easily create random identifiers. For example:

.. code-block:: python

   from randstr import randstr

   batch_records = [{'name': randstr()} for i in range(1000)]

I'm sure there are other tools out there that do similar or exactly
the same thing, but these are mine and I like them. I hope you do too.


.. author:: default
.. categories:: code
.. tags:: python, tools
.. comments::
