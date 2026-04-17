[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html)
    * [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#virtual-environments)
    * [_pth files](https://docs.python.org/3/library/sys_path_init.html#pth-files)
    * [Embedded Python](https://docs.python.org/3/library/sys_path_init.html#embedded-python)


#### Previous topic
[`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html "previous chapter")
#### Next topic
[Python Language Services](https://docs.python.org/3/library/language.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=The+initialization+of+the+sys.path+module+search+path&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys_path_init.html&pagesource=library%2Fsys_path_init.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/language.html "Python Language Services") |
  * [previous](https://docs.python.org/3/library/importlib.metadata.html "importlib.metadata – Accessing package metadata") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html)
  * |
  * Theme  Auto Light Dark |


# The initialization of the [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") module search path[¶](https://docs.python.org/3/library/sys_path_init.html#the-initialization-of-the-sys-path-module-search-path "Link to this heading")
A module search path is initialized when Python starts. This module search path may be accessed at [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").
The first entry in the module search path is the directory that contains the input script, if there is one. Otherwise, the first entry is the current directory, which is the case when executing the interactive shell, a [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) command, or [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) module.
The [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) environment variable is often used to add directories to the search path. If this environment variable is found then the contents are added to the module search path.
Note
[`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) will affect all installed Python versions/environments. Be wary of setting this in your shell profile or global environment variables. The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module offers more nuanced techniques as mentioned below.
The next items added are the directories containing standard Python modules as well as any [extension module](https://docs.python.org/3/glossary.html#term-extension-module)s that these modules depend on. Extension modules are `.pyd` files on Windows and `.so` files on other platforms. The directory with the platform-independent Python modules is called `prefix`. The directory with the extension modules is called `exec_prefix`.
The [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME) environment variable may be used to set the `prefix` and `exec_prefix` locations. Otherwise these directories are found by using the Python executable as a starting point and then looking for various ‘landmark’ files and directories. Note that any symbolic links are followed so the real Python executable location is used as the search starting point. The Python executable location is called `home`.
Once `home` is determined, the `prefix` directory is found by first looking for `python_majorversion__minorversion_.zip`(`python311.zip`). On Windows the zip archive is searched for in `home` and on Unix the archive is expected to be in `lib`. Note that the expected zip archive location is added to the module search path even if the archive does not exist. If no archive was found, Python on Windows will continue the search for `prefix` by looking for `Lib\os.py`. Python on Unix will look for `lib/python_majorversion_._minorversion_/os.py`(`lib/python3.11/os.py`). On Windows `prefix` and `exec_prefix` are the same, however on other platforms `lib/python_majorversion_._minorversion_/lib-dynload`(`lib/python3.11/lib-dynload`) is searched for and used as an anchor for `exec_prefix`. On some platforms `lib` may be `lib64` or another value, see [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir") and [`PYTHONPLATLIBDIR`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPLATLIBDIR).
Once found, `prefix` and `exec_prefix` are available at [`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix") and [`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix") respectively.
If [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME) is not set, and a `pyvenv.cfg` file is found alongside the main executable, or in its parent directory, [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") and [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix") get set to the directory containing `pyvenv.cfg`, otherwise they are set to the same value as [`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix") and [`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix"), respectively. This is used by [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments).
Finally, the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module is processed and `site-packages` directories are added to the module search path. A common way to customize the search path is to create [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize "sitecustomize") or [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize "usercustomize") modules as described in the `site` module documentation.
Note
Certain command line options may further affect path calculations. See [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E), [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I), [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s) and [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) for further details.
Changed in version 3.14: [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") and [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix") are now set to the `pyvenv.cfg` directory during the path initialization. This was previously done by [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration."), therefore affected by [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S).
## Virtual Environments[¶](https://docs.python.org/3/library/sys_path_init.html#virtual-environments "Link to this heading")
Virtual environments place a `pyvenv.cfg` file in their prefix, which causes [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix") and [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix") to point to them, instead of the base installation.
The `prefix` and `exec_prefix` values of the base installation are available at [`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix") and [`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix").
As well as being used as a marker to identify virtual environments, `pyvenv.cfg` may also be used to configure the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") initialization. Please refer to `site`’s [virtual environments documentation](https://docs.python.org/3/library/site.html#site-virtual-environments-configuration).
Note
[`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME) overrides the `pyvenv.cfg` detection.
Note
There are other ways how “virtual environments” could be implemented, this documentation refers implementations based on the `pyvenv.cfg` mechanism, such as [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments."). Most virtual environment implementations follow the model set by `venv`, but there may be exotic implementations that diverge from it.
## _pth files[¶](https://docs.python.org/3/library/sys_path_init.html#pth-files "Link to this heading")
To completely override [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") create a `._pth` file with the same name as the shared library or executable (`python._pth` or `python311._pth`). The shared library path is always known on Windows, however it may not be available on other platforms. In the `._pth` file specify one line for each path to add to `sys.path`. The file based on the shared library name overrides the one based on the executable, which allows paths to be restricted for any program loading the runtime if desired.
When the file exists, all registry and environment variables are ignored, isolated mode is enabled, and [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") is not imported unless one line in the file specifies `import site`. Blank paths and lines starting with `#` are ignored. Each path may be absolute or relative to the location of the file. Import statements other than to `site` are not permitted, and arbitrary code cannot be specified.
Note that `.pth` files (without leading underscore) will be processed normally by the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module when `import site` has been specified.
## Embedded Python[¶](https://docs.python.org/3/library/sys_path_init.html#embedded-python "Link to this heading")
If Python is embedded within another application [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig") and the [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig") structure can be used to initialize Python. The path specific details are described at [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config).
See also
  * [Finding modules](https://docs.python.org/3/using/windows.html#windows-finding-modules) for detailed Windows notes.
  * [Using Python on Unix platforms](https://docs.python.org/3/using/unix.html#using-on-unix) for Unix details.


### [Table of Contents](https://docs.python.org/3/contents.html)
  * [The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html)
    * [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#virtual-environments)
    * [_pth files](https://docs.python.org/3/library/sys_path_init.html#pth-files)
    * [Embedded Python](https://docs.python.org/3/library/sys_path_init.html#embedded-python)


#### Previous topic
[`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html "previous chapter")
#### Next topic
[Python Language Services](https://docs.python.org/3/library/language.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=The+initialization+of+the+sys.path+module+search+path&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys_path_init.html&pagesource=library%2Fsys_path_init.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/language.html "Python Language Services") |
  * [previous](https://docs.python.org/3/library/importlib.metadata.html "importlib.metadata – Accessing package metadata") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
