#  Chapter 1. Introduction
This document is an attempt to summarise the many command-line based tools available to a GNU/Linux based operating system. This guide is not a complete listing (I doubt it's possible to document all available programs), this document lists many tools which are available to GNU/Linux systems and which are, or can be useful to the majority of users.
Each tool description provides a quick overview of it's function and some useful options for that individual tool.
The tools listed that require a GUI, usually the X windowing system, are those listed in the Graphics Tools section. All other tools are completely command-line-based and do not require a GUI to run.
If you are looking for information on GUI based tools you will need to look elsewhere.
Also note that a few of the tools in this guide are bash (the Bourne-Again-SHell) specific, tools specific to other shells are not listed in this document.
For some of the tools that are harder to use, or perform a more complex task, there are several mini-tutorials (or mini-guides; [Chapter 20](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MINI-GUIDES)) within this document.
Where a mini-guide was considered unnecessary, detailed descriptions that explain in detail how a particular tool works, and some examples of how to use it are provided.
Please note that the word “tool” is used interchangeably with the word “command”, both have the same meaning (at least in this guide). For a more detailed explanation, read about the UNIX Tools Philosophy here: [Chapter 3](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#THE-UNIX-TOOLS-PHILOSOPHY) or visit the links in the appendix, [Section A.2.2.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#UNIX-TOOLS-FURTHER-READING).
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **To find out which tools are bash specific**
---|---
|  To find out which tools are bash specific you can type:  | ```
enable -a
```

---
* * *
#  1.1. Who would want to read this guide?
Anyone who is interested in learning about the tools (also known as commands) available to them when using their GNU/Linux based operating system.
Why would you want to learn how to use the command-line (and available tools)? The _C_ ommand _L_ ine _-I_ nterface (CLI), while difficult to learn, is the quickest and most efficient way to use a computer for many different tasks. The CLI is the normal method of use for most UNIX system administrators, programmers and some power users. While a GUI is better suited to some tasks, many operations are best suited to the CLI.
The major motivation behind learning the GNU/Linux CLI is the authors idea that, with software in general, the more time spent learning something equals less time spent performing that particular task _(authors opinion only)_.
This guide is aimed at beginners to intermediate users who want to learn about the command-line tools available to them. Advanced users may wish to use it as a command reference, however this document aims to list commands of interest, as judged by the authors opinion, it is not designed to be completely comprehensive, see the appendix, [Section A.2.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#GENERAL-FURTHER-READING) for further information. Or if you are not looking for a command reference guide, but a more gentle introduction to GNU/Linux you may be interested in the [Introduction to Linux guide](http://www.tldp.org/LDP/intro-linux/html/) authored by Machtelt Garrels.
This guide could also be considered a summarised version of the Linux Cookbook. If you are looking for a book with more detailed descriptions of each tool have a look at the
* * *
#  1.2. Who would not want to read this guide?
Anyone who is not interested in the command-line, or anyone looking for a detailed reference to all available GNU/Linux tools should look elsewhere. This is only a summary, while it does list many commands, it's not a complete listing (I don't think it's possible to make a complete listing anyway).
This document would not be of interest to those who already have an expert knowledge of the command-line interface and do require any reference information. Or those readers who require detailed lists of options for each command, the man pages are better suited to this purpose.
* * *
#  1.3. Availability of sources
The modifiable sources of the original book (in english), are available in LyX format (LyX Document Processor) or Machine-translated SGML (SGML markup language).
LyX is a completely free document processor based on LaTeX, downloadable from
See for the modifiable sources of this document. These are the official versions. We (the translators and current maintainers) plan to continue work on this document and add new chapters and enhancements. If you want to see the version we are currently working on (the "bleeding edge" version), check the
* * *
#  1.4. Conventions used in this guide
The following conventions are used within this guide:

italic

Anything appearing in italic, _like�this_ is either an executable command or emphasized text. Tools (executable commands) are in italics to prevent confusion. Some tools have names which are real english words, such as the “locate” tool.

key�combinations

Are represented by using a '-' (dash sign) in-between the key(s), which must be used in combination. All combinations are also printed in italics to improve clarity. For example **CTRL** -**Z** means hold down the _Control key_ and press the _z_ _key._

admonitions

Admonitions are little pictures used to emphasize something of importance to the reader.
The five types used are:
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **This is a note**
---|---
|  Notes often give important information about a tool.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **This is a tip**
---|---
|  This will offer a useful switch or useful way to use a tool.
![Important](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/important.gif) | **This is something important**
---|---
| This is something that is considered very important. Consider it like a note with extra importance, they are usually there to save the reader time.
![Caution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/caution.gif) | **This is a caution**
---|---
|  This will inform you of something that you be careful about (because it could be harmful to your system).
![Warning](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/warning.gif) | **This is a warning**
---|---
|  This will inform you of something that you shouldn't do (because it probably will break something within your system).

code�examples

Code examples are shown for most commands.
Below is an example of what code looks like:
```
Hello World, I'm a code example. :)
```

---

command�syntax

(or a similar phrase) simply shows how you would normally use the command. Often real examples are used instead of explaining the command syntax.
The phrase “ Command syntax” is always followed by the way you would type a command in a shell.
The standard syntax for any tool is usually:
```
command -options file
```

---
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Note**
---|---
| Note that some tools do not accept options.

wildcards

Also note that most commands, even when not explicitly stated, will work with standard wildcards (or globbing patterns) such as *, [A-Z] and various other standard wildcards. Refer to [Section 20.4.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#STANDARD-WILDCARDS) for further information.

access�keys

Access keys enable navigation through the document, without relying on a mouse. The following keys have been given special meaning in this document:

P

Previous page.

N

Next page.

H

Home of the document (Table of Contents).

U

Up (takes you one level up the section hierarchy).
If you also happen to be reading the document from its original location, then the following access keys can also be used:

S

Start (takes you to the author's start page).

T

The current (“This”) page, without the Sitemenu on the left.

M

The current page in a frameset, where the left frame contains a Menu.
To use the access keys, you have to simultaneously press a modifier key, which may vary from browser to browser. For example in NN6+/Mozilla, the modifier key is **ALT** , so you have to use **ALT** -**N** to go to the next page, and **ALT** -**P** to come back. In other browsers such as IE6, the access keys just give focus to the associated link, so the sequence becomes **ALT** -**N** **Enter** . Try it, you'll like it!
Inline graphic
* * *
#  1.5. Resources used to create this document
To create the GNU/Linux Command-Line Tools Summary, I used
You may also want to check out the
I also had assistance from various [The Linux Documentation Project](http://www.tldp.org) volunteers (see the contributors section [Section 1.7](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONTRIBUTORS) for specific details).
* * *
#  1.6. Feedback
Feedback is necessary for the advancement of this guide. Positive, constructive criticism is encouraged. If you have ideas, suggestions, advice, or problems with this guide, please send an email to the author
![Important](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/important.gif) | **Contributions**
---|---
|  If you wish to make contributions it is recommended (if possible) to read the LyX file(s) for this document. They contain various notes which you can't see in the other versions. These notes highlight the areas that need contributions, certain tools which I cannot understand, tools which have not been added, or tools which were removed. These notes also explain some of the structure of this document.
* * *
#  1.7. Contributors
As you may be able to see, parts of this guide are based off various advice columns on GNU/Linux, anything that has being directly quoted from an article can be found in the references, [_Bibliography_](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#REFERENCES), section of this document.
The following is a list of people who have made a significant contribution to this document, in a rough chronological order.
Chris allowed the use of his lyxtox scripts to convert the LyX file of the document to working DocBook SGML output (to learn how to use the lyxtox scripts yourself, see
  * Chris provided useful suggestions and advice, and added an index listing for many of the commands.
  * Chris is also responsible for the great looking HTML file for this document (the CSS file and HTML customisations are completely his work).
  * Chris has also helped fix up problems in the document (many times), especially with docbook/sgml, and LyX related issues.
  * Chris has also improved the structure of the document by adding labels and fixing minor errors.



William�West:

William provided a thorough review of the document as required by the [Linux Documentation Project](http://www.tldp.org). He is responsible for a variety of improvements to the quality of this document.
His contributions include:
  * Improvements to the readability of this document.
  * Improvements to the structure and consistency of this document.
  * Various grammar improvements throughout the document.
  * Repair of some minor technical errors.


Tabatha, as the [Linux Documentation Project](http://www.tldp.org) Review Coordinator (at the time) also gave a brief review of this document. Her general advice was used to improve the structure, language and grammar of the document.
Rahul provided a brief review of this document for the [Linux Documentation Project](http://www.tldp.org). Advice from his brief review was integrated into this document to improve readability and structure, several references were added as recommended by Rahul.
David's criticism of the document (via the TLDP discuss list) were listened to, and attempts to improve the document were made. A number of his criticisms were addressed and improved.

George�Harmon:

George provided a second language review. His detailed review of the material allowed me to improve the general grammar of the document and some minor errors.
Machtelt provided tips in regard to referencing the correct LDP documents from this guide. As well as general advice on improvements to the guide.

Michael�Kerrisk:

Michael pointed out a number of technical errors in the document after his brief review on behalf of the TLDP during posts to the discussion list.
* * *
#  Chapter 2. Legal
The legal chapter provides information about the disclaimer that applies to the entire document and the licensing information.
* * *
#  2.1. Disclaimer
No liability for the contents of this document can be accepted. Use the concepts, examples and other content at your own risk. There may be errors and inaccuracies, that may of course be damaging to your system. Although this is highly unlikely, you should proceed with caution. The author does not accept any responsibility for any damage incurred.
All copyrights are held by their respective owners, unless specifically noted otherwise. Use of a term in this document should not be regarded as affecting the validity of any trademark or service mark.
Naming of particular products or brands should not be seen as endorsements.
UNIX is a registered trademark of The Open Group.
* * *
#  2.2. License
Copyright � 2003 - 2006 Gareth Anderson. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license can be found in the section called the GNU Free Documentation License or at the
* * *
#  Chapter 3. The Unix Tools Philosophy
A tool is a simple program, usually designed for a specific purpose, it is sometimes referred to (at least throughout this document) as a command.
The “ Unix tools philosophy” emerged during the creation of the UNIX operating system, after the breakthrough invention of the pipe '|' (refer to [Chapter 6](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DIRECTING-INPUT-OUPUT) for information on using the pipe).
The pipe allowed the output of one program to be sent to the input of another. The tools philosophy was to have small programs to accomplish a particular task instead of trying to develop large monolithic programs to do a large number of tasks. To accomplish more complex tasks, tools would simply be connected together, using pipes.
All the core UNIX system tools were designed so that they could operate together. The original text-based editors (and even TeX and LaTeX) use ASCII (the American text encoding standard; an open standard) and you can use tools such as; _sed_ , _awk_ , _vi_ , _grep_ , _cat_ , _more_ , _tr_ and various other text-based tools in conjunction with these editors.
Using this philosophy programmers avoided writing a program (within their larger program) that had already been written by someone else (this could be considered a form of code recycling). For example, command-line spell checkers are used by a number of different applications instead of having each application create its own own spell checker.
This philosophy lives on today in GNU/Linux and various other UNIX system-based operating systems (FreeBSD, NetBSD, OpenBSD, etc.).
For further information (articles) on the UNIX tools philosophy please see the further reading section, here: [Section A.2.2.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#UNIX-TOOLS-FURTHER-READING)
* * *
#  Chapter 4. Shell Tips
The shell tips chapter provides handy tricks that you may wish to use when you are using a GNU/Linux shell (the command-line interface). This information includes handy shortcut key combinations, the shell's command history and information on virtual terminals.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **If you can't boot into your system**
---|---
|  If your having problems booting into your system you may like to use a shell so you can boot into your system and attempt to fix things up again. To do this you need to pass the “init=/bin/sh” to your system before you boot up. If you don't know how to do this please see [Chapter 14](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SECURITY), the technique is the same except this time you pass "init=bin/sh" rather than "single".
* * *
#  4.1. General Shell Tips

Automatic�Command�Completion

Use the TAB key and bash will attempt to complete the command for you automatically. You can use it to complete command (tool) names. You can also use it when working with the file-system, when changing directories, copying files et cetera.
There are also other lesser known ways to use automatic command completion (for example completing user names):[[1]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN1248)

**ESC** -**Y** �(Y:�special�character)

testing autoindexing Will attempt to complete the command name for you. If it fails it will either list the possible completions (if they exist). If there are none it will simply beep (and/or) flash the screen.

**CTRL** -**X** -**Y** �(Y:�special�character)

Lists the possible completions (it won't attempt to complete it for you) or beep if there are no possible completions.
Special-characters:
Use the following special characters combined with either **ESC** -**Y** or **CTRL** -**X** -**Y** , where Y is some special characters. For example **ESC** -**$** or **CTRL** -**X** -**$** to complete an environment variable name.
  * ~ (tilde) complete a user name
  * @ (at sign) complete a machine name
  * $ (dollars sign) complete an environment variable name
  * ! (exclamation mark) a magic character for completing a command name or a file name. The ! special character has the same function as the TAB key. It works in some other situations; for example when completing man page names.



alias

The _alias_ command will list your current aliases. You can use _unalias_ to remove the alias (to disable it just for one command add a “\” (back-slash) before the command)...
An alias allows one command to be substituted for another. This is used to make a command do something else or to automatically add certain options. This can be either be done during one session using the alias command (see below) or the information can be added to the _.bashrc_ file (found in the users home directory).
Below is an example of what an alias section (within your _.bashrc_ file) might look like:
```
