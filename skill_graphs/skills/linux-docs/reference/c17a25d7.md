# Excerpted from life.sh script
```

---
![Caution](https://tldp.org/LDP/abs/images/caution.gif) | A command may not follow a comment on the same line. There is no method of terminating the comment, in order for "live code" to begin on the same line. Use a new line for the next command.
---|---
![Note](https://tldp.org/LDP/abs/images/note.gif) |  Of course, a [quoted](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTINGREF) or an [escaped](https://tldp.org/LDP/abs/html/abs-guide.html#ESCP) # in an [echo](https://tldp.org/LDP/abs/html/abs-guide.html#ECHOREF) statement does _not_ begin a comment. Likewise, a # appears in [certain parameter-substitution constructs](https://tldp.org/LDP/abs/html/abs-guide.html#PSUB2) and in [ numerical constant expressions](https://tldp.org/LDP/abs/html/abs-guide.html#NUMCONSTANTS).  | ```
echo "The # here does not begin a comment."
echo 'The # here does not begin a comment.'
echo The \# here does not begin a comment.
echo The # here begins a comment.

echo ${PATH#*:}       # Parameter substitution, not a comment.
echo $(( 2#101011 ))  # Base conversion, not a comment.

# Thanks, S.C.
```

---
The standard [quoting and escape](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTINGREF) characters (" ' \\) escape the #.
Certain [pattern matching operations](https://tldp.org/LDP/abs/html/abs-guide.html#PSOREX1) also use the #.

;

**Command separator [semicolon].** Permits putting two or more commands on the same line.
```
echo hello; echo there


if [ -x "$filename" ]; then    #  Note the space after the semicolon.
#+                   ^^
  echo "File $filename exists."; cp $filename $filename.bak
else   #                       ^^
  echo "File $filename not found."; touch $filename
fi; echo "File test complete."
```

---
Note that the ";" [sometimes needs to be _escaped_](https://tldp.org/LDP/abs/html/abs-guide.html#FINDREF0).

;;

**Terminator in a[case](https://tldp.org/LDP/abs/html/abs-guide.html#CASEESAC1) option [double semicolon]. **
```
case "$variable" in
  abc)  echo "\$variable = abc" ;;
  xyz)  echo "\$variable = xyz" ;;
esac
```

---

;;&, ;&

**[Terminators](https://tldp.org/LDP/abs/html/abs-guide.html#NCTERM) in a _case_ option ([version 4+](https://tldp.org/LDP/abs/html/abs-guide.html#BASH4REF) of Bash). **

.

**"dot" command [period]. **Equivalent to [source](https://tldp.org/LDP/abs/html/abs-guide.html#SOURCEREF) (see [Example 15-22](https://tldp.org/LDP/abs/html/abs-guide.html#EX38)). This is a bash [builtin](https://tldp.org/LDP/abs/html/abs-guide.html#BUILTINREF).

.

**"dot" , as a component of a filename. **When working with filenames, a leading dot is the prefix of a "hidden" file, a file that an [ls](https://tldp.org/LDP/abs/html/abs-guide.html#LSREF) will not normally show.
```
`bash$ ``**touch .hidden-file**`
`bash$ ``**ls -l**`
`total 10
 -rw-r--r--    1 bozo      4034 Jul 18 22:04 data1.addressbook
 -rw-r--r--    1 bozo      4602 May 25 13:58 data1.addressbook.bak
 -rw-r--r--    1 bozo       877 Dec 17  2000 employment.addressbook`


`bash$ ``**ls -al**`
`total 14
 drwxrwxr-x    2 bozo  bozo      1024 Aug 29 20:54 ./
 drwx------   52 bozo  bozo      3072 Aug 29 20:51 ../
 -rw-r--r--    1 bozo  bozo      4034 Jul 18 22:04 data1.addressbook
 -rw-r--r--    1 bozo  bozo      4602 May 25 13:58 data1.addressbook.bak
 -rw-r--r--    1 bozo  bozo       877 Dec 17  2000 employment.addressbook
 -rw-rw-r--    1 bozo  bozo         0 Aug 29 20:54 .hidden-file`

```

---
When considering directory names, _a single dot_ represents the current working directory, and _two dots_ denote the parent directory.
```
`bash$ ``**pwd**`
`/home/bozo/projects`

`bash$ ``**cd .**`
`bash$ ``**pwd**`
`/home/bozo/projects`

`bash$ ``**cd ..**`
`bash$ ``**pwd**`
`/home/bozo/`

```

---
The _dot_ often appears as the destination (directory) of a file movement command, in this context meaning _current directory_.
```
`bash$ ``**cp /home/bozo/current_work/junk/* .**`

```

---
Copy all the "junk" files to [$PWD](https://tldp.org/LDP/abs/html/abs-guide.html#PWDREF).

.

**"dot" character match. **When [matching characters](https://tldp.org/LDP/abs/html/abs-guide.html#REGEXDOT), as part of a [regular expression](https://tldp.org/LDP/abs/html/abs-guide.html#REGEXREF), a "dot" [matches a single character](https://tldp.org/LDP/abs/html/abs-guide.html#REGEXDOT).

"

**[partial quoting](https://tldp.org/LDP/abs/html/abs-guide.html#DBLQUO) [double quote]. **_"STRING"_ preserves (from interpretation) most of the special characters within _STRING_. See [Chapter 5](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTING).

'

**[full quoting](https://tldp.org/LDP/abs/html/abs-guide.html#SNGLQUO) [single quote]. **_'STRING'_ preserves all special characters within _STRING_. This is a stronger form of quoting than _"STRING"_. See [Chapter 5](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTING).

,

**[comma operator](https://tldp.org/LDP/abs/html/abs-guide.html#COMMAOP). **The _comma operator_ [[16]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN612) links together a series of arithmetic operations. All are evaluated, but only the last one is returned.
```
let "t2 = ((a = 9, 15 / 3))"
# Set "a = 9" and "t2 = 15 / 3"
```

---
The _comma_ operator can also concatenate strings.
```
for file in /{,usr/}bin/*calc
#             ^    Find all executable files ending in "calc"
#+                 in /bin and /usr/bin directories.
do
        if [ -x "$file" ]
        then
          echo $file
        fi
done

# /bin/ipcalc
# /usr/bin/kcalc
# /usr/bin/oidcalc
# /usr/bin/oocalc


# Thank you, Rory Winston, for pointing this out.
```

---

,, ,

**[Lowercase conversion](https://tldp.org/LDP/abs/html/abs-guide.html#CASEMODPARAMSUB) in _parameter substitution_ (added in [version 4](https://tldp.org/LDP/abs/html/abs-guide.html#BASH4REF) of Bash). **

\

**[escape](https://tldp.org/LDP/abs/html/abs-guide.html#ESCP) [backslash]. **A quoting mechanism for single characters.
`**\X**` _escapes_ the character _X_. This has the effect of "quoting" _X_ , equivalent to _'X'_. The \ may be used to quote " and ', so they are expressed literally.
See [Chapter 5](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTING) for an in-depth explanation of escaped characters.

/

**Filename path separator [forward slash].** Separates the components of a filename (as in `/home/bozo/projects/Makefile`).
This is also the division [arithmetic operator](https://tldp.org/LDP/abs/html/abs-guide.html#AROPS1).

`

**[command substitution](https://tldp.org/LDP/abs/html/abs-guide.html#COMMANDSUBREF). **The **`command`** construct makes available the output of **command** for assignment to a variable. This is also known as [backquotes](https://tldp.org/LDP/abs/html/abs-guide.html#BACKQUOTESREF) or backticks.

:

**null command [colon].** This is the shell equivalent of a "NOP" (`_no op_` , a do-nothing operation). It may be considered a synonym for the shell builtin [true](https://tldp.org/LDP/abs/html/abs-guide.html#TRUEREF). The ":" command is itself a _Bash_ [builtin](https://tldp.org/LDP/abs/html/abs-guide.html#BUILTINREF), and its [exit status](https://tldp.org/LDP/abs/html/abs-guide.html#EXITSTATUSREF) is _true_ (0).
```
:
echo $?   # 0
```

---
Endless loop:
```
while :
do
   operation-1
   operation-2
   ...
   operation-n
done

# Same as:
#    while true
#    do
#      ...
#    done
```

---
Placeholder in if/then test:
```
if condition
then :   # Do nothing and branch ahead
else     # Or else ...
   take-some-action
fi
```

---
Provide a placeholder where a binary operation is expected, see [Example 8-2](https://tldp.org/LDP/abs/html/abs-guide.html#ARITHOPS) and [default parameters](https://tldp.org/LDP/abs/html/abs-guide.html#DEFPARAM).
```
: ${username=`whoami`}
# ${username=`whoami`}   Gives an error without the leading :
#                        unless "username" is a command or builtin...

: ${1?"Usage: $0 ARGUMENT"}     # From "usage-message.sh example script.
```

---
Provide a placeholder where a command is expected in a [here document](https://tldp.org/LDP/abs/html/abs-guide.html#HEREDOCREF). See [Example 19-10](https://tldp.org/LDP/abs/html/abs-guide.html#ANONHEREDOC).
Evaluate string of variables using [parameter substitution](https://tldp.org/LDP/abs/html/abs-guide.html#PARAMSUBREF) (as in [Example 10-7](https://tldp.org/LDP/abs/html/abs-guide.html#EX6)).
```
: ${HOSTNAME?} ${USER?} ${MAIL?}
#  Prints error message
#+ if one or more of essential environmental variables not set.
```

---
**[Variable expansion / substring replacement](https://tldp.org/LDP/abs/html/abs-guide.html#EXPREPL1)**.
In combination with the > [redirection operator](https://tldp.org/LDP/abs/html/abs-guide.html#IOREDIRREF), truncates a file to zero length, without changing its permissions. If the file did not previously exist, creates it.
```
: > data.xxx   # File "data.xxx" now empty.

# Same effect as   cat /dev/null >data.xxx
# However, this does not fork a new process, since ":" is a builtin.
```

---
See also [Example 16-15](https://tldp.org/LDP/abs/html/abs-guide.html#EX12).
In combination with the >> redirection operator, has no effect on a pre-existing target file (`**: >> target_file**`). If the file did not previously exist, creates it.
![Note](https://tldp.org/LDP/abs/images/note.gif) | This applies to regular files, not pipes, symlinks, and certain special files.
---|---
May be used to begin a comment line, although this is not recommended. Using # for a comment turns off error checking for the remainder of that line, so almost anything may appear in a comment. However, this is not the case with :.
```
: This is a comment that generates an error, ( if [ $x -eq 3] ).
```

---
The ":" serves as a [field](https://tldp.org/LDP/abs/html/abs-guide.html#FIELDREF) separator, in [`/etc/passwd`](https://tldp.org/LDP/abs/html/abs-guide.html#DATAFILESREF1), and in the [$PATH](https://tldp.org/LDP/abs/html/abs-guide.html#PATHREF) variable.
```
`bash$ ``**echo $PATH**`
`/usr/local/bin:/bin:/usr/bin:/usr/X11R6/bin:/sbin:/usr/sbin:/usr/games`
```

---
A _colon_ is [acceptable as a function name](https://tldp.org/LDP/abs/html/abs-guide.html#FSTRANGEREF).
```
:()
{
  echo "The name of this function is "$FUNCNAME" "
  # Why use a colon as a function name?
  # It's a way of obfuscating your code.
}

:

# The name of this function is :
```

---
This is not [portable](https://tldp.org/LDP/abs/html/abs-guide.html#PORTABILITYISSUES) behavior, and therefore not a recommended practice. In fact, more recent releases of Bash do not permit this usage. An underscore **_** works, though.
A _colon_ can serve as a placeholder in an otherwise empty function.
```
not_empty ()
{
  :
} # Contains a : (null command), and so is not empty.
```

---

!

**reverse (or negate) the sense of a test or exit status [bang].** The ! operator inverts the [exit status](https://tldp.org/LDP/abs/html/abs-guide.html#EXITSTATUSREF) of the command to which it is applied (see [Example 6-2](https://tldp.org/LDP/abs/html/abs-guide.html#NEGCOND)). It also inverts the meaning of a test operator. This can, for example, change the sense of _equal_ ( [=](https://tldp.org/LDP/abs/html/abs-guide.html#EQUALSIGNREF) ) to _not-equal_ ( != ). The ! operator is a Bash [keyword](https://tldp.org/LDP/abs/html/abs-guide.html#KEYWORDREF).
In a different context, the ! also appears in [indirect variable references](https://tldp.org/LDP/abs/html/abs-guide.html#IVRREF).
In yet another context, from the _command line_ , the ! invokes the Bash _history mechanism_ (see [Appendix L](https://tldp.org/LDP/abs/html/abs-guide.html#HISTCOMMANDS)). Note that within a script, the history mechanism is disabled.

*

**wild card [asterisk].** The * character serves as a "wild card" for filename expansion in [globbing](https://tldp.org/LDP/abs/html/abs-guide.html#GLOBBINGREF). By itself, it matches every filename in a given directory.
```
`bash$ ``**echo ***`
`abs-book.sgml add-drive.sh agram.sh alias.sh`

```

---
The * also represents [any number (or zero) characters](https://tldp.org/LDP/abs/html/abs-guide.html#ASTERISKREG) in a [regular expression](https://tldp.org/LDP/abs/html/abs-guide.html#REGEXREF).

*

**[arithmetic operator](https://tldp.org/LDP/abs/html/abs-guide.html#AROPS1). **In the context of arithmetic operations, the * denotes multiplication.
** A double asterisk can represent the [exponentiation](https://tldp.org/LDP/abs/html/abs-guide.html#EXPONENTIATIONREF) operator or [extended file-match](https://tldp.org/LDP/abs/html/abs-guide.html#GLOBSTARREF) _globbing_.

?

**test operator.** Within certain expressions, the ? indicates a test for a condition.
In a [double-parentheses construct](https://tldp.org/LDP/abs/html/abs-guide.html#DBLPARENS), the ? can serve as an element of a C-style _trinary_ operator. [[17]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN888)
`condition`**?**` result-if-true`**:**` result-if-false`
```
(( var0 = var1<98?9:21 ))
#                ^ ^

# if [ "$var1" -lt 98 ]
# then
#   var0=9
# else
#   var0=21
# fi
```

---
In a [parameter substitution](https://tldp.org/LDP/abs/html/abs-guide.html#PARAMSUBREF) expression, the ? [tests whether a variable has been set](https://tldp.org/LDP/abs/html/abs-guide.html#QERRMSG).

?

**wild card.**The ? character serves as a single-character "wild card" for filename expansion in [globbing](https://tldp.org/LDP/abs/html/abs-guide.html#GLOBBINGREF), as well as [representing one character](https://tldp.org/LDP/abs/html/abs-guide.html#QUEXREGEX) in an [extended regular expression](https://tldp.org/LDP/abs/html/abs-guide.html#EXTREGEX).

$

**[Variable substitution](https://tldp.org/LDP/abs/html/abs-guide.html#VARSUBN) (contents of a variable). **
```
var1=5
var2=23skidoo

echo $var1     # 5
echo $var2     # 23skidoo
```

---
A $ prefixing a variable name indicates the _value_ the variable holds.

$

**end-of-line.** In a [regular expression](https://tldp.org/LDP/abs/html/abs-guide.html#REGEXREF), a "$" addresses the [end of a line](https://tldp.org/LDP/abs/html/abs-guide.html#DOLLARSIGNREF) of text.

${}

**[Parameter substitution](https://tldp.org/LDP/abs/html/abs-guide.html#PARAMSUBREF). **

$' ... '

**[Quoted string expansion](https://tldp.org/LDP/abs/html/abs-guide.html#STRQ). **This construct expands single or multiple escaped octal or hex values into ASCII [[18]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN1001) or [Unicode](https://tldp.org/LDP/abs/html/abs-guide.html#UNICODEREF) characters.

$*, $@

**[positional parameters](https://tldp.org/LDP/abs/html/abs-guide.html#APPREF). **

$?

**exit status variable.** The [$? variable](https://tldp.org/LDP/abs/html/abs-guide.html#EXSREF) holds the [exit status](https://tldp.org/LDP/abs/html/abs-guide.html#EXITSTATUSREF) of a command, a [function](https://tldp.org/LDP/abs/html/abs-guide.html#FUNCTIONREF), or of the script itself.

$$

**process ID variable.** The [$$ variable](https://tldp.org/LDP/abs/html/abs-guide.html#PROCCID) holds the _process ID_ [[19]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN1071) of the script in which it appears.

()

**command group.**
```
(a=hello; echo $a)
```

---
![Important](https://tldp.org/LDP/abs/images/important.gif) |  A listing of commands within `_parentheses_` starts a [subshell](https://tldp.org/LDP/abs/html/abs-guide.html#SUBSHELLSREF). Variables inside parentheses, within the subshell, are not visible to the rest of the script. The parent process, the script, [cannot read variables created in the child process](https://tldp.org/LDP/abs/html/abs-guide.html#PARVIS), the subshell.  | ```
a=123
( a=321; )

echo "a = $a"   # a = 123
