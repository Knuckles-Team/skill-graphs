  # `basename $0` is the script's filename.
  exit $E_WRONG_ARGS
fi
```

---
Many times, you will write a script that carries out one particular task. The first script in this chapter is an example. Later, it might occur to you to generalize the script to do other, similar tasks. Replacing the literal ("hard-wired") constants by variables is a step in that direction, as is replacing repetitive code blocks by [functions](https://tldp.org/LDP/abs/html/abs-guide.html#FUNCTIONREF).
* * *
#  2.1. Invoking the script
Having written the script, you can invoke it by `**sh scriptname**` , [[13]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN300) or alternatively `**bash scriptname**`. (Not recommended is using `**sh <scriptname**`, since this effectively disables reading from [`stdin`](https://tldp.org/LDP/abs/html/abs-guide.html#STDINOUTDEF) within the script.) Much more convenient is to make the script itself directly executable with a [chmod](https://tldp.org/LDP/abs/html/abs-guide.html#CHMODREF).

Either:

`**chmod 555 scriptname**` (gives everyone read/execute permission) [[14]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN315)

or

`**chmod +rx scriptname**` (gives everyone read/execute permission)
`**chmod u+rx scriptname**` (gives only the script owner read/execute permission)
Having made the script executable, you may now test it by `**./scriptname**`. [[15]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN327) If it begins with a "sha-bang" line, invoking the script calls the correct command interpreter to run it.
As a final step, after testing and debugging, you would likely want to move it to `/usr/local/bin` (as _root_ , of course), to make the script available to yourself and all other users as a systemwide executable. The script could then be invoked by simply typing **scriptname** **[ENTER]** from the command-line.
* * *
#  2.2. Preliminary Exercises
  1. System administrators often write scripts to automate common tasks. Give several instances where such scripts would be useful.
  2. Write a script that upon invocation shows the [time and date](https://tldp.org/LDP/abs/html/abs-guide.html#DATEREF), [lists all logged-in users](https://tldp.org/LDP/abs/html/abs-guide.html#WHOREF), and gives the system [uptime](https://tldp.org/LDP/abs/html/abs-guide.html#UPTIMEREF). The script then [saves this information](https://tldp.org/LDP/abs/html/abs-guide.html#IOREDIRREF) to a logfile.


# Part 2. Basics

**Table of Contents**


3. [Special Characters](https://tldp.org/LDP/abs/html/abs-guide.html#SPECIAL-CHARS)


4. [Introduction to Variables and Parameters](https://tldp.org/LDP/abs/html/abs-guide.html#VARIABLES)


4.1. [Variable Substitution](https://tldp.org/LDP/abs/html/abs-guide.html#VARSUBN)


4.2. [Variable Assignment](https://tldp.org/LDP/abs/html/abs-guide.html#VARASSIGNMENT)


4.3. [Bash Variables Are Untyped](https://tldp.org/LDP/abs/html/abs-guide.html#UNTYPED)


4.4. [Special Variable Types](https://tldp.org/LDP/abs/html/abs-guide.html#OTHERTYPESV)


5. [Quoting](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTING)


5.1. [Quoting Variables](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTINGVAR)


5.2. [Escaping](https://tldp.org/LDP/abs/html/abs-guide.html#ESCAPINGSECTION)


6. [Exit and Exit Status](https://tldp.org/LDP/abs/html/abs-guide.html#EXIT-STATUS)


7. [Tests](https://tldp.org/LDP/abs/html/abs-guide.html#TESTS)


7.1. [Test Constructs](https://tldp.org/LDP/abs/html/abs-guide.html#TESTCONSTRUCTS)


7.2. [File test operators](https://tldp.org/LDP/abs/html/abs-guide.html#FTO)


7.3. [Other Comparison Operators](https://tldp.org/LDP/abs/html/abs-guide.html#COMPARISON-OPS)


7.4. [Nested `_if/then_` Condition Tests](https://tldp.org/LDP/abs/html/abs-guide.html#NESTEDIFTHEN)


7.5. [Testing Your Knowledge of Tests](https://tldp.org/LDP/abs/html/abs-guide.html#TESTTEST)


8. [Operations and Related Topics](https://tldp.org/LDP/abs/html/abs-guide.html#OPERATIONS)


8.1. [Operators](https://tldp.org/LDP/abs/html/abs-guide.html#OPS)


8.2. [Numerical Constants](https://tldp.org/LDP/abs/html/abs-guide.html#NUMERICAL-CONSTANTS)


8.3. [The Double-Parentheses Construct](https://tldp.org/LDP/abs/html/abs-guide.html#DBLPARENS)


8.4. [Operator Precedence](https://tldp.org/LDP/abs/html/abs-guide.html#OPPRECEDENCE)

* * *
#  Chapter 3. Special Characters
What makes a character _special_? If it has a meaning beyond its _literal meaning_ , a [meta-meaning](https://tldp.org/LDP/abs/html/abs-guide.html#METAMEANINGREF), then we refer to it as a _special character_. Along with commands and [keywords](https://tldp.org/LDP/abs/html/abs-guide.html#KEYWORDREF), _special characters_ are building blocks of Bash scripts.
**Special Characters Found In Scripts and Elsewhere**

#

**Comments.** Lines beginning with a # (with the exception of [ #!](https://tldp.org/LDP/abs/html/abs-guide.html#MAGNUMREF)) are comments and will _not_ be executed.
```
