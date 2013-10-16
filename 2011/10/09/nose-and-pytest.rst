Nose and Pytest
###############

My initial introduction to testing in Python was via `py.test`_, so it
shouldn't be surprising that it has been my preferred test runner. With
that said, I've recently started using `Nose`_ here and there. I
honestly can't say I have a huge preference, but there are a couple
things about Nose that I \*think\* make it better.
The first thing is the command line arguments. Pytest uses a rather
generic keyword flag to limit what tests are run. This always seemed
rather elegant in that you had a single place to interact with the test
gathering using powerful search idiom. When I saw that Nose actually
lets you specifically use a $file:$TestClass.$test\_method model, I
thought it must be limiting. The more I use it though, this is a much
nicer model as it lets you be more specific in a programmatic way.
Another thing I've been liking about nose is that it feels more
pluggable. Pytest seems to always use a rather specific means of
customization via its conftest.py file. Again, seeing as I don't have a
massive amount of experience, this never bothered me. Now that I've seen
some more extensive configuration, making this customizable outside of
the test runner feels like a better model.
One aspect of Pytest that I do like is how it will try to replay a
broken test to provide better debugging information. That said, I think
this depth has its negatives. The `xdist looponfail`_ flag often fails,
which I believe is due to this introspection.
What exposed some of these conclusions was the `nose.el`_ package for
Emacs. It seemed really simple, so I started `porting it to pytest`_. In
the end the port was pretty easy to get going with, but I realized that
it would never be as nice simply because pytest didn't support the same
models. I also recognized that the models seemed like they would be
helpful in many situations and not simply in an Emacs library.
I think I might go ahead and try to port the project I work on at my
job to use Nose and see what happens. There is already a good deal of
stubbing and framework that has be created before running the tests, so
that will either provide a good place to start or become a rabbit hole
of services. In either case, my hope is that in learning nose I will
widen my knowledge of testing and improve my debugging skills.
As an aside, I did look at nose a long time ago and quickly dismissed
it b/c it seemed to prescribe a specialized way to run write tests that
was incompatible with what I had at the time. That seemed like a bunch
of work for little to no gain. Looking back, I might have misunderstood
the requirements. Regardless, I hope people do not trust my suggestions
when choosing a test running tool. Do the work yourself to see what will
work best.

.. _py.test: http://pytest.org
.. _Nose: http://readthedocs.org/docs/nose/en/latest/
.. _xdist looponfail: http://pytest.org/latest/xdist.html#running-tests-in-looponfailing-mode
.. _nose.el: https://bitbucket.org/durin42/nosemacs/src/d413c247aea7/nose.el
.. _porting it to pytest: https://bitbucket.org/elarson/pytest.el


.. author:: default
.. categories:: code
.. tags:: programming, python, testing
.. comments::
