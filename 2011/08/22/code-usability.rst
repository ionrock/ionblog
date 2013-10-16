Code Usability
##############

Often times when we as developers says some piece of code "beautiful" it
is in relation to some aspect of the functionality. Unfortunately, just
because a piece of code does some function using a rather clever
algorithm or pattern, it doesn't make that code usable. Usability is
typically considered in the realm of user interfaces, and to a lesser
extent, programming APIs. I would argue that this compartmentalization
of the word is in fact a deadly prescription for wasted time and money.
Every time you write code that gets deployed (whether that is a server,
version control system or simply a /bin directory), an "interface" is
created that should be usable. The interface I'm talking about here is
not some config or command line flags, but the actual code. When an
application is used by someone, its code needs to be maintained, which
means it must be "used".
The code interface is rarely given the actual attention it deserves,
yet it is a huge source for wasted time and energy. Consider the amount
of time you spend actually writing code vs. reading old code and fixing
bugs. For arguments sake, lets say it is 50% or 20 hours a week. Now
multiply that by your hourly salary and the number of people on your
team and you can start to see how every extra few minutes spent dealing
with code that is not usable costs time and money.
The big question then is how can we write code that is usable?
To be frank, I don't know! It is a huge challenge to create things that
are usable because you need to find a way to sit in the shoes of someone
you may not even know. Something you may believe is clear and direct
could be excruciatingly confusing to someone else. Like most everything
in software development, there is no silver bullet.
With that in mind, there are some things that can help.
The most obvious way to help communicate how to work with code is via
comments. That is why they have been present in programming languages
for so long. It became immediately clear that there is value in
providing text in the same space as code in order to help someone else
understand what is going on. Those that say it adds noise or it makes
the code difficult to read are not making the connection between
comments that communicate and comments that just are. If the comments
get in the way, then there is a good chance those comments are not very
helpful.
The goal of comments should be to answer "why" when looking at a piece
of code. Why did you write the code in the first place? Why does some
variable have some function called on it? Why isn't this abstracted into
a library or other place in the code? Why shouldn't I change it? When
you look at code for the first time you rarely have an understanding of
what is really important and what is a hack. It becomes extremely easy
to think some piece of code is the product of the prior developer's (who
you might be working for!) painstaking attention to detail. The reality
is that developer could have learned the code base starting in the very
function you are looking at and understood next to nothing about what
should really happen in the code. This is where a comment at the
beginning of the function would be extremely helpful that mentions the
writer of the code doesn't really know what is going on and that there
is most likely a better way.
This goes the other direction as well. When you write a concise
algorithm that is fast, elegant and optimized, remember that you can add
as many comments as you want describing your painstaking process and how
it is probably not a good idea to change the code very much. Not only
should take pride in making clear your process, but you make clear the
assumptions you were working under at the time. When those assumptions
change, the next developer working on the code can see immediately the
pros and cons and evaluate them according to current needs.
Since some people do find comments difficult to parse all the time when
writing code, I think it is safe to say that there are good and bad
times to write comments. My thoughts are that you should comment before
you start and before you push/commit. The comments you write before the
code should reflect the design goals, why you are writing the code and
what you hope to get out of it. They should be a thesis for the code.
They may change as the code develops, but if they are changing a lot, it
might be a signal you haven't written your comments very clearly. After
you've written the code it is time to edit prior to publishing. Make
sure your large design comments are clear and correct. Then look for
places in the code where things might be confusing and leave some notes.
Finally, if you are using a DVCS, when leave good comments in the commit
message before pushing. It is like a nice closing paragraph that wraps
up the loose ends and gives someone a clue when slogging through the VCS
logs fixing a bug you just introduced!
In terms of actual code, stick to a style. As trivial as this is, it is
paramount to good design. No designer worth his/her salt uses tons of
fonts and decorations. It is distracting and doesn't help communicate a
clear message. Code should do the same thing and sticking to a style is
a great way to do so. I think this is a huge benefit of Python and the
concept of being "pythonic." It is a commitment to a style of code that
we can all settle on in order to help reduce the number of visual
complexities our brains have to deal with when reading a cryptic format.
Similarly, C# often has a very similar style because most everyone
writing C# is using the same editor (Visual Studio). The point is, pick
a style that works with the majority of developers and stick to it.
Related to the above point on style, consider the next developer's
development environment. If your company requires a certain dev
environment, then you can depend on certain tools to be available. The
converse is that every developer has a completely different environment,
in which case you have a tougher job because the clarity you find in
keeping every class in its own file is in fact a nightmare for another
developer that feels more comfortable navigating within larger files vs.
on the file system. This is one really clear example of how code can be
usable for one person and not for another.
I'm not suggesting that you need to create a hugely detailed style that
permeates the entire code base or have rules for extreme comments. The
point is to make the code easier to use for the next developer that
looks at the code. Making simple agreements that lower the level of
complexity developers have to deal with is a good way to make the code
more usable. Just as keeping the application simple and removing
features can help make a user more successful, communicating as much
about the code as possible in order to make the next developer
successful is the goal when writing usable code.


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
