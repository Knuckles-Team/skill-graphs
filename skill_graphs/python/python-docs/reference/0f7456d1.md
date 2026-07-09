[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html)
    * [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parsing-library)
    * [Introduction](https://docs.python.org/3/library/optparse.html#introduction)
    * [Background](https://docs.python.org/3/library/optparse.html#background)
      * [Terminology](https://docs.python.org/3/library/optparse.html#terminology)
      * [What are options for?](https://docs.python.org/3/library/optparse.html#what-are-options-for)
      * [What are positional arguments for?](https://docs.python.org/3/library/optparse.html#what-are-positional-arguments-for)
    * [Tutorial](https://docs.python.org/3/library/optparse.html#tutorial)
      * [Understanding option actions](https://docs.python.org/3/library/optparse.html#understanding-option-actions)
      * [The store action](https://docs.python.org/3/library/optparse.html#the-store-action)
      * [Handling boolean (flag) options](https://docs.python.org/3/library/optparse.html#handling-boolean-flag-options)
      * [Other actions](https://docs.python.org/3/library/optparse.html#other-actions)
      * [Default values](https://docs.python.org/3/library/optparse.html#default-values)
      * [Generating help](https://docs.python.org/3/library/optparse.html#generating-help)
        * [Grouping Options](https://docs.python.org/3/library/optparse.html#grouping-options)
      * [Printing a version string](https://docs.python.org/3/library/optparse.html#printing-a-version-string)
      * [How `optparse` handles errors](https://docs.python.org/3/library/optparse.html#how-optparse-handles-errors)
      * [Putting it all together](https://docs.python.org/3/library/optparse.html#putting-it-all-together)
    * [Reference Guide](https://docs.python.org/3/library/optparse.html#reference-guide)
      * [Creating the parser](https://docs.python.org/3/library/optparse.html#creating-the-parser)
      * [Populating the parser](https://docs.python.org/3/library/optparse.html#populating-the-parser)
      * [Defining options](https://docs.python.org/3/library/optparse.html#defining-options)
      * [Option attributes](https://docs.python.org/3/library/optparse.html#option-attributes)
      * [Standard option actions](https://docs.python.org/3/library/optparse.html#standard-option-actions)
      * [Standard option types](https://docs.python.org/3/library/optparse.html#standard-option-types)
      * [Parsing arguments](https://docs.python.org/3/library/optparse.html#parsing-arguments)
      * [Querying and manipulating your option parser](https://docs.python.org/3/library/optparse.html#querying-and-manipulating-your-option-parser)
      * [Conflicts between options](https://docs.python.org/3/library/optparse.html#conflicts-between-options)
      * [Cleanup](https://docs.python.org/3/library/optparse.html#cleanup)
      * [Other methods](https://docs.python.org/3/library/optparse.html#other-methods)
    * [Option Callbacks](https://docs.python.org/3/library/optparse.html#option-callbacks)
      * [Defining a callback option](https://docs.python.org/3/library/optparse.html#defining-a-callback-option)
      * [How callbacks are called](https://docs.python.org/3/library/optparse.html#how-callbacks-are-called)
      * [Raising errors in a callback](https://docs.python.org/3/library/optparse.html#raising-errors-in-a-callback)
      * [Callback example 1: trivial callback](https://docs.python.org/3/library/optparse.html#callback-example-1-trivial-callback)
      * [Callback example 2: check option order](https://docs.python.org/3/library/optparse.html#callback-example-2-check-option-order)
      * [Callback example 3: check option order (generalized)](https://docs.python.org/3/library/optparse.html#callback-example-3-check-option-order-generalized)
      * [Callback example 4: check arbitrary condition](https://docs.python.org/3/library/optparse.html#callback-example-4-check-arbitrary-condition)
      * [Callback example 5: fixed arguments](https://docs.python.org/3/library/optparse.html#callback-example-5-fixed-arguments)
      * [Callback example 6: variable arguments](https://docs.python.org/3/library/optparse.html#callback-example-6-variable-arguments)
    * [Extending `optparse`](https://docs.python.org/3/library/optparse.html#extending-optparse)
      * [Adding new types](https://docs.python.org/3/library/optparse.html#adding-new-types)
      * [Adding new actions](https://docs.python.org/3/library/optparse.html#adding-new-actions)
    * [Exceptions](https://docs.python.org/3/library/optparse.html#exceptions)


#### Previous topic
[Migrating `optparse` code to `argparse`](https://docs.python.org/3/howto/argparse-optparse.html "previous chapter")
#### Next topic
[`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=optparse+%E2%80%94+Parser+for+command+line+options&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Foptparse.html&pagesource=library%2Foptparse.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/getpass.html "getpass — Portable password input") |
  * [previous](https://docs.python.org/3/howto/argparse-optparse.html "Migrating optparse code to argparse") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html)
  * |
  * Theme  Auto Light Dark |
