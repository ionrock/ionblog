Mundane Exercises
#################

It can be frustrating to see a ton of code that needs to be refactored
in order to use a new API. Often the process can be automated, but at
the same time, taking the time to automate it might take longer than
just plowing through it. Even though it can be a pain in the neck and
you might fee like you're slinging text, there is usually something to
learn in the process.

I remember a time at my first job that I refactored some code that was
written using a strange (at least to me) style. I found the style was
meant for C code and it emphasized a means of debugging. Nonetheless, I
found it extremely frustrating that I had to edit the file so much just
to read and understand the code. My manager at the time said that was a
good thing, but personally, I felt a lot of pressure to get this done
quickly and thought the process was a waste. Now that I'm a bit older
and wiser, I understand what my old manager meant. It is helpful to get
hands on with code and to see what breaks. Breaking things and getting
your hands dirty is partially why you have tools like version control
and test suites. At the same time, it doesn't make you feel any better
editing mundane text.

The way around this is try and establish a repotoire of repitive tools.
You can always write scripts to read in files, look for some text and
change it accordingly. Like others have said before me, learn regexes
and try to enjoy them because they can make repetative tasks much
easier. But what if a script really is too much work and yet
find/replace isn't quite up to snuff? This is when your editor and your
knowledge of that tool becomes paramount.

But before we get to editing, one thing that is extremely helpful is to
have simple typing skills. Sometimes it is pretty easy to just type
things out rather than look up some keyboard shortcut or command. It is
not a matter of typing fast, but typing quickly with accuracy can be a
huge win. Now back to editors.

Seeing as I use Emacs there are couple tools that have been really
helpful. The first is a regex search and replace. Emacs allows a rather
large set of complex regex operations as well as incrementally
performing the replacements in a way that you can also small edits
midstream. Honestly, I always forget the keybindings for this, so I'm
still working on getting this tactic into my own toolbelt.

The biggest win for me personally has been macros. In Emacs you can
record a macro that will let you do anything in Emacs and repeat the
process. This includes switching to other files, copying and pasting and
executing shell commands. For example, I wanted to change some import
statements in a set of files. I was able to grep for the statements I
wanted to change and then create a macro to visit each point in the file
buffer and adjust the import. It was extremely easy and made a somewhat
error prone manual process automated and reliable.

If you don't use Emacs (shocking!!) then take time and learn how to do
automated editing in Vim (I hear it excels as this sort of thing) or via
command line tools like sed. In taking the time to work through the
mundane, whether it is with a tool or just slinging code, you'll come
out the other side understanding more.


.. author:: default
.. categories:: code
.. tags:: emacs, programming, python
.. comments::
