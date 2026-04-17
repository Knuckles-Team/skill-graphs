[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html "previous chapter")
#### Next topic
[`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+Runtime+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpython.html&pagesource=library%2Fpython.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sys.html "sys — System-specific parameters and functions") |
  * [previous](https://docs.python.org/3/library/zipapp.html "zipapp — Manage executable Python zip archives") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html)
  * |
  * Theme  Auto Light Dark |


# Python Runtime Services[¶](https://docs.python.org/3/library/python.html#python-runtime-services "Link to this heading")
The modules described in this chapter provide a wide range of services related to the Python interpreter and its interaction with its environment. Here’s an overview:
  * [`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
  * [`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html)
    * [Tool identifiers](https://docs.python.org/3/library/sys.monitoring.html#tool-identifiers)
      * [Registering and using tools](https://docs.python.org/3/library/sys.monitoring.html#registering-and-using-tools)
    * [Events](https://docs.python.org/3/library/sys.monitoring.html#events)
      * [Local events](https://docs.python.org/3/library/sys.monitoring.html#local-events)
      * [Deprecated event](https://docs.python.org/3/library/sys.monitoring.html#deprecated-event)
      * [Ancillary events](https://docs.python.org/3/library/sys.monitoring.html#ancillary-events)
      * [Other events](https://docs.python.org/3/library/sys.monitoring.html#other-events)
      * [The STOP_ITERATION event](https://docs.python.org/3/library/sys.monitoring.html#the-stop-iteration-event)
    * [Turning events on and off](https://docs.python.org/3/library/sys.monitoring.html#turning-events-on-and-off)
      * [Setting events globally](https://docs.python.org/3/library/sys.monitoring.html#setting-events-globally)
      * [Per code object events](https://docs.python.org/3/library/sys.monitoring.html#per-code-object-events)
      * [Disabling events](https://docs.python.org/3/library/sys.monitoring.html#disabling-events)
    * [Registering callback functions](https://docs.python.org/3/library/sys.monitoring.html#registering-callback-functions)
      * [Callback function arguments](https://docs.python.org/3/library/sys.monitoring.html#callback-function-arguments)
  * [`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html)
    * [Configuration variables](https://docs.python.org/3/library/sysconfig.html#configuration-variables)
    * [Installation paths](https://docs.python.org/3/library/sysconfig.html#installation-paths)
    * [User scheme](https://docs.python.org/3/library/sysconfig.html#user-scheme)
      * [`posix_user`](https://docs.python.org/3/library/sysconfig.html#posix-user)
      * [`nt_user`](https://docs.python.org/3/library/sysconfig.html#nt-user)
      * [`osx_framework_user`](https://docs.python.org/3/library/sysconfig.html#osx-framework-user)
    * [Home scheme](https://docs.python.org/3/library/sysconfig.html#home-scheme)
      * [`posix_home`](https://docs.python.org/3/library/sysconfig.html#posix-home)
    * [Prefix scheme](https://docs.python.org/3/library/sysconfig.html#prefix-scheme)
      * [`posix_prefix`](https://docs.python.org/3/library/sysconfig.html#posix-prefix)
      * [`nt`](https://docs.python.org/3/library/sysconfig.html#nt)
    * [Installation path functions](https://docs.python.org/3/library/sysconfig.html#installation-path-functions)
    * [Other functions](https://docs.python.org/3/library/sysconfig.html#other-functions)
    * [Command-line usage](https://docs.python.org/3/library/sysconfig.html#command-line-usage)
  * [`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html)
  * [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
    * [`__name__ == '__main__'`](https://docs.python.org/3/library/__main__.html#name-main)
      * [What is the “top-level code environment”?](https://docs.python.org/3/library/__main__.html#what-is-the-top-level-code-environment)
      * [Idiomatic Usage](https://docs.python.org/3/library/__main__.html#idiomatic-usage)
      * [Packaging Considerations](https://docs.python.org/3/library/__main__.html#packaging-considerations)
    * [`__main__.py` in Python Packages](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages)
      * [Idiomatic Usage](https://docs.python.org/3/library/__main__.html#id1)
    * [`import __main__`](https://docs.python.org/3/library/__main__.html#import-main)
  * [`warnings` — Warning control](https://docs.python.org/3/library/warnings.html)
    * [Warning Categories](https://docs.python.org/3/library/warnings.html#warning-categories)
    * [The Warnings Filter](https://docs.python.org/3/library/warnings.html#the-warnings-filter)
      * [Repeated Warning Suppression Criteria](https://docs.python.org/3/library/warnings.html#repeated-warning-suppression-criteria)
      * [Describing Warning Filters](https://docs.python.org/3/library/warnings.html#describing-warning-filters)
      * [Default Warning Filter](https://docs.python.org/3/library/warnings.html#default-warning-filter)
      * [Overriding the default filter](https://docs.python.org/3/library/warnings.html#overriding-the-default-filter)
    * [Temporarily Suppressing Warnings](https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings)
    * [Testing Warnings](https://docs.python.org/3/library/warnings.html#testing-warnings)
    * [Updating Code For New Versions of Dependencies](https://docs.python.org/3/library/warnings.html#updating-code-for-new-versions-of-dependencies)
    * [Available Functions](https://docs.python.org/3/library/warnings.html#available-functions)
    * [Available Context Managers](https://docs.python.org/3/library/warnings.html#available-context-managers)
    * [Concurrent safety of Context Managers](https://docs.python.org/3/library/warnings.html#concurrent-safety-of-context-managers)
  * [`dataclasses` — Data Classes](https://docs.python.org/3/library/dataclasses.html)
    * [Module contents](https://docs.python.org/3/library/dataclasses.html#module-contents)
    * [Post-init processing](https://docs.python.org/3/library/dataclasses.html#post-init-processing)
    * [Class variables](https://docs.python.org/3/library/dataclasses.html#class-variables)
    * [Init-only variables](https://docs.python.org/3/library/dataclasses.html#init-only-variables)
    * [Frozen instances](https://docs.python.org/3/library/dataclasses.html#frozen-instances)
    * [Inheritance](https://docs.python.org/3/library/dataclasses.html#inheritance)
    * [Re-ordering of keyword-only parameters in `__init__()`](https://docs.python.org/3/library/dataclasses.html#re-ordering-of-keyword-only-parameters-in-init)
    * [Default factory functions](https://docs.python.org/3/library/dataclasses.html#default-factory-functions)
    * [Mutable default values](https://docs.python.org/3/library/dataclasses.html#mutable-default-values)
    * [Descriptor-typed fields](https://docs.python.org/3/library/dataclasses.html#descriptor-typed-fields)
  * [`contextlib` — Utilities for `with`-statement contexts](https://docs.python.org/3/library/contextlib.html)
    * [Utilities](https://docs.python.org/3/library/contextlib.html#utilities)
    * [Examples and Recipes](https://docs.python.org/3/library/contextlib.html#examples-and-recipes)
      * [Supporting a variable number of context managers](https://docs.python.org/3/library/contextlib.html#supporting-a-variable-number-of-context-managers)
      * [Catching exceptions from `__enter__` methods](https://docs.python.org/3/library/contextlib.html#catching-exceptions-from-enter-methods)
      * [Cleaning up in an `__enter__` implementation](https://docs.python.org/3/library/contextlib.html#cleaning-up-in-an-enter-implementation)
      * [Replacing any use of `try-finally` and flag variables](https://docs.python.org/3/library/contextlib.html#replacing-any-use-of-try-finally-and-flag-variables)
      * [Using a context manager as a function decorator](https://docs.python.org/3/library/contextlib.html#using-a-context-manager-as-a-function-decorator)
    * [Single use, reusable and reentrant context managers](https://docs.python.org/3/library/contextlib.html#single-use-reusable-and-reentrant-context-managers)
      * [Reentrant context managers](https://docs.python.org/3/library/contextlib.html#reentrant-context-managers)
      * [Reusable context managers](https://docs.python.org/3/library/contextlib.html#reusable-context-managers)
  * [`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
  * [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
    * [`atexit` Example](https://docs.python.org/3/library/atexit.html#atexit-example)
  * [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
    * [Module-Level Functions](https://docs.python.org/3/library/traceback.html#module-level-functions)
    * [`TracebackException` Objects](https://docs.python.org/3/library/traceback.html#tracebackexception-objects)
    * [`StackSummary` Objects](https://docs.python.org/3/library/traceback.html#stacksummary-objects)
    * [`FrameSummary` Objects](https://docs.python.org/3/library/traceback.html#framesummary-objects)
    * [Examples of Using the Module-Level Functions](https://docs.python.org/3/library/traceback.html#examples-of-using-the-module-level-functions)
    * [Examples of Using `TracebackException`](https://docs.python.org/3/library/traceback.html#examples-of-using-tracebackexception)
  * [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
    * [Module Contents](https://docs.python.org/3/library/__future__.html#module-contents)
  * [`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html)
  * [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html)
    * [Types and members](https://docs.python.org/3/library/inspect.html#types-and-members)
    * [Retrieving source code](https://docs.python.org/3/library/inspect.html#retrieving-source-code)
    * [Introspecting callables with the Signature object](https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object)
    * [Classes and functions](https://docs.python.org/3/library/inspect.html#classes-and-functions)
    * [The interpreter stack](https://docs.python.org/3/library/inspect.html#the-interpreter-stack)
    * [Fetching attributes statically](https://docs.python.org/3/library/inspect.html#fetching-attributes-statically)
    * [Current State of Generators, Coroutines, and Asynchronous Generators](https://docs.python.org/3/library/inspect.html#current-state-of-generators-coroutines-and-asynchronous-generators)
    * [Code Objects Bit Flags](https://docs.python.org/3/library/inspect.html#code-objects-bit-flags)
    * [Buffer flags](https://docs.python.org/3/library/inspect.html#buffer-flags)
    * [Command-line interface](https://docs.python.org/3/library/inspect.html#command-line-interface)
  * [`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html)
    * [Annotation semantics](https://docs.python.org/3/library/annotationlib.html#annotation-semantics)
    * [Classes](https://docs.python.org/3/library/annotationlib.html#classes)
    * [Functions](https://docs.python.org/3/library/annotationlib.html#functions)
    * [Recipes](https://docs.python.org/3/library/annotationlib.html#recipes)
      * [Using annotations in a metaclass](https://docs.python.org/3/library/annotationlib.html#using-annotations-in-a-metaclass)
    * [Limitations of the `STRING` format](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-string-format)
    * [Limitations of the `FORWARDREF` format](https://docs.python.org/3/library/annotationlib.html#limitations-of-the-forwardref-format)
    * [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#security-implications-of-introspecting-annotations)
  * [`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html)
    * [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize)
    * [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize)
    * [Readline configuration](https://docs.python.org/3/library/site.html#readline-configuration)
    * [Module contents](https://docs.python.org/3/library/site.html#module-contents)
    * [Command-line interface](https://docs.python.org/3/library/site.html#command-line-interface)


See also
  * See the [`concurrent.interpreters`](https://docs.python.org/3/library/concurrent.interpreters.html#module-concurrent.interpreters "concurrent.interpreters: Multiple interpreters in the same process") module, which similarly exposes core runtime functionality.


#### Previous topic
[`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html "previous chapter")
#### Next topic
[`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+Runtime+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpython.html&pagesource=library%2Fpython.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sys.html "sys — System-specific parameters and functions") |
  * [previous](https://docs.python.org/3/library/zipapp.html "zipapp — Manage executable Python zip archives") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
