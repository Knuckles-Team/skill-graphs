# Trap
**CTRL**-**ALT**-**DEL**

ca::ctrlaltdel:/sbin/shutdown -t3 -r now
```

---
Note that the # means a comment (and is not used). If you simply put a # (hash) before the command it would disable it (it would become a comment).
You could also change the command it runs for example if you changed the _-r_ to a _-h_ the computer would turn off instead of rebooting, or you could have it do anything you want. It's up to your creativity to make it do something interesting.
* * *
#  9.3. Controlling Processes

ps

Will give you a list of the processes running on your system. With no options, _ps_ will list processes that belong to the current user and have a controlling terminal.
Example options include:
  * _-aux_ --- list all running processes (by all users with some information).
  * _-a_ --- list all processes from all users.
  * _-u_ --- list more information including user names, %cpu usage, and %mem usage et cetera.
  * _-x_ --- list processes without controlling terminals.
  * _-l_ --- display different information including UID and nice value.
  * _--forest_ --- this makes it easier to see the process hierarchy, which will give you an indication of how the various processes on your system interrelate (although you should also try _pstree_).


For example to list all running processes with additional information, simply type:
```
ps -aux
```

---

pstree

Displays the processes in the form of a tree structure (similar to how _tree_ does it for directories).
Use the _-p_ option to show process id's.
Example:
```
pstree -p
```

---
This would list all processes and their id's.

pgrep

This command is useful for finding the process id of a particular process when you know part of its name.
Use the _-l_ option to list the name of the process as well and the _-u_ option to search via a particular user(s).
Normally _pgrep_ will only return the pid number; this way you can use it with other commands.
Examples:
```
kill $(pgrep mozilla)
```

---
This would kill any process name that starts with mozilla. Note that this is the same as using _pkill_ (see below).
If you are unfamiliar with the _$(�)_ part of this command, please refer to [Section 6.4](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#PERFORMING-MORE-THAN-ONE-COMMAND).
To list processes id's and names type:
```
pgrep -l process_name
```

---

top

Displays the 'top' (as in CPU usage) processes, provides more detail than _ps_.
_top_ also provides an updated display, it has many options that make it fully customisable, refer to the manual or info page for details.

kill

To kill processes on your system, you will need their pid's or id's . Use _ps_ or _pstree_ to find out the process id's (pid's), or use _jobs_ to find out id's.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **killall and pkill - kill a process by name**
---|---
| _pkill_ and _killall_ can be a lot easier to use than _kill_. _pkill_ allows you to type part of the name of a process to kill it, while _killall_ requires the full process name. See below for more information.
Examples:
```
kill pid
```

---
Simply kill a process (allow it time to save it's files and exit)
```
kill %id
```

---
Same as above, except it uses an id instead of a pid, you need to use a % (percent) when using an id to kill.
```
kill -kill pid
```

---
Force a process to be killed (won't allow files to be saved or updated); only use when necessary because all data that the program had will be lost.
There are also many other kill options such as kill -HUP _..._ refer to the manual/info pages for more information.

killall

Kill a process by it's name, uses names instead of process id's (pid's). Use _-v_ to have _killall_ report whether the kill was successful or not and _-i_ for interactive mode (will prompt you before attempting to kill).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **pkill - a little like a killall with regular expressions**
---|---
| pkill is another command that allows processes to be killed but does so using regular expressions. See below for more information.
For example:
```
killall -iv mozilla
```

---
Would kill anything named “mozilla” and prompt you before each kill and report whether the kill was successful or not. Unfortunately you need to get the name exactly right for _killall_ to work, you would need to use “mozilla-bin” to kill the mozilla browser. If you want something where you don't need to know the exact name try _pkill_(below).

pkill

_pkill_ is used to kill processes according to an extended regular expression. Use the _-u_ option to kill using a user name(s) and process name (for example to only kill a process of a certain user). _pkill_ can also send specific signals to processes.
For normal usage simply type:
```
pkill process_name
```

---
Note that the “process_name” doesn't have to be an exact match...
Or to kill the “process_name” of only the users “fred” and “anon” type:
```
pkill -u fred anon process_name
```

---

skill

_skill_ is used to send a command/username/tty a particular signal.
_skill_ has a number of options available to ensure correct interpretation (otherwise it just guesses what it is), simply type _skill -option(s)_
  * _-L_ --- list the various signals that can be sent
  * _-u_ --- specify a username; this is obviously followed by the user name or a space-seperated list of usernames.
  * _-p_ --- process id (followed by the process id)
  * _-c_ --- command name (this is the same as _killall_)
  * _-t_ --- (tty number)
  * _-v_ --- verbose mode
  * _-i_ --- interactive mode.


_skill_ can be used to stop, continue, or kill processes using the username, command name or process id (or send them any variety of signals you like).
Useful example:
```
skill -STOP abusive_user_name
```

---
The above command will stop all of that users processes, this will cause his screen to freeze until you type:
```
skill -CONT abusive_user_name
```

---
This would tell that all processes may continue as before. Note that this would only work if you are root. Also note you can list more than one user name with the command so it will apply to multiple users.

**CTRL** -**C**

The break key, will kill (break, stop) something that's running on your terminal.

jobs

Prints currently running jobs, as in processes you have executed within the shell.

bg

Backgrounds a process. To start a program in the background (so it doesn't take over the terminal) use an “&” (ampersand) sign at the end of the command. You usually use **CTRL** -**Z** to suspend something you are currently using. You can simply use _bg_ to resume in the background the last job suspended...
Command syntax:
```
bg job_number
```

---
or
```
bg job_name
```

---

fg

Bring a process to the foreground, so you can interact with it. The process will use your current terminal. Note simply use _fg_ to foreground the last job number suspended...
You can bring jobs to the foreground by name or by number (use _jobs_ to find the number).
Command syntax:
```
fg job_number
```

---
or
```
fg job_name
```

---

nice

Sets the priority for a process._nice -20_ is the maximum priority (only administrative users can assign negative priorities),_nice 20_ is the minimum priority. You must be root to give a process a higher priority, but you can always lower the priority of your own processes...
Example:
```
nice -20 make
```

---
Would execute _make_ and it would run at maximum priority.

renice

Changes the priority of an existing command. You may use the options _-u_ to change the priorities of all processes for a particular user name and _-g_ to change priorities for all processes of a particular group. The default is to change via the process id number.
Example:
```
renice +20 2222
```

---
This would change the priority of process 2222 to +20 (minimum priority).

snice

_snice_ works very similarly to _skill_ , only it changes the priority of the process(es). Its function is similar to that of _renice_.
To use options (to ensure correct interpretation) you simply type _snice -option(s):_
  * _-u_ --- specify a username; this is obviously followed by the user name or a space-seperated list of usernames.
  * _-p_ --- process id (followed by the process id)
  * _-c_ --- command name (this is the same as _killall_)
  * _-t_ --- tty number
  * _-v_ --- verbose mode
  * _-i_ --- interactive mode.


Example:
```
snice -10 -u root
```

---
This would increase the priority of all root's processes.
* * *
#  9.4. Controlling services

Concept�Definitions

�
UNIX systems use scripts to control “daemons” which provide “services” (for example your sound output) to run a UNIX system. UNIX systems consist of a variety of services (daemons).
A “daemon” is a system process which runs in the background (zero interaction) performing a particular task.
Daemons normally have a “d” on the end of their name and either listen for certain events or perform a system task, for example _sshd_ listens for secure shell requests to the particular machine and handles them when they occur.
Daemons usually perform critical system tasks such as control swap-space, memory management and various other tasks.

service

_service_ is a shell script available on Mandrake/Mandriva and Redhat systems which allows you to perform various tasks on services.
  * Use the _-s_ option to print the status of all services available
  * Use the _-f_ option followed by a service name to restart that particular service.
  * Use the _-R_ option to restart all services (note that this will kill any current services running, including the X windows system).


For example to restart the daemon _sshd_ you would type:
```
service -f sshd
```

---

Using�the�script�directly

You may also execute the shell script directly from _/etc/init.d_. Simply go to that directory then type _./script_name_.
Executing the script should return the options it can take, by default they will be:
  * restart --- this will make the service stop and then start again.
  * start --- this option will start a service (assuming its not running).
  * stop --- this option will stop a service (assuming its running).
  * status --- this option will tell you about the service


* * *
#  Chapter 10. Managing users

su�username

(Switch User), change to a different user.
Use _su�-_ to switch to root or _su username_ , to switch to a different username.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Using sudo**
---|---
|  Its often considered better practice to use the _sudo_ command rather than switch to the root user The _sudo_ command allows you to perform actions as root but logs the actions you take (so you can trace anything that was done to the system by yourself or others). _sudo_ has a very good manual page which provides plenty of information about it. You use sudo similar to how you execute a normal command with sudo prepended to it, for example: | ```
 sudo rpm -U myrpm.i386.rpm
```

---
This would allow you to install a rpm even if you have the correct sudo access
Note that if you want to return to your original user you don't use _su_ again, type _exit_ or press **CTRL** -**D** .
Simply typing _su_ will give you some root privileges, but there are minor complications relating to environment variables. It's generally considered better practice to use _su�-_ because it has no restrictions.

root

The superuser. This user has power over everything and all, and can do anything with the system (including destroy it, and of course fix it :)). This user is used to perform most administration functions on the system.
* * *
