
 Example :
BEGIN "Telnet"
  LocalPort = "9999"
END
-----------------------------------------------------------------------------

4.2.5. Section "NativeAdmin"

 Same syntax as "Telnet". Not used yet .
-----------------------------------------------------------------------------

4.2.6. Section "Inputs"

 In this section, you can define which inputs you want to use. For each input
you need, add a line in the following format :
InputName = "Type"

 This adds a input named "InputName", the type of which is "Type". As
explained before, there are several types of input :

��*�  "local" to play a stream from a file or a DVD ,

��*� "video" to play a stream from an MPEG encoding card ,

��*� "dvb" to play a stream from a DVB card ,

��*� "v4l" to play a stream from a Video4Linux device .


 Each input must be configured in its own section (see next paragraph) .

 Example :
BEGIN "Inputs"
  local1 = "local"
  pvr    = "video"
  dvb1   = "dvb"
  tuner  = "v4l"
END
-----------------------------------------------------------------------------

4.2.7. Inputs configuration

 For each input declared in the "Inputs" section, excepted "local" inputs,
you must add a section with the same name as the corresponding input. For
instance, if you declared an input "pvr", there should be one section named
"pvr" too. The syntax of such sections depends on the type of the
corresponding input .

 To configure a local input, you don't have to do anything. Except when
another trickplay strategy must be used :
BEGIN "Local1"
  ProgramCount = "1"
  TrickPlay    = "normal"
END

 "Local1" is the name of the local input you want to configure.
"ProgramCount" is the number of programs assigned to this input. "TrickPlay"
is the trickplay strategy that is used by this input (default is "normal") .

 To configure a video input, add a section in the following format :
BEGIN "VideoInputName"
  Device = "device"
  Type   = "type"
END

 "VideoInputName" is the name of the video input you want to configure.
"Device" is the path of the MPEG encoding card you want to read from (default
is "/dev/video"). "Type" is either "Mpeg2-PS" or "Mpeg2-TS", depending on
your device configuration (default is "Mpeg2-PS") .

 Example for a Hauppauge WinTV-PVR-250 card :
BEGIN "pvr"
  Device = "/dev/video0"
  Type   = "Mpeg2-PS"
END

 To configure a dvb input, add a section in the following format :
BEGIN "DvbInputName"
  DeviceNumber = "devicenumber"
  SendMethod   = "0"
END

 "DvbInputName" is the name of the dvb input you want to configure. Set
"SendMethod" to "0" if you to stream the complete DVB stream and set it to
"1" if you only want to stream the MPEG audio and video streams (default is
"0"). "DeviceNumber" is the number of the DVB device you want to read from
(read from /dev/ost/dvr<devicenumber>, default is ""). The dvb configuration
file is defined by the driver. You can find it in $HOME/.dvbrc for /dev/dvb/
adapter0 or in $HOME/.dvbrc.X for /dev/dvb/adapterX .

 Example :
BEGIN "dvb1"
  DeviceNumber = "0"
  TrickPlay = "normal"
END
-----------------------------------------------------------------------------

4.2.8. Section "Channels"

 In this section, you can define the channels (outputs) you want to use. For
each channel, write a line in the following format :
ChannelName = "Type"

 This adds a channel named "ChannelName", the type of which is "Type". "Type"
must be either "network" or "file". Like inputs, channels must be configured
in their own section .

 Example :
BEGIN "Channels"
  localhost  = "network"
  client1    = "network"
  client2    = "network"
  multicast1 = "network"
  multicast2 = "network"
  localfile  = "file"
END
-----------------------------------------------------------------------------

4.2.9. Channels configuration

 For each channel declared in the "Channels" section, you must add a section
with the same name as the corresponding channel. The syntax of such a section
depends on the type of the corresponding channel .

 To configure a network channel, add a section in the following format :
BEGIN "NetChannelName"
  Domain    = "Domain"
  Type      = "Type"
  SrcHost   = "SourceHost"
  SrcPort   = "SourcePort"
  DstHost   = "DestHost"
  DstPort   = "DestPort"
  TTL       = "ttl"
  Interface = "Interface"
END

��*� "NetChannelName" is the name of the network channel you want to
    configure .

��*� "Domain" is either "inet4" if you use IPv4 addresses, or "inet6" if you
    use IPv6 (default is "inet4") .

��*� "Type" is either "unicast", "broadcast" or "multicast" (default is
    "unicast"), depending on what you want to do (and on your "DstHost"
    address) .

��*� "SourceHost" is the IP address (or DNS name) from which VLS will send
    the stream .

��*� "SourcePort" is the UDP port from which the stream will be sent .

��*� "DestHost" is the IP address (or DNS name) to which the stream will be
    sent .

��*� "DestPort" is the UDP port to which the stream will be sent (default is
    "1234") .

��*� "TTL" is an option useful only if "Type" is "multicast" (default value
    is "0"). You can use it to increase the TTL of your multicast packets if
    they have to cross several routers .

��*� "Interface" is an option only supported under GNU/Linux, to force the
    stream to be sent through a given network interface, "eth1" for instance"
    (to use this option, you must have super-user permissions) .


Note "SrcHost" and "SrcPort" are optional (if you don't set them, VLS will
     not 'bind' the socket) .

 To configure a file channel, add a section in the following format :
BEGIN "FileChannelName"
  FileName = "file"
  Append   = "append"
END

 "FileChannelName" is the name of the file channel you want to configure.
"file" is the name of the file where the stream will be stored (default is
"fileout.ts"). "append" is either "yes" or "no", and indicates whether VLS
will append the stream at the end of the file, or rewrite it .

 Example :
BEGIN "localhost"         # The client is on the same host as the server
  DstHost = "localhost"
  DstPort = "1234"
END

BEGIN "client1"           # unicast towards client1
  DstHost = "192.168.1.2"
  DstPort = "1234"
END

BEGIN "client2"           # unicast towards client2 in IPv6
  Domain  = "inet6"
  DstHost = "3ffe:ffff::2:12:42"
  DstPort = "1234"
END

BEGIN "multicast1"         # multicast streaming
  Type    = "multicast"
  DstHost = "239.2.12.42"
  DstPort = "1234"
  TTL     = "2"
END

BEGIN "multicast2"         # multicast streaming in IPv6
  Domain  = "inet6"
  Type    = "multicast"
  DstHost = "ff08::1"
  DstPort = "1234"
  TTL     = "12"
END

BEGIN "localfile"         # file output
  FileName = "stream.ts"
  Append   = "no"
END

Caution If you use Windows, you should specify the "SrcHost" and "SrcPort"
        fields. For example :
        BEGIN "client1"         # The client is on the same host as the server
          SrcHost = "192.168.1.1"  # IP of VLS
          SrcPort = "1242"         # Source port : the value is not important
          DstHost = "192.168.1.2"  # IP of the client
          DstPort = "1234"
        END
-----------------------------------------------------------------------------

4.2.10. Programs Configuration

 As explained before, you must define the programs. Each one is a MPEG stream
(a file, for example). To do this, you must add an "Input" section in your
vls.cfg file. Each "Input" section must have the following syntax :
BEGIN "Input"
  FilesPath    = "path"
  ProgramCount = "count"
END

 "path" is the path where your MPEG files are located (by default it is the
current directory). "count" is the number of programs defined ("0" by
default) .

 For each program you want to define, you must add a section with the
following format :
BEGIN "number"
  Name     = "name"
  Type     = "type"
  FileName = "file"
  Device   = "device"
END

��*� "number" is the program number: the first program has number 1, the
    second number 2, and so on .

��*� "name" is the program name, by which you will tell VLS to start this
    program (see next chapter "Running VLS") .

��*� "type" can be "Mpeg1-PS", "Mpeg2-PS", "Mpeg2-TS", or "DVD". If your
    stream is stored in a MPEG file (*.mpeg, *.mpg, *.vob, and so on...), it
    is probably in Mpeg1-PS or Mpeg2-PS format .

��*� if "type" is set to "Mpeg1-PS", "Mpeg2-PS", or "Mpeg2-TS", VLS will
    assume your stream is stored in the file "file", in the directory "path"
    ("path" being the variable defined in the "Input" section) .

��*� if "type" is "DVD", the variable "Device" will be used instead of
    "FileName" (the variable "FilesPath" is not prepended to the device name
    !). The variable "Device" is the device of your DVD drive ("/dev/hdc" or
    "/dev/cdrom" for instance). You can also play a DVD copied on a hard
    disk: then "device" is the directory where the .vob files are stored ("/
    mnt/data/VIDEO_TS" for instance) .


Note VLS can stream MPEG files that meet two criteria :

     ��*�the file must be MPEG PS (Program Stream) or MPEG TS (Transport Stream),
         that contain video and audio multiplexed. VLS cannot stream MPEG ES
         (Elementary Stream), i.e. a file with only audio or video .

         In order to know if an MPEG file is MPEG PS, MPEG TS or MPEG ES, read the
         file with VLC and look at the messages (select in the menu View / Messages,
         or use the command line vlc -vvv) .

         ��+�If you see a line :

             [00000107] main module debug: using demux module "ts_dvbpsi"

             it means the file is MPEG TS .

         ��+�If you see a line :

             [00000109] main module debug: using demux module "ps"

             it means the file is MPEG PS .

         ��+�If you see a line :

             [00000109] main module debug: using demux module "es"

             it means the file is MPEG ES, VLS can't stream it. .


     ��*�the sequence header of the video must repeat itself regularly, which is
         often the case with MPEG-2, but very rare with MPEG-1. There is no easy way
         to know if the sequence header is repeated regularly. Files with a .vob
         extension are normally MPEG-2 files and files with .mpg or .mpeg extension
         or usually MPEG-1 files .


     You can download this streamable MPEG-2 PS file for your tests : [ftp://
     ftp.videolan.org/pub/videolan/streams/presentation/presentation_short.vob]
     presentation_short.vob .

Note In order to play DVDs, you need to compile VLS with DVD support, which
     uses libdvdread and libdvdcss. You will need read and write access
     rights to the DVD device .

 Full example :
BEGIN "Input"
  FilesPath = "/home/videolan/streams"
  ProgramCount = "4"
END

BEGIN "1"     # MPEG2 stream stored in /home/videolan/streams/Dolby.vob
  Name     = "dolby"
  FileName = "Dolby.vob"
  Type     = "Mpeg2-PS"
END

BEGIN "2"     # another file
  Name     = "canyon"
  FileName = "Dolby_Canyon.vob"
  Type     = "Mpeg2-PS"
END

BEGIN "3"     # DVD
  Name     = "dvd"
  Device   = "/dev/cdrom"
  Type     = "Dvd"
END

BEGIN "4"     # DVD stored on a hard disk
  Name     = "matrix"
  Device   = "/mnt/data/matrix/VIDEO_TS"
  Type     = "Dvd"
END
-----------------------------------------------------------------------------

Chapter 5. Running VLS

5.1. Launching VLS

 If you want to use the telnet interface, running VLS is very easy: just type
vls in a shell console, and that's all. Running vlsd will start VLS as a
daemon and will detach itself from the launching shell. Remember that VLS
will try to load its configuration file (vls.cfg) from the current directory,
and if there is no vls.cfg there, it will try to load it from SYSCONF_DIR/etc
/videolan (see section Configuration) .

Caution If your log file is vls.log as in the example, VLS will need write access in
        the current directory, or you will see something like :
        *** Exception *** in copy constructor (0xbffffc98, copy of 0x80e30a8)
        Unable to open the log file "vls.log": Error: Could not open file 'vls.log':
        Permission denied

        Remember also that you must be root when using the "Interface" option in
        vls.cfg .

  If everything is right, you will see something like :
VideoLAN Server v 0.5.3 (Jun  6 2003) - (c)1999-2003 VideoLAN
2002-03-09 17:24:51 [INFO/Vls]  Module "channel:file" registered
2002-03-09 17:24:51 [INFO/Vls]  Module "channel:network" registered
2002-03-09 17:24:51 [INFO/Vls]  Module "mpegreader:file" registered
2002-03-09 17:24:51 [INFO/Vls]  Module "mpegconverter:ts2ts" registered
[...]

 What you can see on the screen (stderr) is exactly what goes in the log file
vls.log .

 When VLS has been successfully started, it doesn't take any command from its
standard input, so you can put it into background (you can use the screen
utility to do that) .

 On the other hand, if you want to use the command line interface, please see
the [http://www.videolan.org/doc/] VideoLAN HOWTO .
-----------------------------------------------------------------------------

5.2. Using the telnet interface

 After VLS has been launched, it opens a telnet server (on the port 9999 by
default). You can connect to this server with the following command :
% telnet localhost 9999

 You should see something like :
Trying 127.0.0.1...
Connected to vls.
Escape character is '^]'.

Videolan Server Administration System

Login:

 Then you must authenticate with a login/password pair defined in vls.cfg.
When you have been successfully authenticated, you should see a prompt like :
admin@vls>
>

 Then you can type some commands, which are explained in the next paragraph.
To log out, type logout after the telnet prompt .
-----------------------------------------------------------------------------

5.3. Interface commands

5.3.1. help

 Usage: help [command] .

 Called with no argument, "help" gives the list of all the commands
(available or not). Called with one argument it gives details about how to
use the specified command .
-----------------------------------------------------------------------------

5.3.2. browse

 Usage: browse [input] .

 Called without argument, "browse" gives all programs of inputs. Called with
one argument it only gives the programs of the specified input. Each program
is given with its status .
-----------------------------------------------------------------------------

5.3.3. start

  Usage: start <program> <channel> <input> [--loop] [--rtp]

 "start" launches the specified program of the specified input and broadcasts
it through the specified channel. The option "--loop" makes the program being
repeated indefinitely. The option "--rtp" makes the TS packet to be send
through the RTP protocol, as defined in RFC 1889 and RFC 2250 .
-----------------------------------------------------------------------------

5.3.4. stop
