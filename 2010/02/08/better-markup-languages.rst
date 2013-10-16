Better Markup Languages
#######################

I used to be a big fan of XML and I've realized that while it definitely
has its place, there it has been misused the vast majority of the time.
What is interesting is that when I did work with XML, one area that it
seemed to excel in my mind was for document type content. I don't mean
documents as in `JSON`_ and `CouchDB`_, but actual documents like blog
posts, articles, books, etc.
It would make sense then that I would think HTML is a good arena for
XML-ish content, but I'm getting to the point where I'm not sure this is
the case. Recently, I took a look at `HAML`_ and `SASS`_. I didn't try
using them, but simply went through the docs and got a better idea what
the actual markup might look like. The inherit link to `Ruby`_ was
actually appealing because using it in `Rails`_ made so much sense.
Getting rid of the angle brackets in the template language (`ERB`_ I
think) really improved the templates and made things feel like Ruby.
Being a Pythonista, I wondered where's the `Python`_ version.
While I didn't find a port, I did find `SHPAML`_. It seemed really
similar, so I tried writing a few examples. My first impression was that
the syntax would make for a great template library. After talking to
some folks about this, it became clear integrating it into another
template library would make sense. Lo and behold `Mako`_ had a
preprocessor argument that let you do things like run a function on the
template content before passing it to the Mako processor. Adding that
argument let me immediately integrate SHPAML and Mako. It was way too
easy.
The templates looked nice. They did need a bit of getting used to, but
overall, they were really simple. Today I saw a blog about how `HAML it
is bad for content`_. It makes a ton of sense. In fact, that is why I
write my blogs in Emacs using webblogger.el. I get to write like I'm
writing an email, yet I don't have any of the email client to HTML cruft
that always seems to be a problem.
I still think XML has its place, but honestly that place is becoming
harder and harder for me to find. At this point, I'm going to suggest it
can make for a good interchange format, but even then I'm not sure where
something like JSON and conventions wouldn't be a better place to start.
What is making a ton of sense is optimizing templates for the purpose of
the markup. I know HTML is not going anywhere any time soon and HTML
makes for an OK output format. But, it doesn't mean you need to author
in HTML. This has been common for actual content, but I think for
templates you can get some advantages using something like HAML or
SHPAML. Likewise, using something like Markdown or reStructuredText for
actual content is another way to optimize the document formats.
The gain is subtle, but important. It is just a little nicer writing a
SHPAML file. It is not so large a difference that you never want to
write HTML again, but it is enough that the code makes a little more
sense. Personally, while it increases the complexity of the tool chain,
it reduces the complexity of the actual code being written. In this
case, I think the hidden complexity is worth it if you can understand
the templates faster. C did the same thing with machine code, so it is
the same thing here. If you've looked at these sorts of tools before and
dismissed them, I'd suggest taking another look and actually try it.
While it is a question of taste, I believe more people might enjoy the
markup tools more than they expect.

.. _JSON: http://json.org
.. _CouchDB: http://couchdb.apache.org/
.. _HAML: http://haml-lang.com/
.. _SASS: http://sass-lang.com
.. _Ruby: http://ruby-lang.org
.. _Rails: http://rubyonrails.com
.. _ERB: http://ruby-doc.org/stdlib/libdoc/erb/rdoc/classes/ERB.html
.. _Python: http://python.org
.. _SHPAML: http://shpaml.webfaction.com
.. _Mako: http://makotemplates.org
.. _HAML it is bad for content: http://chriseppstein.github.com/blog/2010/02/08/haml-sucks-for-content/


.. author:: default
.. categories:: code
.. tags:: Uncategorized
.. comments::
