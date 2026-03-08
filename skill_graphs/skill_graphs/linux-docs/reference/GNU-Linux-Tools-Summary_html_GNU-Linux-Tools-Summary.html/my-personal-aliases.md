# my personal aliases
alias cp='cp -vi' #to prompt when copying if you want to overwrite and will tell you where information is going
alias rm='rm -i' #Prompts you if you really want to remove it.
alias mv='mv -i' #Prompts you if you are going to overwrite something
```

---
On any Mandriva GNU/Linux system the global aliases (for all users) are all in /etc/profile.d/alias.sh. The above listed commands already have aliases, as well as several other commonly used commands.

set�-x

_set_ is one of bash's inbuilt commands, try looking in the bash manual for its many usage options.
Using _set_ with the _-x_ option will make bash print out each command it is going to run before it runs it.
This can be useful to find out what is happening with certain commands such as things being quoted that contain wildcards or special symbols that could cause problems, or complex aliases. Use _set +x_ to turn this back off.
Examples
After using _set -x_ you can run the command:
```
ls
```

---
The output printed before the command runs (for example):
```
+ ls -F --color=auto
```

---
Which means that the command is really an alias to run _ls_ with the _-F_ and _--color=auto_ options. Use a “\” (backslash) before the command to run it without the alias.

\�(backslash)

The backslash escape character can be used before a shell command to override any aliases.
For example if _rm_ was made into an alias for _rm -i_ then typing “rm” would actually run _rm -i_.
However, typing _\rm_ lets the shell ignore the alias and just run _rm_ (its runs exactly what you type), this way it won't confirm if you want to delete things.
![Caution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/caution.gif) | **Using rm**
---|---
|  Please note that the alias for the remove command is there for a reason. Using it incorrectly could remove files which you don't want removed. Only use _\rm_ if you know exactly what you are doing (recovering files is not easy, _rm_ does not send things to a recycle bin).
The “\” character can be used before special characters (such as a space or a wildcard), to stop bash from trying to expand them. You can make a directory name with a space in it using a backslash before the space. For example you could type _cd_ _My_ \_Directory_ \_With_ \_Spaces_ which normally wouldn't work.
The “\” character can also be used to stop bash from expanding certain symbols (as an alternative you could use single quotation marks, although you may need to use both).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **The TAB Key**
---|---
| Please note that using the TAB key (automatic-command-completion) will automatically use escapes for spaces (so you don't have to type them manually).

script

The “ _script_ ” command creates a typescript, or "capture log" of a shell session - it writes a copy of your session to a file, including commands you type and their output.

~�(tilde�character)

The tilde character is used as an alias to a users home directory.
For example, if your user-name was “fred”, instead of typing _cd /home/fred_ you could simply type _cd ~._ Or to get to fred's tmp directory (under his home directory) you could type _cd ~/tmp._
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Home directory shortcut**
---|---
| ~ (tilde) can also be used as a shortcut to other users home directories, simply type: _~user_name_ and it will take you to the users home directory. Note that you need to spell the username exactly correct, no wildcards.
�

set�bell-style�none

This particular _set_ command will turn off the system bell from the command-line (use xset -b for X windows). If you want the bell to stay off pernamently (no audible bell) then you can add this command to your “.bashrc” or “.bash_profile” (just add it to the same one you have your aliases in...).

reset

The _reset_ command re-initializes your current terminal. This can be useful when the text from your terminal becomes garbled, simply type “reset” and this will fix your terminal.

exit

Closes your current terminal (with x-terminals) or logs-out. Also try **CTRL** -**D** .

logout

Logs out of a terminal, also try **CTRL** -**D** .

echo

A little command that repeats anything you type.
Example:
```
echo “hello world”
```

---
Simply displays “ hello world”.
Example:
```
echo rm -R *
```

---
This will output what will be passed to the _rm_ command (and therefore what would be deleted), putting echo before a command renders it harmless (it just expands wildcards so you know what it will do).
Also try using the _-e_ option with echo. This will allow you to use the escape character sequences to format the output of a line. Such as '\t' for tab, '\n' for newline etc.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Using echo to prevent accidents**
---|---
|  Typing: _echo command(s)_ could Using _echo_ allows you to expand the wildcards to understand what will happen before you actually run the command.
* * *
#  4.2. The command-line history

Using�the�command�history

Use the up and down key's to scroll through previously typed commands. Press [Enter] to execute them or use the left and right arrow keys to edit the command first. Also see _history_ (below).

The�history�command

The _history_ command can be used to list Bash's log of the commands you have typed:
This log is called the “history”. To access it type:
```
history n
```

---
This will only list the last _n_ commands. Type “history” (without options) to see the the entire history list.
You can also type _!n_ to execute command number n. Use _!!_ to execute the last command you typed.
_!-n_ will execute the command n times before (in other words _!-1_ is equivalent to _!!_).
_!string_ will execute the last command starting with that “string” and _!?string?_ will execute the last command containing the word “string”. For example:
```
!cd
```

---
Will re-run the command that you last typed starting with “cd”.
_“ commandName !*”_ will execute the “commandName” with any arguments you used on your last command. This maybe useful if you make a spelling mistake, for example. If you typed:
```
emacs /home/fred/mywork.java /tmp/testme.java
```

---
In an attempt to execute emacs on the above two files this will obviously fail. So what you can do is type:
```
emacs !*
```

---
This will execute emacs with the arguments that you last typed on the command-line. In other words this is equivalent to typing:
```
emacs /home/fred/mywork.java /tmp/testme.java
```

---

Searching�through�the�Command�History�( **CTRL** -**R** )

Use the CTRL-R key to perform a “reverse-i-search”. For example, if you wanted to use the command you used the last time you used _snort_ , you would type:
**CTRL** -**R** then type “snort”.
What you will see in the console window is:
```
(reverse-i-search)`':
```

---
After you have typed what you are looking for, use the **CTRL** -**R** key combination to scroll backward through the history.
Use **CTRL** -**R** repeatedly to find every reference to the string you've entered. Once you've found the command you're looking for, use [Enter] to execute it.
Alternatively, using the right or left arrow keys will place the command on an actual command-line so you can edit it.
* * *
#  4.3. Other Key combinations
GNU/Linux shells have many shortcut keys which you can use to speed up your work, below is a rough list of some (also see **CTRL** -**R** in the history section of the commands, over here, [Section 4.2](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#THE-COMMAND-LINE-HISTORY)).

**CTRL** -**D**

the “end-of-file” (EOF) key combination can be used to quickly log out of any terminal. **CTRL** -**D** is also used in programs such as _“at”_ to signal that you have finished typing your commands (the EOF command).

**CTRL** -**Z**

key combination is used to stop a process. It can be used to put something in the background temporarily.
For example, if you were editing a file with _vim_ or _emacs_ just press **CTRL** -**Z** to regain control of the terminal do what you want and then type _fg_
For further information please see [Section 9.3](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONTROLLING-PROCESSES).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **If _fg_ doesn't work**
---|---
| If _fg_ doesn't work you may need to type _jobs_ and then _fg job_name or fg job_number_

**CTRL** -**A** �and� **CTRL** -**E**

These key combinations are used for going to the start and end of the line on the command line. Use **CTRL** -**A** to jump to the start of the line, and **CTRL** -**E** to jump to the end of the line.

**CTRL** -**K**

This key combination can be used to cut or delete what is currently in front of the cursor.

**CTRL** -**Y**

This key combination can be used to paste the last thing you deleted (using **CTRL** -**K** or **CTRL** -**W** ).

**CTRL** -**W**

This key combination can be used to cut or delete the entire line that has being typed.
* * *
#  4.4. Virtual Terminals and screen
Using the key combination **ALT** -**F*** keys you may change to different virtual terminals. You will have several (usually 6) virtual terminals setup with shells. Number 7 is usually setup with X you need to use **CTRL** -**ALT** -**F*** to change to a terminal from within X (X as in the X windowing system).

screen

is a great program that allows you to switch between multiple virtual terminals on the one physical terminal that you are using. Its a command-line based window manager, clearly this isn't that useful if you do have virtual terminals, but its amazingly useful when you log into machines remotely, using ssh and similar, see [Section 13.3](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#REMOTE-ADMINISTRATION). It works on key-combinations, you type
```
screen
```

---
On the command-line to begin. Now you start with one virtual terminal by default, but using the key combination **CTRL** -**A** and then hitting "C" you can create another virtual terminal to use.
Use **CTRL** -**N** to go to the next virtual terminal and **CTRL** -**P** to go to the previous virtual terminal. Also try hitting **CTRL** -**A** to go backwards and forwards between two particular terminals.
_screen_ also has various other abilities that you can test out. The documentation and guides are well written so please feel free to read the manual page or try searching the internet.
* * *
#  Chapter 5. Help
The help chapter provides information on how you may access the documentation of the GNU/Linux system. There is normally a document describing every single tool you have installed, even if its only brief...

man

This command displays summary information on a program from an online manual. For example typing _man man_ will bring up the manual page for man (the manual page viewer). Note: q is the quit key.
Command syntax:
```
man program_name
```

---
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Also try**
---|---
|  Specifying the section of the manual page, sometimes the man page is different for the same tool in different sections, note sections are numbered 1 to 9. Use apropos to find which section number to look in. The syntax to look at a different section is:  | ```
man section_number tool_name
```

---
For example: ```
man 2 time
```

---
This will show you the man page called time in section 2, the equivalent page in section 1 is completely different

man�-K�keyword

Search the manual pages for a string, as in it will search all manual pages for a particular string within each individual man page, it will then prompt whether you would like to view each page it will find. Use double quotes “ and ” if there are spaces in the string you are typing.
![Caution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/caution.gif) | **Speed issue**
---|---
|  Please be warned that this method is going to be really, really slow. You are searching *all* man pages for a string

man�-f�command

This will list details associated with the command. The root user must run _makewhatis_ (see below) before this command will work.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Equivalent to _whatis_**
---|---
|  This command is the same as running _whatis_

info

Provides a more detailed hyper-text manual on a particular command, this only works for some commands.
Command syntax:
```
info program_name
```

---

whatis

Displays a one-line description of what a program does. The string needs to be an exact match, otherwise _whatis_ won't output anything. Relies on the whatis database (see below).
Command syntax:
```
whatis program_name
```

---

makewhatis

Make the whatis database for _apropos_ , _whatis_ and _man -f._
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Root Privileges**
---|---
| This takes some time and you require root privileges to do this.

apropos

Searches the whatis database for strings, similar to _whatis_ except it finds and prints anything matching the string (or any part of the string). Also relies on the whatis database (see above).
Command syntax:
```
apropos string
```

---
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Equivalent to...**
---|---
|  _apropos_ is the same as doing _man -k_ (lowercase k).
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Please note**
---|---
| You need to run _makewhatis_ (as root) so _whatis_ , _man -f_ and _apropos_ will work.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Also try**
---|---
| Using a program with the _-?_ , _--h_ , _--help_ , and the _-h_ options, they will display very short summary information on the command usage options.
* * *
#  Chapter 6. Directing Input/Output
The directing input/output chapter explains how you can use a program and send its output to a file or to another command that you wish to use. This technique is very powerful and there are a number of ways of doing this.
* * *
#  6.1. Concept Definitions
All three of the following definitions are called “ File Streams.” They hold information that is either received from somewhere or sent to somewhere. In a UNIX system, the keyboard input (standard input), information printed to the screen (standard output) and error output (also printed to the screen) are treated as separate File Streams.

Standard�output

Standard output is the output from the program printed to the screen, not including error output (see below).

Standard�input

Standard input is the input from the user. Normally the keyboard is used as the standard input device in a UNIX system.

Standard�error

Standard error is error output from programs. This output is also sent to the screen and will normally be seen mixed in with standard output. The difference between standard output and standard error is that standard error is unbuffered (it appears immediately on the screen) and standard error is only printed when something goes wrong (it will give you details of what went wrong).
* * *
#  6.2. Usage

>

The greater than symbol is used to send information somewhere (for example a text file)
Example:
```
cat file1 file2 > file1_and_2.txt
```

---
This will concatenate the files together into one big file named “file1_and_2.txt”. Note that this will overwrite any existing file.

<

The less than symbol will insert information from somewhere (a text file) as if you typed it yourself. Often used with commands that are designed to get information from standard input only.
For example (using tr):
```
tr '[A-Z]' '[a-z]' < fileName.txt > fileNameNew.txt
```

---
The example above would insert the contents of “fileName.txt” into the input of _tr_ and output the results to “fileNameNew.txt”.

>>

The >> symbol appends (adds) information to the end of a file or creates one if the file doesn't exist.

<<

The << symbol is sometimes used with commands that use standard input to take information. You simply type _< < word_ (where word can be any string) at the end of the command. However its main use is in shell scripting.
The command takes your input until you type “word”, which causes the command to terminate and process the input.
Using << is similar to using **CTRL** -**D** (EOF key)_,_ except it uses a string to perform the end-of-file function. This design allows it to be used in shell scripts.
For example type "cat" (with no options...) and it will work on standard input.
To stop entering standard input you would normally hit **CTRL** -**D** .
As an alternative you can type "cat << FINISHED", then type what you want.
When you are finished, instead of hitting **CTRL** -**D** you could type "FINISHED" and it will end (the word FINISHED will not be recorded).

2>

Redirects error output. For example, to redirect the error output to /dev/null, so you do not see it, simply append this to the end of another command...
For example:
```
make some_file 2> /dev/null
```

---
This will run make on a file and send all error output to /dev/null

|

The “pipe” command allows the output of one command to be sent to the input of another.
For example:
```
cat file1.txt file2.txt | less
```

---
Concatenates the files together, then runs _less_ on them. If you are only going to look at a single file, you would simply use _less_ on the file...

tee

Sends output of a program to a file and to standard output. Think of it as a T intersection...it goes two ways.
For example:
```
ls /home/user | tee my_directories.txt
```

---
Lists the files (displays the output on the screen) and sends the output to a file: “my_directories.txt”.

&>

Redirects standard output and error output to a specific location.
For example:
```
make &> /dev/null
```

---
Sends both error output and standard output to /dev/null so you won't see anything...
* * *
#  6.3. Command Substitution
Command substitution is basically another way to do a pipe, you can use pipes and command substitution interchangeably, it's up to you which one you find easier...
Command substitution can be done in two distinct ways.
�

Method�One�(back-quotes)

�
Simply type:
```
command_1 `command_2 -options`
```

---
This will execute “command_2” and it's output will become the input to “command_1”.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Backquote key**
---|---
| The back-quote key is usually located at the same place as the tilde, above the [Tab] key.

Method�Two�(dollars�sign)

�
Simply type:
```
command_1 $(command_2)
```

---
This will execute “command_2” and it's output will become the input to “command_1”.

Using�the�pipe�instead

�
You can of course use pipes to do the same thing, if you don't know what a pipe is, please see [Section 6.2](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#USAGE-INPUT-OUTPUT). For example instead of doing:
```
less $cat file1.txt file2.txt
```

---
You could do:
```
cat file1.txt file2.txt | less
```

---
And end up with exactly the same result, it's up to you which way you find easier.
* * *
#  6.4. Performing more than one command

Executing�the�second�command�only�if�the�first�is�successful

�
To do this you would type:
```
command1 && command2
```

---
command2 will be executed if command1 successfully completes (if command1 fails command2 won't be run). This is called a logical AND.

Executing�the�second�command�only�if�the�first�fails

�
To do this you would type:
```
command1 || command2
```

---
command2 will be executed if command1 does not successfully complete (if command1 is successful command2 won't be run). This is called a logical OR.

Executing�commands�sequentially

�
To execute commands sequentially regardless of the success/failure of the previous you simply type:
```
command1; command2
```

---
command2 will execute once command1 has completed.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **More than two commands**
---|---
| You can continue to use ';' (semicolon) characters to do more and more commands on the one line.
* * *
#  Chapter 7. Working with the file-system
The working with the file-system chapter explains a number of commands that you use to move around the file system hierarchy and manipulate the files. Also explained are finding files and how to mass-rename files.
* * *
#  7.1. Moving around the filesystem

cd

Change directory. Use _“ cd ..”_ to go up one directory.
One dot '.' represents the current directory while two dots '..' represent the parent directory.
_“ cd -”_ will return you to the previous directory (a bit like an “undo”).
You can also use _cd absolute�path_ or _cd relative�path_ (see below):

Absolute�paths

An “ absolute path” is easily recognised from the leading forward slash, /. The / means that you start at the top level directory and continue down.
For example to get to /boot/grub
```
cd /boot/grub
```

---
This is an absolute path because you start at the top of the hierarchy and go downwards from there (it doesn't matter where in the filesystem you were when you typed the command).

Relative�paths

A “ relative path” doesn't have a preceding slash. Use a relative path when you start from a directory below the top level directory structure. This is dependent on where you are in the filesystem.
For example
```
cd music
```

---
Please note that there is no / using the above _cd_ command. Using a / would cause this to be an absolute path, working from the top of the hierarchy downward.

ls

List files and directories. Typing “ls” will list files and directories, but will not list hidden files or directories that start with a leading full stop “.”.
Example options:
  * _ls -l_ --- long style, this lists permissions, file size, modification date, ownership.
  * _ls -a_ --- this means "show all", this shows hidden files, by default any file or directory starting with a '.' will not be shown.
  * _ls -d_ --- list directory entries rather than contents (see example below)
  * _ls -F_ --- append symbols to particular files, such as * (asterisk) for executable files.
  * _ls -S_ --- sort the output of the command in descending order sorted by size.
  * _ls -R_ --- (recursive) to list everything in the directories below as well as the current directory.


Command syntax, either:
```
ls -options
```

---
This simply lists everything in the current directory, the options are not required (options such as _-l_ , _-a_ et cetera).
```
ls -options string
```

---
This lists files using a certain string. The string can contain standard wildcards to list multiple files, to learn more about standard wildcards please read [Section 20.4.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#STANDARD-WILDCARDS)
You can use _ls -d_ to show directories that match an exact string, or use standard wildcards. Type “ ls -d */” to list all subdirectories of the current directory. Depending on the setup of your aliases (see [Chapter 4](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SHELL-TIPS)) you may simply be able to type _lsd_ as the equivalent to _ls -d */_.
Examples for _ls -d_ :
```
ls -d_ _*/
```

---
Lists all subdirectories of current directory.
```
ls -d string*
```

---
Lists directories that start with "string".
```
ls -d /usr/*/*/doc
```

---
Lists all directories that are two levels below the /usr/ directory and have a directory called “doc”, this trick can come in quite handy sometimes.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **You can also use**
---|---
| Depending on how your aliases (see [Chapter 4](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SHELL-TIPS)) are setup you can also use _l_ , _la_ (list all) and _ll_ (list long) to perform the above commands

pwd

Print working directory. Print the absolute (complete) path to the directory the user is currently in.
Command syntax:
```
pwd
```

---
This will tell you the full path to the directory you are in, for example it may output “/usr/local/bin” if you are currently in that directory.

tree

Outputs an ASCII text tree/graph starting at a given directory (by default the current directory). This command recursively lists all files and all directories.
In other words, it will list files within the directories below the current one, as well as all files in the current directory.
_tree_ has a large number of options, refer to the manual page for details.
Command syntax:
```
tree
```

---
or
```
tree -option(s) /optional/directory/to/list
```

---
* * *
##  7.1.1. Finding files

find

_find_ is a tool which looks for files on a filesystem. _find_ has a large number of options which can be used to customise the search (refer to the manual/info pages).
Note that find works with standard wildcards,[Section 20.4.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#STANDARD-WILDCARDS), and can work with regular expressions, [Section 20.4.2](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#REGULAR-EXPRESSIONS).
Basic example:
```
find / -name file
```

---
This would look for a file named “file” and start at the root directory (it will search all directories including those that are mounted filesystems).
The _`-name'_ option is case sensitive you can use the _`-iname'_ option to find something regardless of case.
Use the _'-regex'_ and _'-iregex'_ to find something according to a regular expression (either case sensitive or case insensitive respectively).
The _'-exec'_ option is one of the more advanced find operations. It executes a command on the files it finds (such as moving or removing it or anything else...).
To use the _-exec_ option: use find to find something, then add the _-exec_ option to the end, then:
```
command_to_be_executed ![\(1\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/1.gif)  then '{}'_ _(curly brackets) ![\(2\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/2.gif) then the arguments (for example a new directory)  and finally a ';' ![\(3\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/3.gif).
```

---
See below for an example of use this command.

[![\(1\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/1.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#COMMAND)
     This is the tool you want to execute on the files find locates. For example if you wanted to remove everything it finds then you would use _-exec rm -f_

[![\(2\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/2.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#BRACKETS)
     The curly brackets are used in find to represent the current file which has been found. ie. If it found the file shopping.doc then {} would be substituted with shopping.doc. It would then continue to substitute {} for each file it finds. The brackets are normally protected by backslashes (\\) or single-quotation marks ('), to stop bash expanding them (trying to interpret them as a special command eg. a wildcard).

[![\(3\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/3.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#END)
     This is the symbol used by find to signal the end of the commands. It's usually protected by a backslash (\\) or quotes to stop bash from trying to expand it.
```
find / -name '*.doc' -exec cp '{}' /tmp/ ';'
```

---
The above command would find any files with the extension '.doc' and copy them to your /tmp directory, obviously this command is quite useless, it's just an example of what find can do. Note that the quotation marks are there to stop bash from trying to interpret the other characters as something.
Excluding particular folders with _find_ can be quite confusing, but it may be necessary if you want to search your main disk (without searching every mounted filesystem). Use the _-path_ option to exclude the particular folder (note, you cannot have a '/' (forward slash) on the end) and the _-prune_ option to exclude the subdirectories. An example is below:
```
find / -path '/mnt/win_c' -prune -o -name "string" -print
```

---
This example will search your entire directory tree (everything that is mounted under it) excluding /mnt/win_c and all of the subdirectories under /mnt/win_c. When using the _-path_ option you can use wildcards.
Note that you could add more _-path '/directory'_ statements on if you wanted.
_find_ has many, many different options, refer to the manual (and info) page for more details.

slocate

_slocate_ outputs a list of all files on the system that match the pattern, giving their full path name (it doesn't have to be an exact match, anything which contains the word is shown).
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Replaces _locate_**
---|---
| Secure locate is a replacement for _locate_ , both have identical syntax. On most distributions locate is an alias to _slocate_.
Command syntax:
```
slocate string
```

---
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **This won't work unless**
---|---
| You need to run either _updatedb_ (as root) or _slocate -u_(as root) for slocate to work.

whereis

whereis locates the binary, source, and manual page for a particular program, it uses exact matches only, if you only know part of the name use _slocate_.
Command syntax:
```
whereis program_name
```

---

which

Virtually the same as whereis, except it only finds the executable (the physical program). It only looks in the PATH (environment variable) of a users shell.
Use the _-a_ option to list all occurrences of the particular program_name in your path (so if there's more than one you can see it).
Command syntax:
```
which program_name
```

---
* * *
#  7.2. Working with files and folders

mkdir

Make a directory. Use _mkdir -p_ to create subdirectories automatically.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Directories are Folders**
---|---
| Directories are sometimes called folders in other operating systems (such as Microsoft Windows)
Examples:
```
mkdir -p /home/matt/work/maths
```

---
This would create the directories “work” and “maths” under matt's home directory (if matt's home directory didn't exist it would create that too).
```
mkdir foo
```

---
This would create a directory in the current path named “foo”.

rm

Remove/delete a file(s) or directories(s). You can use standard wildcards with this command [Section 20.4.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#STANDARD-WILDCARDS).
Command syntax:
```
rm -options file_or_folder
```

---
You can of course use standard wildcards to delete multiple files or multiple directories and files.
Use the _-R_ or _-r_ option to remove recursively, this removes everything within subdirectories. Also try the _-f_ option to force removal (useful when you don't want to be prompted).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Disabling Aliases (per execution)**
---|---
| On some systems such as Mandrake an alias will send _rm_ to _rm -i_ (prompting you for every file you wish to delete). To override this use: _\rm -R directory_(using the \ disables the alias for this run only)

rmdir

Remove an empty directory. If you want to remove a directory with files in it type “ rm -R directory”, read above for information on _rm -R_
Command syntax:
```
rmdir directory
```

---
This will only remove directory if it's empty otherwise it will exit with an error message.

mv

Move a file or a directory to a new location or rename a file/directory.
Rename example:
```
mv filename1 filename2
```

---
Renames filename1 to filename2.
To move a file or directory, simply type:
```
mv original_file_or_folder new_location
```

---
Note that this command can use standard wildcards [Section 20.4.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#STANDARD-WILDCARDS) to move files (not for renaming).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Move and rename**
---|---
|  Note that you can also move and rename a file in a single command. The difference is with the destination (right hand side) you change the filename to the new name of the file. For example typing: | ```
mv /etc/configuration.txt /home/joe/backupconfig
```

---
This would move the file "configuration.txt" to /home/joe/ and rename it "backupconfig"

cp

Copy a file. Has a number of useful options, such as _-R_(or _-r_) which recursively copies directories and subdirectories.
Command syntax:
```
cp -options file_or_files new_location
```

---
Examples:
```
cp file1 file2
```

---
Simply copy file1 to file2 (in the same directory).
```
cp /tmp/file1 ~/file2 /mnt/win_c
```

---
Where the last option is the directory to be copied to. The above example copies two files from different areas of the file system to /mnt/win_c
```
cp -R directory_and_or_files new_location
```

---
This command will copy directories (and all subdirectories) and/or files t _o new_location_
Note that this command can use standard wildcards [Section 20.4.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#STANDARD-WILDCARDS) to copy multiple files.
You may also like to try the “-u” when moving large directories around, this copies only if the source file is newer than the destination to where you are copying to, or if the destination file does not exist at all.

ln

Create a link to a file. There are two types of links:

Hard�links

Hard links are considered pointers to a file (the number is listed by typing _ls -l_)
The file itself only goes away when all hard-links are deleted. If you delete the original file and there are hard links to it the original file will remain.
Example:
```
ln target_name link_name
```

---
Will create a “hard link” to target_name called link_name, you need to delete both of these to remove the file.

Symbolic�links

Symbolic links are created by typing “ln -s”.
The advantage of symbolic links is that the target can be to something on another file-system, while hard-links can only exist on the same file-system.
For example:
```
ln -s target_name link_name
```

---
This creates a symbolic link to “target_name” called “link_name”, if you delete the original file the symbolic link won't work (it becomes a broken link).

shred

Securely remove a file by overwriting it first. Prevents the data from being recovered by software (and even by most hardware), please be very careful when using shred as you may never be able to retrieve the data you have run the application on.
For example:
```
shred -n 2 -z -v /dev/hda1
```

---
> “What this tells shred, is to overwrite the partition 2 times with random data (- n 2) then finish it up by writing over it with zeroes (-z) and show you its progress (-v). Of course, change /dev/hda1 to the correct partition . Each pass can take some time, which is why I set it to only do 2 random passes instead of the default 25. You can adjust this number, of course, to your particular level of paranoia and the amount of time you have.
> Since shred writes on such a low-level, it doesn't actually matter what kind of filesystem is on the partition--everything will be unrecoverable. Once shred is finished, you can shutdown the machine and sell or throw away the drive with peace of mind.
> ...However, even shre dding devices is not always completely reliable. For example, most disks map out bad sectors invisibly to the application; if the bad sectors contain sensitive data, `shred' won't be able to destroy it. [ shred info page ].”[[2]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN3712)
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Shredding files doesn't work with all filesystems**
---|---
| Please note that as mentioned in the shred manual page (please see the manual and preferably info pages for more information). _shred_ does not work correctly
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Alternatives to using shred**
---|---
|  shred has its disadvantages when run on a filesystem. First of all since it has to be installed you cannot run shred on your operating systems filesystem, you also cannot use shred on a windows machine easily since you cannot install _shred_ on this machine. You may like to try alternatives such as the DBAN project that create self-booting floppy disks that can completely erase a machines hard disk.
You may also like to see how _chattr_ can assist you in shredding files once they are removed (it has similar problems to shred, only ext2 and ext3 style filesystems...), please see [Section 14.2](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FILE-PERMISSIONS).

du

Displays information about file size. Use _du filename_ to display the size of a particular file. If you use it on directories it will display the information on the size of the files in the directory and each subdirectory.
Options for du (use _du -option(s)_):
  * _-c_ -- this will make _du_ print a grand total after all arguments have being processed.
  * _-s_ -- summarises for each argument (prints the total).
  * _-h_ -- prints things in “ human readable” mode; for example printing 1M (megabyte) rather than 1,024,000 (bytes).


Using the _-hs_ options on a directory will display the total size of the directory and all subdirectories.
Command syntax:
```
du -options file_directory_or_files
```

---
Example:
```
du -hs *
```

---
This command will list the size of all files in the current directory and it will list the size of subdirectories, it will list things in human-readable sizes using 1024 Kb is a Megabyte, M for megabyte, K for kilobyte etc.

file

Attempts to find out what type of file it is, for example it may say it's: binary, an image file (well it will say jpeg, bmp et cetera), ASCII text, C header file and many other kinds of files, it's a very useful utility.
Command syntax:
```
file file_name
```

---

stat

Tells you detailed information about a file, including inode number creation/access date. Also has many advanced options and uses.
For simple use type:
```
stat file
```

---

dd

Copies data on a very low level and can be used to create copies of disks [Section 20.3](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DUPLICATING-DISKS) and many other things (for example CD image files).
_dd_ can also perform conversions on files and vary the block size used when writing the file.
Command syntax, note the block size and count are optional and you can use files instead of devices...
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Please note**
---|---
| _dd_ is an advanced and difficult to use command. Its also very powerful, so be careful what you do with it
Command syntax:
```
dd if=/dev/xxx of=/dev/xxx bs=xxxx count=x
```

---
![Warning](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/warning.gif) | **Warning**
---|---
| The command _dd_ is used to work on a very low level. It can be used to overwrite important information such as your master-boot record or various important sections of your hard-disk. Please be careful when using it (especially when working with devices instead of files).

touch

This command is used to create empty files, simply do _touch file_name_. It is also used to update the timestamps on files.
_touch_ can be used to change the time and/or date of a file:
```
touch -t 05070915 my_report.txt[[3]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN3941)
```

---
This command would change the timestamp on my_report.txt so that it would look like you created it at 9:15. The first four digits stand for May 7th (0507), in MM-DD (American style), and the last four (0915) the time, 9:15 in the morning.
Instead of using plain numbers to change the time, you can use options similar to that of the _date_ tool. For example:
```
touch -d '5 May 2000' some_file.txt
```

---
You can also use _--date=_ instead of _-d._ Also have a look at the date command under [Section 8.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DATE-TIME-CALENDARS) for examples on using _-d_ and _--date=_ (the syntax for the date part is exactly the same when using _-d_ or _--date_).

split

Splits files into several smaller files.
Use the _-b�xx_ option to split into _xx_ bytes, also try _-k_ for kilobytes, and _-m_ for megabytes. You can use it to split text files and any other files... you can use _cat_ to re-combine the files.
This may be useful if you have to transfer something to floppy disks or you wish to divide text files into certain sizes.
Command syntax:
```
split -options file
```

---
This will split the input file into 1000 lines of input each (that's the default...), and output (using the above example), with the input name file, “fileaa” (1st part of file), “fileab” (2nd part of file), “fileac” (3rd part of file) etc. until the there is no more of the file left to split.
* * *
