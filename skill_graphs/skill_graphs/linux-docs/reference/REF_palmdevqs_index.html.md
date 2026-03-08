#  ![](https://tldp.org/REF/palmdevqs/pics/hellocropped.gif)Linux Palm Developer's Quick Start Guide
Jim Weller

Wed Feb 21 04:33:07 AKST 2001
The current version is at
## Table of Contents
  1. [Introduction](https://tldp.org/REF/palmdevqs/index.html#intro)

  2. [Requirements](https://tldp.org/REF/palmdevqs/index.html#req)

  3. [Setup and install](https://tldp.org/REF/palmdevqs/index.html#install)

  4. [Hello world program](https://tldp.org/REF/palmdevqs/index.html#hello)

  5. [Screen shots](https://tldp.org/REF/palmdevqs/index.html#screenshots)

  6. [References](https://tldp.org/REF/palmdevqs/index.html#refs)

  7. [Downloads](https://tldp.org/REF/palmdevqs/index.html#dloads)




## 1. Introduction
This guide is intended to help those new to palm programming get started developing using linux, PRC Tools, GNU tools, and the PalmOS© SDK. It assumes a fair knowledge of linux and
These are my notes from the night when I learned these tools. It will take you from clueless to empowered (able to compile a HelloWorld program). I couldn't find a working equivalent. So, I hope this information will be helpful, but it is provided with no warranty or guarantee. If you break anything you get to keep both pieces.
[[top]](https://tldp.org/REF/palmdevqs/index.html#top)
## 2. Requirements
You'll need to download the PRC tools, the palm emulator, the PalmOS © SDK, and some [downloads](https://tldp.org/REF/palmdevqs/index.html#dloads) ). I downloaded to ~/palm/archive (YMMV).
#### PalmOS © SDK
Get sdk,examples, and docs (hidden behind cgi that makes you read license agreement)


* sdk35-docs.tar.gz
* sdk35-examples.tar.gz
* sdk35.tar.gz
#### PalmOS © Emulator
Building the emulator for linux was a another step I didn't want to deal with **yet**. Fear not. It's Weller with 2 L's. I will do it soon, and I'll rewrite this doc to reflect that portion. For now I just got the windows prebuilt emulator and skins. Pretty straight forward. You install a palm app that comes with the package to your handheld. This allows you to download the PalmOS © image from the palm's rom. You have to pay money and sign an NDA (double whammy) to get other rom images/versions. Anybody got an archive ;) Do the deed as in the readmes and Blamh your palm on your desktop. Plus you can hotsync over the network with the regular hotsync manager and the emulator.


* emulator-win.zip
* emulator_skins_15.zip
#### PRC Tools
Get the prc tools (patches to


* prc-tools-2.0.tar.gz
#### GNU Tools
Get gdb,gcc,binutils


* gdb-4.18.tar.gz
* gcc-2.95.2.tar.gz
* binutils-2.91.tar.gz

[[top]](https://tldp.org/REF/palmdevqs/index.html#top)
## 3. Setting up, building and installing the tools
Now your ready to unpack, configure, build, and install the tools. You need to do all the commands listed in the box below: including LONG ASS COMPILE®: Complete with Jim-isms and fixes. Here are some things to keep in mind about the commands in the box below.


* The SDK is not right for linux. You'll notice a move from the "Palm OS 3.5 Support" to sdkpalmos-3.5 and Incs to includes.
* Since you'll need your new versions of binutils during the build, put /usr/local/palm/bin in your PATH ahead of time
* I use the MYARCHIVEDIR and MYPALMDIR variables to store the location of important files
* The default install goes to /usr/local. I like to comparmentalize things in /usr/local/<app>. That's /usr/local/palm in this case. Then I add /usr/local/palm/bin to my PATH.

```
  export MYPALMDIR=/root/palm
  export MYARCHIVEDIR=$MYPALMDIR/archive
  export PATH=/usr/local/palm/bin:$PATH
  mkdir /usr/local/palmdev
  mkdir /usr/local/palm
  cd $MYPALMDIR
  tar -xzf $MYARCHIVEDIR/sdk35.tar.gz
  mv Palm\ OS \ 3.5\ Support/ /usr/local/palmdev/sdkpalmos-3.5
  cd /usr/local/palmdev/sdkpalmos-3.5
  mv Incs include
  cd $MYPALMDIR
  mkdir src
  cd src
  tar -xzf $MYARCHIVEDIR/binutils-2.9.1.tar.gz
  tar -xzf $MYARCHIVEDIR/gcc-2.95.2.tar.gz
  tar -xzf $MYARCHIVEDIR/gdb-4.18.tar.gz
  tar -xzf $MYARCHIVEDIR/prc-tools-2.0.tar.gz
  cat prc-tools-2.0/{binutils-2.9.1,gcc-2.95.2,gdb-4.18}.palmos.diff | patch -p0
  cd prc-tools-2.0/
  ln -s ../binutils-2.9.1 binutils
  ln -s ../gcc-2.95.2 gcc
  ln -s ../gdb-4.18 gdb
  cd ..
  mkdir build
  cd build
  mkdir empty
  ../prc-tools-2.0/configure \
    --target=m68k-palmos; \
    --enable-languages=c,c++  \
    --with-headers=`pwd`/empty  \
    --sharedstatedir=/usr/local/palmdev \
    --prefix=/usr/local/palm --with-build-sdk=3.5 \
    --exec-prefix=/usr/local/palm;
  make all-install

```

---
Assuming all goes as expected. You'll have the SDK stuff in /usr/local/palmdev and then platform specific tools (m68k-palmos-gcc,m68k-palmos-c++,m68k-palmos-ranlib, etc.) in /usr/local/palm. Now put /usr/local/palm/bin in your permanent path (edit .bashrc,.cshrc, profile etc.).
[[top]](https://tldp.org/REF/palmdevqs/index.html#top)
## 4. A Hello World Program
Now you can compile a hello proggie.
I had to hack up all the demos from the HOWTOs after reading the SDK header files. The header names, primitive types, and compiler tool's names are incorrect for version 3.5 of the PalmOS © SDK in the HOWTO samples. Plus, it appears that the Examples that come with the SDK all have zero length resource files (e.g. SampleCalculator.rsrc). I compiled the packages, but they crashed on the emulator.
Save the below snippet in a text file called hello.c .

```
#include <PalmOS.h>

// ---------------------------------------------------------------------
// PilotMain is called by the startup code and implements a simple event
// handling loop.
// ---------------------------------------------------------------------
UInt32 PilotMain( UInt16 cmd, void *cmdPBP, UInt16 launchFlags )
{
    EventType event;


    if (cmd == sysAppLaunchCmdNormalLaunch) {

        //  Display a string.
        WinDrawChars( "Hello, world!", 13, 55, 60 );

        //  Main event loop:
        do {
            //  Doze until an event arrives.
            EvtGetEvent( &event, evtWaitForever );

            //  System gets first chance to handle the event.
            SysHandleEvent( &event );

            //  Normally, we would do other event processing here.

        // Return from PilotMain when an appStopEvent is received.
        } while (event.eType != appStopEvent);
    }
    return;
}


```

---
You can compile it like this. Did you fix your PATH to have /usr/local/palm/bin ?
```
  m68k-palmos-gcc hello.c -o hello
  m68k-palmos-obj-res hello
  build-prc hello.prc "Hello, World" WRLD *.hello.grc

```

---
Blamho! Now you'll have a hello.prc that you can put in the emulator (works!) or in your palm (WORKS!).


[[top]](https://tldp.org/REF/palmdevqs/index.html#top)
## 5. Screen Shots
Here's some pics and screen shots of the emulator (running under windows) running hello.prc (compiled under linux). You'll note the name of the app is what was specified on the build-prc command line. I also tested the hello.prc file on my PalmIIIe. It Works!
![](https://tldp.org/REF/palmdevqs/pics/emulator.gif) ![](https://tldp.org/REF/palmdevqs/pics/launcher.gif) ![](https://tldp.org/REF/palmdevqs/pics/hello.gif)

[[top]](https://tldp.org/REF/palmdevqs/index.html#top)
## 6. References
I glommed all this together from the following urls.


* PRC tools



* How to build prc tools (see notes)



* POSE the PalmOS © emulator (gotta' sell soul to NDA demon to get ROMS)



* PalmOS © SDK version 3.5 (broken for linux) (see notes)



* GNU (The Ivory Tower)



* POSE HOWTO



* Palm Development howto



* Palm development article


[[top]](https://tldp.org/REF/palmdevqs/index.html#top)
## 7. Downloads
I have copies of the software mentioned locally here at












[[top]](https://tldp.org/REF/palmdevqs/index.html#top)


* * *
All trademarks and copyrighted materials on this page are owned by their respective owners. The Rest Copyright ©
