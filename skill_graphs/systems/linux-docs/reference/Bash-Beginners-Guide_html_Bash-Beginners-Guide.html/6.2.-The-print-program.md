#  6.2. The print program
##  6.2.1. Printing selected fields
The **print** command in **awk** outputs selected data from the input file.
When **awk** reads a line of a file, it divides the line in fields based on the specified _input field separator_ , `FS`, which is an **awk** variable (see [Section 6.3.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_03_02)). This variable is predefined to be one or more spaces or tabs.
The variables `$1`, `$2`, `$3`, ..., `$N` hold the values of the first, second, third until the last field of an input line. The variable `$0` (zero) holds the value of the entire line. This is depicted in the image below, where we see six columns in the output of the **df** command:
**Figure 6-1. Fields in awk**
![](https://tldp.org/LDP/Bash-Beginners-Guide/html/images/awk.png)
In the output of **ls` -l`**, there are 9 columns. The **print** statement uses these fields as follows:
```

`kelly@octarine ~/test>` **ls `-l` | awk `_'{ print $5 $9 }'_`**
160orig
121script.sed
120temp_file
126test
120twolines
441txt2html.sh

`kelly@octarine ~/test>`

```

---
This command printed the fifth column of a long file listing, which contains the file size, and the last column, the name of the file. This output is not very readable unless you use the official way of referring to columns, which is to separate the ones that you want to print with a comma. In that case, the default output separater character, usually a space, will be put in between each output field.
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **Local configuration**
---|---
| Note that the configuration of the output of the **ls` -l`** command might be different on your system. Display of time and date is dependent on your locale setting.
* * *
##  6.2.2. Formatting fields
Without formatting, using only the output separator, the output looks rather poor. Inserting a couple of tabs and a string to indicate what output this is will make it look a lot better:
```

`kelly@octarine ~/test>` **ls `-ldh` `*` | grep `-v` `_total_` | \
awk `_'{ print "Size is " $5 " bytes for " $9 }'_`**
Size is 160 bytes for orig
Size is 121 bytes for script.sed
Size is 120 bytes for temp_file
Size is 126 bytes for test
Size is 120 bytes for twolines
Size is 441 bytes for txt2html.sh

`kelly@octarine ~/test>`

```

---
Note the use of the backslash, which makes long input continue on the next line without the shell interpreting this as a separate command. While your command line input can be of virtually unlimited length, your monitor is not, and printed paper certainly isn't. Using the backslash also allows for copying and pasting of the above lines into a terminal window.
The `-h` option to **ls** is used for supplying humanly readable size formats for bigger files. The output of a long listing displaying the total amount of blocks in the directory is given when a directory is the argument. This line is useless to us, so we add an asterisk. We also add the `-d` option for the same reason, in case asterisk expands to a directory.
The backslash in this example marks the continuation of a line. See [Section 3.3.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_03_02).
You can take out any number of columns and even reverse the order. In the example below this is demonstrated for showing the most critical partitions:
```

`kelly@octarine ~>` **df `-h` | sort `-rnk` `_5_` | head `_-3_` | \
awk `_'{ print "Partition " $6 "\t: " $5 " full!" }'_`**
Partition /var  : 86% full!
Partition /usr  : 85% full!
Partition /home : 70% full!

`kelly@octarine ~>`

```

---
The table below gives an overview of special formatting characters:
**Table 6-1. Formatting characters for gawk**
Sequence | Meaning
---|---
\a | Bell character
\n | Newline character
\t | Tab
Quotes, dollar signs and other meta-characters should be escaped with a backslash.
* * *
##  6.2.3. The print command and regular expressions
A regular expression can be used as a pattern by enclosing it in slashes. The regular expression is then tested against the entire text of each record. The syntax is as follows:
**awk 'EXPRESSION { PROGRAM }'` file(s)`**
The following example displays only local disk device information, networked file systems are not shown:
```

`kelly is in ~>` **df `-h` | awk `_'/dev\/hd/ { print $6 "\t: " $5 }'_`**
/       : 46%
/boot   : 10%
/opt    : 84%
/usr    : 97%
/var    : 73%
/.vol1  : 8%

`kelly is in ~>`

```

---
Slashes need to be escaped, because they have a special meaning to the **awk** program.
Below another example where we search the `/etc` directory for files ending in ".conf" and starting with either "a" _or_ "x", using extended regular expressions:
```

`kelly is in /etc>` **ls `-l` | awk `_'/\<(a|x).*\.conf$/ { print $9 }'_`**
amd.conf
antivir.conf
xcdroast.conf
xinetd.conf

`kelly is in /etc>`

```

---
This example illustrates the special meaning of the dot in regular expressions: the first one indicates that we want to search for any character after the first search string, the second is escaped because it is part of a string to find (the end of the file name).
* * *
##  6.2.4. Special patterns
In order to precede output with comments, use the **BEGIN** statement:
```

`kelly is in /etc>` **ls `-l` | \
awk `_'BEGIN { print "Files found:\n" } /\<[a|x].*\.conf$/ { print $9 }'_`**
Files found:
amd.conf
antivir.conf
xcdroast.conf
xinetd.conf

`kelly is in /etc>`

```

---
The **END** statement can be added for inserting text after the entire input is processed:
```

`kelly is in /etc>` **ls `-l` | \
awk `_'/\<[a|x].*\.conf$/ { print $9 } END { print \
"Can I do anything else for you, mistress?" }'_`**
amd.conf
antivir.conf
xcdroast.conf
xinetd.conf
Can I do anything else for you, mistress?

`kelly is in /etc>`

```

---
* * *
##  6.2.5. Gawk scripts
As commands tend to get a little longer, you might want to put them in a script, so they are reusable. An **awk** script contains **awk** statements defining patterns and actions.
As an illustration, we will build a report that displays our most loaded partitions. See [Section 6.2.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_02_02).
```

`kelly is in ~>` **cat `diskrep.awk`**
BEGIN { print "*** WARNING WARNING WARNING ***" }
/\<[8|9][0-9]%/ { print "Partition " $6 "\t: " $5 " full!" }
END { print "*** Give money for new disks URGENTLY! ***" }

kelly is in ~> df -h | awk -f diskrep.awk
*** WARNING WARNING WARNING ***
Partition /usr  : 97% full!
*** Give money for new disks URGENTLY! ***

`kelly is in ~>`

```

---
**awk** first prints a begin message, then formats all the lines that contain an eight or a nine at the beginning of a word, followed by one other number and a percentage sign. An end message is added.
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **Syntax highlighting**
---|---
| Awk is a programming language. Its syntax is recognized by most editors that can do syntax highlighting for other languages, such as C, Bash, HTML, etc.
* * *
