[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
    * [ArgumentParser objects](https://docs.python.org/3/library/argparse.html#argumentparser-objects)
      * [prog](https://docs.python.org/3/library/argparse.html#prog)
      * [usage](https://docs.python.org/3/library/argparse.html#usage)
      * [description](https://docs.python.org/3/library/argparse.html#description)
      * [epilog](https://docs.python.org/3/library/argparse.html#epilog)
      * [parents](https://docs.python.org/3/library/argparse.html#parents)
      * [formatter_class](https://docs.python.org/3/library/argparse.html#formatter-class)
      * [prefix_chars](https://docs.python.org/3/library/argparse.html#prefix-chars)
      * [fromfile_prefix_chars](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars)
      * [argument_default](https://docs.python.org/3/library/argparse.html#argument-default)
      * [allow_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev)
      * [conflict_handler](https://docs.python.org/3/library/argparse.html#conflict-handler)
      * [add_help](https://docs.python.org/3/library/argparse.html#add-help)
      * [exit_on_error](https://docs.python.org/3/library/argparse.html#exit-on-error)
      * [suggest_on_error](https://docs.python.org/3/library/argparse.html#suggest-on-error)
      * [color](https://docs.python.org/3/library/argparse.html#color)
    * [The add_argument() method](https://docs.python.org/3/library/argparse.html#the-add-argument-method)
      * [name or flags](https://docs.python.org/3/library/argparse.html#name-or-flags)
      * [action](https://docs.python.org/3/library/argparse.html#action)
      * [nargs](https://docs.python.org/3/library/argparse.html#nargs)
      * [const](https://docs.python.org/3/library/argparse.html#const)
      * [default](https://docs.python.org/3/library/argparse.html#default)
      * [type](https://docs.python.org/3/library/argparse.html#type)
      * [choices](https://docs.python.org/3/library/argparse.html#choices)
      * [required](https://docs.python.org/3/library/argparse.html#required)
      * [help](https://docs.python.org/3/library/argparse.html#help)
      * [metavar](https://docs.python.org/3/library/argparse.html#metavar)
      * [dest](https://docs.python.org/3/library/argparse.html#dest)
      * [deprecated](https://docs.python.org/3/library/argparse.html#deprecated)
      * [Action classes](https://docs.python.org/3/library/argparse.html#action-classes)
    * [The parse_args() method](https://docs.python.org/3/library/argparse.html#the-parse-args-method)
      * [Option value syntax](https://docs.python.org/3/library/argparse.html#option-value-syntax)
      * [Invalid arguments](https://docs.python.org/3/library/argparse.html#invalid-arguments)
      * [Arguments containing `-`](https://docs.python.org/3/library/argparse.html#arguments-containing)
      * [Argument abbreviations (prefix matching)](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching)
      * [Beyond `sys.argv`](https://docs.python.org/3/library/argparse.html#beyond-sys-argv)
      * [The Namespace object](https://docs.python.org/3/library/argparse.html#the-namespace-object)
    * [Other utilities](https://docs.python.org/3/library/argparse.html#other-utilities)
      * [Subcommands](https://docs.python.org/3/library/argparse.html#subcommands)
      * [FileType objects](https://docs.python.org/3/library/argparse.html#filetype-objects)
      * [Argument groups](https://docs.python.org/3/library/argparse.html#argument-groups)
      * [Mutual exclusion](https://docs.python.org/3/library/argparse.html#mutual-exclusion)
      * [Parser defaults](https://docs.python.org/3/library/argparse.html#parser-defaults)
      * [Printing help](https://docs.python.org/3/library/argparse.html#printing-help)
      * [Partial parsing](https://docs.python.org/3/library/argparse.html#partial-parsing)
      * [Customizing file parsing](https://docs.python.org/3/library/argparse.html#customizing-file-parsing)
      * [Exiting methods](https://docs.python.org/3/library/argparse.html#exiting-methods)
      * [Intermixed parsing](https://docs.python.org/3/library/argparse.html#intermixed-parsing)
      * [Registering custom types or actions](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions)
    * [Exceptions](https://docs.python.org/3/library/argparse.html#exceptions)


#### Previous topic
[Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html "previous chapter")
#### Next topic
[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=argparse+%E2%80%94+Parser+for+command-line+options%2C+arguments+and+subcommands&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fargparse.html&pagesource=library%2Fargparse.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/howto/argparse.html "Argparse Tutorial") |
  * [previous](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
  * |
  * Theme  Auto Light Dark |
