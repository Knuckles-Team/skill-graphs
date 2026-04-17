#  1.5. Developing good scripts
##  1.5.1. Properties of good scripts
This guide is mainly about the last shell building block, scripts. Some general considerations before we continue:
  1. A script should run without errors.
  2. It should perform the task for which it is intended.
  3. Program logic is clearly defined and apparent.
  4. A script does not do unnecessary work.
  5. Scripts should be reusable.


* * *
##  1.5.2. Structure
The structure of a shell script is very flexible. Even though in Bash a lot of freedom is granted, you must ensure correct logic, flow control and efficiency so that users executing the script can do so easily and correctly.
When starting on a new script, ask yourself the following questions:
  * Will I be needing any information from the user or from the user's environment?
  * How will I store that information?
  * Are there any files that need to be created? Where and with which permissions and ownerships?
  * What commands will I use? When using the script on different systems, do all these systems have these commands in the required versions?
  * Does the user need any notifications? When and why?


* * *
##  1.5.3. Terminology
The table below gives an overview of programming terms that you need to be familiar with:
**Table 1-1. Overview of programming terms**
Term | What is it?
---|---
Command control | Testing exit status of a command in order to determine whether a portion of the program should be executed.
Conditional branch | Logical point in the program when a condition determines what happens next.
Logic flow | The overall design of the program. Determines logical sequence of tasks so that the result is successful and controlled.
Loop | Part of the program that is performed zero or more times.
User input | Information provided by an external source while the program is running, can be stored and recalled when needed.
* * *
##  1.5.4. A word on order and logic
In order to speed up the developing process, the logical order of a program should be thought over in advance. This is your first step when developing a script.
A number of methods can be used; one of the most common is working with lists. Itemizing the list of tasks involved in a program allows you to describe each process. Individual tasks can be referenced by their item number.
Using your own spoken language to pin down the tasks to be executed by your program will help you to create an understandable form of your program. Later, you can replace the everyday language statements with shell language words and constructs.
The example below shows such a logic flow design. It describes the rotation of log files. This example shows a possible repetitive loop, controlled by the number of base log files you want to rotate:
  1. Do you want to rotate logs?
    1. If yes:
      1. Enter directory name containing the logs to be rotated.
      2. Enter base name of the log file.
      3. Enter number of days logs should be kept.
      4. Make settings permanent in user's crontab file.
    2. If no, go to step 3.
  2. Do you want to rotate another set of logs?
    1. If yes: repeat step 1.
    2. If no: go to step 3.
  3. Exit


The user should provide information for the program to do something. Input from the user must be obtained and stored. The user should be notified that his crontab will change.
* * *
##  1.5.5. An example Bash script: mysystem.sh
The `mysystem.sh` script below executes some well-known commands (**date** , **w** , **uname** , **uptime**) to display information about you and your machine.
```

`tom:~>` **cat `-n` `mysystem.sh`**
     1  #!/bin/bash
     2  clear
     3  echo "This is information provided by mysystem.sh.  Program starts now."
     4
     5  echo "Hello, $USER"
     6  echo
     7
     8  echo "Today's date is `date`, this is week `date +"%V"`."
     9  echo
    10
    11  echo "These users are currently connected:"
    12  w | cut -d " " -f 1 - | grep -v USER | sort -u
    13  echo
    14
    15  echo "This is `uname -s` running on a `uname -m` processor."
    16  echo
    17
    18  echo "This is the uptime information:"
    19  uptime
    20  echo
    21
    22  echo "That's all folks!"

```

---
A script always starts with the same two characters, "#!". After that, the shell that will execute the commands following the first line is defined. This script starts with clearing the screen on line 2. Line 3 makes it print a message, informing the user about what is going to happen. Line 5 greets the user. Lines 6, 9, 13, 16 and 20 are only there for orderly output display purposes. Line 8 prints the current date and the number of the week. Line 11 is again an informative message, like lines 3, 18 and 22. Line 12 formats the output of the **w** ; line 15 shows operating system and CPU information. Line 19 gives the uptime and load information.
Both **echo** and **printf** are Bash built-in commands. The first always exits with a 0 status, and simply prints arguments followed by an end of line character on the standard output, while the latter allows for definition of a formatting string and gives a non-zero exit status code upon failure.
This is the same script using the **printf** built-in:
```

`tom:~>` **cat `mysystem.sh`**
#!/bin/bash
clear
printf "This is information provided by mysystem.sh.  Program starts now.\n"

printf "Hello, $USER.\n\n"

printf "Today's date is `date`, this is week `date +"%V"`.\n\n"

printf "These users are currently connected:\n"
w | cut -d " " -f 1 - | grep -v USER | sort -u
printf "\n"

printf "This is `uname -s` running on a `uname -m` processor.\n\n"

printf "This is the uptime information:\n"
uptime
printf "\n"

printf "That's all folks!\n"

```

---
Creating user friendly scripts by means of inserting messages is treated in [Chapter 8](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_08).
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **Standard location of the Bourne Again shell**
---|---
| This implies that the **bash** program is installed in `/bin`.
![Warning](https://tldp.org/LDP/Bash-Beginners-Guide/images/warning.gif) | **If stdout is not available**
---|---
| If you execute a script from cron, supply full path names and redirect output and errors. Since the shell runs in non-interactive mode, any errors will cause the script to exit prematurely if you don't think about this.
The following chapters will discuss the details of the above scripts.
* * *
##  1.5.6. Example init script
An init script starts system services on UNIX and Linux machines. The system log daemon, the power management daemon, the name and mail daemons are common examples. These scripts, also known as startup scripts, are stored in a specific location on your system, such as `/etc/rc.d/init.d` or `/etc/init.d`. Init, the initial process, reads its configuration files and decides which services to start or stop in each run level. A run level is a configuration of processes; each system has a single user run level, for instance, for performing administrative tasks, for which the system has to be in an unused state as much as possible, such as recovering a critical file system from a backup. Reboot and shutdown run levels are usually also configured.
The tasks to be executed upon starting a service or stopping it are listed in the startup scripts. It is one of the system administrator's tasks to configure **init** , so that services are started and stopped at the correct moment. When confronted with this task, you need a good understanding of the startup and shutdown procedures on your system. We therefore advise that you read the man pages for **init** and `inittab` before starting on your own initialization scripts.
Here is a very simple example, that will play a sound upon starting and stopping your machine:
```

#!/bin/bash

# This script is for /etc/rc.d/init.d
# Link in rc3.d/S99audio-greeting and rc0.d/K01audio-greeting

case "$1" in
'start')
  cat /usr/share/audio/at_your_service.au > /dev/audio
  ;;
'stop')
  cat /usr/share/audio/oh_no_not_again.au > /dev/audio
  ;;
esac
exit 0

```

---
The **case** statement often used in this kind of script is described in [Section 7.2.5](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_02_05).
* * *
