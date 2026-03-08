[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[Thread Safety Guarantees](https://docs.python.org/3/library/threadsafety.html "previous chapter")
#### Next topic
[`string` — Common string operations](https://docs.python.org/3/library/string.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Text+Processing+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftext.html&pagesource=library%2Ftext.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/string.html "string — Common string operations") |
  * [previous](https://docs.python.org/3/library/threadsafety.html "Thread Safety Guarantees") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html)
  * |
  * Theme  Auto Light Dark |


# Text Processing Services[¶](https://docs.python.org/3/library/text.html#text-processing-services "Link to this heading")
The modules described in this chapter provide a wide range of string manipulation operations and other text processing services.
The [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.") module described under [Binary Data Services](https://docs.python.org/3/library/binary.html#binaryservices) is also highly relevant to text processing. In addition, see the documentation for Python’s built-in string type in [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#textseq).
  * [`string` — Common string operations](https://docs.python.org/3/library/string.html)
    * [String constants](https://docs.python.org/3/library/string.html#string-constants)
    * [Custom String Formatting](https://docs.python.org/3/library/string.html#custom-string-formatting)
    * [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
      * [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
      * [Format examples](https://docs.python.org/3/library/string.html#format-examples)
    * [Template strings ($-strings)](https://docs.python.org/3/library/string.html#template-strings-strings)
    * [Helper functions](https://docs.python.org/3/library/string.html#helper-functions)
  * [`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html)
    * [Template strings](https://docs.python.org/3/library/string.templatelib.html#template-strings)
    * [Types](https://docs.python.org/3/library/string.templatelib.html#types)
    * [Helper functions](https://docs.python.org/3/library/string.templatelib.html#helper-functions)
  * [`re` — Regular expression operations](https://docs.python.org/3/library/re.html)
    * [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)
    * [Module Contents](https://docs.python.org/3/library/re.html#module-contents)
      * [Flags](https://docs.python.org/3/library/re.html#flags)
      * [Functions](https://docs.python.org/3/library/re.html#functions)
      * [Exceptions](https://docs.python.org/3/library/re.html#exceptions)
    * [Regular Expression Objects](https://docs.python.org/3/library/re.html#regular-expression-objects)
    * [Match Objects](https://docs.python.org/3/library/re.html#match-objects)
    * [Regular Expression Examples](https://docs.python.org/3/library/re.html#regular-expression-examples)
      * [Checking for a Pair](https://docs.python.org/3/library/re.html#checking-for-a-pair)
      * [Simulating scanf()](https://docs.python.org/3/library/re.html#simulating-scanf)
      * [search() vs. match()](https://docs.python.org/3/library/re.html#search-vs-match)
      * [Making a Phonebook](https://docs.python.org/3/library/re.html#making-a-phonebook)
      * [Text Munging](https://docs.python.org/3/library/re.html#text-munging)
      * [Finding all Adverbs](https://docs.python.org/3/library/re.html#finding-all-adverbs)
      * [Finding all Adverbs and their Positions](https://docs.python.org/3/library/re.html#finding-all-adverbs-and-their-positions)
      * [Raw String Notation](https://docs.python.org/3/library/re.html#raw-string-notation)
      * [Writing a Tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer)
  * [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
    * [SequenceMatcher Objects](https://docs.python.org/3/library/difflib.html#sequencematcher-objects)
    * [SequenceMatcher Examples](https://docs.python.org/3/library/difflib.html#sequencematcher-examples)
    * [Differ Objects](https://docs.python.org/3/library/difflib.html#differ-objects)
    * [Differ Example](https://docs.python.org/3/library/difflib.html#differ-example)
    * [A command-line interface to difflib](https://docs.python.org/3/library/difflib.html#a-command-line-interface-to-difflib)
    * [ndiff example](https://docs.python.org/3/library/difflib.html#ndiff-example)
  * [`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html)
  * [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
  * [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
  * [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
    * [Init file](https://docs.python.org/3/library/readline.html#init-file)
    * [Line buffer](https://docs.python.org/3/library/readline.html#line-buffer)
    * [History file](https://docs.python.org/3/library/readline.html#history-file)
    * [History list](https://docs.python.org/3/library/readline.html#history-list)
    * [Startup hooks](https://docs.python.org/3/library/readline.html#startup-hooks)
    * [Completion](https://docs.python.org/3/library/readline.html#completion)
    * [Example](https://docs.python.org/3/library/readline.html#example)
  * [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)


#### Previous topic
[Thread Safety Guarantees](https://docs.python.org/3/library/threadsafety.html "previous chapter")
#### Next topic
[`string` — Common string operations](https://docs.python.org/3/library/string.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Text+Processing+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftext.html&pagesource=library%2Ftext.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/string.html "string — Common string operations") |
  * [previous](https://docs.python.org/3/library/threadsafety.html "Thread Safety Guarantees") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
