[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html)
    * [Command-line interface](https://docs.python.org/3/library/ensurepip.html#command-line-interface)
    * [Module API](https://docs.python.org/3/library/ensurepip.html#module-api)


#### Previous topic
[Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html "previous chapter")
#### Next topic
[`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ensurepip+%E2%80%94+Bootstrapping+the+pip+installer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fensurepip.html&pagesource=library%2Fensurepip.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/venv.html "venv — Creation of virtual environments") |
  * [previous](https://docs.python.org/3/library/distribution.html "Software Packaging and Distribution") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html) »
  * [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html)
  * |
  * Theme  Auto Light Dark |


#  `ensurepip` — Bootstrapping the `pip` installer[¶](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "Link to this heading")
Added in version 3.4.
**Source code:**
* * *
The `ensurepip` package provides support for bootstrapping the `pip` installer into an existing Python installation or virtual environment. This bootstrapping approach reflects the fact that `pip` is an independent project with its own release cycle, and the latest available stable version is bundled with maintenance and feature releases of the CPython reference interpreter.
In most cases, end users of Python shouldn’t need to invoke this module directly (as `pip` should be bootstrapped by default), but it may be needed if installing `pip` was skipped when installing Python (or when creating a virtual environment) or after explicitly uninstalling `pip`.
Note
This module _does not_ access the internet. All of the components needed to bootstrap `pip` are included as internal parts of the package.
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
See also

[Installing Python Modules](https://docs.python.org/3/installing/index.html#installing-index)

The end user guide for installing Python packages

[**PEP 453**](https://peps.python.org/pep-0453/): Explicit bootstrapping of pip in Python installations

The original rationale and specification for this module.
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
## Command-line interface[¶](https://docs.python.org/3/library/ensurepip.html#command-line-interface "Link to this heading")
The command line interface is invoked using the interpreter’s `-m` switch.
The simplest possible invocation is:
Copy```
python -m ensurepip

```

This invocation will install `pip` if it is not already installed, but otherwise does nothing. To ensure the installed version of `pip` is at least as recent as the one available in `ensurepip`, pass the `--upgrade` option:
Copy```
python -m ensurepip --upgrade

```

By default, `pip` is installed into the current virtual environment (if one is active) or into the system site packages (if there is no active virtual environment). The installation location can be controlled through two additional command line options:

--root <dir>[¶](https://docs.python.org/3/library/ensurepip.html#cmdoption-ensurepip-root "Link to this definition")

Installs `pip` relative to the given root directory rather than the root of the currently active virtual environment (if any) or the default root for the current Python installation.

--user[¶](https://docs.python.org/3/library/ensurepip.html#cmdoption-ensurepip-user "Link to this definition")

Installs `pip` into the user site packages directory rather than globally for the current Python installation (this option is not permitted inside an active virtual environment).
By default, the scripts `pipX` and `pipX.Y` will be installed (where X.Y stands for the version of Python used to invoke `ensurepip`). The scripts installed can be controlled through two additional command line options:

--altinstall[¶](https://docs.python.org/3/library/ensurepip.html#cmdoption-ensurepip-altinstall "Link to this definition")

If an alternate installation is requested, the `pipX` script will _not_ be installed.

--default-pip[¶](https://docs.python.org/3/library/ensurepip.html#cmdoption-ensurepip-default-pip "Link to this definition")

If a “default pip” installation is requested, the `pip` script will be installed in addition to the two regular scripts.
Providing both of the script selection options will trigger an exception.
## Module API[¶](https://docs.python.org/3/library/ensurepip.html#module-api "Link to this heading")
`ensurepip` exposes two functions for programmatic use:

ensurepip.version()[¶](https://docs.python.org/3/library/ensurepip.html#ensurepip.version "Link to this definition")

Returns a string specifying the available version of pip that will be installed when bootstrapping an environment.

ensurepip.bootstrap(_root =None_, _upgrade =False_, _user =False_, _altinstall =False_, _default_pip =False_, _verbosity =0_)[¶](https://docs.python.org/3/library/ensurepip.html#ensurepip.bootstrap "Link to this definition")

Bootstraps `pip` into the current or designated environment.
_root_ specifies an alternative root directory to install relative to. If _root_ is `None`, then installation uses the default install location for the current environment.
_upgrade_ indicates whether or not to upgrade an existing installation of an earlier version of `pip` to the available version.
_user_ indicates whether to use the user scheme rather than installing globally.
By default, the scripts `pipX` and `pipX.Y` will be installed (where X.Y stands for the current version of Python).
If _altinstall_ is set, then `pipX` will _not_ be installed.
If _default_pip_ is set, then `pip` will be installed in addition to the two regular scripts.
Setting both _altinstall_ and _default_pip_ will trigger [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
_verbosity_ controls the level of output to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") from the bootstrapping operation.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `ensurepip.bootstrap` with argument `root`.
Note
The bootstrapping process has side effects on both `sys.path` and `os.environ`. Invoking the command line interface in a subprocess instead allows these side effects to be avoided.
Note
The bootstrapping process may install additional modules required by `pip`, but other software should not assume those dependencies will always be present by default (as the dependencies may be removed in a future version of `pip`).
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html)
    * [Command-line interface](https://docs.python.org/3/library/ensurepip.html#command-line-interface)
    * [Module API](https://docs.python.org/3/library/ensurepip.html#module-api)


#### Previous topic
[Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html "previous chapter")
#### Next topic
[`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ensurepip+%E2%80%94+Bootstrapping+the+pip+installer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fensurepip.html&pagesource=library%2Fensurepip.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/venv.html "venv — Creation of virtual environments") |
  * [previous](https://docs.python.org/3/library/distribution.html "Software Packaging and Distribution") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html) »
  * [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
