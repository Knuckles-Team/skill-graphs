[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)
    * [Using the `subprocess` Module](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)
      * [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments)
      * [Popen Constructor](https://docs.python.org/3/library/subprocess.html#popen-constructor)
      * [Exceptions](https://docs.python.org/3/library/subprocess.html#exceptions)
    * [Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations)
    * [Popen Objects](https://docs.python.org/3/library/subprocess.html#popen-objects)
    * [Windows Popen Helpers](https://docs.python.org/3/library/subprocess.html#windows-popen-helpers)
      * [Windows Constants](https://docs.python.org/3/library/subprocess.html#windows-constants)
    * [Older high-level API](https://docs.python.org/3/library/subprocess.html#older-high-level-api)
    * [Replacing Older Functions with the `subprocess` Module](https://docs.python.org/3/library/subprocess.html#replacing-older-functions-with-the-subprocess-module)
      * [Replacing **/bin/sh** shell command substitution](https://docs.python.org/3/library/subprocess.html#replacing-bin-sh-shell-command-substitution)
      * [Replacing shell pipeline](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline)
      * [Replacing `os.system()`](https://docs.python.org/3/library/subprocess.html#replacing-os-system)
      * [Replacing the `os.spawn` family](https://docs.python.org/3/library/subprocess.html#replacing-the-os-spawn-family)
      * [Replacing `os.popen()`](https://docs.python.org/3/library/subprocess.html#replacing-os-popen)
    * [Legacy Shell Invocation Functions](https://docs.python.org/3/library/subprocess.html#legacy-shell-invocation-functions)
    * [Notes](https://docs.python.org/3/library/subprocess.html#notes)
      * [Timeout Behavior](https://docs.python.org/3/library/subprocess.html#timeout-behavior)
      * [Converting an argument sequence to a string on Windows](https://docs.python.org/3/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows)
      * [Disable use of `posix_spawn()`](https://docs.python.org/3/library/subprocess.html#disable-use-of-posix-spawn)


#### Previous topic
[`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html "previous chapter")
#### Next topic
[`sched` — Event scheduler](https://docs.python.org/3/library/sched.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=subprocess+%E2%80%94+Subprocess+management&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsubprocess.html&pagesource=library%2Fsubprocess.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sched.html "sched — Event scheduler") |
  * [previous](https://docs.python.org/3/library/concurrent.interpreters.html "concurrent.interpreters — Multiple interpreters in the same process") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline)
  * |
  * Theme  Auto Light Dark |
