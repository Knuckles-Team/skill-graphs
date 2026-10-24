[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
    * [Tokenizing Input](https://docs.python.org/3/library/tokenize.html#tokenizing-input)
    * [Command-Line Usage](https://docs.python.org/3/library/tokenize.html#command-line-usage)
    * [Examples](https://docs.python.org/3/library/tokenize.html#examples)


#### Previous topic
[`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html "previous chapter")
#### Next topic
[`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tokenize+%E2%80%94+Tokenizer+for+Python+source&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftokenize.html&pagesource=library%2Ftokenize.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tabnanny.html "tabnanny — Detection of ambiguous indentation") |
  * [previous](https://docs.python.org/3/library/keyword.html "keyword — Testing for Python keywords") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
  * |
  * Theme  Auto Light Dark |


#  `tokenize` — Tokenizer for Python source[¶](https://docs.python.org/3/library/tokenize.html#module-tokenize "Link to this heading")
**Source code:**
* * *
The `tokenize` module provides a lexical scanner for Python source code, implemented in Python. The scanner in this module returns comments as tokens as well, making it useful for implementing “pretty-printers”, including colorizers for on-screen displays.
To simplify token stream handling, all [operator](https://docs.python.org/3/reference/lexical_analysis.html#operators) and [delimiter](https://docs.python.org/3/reference/lexical_analysis.html#delimiters) tokens and [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "Ellipsis") are returned using the generic [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP") token type. The exact type can be determined by checking the `exact_type` property on the [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) returned from [`tokenize.tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize").
Warning
Note that the functions in this module are only designed to parse syntactically valid Python code (code that does not raise when parsed using [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse")). The behavior of the functions in this module is **undefined** when providing invalid Python code and it can change at any point.
## Tokenizing Input[¶](https://docs.python.org/3/library/tokenize.html#tokenizing-input "Link to this heading")
The primary entry point is a [generator](https://docs.python.org/3/glossary.html#term-generator):

tokenize.tokenize(_readline_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "Link to this definition")

The `tokenize()` generator requires one argument, _readline_ , which must be a callable object which provides the same interface as the [`io.IOBase.readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") method of file objects. Each call to the function should return one line of input as bytes.
The generator produces 5-tuples with these members: the token type; the token string; a 2-tuple `(srow, scol)` of ints specifying the row and column where the token begins in the source; a 2-tuple `(erow, ecol)` of ints specifying the row and column where the token ends in the source; and the line on which the token was found. The line passed (the last tuple item) is the _physical_ line. The 5 tuple is returned as a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) with the field names: `type string start end line`.
The returned [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) has an additional property named `exact_type` that contains the exact operator type for [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP") tokens. For all other token types `exact_type` equals the named tuple `type` field.
Changed in version 3.1: Added support for named tuples.
Changed in version 3.3: Added support for `exact_type`.
`tokenize()` determines the source encoding of the file by looking for a UTF-8 BOM or encoding cookie, according to [**PEP 263**](https://peps.python.org/pep-0263/).

tokenize.generate_tokens(_readline_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.generate_tokens "Link to this definition")

Tokenize a source reading unicode strings instead of bytes.
Like [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize"), the _readline_ argument is a callable returning a single line of input. However, `generate_tokens()` expects _readline_ to return a str object rather than bytes.
The result is an iterator yielding named tuples, exactly like [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize"). It does not yield an [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING") token.
All constants from the [`token`](https://docs.python.org/3/library/token.html#module-token "token: Constants representing terminal nodes of the parse tree.") module are also exported from `tokenize`.
Another function is provided to reverse the tokenization process. This is useful for creating tools that tokenize a script, modify the token stream, and write back the modified script.

tokenize.untokenize(_iterable_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.untokenize "Link to this definition")

Converts tokens back into Python source code. The _iterable_ must return sequences with at least two elements, the token type and the token string. Any additional sequence elements are ignored.
The result is guaranteed to tokenize back to match the input so that the conversion is lossless and round-trips are assured. The guarantee applies only to the token type and token string as the spacing between tokens (column positions) may change.
It returns bytes, encoded using the [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING") token, which is the first token sequence output by [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize"). If there is no encoding token in the input, it returns a str instead.
[`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize") needs to detect the encoding of source files it tokenizes. The function it uses to do this is available:

tokenize.detect_encoding(_readline_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.detect_encoding "Link to this definition")

The `detect_encoding()` function is used to detect the encoding that should be used to decode a Python source file. It requires one argument, readline, in the same way as the [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize") generator.
It will call readline a maximum of twice, and return the encoding used (as a string) and a list of any lines (not decoded from bytes) it has read in.
It detects the encoding from the presence of a UTF-8 BOM or an encoding cookie as specified in [**PEP 263**](https://peps.python.org/pep-0263/). If both a BOM and a cookie are present, but disagree, a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") will be raised. Note that if the BOM is found, `'utf-8-sig'` will be returned as an encoding.
If no encoding is specified, then the default of `'utf-8'` will be returned.
Use [`open()`](https://docs.python.org/3/library/tokenize.html#tokenize.open "tokenize.open") to open Python source files: it uses `detect_encoding()` to detect the file encoding.

tokenize.open(_filename_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.open "Link to this definition")

Open a file in read only mode using the encoding detected by [`detect_encoding()`](https://docs.python.org/3/library/tokenize.html#tokenize.detect_encoding "tokenize.detect_encoding").
Added in version 3.2.

_exception_ tokenize.TokenError[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenError "Link to this definition")

Raised when either a docstring or expression that may be split over several lines is not completed anywhere in the file, for example:
Copy```
"""Beginning of
docstring

```

or:
Copy```
[1,
 2,
 3

```

## Command-Line Usage[¶](https://docs.python.org/3/library/tokenize.html#command-line-usage "Link to this heading")
Added in version 3.3.
The `tokenize` module can be executed as a script from the command line. It is as simple as:
Copy```
python -m tokenize [-e] [filename.py]

```

The following options are accepted:

-h, --help[¶](https://docs.python.org/3/library/tokenize.html#cmdoption-tokenize-h "Link to this definition")

show this help message and exit

-e, --exact[¶](https://docs.python.org/3/library/tokenize.html#cmdoption-tokenize-e "Link to this definition")

display token names using the exact type
If `filename.py` is specified its contents are tokenized to stdout. Otherwise, tokenization is performed on stdin.
## Examples[¶](https://docs.python.org/3/library/tokenize.html#examples "Link to this heading")
Example of a script rewriter that transforms float literals into Decimal objects:
Copy```
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO

def decistmt(s):
    """Substitute Decimals for floats in a string of statements.

    >>> from decimal import Decimal
    >>> s = 'print(+21.3e-5*-.1234/81.7)'
    >>> decistmt(s)
    "print (+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7'))"

    The format of the exponent is inherited from the platform C library.
    Known cases are "e-007" (Windows) and "e-07" (not Windows).  Since
    we're only showing 12 digits, and the 13th isn't close to 5, the
    rest of the output should be platform-independent.

    >>> exec(s)  #doctest: +ELLIPSIS
    -3.21716034272e-0...7

    Output from calculations with Decimal should be identical across all
    platforms.

    >>> exec(decistmt(s))
    -3.217160342717258261933904529E-7
    """
    result = []
    g = tokenize(BytesIO(s.encode('utf-8')).readline)  # tokenize the string
    for toknum, tokval, _, _, _ in g:
        if toknum == NUMBER and '.' in tokval:  # replace NUMBER tokens
            result.extend([
                (NAME, 'Decimal'),
                (OP, '('),
                (STRING, repr(tokval)),
                (OP, ')')
            ])
        else:
            result.append((toknum, tokval))
    return untokenize(result).decode('utf-8')

```

Example of tokenizing from the command line. The script:
Copy```
def say_hello():
    print("Hello, World!")

say_hello()

```

will be tokenized to the following output where the first column is the range of the line/column coordinates where the token is found, the second column is the name of the token, and the final column is the value of the token (if any)
Copy```
$ python -m tokenize hello.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,13:           NAME           'say_hello'
1,13-1,14:          OP             '('
1,14-1,15:          OP             ')'
1,15-1,16:          OP             ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,9:            NAME           'print'
2,9-2,10:           OP             '('
2,10-2,25:          STRING         '"Hello, World!"'
2,25-2,26:          OP             ')'
2,26-2,27:          NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,9:            NAME           'say_hello'
4,9-4,10:           OP             '('
4,10-4,11:          OP             ')'
4,11-4,12:          NEWLINE        '\n'
5,0-5,0:            ENDMARKER      ''

```

The exact token type names can be displayed using the [`-e`](https://docs.python.org/3/library/tokenize.html#cmdoption-tokenize-e) option:
Copy```
$ python -m tokenize -e hello.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,13:           NAME           'say_hello'
1,13-1,14:          LPAR           '('
1,14-1,15:          RPAR           ')'
1,15-1,16:          COLON          ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,9:            NAME           'print'
2,9-2,10:           LPAR           '('
2,10-2,25:          STRING         '"Hello, World!"'
2,25-2,26:          RPAR           ')'
2,26-2,27:          NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,9:            NAME           'say_hello'
4,9-4,10:           LPAR           '('
4,10-4,11:          RPAR           ')'
4,11-4,12:          NEWLINE        '\n'
5,0-5,0:            ENDMARKER      ''

```

Example of tokenizing a file programmatically, reading unicode strings instead of bytes with [`generate_tokens()`](https://docs.python.org/3/library/tokenize.html#tokenize.generate_tokens "tokenize.generate_tokens"):
Copy```
import tokenize

with tokenize.open('hello.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)

```

Or reading bytes directly with [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize"):
Copy```
import tokenize

with open('hello.py', 'rb') as f:
    tokens = tokenize.tokenize(f.readline)
    for token in tokens:
        print(token)

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
    * [Tokenizing Input](https://docs.python.org/3/library/tokenize.html#tokenizing-input)
    * [Command-Line Usage](https://docs.python.org/3/library/tokenize.html#command-line-usage)
    * [Examples](https://docs.python.org/3/library/tokenize.html#examples)


#### Previous topic
[`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html "previous chapter")
#### Next topic
[`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tokenize+%E2%80%94+Tokenizer+for+Python+source&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftokenize.html&pagesource=library%2Ftokenize.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tabnanny.html "tabnanny — Detection of ambiguous indentation") |
  * [previous](https://docs.python.org/3/library/keyword.html "keyword — Testing for Python keywords") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
