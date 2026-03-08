# This script can clean up files that were last accessed over 365 days ago.

USAGE="Usage: $0 dir1 dir2 dir3 ... dirN"

if [ "$#" == "0" ]; then
	echo "$USAGE"
	exit 1
fi

while (( "$#" )); do

if [[ $(ls "$1") == "" ]]; then
	echo "Empty directory, nothing to be done."
  else
	find "$1" -type f -a -atime +365 -exec rm -i {} \;
fi

shift

done

```

---
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **-exec vs. xargs**
---|---
|  The above **find** command can be replaced with the following: **find` options` | xargs [commands_to_execute_on_found_files]** The **xargs** command builds and executes command lines from standard input. This has the advantage that the command line is filled until the system limit is reached. Only then will the command to execute be called, in the above example this would be **rm**. If there are more arguments, a new command line will be used, until that one is full or until there are no more arguments. The same thing using **find` -exec`** calls on the command to execute on the found files every time a file is found. Thus, using **xargs** greatly speeds up your scripts and the performance of your machine.
In the next example, we modified the script from [Section 8.2.4.4](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_08_02_04_04) so that it accepts multiple packages to install at once:
```

#!/bin/bash
if [ $# -lt 1 ]; then
        echo "Usage: $0 package(s)"
        exit 1
fi
while (($#)); do
	yum install "$1" << CONFIRM
y
CONFIRM
shift
done

```

---
* * *
#  9.8. Summary
In this chapter, we discussed how repetitive commands can be incorporated in loop constructs. Most common loops are built using the **for** , **while** or **until** statements, or a combination of these commands. The **for** loop executes a task a defined number of times. If you don't know how many times a command should execute, use either **until** or **while** to specify when the loop should end.
Loops can be interrupted or reiterated using the **break** and **continue** statements.
A file can be used as input for a loop using the input redirection operator, loops can also read output from commands that is fed into the loop using a pipe.
The **select** construct is used for printing menus in interactive scripts. Looping through the command line arguments to a script can be done using the **shift** statement.
* * *
#  9.9. Exercises
Remember: when building scripts, work in steps and test each step before incorporating it in your script.
  1. Create a script that will take a (recursive) copy of files in `/etc` so that a beginning system administrator can edit files without fear.
  2. Write a script that takes exactly one argument, a directory name. If the number of arguments is more or less than one, print a usage message. If the argument is not a directory, print another message. For the given directory, print the five biggest files and the five files that were most recently modified.
  3. Can you explain why it is so important to put the variables in between double quotes in the example from [Section 9.4.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_04_02)?
  4. Write a script similar to the one in [Section 9.5.1](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_05_01), but think of a way of quitting after the user has executed 3 loops.
  5. Think of a better solution than **move` -b`** for the script from [Section 9.5.3](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_05_03) to prevent overwriting of existing files. For instance, test whether or not a file exists. Don't do unnecessary work!
  6. Rewrite the `whichdaemon.sh` script from [Section 7.2.4](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_02_04), so that it:
     * Prints a list of servers to check, such as Apache, the SSH server, the NTP daemon, a name daemon, a power management daemon, and so on.
     * For each choice the user can make, print some sensible information, like the name of the web server, NTP trace information, and so on.
     * Optionally, build in a possibility for users to check other servers than the ones listed. For such cases, check that at least the given process is running.
     * Review the script from [Section 9.2.2.4](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_02_02_04). Note how character input other than **q** is processed. Rebuild this script so that it prints a message if characters are given as input.


* * *
#  Chapter 10. More on variables
> In this chapter, we will discuss the advanced use of variables and arguments. Upon completion, you will be able to:
>   * Declare and use an array of variables
>   * Specify the sort of variable you want to use
>   * Make variables read-only
>   * Use **set** to assign a value to a variable
>

* * *
#  10.1. Types of variables
##  10.1.1. General assignment of values
As we already saw, Bash understands many different kinds of variables or parameters. Thus far, we haven't bothered much with what kind of variables we assigned, so our variables could hold any value that we assigned to them. A simple command line example demonstrates this:
```

`[bob in ~]` **`VARIABLE`=`_12_`**

`[bob in ~]` **echo `$VARIABLE`**
12

`[bob in ~]` **`VARIABLE`=`_string_`**

`[bob in ~]` **echo `$VARIABLE`**
string

```

---
There are cases when you want to avoid this kind of behavior, for instance when handling telephone and other numbers. Apart from integers and variables, you may also want to specify a variable that is a constant. This is often done at the beginning of a script, when the value of the constant is declared. After that, there are only references to the constant variable name, so that when the constant needs to be changed, it only has to be done once. A variable may also be a series of variables of any type, a so-called _array_ of variables (`VAR0``VAR1`, `VAR2`, ... `WARN`).
* * *
##  10.1.2. Using the declare built-in
Using a **declare** statement, we can limit the value assignment to variables.
The syntax for **declare** is the following:
**declare` OPTION(s)` `VARIABLE`=value**
The following options are used to determine the type of data the variable can hold and to assign it attributes:
**Table 10-1. Options to the declare built-in**
Option | Meaning
---|---
`-a` | Variable is an array.
`-f` | Use function names only.
`-i` | The variable is to be treated as an integer; arithmetic evaluation is performed when the variable is assigned a value (see [Section 3.4.6](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_04_05)).
`-p` | Display the attributes and values of each variable. When `-p` is used, additional options are ignored.
`-r` | Make variables read-only. These variables cannot then be assigned values by subsequent assignment statements, nor can they be unset.
`-t` | Give each variable the _trace_ attribute.
`-x` | Mark each variable for export to subsequent commands via the environment.
Using `+` instead of `-` turns off the attribute instead. When used in a function, **declare** creates local variables.
The following example shows how assignment of a type to a variable influences the value.
```

`[bob in ~]` **declare `-i` `VARIABLE`=`_12_`**

`[bob in ~]` **`VARIABLE`=`_string_`**

`[bob in ~]` **echo `$VARIABLE`**
0

`[bob in ~]` **declare `-p` `VARIABLE`**
declare -i VARIABLE="0"

```

---
Note that Bash has an option to declare a numeric value, but none for declaring string values. This is because, by default, if no specifications are given, a variable can hold any type of data:
```

`[bob in ~]` **`OTHERVAR`=`_blah_`**

`[bob in ~]` **declare `-p` `OTHERVAR`**
declare -- OTHERVAR="blah"

```

---
As soon as you restrict assignment of values to a variable, it can only hold that type of data. Possible restrictions are either integer, constant or array.
See the Bash info pages for information on return status.
* * *
##  10.1.3. Constants
In Bash, constants are created by making a variable read-only. The **readonly** built-in marks each specified variable as unchangeable. The syntax is:
**readonly` OPTION` `VARIABLE(s)`**
The values of these variables can then no longer be changed by subsequent assignment. If the `-f` option is given, each variable refers to a shell function; see [Chapter 11](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_11). If `-a` is specified, each variable refers to an array of variables. If no arguments are given, or if `-p` is supplied, a list of all read-only variables is displayed. Using the `-p` option, the output can be reused as input.
The return status is zero, unless an invalid option was specified, one of the variables or functions does not exist, or `-f` was supplied for a variable name instead of for a function name.
```

`[bob in ~]` **readonly `TUX`=`_penguinpower_`**

`[bob in ~]` **`TUX`=`_Mickeysoft_`**
bash: TUX: readonly variable

```

---
* * *
#  10.2. Array variables
##  10.2.1. Creating arrays
An array is a variable containing multiple values. Any variable may be used as an array. There is no maximum limit to the size of an array, nor any requirement that member variables be indexed or assigned contiguously. Arrays are zero-based: the first element is indexed with the number 0.
Indirect declaration is done using the following syntax to declare a variable:
**`ARRAY[INDEXNR]` =value**
The _INDEXNR_ is treated as an arithmetic expression that must evaluate to a positive number.
Explicit declaration of an array is done using the **declare** built-in:
**declare` -a` `ARRAYNAME`**
A declaration with an index number will also be accepted, but the index number will be ignored. Attributes to the array may be specified using the **declare** and **readonly** built-ins. Attributes apply to all variables in the array; you can't have mixed arrays.
Array variables may also be created using compound assignments in this format:
**`ARRAY` =(value1 value2 ... valueN)**
Each value is then in the form of _[indexnumber=]string_. The index number is optional. If it is supplied, that index is assigned to it; otherwise the index of the element assigned is the number of the last index that was assigned, plus one. This format is accepted by **declare** as well. If no index numbers are supplied, indexing starts at zero.
Adding missing or extra members in an array is done using the syntax:
**`ARRAYNAME[indexnumber]` =value**
Remember that the **read** built-in provides the `-a` option, which allows for reading and assigning values for member variables of an array.
* * *
##  10.2.2. Dereferencing the variables in an array
In order to refer to the content of an item in an array, use curly braces. This is necessary, as you can see from the following example, to bypass the shell interpretation of expansion operators. If the index number is _@_ or _*_ , all members of an array are referenced.
```

`[bob in ~]` **`ARRAY`=`_(one two three)_`**

`[bob in ~]` **echo `${ARRAY[*]}`**
one two three

`[bob in ~]` **echo `$ARRAY[*]`**
one[*]

`[bob in ~]` **echo `${ARRAY[2]}`**
three

`[bob in ~]` **`ARRAY[3]`=`_four_`**

`[bob in ~]` **echo `${ARRAY[*]}`**
one two three four

```

---
Referring to the content of a member variable of an array without providing an index number is the same as referring to the content of the first element, the one referenced with index number zero.
* * *
##  10.2.3. Deleting array variables
The **unset** built-in is used to destroy arrays or member variables of an array:
```

`[bob in ~]` **unset `ARRAY[1]`**

`[bob in ~]` **echo `${ARRAY[*]}`**
one three four

`[bob in ~]` **unset `ARRAY`**

`[bob in ~]` **echo `${ARRAY[*]}`**
<--no output-->

```

---
* * *
##  10.2.4. Examples of arrays
Practical examples of the usage of arrays are hard to find. You will find plenty of scripts that don't really do anything on your system but that do use arrays to calculate mathematical series, for instance. And that would be one of the more interesting examples...most scripts just show what you can do with an array in an oversimplified and theoretical way.
The reason for this dullness is that arrays are rather complex structures. You will find that most practical examples for which arrays could be used are already implemented on your system using arrays, however on a lower level, in the C programming language in which most UNIX commands are written. A good example is the Bash **history** built-in command. Those readers who are interested might check the `built-ins` directory in the Bash source tree and take a look at `fc.def`, which is processed when compiling the built-ins.
Another reason good examples are hard to find is that not all shells support arrays, so they break compatibility.
After long days of searching, I finally found this example operating at an Internet provider. It distributes Apache web server configuration files onto hosts in a web farm:
```

#!/bin/bash

if [ $(whoami) != 'root' ]; then
        echo "Must be root to run $0"
        exit 1;
fi
if [ -z $1 ]; then
        echo "Usage: $0 </path/to/httpd.conf>"
        exit 1
fi

httpd_conf_new=$1
httpd_conf_path="/usr/local/apache/conf"
login=htuser

farm_hosts=(web03 web04 web05 web06 web07)

for i in ${farm_hosts[@]}; do
        su $login -c "scp $httpd_conf_new ${i}:${httpd_conf_path}"
        su $login -c "ssh $i sudo /usr/local/apache/bin/apachectl graceful"

done
exit 0

```

---
First two tests are performed to check whether the correct user is running the script with the correct arguments. The names of the hosts that need to be configured are listed in the array `farm_hosts`. Then all these hosts are provided with the Apache configuration file, after which the daemon is restarted. Note the use of commands from the Secure Shell suite, encrypting the connections to remote hosts.
Thanks, Eugene and colleague, for this contribution.
Dan Richter contributed the following example. This is the problem he was confronted with:
"...In my company, we have demos on our web site, and every week someone has to test all of them. So I have a cron job that fills an array with the possible candidates, uses **date` +%W`** to find the week of the year, and does a modulo operation to find the correct index. The lucky person gets notified by e-mail."
And this was his way of solving it:
```

#!/bin/bash
