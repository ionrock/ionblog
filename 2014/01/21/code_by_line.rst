Code by Line
============

I saw `this tweet
<https://twitter.com/InscrutableTed/status/425811472262778880>`_:

  Limiting lines to 80 characters is a great way to ensure that
  variable names remain cryptically short while lines break in
  confusing places.

It makes some sense. For example, if I had something like:::

  put_to_s3(project_bucket, resultant_keyname, use_multipart=True, overwrite=False, confirm=True)

One way to a shorter line would be to make some variables names a bit
shorter: ::

  put_to_s3(bucket, key, use_multipart=True, overwrite=False, confirm=True)

Unfortunately, this doesnt' quite do the trick. A better tact, that
has benefits that go beyond 80 characters, is to utilize vertical
space. Or in simpler terms, code by lines rather than variables. For
example, I would have refactored the original code like this. ::

  put_to_s3(
      project_bucket,
      resultant_keyname,
      use_multipart=True,
      overwrite=False,
      confirm=True
  )

I get to keep my more descriptive names and when the signature of the
function changes or I have to add another keyword argument, the diff /
patch will be much clearer. Also, and this is obviously subjective, if
the vertical listing seems to grow large, you have a more obvious
"smell" to the code when you are browsing the codebase.

It is understandable to assume that limiting line size could result in
cryptic variable names, but more often than not, longer lines end up
being more difficult to read and decode. More importantly, you end up
fighting the endless suite of line based tools we utilize in version
control. The next time you feel limited by the line length, consider
the vertical space you have and if that might allow you to have your
descriptive variable names along side your line based coding tools.


.. author:: default
.. categories:: code
.. tags:: python vcs diff emacs
.. comments::
