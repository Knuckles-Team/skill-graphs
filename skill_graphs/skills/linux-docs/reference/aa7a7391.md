
 This module allows you to read .mp4 files
-----------------------------------------------------------------------------

2.6.8. mkv

default: enabled

 This module allows you to read files that use the Matroska free format .
-----------------------------------------------------------------------------

2.6.9. ps,ts

Always enabled

 These modules allow you to read MPEG2 Program Stream or Transport Tream
files .
-----------------------------------------------------------------------------

2.6.10. id3,m3u

Always enabled

 These modules allow you to read M3U, B4S, PLS, and ASX playlists, and ID3
tags .
-----------------------------------------------------------------------------

2.7. Interface modules

 These modules allow you to choose the interface or interfaces you want to
use (whether graphical or control interfaces).
-----------------------------------------------------------------------------

2.7.1. wxwindows

default: enabled

 The wxWindows interface is a portable interface that is currently working
under GNU/Linux and Windows. It is now the best graphical interface available
under both Windows and GNU/Linux .
-----------------------------------------------------------------------------

2.7.2. skins

default: enabled on win32

 This skinnable interface module works under Win32 and X11. You can create
your own skins very easily with XML files .
-----------------------------------------------------------------------------

2.7.3. gtk

default: enabled

 This is the GTK+ interface. It needs gtk libraries and headers files if you
are compiling it. Note that it can also be used under Windows .
-----------------------------------------------------------------------------

2.7.4. gnome

default: disabled

 For GNU/Linux only

 This is the Gnome interface. It needs gnome libraries (libgnome32 package
under Debian) and headers (libgnome-dev package under Debian) if you wish to
compile it .
-----------------------------------------------------------------------------

2.7.5. qt

default: disabled

 This is the QT interface module. You will need the libraries (libqt2 package
on Debian) and headers (libqt-dev package under Debian) if you wish to
compile it .
-----------------------------------------------------------------------------

2.7.6. kde

default: disabled

 For GNU/Linux only

 This is the KDE interface module. You will need the libraries (kdelibs3
package on Debian) and headers (kde-devel package under Debian) if you wish
to compile it .
-----------------------------------------------------------------------------

2.7.7. rc

Always enabled

 This is the Remote Control interface module. It allows you to control VLC
via commands, such as play, stop, etc... or via a script. This interface is
text-based, so you should use it when you are in console mode .
-----------------------------------------------------------------------------

2.7.8. http

Always enabled

 This module allows you to remote control your VLC via a web browser. You can
create custom web pages. [http://wiki.videolan.org/index.php/HTTP] More info
here .
-----------------------------------------------------------------------------

2.7.9. ncurses

default: disabled

 For GNU/Linux only

  This is a text interface, using ncurses library. You will need ncurses
headers if you want to compile it (libncurses5-dev package on Debian) .
-----------------------------------------------------------------------------

2.7.10. lirc

default: disabled

 For GNU/Linux only

 This interface module allows you to control VLC through a remote. A lircrc
example is provided to help you configure it to your remote (see doc/lirc/
example.lircrc) .
-----------------------------------------------------------------------------

2.7.11. opie

default: disabled

 This is an interface plugin for the Qt Embedded library (iPaq graphical
library) .
-----------------------------------------------------------------------------

2.7.12. gestures

Always enabled

 This module allows you to control VLC via mouse gestures .
-----------------------------------------------------------------------------

2.7.13. joystick

default: disabled

 For GNU/Linux only

 This module allows you to control VLC via a joystick with many options. More
information can be found [http://wiki.videolan.org/index.php/Joystick] here .
-----------------------------------------------------------------------------

2.8. Codec modules

 The following modules add codec (ie, compression formats) support .
-----------------------------------------------------------------------------

2.8.1. a52

default: enabled

 This decoder uses liba52 (see the [http://liba52.sourceforge.net/] liba52
web site .
-----------------------------------------------------------------------------

2.8.2. ffmpeg

default: enabled

 This is a free MPEG-4/DivX/OpenDivX codec : ffmpeg (see the ffmpeg web site)
.
-----------------------------------------------------------------------------

2.8.3. vorbis

default: enabled

 This codec allows you to read the Vorbis (audio) encoded files .
-----------------------------------------------------------------------------

2.8.4. xvid

default: disabled

 This codec allows you to read files encoded with Xvid (see Xvid web site) .
-----------------------------------------------------------------------------

2.8.5. mad

default: enabled

 This codec is a very smart MP3 decoder, that only uses integers. This allows
its use for CPU which don't handle floating point numbers (on PDA, for
example) .
-----------------------------------------------------------------------------

2.8.6. libmpeg2

default: enabled

 This codec allows to read MPEG2 files .
-----------------------------------------------------------------------------

2.8.7. faad

default: disabled

 Faad is an MPEG-4 audio decoder .
-----------------------------------------------------------------------------

2.8.8. tarkin

default: disabled

 tarkin is a new codec (experimental) by the Ogg Project (see the Ogg Vorbis
web site) .
-----------------------------------------------------------------------------

2.8.9. theora

default: disabled

 theora is a new codec (experimental) by the Ogg Project (see the Ogg Vorbis
web site) .
-----------------------------------------------------------------------------

2.8.10. cinepak

default: enabled

 This codec decodes the Cinepak format .
-----------------------------------------------------------------------------

2.8.11. tremor

default: disabled

 This is an Ogg/Vorbis codec that only makes integer calculus, which allow
its use on CPU which don't have floating point support (see the Ogg Vorbis
web .
-----------------------------------------------------------------------------

2.9. OS support modules

 The following modules add support for different OSs .
-----------------------------------------------------------------------------

2.9.1. macosx

 This is the MacOS X support module, including a native interface .
-----------------------------------------------------------------------------

2.9.2. qnx

 This is the QNX RTOS support module .
-----------------------------------------------------------------------------

2.10. Miscellaneous

 This section describes a few more modules that don't belong to any of the
categories described before .
-----------------------------------------------------------------------------

2.10.1. sout

default: enabled

 Stream Output is a new feature of VLC that allows it to stream an MPEG-1,
MPEG-2 or MPEG-4/DivX file or a DVD .

 For more details, please have a look at the The command line interface
section .
-----------------------------------------------------------------------------

2.10.2. test-suite

default: disabled

 This builds a special VLC, for testing purposes only .
-----------------------------------------------------------------------------

2.10.3. mozilla

default: disabled

  This is not really a module. When enabled, a VLC-based Mozilla plugin is
built .
-----------------------------------------------------------------------------

2.10.4. xosd

default: disabled

 For Unix only

  This plugin outputs the current stream to an "OSD" (On Screen Display) .
-----------------------------------------------------------------------------

2.11. Compilation Options

 There are a few options that you can set when running the configure script,
which are not related to modules .

 You can have a look at these options by typing :
% ./configure --help

 You can for example control all the installation directories, the system for
which you want to build VLC for (if not guessed correctly),...

 You can also choose to enable or disable some optimizations.
-----------------------------------------------------------------------------

2.11.1. --disable-plugins

  If you select this option, no plugins will be enabled. This is definitely
not recommended, as you would get a very poor VLC, and should only be used
for testing purposes .
-----------------------------------------------------------------------------

Chapter 3. Installing VLC

3.1. Installing VLC

  There are VLC binaries available for the many OSes, but not for all
supported OSes. If there are no binaries for your OS or if you want to change
the default settings, you can compile VLC from sources.
-----------------------------------------------------------------------------

3.1.1. Windows

  VLC works under Windows 95/98/ME/2000/XP. Download the self-extracting file
from the VLC Windows download page. Launch the .exe to install VLC.
-----------------------------------------------------------------------------

3.1.2. BeOS

  Download the Zip file from the VLC BeOS download page. Unzip the file in a
directory to install VLC.
-----------------------------------------------------------------------------

3.1.3. Mac OS X

  Download the Mac OS X package from the VLC MacOS X download page .
Double-click on the icon of the package : an icon will appear on your
Desktop, right beside your drive(s). Open it and drag the VLC application
from the resulting window to the place where you want to install it (it
should be /Applications).
-----------------------------------------------------------------------------

3.1.4. Debian GNU/Linux

3.1.4.1. Debian stable (woody)

Add the following lines to your /etc/apt/sources.list:
deb http://www.videolan.org/pub/videolan/debian $(ARCH)/
deb-src http://www.videolan.org/pub/videolan/debian sources/

 Then, for a normal install, do:
# apt-get update
# apt-get install gnome-vlc libdvdcss2
-----------------------------------------------------------------------------

3.1.4.2. Debian unstable (sid)

Add the following lines to your /etc/apt/sources.list:
deb http://www.videolan.org/pub/videolan/debian $(ARCH)/
deb-src http://www.videolan.org/pub/videolan/debian sources/

 Then, for a normal install, do:
# apt-get update
# apt-get install wxvlc libdvdcss2
-----------------------------------------------------------------------------

3.1.4.3. Debian testing (sarge)

  You should not be using Debian testing unless you perfectly know what you
are doing. It is almost impossible to support Debian testing and there are no
plans to do it. For more information on Debian testing, please look: [http:/
/www.debian.org/devel/testing] testing page
-----------------------------------------------------------------------------

3.1.5. Linux Mandrake

  There are VLC packages for Mandrake 9.1 and cooker.

  To install them, add the following sources for either Mandrake 9.1 or
Cooker (you can use [http://plf.zarb.org/~nanardon/] Easy urpmi for that):
contrib from the core distribution and plf (Penguin Liberation Front) from
the external add-ons.

 Then install the required packages with urpmi:
# urpmi libdvdcss2 libdvdplay0 wxvlc vlc-plugin-a52 vlc-plugin-ogg vlc-plugin-mad
-----------------------------------------------------------------------------

3.1.6. Linux Redhat

 Download the RPM package vlc and the packages listed in the required
libraries and codecs section (the other packages are just optional) from the
VLC Red Hat download page and put them all into the same directory.

Then install the RPM packages you have downloaded:
# rpm -U *.rpm

  If you have not installed all the RPM packages included with your
distribution, you may be asked to install a few of them first.
-----------------------------------------------------------------------------

3.1.7. Compile the sources by yourself (for every other OS)

The method below is for any Unix system supported by VLC, for which there is
no packages available. It explains how to compile and install VLC and the
needed libraries from their source code.

You can also compile VLC under Linux this way if you want to modify the
default supported modules.
-----------------------------------------------------------------------------

3.1.7.1. Install the libraries

Many libraries are needed :

��*�libdvbpsi (compulsory) ,

��*�mpeg2dec (compulsory) ,

��*�libdvdcss if you want to be able to read encrypted DVDs ,

��*�libdvdplay if you want to have DVD menu navigation ,

��*�a52dec if you want to be able to decode the AC3 (i.e. A52) sound format
    often used in DVDs ,

��*�ffmpeg, libmad, faad2 if you want to read MPEG 4 / DivX files ,

��*�libogg & libvorbis if you want to read Ogg Vorbis files .


 Download the libraries from the VLC sources download page.

 For each library :

��*� uncompress :
    % tar xvzf library.tar.gz

    or
    % tar xvjf library.tar.bz2

��*� configure :
    % cd library
    % ./configure

��*� compile and install :
    % make
    # make install


  Check that the configuration file /etc/ld.so.conf contains the following
line :
/usr/local/lib

  If the line is not present, add-it and then run (as root):
# ldconfig
-----------------------------------------------------------------------------

3.1.7.2. Install VLC

  Download the sources of the lastest release : get the file
vlc-version.tar.gz from the VLC sources download page. Uncompress-it :
% tar xvzf vlc-version.tar.gz
% cd vlc-version

  To get the list of configuration options, do :
% ./configure --help

 Please note that all the modules are described in the Modules section of the
VLC User Guide .

 Examples of very simple configurations:

��*� if you want a basic VLC, do :
    % ./configure

��*�  if you want the Gnome interface instead of the GTK interface (you will
    need the development packages of Gnome) :
    % ./configure --enable-gnome


 Then, compile and install :
% make
% su
Password:  [Root Password]
# make install

  Please note that the installation (make install command) is not mandatory.
You can execute VLC from where you compiled it.
-----------------------------------------------------------------------------

3.2. Uninstalling VLC

3.2.1. Windows

  Click on the Uninstall VLC icon that was created during installation .
-----------------------------------------------------------------------------

3.2.2. BeOS

 Delete the vlc-version directory. You can also remove the configuration file
/boot/home/config/settings/vlcrc .
-----------------------------------------------------------------------------

3.2.3. Mac OS X

 Drag the VLC application to your trash can .
-----------------------------------------------------------------------------

3.2.4. Debian GNU/Linux

 Remove the packages that you installed :
# apt-get remove --purge vlc-gnome vlc-mad libdvdcss2 libdvbpsi1
-----------------------------------------------------------------------------

3.2.5. GNU/Linux Redhat, Mandrake and SuSE

 Uninstall the RPM packages that you installed :
# rpm -e vlc-version vlc-mad-version vlc-gnome-version
libdvdcss2-version libdvdpsi1-version
-----------------------------------------------------------------------------

3.2.6. If you compiled VLC from sources

 Go to the directory containing VLC sources and execute :
# make uninstall

 Then you can remove the VLC sources .
-----------------------------------------------------------------------------

Chapter 4. The command line interface

4.1. Introduction

 Many options are only available through command line. They are detailed here
.
-----------------------------------------------------------------------------

4.2. Opening streams

 The following commands start VLC and add the first element to the playlist .
-----------------------------------------------------------------------------

4.2.1. Opening a file

 Start VLC with :
% vlc -vvv my_file.mpg

 Although VLC should be able to recognize the file type, you may tell VLC
what codec to use with the --codec option. For example to play my_file.mpg
using ffmpeg audo/video decoder do :
% vlc -vvv --codec ffmpeg my_file.mpg

  A list of all video and audio codecs supported by VLC is available on the
VLC features list .
-----------------------------------------------------------------------------

4.2.2. Opening a DVD or VCD, or an audio CD

 Start VLC with
% vlc -vvv dvd:[device][@raw_device][@[title][,[chapter][,angle]]]


 or (VCD):
% vlc -vvv vcd:[device][@[title][,[chapter][peripherique][@[titre][,chapitre]]

 or (Audio CD):
% vlc -vvv cdda:[device][@[title]][peripherique][@[titre]]

 where device is the complete path to your DVD or CD-ROM drive .
-----------------------------------------------------------------------------

4.2.3. Start a network stream

 To receive an unicast UDP stream (sent by VLS or VLC's stream output), start
VLC with :
% vlc -vvv udp:[@:server_port]

 To receive an multicast UDP stream (sent by VLS or VLC's stream output),
start VLC with :
% vlc -vvv udp:@multicast_address[:server_port]

 To receive a HTTP stream, start VLC with :
% vlc -vvv http://www.example.org/your_file.mpg
-----------------------------------------------------------------------------

4.3. Modules selection

  VLC tries to select the most appropriate interface, input and output
modules, among the ones available on the system, according to the stream it
is given to read. However, you may wish to force the use of a specific module
with the following options (for the complete list of modules, see the Modules
and options for VLC section) ) :

��*�--intf <module> allows you to select the interface module .

��*�--extraintf <module> allows you to select extra interface modules that
    will be launched in addition to the main one .

��*�--aout <module> allows you to select the audio output module .

��*�--vout <module> allows you to select the video output module .

��*�--filter <module> allows you to add a video filter module .

��*�--memcpy <module> allows you to choose a memory copy module .


-----------------------------------------------------------------------------
4.4. Stream Output

4.4.1. Description of the stream output

 VLC's stream output allows VLC to be used as a streaming server instead of a
client ! It has very extended capabilities :

��*� stream in unicast and multicast on an IPv4 or IPv6 network everything
    that VLC is able to read, via UDP, RTP or HTTP ;

��*� save the input stream to a file in AVI, PS, TS or OGG format ;

��*� transcode an input stream, and then, send it, to the network or to a
    file .


 To know about the full possibilities of VLC's stream output, see the [http:/
/www.videolan.org/streaming/features.html]  streaming features page .
-----------------------------------------------------------------------------

4.4.2. Architecture and syntax

 the stream output has a powerful architecture that uses modules. Each module
has capabilities, and you can chain the modules to enhance the possibilities
.

 Here is the list of the modules currently available :

��*�standard "sends" the stream via an access output module: for example,
    UDP, file, HTTP, ... You will probably want to use this module at the end
    of your chains .

��*�transcode allows you to transcode the audio and the video of the input
    stream "on the fly" (if your computer is powerful enough) .

��*�duplicate allows you to create a second chain, where the stream will be
    handled in an independent way .

��*�display allows you to display the input stream, as VLC would normally do.
    Used with the duplicate module, this allows you to view the stream as you
    send it .

��*�es allows you to make separate Elementary Etreams (ES) out of an input
    stream .


 Each of these modules may take options. Here is the syntax that you must use
:
% vlc input_stream --sout '#module1{option1=...,option2=...}:#module2{option1=...,option2=...}:...'

 For example, to transcode a stream and send it, use :
% vlc input_stream --sout '#transcode{options}:#standard{options}'
-----------------------------------------------------------------------------

4.4.3. Description of the modules

4.4.3.1. standard (alias std)

 Sends a stream .

Options:

��*�access: how to send : file, udp, rtp, http.

��*�mux: which muxer (ie, which format) will be used. It can be one of avi
    (for AVI format) , ogg (for OGG format) , ps (for MPEG2-PS format) , ts
    (for MPEG2-TS format) .

��*�url: if you use the file access, it will be the location where to store
    the stream; if you use another access, it will be the unicast or
    multicast IP address where you want to stream .

��*�sap: if you use the udp or rtp accesses, use this option to announce your
    stream, using SAP/SDP. This option contains the name under which you want
    to announce the program .

��*�slp: like sap, but use the SLP protocol. You need to have libslp on your
    system .

��*�sap_ipv: if you use the sap option, use this option to specify if you
    want to send the SAP announces in IPv4 or IPv6. The value of this option
    is 4 or 6 si vous utilisez sap, utilisez ceci pour sp�cifier si vous
    d�sirez envoyer les announces SAP en IPv4 -d�faut- ou IPv6. La valeur �
    utiliser est 4 ou 6 .


Note If you are streaming in multicast, you may want to use the global option
     --ttl 12 to set the TTL to a value superior to 1.
-----------------------------------------------------------------------------

4.4.3.2. display

 Displays the stream .

Options:

��*�noaudio: Ignore audio .

��*�novideo: Ignore video .


-----------------------------------------------------------------------------
4.4.3.3. duplicate

 Duplicates the stream to a new stream output chain .

Options:

��*�dst: A new stream output chain of modules, as described earlier .


-----------------------------------------------------------------------------
4.4.3.4. transcode

 Changes the codec and/or bitrates for a stream .

Options:

��*�acodec: the new audio codec. It can be one of mpga (MPEG audio layer 2),
    a52 or ac3 (AC3 sound) or vorb (Vorbis)

��*�ab: audio bitrate in Kbps .

��*�vcodec: the new video codec. It can be one of mp4v (MPEG4), mpgv (MPEG1),
    DIV1, DIV2, DIV3 (DivX 1,2,3), H263 (H263), I263 (H263I), WMV1 or WMV2
    (Windows Media Video 1 or 2), MJPG (MJPEG), MJPB (MJPEGB) .

��*�width: video width .

��*�height: video height .

��*�vb: video bitrate in kbps .

��*�vt: video bitrate tolerance in bps .

��*�deinterlace: deinterlace the stream .

��*�croptop: number of pixels removed from the top of the video .

��*�cropbottom: number of pixel removed from the bottom of the video .

��*�cropleft: number of pixels removed from the left of the video .
