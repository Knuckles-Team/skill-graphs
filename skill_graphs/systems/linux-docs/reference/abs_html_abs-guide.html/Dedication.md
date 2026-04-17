#  Dedication
For Anita, the source of all the magic

**Table of Contents**


Part 1. [Introduction](https://tldp.org/LDP/abs/html/abs-guide.html#PART1)


1. [Shell Programming!](https://tldp.org/LDP/abs/html/abs-guide.html#WHY-SHELL)


2. [Starting Off With a Sha-Bang](https://tldp.org/LDP/abs/html/abs-guide.html#SHA-BANG)


Part 2. [Basics](https://tldp.org/LDP/abs/html/abs-guide.html#PART2)


3. [Special Characters](https://tldp.org/LDP/abs/html/abs-guide.html#SPECIAL-CHARS)


4. [Introduction to Variables and Parameters](https://tldp.org/LDP/abs/html/abs-guide.html#VARIABLES)


5. [Quoting](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTING)


6. [Exit and Exit Status](https://tldp.org/LDP/abs/html/abs-guide.html#EXIT-STATUS)


7. [Tests](https://tldp.org/LDP/abs/html/abs-guide.html#TESTS)


8. [Operations and Related Topics](https://tldp.org/LDP/abs/html/abs-guide.html#OPERATIONS)


Part 3. [Beyond the Basics](https://tldp.org/LDP/abs/html/abs-guide.html#PART3)


9. [Another Look at Variables](https://tldp.org/LDP/abs/html/abs-guide.html#VARIABLES2)


10. [Manipulating Variables](https://tldp.org/LDP/abs/html/abs-guide.html#MANIPULATINGVARS)


11. [Loops and Branches](https://tldp.org/LDP/abs/html/abs-guide.html#LOOPS)


12. [Command Substitution](https://tldp.org/LDP/abs/html/abs-guide.html#COMMANDSUB)


13. [Arithmetic Expansion](https://tldp.org/LDP/abs/html/abs-guide.html#ARITHEXP)


14. [Recess Time](https://tldp.org/LDP/abs/html/abs-guide.html#RECESS-TIME)


Part 4. [Commands](https://tldp.org/LDP/abs/html/abs-guide.html#PART4)


15. [Internal Commands and Builtins](https://tldp.org/LDP/abs/html/abs-guide.html#INTERNAL)


16. [External Filters, Programs and Commands](https://tldp.org/LDP/abs/html/abs-guide.html#EXTERNAL)


17. [System and Administrative Commands](https://tldp.org/LDP/abs/html/abs-guide.html#SYSTEM)


Part 5. [Advanced Topics](https://tldp.org/LDP/abs/html/abs-guide.html#PART5)


18. [Regular Expressions](https://tldp.org/LDP/abs/html/abs-guide.html#REGEXP)


19. [Here Documents](https://tldp.org/LDP/abs/html/abs-guide.html#HERE-DOCS)


20. [I/O Redirection](https://tldp.org/LDP/abs/html/abs-guide.html#IO-REDIRECTION)


21. [Subshells](https://tldp.org/LDP/abs/html/abs-guide.html#SUBSHELLS)


22. [Restricted Shells](https://tldp.org/LDP/abs/html/abs-guide.html#RESTRICTED-SH)


23. [Process Substitution](https://tldp.org/LDP/abs/html/abs-guide.html#PROCESS-SUB)


24. [Functions](https://tldp.org/LDP/abs/html/abs-guide.html#FUNCTIONS)


25. [Aliases](https://tldp.org/LDP/abs/html/abs-guide.html#ALIASES)


26. [List Constructs](https://tldp.org/LDP/abs/html/abs-guide.html#LIST-CONS)


27. [Arrays](https://tldp.org/LDP/abs/html/abs-guide.html#ARRAYS)


28. [Indirect References](https://tldp.org/LDP/abs/html/abs-guide.html#IVR)


29. [`/dev` and `/proc`](https://tldp.org/LDP/abs/html/abs-guide.html#DEVPROC)


30. [Network Programming](https://tldp.org/LDP/abs/html/abs-guide.html#NETWORKPROGRAMMING)


31. [Of Zeros and Nulls](https://tldp.org/LDP/abs/html/abs-guide.html#ZEROS)


32. [Debugging](https://tldp.org/LDP/abs/html/abs-guide.html#DEBUGGING)


33. [Options](https://tldp.org/LDP/abs/html/abs-guide.html#OPTIONS)


34. [Gotchas](https://tldp.org/LDP/abs/html/abs-guide.html#GOTCHAS)


35. [Scripting With Style](https://tldp.org/LDP/abs/html/abs-guide.html#SCRSTYLE)


36. [Miscellany](https://tldp.org/LDP/abs/html/abs-guide.html#MISCELLANY)


37. [Bash, versions 2, 3, and 4](https://tldp.org/LDP/abs/html/abs-guide.html#BASH2)


38. [Endnotes](https://tldp.org/LDP/abs/html/abs-guide.html#ENDNOTES)


38.1. [Author's Note](https://tldp.org/LDP/abs/html/abs-guide.html#AUTHORSNOTE)


38.2. [About the Author](https://tldp.org/LDP/abs/html/abs-guide.html#ABOUTAUTHOR)


38.3. [Where to Go For Help](https://tldp.org/LDP/abs/html/abs-guide.html#WHEREHELP)


38.4. [Tools Used to Produce This Book](https://tldp.org/LDP/abs/html/abs-guide.html#TOOLSUSED)


38.5. [Credits](https://tldp.org/LDP/abs/html/abs-guide.html#CREDITS)


38.6. [Disclaimer](https://tldp.org/LDP/abs/html/abs-guide.html#DISCLAIMER)


[Bibliography](https://tldp.org/LDP/abs/html/abs-guide.html#BIBLIO)


A. [Contributed Scripts](https://tldp.org/LDP/abs/html/abs-guide.html#CONTRIBUTED-SCRIPTS)


B. [Reference Cards](https://tldp.org/LDP/abs/html/abs-guide.html#REFCARDS)


C. [A Sed and Awk Micro-Primer](https://tldp.org/LDP/abs/html/abs-guide.html#SEDAWK)


C.1. [Sed](https://tldp.org/LDP/abs/html/abs-guide.html#AEN23170)


C.2. [Awk](https://tldp.org/LDP/abs/html/abs-guide.html#AWK)


D. [Parsing and Managing Pathnames](https://tldp.org/LDP/abs/html/abs-guide.html#PATHMANAGEMENT)


E. [Exit Codes With Special Meanings](https://tldp.org/LDP/abs/html/abs-guide.html#EXITCODES)


F. [A Detailed Introduction to I/O and I/O Redirection](https://tldp.org/LDP/abs/html/abs-guide.html#IOREDIRINTRO)


G. [Command-Line Options](https://tldp.org/LDP/abs/html/abs-guide.html#COMMAND-LINE-OPTIONS)


G.1. [Standard Command-Line Options](https://tldp.org/LDP/abs/html/abs-guide.html#STANDARD-OPTIONS)


G.2. [Bash Command-Line Options](https://tldp.org/LDP/abs/html/abs-guide.html#BASH-OPTIONS)


H. [Important Files](https://tldp.org/LDP/abs/html/abs-guide.html#FILES)


I. [Important System Directories](https://tldp.org/LDP/abs/html/abs-guide.html#SYSTEMDIRS)


J. [An Introduction to Programmable Completion](https://tldp.org/LDP/abs/html/abs-guide.html#TABEXPANSION)


K. [Localization](https://tldp.org/LDP/abs/html/abs-guide.html#LOCALIZATION)


L. [History Commands](https://tldp.org/LDP/abs/html/abs-guide.html#HISTCOMMANDS)


M. [Sample `.bashrc` and `.bash_profile` Files](https://tldp.org/LDP/abs/html/abs-guide.html#SAMPLE-BASHRC)


N. [Converting DOS Batch Files to Shell Scripts](https://tldp.org/LDP/abs/html/abs-guide.html#DOSBATCH)


O. [Exercises](https://tldp.org/LDP/abs/html/abs-guide.html#EXERCISES)


O.1. [Analyzing Scripts](https://tldp.org/LDP/abs/html/abs-guide.html#SCRIPTANALYSIS)


O.2. [Writing Scripts](https://tldp.org/LDP/abs/html/abs-guide.html#WRITINGSCRIPTS)


P. [Revision History](https://tldp.org/LDP/abs/html/abs-guide.html#REVISIONHISTORY)


Q. [Download and Mirror Sites](https://tldp.org/LDP/abs/html/abs-guide.html#MIRRORSITES)


R. [To Do List](https://tldp.org/LDP/abs/html/abs-guide.html#TODOLIST)


S. [Copyright](https://tldp.org/LDP/abs/html/abs-guide.html#COPYRIGHT)


T. [ASCII Table](https://tldp.org/LDP/abs/html/abs-guide.html#ASCIITABLE)


[Index](https://tldp.org/LDP/abs/html/abs-guide.html#XREFINDEX)


**List of Tables**


8-1. [Operator Precedence](https://tldp.org/LDP/abs/html/abs-guide.html#AEN4294)


15-1. [Job identifiers](https://tldp.org/LDP/abs/html/abs-guide.html#JOBIDTABLE)


33-1. [Bash options](https://tldp.org/LDP/abs/html/abs-guide.html#AEN19601)


36-1. [Numbers representing colors in Escape Sequences](https://tldp.org/LDP/abs/html/abs-guide.html#AEN20327)


B-1. [Special Shell Variables](https://tldp.org/LDP/abs/html/abs-guide.html#AEN22402)


B-2. [TEST Operators: Binary Comparison](https://tldp.org/LDP/abs/html/abs-guide.html#AEN22473)


B-3. [TEST Operators: Files](https://tldp.org/LDP/abs/html/abs-guide.html#AEN22593)


B-4. [Parameter Substitution and Expansion](https://tldp.org/LDP/abs/html/abs-guide.html#AEN22728)


B-5. [String Operations](https://tldp.org/LDP/abs/html/abs-guide.html#AEN22828)


B-6. [Miscellaneous Constructs](https://tldp.org/LDP/abs/html/abs-guide.html#AEN22979)


C-1. [Basic sed operators](https://tldp.org/LDP/abs/html/abs-guide.html#AEN23200)


C-2. [Examples of sed operators](https://tldp.org/LDP/abs/html/abs-guide.html#AEN23271)


E-1. [_Reserved_ Exit Codes](https://tldp.org/LDP/abs/html/abs-guide.html#AEN23549)


N-1. [Batch file keywords / variables / operators, and their shell equivalents](https://tldp.org/LDP/abs/html/abs-guide.html#AEN24336)


N-2. [DOS commands and their UNIX equivalents](https://tldp.org/LDP/abs/html/abs-guide.html#AEN24545)


P-1. [Revision History](https://tldp.org/LDP/abs/html/abs-guide.html#AEN25364)


**List of Examples**


2-1. [_cleanup_ : A script to clean up log files in /var/log](https://tldp.org/LDP/abs/html/abs-guide.html#EX1)


2-2. [_cleanup_ : An improved clean-up script](https://tldp.org/LDP/abs/html/abs-guide.html#EX1A)


2-3. [_cleanup_ : An enhanced and generalized version of above scripts.](https://tldp.org/LDP/abs/html/abs-guide.html#EX2)


3-1. [Code blocks and I/O redirection](https://tldp.org/LDP/abs/html/abs-guide.html#EX8)


3-2. [Saving the output of a code block to a file](https://tldp.org/LDP/abs/html/abs-guide.html#RPMCHECK)


3-3. [Running a loop in the background](https://tldp.org/LDP/abs/html/abs-guide.html#BGLOOP)


3-4. [Backup of all files changed in last day](https://tldp.org/LDP/abs/html/abs-guide.html#EX58)


4-1. [Variable assignment and substitution](https://tldp.org/LDP/abs/html/abs-guide.html#EX9)


4-2. [Plain Variable Assignment](https://tldp.org/LDP/abs/html/abs-guide.html#EX15)


4-3. [Variable Assignment, plain and fancy](https://tldp.org/LDP/abs/html/abs-guide.html#EX16)


4-4. [Integer or string?](https://tldp.org/LDP/abs/html/abs-guide.html#INTORSTRING)


4-5. [Positional Parameters](https://tldp.org/LDP/abs/html/abs-guide.html#EX17)


4-6. [_wh_ , _whois_ domain name lookup](https://tldp.org/LDP/abs/html/abs-guide.html#EX18)


4-7. [Using _shift_](https://tldp.org/LDP/abs/html/abs-guide.html#EX19)


5-1. [Echoing Weird Variables](https://tldp.org/LDP/abs/html/abs-guide.html#WEIRDVARS)


5-2. [Escaped Characters](https://tldp.org/LDP/abs/html/abs-guide.html#ESCAPED)


5-3. [Detecting key-presses](https://tldp.org/LDP/abs/html/abs-guide.html#BASHEK)


6-1. [exit / exit status](https://tldp.org/LDP/abs/html/abs-guide.html#EX5)


6-2. [Negating a condition using !](https://tldp.org/LDP/abs/html/abs-guide.html#NEGCOND)


7-1. [What is truth?](https://tldp.org/LDP/abs/html/abs-guide.html#EX10)


7-2. [Equivalence of _test_ , `/usr/bin/test`, [ ], and `/usr/bin/[`](https://tldp.org/LDP/abs/html/abs-guide.html#EX11)


7-3. [Arithmetic Tests using (( ))](https://tldp.org/LDP/abs/html/abs-guide.html#ARITHTESTS)


7-4. [Testing for broken links](https://tldp.org/LDP/abs/html/abs-guide.html#BROKENLINK)


7-5. [Arithmetic and string comparisons](https://tldp.org/LDP/abs/html/abs-guide.html#EX13)


7-6. [Testing whether a string is _null_](https://tldp.org/LDP/abs/html/abs-guide.html#STRTEST)


7-7. [_zmore_](https://tldp.org/LDP/abs/html/abs-guide.html#EX14)


8-1. [Greatest common divisor](https://tldp.org/LDP/abs/html/abs-guide.html#GCD)


8-2. [Using Arithmetic Operations](https://tldp.org/LDP/abs/html/abs-guide.html#ARITHOPS)


8-3. [Compound Condition Tests Using && and ||](https://tldp.org/LDP/abs/html/abs-guide.html#ANDOR)


8-4. [Representation of numerical constants](https://tldp.org/LDP/abs/html/abs-guide.html#NUMBERS)


8-5. [C-style manipulation of variables](https://tldp.org/LDP/abs/html/abs-guide.html#CVARS)


9-1. [$IFS and whitespace](https://tldp.org/LDP/abs/html/abs-guide.html#IFSH)


9-2. [Timed Input](https://tldp.org/LDP/abs/html/abs-guide.html#TMDIN)


9-3. [Once more, timed input](https://tldp.org/LDP/abs/html/abs-guide.html#TIMEOUT)


9-4. [Timed _read_](https://tldp.org/LDP/abs/html/abs-guide.html#TOUT)


9-5. [Am I root?](https://tldp.org/LDP/abs/html/abs-guide.html#AMIROOT)


9-6. [_arglist_ : Listing arguments with $* and $@](https://tldp.org/LDP/abs/html/abs-guide.html#ARGLIST)


9-7. [Inconsistent `$*` and `$@` behavior](https://tldp.org/LDP/abs/html/abs-guide.html#INCOMPAT)


9-8. [`$*` and `$@` when `$IFS` is empty](https://tldp.org/LDP/abs/html/abs-guide.html#IFSEMPTY)


9-9. [Underscore variable](https://tldp.org/LDP/abs/html/abs-guide.html#USCREF)


9-10. [Using _declare_ to type variables](https://tldp.org/LDP/abs/html/abs-guide.html#EX20)


9-11. [Generating random numbers](https://tldp.org/LDP/abs/html/abs-guide.html#EX21)


9-12. [Picking a random card from a deck](https://tldp.org/LDP/abs/html/abs-guide.html#PICKCARD)


9-13. [Brownian Motion Simulation](https://tldp.org/LDP/abs/html/abs-guide.html#BROWNIAN)


9-14. [Random between values](https://tldp.org/LDP/abs/html/abs-guide.html#RANDOMBETWEEN)


9-15. [Rolling a single die with RANDOM](https://tldp.org/LDP/abs/html/abs-guide.html#RANDOMTEST)


9-16. [Reseeding RANDOM](https://tldp.org/LDP/abs/html/abs-guide.html#SEEDINGRANDOM)


9-17. [Pseudorandom numbers, using ](https://tldp.org/LDP/abs/html/abs-guide.html#RANDOM2)[awk](https://tldp.org/LDP/abs/html/abs-guide.html#AWKREF)


10-1. [Inserting a blank line between paragraphs in a text file](https://tldp.org/LDP/abs/html/abs-guide.html#PARAGRAPHSPACE)


10-2. [Generating an 8-character "random" string](https://tldp.org/LDP/abs/html/abs-guide.html#RANDSTRING)


10-3. [Converting graphic file formats, with filename change](https://tldp.org/LDP/abs/html/abs-guide.html#CVT)


10-4. [Converting streaming audio files to _ogg_](https://tldp.org/LDP/abs/html/abs-guide.html#RA2OGG)


10-5. [Emulating _getopt_](https://tldp.org/LDP/abs/html/abs-guide.html#GETOPTSIMPLE)


10-6. [Alternate ways of extracting and locating substrings](https://tldp.org/LDP/abs/html/abs-guide.html#SUBSTRINGEX)


10-7. [Using parameter substitution and error messages](https://tldp.org/LDP/abs/html/abs-guide.html#EX6)


10-8. [Parameter substitution and "usage" messages](https://tldp.org/LDP/abs/html/abs-guide.html#USAGEMESSAGE)


10-9. [Length of a variable](https://tldp.org/LDP/abs/html/abs-guide.html#LENGTH)


10-10. [Pattern matching in parameter substitution](https://tldp.org/LDP/abs/html/abs-guide.html#PATTMATCHING)


10-11. [Renaming file extensions:](https://tldp.org/LDP/abs/html/abs-guide.html#RFE)


10-12. [Using pattern matching to parse arbitrary strings](https://tldp.org/LDP/abs/html/abs-guide.html#EX7)


10-13. [Matching patterns at prefix or suffix of string](https://tldp.org/LDP/abs/html/abs-guide.html#VARMATCH)


11-1. [Simple _for_ loops](https://tldp.org/LDP/abs/html/abs-guide.html#EX22)


11-2. [_for_ loop with two parameters in each [list] element](https://tldp.org/LDP/abs/html/abs-guide.html#EX22A)


11-3. [_Fileinfo:_ operating on a file list contained in a variable](https://tldp.org/LDP/abs/html/abs-guide.html#FILEINFO)


11-4. [Operating on a parameterized file list](https://tldp.org/LDP/abs/html/abs-guide.html#FILEINFO01)


11-5. [Operating on files with a _for_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#LISTGLOB)


11-6. [Missing `**in [list]**` in a _for_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#EX23)


11-7. [Generating the `**[list]**` in a _for_ loop with command substitution](https://tldp.org/LDP/abs/html/abs-guide.html#FORLOOPCMD)


11-8. [A _grep_ replacement for binary files](https://tldp.org/LDP/abs/html/abs-guide.html#BINGREP)


11-9. [Listing all users on the system](https://tldp.org/LDP/abs/html/abs-guide.html#USERLIST)


11-10. [Checking all the binaries in a directory for authorship](https://tldp.org/LDP/abs/html/abs-guide.html#FINDSTRING)


11-11. [Listing the _symbolic links_ in a directory](https://tldp.org/LDP/abs/html/abs-guide.html#SYMLINKS)


11-12. [Symbolic links in a directory, saved to a file](https://tldp.org/LDP/abs/html/abs-guide.html#SYMLINKS2)


11-13. [A C-style _for_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#FORLOOPC)


11-14. [Using _efax_ in batch mode](https://tldp.org/LDP/abs/html/abs-guide.html#EX24)


11-15. [Simple _while_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#EX25)


11-16. [Another _while_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#EX26)


11-17. [_while_ loop with multiple conditions](https://tldp.org/LDP/abs/html/abs-guide.html#EX26A)


11-18. [C-style syntax in a _while_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#WHLOOPC)


11-19. [_until_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#EX27)


11-20. [Nested Loop](https://tldp.org/LDP/abs/html/abs-guide.html#NESTEDLOOP)


11-21. [Effects of _break_ and **continue** in a loop](https://tldp.org/LDP/abs/html/abs-guide.html#EX28)


11-22. [Breaking out of multiple loop levels](https://tldp.org/LDP/abs/html/abs-guide.html#BREAKLEVELS)


11-23. [Continuing at a higher loop level](https://tldp.org/LDP/abs/html/abs-guide.html#CONTINUELEVELS)


11-24. [Using _continue N_ in an actual task](https://tldp.org/LDP/abs/html/abs-guide.html#CONTINUENEX)


11-25. [Using _case_](https://tldp.org/LDP/abs/html/abs-guide.html#EX29)


11-26. [Creating menus using _case_](https://tldp.org/LDP/abs/html/abs-guide.html#EX30)


11-27. [Using _command substitution_ to generate the _case_ variable](https://tldp.org/LDP/abs/html/abs-guide.html#CASECMD)


11-28. [Simple string matching](https://tldp.org/LDP/abs/html/abs-guide.html#MATCHSTRING)


11-29. [Checking for alphabetic input](https://tldp.org/LDP/abs/html/abs-guide.html#ISALPHA)


11-30. [Creating menus using _select_](https://tldp.org/LDP/abs/html/abs-guide.html#EX31)


11-31. [Creating menus using _select_ in a function](https://tldp.org/LDP/abs/html/abs-guide.html#EX32)


12-1. [Stupid script tricks](https://tldp.org/LDP/abs/html/abs-guide.html#STUPSCR)


12-2. [Generating a variable from a loop](https://tldp.org/LDP/abs/html/abs-guide.html#CSUBLOOP)


12-3. [Finding anagrams](https://tldp.org/LDP/abs/html/abs-guide.html#AGRAM2)


15-1. [A script that spawns multiple instances of itself](https://tldp.org/LDP/abs/html/abs-guide.html#SPAWNSCR)


15-2. [_printf_ in action](https://tldp.org/LDP/abs/html/abs-guide.html#EX47)


15-3. [Variable assignment, using _read_](https://tldp.org/LDP/abs/html/abs-guide.html#EX36)


15-4. [What happens when _read_ has no variable](https://tldp.org/LDP/abs/html/abs-guide.html#READNOVAR)


15-5. [Multi-line input to _read_](https://tldp.org/LDP/abs/html/abs-guide.html#READR)


15-6. [Detecting the arrow keys](https://tldp.org/LDP/abs/html/abs-guide.html#ARROWDETECT)


15-7. [Using _read_ with ](https://tldp.org/LDP/abs/html/abs-guide.html#READREDIR)[file redirection](https://tldp.org/LDP/abs/html/abs-guide.html#IOREDIRREF)


15-8. [Problems reading from a pipe](https://tldp.org/LDP/abs/html/abs-guide.html#READPIPE)


15-9. [Changing the current working directory](https://tldp.org/LDP/abs/html/abs-guide.html#EX37)


15-10. [Letting _let_ do arithmetic.](https://tldp.org/LDP/abs/html/abs-guide.html#EX46)


15-11. [Showing the effect of _eval_](https://tldp.org/LDP/abs/html/abs-guide.html#EX43)


15-12. [Using _eval_ to select among variables](https://tldp.org/LDP/abs/html/abs-guide.html#ARRCHOICE)


15-13. [_Echoing_ the _command-line parameters_](https://tldp.org/LDP/abs/html/abs-guide.html#ECHOPARAMS)


15-14. [Forcing a log-off](https://tldp.org/LDP/abs/html/abs-guide.html#EX44)


15-15. [A version of _rot13_](https://tldp.org/LDP/abs/html/abs-guide.html#ROT14)


15-16. [Using _set_ with positional parameters](https://tldp.org/LDP/abs/html/abs-guide.html#EX34)


15-17. [Reversing the positional parameters](https://tldp.org/LDP/abs/html/abs-guide.html#REVPOSPARAMS)


15-18. [Reassigning the positional parameters](https://tldp.org/LDP/abs/html/abs-guide.html#SETPOS)


15-19. ["Unsetting" a variable](https://tldp.org/LDP/abs/html/abs-guide.html#UNS)


15-20. [Using _export_ to pass a variable to an embedded _awk_ script](https://tldp.org/LDP/abs/html/abs-guide.html#COLTOTALER3)


15-21. [Using _getopts_ to read the options/arguments passed to a script](https://tldp.org/LDP/abs/html/abs-guide.html#EX33)


15-22. ["Including" a data file](https://tldp.org/LDP/abs/html/abs-guide.html#EX38)


15-23. [A (useless) script that sources itself](https://tldp.org/LDP/abs/html/abs-guide.html#SELFSOURCE)


15-24. [Effects of _exec_](https://tldp.org/LDP/abs/html/abs-guide.html#EX54)


15-25. [A script that _exec's_ itself](https://tldp.org/LDP/abs/html/abs-guide.html#SELFEXEC)


15-26. [Waiting for a process to finish before proceeding](https://tldp.org/LDP/abs/html/abs-guide.html#EX39)


15-27. [A script that kills itself](https://tldp.org/LDP/abs/html/abs-guide.html#SELFDESTRUCT)


16-1. [Using _ls_ to create a table of contents for burning a CDR disk](https://tldp.org/LDP/abs/html/abs-guide.html#EX40)


16-2. [Hello or Good-bye](https://tldp.org/LDP/abs/html/abs-guide.html#HELLOL)


16-3. [_Badname_ , eliminate file names in current directory containing bad characters and ](https://tldp.org/LDP/abs/html/abs-guide.html#EX57)[whitespace](https://tldp.org/LDP/abs/html/abs-guide.html#WHITESPACEREF).


16-4. [Deleting a file by its _inode_ number](https://tldp.org/LDP/abs/html/abs-guide.html#IDELETE)


16-5. [Logfile: Using _xargs_ to monitor system log](https://tldp.org/LDP/abs/html/abs-guide.html#EX41)


16-6. [Copying files in current directory to another](https://tldp.org/LDP/abs/html/abs-guide.html#EX42)


16-7. [Killing processes by name](https://tldp.org/LDP/abs/html/abs-guide.html#KILLBYNAME)


16-8. [Word frequency analysis using _xargs_](https://tldp.org/LDP/abs/html/abs-guide.html#WF2)


16-9. [Using _expr_](https://tldp.org/LDP/abs/html/abs-guide.html#EX45)


16-10. [Using _date_](https://tldp.org/LDP/abs/html/abs-guide.html#EX51)


16-11. [_Date_ calculations](https://tldp.org/LDP/abs/html/abs-guide.html#DATECALC)


16-12. [Word Frequency Analysis](https://tldp.org/LDP/abs/html/abs-guide.html#WF)


16-13. [Which files are scripts?](https://tldp.org/LDP/abs/html/abs-guide.html#SCRIPTDETECTOR)


16-14. [Generating 10-digit random numbers](https://tldp.org/LDP/abs/html/abs-guide.html#RND)


16-15. [Using _tail_ to monitor the system log](https://tldp.org/LDP/abs/html/abs-guide.html#EX12)


16-16. [Printing out the _From_ lines in stored e-mail messages](https://tldp.org/LDP/abs/html/abs-guide.html#FROMSH)


16-17. [Emulating _grep_ in a script](https://tldp.org/LDP/abs/html/abs-guide.html#GRP)


16-18. [Crossword puzzle solver](https://tldp.org/LDP/abs/html/abs-guide.html#CWSOLVER)


16-19. [Looking up definitions in Webster's 1913 Dictionary](https://tldp.org/LDP/abs/html/abs-guide.html#DICTLOOKUP)


16-20. [Checking words in a list for validity](https://tldp.org/LDP/abs/html/abs-guide.html#LOOKUP)


16-21. [_toupper_ : Transforms a file to all uppercase.](https://tldp.org/LDP/abs/html/abs-guide.html#EX49)


16-22. [_lowercase_ : Changes all filenames in working directory to lowercase.](https://tldp.org/LDP/abs/html/abs-guide.html#LOWERCASE)


16-23. [_du_ : DOS to UNIX text file conversion.](https://tldp.org/LDP/abs/html/abs-guide.html#DU)


16-24. [_rot13_ : ultra-weak encryption.](https://tldp.org/LDP/abs/html/abs-guide.html#ROT13)


16-25. [Generating "Crypto-Quote" Puzzles](https://tldp.org/LDP/abs/html/abs-guide.html#CRYPTOQUOTE)


16-26. [Formatted file listing.](https://tldp.org/LDP/abs/html/abs-guide.html#EX50)


16-27. [Using _column_ to format a directory listing](https://tldp.org/LDP/abs/html/abs-guide.html#COL)


16-28. [_nl_ : A self-numbering script.](https://tldp.org/LDP/abs/html/abs-guide.html#LNUM)


16-29. [_manview_ : Viewing formatted manpages](https://tldp.org/LDP/abs/html/abs-guide.html#MANVIEW)


16-30. [Using _cpio_ to move a directory tree](https://tldp.org/LDP/abs/html/abs-guide.html#EX48)


16-31. [Unpacking an _rpm_ archive](https://tldp.org/LDP/abs/html/abs-guide.html#DERPM)


16-32. [Stripping comments from C program files](https://tldp.org/LDP/abs/html/abs-guide.html#STRIPC)


16-33. [Exploring `/usr/X11R6/bin`](https://tldp.org/LDP/abs/html/abs-guide.html#WHAT)


16-34. [An "improved" _strings_ command](https://tldp.org/LDP/abs/html/abs-guide.html#WSTRINGS)


16-35. [Using _cmp_ to compare two files within a script.](https://tldp.org/LDP/abs/html/abs-guide.html#FILECOMP)


16-36. [_basename_ and _dirname_](https://tldp.org/LDP/abs/html/abs-guide.html#EX35)


16-37. [A script that copies itself in sections](https://tldp.org/LDP/abs/html/abs-guide.html#SPLITCOPY)


16-38. [Checking file integrity](https://tldp.org/LDP/abs/html/abs-guide.html#FILEINTEGRITY)


16-39. [Uudecoding encoded files](https://tldp.org/LDP/abs/html/abs-guide.html#EX52)


16-40. [Finding out where to report a spammer](https://tldp.org/LDP/abs/html/abs-guide.html#SPAMLOOKUP)


16-41. [Analyzing a spam domain](https://tldp.org/LDP/abs/html/abs-guide.html#ISSPAMMER)


16-42. [Getting a stock quote](https://tldp.org/LDP/abs/html/abs-guide.html#QUOTEFETCH)


16-43. [Updating FC4](https://tldp.org/LDP/abs/html/abs-guide.html#FC4UPD)


16-44. [Using _ssh_](https://tldp.org/LDP/abs/html/abs-guide.html#REMOTE)


16-45. [A script that mails itself](https://tldp.org/LDP/abs/html/abs-guide.html#SELFMAILER)


16-46. [Generating prime numbers](https://tldp.org/LDP/abs/html/abs-guide.html#PRIMES2)


16-47. [Monthly Payment on a Mortgage](https://tldp.org/LDP/abs/html/abs-guide.html#MONTHLYPMT)


16-48. [Base Conversion](https://tldp.org/LDP/abs/html/abs-guide.html#BASE)


16-49. [Invoking _bc_ using a _here document_](https://tldp.org/LDP/abs/html/abs-guide.html#ALTBC)


16-50. [Calculating PI](https://tldp.org/LDP/abs/html/abs-guide.html#CANNON)


16-51. [Converting a decimal number to hexadecimal](https://tldp.org/LDP/abs/html/abs-guide.html#HEXCONVERT)


16-52. [Factoring](https://tldp.org/LDP/abs/html/abs-guide.html#FACTR)


16-53. [Calculating the hypotenuse of a triangle](https://tldp.org/LDP/abs/html/abs-guide.html#HYPOT)


16-54. [Using _seq_ to generate loop arguments](https://tldp.org/LDP/abs/html/abs-guide.html#EX53)


16-55. [Letter Count"](https://tldp.org/LDP/abs/html/abs-guide.html#LETTERCOUNT)


16-56. [Using _getopt_ to parse command-line options](https://tldp.org/LDP/abs/html/abs-guide.html#EX33A)


16-57. [A script that copies itself](https://tldp.org/LDP/abs/html/abs-guide.html#SELFCOPY)


16-58. [Exercising _dd_](https://tldp.org/LDP/abs/html/abs-guide.html#EXERCISINGDD)


16-59. [Capturing Keystrokes](https://tldp.org/LDP/abs/html/abs-guide.html#DDKEYPRESS)


16-60. [Preparing a bootable SD card for the _Raspberry Pi_](https://tldp.org/LDP/abs/html/abs-guide.html#RPSDCARD)


16-61. [Securely deleting a file](https://tldp.org/LDP/abs/html/abs-guide.html#BLOTOUT)


16-62. [Filename generator](https://tldp.org/LDP/abs/html/abs-guide.html#TEMPFILENAME)


16-63. [Converting meters to miles](https://tldp.org/LDP/abs/html/abs-guide.html#UNITCONVERSION)


16-64. [Using _m4_](https://tldp.org/LDP/abs/html/abs-guide.html#M4)


17-1. [Setting a new password](https://tldp.org/LDP/abs/html/abs-guide.html#SETNEWPW)


17-2. [Setting an _erase_ character](https://tldp.org/LDP/abs/html/abs-guide.html#ERASE)


17-3. [_secret password_ : Turning off terminal echoing](https://tldp.org/LDP/abs/html/abs-guide.html#SECRETPW)


17-4. [Keypress detection](https://tldp.org/LDP/abs/html/abs-guide.html#KEYPRESS)


17-5. [Checking a remote server for _identd_](https://tldp.org/LDP/abs/html/abs-guide.html#ISCAN)


17-6. [_pidof_ helps kill a process](https://tldp.org/LDP/abs/html/abs-guide.html#KILLPROCESS)


17-7. [Checking a CD image](https://tldp.org/LDP/abs/html/abs-guide.html#ISOMOUNTREF)


17-8. [Creating a filesystem in a file](https://tldp.org/LDP/abs/html/abs-guide.html#CREATEFS)


17-9. [Adding a new hard drive](https://tldp.org/LDP/abs/html/abs-guide.html#ADDDRV)


17-10. [Using _umask_ to hide an output file from prying eyes](https://tldp.org/LDP/abs/html/abs-guide.html#ROT13A)


17-11. [_Backlight_ : changes the brightness of the (laptop) screen backlight](https://tldp.org/LDP/abs/html/abs-guide.html#BACKLIGHT)


17-12. [_killall_ , from `/etc/rc.d/init.d`](https://tldp.org/LDP/abs/html/abs-guide.html#EX55)


19-1. [_broadcast_ : Sends message to everyone logged in](https://tldp.org/LDP/abs/html/abs-guide.html#EX70)


19-2. [_dummyfile_ : Creates a 2-line dummy file](https://tldp.org/LDP/abs/html/abs-guide.html#EX69)


19-3. [Multi-line message using _cat_](https://tldp.org/LDP/abs/html/abs-guide.html#EX71)


19-4. [Multi-line message, with tabs suppressed](https://tldp.org/LDP/abs/html/abs-guide.html#EX71A)


19-5. [Here document with replaceable parameters](https://tldp.org/LDP/abs/html/abs-guide.html#EX71B)


19-6. [Upload a file pair to _Sunsite_ incoming directory](https://tldp.org/LDP/abs/html/abs-guide.html#EX72)


19-7. [Parameter substitution turned off](https://tldp.org/LDP/abs/html/abs-guide.html#EX71C)


19-8. [A script that generates another script](https://tldp.org/LDP/abs/html/abs-guide.html#GENERATESCRIPT)


19-9. [Here documents and functions](https://tldp.org/LDP/abs/html/abs-guide.html#HF)


19-10. ["Anonymous" Here Document](https://tldp.org/LDP/abs/html/abs-guide.html#ANONHEREDOC)


19-11. [Commenting out a block of code](https://tldp.org/LDP/abs/html/abs-guide.html#COMMENTBLOCK)


19-12. [A self-documenting script](https://tldp.org/LDP/abs/html/abs-guide.html#SELFDOCUMENT)


19-13. [Prepending a line to a file](https://tldp.org/LDP/abs/html/abs-guide.html#PREPENDEX)


19-14. [Parsing a mailbox](https://tldp.org/LDP/abs/html/abs-guide.html#MAILBOXGREP)


20-1. [Redirecting `stdin` using _exec_](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR1)


20-2. [Redirecting `stdout` using _exec_](https://tldp.org/LDP/abs/html/abs-guide.html#REASSIGNSTDOUT)


20-3. [Redirecting both `stdin` and `stdout` in the same script with _exec_](https://tldp.org/LDP/abs/html/abs-guide.html#UPPERCONV)


20-4. [Avoiding a subshell](https://tldp.org/LDP/abs/html/abs-guide.html#AVOIDSUBSHELL)


20-5. [Redirected _while_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR2)


20-6. [Alternate form of redirected _while_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR2A)


20-7. [Redirected _until_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR3)


20-8. [Redirected _for_ loop](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR4)


20-9. [Redirected _for_ loop (both `stdin` and `stdout` redirected)](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR4A)


20-10. [Redirected _if/then_ test](https://tldp.org/LDP/abs/html/abs-guide.html#REDIR5)


20-11. [Data file _names.data_ for above examples](https://tldp.org/LDP/abs/html/abs-guide.html#NAMESDATA)


20-12. [Logging events](https://tldp.org/LDP/abs/html/abs-guide.html#LOGEVENTS)


21-1. [Variable scope in a subshell](https://tldp.org/LDP/abs/html/abs-guide.html#SUBSHELL)


21-2. [List User Profiles](https://tldp.org/LDP/abs/html/abs-guide.html#ALLPROFS)


21-3. [Running parallel processes in subshells](https://tldp.org/LDP/abs/html/abs-guide.html#PARALLEL-PROCESSES)


22-1. [Running a script in restricted mode](https://tldp.org/LDP/abs/html/abs-guide.html#RESTRICTED)


23-1. [Code block redirection without forking](https://tldp.org/LDP/abs/html/abs-guide.html#WRPS)


23-2. [Redirecting the output of _process substitution_ into a loop.](https://tldp.org/LDP/abs/html/abs-guide.html#PSUBP)


24-1. [Simple functions](https://tldp.org/LDP/abs/html/abs-guide.html#EX59)


24-2. [Function Taking Parameters](https://tldp.org/LDP/abs/html/abs-guide.html#EX60)


24-3. [Functions and command-line args passed to the script](https://tldp.org/LDP/abs/html/abs-guide.html#FUNCCMDLINEARG)


24-4. [Passing an indirect reference to a function](https://tldp.org/LDP/abs/html/abs-guide.html#INDFUNC)


24-5. [Dereferencing a parameter passed to a function](https://tldp.org/LDP/abs/html/abs-guide.html#DEREFERENCECL)


24-6. [Again, dereferencing a parameter passed to a function](https://tldp.org/LDP/abs/html/abs-guide.html#REFPARAMS)


24-7. [Maximum of two numbers](https://tldp.org/LDP/abs/html/abs-guide.html#MAX)


24-8. [Converting numbers to Roman numerals](https://tldp.org/LDP/abs/html/abs-guide.html#EX61)


24-9. [Testing large return values in a function](https://tldp.org/LDP/abs/html/abs-guide.html#RETURNTEST)


24-10. [Comparing two large integers](https://tldp.org/LDP/abs/html/abs-guide.html#MAX2)


24-11. [Real name from username](https://tldp.org/LDP/abs/html/abs-guide.html#REALNAME)


24-12. [Local variable visibility](https://tldp.org/LDP/abs/html/abs-guide.html#EX62)


24-13. [Demonstration of a simple recursive function](https://tldp.org/LDP/abs/html/abs-guide.html#RECURSIONDEMO)


24-14. [Another simple demonstration](https://tldp.org/LDP/abs/html/abs-guide.html#RECURSIONDEMO2)


24-15. [Recursion, using a local variable](https://tldp.org/LDP/abs/html/abs-guide.html#EX63)


24-16. [_The Fibonacci Sequence_](https://tldp.org/LDP/abs/html/abs-guide.html#FIBO)


24-17. [_The Towers of Hanoi_](https://tldp.org/LDP/abs/html/abs-guide.html#HANOI)


25-1. [Aliases within a script](https://tldp.org/LDP/abs/html/abs-guide.html#AL)


25-2. [_unalias_ : Setting and unsetting an alias](https://tldp.org/LDP/abs/html/abs-guide.html#UNAL)


26-1. [Using an _and list_ to test for command-line arguments](https://tldp.org/LDP/abs/html/abs-guide.html#EX64)


26-2. [Another command-line arg test using an _and list_](https://tldp.org/LDP/abs/html/abs-guide.html#ANDLIST2)


26-3. [Using _or lists_ in combination with an _and list_](https://tldp.org/LDP/abs/html/abs-guide.html#EX65)


27-1. [Simple array usage](https://tldp.org/LDP/abs/html/abs-guide.html#EX66)


27-2. [Formatting a poem](https://tldp.org/LDP/abs/html/abs-guide.html#POEM)


27-3. [Various array operations](https://tldp.org/LDP/abs/html/abs-guide.html#ARRAYOPS)


27-4. [String operations on arrays](https://tldp.org/LDP/abs/html/abs-guide.html#ARRAYSTROPS)


27-5. [Loading the contents of a script into an array](https://tldp.org/LDP/abs/html/abs-guide.html#SCRIPTARRAY)


27-6. [Some special properties of arrays](https://tldp.org/LDP/abs/html/abs-guide.html#EX67)


27-7. [Of empty arrays and empty elements](https://tldp.org/LDP/abs/html/abs-guide.html#EMPTYARRAY)


27-8. [Initializing arrays](https://tldp.org/LDP/abs/html/abs-guide.html#ARRAYASSIGN)


27-9. [Copying and concatenating arrays](https://tldp.org/LDP/abs/html/abs-guide.html#COPYARRAY)


27-10. [More on concatenating arrays](https://tldp.org/LDP/abs/html/abs-guide.html#ARRAYAPPEND)


27-11. [The Bubble Sort](https://tldp.org/LDP/abs/html/abs-guide.html#BUBBLE)


27-12. [Embedded arrays and indirect references](https://tldp.org/LDP/abs/html/abs-guide.html#EMBARR)


27-13. [The Sieve of Eratosthenes](https://tldp.org/LDP/abs/html/abs-guide.html#EX68)


27-14. [The Sieve of Eratosthenes, Optimized](https://tldp.org/LDP/abs/html/abs-guide.html#EX68A)


27-15. [Emulating a push-down stack](https://tldp.org/LDP/abs/html/abs-guide.html#STACKEX)


27-16. [Complex array application: _Exploring a weird mathematical series_](https://tldp.org/LDP/abs/html/abs-guide.html#QFUNCTION)


27-17. [Simulating a two-dimensional array, then tilting it](https://tldp.org/LDP/abs/html/abs-guide.html#TWODIM)


28-1. [Indirect Variable References](https://tldp.org/LDP/abs/html/abs-guide.html#INDREF)


28-2. [Passing an indirect reference to _awk_](https://tldp.org/LDP/abs/html/abs-guide.html#COLTOTALER2)


29-1. [Using `/dev/tcp` for troubleshooting](https://tldp.org/LDP/abs/html/abs-guide.html#DEVTCP)


29-2. [Playing music](https://tldp.org/LDP/abs/html/abs-guide.html#MUSICSCR)


29-3. [Finding the process associated with a PID](https://tldp.org/LDP/abs/html/abs-guide.html#PIDID)


29-4. [On-line connect status](https://tldp.org/LDP/abs/html/abs-guide.html#CONSTAT)


30-1. [Print the server environment](https://tldp.org/LDP/abs/html/abs-guide.html#TESTCGI)


30-2. [IP addresses](https://tldp.org/LDP/abs/html/abs-guide.html#IPADDRESSES)


31-1. [Hiding the cookie jar](https://tldp.org/LDP/abs/html/abs-guide.html#COOKIES)


31-2. [Setting up a swapfile using `/dev/zero`](https://tldp.org/LDP/abs/html/abs-guide.html#EX73)


31-3. [Creating a ramdisk](https://tldp.org/LDP/abs/html/abs-guide.html#RAMDISK)


32-1. [A buggy script](https://tldp.org/LDP/abs/html/abs-guide.html#EX74)


32-2. [Missing ](https://tldp.org/LDP/abs/html/abs-guide.html#MISSINGKEYWORD)[keyword](https://tldp.org/LDP/abs/html/abs-guide.html#KEYWORDREF)


32-3. [_test24_ : another buggy script](https://tldp.org/LDP/abs/html/abs-guide.html#EX75)


32-4. [Testing a condition with an _assert_](https://tldp.org/LDP/abs/html/abs-guide.html#ASSERT)


32-5. [Trapping at exit](https://tldp.org/LDP/abs/html/abs-guide.html#EX76)


32-6. [Cleaning up after **Control-C**](https://tldp.org/LDP/abs/html/abs-guide.html#ONLINE)


32-7. [A Simple Implementation of a Progress Bar](https://tldp.org/LDP/abs/html/abs-guide.html#PROGRESSBAR2)


32-8. [Tracing a variable](https://tldp.org/LDP/abs/html/abs-guide.html#VARTRACE)


32-9. [Running multiple processes (on an SMP box)](https://tldp.org/LDP/abs/html/abs-guide.html#MULTIPLEPROC)


34-1. [Numerical and string comparison are not equivalent](https://tldp.org/LDP/abs/html/abs-guide.html#BADOP)


34-2. [Subshell Pitfalls](https://tldp.org/LDP/abs/html/abs-guide.html#SUBPIT)


34-3. [Piping the output of _echo_ to a _read_](https://tldp.org/LDP/abs/html/abs-guide.html#BADREAD)


36-1. [_shell wrapper_](https://tldp.org/LDP/abs/html/abs-guide.html#EX3)


36-2. [A slightly more complex _shell wrapper_](https://tldp.org/LDP/abs/html/abs-guide.html#EX4)


36-3. [A generic _shell wrapper_ that writes to a logfile](https://tldp.org/LDP/abs/html/abs-guide.html#LOGGINGWRAPPER)


36-4. [A _shell wrapper_ around an awk script](https://tldp.org/LDP/abs/html/abs-guide.html#PRASC)


36-5. [A _shell wrapper_ around another awk script](https://tldp.org/LDP/abs/html/abs-guide.html#COLTOTALER)


36-6. [Perl embedded in a _Bash_ script](https://tldp.org/LDP/abs/html/abs-guide.html#EX56)


36-7. [Bash and Perl scripts combined](https://tldp.org/LDP/abs/html/abs-guide.html#BASHANDPERL)


36-8. [Python embedded in a _Bash_ script](https://tldp.org/LDP/abs/html/abs-guide.html#EX56PY)


36-9. [A script that speaks](https://tldp.org/LDP/abs/html/abs-guide.html#SPEECH0)


36-10. [A (useless) script that recursively calls itself](https://tldp.org/LDP/abs/html/abs-guide.html#RECURSE)


36-11. [A (useful) script that recursively calls itself](https://tldp.org/LDP/abs/html/abs-guide.html#PBOOK)


36-12. [Another (useful) script that recursively calls itself](https://tldp.org/LDP/abs/html/abs-guide.html#USRMNT)


36-13. [A "colorized" address database](https://tldp.org/LDP/abs/html/abs-guide.html#EX30A)


36-14. [Drawing a box](https://tldp.org/LDP/abs/html/abs-guide.html#DRAW-BOX)


36-15. [Echoing colored text](https://tldp.org/LDP/abs/html/abs-guide.html#COLORECHO)


36-16. [A "horserace" game](https://tldp.org/LDP/abs/html/abs-guide.html#HORSERACE)


36-17. [A Progress Bar](https://tldp.org/LDP/abs/html/abs-guide.html#PROGRESSBAR)


36-18. [Return value trickery](https://tldp.org/LDP/abs/html/abs-guide.html#MULTIPLICATION)


36-19. [Even more return value trickery](https://tldp.org/LDP/abs/html/abs-guide.html#SUMPRODUCT)


36-20. [Passing and returning arrays](https://tldp.org/LDP/abs/html/abs-guide.html#ARRFUNC)


36-21. [Fun with anagrams](https://tldp.org/LDP/abs/html/abs-guide.html#AGRAM)


36-22. [Widgets invoked from a shell script](https://tldp.org/LDP/abs/html/abs-guide.html#DIALOG)


36-23. [Test Suite](https://tldp.org/LDP/abs/html/abs-guide.html#TESTSUITE)


37-1. [String expansion](https://tldp.org/LDP/abs/html/abs-guide.html#EX77)


37-2. [Indirect variable references - the new way](https://tldp.org/LDP/abs/html/abs-guide.html#EX78)


37-3. [Simple database application, using indirect variable referencing](https://tldp.org/LDP/abs/html/abs-guide.html#RESISTOR)


37-4. [Using arrays and other miscellaneous trickery to deal four random hands from a deck of cards](https://tldp.org/LDP/abs/html/abs-guide.html#CARDS)


37-5. [A simple address database](https://tldp.org/LDP/abs/html/abs-guide.html#FETCHADDRESS)


37-6. [A somewhat more elaborate address database](https://tldp.org/LDP/abs/html/abs-guide.html#FETCHADDRESS2)


37-7. [Testing characters](https://tldp.org/LDP/abs/html/abs-guide.html#CASE4)


37-8. [Reading N characters](https://tldp.org/LDP/abs/html/abs-guide.html#READN)


37-9. [Using a _here document_ to set a variable](https://tldp.org/LDP/abs/html/abs-guide.html#HERECOMMSUB)


37-10. [Piping input to a ](https://tldp.org/LDP/abs/html/abs-guide.html#LASTPIPEOPT)[read](https://tldp.org/LDP/abs/html/abs-guide.html#READREF)


37-11. [Negative array indices](https://tldp.org/LDP/abs/html/abs-guide.html#NEGARRAY)


37-12. [Negative parameter in string-extraction construct](https://tldp.org/LDP/abs/html/abs-guide.html#NEGOFFSET)


A-1. [_mailformat_ : Formatting an e-mail message](https://tldp.org/LDP/abs/html/abs-guide.html#MAILFORMAT)


A-2. [_rn_ : A simple-minded file renaming utility](https://tldp.org/LDP/abs/html/abs-guide.html#RN)


A-3. [_blank-rename_ : Renames filenames containing blanks](https://tldp.org/LDP/abs/html/abs-guide.html#BLANKRENAME)


A-4. [_encryptedpw_ : Uploading to an ftp site, using a locally encrypted password](https://tldp.org/LDP/abs/html/abs-guide.html#ENCRYPTEDPW)


A-5. [_copy-cd_ : Copying a data CD](https://tldp.org/LDP/abs/html/abs-guide.html#COPYCD)


A-6. [Collatz series](https://tldp.org/LDP/abs/html/abs-guide.html#COLLATZ)


A-7. [_days-between_ : Days between two dates](https://tldp.org/LDP/abs/html/abs-guide.html#DAYSBETWEEN)


A-8. [Making a _dictionary_](https://tldp.org/LDP/abs/html/abs-guide.html#MAKEDICT)


A-9. [Soundex conversion](https://tldp.org/LDP/abs/html/abs-guide.html#SOUNDEX)


A-10. [_Game of Life_](https://tldp.org/LDP/abs/html/abs-guide.html#LIFESLOW)


A-11. [Data file for _Game of Life_](https://tldp.org/LDP/abs/html/abs-guide.html#GEN0DATA)


A-12. [_behead_ : Removing mail and news message headers](https://tldp.org/LDP/abs/html/abs-guide.html#BEHEAD)


A-13. [_password_ : Generating random 8-character passwords](https://tldp.org/LDP/abs/html/abs-guide.html#PW)


A-14. [_fifo_ : Making daily backups, using named pipes](https://tldp.org/LDP/abs/html/abs-guide.html#FIFO)


A-15. [Generating prime numbers using the modulo operator](https://tldp.org/LDP/abs/html/abs-guide.html#PRIMES)


A-16. [_tree_ : Displaying a directory tree](https://tldp.org/LDP/abs/html/abs-guide.html#TREE)


A-17. [_tree2_ : Alternate directory tree script](https://tldp.org/LDP/abs/html/abs-guide.html#TREE2)


A-18. [_string functions_ : C-style string functions](https://tldp.org/LDP/abs/html/abs-guide.html#STRING)


A-19. [Directory information](https://tldp.org/LDP/abs/html/abs-guide.html#DIRECTORYINFO)


A-20. [Library of hash functions](https://tldp.org/LDP/abs/html/abs-guide.html#HASHLIB)


A-21. [Colorizing text using hash functions](https://tldp.org/LDP/abs/html/abs-guide.html#HASHEXAMPLE)


A-22. [More on hash functions](https://tldp.org/LDP/abs/html/abs-guide.html#HASHEX2)


A-23. [Mounting USB keychain storage devices](https://tldp.org/LDP/abs/html/abs-guide.html#USBINST)


A-24. [Converting to HTML](https://tldp.org/LDP/abs/html/abs-guide.html#TOHTML)


A-25. [Preserving weblogs](https://tldp.org/LDP/abs/html/abs-guide.html#ARCHIVWEBLOGS)


A-26. [Protecting literal strings](https://tldp.org/LDP/abs/html/abs-guide.html#PROTECTLITERAL)


A-27. [Unprotecting literal strings](https://tldp.org/LDP/abs/html/abs-guide.html#UNPROTECTLITERAL)


A-28. [Spammer Identification](https://tldp.org/LDP/abs/html/abs-guide.html#ISSPAMMER2)


A-29. [Spammer Hunt](https://tldp.org/LDP/abs/html/abs-guide.html#WHX)


A-30. [Making _wget_ easier to use](https://tldp.org/LDP/abs/html/abs-guide.html#WGETTER2)


A-31. [A _podcasting_ script](https://tldp.org/LDP/abs/html/abs-guide.html#BASHPODDER)


A-32. [Nightly backup to a firewire HD](https://tldp.org/LDP/abs/html/abs-guide.html#NIGHTLYBACKUP)


A-33. [An expanded _cd_ command](https://tldp.org/LDP/abs/html/abs-guide.html#CDLL)


A-34. [A soundcard setup script](https://tldp.org/LDP/abs/html/abs-guide.html#SOUNDCARDON)


A-35. [Locating split paragraphs in a text file](https://tldp.org/LDP/abs/html/abs-guide.html#FINDSPLIT)


A-36. [Insertion sort](https://tldp.org/LDP/abs/html/abs-guide.html#INSERTIONSORT)


A-37. [Standard Deviation](https://tldp.org/LDP/abs/html/abs-guide.html#STDDEV)


A-38. [A _pad_ file generator for shareware authors](https://tldp.org/LDP/abs/html/abs-guide.html#PADSW)


A-39. [A _man page_ editor](https://tldp.org/LDP/abs/html/abs-guide.html#MANED)


A-40. [Petals Around the Rose](https://tldp.org/LDP/abs/html/abs-guide.html#PETALS)


A-41. [Quacky: a Perquackey-type word game](https://tldp.org/LDP/abs/html/abs-guide.html#QKY)


A-42. [Nim](https://tldp.org/LDP/abs/html/abs-guide.html#NIM)


A-43. [A command-line stopwatch](https://tldp.org/LDP/abs/html/abs-guide.html#STOPWATCH)


A-44. [An all-purpose shell scripting homework assignment solution](https://tldp.org/LDP/abs/html/abs-guide.html#HOMEWORK)


A-45. [The Knight's Tour](https://tldp.org/LDP/abs/html/abs-guide.html#KTOUR)


A-46. [Magic Squares](https://tldp.org/LDP/abs/html/abs-guide.html#MSQUARE)


A-47. [Fifteen Puzzle](https://tldp.org/LDP/abs/html/abs-guide.html#FIFTEEN)


A-48. [_The Towers of Hanoi, graphic version_](https://tldp.org/LDP/abs/html/abs-guide.html#HANOI2)


A-49. [_The Towers of Hanoi, alternate graphic version_](https://tldp.org/LDP/abs/html/abs-guide.html#HANOI2A)


A-50. [An alternate version of the ](https://tldp.org/LDP/abs/html/abs-guide.html#USEGETOPT)[getopt-simple.sh](https://tldp.org/LDP/abs/html/abs-guide.html#GETOPTSIMPLE) script


A-51. [The version of the _UseGetOpt.sh_ example used in the ](https://tldp.org/LDP/abs/html/abs-guide.html#USEGETOPT2)[Tab Expansion appendix](https://tldp.org/LDP/abs/html/abs-guide.html#TABEXPANSION)


A-52. [Cycling through all the possible color backgrounds](https://tldp.org/LDP/abs/html/abs-guide.html#SHOWALLC)


A-53. [Morse Code Practice](https://tldp.org/LDP/abs/html/abs-guide.html#SAMORSE)


A-54. [Base64 encoding/decoding](https://tldp.org/LDP/abs/html/abs-guide.html#BASE64)


A-55. [Inserting text in a file using _sed_](https://tldp.org/LDP/abs/html/abs-guide.html#SEDAPPEND)


A-56. [The Gronsfeld Cipher](https://tldp.org/LDP/abs/html/abs-guide.html#GRONSFELD)


A-57. [Bingo Number Generator](https://tldp.org/LDP/abs/html/abs-guide.html#BINGO)


A-58. [Basics Reviewed](https://tldp.org/LDP/abs/html/abs-guide.html#BASICSREVIEWED)


A-59. [Testing execution times of various commands](https://tldp.org/LDP/abs/html/abs-guide.html#TESTEXECTIME)


A-60. [Associative arrays vs. conventional arrays (execution times)](https://tldp.org/LDP/abs/html/abs-guide.html#ASSOCARRTEST)


C-1. [Counting Letter Occurrences](https://tldp.org/LDP/abs/html/abs-guide.html#LETTERCOUNT2)


J-1. [Completion script for _UseGetOpt.sh_](https://tldp.org/LDP/abs/html/abs-guide.html#USEGETOPTEX)


M-1. [Sample `.bashrc` file](https://tldp.org/LDP/abs/html/abs-guide.html#BASHRC)


M-2. [`.bash_profile` file](https://tldp.org/LDP/abs/html/abs-guide.html#BASHPROF)


N-1. [VIEWDATA.BAT: DOS Batch File](https://tldp.org/LDP/abs/html/abs-guide.html#VIEWDAT)


N-2. [_viewdata.sh_ : Shell Script Conversion of VIEWDATA.BAT](https://tldp.org/LDP/abs/html/abs-guide.html#VIEWDATA)


T-1. [A script that generates an ASCII table](https://tldp.org/LDP/abs/html/abs-guide.html#ASCIISH)


T-2. [Another ASCII table script](https://tldp.org/LDP/abs/html/abs-guide.html#ASCII2SH)


T-3. [A third ASCII table script, using _awk_](https://tldp.org/LDP/abs/html/abs-guide.html#ASCII3SH)
