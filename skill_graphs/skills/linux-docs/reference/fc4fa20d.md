#  2.5. Exercises
Most of what we learn is by making mistakes and by seeing how things can go wrong. These exercises are made to get you to read some error messages. The order in which you do these exercises is important.
Don't forget to use the Bash features on the command line: try to do the exercises typing as few characters as possible!
* * *
##  2.5.1. Connecting and disconnecting
  * Determine whether you are working in text or in graphical mode.
I am working in text/graphical mode. (cross out what's not applicable)
  * Log in with the user name and password you made for yourself during the installation.
  * Log out.
  * Log in again, using a non-existent user name
-> What happens?


* * *
##  2.5.2. Passwords
Log in again with your user name and password.
  * Change your password into _P6p3.aa!_ and hit the **Enter** key.
-> What happens?
  * Try again, this time enter a password that is ridiculously easy, like _123_ or _aaa_.
-> What happens?
  * Try again, this time don't enter a password but just hit the **Enter** key.
-> What happens?
  * Try the command **psswd** instead of **passwd**
-> What happens?


![Warning](https://tldp.org/LDP/intro-linux/images/warning.gif) | **New password**
---|---
|  Unless you change your password back again to what it was before this exercise, it will be "P6p3.aa!". Change your password after this exercise! Note that some systems might not allow to recycle passwords, i.e. restore the original one within a certain amount of time or a certain amount of password changes, or both.
* * *
##  2.5.3. Directories
These are some exercises to help you get the feel.
  * Enter the command **cd` blah`**
-> What happens?
  * Enter the command **cd`..`**
Mind the space between "cd" and ".."! Use the **pwd** command.
-> What happens?
  * List the directory contents with the **ls** command.
-> What do you see?
-> What do you think these are?
-> Check using the **pwd** command.
  * Enter the **cd** command.
-> What happens?
  * Repeat step 2 two times.
-> What happens?
  * Display the content of this directory.
  * Try the command **cd` root`**
-> What happens?
-> To which directories do you have access?
  * Repeat step 4.
Do you know another possibility to get where you are now?


* * *
##  2.5.4. Files
  * Change directory to `/` and then to `etc`. Type **ls** ; if the output is longer than your screen, make the window longer, or try **Shift** +**PageUp** and **Shift** +**PageDown**.
The file `inittab` contains the answer to the first question in this list. Try the **file** command on it.
-> The file type of my `inittab` is .....
  * Use the command **cat` inittab`** and read the file.
-> What is the default mode of your computer?
  * Return to your home directory using the **cd** command.
  * Enter the command **file`.`**
-> Does this help to find the meaning of "."?
  * Can you look at "." using the **cat** command?
  * Display help for the **cat** program, using the `--help` option. Use the option for numbering of output lines to count how many users are listed in the file `/etc/passwd`.


* * *
##  2.5.5. Getting help
  * Read **man` _intro_`**
  * Read **man` _ls_`**
  * Read **info` _passwd_`**
  * Enter the **apropos` pwd`** command.
  * Try **man** or **info** on **cd**.
-> How would you find out more about **cd**?
  * Read **ls` --help`** and try it out.


* * *
