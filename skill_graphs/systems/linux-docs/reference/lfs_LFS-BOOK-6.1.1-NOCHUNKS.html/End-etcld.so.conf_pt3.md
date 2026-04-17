**soelim** |  Reads files and replaces lines of the form _.so file_ by the contents of the mentioned _file_
**tbl** |  Compiles descriptions of tables embedded within troff input files into commands that are understood by **troff**
**tfmtodit** |  Creates a font file for use with **groff -Tdvi**
**troff** |  Is highly compatible with Unix **troff** ; it should usually be invoked using the **groff** command, which will also run preprocessors and post-processors in the appropriate order and with the appropriate options
**zsoelim** |  A link to **soelim**
##  6.28. Sed-4.1.4
The Sed package contains a stream editor.
**Approximate build time:** 0.2 SBU
**Required disk space:** 8.4 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make, and Texinfo
###  6.28.1. Installation of Sed
By default, Sed installs its HTML documentation in `/usr/share/doc`. Alter this to `/usr/share/doc/sed-4.1.4` by applying the following **sed** :
```
`sed -i 's@/doc@&/sed-4.1.4@' doc/Makefile.in`
```

Prepare Sed for compilation:
```
`./configure --prefix=/usr --bindir=/bin`
```

Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the package:
```
`make install`
```

###  6.28.2. Contents of Sed
**Installed program:** sed
###  Short Descriptions
**sed** |  Filters and transforms text files in a single pass
---|---
##  6.29. Flex-2.5.31
The Flex package contains a utility for generating programs that recognize patterns in text.
**Approximate build time:** 0.1 SBU
**Required disk space:** 22.5 MB
**Installation depends on:** Bash, Binutils, Bison, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, M4, Make, and Sed
###  6.29.1. Installation of Flex
Flex contains several known bugs. Fix these with the following patch:
```
`patch -Np1 -i ../flex-2.5.31-debian_fixes-3.patch`
```

The GNU autotools detects that the Flex source code has been modified by the previous patch and tries to update the man page accordingly. This does not work correctly on many systems, and the default page is fine, so make sure it does not get regenerated:
```
`touch doc/flex.1`
```

Prepare Flex for compilation:
```
`./configure --prefix=/usr`
```

Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the package:
```
`make install`
```

There are some packages that expect to find the `lex` library in `/usr/lib`. Create a symlink to account for this:
```
`ln -sv libfl.a /usr/lib/libl.a`
```

A few programs do not know about **flex** yet and try to run its predecessor, **lex**. To support those programs, create a wrapper script named `lex` that calls `flex` in **lex** emulation mode:
```
`cat > /usr/bin/lex << "EOF"
`#!/bin/sh
