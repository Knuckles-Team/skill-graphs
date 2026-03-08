# End /etc/inputrc`
EOF`
```

##  7.9. The Bash Shell Startup Files
The shell program **/bin/bash** (hereafter referred to as “the shell”) uses a collection of startup files to help create an environment to run in. Each file has a specific use and may affect login and interactive environments differently. The files in the `/etc` directory provide global settings. If an equivalent file exists in the home directory, it may override the global settings.
An interactive login shell is started after a successful login, using **/bin/login** , by reading the `/etc/passwd` file. An interactive non-login shell is started at the command-line (e.g., `[prompt]$`**/bin/bash**). A non-interactive shell is usually present when a shell script is running. It is non-interactive because it is processing a script and not waiting for user input between commands.
For more information, see **info bash** under the _Bash Startup Files and Interactive Shells_ section.
The files `/etc/profile` and `~/.bash_profile` are read when the shell is invoked as an interactive login shell.
The base `/etc/profile` below sets some environment variables necessary for native language support. Setting them properly results in:
  * The output of programs translated into the native language
  * Correct classification of characters into letters, digits and other classes. This is necessary for **bash** to properly accept non-ASCII characters in command lines in non-English locales
  * The correct alphabetical sorting order for the country
  * Appropriate default paper size
  * Correct formatting of monetary, time, and date values


This script also sets the `INPUTRC` environment variable that makes Bash and Readline use the `/etc/inputrc` file created earlier.
Replace _`[ll]`_ below with the two-letter code for the desired language (e.g., “en”) and _`[CC]`_ with the two-letter code for the appropriate country (e.g., “GB”). _`[charmap]`_ should be replaced with the canonical charmap for your chosen locale.
The list of all locales supported by Glibc can be obtained by running the following command:
```
`locale -a`
```

Locales can have a number of synonyms, e.g. “ISO-8859-1” is also referred to as “iso8859-1” and “iso88591”. Some applications cannot handle the various synonyms correctly, so it is safest to choose the canonical name for a particular locale. To determine the canonical name, run the following command, where _`[locale name]`_ is the output given by **locale -a** for your preferred locale (“en_GB.iso88591” in our example).
```
`LC_ALL=_`[locale name]`_ locale charmap`
```

For the “en_GB.iso88591” locale, the above command will print:
```
ISO-8859-1
```

This results in a final locale setting of “en_GB.ISO-8859-1”. It is important that the locale found using the heuristic above is tested prior to it being added to the Bash startup files:
```
`LC_ALL=[locale name] locale country
LC_ALL=[locale name] locale language
LC_ALL=[locale name] locale charmap
LC_ALL=[locale name] locale int_curr_symbol
LC_ALL=[locale name] locale int_prefix`
```

The above commands should print the country and language names, the character encoding used by the locale, the local currency and the prefix to dial before the telephone number in order to get into the country. If any of the commands above fail with a message similar to the one shown below, this means that your locale was either not installed in Chapter 6 or is not supported by the default installation of Glibc.
```
`locale: Cannot set LC_* to default locale: No such file or directory`
```

If this happens, you should either install the desired locale using the **localedef** command, or consider choosing a different locale. Further instructions assume that there are no such error messages from Glibc.
Some packages beyond LFS may also lack support for your chosen locale. One example is the X library (part of the X Window System), which outputs the following error message:
```
`Warning: locale not supported by Xlib, locale set to C`
```

Sometimes it is possible to fix this by removing the charmap part of the locale specification, as long as that does not change the character map that Glibc associates with the locale (this can be checked by running the **locale charmap** command in both locales). For example, one would have to change "de_DE.ISO-8859-15@euro" to "de_DE@euro" in order to get this locale recognized by Xlib.
Other packages can also function incorrectly (but may not necessarily display any error messages) if the locale name does not meet their expectations. In those cases, investigating how other Linux distributions support your locale might provide some useful information.
Once the proper locale settings have been determined, create the `/etc/profile` file:
```
`cat > /etc/profile << "EOF"
`# Begin /etc/profile

export LANG=_`[ll]`___`[CC]`_._`[charmap]`_
export INPUTRC=/etc/inputrc
