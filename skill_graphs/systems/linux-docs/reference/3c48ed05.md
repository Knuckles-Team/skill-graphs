#  Bash Guide for Beginners
###  Machtelt Garrels
Garrels BVBA


`<`

Version 1.11 Last updated 20081227 Edition
* * *

**Table of Contents**


[Introduction](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN32)


1. [Why this guide?](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_01)


2. [Who should read this book?](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_02)


3. [New versions, translations and availability](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_03)


4. [Revision History](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_04)


5. [Contributions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_05)


6. [Feedback](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_06)


7. [Copyright information](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_07)


8. [What do you need?](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_08)


9. [Conventions used in this document](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_09)


10. [Organization of this document](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#intro_10)


1. [Bash and Bash scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_01)


1.1. [Common shell programs](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_01)


1.2. [Advantages of the Bourne Again SHell](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_02)


1.3. [Executing commands](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_03)


1.4. [Building blocks](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_04)


1.5. [Developing good scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_05)


1.6. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_06)


1.7. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_01_07)


2. [Writing and debugging scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_02)


2.1. [Creating and running a script](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_02_01)


2.2. [Script basics](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_02_02)


2.3. [Debugging Bash scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_02_03)


2.4. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_02_05)


2.5. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_02_06)


3. [The Bash environment](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_03)


3.1. [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_01)


3.2. [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_02)


3.3. [Quoting characters](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_03)


3.4. [Shell expansion](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_04)


3.5. [Aliases](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_05)


3.6. [More Bash options](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_06)


3.7. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_07)


3.8. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_03_08)


4. [Regular expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_04)


4.1. [Regular expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_04_01)


4.2. [Examples using grep](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_04_02)


4.3. [Pattern matching using Bash features](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_04_03)


4.4. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_04_04)


4.5. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_04_05)


5. [The GNU sed stream editor](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_05)


5.1. [Introduction](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_05_01)


5.2. [Interactive editing](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_05_02)


5.3. [Non-interactive editing](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_05_03)


5.4. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_05_04)


5.5. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_05_05)


6. [The GNU awk programming language](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_06)


6.1. [Getting started with gawk](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_01)


6.2. [The print program](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_02)


6.3. [Gawk variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_03)


6.4. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_04)


6.5. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_06_05)


7. [Conditional statements](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_07)


7.1. [Introduction to if](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_01)


7.2. [More advanced if usage](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_02)


7.3. [Using case statements](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_03)


7.4. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_04)


7.5. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_05)


8. [Writing interactive scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_08)


8.1. [Displaying user messages](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_08_01)


8.2. [Catching user input](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_08_02)


8.3. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_08_03)


8.4. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_08_04)


9. [Repetitive tasks](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_09)


9.1. [The for loop](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_01)


9.2. [The while loop](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_02)


9.3. [The until loop](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_03)


9.4. [I/O redirection and loops](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_04)


9.5. [Break and continue](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_05)


9.6. [Making menus with the select built-in](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_06)


9.7. [The shift built-in](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_07)


9.8. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_08)


9.9. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_09)


10. [More on variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_10)


10.1. [Types of variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_10_01)


10.2. [Array variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_10_02)


10.3. [Operations on variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_10_03)


10.4. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_10_04)


10.5. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_10_05)


11. [Functions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_11)


11.1. [Introduction](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_11_01)


11.2. [Examples of functions in scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_11_02)


11.3. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_11_03)


11.4. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_11_04)


12. [Catching signals](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_12)


12.1. [Signals](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_12_01)


12.2. [Traps](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_12_02)


12.3. [Summary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_12_03)


12.4. [Exercises](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_12_04)


A. [Shell Features](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#app3)


A.1. [Common features](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN7243)


A.2. [Differing features](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN7369)


[Glossary](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#glossary)


[Index](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#glossary)


**List of Tables**


1. [Typographic and usage conventions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#conventions)


1-1. [Overview of programming terms](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_01_01)


2-1. [Overview of set debugging options](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_02_01)


3-1. [Reserved Bourne shell variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_03_01)


3-2. [Reserved Bash variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_03_02)


3-3. [Special bash variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_03_03)


3-4. [Arithmetic operators](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_03_04)


4-1. [Regular expression operators](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#table_04_01)


5-1. [Sed editing commands](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_05_01)


5-2. [Sed options](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_05_02)


6-1. [Formatting characters for gawk](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_06_01)


7-1. [Primary expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_07_01)


7-2. [Combining expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_07_02)


8-1. [Escape sequences used by the echo command](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_08_01)


8-2. [Options to the read built-in](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_08_02)


10-1. [Options to the declare built-in](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_10_01)


12-1. [Control signals in Bash](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_12_01)


12-2. [Common kill signals](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#tab_12_02)


A-1. [Common Shell Features](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN7246)


A-2. [Differing Shell Features](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN7387)


**List of Figures**


1. [Bash Guide for Beginners front cover](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN71)


2-1. [script1.sh](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN1409)


3-1. [Different prompts for different users](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN1878)


6-1. [Fields in awk](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN4111)


7-1. [Testing of a command line argument with if](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN5029)


7-2. [Example using Boolean operators](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#AEN5144)

* * *
