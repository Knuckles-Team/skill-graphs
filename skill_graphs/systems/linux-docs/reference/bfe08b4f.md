```
VLS user guide

Cyril Deguet

Alexis de Lattre

Copyright � 2002, 2003 the VideoLAN project


 This document is the complete user guide of VLS .

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Free Documentation License, Version 1.2 or any later
version published by the Free Software Foundation ; with no Invariant
Sections, with no Front-Cover Texts, and with no Back-Cover Texts. The text
of the license can be found in the appendix GNU Free Documentation License.

-----------------------------------------------------------------------------
Table of Contents
1. Introduction
    1.1. What is the VideoLAN project ?
    1.2. What is a codec ?
    1.3. How can I use VideoLAN ?
    1.4. Command line usage


2. Installing VLS
    2.1. Installing VLS
    2.2. Uninstalling VLS


3. Overview and basic concepts
    3.1. VLS structure
    3.2. Administration interface


4. Configuration
    4.1. General structure
    4.2. Writing a vls.cfg


5. Running VLS
    5.1. Launching VLS
    5.2. Using the telnet interface
    5.3. Interface commands


A. GNU Free Documentation License
    A.1. PREAMBLE
    A.2. APPLICABILITY AND DEFINITIONS
    A.3. VERBATIM COPYING
    A.4. COPYING IN QUANTITY
    A.5. MODIFICATIONS
    A.6. COMBINING DOCUMENTS
    A.7. COLLECTIONS OF DOCUMENTS
    A.8. AGGREGATION WITH INDEPENDENT WORKS
    A.9. TRANSLATION
    A.10. TERMINATION
    A.11. FUTURE REVISIONS OF THIS LICENSE
    A.12. ADDENDUM: How to use this License for your documents



List of Figures
1-1. Global VideoLAN solution La solution VideoLAN globale
1-2. Windows terminal
1-3. Linux X terminal
1-4. Mac OS X terminal
1-5. BeOS terminal
3-1. VLS structure

-----------------------------------------------------------------------------
Chapter 1. Introduction

1.1. What is the VideoLAN project ?

1.1.1. Overview

VideoLAN is a complete software solution for video streaming, developed by
students of the Ecole Centrale Paris and developers from all over the world,
under the GNU General Public License (GPL). VideoLAN is designed to stream
MPEG videos on high bandwidth networks.

The VideoLAN solution includes :

��*�VLS (VideoLAN Server), which can stream MPEG-1, MPEG-2 and MPEG-4 files,
    DVDs, digital satellite channels, digital terrestrial television channels
    and live videos on the network in unicast or multicast,

��*�VLC (initially VideoLAN Client), which can be used as a server to stream
    MPEG-1, MPEG-2 and MPEG-4 files, DVDs and live videos on the network in
    unicast or multicast ; or used as a client to receive, decode and display
    MPEG streams under multiple operating systems.


Here is an illustration of the complete VideoLAN solution :


Figure 1-1. Global VideoLAN solution La solution VideoLAN globale

[global-diagram]

More details about the project can be found on the [http://www.videolan.org/]
VideoLAN Web site.
-----------------------------------------------------------------------------

1.1.2. VideoLAN software

1.1.2.1. VLC

VLC works on many platforms : Linux, Windows, Mac OS X, BeOS, *BSD, Solaris,
Familiar Linux, Yopy/Linupy and QNX. It can read :

��*�MPEG-1, MPEG-2 and MPEG-4 / DivX files from a hard disk, a CD-ROM drive,
    ...

��*�DVDs and VCDs,

��*�from a satellite card (DVB-S),

��*�MPEG-1, MPEG-2 and MPEG-4 streams from the network sent by VLS or VLC's
    stream output.


 VLC can also be used as a server to stream :

��*�MPEG-1, MPEG-2 and MPEG-4 / DivX files,

��*�DVDs,

��*�from an MPEG encoding card,


  to :

��*�one machine (i.e. to one IP address) : this is called unicast,

��*�a dynamic group of machines that the clients can join or leave (i.e. to a
    multicast IP address) : this is called multicast,


in IPv4 or IPv6 .

To get the complete list of VLC's possibilities on each plateform supported,
see the VLC features page.

Note VLC doesn't work on Mac OS 9, and will probably never do.
-----------------------------------------------------------------------------

1.1.2.2. VLS

  VLS can stream :

��*� an MPEG-1, MPEG-2 or MPEG-4 files stored on a hard drive or on a CD,

��*� a DVD located in a local DVD drive or copied on a hard disk,

��*� a satellite card (DVB-S) or a digital terrestrial television card (DVB-T)
    ,

��*� an MPEG encoding card ;


to:

��*�one machine (i.e. to one IP address) : this is called unicast,

��*�a dynamic group of machines that the clients can join or leave (i.e. to a
    multicast IP address) : this is called multicast,


in IPv4 or IPv6 .

A Pentium 100 MHz with 32 MB of memory should be enough to send one stream on
the network. When streaming a lot of videos stored on a hard drive, the
actual limitation is not the processor but the hard drive and the network
connection.

VLS works under Linux and Windows. To get the complete list of VLS's
possibilities on each plateform supported, see the streaming features page.
-----------------------------------------------------------------------------

1.1.2.3. Mini-SAP-server

 You can add a channel information service based on the SAP/SDP standard to
the VideoLAN solution. The mini-SAP-server sends announces about the
multicast programs on the network in IPv4 or IPv6, and VLCs receive these
announces and automatically add the programs announced to their playlist.

 The mini-SAP-server works under Linux and Mac OS X.
-----------------------------------------------------------------------------

1.2. What is a codec ?

 To fully understand the VideoLAN solution, you must understand the
difference between a codec and a container format

��*� A codec is a compression algorithm, used to reduce the size of a stream.
    There are audio codecs and video codecs. MPEG-1, MPEG-2, MPEG-4, Vorbis,
    DivX, ... are codecs

��*� A container format contains one or several streams already encoded by
    codecs. Very often, there is an audio stream and a video one. AVI, Ogg,
    MOV, ASF, ... are container formats. The streams contained can be encoded
    using different codecs. In a perfect world, you could put any codec in
    any container format. Unfortunately, there are some incompatibilities.
    You can find a matrix of possible codecs and container formats on the
    features page


 To decode a stream, VLC first demuxes it. This means that it reads the
container format and separates audio, video, and subtitles, if any. Then,
each of these are passed decoders that do the mathematical processing to
decompress the streams .

 There is a particular thing about MPEG:

��*� MPEG is a codec. There are several versions of it, called MPEG-1,
    MPEG-2, MPEG-4, ...

��*�MPEG is also a container format, sometimes referred to as MPEG System.
    There are several types of MPEG: ES, PS, and TS

    When you play an MPEG video from a DVD, for instance, the MPEG stream is
    actually composed of several streams (called Elementary Streams, ES):
    there is one stream for video, one for audio, another for subtitles, and
    so on. These different streams are mixed together into a single Program
    Stream (PS). So, the .VOB files you can find in a DVD are actually
    MPEG-PS files. But this PS format is not adapted for streaming video
    through a network or by satellite, for instance. So, another format
    called Transport Stream (TS) was designed for streaming MPEG videos
    through such channels.


-----------------------------------------------------------------------------
1.3. How can I use VideoLAN ?

1.3.1. Documentation

 The user documentation of VideoLAN is made up of 4 documents :

��*� the VideoLAN Quickstart. This document will give you a quick overview of
    of VLC, VLC's stream output, the Video On Demand solution and the channel
    information service system.

��*� the VideoLAN HOWTO. This document is the complete guide of the VideoLAN
    streaming solution.

��*� the VLC user guide. This document is the complete guide for VLC.

��*� the VLS user guide. This document is the complete guide for VLS.

��*� the VideoLAN FAQ. This document contains Frequently Asked Questions
    about VideoLAN.


  The latest version of these documents can be found on the [http://
www.videolan.org/doc/] documentation page .

  You can also have a look at the [http://wiki.videolan.org] VideoLAN Wiki.
This is a website that everyone can change. We use it to document everything
that is not in the "official" documentation: the tips and tricks for each
O.S., the graphical interfaces, etc...
-----------------------------------------------------------------------------

1.3.2. User support

  If you have problems using VideoLAN, and if you don't find the answer to
your problems in the documentation, please look at the online archive of the
mailing-lists. There are two English-speaking mailing-lists for the users :

��*�vlc@videolan.org for the questions on VLC ,

��*�streaming@videolan.org for the questions on VLS, mini-SAP-server and the
    network .


  If you want to subscribe or unsubscribe to the mailing-lists, please go to
the [http://www.videolan.org/support/lists.html]  mailing-list page.

 You can also talk with VideoLAN users and developers on IRC : server
irc.freenode.net, channel #videolan .

 If you find a bug, please follow the instructions on the [http://
www.videolan.org/support/bug-reporting.html]  bug reporting page .
-----------------------------------------------------------------------------

1.4. Command line usage

��*�  VLC has many different graphical interfaces, that are organized quite
    differently in order to be in harmony with the guidelines of each
    operating system supported. Documenting the use of each graphical
    interface is too long, and some features are only available via the
    command line interface. Therefore we decided to document only the command
    line interface, but in many cases it should be easy to guess how to use
    the graphical interface for the same use !

��*� VLS has a command line and a telnet interface, but no graphical
    interface !


  All the commands that show up in this document should be typed inside a
terminal. .
-----------------------------------------------------------------------------

1.4.1. Open a terminal

1.4.1.1. Windows

 Click on Start, Run and type :

��*�cmd Enter (Windows 2000 / XP),

��*�command Enter (Windows 95 / 98 / ME).


 The terminal appears Le terminal apparait


Figure 1-2. Windows terminal

[terminal-windows]

Note Under Windows, you need to be in the directory where the program is
     installed to run it.
-----------------------------------------------------------------------------

1.4.1.2. Linux / Unix

 Open a terminal :


Figure 1-3. Linux X terminal

[terminal-linux]

 In the documentation, we adopt the following conventions for the Unix
commands :

��*� commands that should be typed as root have a # prompt :
    # command_to_be_typed_as_root

��*� commands that should be typed as a regular user have a % prompt :
    % command_to_be_typed_as_regular_user


-----------------------------------------------------------------------------
1.4.1.3. Mac OS X

  Go to Applications, open the folder Utilities and double-click on Terminal
:


Figure 1-4. Mac OS X terminal

[terminal-macosx]

Note Under Mac OS X, you need to be in the directory where the program is
     installed to run it, and start the command with ./ .
-----------------------------------------------------------------------------

1.4.1.4. BeOS

 In the deskbar, go to Application and then Terminal :


Figure 1-5. BeOS terminal

[terminal-beos]

Note Under BeOS, you need to be in the directory where the program is
     installed to run it, and start the command with ./ .
-----------------------------------------------------------------------------

Chapter 2. Installing VLS

2.1. Installing VLS

2.1.1. Windows

 Download the ZIP file from the VLS Windows download page, unzip-it and run
setup.exe .
-----------------------------------------------------------------------------

2.1.2. GNULinux & Mac OS X

2.1.2.1. Install the libraries

 Many libraries are needed for particular uses

��*�libdvbpsi (always needed)

��*�libdvdcss if you want to be able to access encrypted DVDs ,

��*�libdvdread if you want to be able to stream DVDs ,

��*�libdvb if you want to be able to stream from a DVB card (a satellite card
    or a digital terrestrial TV card) .


 Download the libraries from the VLS sources download page .

 For each library, uncompress, configure (unless for libdvb which doesn't
have a ./configure), compile and install :
% tar xvzf library.tar.gz
% cd library
% ./configure
% make
# make install

 Check that the configuration file /etc/ld.so.conf contains the following
line :
/usr/local/lib

 If the line is not present, add-it and then run :
# ldconfig
-----------------------------------------------------------------------------

2.1.2.2. Install VLS

 Download the sources of the latest release : get the file vls-version.tar.gz
from the VLS sources download page. Uncompress-it and generate ./configure :
% tar xvzf vls-version.tar.gz
% cd vls-version

 To get the list of configuration options, do
% ./configure --help

 Then configure vls :

��*� if you want a basic VLS without DVD support, do :
    % ./configure --disable-dvd

��*� if you want a VLS with DVD support, do :
    % ./configure

��*� if you want a VLS with DVB support, do :
    % ./configure --enable-dvb --with-dvb=PATH_TO_DVB_DRIVERS --with-libdvb=PATH_TO_LIBDVB


 Then, compile and install :
% make
# make install

 You can also do a make uninstall, make clean or make distclean as needed .
-----------------------------------------------------------------------------

2.2. Uninstalling VLS

2.2.1. Windows

 Go to the Control Panel, click on Add and remove programs, select VLS and
click on Modify/Remove and follow the steps to uninstall the program .
-----------------------------------------------------------------------------

2.2.2. If you compiled VLS from sources

 Go to the directory containing VLS sources and run :
# make uninstall

 Then you can remove the VLS sources .
-----------------------------------------------------------------------------

Chapter 3. Overview and basic concepts

3.1. VLS structure

 From a user's point of view, VLS can be divided into four kinds of
components :

��*� a manager ,

��*� inputs ,

��*� converters ,

��*�  et des sorties .


Figure 3-1. VLS structure

[archi-vls]
-----------------------------------------------------------------------------

3.1.1. Input

 The role of an input is to read MPEG streams from a given source (file, DVD,
DVB card, device, ...), and feed the right converters with these streams. An
input may be able to read several streams, which are called programs. There
are several kinds of inputs :

��*� the local input, which can read videos from files or DVDs ,

��*�  the video input, which can read videos from MPEG encoding cards devices
    ,

��*� the dvb input, which can read videos from DVB cards, l'entr�e dvb, qui
    peut lire depuis des cartes DVB,

��*� the v4l input, which can read from acquisition cards supported by the
    Video4Linux drivers .


 You can use several inputs and play several programs at the same time .
-----------------------------------------------------------------------------

3.1.2. Converter

 The role of a converter is to receive a stream from an input, and convert it
into the MPEG-TS format. VLS is able to convert PS streams (from DVDs, for
instance) into TS streams (ps2ts converter). Of course, it can also read TS
streams, and fix them by handling stream discontinuities (ts2ts converter) .
-----------------------------------------------------------------------------

3.1.3. Channel

  A channel receives a stream from a converter, and send it to a given
destination (network, file, ...). If you want, you can call a "channel" an
"output": it is the same thing !). Currently, two kinds of channels are
supported: network and file. Note that, at the moment, VLS can support only
one output per stream, so you cannot play a stream on the network and write
it into a file at the same time. The network output is highly configurable:
you can choose which network interface you want to use, and specify source
and destination IP addresses .
-----------------------------------------------------------------------------

3.1.4. Manager

 The manager controls the way streams are sent. Through an administration
interface, you can tell the manager to start, stop, suspend, resume, forward
or rewind the different programs. You can also get a list of all programs
available in the Program Table. The manager gets this table from the VLS
configuration file (vls.cfg), so it cannot be changed once VLS has been
started. At the moment, you cannot ask the manager whether a given stream is
being broadcasted, but you will get an error message if you try to stop a
stream that was not broadcasted .
-----------------------------------------------------------------------------

3.2. Administration interface

 There are currently two ways to launch the streaming :

��*� you can use the command line to give arguments at startup;

��*� or you can use the telnet interface to start/stop/pause the streaming
    whenever you want .


 When using the telnet interface, you must authenticate before typing any
command, because any user may not be allowed to execute any command (this can
be configured in the vls.cfg configuration file) .
-----------------------------------------------------------------------------

Chapter 4. Configuration

 VLS reads its configuration from the vls.cfg configuration file, which is
supposed to be located in the current directory or in SYSCONF_DIR/videolan/
vls (where SYSCONF_DIR is /usr/local/etc if you built and installed VLS by
hand, or is /etc if you installed the debian binary package) .

 To write a vls.cfg file, use the one supplied with VLS as a start-point .
-----------------------------------------------------------------------------

4.1. General structure

 VLS configuration file vls.cfg is divided into sections, and each section
may contain several variables :
BEGIN "FirstSection"
  Variable1 = "value1"
  Variable2 = "value2"
  [...]
END

BEGIN "SecondSection"
  Variable1 = "value1"
  Variable3 = "value3"
  [...]
END


[...]

 All section names, variable names and values are not case-sensitive. There
can be empty sections and subsections. Comments must follow a # character.
Some variables have a default value; it means that you can omit to declare
these variables, and then they will be given their default value .
-----------------------------------------------------------------------------

4.2. Writing a vls.cfg

 Here is an explanation of all the sections you can find in a vls.cfg :
-----------------------------------------------------------------------------

4.2.1. Section "Vls"

 This section contains application wide settings .
LogFile = "name"

 Name of VLS log file. If left empty "", then no logging to files is done.
Default is "vls.log" .
SystemLog = "[disable|enable]"

 Logging to the SystemLog. Today, only the SystemLog using syslogd is
implemented: compile with ./configure --enable-syslog .

Caution If VLS is started as vlsd, then the following configuration is
        mandatory :
        BEGIN "Vls"
          LogFile   = ""
          SystemLog = "enabled"
          ScreenLog = "disabled"
        END
ScreenLog = "[disable|enable]"

 Logging to the console .

 Example :
BEGIN "Vls"
  LogFile   = "vls.log"
  SystemLog = "disable"
  ScreenLog = "enable"
END
-----------------------------------------------------------------------------

4.2.2. Section "Groups"

 In this section, you can define some groups of users, and which commands
these users are allowed to execute. For each group you want to define, you
must add a line in the following format :
groupname = "command1|command2|..."

 This adds a group "groupname", the users of which are allowed to execute
command1, command2, and so on. At the moment, the available commands are:
help, browse, start, suspend, resume, forward, rewind, stop, shutdown, logout
.

 Example :
BEGIN "Groups"
  monitor = "help|browse|logout"
  master  = "help|browse|start|resume|suspend|forward|rewind|stop|shutdown|logout"
END
-----------------------------------------------------------------------------

4.2.3. Section "Users"

 This section contains a list of users allowed to control VLS through an
administration interface. For each user, add a line in the following format :
username = "password:groupname"

 This adds a user "username", who belongs to the group "groupname" (defined
in the "Groups" section) and can log in with the password "password" .

��*� Under Unix/Linux, the password must be encrypted, with a tool such as
    mkpasswd, or with the UNIX function "crypt" .

��*� Under Windows, the password must be in clear text .


 Example for Unix/Linux :
BEGIN "Users"
  monitor = "3BcKWoiQn0vi6:monitor"       # password is 'monitor'
  admin   = "42BKiCguFAL/c:master"        # password is 'Vir4Gv5S'
END
-----------------------------------------------------------------------------

4.2.4. Section "Telnet"

 In this section, you can configure the telnet administration interface .
LocalPort = "port"

 Defines which port will be used for the telnet server. Default port is
"9999" .
Domain = "domain"

 Either "inet4" or "inet6" (default is "inet4"). If you want to use IPv4
addresses, put "inet4", and if you want to use IPv6, put "inet6" .
LocalAddress = "IP address"

 Defines on which IP address the telnet server will listen for requests.
Default address is "0.0.0.0" (or "0::0" with IPv6) .
