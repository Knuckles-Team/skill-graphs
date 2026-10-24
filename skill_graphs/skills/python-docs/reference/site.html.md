[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html)
    * [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize)
    * [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize)
    * [Readline configuration](https://docs.python.org/3/library/site.html#readline-configuration)
    * [Module contents](https://docs.python.org/3/library/site.html#module-contents)
    * [Command-line interface](https://docs.python.org/3/library/site.html#command-line-interface)


#### Previous topic
[`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html "previous chapter")
#### Next topic
[Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=site+%E2%80%94+Site-specific+configuration+hook&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsite.html&pagesource=library%2Fsite.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/custominterp.html "Custom Python Interpreters") |
  * [previous](https://docs.python.org/3/library/annotationlib.html "annotationlib — Functionality for introspecting annotations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html)
  * |
  * Theme  Auto Light Dark |


#  `site` — Site-specific configuration hook[¶](https://docs.python.org/3/library/site.html#module-site "Link to this heading")
**Source code:**
* * *
**This module is automatically imported during initialization.** The automatic import can be suppressed using the interpreter’s [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) option.
Importing this module normally appends site-specific paths to the module search path and adds [callables](https://docs.python.org/3/library/constants.html#site-consts), including [`help()`](https://docs.python.org/3/library/functions.html#help "help") to the built-in namespace. However, Python startup option [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) blocks this and this module can be safely imported with no automatic modifications to the module search path or additions to the builtins. To explicitly trigger the usual site-specific additions, call the [`main()`](https://docs.python.org/3/library/site.html#site.main "site.main") function.
Changed in version 3.3: Importing the module used to trigger paths manipulation even when using [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S).
It starts by constructing up to four directories from a head and a tail part. For the head part, it uses `sys.prefix` and `sys.exec_prefix`; empty heads are skipped. For the tail part, it uses the empty string and then `lib/site-packages` (on Windows) or `lib/python_X.Y[t]_/site-packages`(on Unix and macOS). (The optional suffix “t” indicates the[ free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build), and is appended if `"t"` is present in the [`sys.abiflags`](https://docs.python.org/3/library/sys.html#sys.abiflags "sys.abiflags") constant.) For each of the distinct head-tail combinations, it sees if it refers to an existing directory, and if so, adds it to `sys.path` and also inspects the newly added path for configuration files.
Changed in version 3.5: Support for the “site-python” directory has been removed.
Changed in version 3.13: On Unix, [Free threading](https://docs.python.org/3/glossary.html#term-free-threading) Python installations are identified by the “t” suffix in the version-specific directory name, such as `lib/python3.13t/`.
Changed in version 3.14: `site` is no longer responsible for updating [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") and [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix") on [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments). This is now done during the [path initialization](https://docs.python.org/3/library/sys_path_init.html#sys-path-init). As a result, under sys-path-init-virtual-environments, `sys.prefix` and `sys.exec_prefix` no longer depend on the `site` initialization, and are therefore unaffected by [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S).
When running under a [virtual environment](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments), the `pyvenv.cfg` file in [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") is checked for site-specific configurations. If the `include-system-site-packages` key exists and is set to `true` (case-insensitive), the system-level prefixes will be searched for site-packages, otherwise they won’t.
A path configuration file is a file whose name has the form `_name_.pth`and exists in one of the four directories mentioned above; its contents are additional items (one per line) to be added to`sys.path`. Non-existing items are never added to `sys.path`, and no check is made that the item refers to a directory rather than a file. No item is added to `sys.path` more than once. Blank lines and lines beginning with `#` are skipped. Lines starting with `import` (followed by space or tab) are executed.
Note
An executable line in a `.pth` file is run at every Python startup, regardless of whether a particular module is actually going to be used. Its impact should thus be kept to a minimum. The primary intended purpose of executable lines is to make the corresponding module(s) importable (load 3rd-party import hooks, adjust `PATH` etc). Any other initialization is supposed to be done upon a module’s actual import, if and when it happens. Limiting a code chunk to a single line is a deliberate measure to discourage putting anything more complex here.
Changed in version 3.13: The `.pth` files are now decoded by UTF-8 at first and then by the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding) if it fails.
For example, suppose `sys.prefix` and `sys.exec_prefix` are set to `/usr/local`. The Python X.Y library is then installed in `/usr/local/lib/python_X.Y_`. Suppose this has a subdirectory`/usr/local/lib/python _X.Y_/site-packages`with three subsubdirectories,`foo` , `bar` and `spam`, and two path configuration files, `foo.pth` and `bar.pth`. Assume `foo.pth` contains the following:
```
# foo package configuration

foo
bar
bletch

```

and `bar.pth` contains:
```
# bar package configuration

bar

```

Then the following version-specific directories are added to `sys.path`, in this order:
```
/usr/local/lib/pythonX.Y/site-packages/bar
/usr/local/lib/pythonX.Y/site-packages/foo

```

Note that `bletch` is omitted because it doesn’t exist; the `bar` directory precedes the `foo` directory because `bar.pth` comes alphabetically before `foo.pth`; and `spam` is omitted because it is not mentioned in either path configuration file.
##  `sitecustomize`[¶](https://docs.python.org/3/library/site.html#module-sitecustomize "Link to this heading")
After these path manipulations, an attempt is made to import a module named `sitecustomize`, which can perform arbitrary site-specific customizations. It is typically created by a system administrator in the site-packages directory. If this import fails with an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") or its subclass exception, and the exception’s [`name`](https://docs.python.org/3/library/exceptions.html#ImportError.name "ImportError.name") attribute equals `'sitecustomize'`, it is silently ignored. If Python is started without output streams available, as with `pythonw.exe` on Windows (which is used by default to start IDLE), attempted output from `sitecustomize` is ignored. Any other exception causes a silent and perhaps mysterious failure of the process.
##  `usercustomize`[¶](https://docs.python.org/3/library/site.html#module-usercustomize "Link to this heading")
After this, an attempt is made to import a module named `usercustomize`, which can perform arbitrary user-specific customizations, if [`ENABLE_USER_SITE`](https://docs.python.org/3/library/site.html#site.ENABLE_USER_SITE "site.ENABLE_USER_SITE") is true. This file is intended to be created in the user site-packages directory (see below), which is part of `sys.path` unless disabled by [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s). If this import fails with an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") or its subclass exception, and the exception’s [`name`](https://docs.python.org/3/library/exceptions.html#ImportError.name "ImportError.name") attribute equals `'usercustomize'`, it is silently ignored.
Note that for some non-Unix systems, `sys.prefix` and `sys.exec_prefix` are empty, and the path manipulations are skipped; however the import of [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize "sitecustomize") and `usercustomize` is still attempted.
## Readline configuration[¶](https://docs.python.org/3/library/site.html#readline-configuration "Link to this heading")
On systems that support [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python."), this module will also import and configure the [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") module, if Python is started in [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive) and without the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) option. The default behavior is to enable tab completion and to use `~/.python_history` as the history save file. To disable it, delete (or override) the [`sys.__interactivehook__`](https://docs.python.org/3/library/sys.html#sys.__interactivehook__ "sys.__interactivehook__") attribute in your [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize "sitecustomize") or [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize "usercustomize") module or your [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP) file.
Changed in version 3.4: Activation of rlcompleter and history was made automatic.
## Module contents[¶](https://docs.python.org/3/library/site.html#module-contents "Link to this heading")

site.PREFIXES[¶](https://docs.python.org/3/library/site.html#site.PREFIXES "Link to this definition")

A list of prefixes for site-packages directories.

site.ENABLE_USER_SITE[¶](https://docs.python.org/3/library/site.html#site.ENABLE_USER_SITE "Link to this definition")

Flag showing the status of the user site-packages directory. `True` means that it is enabled and was added to `sys.path`. `False` means that it was disabled by user request (with [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s) or [`PYTHONNOUSERSITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE)). `None` means it was disabled for security reasons (mismatch between user or group id and effective id) or by an administrator.

site.USER_SITE[¶](https://docs.python.org/3/library/site.html#site.USER_SITE "Link to this definition")

Path to the user site-packages for the running Python. Can be `None` if [`getusersitepackages()`](https://docs.python.org/3/library/site.html#site.getusersitepackages "site.getusersitepackages") hasn’t been called yet. Default value is `~/.local/lib/python_X.Y_[t]/site-packages`for UNIX and non-framework macOS builds,`~/Library/Python/_X.Y_/lib/python/site-packages`for macOS framework builds, and` _%APPDATA%_\Python\Python_XY_\site-packages`on Windows. The optional “t” indicates the free-threaded build. This directory is a site directory, which means that`.pth` files in it will be processed.

site.USER_BASE[¶](https://docs.python.org/3/library/site.html#site.USER_BASE "Link to this definition")

Path to the base directory for the user site-packages. Can be `None` if [`getuserbase()`](https://docs.python.org/3/library/site.html#site.getuserbase "site.getuserbase") hasn’t been called yet. Default value is `~/.local` for UNIX and macOS non-framework builds, `~/Library/Python/_X.Y_`for macOS framework builds, and` _%APPDATA%_\Python`for Windows. This value is used to compute the installation directories for scripts, data files, Python modules, etc. for the[ user installation scheme](https://docs.python.org/3/library/sysconfig.html#sysconfig-user-scheme). See also [`PYTHONUSERBASE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUSERBASE).

site.main()[¶](https://docs.python.org/3/library/site.html#site.main "Link to this definition")

Adds all the standard site-specific directories to the module search path. This function is called automatically when this module is imported, unless the Python interpreter was started with the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) flag.
Changed in version 3.3: This function used to be called unconditionally.

site.addsitedir(_sitedir_ , _known_paths =None_)[¶](https://docs.python.org/3/library/site.html#site.addsitedir "Link to this definition")

Add a directory to sys.path and process its `.pth` files. Typically used in [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize "sitecustomize") or [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize "usercustomize") (see above).

site.getsitepackages()[¶](https://docs.python.org/3/library/site.html#site.getsitepackages "Link to this definition")

Return a list containing all global site-packages directories.
Added in version 3.2.

site.getuserbase()[¶](https://docs.python.org/3/library/site.html#site.getuserbase "Link to this definition")

Return the path of the user base directory, [`USER_BASE`](https://docs.python.org/3/library/site.html#site.USER_BASE "site.USER_BASE"). If it is not initialized yet, this function will also set it, respecting [`PYTHONUSERBASE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUSERBASE).
Added in version 3.2.

site.getusersitepackages()[¶](https://docs.python.org/3/library/site.html#site.getusersitepackages "Link to this definition")

Return the path of the user-specific site-packages directory, [`USER_SITE`](https://docs.python.org/3/library/site.html#site.USER_SITE "site.USER_SITE"). If it is not initialized yet, this function will also set it, respecting [`USER_BASE`](https://docs.python.org/3/library/site.html#site.USER_BASE "site.USER_BASE"). To determine if the user-specific site-packages was added to `sys.path` [`ENABLE_USER_SITE`](https://docs.python.org/3/library/site.html#site.ENABLE_USER_SITE "site.ENABLE_USER_SITE") should be used.
Added in version 3.2.
## Command-line interface[¶](https://docs.python.org/3/library/site.html#command-line-interface "Link to this heading")
The `site` module also provides a way to get the user directories from the command line:
Copy```
$ python -m site --user-site
/home/user/.local/lib/python3.11/site-packages

```

If it is called without arguments, it will print the contents of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") on the standard output, followed by the value of [`USER_BASE`](https://docs.python.org/3/library/site.html#site.USER_BASE "site.USER_BASE") and whether the directory exists, then the same thing for [`USER_SITE`](https://docs.python.org/3/library/site.html#site.USER_SITE "site.USER_SITE"), and finally the value of [`ENABLE_USER_SITE`](https://docs.python.org/3/library/site.html#site.ENABLE_USER_SITE "site.ENABLE_USER_SITE").

--user-base[¶](https://docs.python.org/3/library/site.html#cmdoption-site-user-base "Link to this definition")

Print the path to the user base directory.

--user-site[¶](https://docs.python.org/3/library/site.html#cmdoption-site-user-site "Link to this definition")

Print the path to the user site-packages directory.
If both options are given, user base and user site will be printed (always in this order), separated by [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep").
If any option is given, the script will exit with one of these values: `0` if the user site-packages directory is enabled, `1` if it was disabled by the user, `2` if it is disabled for security reasons or by an administrator, and a value greater than 2 if there is an error.
See also
  * [**PEP 370**](https://peps.python.org/pep-0370/) – Per user site-packages directory
  * [The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init) – The initialization of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").


### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html)
    * [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize)
    * [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize)
    * [Readline configuration](https://docs.python.org/3/library/site.html#readline-configuration)
    * [Module contents](https://docs.python.org/3/library/site.html#module-contents)
    * [Command-line interface](https://docs.python.org/3/library/site.html#command-line-interface)


#### Previous topic
[`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html "previous chapter")
#### Next topic
[Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=site+%E2%80%94+Site-specific+configuration+hook&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsite.html&pagesource=library%2Fsite.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/custominterp.html "Custom Python Interpreters") |
  * [previous](https://docs.python.org/3/library/annotationlib.html "annotationlib — Functionality for introspecting annotations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
