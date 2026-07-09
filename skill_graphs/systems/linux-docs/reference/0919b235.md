# deb http://security.debian.org/ stable/updates main

```

---
Contains a list of apt-sources from which packages may be installed via APT.

/etc/asound.conf

ALSA (Advanced Linux Sound Architecture) configuration file. It is normally created via alsactl or other third-party sound configuration utilities that may be specific to a distribution such as sndconfig from Redhat.

/etc/at.deny

Users denied access to the at daemon. The 'at' command allows user to execute programs at an arbitrary time.

/etc/autoconf

Configuration files for autoconf. 'autoconf' creates scripts to configure source code packages using templates. To create configure from configure.in, run the autoconf program with no arguments. autoconf processes configure.ac with the m4 macro processor, using the Autoconf macros. If you give autoconf an argument, it reads that file instead of configure.ac and writes the configuration script to the standard output instead of to configure. If you give autoconf the argument -, it reads the standard input instead of configure.ac and writes the configuration script on the standard output.
The Autoconf macros are defined in several files. Some of the files are distributed with Autoconf; autoconf reads them first. Then it looks for the optional file acsite.m4 in the directory that contains the distributed Autoconf macro files, and for the optional file aclocal.m4 in the current directory. Those files can contain your site's or the package's own Autoconf macro definitions. If a macro is defined in more than one of the files that autoconf reads, the last definition it reads overrides the earlier ones.

/etc/bash.bashrc

System wide functions and aliases' file for interactive bash shells.

/etc/bash_completion

Programmable completion functions for bash 2.05a.

/etc/chatscripts/provider

This is the chat script used to dial out to your default service provider.

/etc/cron.d, /etc/cron.daily, /etc/cron.weekly, /etc/cron.monthly

These directories contain scripts to be executed on a regular basis by the cron daemon.

/etc/crontab

'cron' configuration file. This file is for the cron table to setup the automatic running of system routines. A cron table can also be established for individual users. The location of these user cron table files will be explained later on.
```
