Packaging vs. Freezing
######################

I'm currently waiting through setting up an environment for a project
and start thinking about how slow this process is. In some ways it
doesn't really matter. How often do you really set up a development
environment? That said, if you can't easily set up your development
environment, what makes you think you are setting up your production
environment in a way that is reliable?

The essence of any installation is taking a set of files and putting
them on the file system in a way some executable can run. There can
always be other aspects such as updating databases or running some
indexing process, but generally, you put the files in the folders.

One strategy for release is to take your development structure and
simply tar it up. The benefits of this model is that it is simple and
relatively reliable. When you are deploying to a platform where all you
get is a single directory, this can in fact be advantageous. The
downside comes about when you lose your development system or whatever
system it is you are using to build from. The work you put into making
sure things run is gone and even though you can recreate it, there is no
telling what really changed.

Another strategy is to create a package. In this situation the
important thing is not the "package" but the "creation".  In this
scenario you have some sort of a tool that takes the source, compiles it
(if necessary) and places all the files in a package that can be
extracted on the file system. Unlike freezing, this process is more
reliable and understood in terms of knowing what has to happen to go
from source code to a package. The biggest hurdle is that you have know
where everything goes, which can feel like a daunting task. You also may
have to package up other dependencies, which can also be a large
endeavor.

Personally, I'm a fan of packaging. Even though my experience is
limited, I've come to the conclusion that the process of understanding
where everything is going to go, documenting it in a processable format
and creating a step for that process is the only way you really will be
certain your environment can be trust worthy.

When I say "trust worthy" I'm not talking about security. What I'm
really talking about is confidence. Businesses consistently pay more for
items that could be bought more inexpensively, but they pay the extra
cost for the confidence the good with function or be quickly replaced
when they fail. Packaging allows you to build that confidence so you can
be sure when something breaks or goes down, reproducing the environment
is just a script away. When you can't be sure you've build your
environment correctly, then you really can't be sure any of the software
will work as expected.


.. author:: default
.. categories:: code
.. tags:: programming, testing
.. comments::
