Be Careful Designing DSLs
#########################

During my brief stint as a Ruby developer the flavor of the week seemed
to be writing Domain Specific Languages or DSLs. The DLS trend was
exceptionally disturbing to me as I came from the world of XML, which is
effectively a world of DSLs with angle brackets.

FWIW, I never avoided XML. I still think XSLT is a great, yet highly
misunderstood, language. The problem with XML was the users. Most users
of XML (myself included) don't realize the technical debt required for
an XML format. You start using XML and creating your own formats without
understanding that those formats are exceptionally important for data
interop. What's more, many times you don't even need your own format
since something like JSON or even a RPC call would be better.

The thing that draws people into the XML rabbit hole is the parser. You
don't have to go very far from your core language to parse and process
XML data. That is a really big deal! Writing parsers and designing
languages are hard. But just because it is easy to parse, doesn't make
it a good language.

Recently I started writing a simple query language for MongoDB. The idea
is to provide a concise language to be used in a URL query string. I've
made an effort to write down my ideas on what could work. My goal is not
to construct an entirely new language here and instead build on the
shoulders of giants by drawing from things like the GMail advanced query
format and Xapian.

What I'm finding is that writing a good DSL is really hard! The parsing
is half the trouble because it is easy to feel like you designed a good
language only to realize your simple parser is going to become really
complicated. Likewise, if you do choose to emphasize easy parsing, there
is a good chance your language could suffer. Not to mention the
subjective nature of what makes a language "good" or "bad". I had a
short epiphany that using a LISP like dialect would make parsing really
easy and knew in the back of my mind its syntax would be jarring to most
users.

The point being is that writing a parser is not terribly difficult once
you understand the principles. Coming up with a small DSL can be
relatively easy as well. What is difficult is finding the right balance
where your language and parser are both maintainable for the foreseeable
future. Finding a balance of theoretical quality among practical
constraints is a huge challenge and no one to be taken lightly.
Hopefully, my current attempt will find some of the balance and I won't
regret the result.


.. author:: default
.. categories:: code
.. tags:: programming
.. comments::
