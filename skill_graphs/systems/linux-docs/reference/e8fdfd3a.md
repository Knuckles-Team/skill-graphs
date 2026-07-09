#  1.4. Building blocks
##  1.4.1. Shell building blocks
###  1.4.1.1. Shell syntax
If input is not commented, the shell reads it and divides it into words and operators, employing quoting rules to define the meaning of each character of input. Then these words and operators are translated into commands and other constructs, which return an exit status available for inspection or processing. The above fork-and-exec scheme is only applied after the shell has analyzed input in the following way:
  * The shell reads its input from a file, from a string or from the user's terminal.
  * Input is broken up into words and operators, obeying the quoting rules, see [Chapter 3](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_03). These tokens are separated by _metacharacters_. Alias expansion is performed.
  * The shell _parses_ (analyzes and substitutes) the tokens into simple and compound commands.
  * Bash performs various shell expansions, breaking the expanded tokens into lists of filenames and commands and arguments.
  * Redirection is performed if necessary, redirection operators and their operands are removed from the argument list.
  * Commands are executed.
  * Optionally the shell waits for the command to complete and collects its exit status.


* * *
###  1.4.1.2. Shell commands
A simple shell command such as **touch` file1` `file2` `file3`** consists of the command itself followed by arguments, separated by spaces.
More complex shell commands are composed of simple commands arranged together in a variety of ways: in a pipeline in which the output of one command becomes the input of a second, in a loop or conditional construct, or in some other grouping. A couple of examples:
**ls | more**
**gunzip` file.tar.gz` | tar `xvf` `_-_`**
* * *
###  1.4.1.3. Shell functions
Shell functions are a way to group commands for later execution using a single name for the group. They are executed just like a "regular" command. When the name of a shell function is used as a simple command name, the list of commands associated with that function name is executed.
Shell functions are executed in the current shell context; no new process is created to interpret them.
Functions are explained in [Chapter 11](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_11).
* * *
###  1.4.1.4. Shell parameters
A parameter is an entity that stores values. It can be a name, a number or a special value. For the shell's purpose, a variable is a parameter that stores a name. A variable has a value and zero or more attributes. Variables are created with the **declare** shell built-in command.
If no value is given, a variable is assigned the null string. Variables can only be removed with the **unset** built-in.
Assigning variables is discussed in [Section 3.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_02), advanced use of variables in [Chapter 10](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_10).
* * *
###  1.4.1.5. Shell expansions
Shell expansion is performed after each command line has been split into tokens. These are the expansions performed:
  * Brace expansion
  * Tilde expansion
  * Parameter and variable expansion
  * Command substitution
  * Arithmetic expansion
  * Word splitting
  * Filename expansion


We'll discuss these expansion types in detail in [Section 3.4](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_04).
* * *
###  1.4.1.6. Redirections
Before a command is executed, its input and output may be redirected using a special notation interpreted by the shell. Redirection may also be used to open and close files for the current shell execution environment.
* * *
###  1.4.1.7. Executing commands
When executing a command, the words that the parser has marked as variable assignments (preceding the command name) and redirections are saved for later reference. Words that are not variable assignments or redirections are expanded; the first remaining word after expansion is taken to be the name of the command and the rest are arguments to that command. Then redirections are performed, then strings assigned to variables are expanded. If no command name results, variables will affect the current shell environment.
An important part of the tasks of the shell is to search for commands. Bash does this as follows:
  * Check whether the command contains slashes. If not, first check with the function list to see if it contains a command by the name we are looking for.
  * If command is not a function, check for it in the built-in list.
  * If command is neither a function nor a built-in, look for it analyzing the directories listed in `PATH`. Bash uses a _hash table_ (data storage area in memory) to remember the full path names of executables so extensive `PATH` searches can be avoided.
  * If the search is unsuccessful, bash prints an error message and returns an exit status of 127.
  * If the search was successful or if the command contains slashes, the shell executes the command in a separate execution environment.
  * If execution fails because the file is not executable and not a directory, it is assumed to be a shell script.
  * If the command was not begun asynchronously, the shell waits for the command to complete and collects its exit status.


* * *
###  1.4.1.8. Shell scripts
When a file containing shell commands is used as the first non-option argument when invoking Bash (without `-c` or `-s`, this will create a non-interactive shell. This shell first searches for the script file in the current directory, then looks in `PATH` if the file cannot be found there.
* * *
