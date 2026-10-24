[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html)
    * [Basic Example](https://docs.python.org/3/library/zipapp.html#basic-example)
    * [Command-Line Interface](https://docs.python.org/3/library/zipapp.html#command-line-interface)
    * [Python API](https://docs.python.org/3/library/zipapp.html#python-api)
    * [Examples](https://docs.python.org/3/library/zipapp.html#examples)
    * [Specifying the Interpreter](https://docs.python.org/3/library/zipapp.html#specifying-the-interpreter)
    * [Creating Standalone Applications with zipapp](https://docs.python.org/3/library/zipapp.html#creating-standalone-applications-with-zipapp)
      * [Caveats](https://docs.python.org/3/library/zipapp.html#caveats)
    * [The Python Zip Application Archive Format](https://docs.python.org/3/library/zipapp.html#the-python-zip-application-archive-format)


#### Previous topic
[`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html "previous chapter")
#### Next topic
[Python Runtime Services](https://docs.python.org/3/library/python.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zipapp+%E2%80%94+Manage+executable+Python+zip+archives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzipapp.html&pagesource=library%2Fzipapp.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/python.html "Python Runtime Services") |
  * [previous](https://docs.python.org/3/library/venv.html "venv — Creation of virtual environments") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html) »
  * [`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html)
  * |
  * Theme  Auto Light Dark |


#  `zipapp` — Manage executable Python zip archives[¶](https://docs.python.org/3/library/zipapp.html#module-zipapp "Link to this heading")
Added in version 3.5.
**Source code:**
* * *
This module provides tools to manage the creation of zip files containing Python code, which can be [executed directly by the Python interpreter](https://docs.python.org/3/using/cmdline.html#using-on-interface-options). The module provides both a [Command-Line Interface](https://docs.python.org/3/library/zipapp.html#zipapp-command-line-interface) and a [Python API](https://docs.python.org/3/library/zipapp.html#zipapp-python-api).
## Basic Example[¶](https://docs.python.org/3/library/zipapp.html#basic-example "Link to this heading")
The following example shows how the [Command-Line Interface](https://docs.python.org/3/library/zipapp.html#zipapp-command-line-interface) can be used to create an executable archive from a directory containing Python code. When run, the archive will execute the `main` function from the module `myapp` in the archive.
Copy```
$ python -m zipapp myapp -m "myapp:main"
$ python myapp.pyz
<output from myapp>

```

## Command-Line Interface[¶](https://docs.python.org/3/library/zipapp.html#command-line-interface "Link to this heading")
When called as a program from the command line, the following form is used:
Copy```
$ python -m zipapp source [options]

```

If _source_ is a directory, this will create an archive from the contents of _source_. If _source_ is a file, it should be an archive, and it will be copied to the target archive (or the contents of its shebang line will be displayed if the –info option is specified).
The following options are understood:

-o <output>, --output=<output>[¶](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-o "Link to this definition")

Write the output to a file named _output_. If this option is not specified, the output filename will be the same as the input _source_ , with the extension `.pyz` added. If an explicit filename is given, it is used as is (so a `.pyz` extension should be included if required).
An output filename must be specified if the _source_ is an archive (and in that case, _output_ must not be the same as _source_).

-p <interpreter>, --python=<interpreter>[¶](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-p "Link to this definition")

Add a `#!` line to the archive specifying _interpreter_ as the command to run. Also, on POSIX, make the archive executable. The default is to write no `#!` line, and not make the file executable.

-m <mainfn>, --main=<mainfn>[¶](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-m "Link to this definition")

Write a `__main__.py` file to the archive that executes _mainfn_. The _mainfn_ argument should have the form “pkg.mod:fn”, where “pkg.mod” is a package/module in the archive, and “fn” is a callable in the given module. The `__main__.py` file will execute that callable.
[`--main`](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-m) cannot be specified when copying an archive.

-c, --compress[¶](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-c "Link to this definition")

Compress files with the deflate method, reducing the size of the output file. By default, files are stored uncompressed in the archive.
[`--compress`](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-c) has no effect when copying an archive.
Added in version 3.7.

--info[¶](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-info "Link to this definition")

Display the interpreter embedded in the archive, for diagnostic purposes. In this case, any other options are ignored and SOURCE must be an archive, not a directory.

-h, --help[¶](https://docs.python.org/3/library/zipapp.html#cmdoption-zipapp-h "Link to this definition")

Print a short usage message and exit.
## Python API[¶](https://docs.python.org/3/library/zipapp.html#python-api "Link to this heading")
The module defines two convenience functions:

zipapp.create_archive(_source_ , _target =None_, _interpreter =None_, _main =None_, _filter =None_, _compressed =False_)[¶](https://docs.python.org/3/library/zipapp.html#zipapp.create_archive "Link to this definition")

Create an application archive from _source_. The source can be any of the following:
  * The name of a directory, or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) referring to a directory, in which case a new application archive will be created from the content of that directory.
  * The name of an existing application archive file, or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) referring to such a file, in which case the file is copied to the target (modifying it to reflect the value given for the _interpreter_ argument). The file name should include the `.pyz` extension, if required.
  * A file object open for reading in bytes mode. The content of the file should be an application archive, and the file object is assumed to be positioned at the start of the archive.


The _target_ argument determines where the resulting archive will be written:
  * If it is the name of a file, or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object), the archive will be written to that file.
  * If it is an open file object, the archive will be written to that file object, which must be open for writing in bytes mode.
  * If the target is omitted (or `None`), the source must be a directory and the target will be a file with the same name as the source, with a `.pyz` extension added.


The _interpreter_ argument specifies the name of the Python interpreter with which the archive will be executed. It is written as a “shebang” line at the start of the archive. On POSIX, this will be interpreted by the OS, and on Windows it will be handled by the Python launcher. Omitting the _interpreter_ results in no shebang line being written. If an interpreter is specified, and the target is a filename, the executable bit of the target file will be set.
The _main_ argument specifies the name of a callable which will be used as the main program for the archive. It can only be specified if the source is a directory, and the source does not already contain a `__main__.py` file. The _main_ argument should take the form “pkg.module:callable” and the archive will be run by importing “pkg.module” and executing the given callable with no arguments. It is an error to omit _main_ if the source is a directory and does not contain a `__main__.py` file, as otherwise the resulting archive would not be executable.
The optional _filter_ argument specifies a callback function that is passed a Path object representing the path to the file being added (relative to the source directory). It should return `True` if the file is to be added.
The optional _compressed_ argument determines whether files are compressed. If set to `True`, files in the archive are compressed with the deflate method; otherwise, files are stored uncompressed. This argument has no effect when copying an existing archive.
If a file object is specified for _source_ or _target_ , it is the caller’s responsibility to close it after calling create_archive.
When copying an existing archive, file objects supplied only need `read` and `readline`, or `write` methods. When creating an archive from a directory, if the target is a file object it will be passed to the `zipfile.ZipFile` class, and must supply the methods needed by that class.
Changed in version 3.7: Added the _filter_ and _compressed_ parameters.

zipapp.get_interpreter(_archive_)[¶](https://docs.python.org/3/library/zipapp.html#zipapp.get_interpreter "Link to this definition")

Return the interpreter specified in the `#!` line at the start of the archive. If there is no `#!` line, return [`None`](https://docs.python.org/3/library/constants.html#None "None"). The _archive_ argument can be a filename or a file-like object open for reading in bytes mode. It is assumed to be at the start of the archive.
## Examples[¶](https://docs.python.org/3/library/zipapp.html#examples "Link to this heading")
Pack up a directory into an archive, and run it.
Copy```
$ python -m zipapp myapp
$ python myapp.pyz
<output from myapp>

```

The same can be done using the [`create_archive()`](https://docs.python.org/3/library/zipapp.html#zipapp.create_archive "zipapp.create_archive") function:
Copy```
>>> import zipapp
>>> zipapp.create_archive('myapp', 'myapp.pyz')

```

To make the application directly executable on POSIX, specify an interpreter to use.
Copy```
$ python -m zipapp myapp -p "/usr/bin/env python"
$ ./myapp.pyz
<output from myapp>

```

To replace the shebang line on an existing archive, create a modified archive using the [`create_archive()`](https://docs.python.org/3/library/zipapp.html#zipapp.create_archive "zipapp.create_archive") function:
Copy```
>>> import zipapp
>>> zipapp.create_archive('old_archive.pyz', 'new_archive.pyz', '/usr/bin/python3')

```

To update the file in place, do the replacement in memory using a [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object, and then overwrite the source afterwards. Note that there is a risk when overwriting a file in place that an error will result in the loss of the original file. This code does not protect against such errors, but production code should do so. Also, this method will only work if the archive fits in memory:
Copy```
>>> import zipapp
>>> import io
>>> temp = io.BytesIO()
>>> zipapp.create_archive('myapp.pyz', temp, '/usr/bin/python2')
>>> with open('myapp.pyz', 'wb') as f:
>>>     f.write(temp.getvalue())

```

## Specifying the Interpreter[¶](https://docs.python.org/3/library/zipapp.html#specifying-the-interpreter "Link to this heading")
Note that if you specify an interpreter and then distribute your application archive, you need to ensure that the interpreter used is portable. The Python launcher for Windows supports most common forms of POSIX `#!` line, but there are other issues to consider:
  * If you use “/usr/bin/env python” (or other forms of the “python” command, such as “/usr/bin/python”), you need to consider that your users may have either Python 2 or Python 3 as their default, and write your code to work under both versions.
  * If you use an explicit version, for example “/usr/bin/env python3” your application will not work for users who do not have that version. (This may be what you want if you have not made your code Python 2 compatible).
  * There is no way to say “python X.Y or later”, so be careful of using an exact version like “/usr/bin/env python3.4” as you will need to change your shebang line for users of Python 3.5, for example.


Typically, you should use an “/usr/bin/env python2” or “/usr/bin/env python3”, depending on whether your code is written for Python 2 or 3.
## Creating Standalone Applications with zipapp[¶](https://docs.python.org/3/library/zipapp.html#creating-standalone-applications-with-zipapp "Link to this heading")
Using the `zipapp` module, it is possible to create self-contained Python programs, which can be distributed to end users who only need to have a suitable version of Python installed on their system. The key to doing this is to bundle all of the application’s dependencies into the archive, along with the application code.
The steps to create a standalone archive are as follows:
  1. Create your application in a directory as normal, so you have a `myapp` directory containing a `__main__.py` file, and any supporting application code.
  2. Install all of your application’s dependencies into the `myapp` directory, using pip:
Copy```
$ python -m pip install -r requirements.txt --target myapp

```

(this assumes you have your project requirements in a `requirements.txt` file - if not, you can just list the dependencies manually on the pip command line).
  3. Package the application using:
Copy```
$ python -m zipapp -p "interpreter" myapp

```



This will produce a standalone executable, which can be run on any machine with the appropriate interpreter available. See [Specifying the Interpreter](https://docs.python.org/3/library/zipapp.html#zipapp-specifying-the-interpreter) for details. It can be shipped to users as a single file.
On Unix, the `myapp.pyz` file is executable as it stands. You can rename the file to remove the `.pyz` extension if you prefer a “plain” command name. On Windows, the `myapp.pyz[w]` file is executable by virtue of the fact that the Python interpreter registers the `.pyz` and `.pyzw` file extensions when installed.
### Caveats[¶](https://docs.python.org/3/library/zipapp.html#caveats "Link to this heading")
If your application depends on a package that includes a C extension, that package cannot be run from a zip file (this is an OS limitation, as executable code must be present in the filesystem for the OS loader to load it). In this case, you can exclude that dependency from the zipfile, and either require your users to have it installed, or ship it alongside your zipfile and add code to your `__main__.py` to include the directory containing the unzipped module in `sys.path`. In this case, you will need to make sure to ship appropriate binaries for your target architecture(s) (and potentially pick the correct version to add to `sys.path` at runtime, based on the user’s machine).
## The Python Zip Application Archive Format[¶](https://docs.python.org/3/library/zipapp.html#the-python-zip-application-archive-format "Link to this heading")
Python has been able to execute zip files which contain a `__main__.py` file since version 2.6. In order to be executed by Python, an application archive simply has to be a standard zip file containing a `__main__.py` file which will be run as the entry point for the application. As usual for any Python script, the parent of the script (in this case the zip file) will be placed on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") and thus further modules can be imported from the zip file.
The zip file format allows arbitrary data to be prepended to a zip file. The zip application format uses this ability to prepend a standard POSIX “shebang” line to the file (`#!/path/to/interpreter`).
Formally, the Python zip application format is therefore:
  1. An optional shebang line, containing the characters `b'#!'` followed by an interpreter name, and then a newline (`b'\n'`) character. The interpreter name can be anything acceptable to the OS “shebang” processing, or the Python launcher on Windows. The interpreter should be encoded in UTF-8 on Windows, and in [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") on POSIX.
  2. Standard zipfile data, as generated by the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") module. The zipfile content _must_ include a file called `__main__.py` (which must be in the “root” of the zipfile - i.e., it cannot be in a subdirectory). The zipfile data can be compressed or uncompressed.


If an application archive has a shebang line, it may have the executable bit set on POSIX systems, to allow it to be executed directly.
There is no requirement that the tools in this module are used to create application archives - the module is a convenience, but archives in the above format created by any means are acceptable to Python.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html)
    * [Basic Example](https://docs.python.org/3/library/zipapp.html#basic-example)
    * [Command-Line Interface](https://docs.python.org/3/library/zipapp.html#command-line-interface)
    * [Python API](https://docs.python.org/3/library/zipapp.html#python-api)
    * [Examples](https://docs.python.org/3/library/zipapp.html#examples)
    * [Specifying the Interpreter](https://docs.python.org/3/library/zipapp.html#specifying-the-interpreter)
    * [Creating Standalone Applications with zipapp](https://docs.python.org/3/library/zipapp.html#creating-standalone-applications-with-zipapp)
      * [Caveats](https://docs.python.org/3/library/zipapp.html#caveats)
    * [The Python Zip Application Archive Format](https://docs.python.org/3/library/zipapp.html#the-python-zip-application-archive-format)


#### Previous topic
[`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html "previous chapter")
#### Next topic
[Python Runtime Services](https://docs.python.org/3/library/python.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zipapp+%E2%80%94+Manage+executable+Python+zip+archives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzipapp.html&pagesource=library%2Fzipapp.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/python.html "Python Runtime Services") |
  * [previous](https://docs.python.org/3/library/venv.html "venv — Creation of virtual environments") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html) »
  * [`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
