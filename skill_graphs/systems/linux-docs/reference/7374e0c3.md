#  Punctuation

**$BASH environment variable**

Expands to the full pathname used to invoke this instance of bash. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$BASH_VERSION environment variable**

Expands to the version number of this instance of bash. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$CDPATH environment variable**

The search path for the cd command. This is a colon-separated list of directories in which the shell looks for destination directories specified by the cd command. A sample value is ``.:~:/usr''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$ENV environment variable**

If this parameter is set when bash is executing a shell script, its value is interpreted as a filename containing commands to initialize the shell, as in .bashrc. The value of ENV is subjected to parameter expansion, command substitution, and arithmetic expansion before being interpreted as a pathname. PATH is not used to search for the resultant pathname. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$FIGNORE environment variable**

A colon-separated list of suffixes to ignore when performing filename completion (see READLINE below). A filename whose suffix matches one of the entries in FIGNORE is excluded from the list of matched filenames. A sample value is ``.o:~''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HISTCMD environment variable**

The history number, or index in the history list, of the current command. If HISTCMD is unset, it loses its special properties, even if it is subsequently reset. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HISTCONTROL environment variable**

If set to a value of ignorespace, lines which begin with a space character are not entered on the history list. If set to a value of ignoredups, lines matching the last history line are not entered. A value of ignoreboth combines the two options. If unset, or if set to any other value than those above, all lines read by the parser are saved on the history list. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HISTFILE environment variable**

The name of the file in which command history is saved. (See HISTORY below.) The default value is ~/.bash_history. If unset, the command history is not saved when an interactive shell exits. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HISTFILESIZE environment variable**

The maximum number of lines contained in the history file. When this variable is assigned a value, the history file is truncated, if necessary, to contain no more than that number of lines. The default value is 500. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HISTSIZE environment variable**

The number of commands to remember in the command history (see HISTORY below). The default value is 500. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HOME environment variable**

The home directory of the current user; the default argument for the cd builtin command. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HOSTFILE**

Contains the name of a file in the same format as /etc/hosts that should be read when the shell needs to complete a hostname. The file may be changed interactively; the next time hostname completion is attempted bash adds the contents of the new file to the already existing database. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$HOSTTYPE**

Automatically set to a string that uniquely describes the type of machine on which bash is executing. The default is system-dependent. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$IFS**

In UNIX, the $IFS variable separates commands. It is usually configured to be the semicolon (;) and newline characters. However, it can be reconfigured to be other characters as well. Data-driven attacks will sometimes seek to reset the IFS variable (e.g. IFS=x), then cause execution within the data field without having to insert shell metacharacters. Tidbit: On Linux, the $FF variable may also be used like $IFS. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$IFS**

The Internal Field Separator that is used for word splitting after expansion and to split lines into words with the read builtin command. The default value is ``<space><tab><newline>''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$IGNOREEOF**

Controls the action of the shell on receipt of an EOF character as the sole input. If set, the value is the number of consecutive EOF characters typed as the first characters on an input line before bash exits. If the variable exists but does not have a numeric value, or has no value, the default value is 10. If it does not exist, EOF signifies the end of input to the shell. This is only in effect for interactive shells. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$INPUTRC environment variable**

The filename for the readline startup file, overriding the default of ~/.inputrc (see READLINE below). From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$LINENO**

Each time this parameter is referenced, the shell substitutes a decimal number representing the current sequential line number (starting with 1) within a script or function. When not in a script or function, the value substituted is not guaranteed to be meaningful. When in a function, the value is not the number of the source line that the command appears on (that information has been lost by the time the function is executed), but is an approximation of the number of simple commands executed in the current function. If LINENO is unset, it loses its special properties, even if it is subsequently reset. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$MAIL**

If this parameter is set to a filename and the MAILPATH variable is not set, bash informs the user of the arrival of mail in the specified file. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$MAILCHECK**

Specifies how often (in seconds) bash checks for mail. The default is 60 seconds. When it is time to check for mail, the shell does so before prompting. If this variable is unset, the shell disables mail checking. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$MAILPATH**

A colon-separated list of pathnames to be checked for mail. The message to be printed may be specified by separating the pathname from the message with a `?'. $_ stands for the name of the current mailfile. Example: MAILPATH='/usr/spool/mail/bfox?"You have mail":~/shell-mail?"$_ has mail!"' Bash supplies a default value for this variable, but the location of the user mail files that it uses is system dependent (e.g., /usr/spool/mail/$USER). From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$MAIL_WARNING**

If set, and a file that bash is checking for mail has been accessed since the last time it was checked, the message ``The mail in mailfile has been read'' is printed. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$OLDPWD**

The previous working directory as set by the cd command. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$OSTYPE**

Automatically set to a string that describes the operating system on which bash is executing. The default is system-dependent. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PATH**

The search path for commands. It is a colon-separated list of directories in which the shell looks for commands (see COMMAND EXECUTION below). The default path is system-dependent, and is set by the administrator who installs bash. A common value is ``/usr/gnu/bin:/usr/local/bin:/usr/ucb:/bin:/usr/bin:.''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PATH**

The shell looks for commands and programs in a list of file paths stored in the PATH environment variable. An environment variable stores information in a place where other programs and commands can access it. Environment variables store information such as the shell that you are using, your login name, and your current working directory. To see a list of all the environment variables currently defined; type 'set' at the prompt. When you type a command at the shell prompt, the shell will look for that command's program file in each directory listed in the PATH variable, in order. The first program found matching the command you typed will be run. If the command's program file is not in a directory listed in you PATH environment variable, the shell returns a "commands not found" error. By default, the shell does not look in your current working directory or your home directory for commands This is really a security mechanism so that you don't execute programs by accident. What if a malicious user put a harmful program called ls in your home directory? If you typed ls and the shell looked for the fake program in your home directory before the real program in the /bin directory, what do you think woul dhappen? If you thought bad things, you are on the right track. Since your PATH doesn't have the current directory as one of its search locations, programs in your current directory must be called with an absolute path of a relative path specified as './program-name'. To see what directories are part of your PATH enter this command: # echo $PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11 From Complete-Idiot's Guide to Linux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PROMPT_COMMAND**

If set, the value is executed as a command prior to issuing each primary prompt. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PS1**

The value of this parameter is expanded (see PROMPTING below) and used as the primary prompt string. The default value is ``bash\$ ''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PS2**

The value of this parameter is expanded and used as the secondary prompt string. The default is ``> ''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PS3**

The value of this parameter is used as the prompt for the select command (see SHELL GRAMMAR above). From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PS4**

The value of this parameter is expanded and the value is printed before each command bash displays during an execution trace. The first character of PS4 is replicated multiple times, as necessary, to indicate multiple levels of indirection. The default is ``+ ''. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$PWD**

The current working directory as set by the cd command. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$RANDOM**

Each time this parameter is referenced, a random integer is generated. The sequence of random numbers may be initialized by assigning a value to RANDOM. If RANDOM is unset, it loses its special properties, even if it is subsequently reset. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$SECONDS**

Each time this parameter is referenced, the number of seconds since shell invocation is returned. If a value is assigned to SECONDS. the value returned upon subsequent references is the number of seconds since the assignment plus the value assigned. If SECONDS is unset, it loses its special properties, even if it is subsequently reset. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**$SHLVL**

Incremented by one each time an instance of bash is started. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.#01**

and higher A method of numbering picture files for a roll of film that has been scanned for computer presentation From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.$$$**

Used by OS/2 to keep track of archived files From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.(Pagis)**

native format From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.000**

Data file (GEOWorks) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.000-20009**

Used to number old (backup) versions of files (for example, CONFIG.SYS when changed by an installation program); also used to number From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.001-999**

Database index files used by (Superbase) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.1-STEP**

Backup file (Iomega Backup) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.113**

Backup data file (Iomega Backup) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.123**

Lotus 123 97 file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.12M**

Smartmaster file (Lotus 1-2-3 '97) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.1ST**

Documenting wizard list (Microsoft Visual FoxPro) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.2D**

Two-dimensional drawing file (VersaCAD) (http://www.versacad.com/vcadhome.htm) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.2GR**

and 3GR VGA Graphics driver/configuration files (Microsoft Windows) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.386**

A file for use in an 80386 or higher microprocessor From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.3D**

Three-dimensional drawing file (VersaCAD) (http://www.versacad.com/vcadhome.htm) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.3DM**

3D NURBS modeler, (Rhino) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.3DS**

A file in 3D Studio (for DOS) format From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.411**

Data file (Used by digital cameras) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.4GE**

Compiled code (Informix 4GL) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.4GL**

Source code (Informix 4GL) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.4V**

Music file (Quartet) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.669**

Music mod file (Composer 669)(Unis Composer) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.669**

Tracker module (Composer 669) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.8**

Source file (Assembly) (Similar to Microsoft Assembler) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.@@@**

Screen files used in the installation and instruction on use of such applications as Microsoft Codeview for C From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.a**

Archive. lib*.a is a static library. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A**

Library file (Unix) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A**

Object code library From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A3L**

Authorware 3.x library From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A3M**

Authorware MacIntosh file (unpackaged) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A3W**

Authorware Windows file (unpackaged) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A4L**

Authorware 4.x library From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A4M**

Authorware MacIntosh file (unpackaged) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A4P**

Authorware file (packaged without runtime) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A4W**

Authorware Windows file (unpackaged) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A5L**

Authorware 5.x library From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.A5W**

Authorware Windows file (unpackaged) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AA**

Audible audio file (commonly used for downloadable audio books) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AAM**

Authorware shocked file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AAS**

Authorware shocked packet From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AB**

Applix Builder file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABF**

Adobe Binary Screen Font From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABK**

Backup file (PrintMaster Gold) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABK**

Corel Draw AutoBackup From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABM**

Audio album file (HitPlayer) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABO**

Applix Builder Turbo file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABS**

MPEG Audio Sound file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABS**

Sometimes used to denote an abstract (as in an abstract or summary of a scientific paper) AutoBackup From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ABS**

Standard GNU compiler output file for a PC platform From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACA**

HTTP animation file (Microsoft Agent) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACA**

Project Manager Workbench file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACB**

ACBM Graphic image From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACC**

DR-DOS Viewmax file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACD**

Character definition file (Microsoft Agent) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACE**

ACE Archiver Compression <http://searchStorage.techtarget.com/sDefinition/0,,sid5_gci211828,00.html> file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACF**

HTTP character file (Microsoft Agent) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACPI**

ACPI development appraisal (ACIWEB) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACL**

Corel Draw 6 keyboard accelerator file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACM**

Dynamic Link Library (DLL) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACM**

Interplay compressed sound file (Fallout 1,2, Baulder's Gate) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACM**

Windows system directory file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACP**

Microsoft Office Assistant Preview file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACR**

American College of Radiology file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACS**

Character structured storage file (Microsoft Agent) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACT**

Action Presentation From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACT**

Documenting wizard action diagram (Microsoft Visual FoxPro) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACT**

FoxPro Foxdoc Action Diagram From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACT**

Microsoft Office Assistant Actor file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ACV**

Used to Compress and decompress audio data From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AD**

After Dark screensaver From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.Ada**

<http://search390.techtarget.com/sDefinition/0,,sid10_gci211523,00.html> Ada source text file (non-GNAT) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADB**

Ada source text body file (GNAT) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADB**

HP 100LX Organizer Appointment database From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADC**

Scanstudio 16 color Bitmap Graphic file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADD**

OS/2 adapter driver file used in the boot process From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADF**

Amiga <http://WhatIs.techtarget.com/definition/0,,sid9_gci211557,00.html> disk file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADI**

AutoCAD device-independent binary plotter file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADL**

QEMM Mca adaptor description library From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADM**

After Dark MultiModule screensaver (Microsoft) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADM**

Windows NT <http://searchWin2000.techtarget.com/sDefinition/0,,sid1_gci213368,00.html> policy template From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AND**

Lotus 1-2-3 Add-In file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADP**

Astound Dynamite file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADP**

Dynamic Page file (AOLserver) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADP**

FaxWorks Faxmodem setup file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADR**

After Dark Randomizer screensaver From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADR**

Smart Address address book From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADS**

Ada source text specification file (GNAT) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADT**

AdTech Fax file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADT**

HP NewWave datafile for card applications From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADX**

Archetype Designer Document From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADX**

Dynazip Active Delivery script From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADX**

Lotus Approach dBase Index From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.ADZ**

Packed ADF file (Extracts with WinZip) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AE**

Author/Editor file (SoftQuad) From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**.AEP**

ArcExplorer project file From Whatis-Extensions <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
