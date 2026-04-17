#  Chapter 8. Finding information about the system

time

If you are looking for how to change the time please refer to _date_ here: [Section 8.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DATE-TIME-CALENDARS).
_time_ is a utility to measure the amount of time it takes a program to execute. It also measures CPU usage and displays statistics.
Use _time -v_(verbose mode) to display even more detailed statistics about the particular program.
Example usage:
```
time program_name options
```

---

/proc

The files under the /proc (process information pseudo file-system) show various information about the system. Consider it a window to the information that the kernel uses.
For example:
```
cat /proc/cpuinfo
```

---
Displays information about the CPU.
```
less /proc/modules_ _
```

---
Use the above command to view information about what kernel-modules are loaded on your system.

dmesg

_dmesg_ can be used to print (or control) the “ kernel ring buffer”. _dmesg_ is generally used to print the contents of your bootup messages displayed by the kernel. This is often useful when debugging problems.
Simply type:
```
dmesg
```

---

df

Displays information about the space on mounted file-systems. Use the _-h_ option to have _df_ list the space in a 'human readable' format. ie. if there are 1024 kilobytes left (approximately) then _df_ will say there is 1MB left.
Command syntax:
```
df -options /dev/hdx
```

---
The latter part is optional, you can simply use _df_ with or without options to list space on all file-systems.

who

Displays information on which users are logged into the system including the time they logged in.
Command syntax:
```
who
```

---

w

Displays information on who is logged into the system and what they are doing (ie. the processes they are running). It's similar to _who_ but displays slightly different information.
Command syntax:
```
w
```

---

users

Very similar to _who_ except it only prints out the user names who are currently logged in. (Doesn't need or take any options).
Command syntax:
```
users
```

---

last

Displays records of when various users have logged in or out. This includes information on when the computer was rebooted.
To execute this simply type:
```
last
```

---

lastlog

Displays a list of users and what day/time they logged into the system.
Simply type:
```
lastlog
```

---

whoami

Tells the user who they are currently logged in as, this is normally the usename they logged in with but can be changed with commands like su). _whoami_ does not need or take any options.
Simply type:
```
whoami
```

---

free

Displays memory statistics (total, free, used, cached, swap). Use the _-t_ option to display totals of everything and use the _-m_ to display memory in megabytes.
Example:
```
free -tm
```

---
This will display the memory usage including totals in megabytes.

uptime

Print how long the computer has been “up”, how long the computer has been running. It also displays the number of users and the processor load (how hard the CPU has been working...).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **The w command**
---|---
| The _w_ command displays the output of the uptime command when you run this command. You could use the _w_ command instead of uptime.

uname

uname is used to print information on the system such as OS type, kernel version et cetera.
Some _uname_ options:
  * _-a_ --- print all the available information.
  * _-m_ --- print only information related to the machine itself.
  * _-n_ --- print only the machine hostname.
  * _-r_ --- print the release number of the current kernel.
  * _-s_ --- print the operating system name
  * _-p_ --- print the processor type.


Command syntax:
```
uname -options
```

---

xargs

Note that _xargs_ is an advanced, confusing, yet powerful command. _xargs_ is a command used to run other commands as many times as necessary, this way it prevents any kind of overload... When you run a command then add a _“| xargs command2_ ”. The results of command1 will be passed to command2, possibly on a line-by-line basis or something similar.
Understanding _xargs_ tends to be very difficult and my explanation is not the best. Refer to the examples below or try [6] of the [_Bibliography_](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#REFERENCES) for another _xargs_ tutorial.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Alternatives to using xargs**
---|---
|  Please note that the below explanation of _xargs_ is not the strongest (at the time of writing I could not find anything better :()). Alternatives may include writing a simple bash script to do the job which is not the most difficult task in the world.
Examples:
```
ls | xargs grep work
```

---
The first command is obvious, it will list the files in the current directory. For each line of output of _ls_ , _xargs_ will run _grep_ on that particular line and look for the string “work”. The output have the each time _grep_ is executed on a new line, the output would look like:
```
file_name: results_of_grep
```

---
If _grep_ didn't find the word then there would be no output if it had an error then it will output the error. Obviously this isn't very useful (you could just do:
```
grep 'word' *
```

---
_xargs_ also takes various options:
  * _-nx_ --- will group the first x commands together
  * _-lx_ --- xargs will execute the command for every x number of lines of input
  * _-p_ --- prompt whether or not to execute this particular string
  * _-t_ --- (tell) be verbose, echo each command before performing it
  * _-i_ --- will use substitution similar to find's -exec option, it will execute certain commands on something.


Example:
```
ls dir1 | xargs -i mv dir1/'{}' dir2/'{}'
```

---
The {} would be substituted for the current input (in this example the current file/directory) listed within the directory. The above command would move every file listed in dir1 to dir2. Obviously this command won't be too useful, it would be easier to go to dir1 and type _mv * ../dir2_
Here is a more useful example:
```
\ls *.wav | xargs -i lame -h '{}' '{}'.mp3
```

---
This would find all wave files within the current directory and convert them to mp3 files (encoded with lame) and append a “.mp3” to the end of the filename, unfortunately it doesn't remove the .wav and so its not too useful...but it works.
* * *
