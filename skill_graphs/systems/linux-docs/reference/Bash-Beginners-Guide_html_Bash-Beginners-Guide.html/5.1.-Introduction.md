#  5.1. Introduction
##  5.1.1. What is sed?
A Stream EDitor is used to perform basic transformations on text read from a file or a pipe. The result is sent to standard output. The syntax for the **sed** command has no output file specification, but results can be saved to a file using output redirection. The editor does not modify the original input.
What distinguishes **sed** from other editors, such as **vi** and **ed** , is its ability to filter text that it gets from a pipeline feed. You do not need to interact with the editor while it is running; that is why **sed** is sometimes called a _batch editor_. This feature allows use of editing commands in scripts, greatly easing repetitive editing tasks. When facing replacement of text in a large number of files, **sed** is a great help.
* * *
##  5.1.2. sed commands
The **sed** program can perform text pattern substitutions and deletions using regular expressions, like the ones used with the **grep** command; see [Section 4.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_04_02).
The editing commands are similar to the ones used in the **vi** editor:
**Table 5-1. Sed editing commands**
Command | Result
---|---
a\ | Append text below current line.
c\ | Change text in the current line with new text.
d | Delete text.
i\ | Insert text above current line.
p | Print text.
r | Read a file.
s | Search and replace text.
w | Write to a file.
Apart from editing commands, you can give options to **sed**. An overview is in the table below:
**Table 5-2. Sed options**
Option | Effect
---|---
`-e SCRIPT` | Add the commands in SCRIPT to the set of commands to be run while processing the input.
`-f` | Add the commands contained in the file SCRIPT-FILE to the set of commands to be run while processing the input.
`-n` | Silent mode.
`-V` | Print version information and exit.
The **sed** info pages contain more information; we only list the most frequently used commands and options here.
* * *
