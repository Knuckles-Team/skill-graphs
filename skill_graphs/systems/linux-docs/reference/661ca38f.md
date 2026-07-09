#  Chapter 2. Starting Off With a Sha-Bang
|  _Shell programming is a 1950s juke box . . ._ _--Larry Wall_
---|---
In the simplest case, a script is nothing more than a list of system commands stored in a file. At the very least, this saves the effort of retyping that particular sequence of commands each time it is invoked.
**Example 2-1._cleanup_ : A script to clean up log files in /var/log **
```
# Cleanup
# Run as root, of course.

cd /var/log
cat /dev/null > messages
cat /dev/null > wtmp
echo "Log files cleaned up."
```

---
There is nothing unusual here, only a set of commands that could just as easily have been invoked one by one from the command-line on the console or in a terminal window. The advantages of placing the commands in a script go far beyond not having to retype them time and again. The script becomes a _program_ -- a _tool_ -- and it can easily be modified or customized for a particular application.
**Example 2-2._cleanup_ : An improved clean-up script**
```
#!/bin/bash
# Proper header for a Bash script.

# Cleanup, version 2

# Run as root, of course.
# Insert code here to print error message and exit if not root.

LOG_DIR=/var/log
# Variables are better than hard-coded values.
cd $LOG_DIR

cat /dev/null > messages
cat /dev/null > wtmp


echo "Logs cleaned up."

exit #  The right and proper method of "exiting" from a script.
     #  A bare "exit" (no parameter) returns the exit status
     #+ of the preceding command.
```

---
Now _that's_ beginning to look like a real script. But we can go even farther . . .
**Example 2-3._cleanup_ : An enhanced and generalized version of above scripts.**
```
#!/bin/bash
# Cleanup, version 3

#  Warning:
#  -------
#  This script uses quite a number of features that will be explained
#+ later on.
#  By the time you've finished the first half of the book,
#+ there should be nothing mysterious about it.



LOG_DIR=/var/log
ROOT_UID=0     # Only users with $UID 0 have root privileges.
LINES=50       # Default number of lines saved.
E_XCD=86       # Can't change directory?
E_NOTROOT=87   # Non-root exit error.


# Run as root, of course.
if [ "$UID" -ne "$ROOT_UID" ]
then
  echo "Must be root to run this script."
  exit $E_NOTROOT
fi

if [ -n "$1" ]
# Test whether command-line argument is present (non-empty).
then
  lines=$1
else
  lines=$LINES # Default, if not specified on command-line.
fi


#  Stephane Chazelas suggests the following,
#+ as a better way of checking command-line arguments,
#+ but this is still a bit advanced for this stage of the tutorial.
#
#    E_WRONGARGS=85  # Non-numerical argument (bad argument format).
#
#    case "$1" in
#    ""      ) lines=50;;
#    *[!0-9]*) echo "Usage: `basename $0` lines-to-cleanup";
#     exit $E_WRONGARGS;;
#    *       ) lines=$1;;
#    esac
#
#* Skip ahead to "Loops" chapter to decipher all this.


cd $LOG_DIR

if [ `pwd` != "$LOG_DIR" ]  # or   if [ "$PWD" != "$LOG_DIR" ]
                            # Not in /var/log?
then
  echo "Can't change to $LOG_DIR."
  exit $E_XCD
fi  # Doublecheck if in right directory before messing with log file.

# Far more efficient is:
#
# cd /var/log || {
#   echo "Cannot change to necessary directory." >&2
#   exit $E_XCD;
# }




tail -n $lines messages > mesg.temp # Save last section of message log file.
mv mesg.temp messages               # Rename it as system log file.


#  cat /dev/null > messages
#* No longer needed, as the above method is safer.

cat /dev/null > wtmp  #  ': > wtmp' and '> wtmp'  have the same effect.
echo "Log files cleaned up."
#  Note that there are other log files in /var/log not affected
#+ by this script.

exit 0
#  A zero return value from the script upon exit indicates success
#+ to the shell.
```

---
Since you may not wish to wipe out the entire system log, this version of the script keeps the last section of the message log intact. You will constantly discover ways of fine-tuning previously written scripts for increased effectiveness.
* * *
The _sha-bang_ ( #!) [[6]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN205) at the head of a script tells your system that this file is a set of commands to be fed to the command interpreter indicated. The #! is actually a two-byte [[7]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN214) _magic number_ , a special marker that designates a file type, or in this case an executable shell script (type `**man magic**` for more details on this fascinating topic). Immediately following the _sha-bang_ is a _path name_. This is the path to the program that interprets the commands in the script, whether it be a shell, a programming language, or a utility. This command interpreter then executes the commands in the script, starting at the top (the line following the _sha-bang_ line), and ignoring comments. [[8]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN226)
```
#!/bin/sh
#!/bin/bash
#!/usr/bin/perl
#!/usr/bin/tcl
#!/bin/sed -f
#!/bin/awk -f
```

---
Each of the above script header lines calls a different command interpreter, be it `/bin/sh`, the default shell (**bash** in a Linux system) or otherwise. [[9]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN242) Using `**#!/bin/sh**` , the default Bourne shell in most commercial variants of UNIX, makes the script [portable](https://tldp.org/LDP/abs/html/abs-guide.html#PORTABILITYISSUES) to non-Linux machines, though you [sacrifice Bash-specific features](https://tldp.org/LDP/abs/html/abs-guide.html#BINSH). The script will, however, conform to the POSIX [[10]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN256) **sh** standard.
Note that the path given at the "sha-bang" must be correct, otherwise an error message -- usually "Command not found." -- will be the only result of running the script. [[11]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN269)
#! can be omitted if the script consists only of a set of generic system commands, using no internal shell directives. The second example, above, requires the initial #!, since the variable assignment line, `**lines=50**` , uses a shell-specific construct. [[12]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN279) Note again that `**#!/bin/sh**` invokes the default shell interpreter, which defaults to `/bin/bash` on a Linux machine.
![Tip](https://tldp.org/LDP/abs/images/tip.gif) |  This tutorial encourages a modular approach to constructing a script. Make note of and collect "boilerplate" code snippets that might be useful in future scripts. Eventually you will build quite an extensive library of nifty routines. As an example, the following script prolog tests whether the script has been invoked with the correct number of parameters. | ```
E_WRONG_ARGS=85
script_parameters="-a -h -m -z"
