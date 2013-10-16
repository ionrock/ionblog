=================================
 Recognizing Patterns and Macros
=================================

If you've ever had to write a language for a user you've probably had a
vision of how you could make things easier for the user to write in
domain specific language (DSL). The thing about many DSLs is that they
inherit from the parent language. I'm specifically looking at you Ruby,
even though that is no where close to the real use case I'm describing.
No, my use case is much closer to the many declarative XML based
languages. These are all languages that, aside from the parser, create
syntax and structure from scratch.

The question then is how do you recognize when your initial structure
has outgrown its humble roots. More importantly, how do you meet your
users requirements without increasing complexity? I should also mention
that complexity is the only real measure that we should be addressing.
This is my opinion, but it is based in the idea that no matter the
syntax, complexity is what you are battling against. Complexity is also
not simply a measure of how many different tokens or keywords, but
rather the number of specific details that must be kept in the forefront
of your mind in order to get the correct meaning.

Lets take a look at a piece of code:

::

    eligible_rangliste1_counter=int[]
    eligible_rangliste2_counter=int[]
    eligible_rangliste2a_counter=int[]
    eligible_rangliste3_counter=int[]
    eligible_rangliste4_counter=int[]
    eligible_rangliste5_counter=int[]
    eligible_rangliste5a_counter=int[]
    eligible_rangliste6_counter=int[]

This looks pretty nasty. The first optimization would be to allow
something like a dict. I'm going to focus on Python references b/c not
only is that what I use every day, but it is also the parent language.
If we improve things by introducing a dict, then that makes sense for
the initial variable definitions. But then the question is how you use
those variables. The above code block is actually within a set of code
defined between some curly braces (think wiki syntax as opposed to a C
function). Outside of the curly braces the syntax changes.

Using one of the variables in the traditional scope, the core of the
special language, we prefix its usage with a $. Again, it is very
similar to a template language in this regard. The problem is things
like square brackets already have meaning within the parser in the
normal scope. This makes it somewhat difficult to simply add features
like a dict that would generally improve the use of complicated or
repetitive patterns.

This is the challenge in having a DSL. On the one hand it makes things
much simpler. You can write a simple language that doesn't have to look
like HTML or other more visually noisy languages that have a subtle
parsing requirement that doesn't really help authors. On the other hand,
the parser must be written in a way to support later features that might
conflict with the current syntax that is in the field. Backwards
compatibility is a must in these situations because unless you've
written your parser and objects in such a way as to allow lossless
serialization, fixing old scripts ends up being a bug ridden exercise in
regex.

Beyond the practical challenges of syntax, there are still questions as
to what is truly easier for users. Take an idea such as modules, again
as in Python. How do you allow including them in the code? Do they get
included where they effectively become written inline or can we import
the code, adding thing via a virtual context. How does the editor play a
role in the whole operation? In our case, the language is not something
people interact with on the command line but rather via a simple web
interface. Therefore, things like imports/includes involve not only the
mechanical functionality, but the UI for writing, validating and storing
them within their own scope. When you consider the environment you have
the consideration of whether or not the include actually becomes like a
macro when the code gets saved. Likewise, macros are another tact to
take in order to make things easier for scripters to reuse code.

In some ways the answer is really all of the above, but that still begs
the question of whether moving the complexity outside of the basic
language and script has simplified things or in fact just moved the
complexity. What you want to do is remove complexity by allowing the
user to think at a higher level. This means abstractions that create a
contract with the more detailed lower level aspects lets the user work
without the need to consider whether or not some lower level piece gets
done. Adding things like imports/includes and macros may all do that,
but they are dependent on how they are used. Some fancy user might end
up writing scripts like this:

::

    include opening
    include b2b_12
    include b2b_13
    include b2b_14
    include gen_opt_6
    include footer
    include postproc

At this point you've successfully created something extremely opaque.
The complexity is not gone, but simply moved.

Just like in programming you notice patterns and develop tactics for
abstraction, when writing a DSL you have a similar task. The difference
is that instead of writing it for your own use cases in a known language
where users are expected to understand a larger environment (build
system, vcs, editor, etc.), you are defining a language for a
potentially non-technical user. These users don't read blogs on writing
code. They don't go to conferences for your language. The users don't
look forward to the latest version that includes closures. Instead they
rely on you to guide their options in a way that lets them get their
work done quickly. It is your responsibility to take their use cases,
find the patterns and figure out a way of adding abstractions that
actually help improve the complexity. It is anything but easy.



.. author:: default
.. categories:: code
.. tags:: programming, python
.. comments::
