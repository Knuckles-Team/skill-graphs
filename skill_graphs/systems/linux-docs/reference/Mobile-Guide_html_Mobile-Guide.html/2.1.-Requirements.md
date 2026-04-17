#  2.1. Requirements
From the [Battery-Powered-HOWTO](http://tldp.org/HOWTO/Battery-Powered/) I got this recommendation (modified by WH):
A Message to Linux Distributors: If you happen to be a Linux distributor, thank you for reading all this. Laptops are becoming more and more popular, but still most Linux distributions are not very well prepared for portable computing. Please make this section of this document obsolete, and make a few changes in your distribution.
The installation routine should include a configuration, optimized for laptops. The _minimal install_ is often not lean enough. There are a lot of things that a laptop user does not need on the road. Just a few examples. There is no need for three different versions of **vi**. Some portable systems do not need printing support.
Don't forget to describe _laptop-specific installation problems_ , e. g. how to install your distribution without a CD/DVD-ROM drive.
Add better _power management_ and seamless _PCMCIA support_ to your distribution. Add a recompiled kernel and an alternative set of PCMCIA drivers with _apm support_ that the user can install on demand. Include a precompiled _apmd package_ with your distribution. Also include IrDA® infrared support and USB support.
Add support for dynamically _switching network configurations_. Most Linux laptops travel between locations with different network settings (e. g. the network at home, the network at the office and the network at the university) and have to change the network ID very often.
Add a _convenient PPP dialer_ with an address book, that does not try to start multiple copies of the PPP daemon if you click on the button twice (e.g., the RedHat **usernet** tool). It would be nice to have the PPP dialer also display the connection speed and some statistics. One nice command line dialer that autodetects modems and PPP services is **wvdial** from
At TuxMobil you may find a huge number of links to
  * in German
  * in Russian
  * and in Chinese


* * *
