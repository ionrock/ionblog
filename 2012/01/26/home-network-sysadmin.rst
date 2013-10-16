Home Network Sysadmin
#####################

After an excellent term of service, my Linksys WRT54G finally started
showing its age and revealed a need to be replaced. It was the first
wireless router I had ever had and served me well. Yet, with new
hardware comes new possibilities.

Besides an upgrade to the newer specifications, one of my goals was to
find a router that allowed network storage. NAS systems have become
insanely cheap, but they are not mobile. We often need our files on the
road, which means the router + hard drive combination is a slightly
better fit.

I settled on a Netgear WNR3500L after a good 20 minutes at Frys randomly
looking at the selection of networking gear. This process took much
longer than expected as my home sysadmin skills have wavered in light of
cheap VPS hosting. It was always a lot of fun to run a dynamic DNS
service and host my website and media files at home. Unfortunately, I
now value reliable service over noodling on geeky endeavors at the
house. The result is that computer and home network hardware have failed
to pique my interest for quite some time. I'd consider myself completely
out of the loop when it comes to knowing what kinds of hardware is out
there. Fortunately for me, home networking gear hasn't changed too
terribly much.

My new router supports something called Readyshare (they put a TM at the
end of this, so I suspect it is something specific to Netgear) that will
let you place a USB based storage device on the network. It shares it
via Samba. It was trivial to set up and I was backing up my data in no
time.

I also use Vonage for my home phone and previously had its router doing
my local DHCP and sitting in front of my wireless router. Seeing as I
rarely even use my home phone (it forwards to my cell), it made more
sense to go ahead an put this new wireless router first in the chain.
After a little trial an error, I configured my vonage router with a
static IP and opened the necessary ports for UDP traffic, successfully
allowing my home phone to function once again. The fact this didn't take
a few days of noodling to get to work made me feel pretty good about the
whole process.

There are times where I wish I could be a sysadmin. Actually, I take
that back. There are times I wish I knew what a sysadmin knows. None of
it is so difficult you can't understand it, but it takes practice and
requires a different type of mindset that thrives in making software and
hardware play nice. I'm confident when this router dies after 10+ years
I'll have another chance to flex my sysadmin muscles a bit at home and
be thankful for the experience. But, I'm also thankful I don't have to
do it every day. Thanks to all you sysadmins out there!


.. author:: default
.. categories:: code
.. tags:: sysadmin
.. comments::
