============================
 Simple Test Driven Develop
============================

I've always been a theoretical proponent of Test Driven Development
(TDD). Part of it is simple pragmatism. It is nice to imagine a world
where you can simply write code, switch to a terminal, run the tests and
pretty much know things are working. This is especially heavenly when
compared to testing Javascript across browsers.

Yet, when I have really looked into TDD as a structured practice it
becomes less inviting. There are some ideas that promote fixing code so
tests pass, regardless of whether or not you really solve the problem.
I'm positive there is a rigor that helps to make this a successful means
of writing code, but for me it is just a bit too abstract and
scholastic. I'll admit that I don't know what the heck I'm talking
about. But, since first impressions are important, it seems relevant to
point out that TDD as a documented practice (much like Extreme
Programming) doesn't make as much sense.

With that in mind here is my description of how to do TDD.

1. Write something you think should work.

The first thing you can do before you test is having something to test.
Consider it a hypothesis where you had an idea for some and made a first
pass at implementing it. I have real problem writing tests first. It is
difficult to imagine what you should really test. I have enough problems
thinking about how to design and write a program where doing the same
for tests before there is any code just doesn't make sense. Even if you
invest the time to come up with decent tests, you could have easily
invested the time in the initial design and in both cases you would have
gained the benefits of thinking through a problem. So, why waste the
time on the tests and go ahead and learn more about your actual code and
usually the domain you're programming in.

2. Write something to prove that it basically works.

If you write Python, there is the "if \_\_name\_\_ == '\_\_main\_\_'"
pattern. This is the kind of thing I'm talking about. You can write a
small bit of code to make sure things look OK. If it is an API you get a
minute to think about what it looks like to code to it. You also get a
sanity check for catching compiler type errors such as spelling mistakes
or broken imports. The idea here is not to write a test per se, but
rather just create a small bit of code to help get the basics working.
3. Write a test that encompasses your basic proof.

Eventually, your basic code is going to start getting complicated. I
don't have a rule for this and neither should you. If you find you've
written the same thing twice, then that is a good time to try moving it
to some tests. At this point you need to make sure your test environment
is really working for you. From here on out you are going to actually be
doing things like writing tests as you add features, so you want to be
sure that your bases are covered. The goal is to have a command to run
that tells you your code is working. You have some code that more or
less works and you need a way to automate more complicated input to that
code. Hopefully this subtle difference is clear.

4. Write a test for each feature/bug.

At this point you have a command to run your tests and individual
tests. This is probably using something like `nose`_ or `py.test`_. Now
you can really get on the ball and start doing more TDD-ish practices
like writing tests before code. The reason that it works at this point
is because you can start introducing different input in a structured
way. You're not firing blind into the dark without any idea what is even
out there. You've written your code and found something that sort of
works. You've put together a means of testing it and covering more use
cases. Now you can think in terms of more uses cases that need tests.
5. Refactor the code.

This last step is to point out that after you test should be prepared
to potentially refactor your code. This is kind of the point. Tests give
you confidence that you haven't backtracked and broken things.

Refactoring is where you can improve your communication skills by making
the code clearer. I'd lump in adding comments and documentation to this
step as well since documenting is a good way to realize flaws in your
design. When you realize that you just gave 14 steps for connecting to
your simple RESTful service, then you'll probably see there are some
details that still need work.

That is pretty much it. I'm a proponent of writing tests first, but
only when you really have a grasp on what you're doing. One of the draws
of TDD (and most development practices) is that you are forced to think
about the problem. Most people do poorly at the waterfall method of
project management because they don't have the discipline to that
thinking up front. In of TDD, moving that process to the test writing
phase has presents the same discipline requirement with the same lack of
understanding. I think things like agile project management don't
necessarily skirt the planning issues as much as they point out that
failing fast and learning is what really works. In this case my
simplified version of TDD is there to help fail fast and learn. What's
more you can potentially learn more about your users rather than your
own ideas about your users. Your users won't run your tests, they will
be running your code, so focus on what solves user's problems.


.. _nose: http://somethingaboutorange.com/mrl/projects/nose/0.11.1/
.. _py.test: http://pytest.org


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
