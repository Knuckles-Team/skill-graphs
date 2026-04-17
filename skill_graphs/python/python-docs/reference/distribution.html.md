[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html "previous chapter")
#### Next topic
[`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Software+Packaging+and+Distribution&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdistribution.html&pagesource=library%2Fdistribution.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ensurepip.html "ensurepip — Bootstrapping the pip installer") |
  * [previous](https://docs.python.org/3/library/tracemalloc.html "tracemalloc — Trace memory allocations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html)
  * |
  * Theme  Auto Light Dark |


# Software Packaging and Distribution[¶](https://docs.python.org/3/library/distribution.html#software-packaging-and-distribution "Link to this heading")
These libraries help you with publishing and installing Python software. While these modules are designed to work in conjunction with the
  * [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html)
    * [Command-line interface](https://docs.python.org/3/library/ensurepip.html#command-line-interface)
    * [Module API](https://docs.python.org/3/library/ensurepip.html#module-api)
  * [`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
    * [Creating virtual environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
    * [How venvs work](https://docs.python.org/3/library/venv.html#how-venvs-work)
    * [API](https://docs.python.org/3/library/venv.html#api)
    * [An example of extending `EnvBuilder`](https://docs.python.org/3/library/venv.html#an-example-of-extending-envbuilder)
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
[`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html "previous chapter")
#### Next topic
[`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Software+Packaging+and+Distribution&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdistribution.html&pagesource=library%2Fdistribution.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ensurepip.html "ensurepip — Bootstrapping the pip installer") |
  * [previous](https://docs.python.org/3/library/tracemalloc.html "tracemalloc — Trace memory allocations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
