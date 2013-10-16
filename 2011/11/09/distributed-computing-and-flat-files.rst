Distributed Computing and Flat Files
####################################

Lately, I've been thinking a lot about different MapReduce
implementations. I noticed a theme regarding most systems was the
establishment of some file system. One reason is to have some level of
abstraction over the distributed data, but the more I think about it,
the real reason is because you need to have atomic pieces in order to
compute something in a distributed manner.

The great thing about a file is that you can always read it. At some
level all databases end up reading files (except the in memory ones...)
and this works well because reading doesn't interfere with anyone else.
This is why you see web servers handle static files an order of
magnitude faster than dynamic pages. A dynamic page has to consider
state and anytime you need to check the state that means something gets
computed or something changed. In order to distribute computation over
distinct resources, you need to avoid those state changes and what
better way than files.

With that concept in mind, I want to test the speed of reading files in
different systems but the process of testing it is not apples to apples
because some system might do some low level tricks or read other files.
For argument's sake, I'm going to disregard the physical disk. If a disk
is faster then it will be faster and if you are doing something at a
very low level to be sure data gets written in a way that avoids seeks
on the platter, then it is beyond simply "reading a file" because it is
dependent on how it was written. Hopefully this gives me a decent enough
picture to see what reading a file really costs.

I'm going to throw out the typical disclaimer that these are just silly
benchmarks that hopefully help me drawn a general conclusion regarding
reading files. I'm not trying to say one language is faster than another
past finding out whether a higher level language using a C function is
an order of magnitude slower than a compiled language that uses the same
C system calls.

The two languages I chose are Go and Python. Python should be an
obvious choice because I use it every day and if I were to write some
sort of distributed processing system based on reading files, it would
be Python I'd turn to first. The decision to use Go is because it is a
"system" language and I'm somewhat interested in it because it does do
concurrency well, even though this test has absolutely nothing to do
with concurrency.

Here is the Python: ::

  import sys
   
  if __name__ == '__main__':
      fname = sys.argv[1]
      print 'got', fname
      afile = open(fname)
      count = 0
      chunk = afile.read(512)
      while chunk:
          chunk = afile.read(512)
          count += 1
      print count

We are reading the file once through via 512 byte chunks instead
looping over the lines just because in Go we'll have to read the file by
chunks.

Here is the code in Go: ::

  package main
   
  import (
       "os"
       "fmt"
  )
   
  func main() {
       var fname string = os.Args[1]
       var buf [512]byte
       var count int
   
       fmt.Printf("Got %s\n", fname)
   
       afile, _ := os.Open(fname)
       for {
           nr, _ := afile.Read(buf[:])
           if nr == 0 || nr < 0 {
               fmt.Print(count)
               os.Exit(1)
           }
           count++
       }
  }

I'm just learning Go and honestly don't know nearly as much as I'd like
about C, so please take this with a grain of salt.

I ran both programs a few times using the time command. The results
were pretty similar. ::

  # Using Go
  real 0m0.049s
  user 0m0.012s
  sys 0m0.036s
  # Using Python
  real 0m0.054s
  user 0m0.044s
  sys 0m0.012s

The conclusion I would draw is not that one is faster than the other,
but simply, that opening a file is usually about the same in in most
languages. This is an important point because it means that some
database is typically going to have a similar level of overhead just
reading files. If you can optimize things further once you open the
files, there is a decent chance you can create something that is faster
than a generic database. This optimization is probably non-trivial.
Parsing the content of the file could be expensive and navigating the
contents could also be difficult. That said, most databases keep a
customized format on the disk in order to find delimiters and limit
creating tons of files. In a MapReduce type system, looping over all the
files in a directory and knowing that the whole file needs to be read as
a single entity could actually be an optimization vs. having to seek to
different portions in order to find specific information.

No matter what sort of system you need to build, it is good to know
that you are building it on the shoulders of all the great software
engineers that came before you. At some point the concept of a "file"
became a critical interface and that interface still stands as a
valuable tool to getting work done. It is not surprising that the simple
file still manages to be at the center of innovation as we move towards
more and more cores, crossing massive networks.


.. author:: default
.. categories:: code
.. tags:: mongodb, programming, python, testing
.. comments::
