Pivoting Code
#############

Programming as a culture has changed quite a bit throughout the years.

The focus on largely geeky topics has become less and less as more
people "startup" companies and consider how they can follow in the
footsteps of other great hackers and innovators. The subject matter of
most tech news relates to things like scaling, game theory and
understanding markets. There is still plenty of information about purely
geeky pursuits, but I would argue the geek of today is not interested in
the same geekery as those of yesteryear.

The term "pivot" as taken from the startup world means to change the
focus of some business in order to find success. The goal with pivoting
is that you cease to spend time polishing a turd and instead change your
focus to where actual customers are. This concept is not limited to
startups though. It is important to understand when to pivot actual code
as well.

At work we've been reworking an important system and throughout the
process I've been challenged to change the way I think about some of the
problems. My mentality up until this point has been focused on being a
good steward of the previously written software and make every attempt
to provide a fluid transition from one system to the next.

Unfortunately, I needed to pivot. The fact was that writing code that
let every old test pass was not a sustainable measure. The old tests
were wrong in some cases. They contained assumptions that were no longer
true and adjusting the tests or the code to bend to these assumption
only reduced their benefit. The converse of fixing the test often meant
doing a lot of work on new components that really had not been
specified.

The pivot came to me when I realized that I hit a barrier where the new
code needed to start becoming intermingled with the old code. It is when
the tests run in isolation become worthless because nothing is actually
using the code. I hope this sound familiar because it is almost the
exact same experience a startup founder might experience when the
product is actually released. If no one is using it then what is the
point.

With this barrier firmly in place my next steps were to see what was
working and failing. In analyzing the current state, it became clear
that I wasn't nearly as far off as I anticipated. I could continue some
of the work adjusting the tests and fixing bugs and it was actually
beneficial. What is important though was that I needed to analyze the
current state of things before moving on. When pivoting code you have to
take time to see where things are making sense and where they are not.

It is not fun work because it is monotonous and requires focus pouring
through the code, but it is beneficial and will help in pivoting how you
work on the code.

The practice of performing a pivot is as follows:

#. Stop and recognized when things are too complex
#. Analyzing the current state (what breaks and what doesn't)
#. Establish the metric that matters (fix what breaks or write new
   tests)
#. Take action

Personally, I've always had a problem making major changes to code. I'd
either just want to rewrite everything or fix it. There was no in
between. For me, pivoting is a good way to organize the middle ground.

It manages the mental complexity my brain is trying to add in a way that
is productive so I can move forward. If you ever find yourself stuck in
a rut with some code, there is a good chance a pivot would be helpful to
get things moving again.


.. author:: default
.. categories:: code
.. tags:: programming, testing
.. comments::
