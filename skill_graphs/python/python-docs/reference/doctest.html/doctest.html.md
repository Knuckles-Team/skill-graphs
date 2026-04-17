[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`doctest` — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
    * [Simple Usage: Checking Examples in Docstrings](https://docs.python.org/3/library/doctest.html#simple-usage-checking-examples-in-docstrings)
    * [Simple Usage: Checking Examples in a Text File](https://docs.python.org/3/library/doctest.html#simple-usage-checking-examples-in-a-text-file)
    * [Command-line Usage](https://docs.python.org/3/library/doctest.html#command-line-usage)
    * [How It Works](https://docs.python.org/3/library/doctest.html#how-it-works)
      * [Which Docstrings Are Examined?](https://docs.python.org/3/library/doctest.html#which-docstrings-are-examined)
      * [How are Docstring Examples Recognized?](https://docs.python.org/3/library/doctest.html#how-are-docstring-examples-recognized)
      * [What’s the Execution Context?](https://docs.python.org/3/library/doctest.html#what-s-the-execution-context)
      * [What About Exceptions?](https://docs.python.org/3/library/doctest.html#what-about-exceptions)
      * [Option Flags](https://docs.python.org/3/library/doctest.html#option-flags)
      * [Directives](https://docs.python.org/3/library/doctest.html#directives)
      * [Warnings](https://docs.python.org/3/library/doctest.html#warnings)
    * [Basic API](https://docs.python.org/3/library/doctest.html#basic-api)
    * [Unittest API](https://docs.python.org/3/library/doctest.html#unittest-api)
    * [Advanced API](https://docs.python.org/3/library/doctest.html#advanced-api)
      * [DocTest Objects](https://docs.python.org/3/library/doctest.html#doctest-objects)
      * [Example Objects](https://docs.python.org/3/library/doctest.html#example-objects)
      * [DocTestFinder objects](https://docs.python.org/3/library/doctest.html#doctestfinder-objects)
      * [DocTestParser objects](https://docs.python.org/3/library/doctest.html#doctestparser-objects)
      * [TestResults objects](https://docs.python.org/3/library/doctest.html#testresults-objects)
      * [DocTestRunner objects](https://docs.python.org/3/library/doctest.html#doctestrunner-objects)
      * [OutputChecker objects](https://docs.python.org/3/library/doctest.html#outputchecker-objects)
    * [Debugging](https://docs.python.org/3/library/doctest.html#debugging)
    * [Soapbox](https://docs.python.org/3/library/doctest.html#soapbox)


#### Previous topic
[Python Development Mode](https://docs.python.org/3/library/devmode.html "previous chapter")
#### Next topic
[`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=doctest+%E2%80%94+Test+interactive+Python+examples&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdoctest.html&pagesource=library%2Fdoctest.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/unittest.html "unittest — Unit testing framework") |
  * [previous](https://docs.python.org/3/library/devmode.html "Python Development Mode") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`doctest` — Test interactive Python examples](https://docs.python.org/3/library/doctest.html#directives)
  * |
  * Theme  Auto Light Dark |
