```
VLC user guide

Henri Fallon

Alexis de Lattre

Johan Bilien

Anil Daoud

Mathieu Gautier

Cl�meant Stenac

Copyright � 2002, 2003 the VideoLAN project


 This document is the complete user guide of VLC .

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


2. Modules and options for VLC
    2.1. The modules
    2.2. Video outputs
    2.3. Video filters modules
    2.4. Audio outputs
    2.5. Input modules
    2.6. Demuxers
    2.7. Interface modules
    2.8. Codec modules
    2.9. OS support modules
    2.10. Miscellaneous
    2.11. Compilation Options


3. Installing VLC
    3.1. Installing VLC
    3.2. Uninstalling VLC


4. The command line interface
    4.1. Introduction
    4.2. Opening streams
    4.3. Modules selection
    4.4. Stream Output
    4.5. Other Options


5. The Mozilla plugin
    5.1. Install the plugin
    5.2. Build HTML pages that use the plugin


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

Chapter 2. Modules and options for VLC

2.1. The modules

VLC uses a modular system, which allows to add easily new functions and
formats. Here is a description of nearly all the VLC modules. A few
"internal" modules won't be explained here. For a complete list of all VLC
modules, please have a look at the LIST file in the subdirectory "modules" of
the VLC source tree.

If you installed VLC through a binary file, you will get the default modules.
If, however, you want to customize VLC to your needs, you will have to
compile VLC from sources.

If you don't intend to compile VLC and want only the regular functions,
reading this part is not very useful.

The compilation itself is explained in the next chapter.

 If you wish to compile a module which is stated disabled by default, you
have to launch the configure script with :
% ./configure
--enable-module_name

 On the other hand, if you would like to disable a module that is enabled by
default, you would have to use :
% ./configure
--disable-module_name

 Each VLC module has its own help and options. To see what options are
associated with a module, use :
 % vlc -p
module_name

 or use the "Preferences" Panel of your favorite graphical interface .
-----------------------------------------------------------------------------

2.2. Video outputs

 Video outputs are the modules that enable the support of some systems to
display the video on your screen.
-----------------------------------------------------------------------------

2.2.1. x11

default: enabled

 For Unix with X11 servers only

 This is the basic x11 video output. It only requires a working X11 server.
You will need xlibs headers to compile it (xlibs-dev package on Debian
systems).
-----------------------------------------------------------------------------

2.2.2. xvideo

default: enabled

 For GNU/Linux only

 It requires an xvideo compliant graphic card (it is the case for nearly all
modern cards). It uses hardware acceleration for YUV transformation and
rescaling.
-----------------------------------------------------------------------------

2.2.3. sdl

default: enabled

  This video output uses sdl libraries. You need at least version 1.1.6 of
this libraries.

  You may indicate the path to the sdl-config program with the
--with-sdl-config-path=PATH switch, when running the configure script.
-----------------------------------------------------------------------------

2.2.4. directx

default: enabled on win32

 For Windows only

 This video output uses Microsoft Direct X libraries. It is recommended for
the win32 port.

 You may indicate the path to directX libraries and headers with the
--with-directx=PATH switch, when running the configure script.
-----------------------------------------------------------------------------

2.2.5. wingdi

default: enabled on win32

 For Windows only

 This video output uses GDI. It is designed for users who don't have Direct
X, but the perfs are very low. If you have DirectX, do not use it.
-----------------------------------------------------------------------------

2.2.6. fb

default: enabled on GNU/Linux

 For GNU/Linux only

 This is the frame buffer video output. It requires that your kernel was
compiled with frame buffer support.
-----------------------------------------------------------------------------

2.2.7. glide

default: disabled

 This video output uses Glide libraries (hardware acceleration for 3Dfx
cards).

 You may indicate the path to the library with the --with-glide=PATH
configure option.
-----------------------------------------------------------------------------

2.2.8. mga

default: disabled

 For GNU/Linux only

 This module provides hardware acceleration for Matrox cards under GNU/Linux.
-----------------------------------------------------------------------------

2.2.9. ggi

default: disabled
-----------------------------------------------------------------------------

2.2.10. aa

default: disabled

 This is the ASCII Art Video Output. This video output uses the aalib library
to display video through ASCII art. It requires aalib headers (aalib1-dev
package under Debian GNU/Linux) to compile.
-----------------------------------------------------------------------------

2.2.11. svgalib

default: disabled

 For GNU/Linux only

 This is a video output for the SVGAlib library.
-----------------------------------------------------------------------------

2.2.12. qte

default: disabled

 For iPaq only

 This is a video output for QT Embedded, an iPaq-specifiq graphical library .
-----------------------------------------------------------------------------

2.3. Video filters modules

 These modules allow you to perform modifications on the rendered image .
-----------------------------------------------------------------------------

2.3.1. deinterlace

Always enabled

  This filter deinterlaces video. It is useful with streams coming from a
digital satellite channel or digital terrestrial television channels .
-----------------------------------------------------------------------------

2.3.2. wall

Always enabled

 This filter allows you to have the video cut in pieces in several windows,
which you can order as you wish. It can be used to generate image walls with
several sources.
-----------------------------------------------------------------------------

2.3.3. distort

Always enabled

 This filter adds a distortion effect to the video. Who said it was useless ?
:-)
-----------------------------------------------------------------------------

2.3.4. transform

Always enabled

 This filter allows to rotate the video in several ways .
-----------------------------------------------------------------------------

2.3.5. invert

Always enabled

 This filter inverses colors.
-----------------------------------------------------------------------------

2.3.6. adjust

Always enabled

 This filter allows you to set image contrast, hue, saturation and brightness
-----------------------------------------------------------------------------

2.3.7. clone

Always enabled

  Ce filtre vous permet de dupliquer l'image.
-----------------------------------------------------------------------------

2.3.8. crop

Always enabled

 This filter allows you to crop parts of the image.
-----------------------------------------------------------------------------

2.3.9. motionblur

Always enabled

 This filter adds a "motion blur" effect to the image.
-----------------------------------------------------------------------------

2.4. Audio outputs

These modules allow you to choose the way the sound will be output to your
audio system .
-----------------------------------------------------------------------------

2.4.1. oss

default: enabled on GNU/Linux

 For GNU/Linux and Unix only

 This is the audio output for OSS (Open Sound System) output (/dev/dsp, for
example, under Linux). It requires that your kernel was compiled with support
for your sound card, or, if you use ALSA (Advanced Linux Sound System), the
OSS emulation layer must be active.
-----------------------------------------------------------------------------

2.4.2. alsa

default: disabled

 For GNU/Linux only

 This is the sound output for ALSA (Advanced Linux Sound Architecture). It
only works under Linux, and it requires that you installed the ALSA drivers
and libraries.
-----------------------------------------------------------------------------

2.4.3. esd

default: disabled

 For GNU/Linux & Unix only

 This sound output has ESD (Enlightened Sound Daemon) support (usually used
with Gnome). You must have the daemon and its libraries installed.
-----------------------------------------------------------------------------

2.4.4. arts

default: disabled

 For GNU/Linux & Unix only

 This sound output has aRts (KDE's sound server) support. You must have the
daemon and its libraries installed .
-----------------------------------------------------------------------------

2.4.5. waveout

default: enabled on win

 For Windows only

 This is the Wave output, which is used by the win32 port.
-----------------------------------------------------------------------------

2.4.6. coreaudio

default: enabled on Mac OS X

 For Mac OS X only

 This audio output uses CoreAudio under Mac OS X
-----------------------------------------------------------------------------

2.4.7. sdl

default: enabled

  This audio output uses SDL. Please refer to the video output.
-----------------------------------------------------------------------------

2.5. Input modules

 These modules allow VLC to read its streams from different sources .
-----------------------------------------------------------------------------

2.5.1. dvdplay

default: enabled

 This is the regular DVD input module. It will need libdvdcss for DVD
decryption (see the [http://developers.videolan.org/libdvdcss/] libdvdcss
page) and libdvdplay for DVD navigation (see the [http://
developers.videolan.org/libdvdplay/] libdvdplay page) .
-----------------------------------------------------------------------------

2.5.2. dvd

default: enabled

 This is the old DVD input module. It uses libdvdcss for DVD decryption (see
the libdvdcss page) .
-----------------------------------------------------------------------------

2.5.3. dvdread

default: disabled

 This is an alternative to the previous ones. It uses libdvdread for DVD
reading (see the Ogle download page) and libdvdcss for DVD decryption (see
the libdvdcss page).
-----------------------------------------------------------------------------

2.5.4. vcd

default: enabled

This is the VideoCD input .
-----------------------------------------------------------------------------

2.5.5. cdda

default: enabled

This is the Audio CD input .
-----------------------------------------------------------------------------

2.5.6. http,ftp,udp,file,directory,mms

Always enabled

 These are standard input modules. The HTTP input can be used for Video On
Demand .
-----------------------------------------------------------------------------

2.5.7. satellite

default: disabled

 This is an input module that allows to read directly from a Hauppauge WinTV
Nova card under GNU/Linux. It requires drivers 0.9.4 available from [http://
www.linuxtv.org/] linuxtv.org .
-----------------------------------------------------------------------------

2.5.8. v4l

default: disabled

 For GNU/Linux only

 This module allows to get Video4Linux streams .
-----------------------------------------------------------------------------

2.5.9. dvb

default: disabled

 For GNU/Linux only

 This module allows to read from DVB-S, DVB-T, and DBC-C satellite, digital
terrestrial, or cable cards. It uses the Video4Linux 2 API, that is only
available in kernel 2.5.X and 2.6.X .
-----------------------------------------------------------------------------

2.5.10. pvr

default: disabled

 For GNU/Linux only

 This module allows to read from Hauppauge PVR cards .
-----------------------------------------------------------------------------

2.5.11. slp

default: enabled

 This module allows to get the names and addresses for streams announced
using the SLP protocol
-----------------------------------------------------------------------------

2.6. Demuxers

 In a video stream, the video signal and the audio one are always into
"containers" formats. Demuxers extract the streams from it and pass it to the
decoders .

  For example, an AVI file can contain a MPEG-4 video, or an uncompressed
video. AVI is only a storing format, not a compression format .
-----------------------------------------------------------------------------

2.6.1. avi

Always enabled

 This module allows you to read .avi files .
-----------------------------------------------------------------------------

2.6.2. asf

Always enabled

 This module allows you to read .asf files
-----------------------------------------------------------------------------

2.6.3. aac

Always enabled

 This module allows you to read AAC files
-----------------------------------------------------------------------------

2.6.4. ogg

default: enabled

 This module allows you to read .ogg files
-----------------------------------------------------------------------------

2.6.5. rawdv

Always enabled

 This module allows you to read DV files
-----------------------------------------------------------------------------

2.6.6. dvbpsi

default: enabled

 This module allows to demux streams from a satellite card.
-----------------------------------------------------------------------------

2.6.7. mp4

Always enabled
