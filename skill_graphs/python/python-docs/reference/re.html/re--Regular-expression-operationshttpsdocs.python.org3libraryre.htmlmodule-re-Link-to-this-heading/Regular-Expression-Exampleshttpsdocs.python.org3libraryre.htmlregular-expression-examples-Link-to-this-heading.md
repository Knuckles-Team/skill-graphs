## Regular Expression Examples[¶](https://docs.python.org/3/library/re.html#regular-expression-examples "Link to this heading")
### Checking for a Pair[¶](https://docs.python.org/3/library/re.html#checking-for-a-pair "Link to this heading")
In this example, we’ll use the following helper function to display match objects a little more gracefully:
Copy```
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

```

Suppose you are writing a poker program where a player’s hand is represented as a 5-character string with each character representing a card, “a” for ace, “k” for king, “q” for queen, “j” for jack, “t” for 10, and “2” through “9” representing the card with that value.
To see if a given string is a valid hand, one could do the following:
Copy```
>>> valid = re.compile(r"^[a2-9tjqk]{5}$")
>>> displaymatch(valid.match("akt5q"))  # Valid.
"<Match: 'akt5q', groups=()>"
>>> displaymatch(valid.match("akt5e"))  # Invalid.
>>> displaymatch(valid.match("akt"))    # Invalid.
>>> displaymatch(valid.match("727ak"))  # Valid.
"<Match: '727ak', groups=()>"

```

That last hand, `"727ak"`, contained a pair, or two of the same valued cards. To match this with a regular expression, one could use backreferences as such:
Copy```
>>> pair = re.compile(r".*(.).*\1")
>>> displaymatch(pair.match("717ak"))     # Pair of 7s.
"<Match: '717', groups=('7',)>"
>>> displaymatch(pair.match("718ak"))     # No pairs.
>>> displaymatch(pair.match("354aa"))     # Pair of aces.
"<Match: '354aa', groups=('a',)>"

```

To find out what card the pair consists of, one could use the [`group()`](https://docs.python.org/3/library/re.html#re.Match.group "re.Match.group") method of the match object in the following manner:
Copy```
>>> pair = re.compile(r".*(.).*\1")
>>> pair.match("717ak").group(1)
'7'

# Error because re.match() returns None, which doesn't have a group() method:
>>> pair.match("718ak").group(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    re.match(r".*(.).*\1", "718ak").group(1)
AttributeError: 'NoneType' object has no attribute 'group'

>>> pair.match("354aa").group(1)
'a'

```

### Simulating scanf()[¶](https://docs.python.org/3/library/re.html#simulating-scanf "Link to this heading")
Python does not currently have an equivalent to `scanf()`. Regular expressions are generally more powerful, though also more verbose, than `scanf()` format strings. The table below offers some more-or-less equivalent mappings between `scanf()` format tokens and regular expressions.
`scanf()` Token | Regular Expression
---|---
`%c` | `.`
`%5c` | `.{5}`
`%d` | `[-+]?\d+`
`%e`, `%E`, `%f`, `%g` | `[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?`
`%i` | `[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)`
`%o` | `[-+]?[0-7]+`
`%s` | `\S+`
`%u` | `\d+`
`%x`, `%X` | `[-+]?(0[xX])?[\dA-Fa-f]+`
To extract the filename and numbers from a string like
Copy```
/usr/sbin/sendmail - 0 errors, 4 warnings

```

you would use a `scanf()` format like
Copy```
%s - %d errors, %d warnings

```

The equivalent regular expression would be
Copy```
(\S+) - (\d+) errors, (\d+) warnings

```

### search() vs. match()[¶](https://docs.python.org/3/library/re.html#search-vs-match "Link to this heading")
Python offers different primitive operations based on regular expressions:
  * [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match") checks for a match only at the beginning of the string
  * [`re.search()`](https://docs.python.org/3/library/re.html#re.search "re.search") checks for a match anywhere in the string (this is what Perl does by default)
  * [`re.fullmatch()`](https://docs.python.org/3/library/re.html#re.fullmatch "re.fullmatch") checks for entire string to be a match


For example:
Copy```
>>> re.match("c", "abcdef")    # No match
>>> re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
>>> re.fullmatch("p.*n", "python") # Match
<re.Match object; span=(0, 6), match='python'>
>>> re.fullmatch("r.*n", "python") # No match

```

Regular expressions beginning with `'^'` can be used with [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") to restrict the match at the beginning of the string:
Copy```
>>> re.match("c", "abcdef")    # No match
>>> re.search("^c", "abcdef")  # No match
>>> re.search("^a", "abcdef")  # Match
<re.Match object; span=(0, 1), match='a'>

```

Note however that in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode [`match()`](https://docs.python.org/3/library/re.html#re.match "re.match") only matches at the beginning of the string, whereas using [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") with a regular expression beginning with `'^'` will match at the beginning of each line.
Copy```
>>> re.match("X", "A\nB\nX", re.MULTILINE)  # No match
>>> re.search("^X", "A\nB\nX", re.MULTILINE)  # Match
<re.Match object; span=(4, 5), match='X'>

```

### Making a Phonebook[¶](https://docs.python.org/3/library/re.html#making-a-phonebook "Link to this heading")
[`split()`](https://docs.python.org/3/library/re.html#re.split "re.split") splits a string into a list delimited by the passed pattern. The method is invaluable for converting textual data into data structures that can be easily read and modified by Python as demonstrated in the following example that creates a phonebook.
First, here is the input. Normally it may come from a file, here we are using triple-quoted string syntax
Copy```
>>> text = """Ross McFluff: 834.345.1254 155 Elm Street
...
... Ronald Heathmore: 892.345.3428 436 Finley Avenue
... Frank Burger: 925.541.7625 662 South Dogwood Way
...
...
... Heather Albrecht: 548.326.4584 919 Park Place"""

```

The entries are separated by one or more newlines. Now we convert the string into a list with each nonempty line having its own entry:
Copy```
>>> entries = re.split("\n+", text)
>>> entries
['Ross McFluff: 834.345.1254 155 Elm Street',
'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
'Frank Burger: 925.541.7625 662 South Dogwood Way',
'Heather Albrecht: 548.326.4584 919 Park Place']

```

Finally, split each entry into a list with first name, last name, telephone number, and address. We use the `maxsplit` parameter of [`split()`](https://docs.python.org/3/library/re.html#re.split "re.split") because the address has spaces, our splitting pattern, in it:
Copy```
>>> [re.split(":? ", entry, maxsplit=3) for entry in entries]
[['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],
['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

```

The `:?` pattern matches the colon after the last name, so that it does not occur in the result list. With a `maxsplit` of `4`, we could separate the house number from the street name:
Copy```
>>> [re.split(":? ", entry, maxsplit=4) for entry in entries]
[['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]

```

### Text Munging[¶](https://docs.python.org/3/library/re.html#text-munging "Link to this heading")
[`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub") replaces every occurrence of a pattern with a string or the result of a function. This example demonstrates using `sub()` with a function to “munge” text, or randomize the order of all the characters in each word of a sentence except for the first and last characters:
Copy```
>>> def repl(m):
...     inner_word = list(m.group(2))
...     random.shuffle(inner_word)
...     return m.group(1) + "".join(inner_word) + m.group(3)
...
>>> text = "Professor Abdolmalek, please report your absences promptly."
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pofsroser Aodlambelk, plasee report your asnebces potlmrpy.'

```

### Finding all Adverbs[¶](https://docs.python.org/3/library/re.html#finding-all-adverbs "Link to this heading")
[`findall()`](https://docs.python.org/3/library/re.html#re.findall "re.findall") matches _all_ occurrences of a pattern, not just the first one as [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") does. For example, if a writer wanted to find all of the adverbs in some text, they might use `findall()` in the following manner:
Copy```
>>> text = "He was carefully disguised but captured quickly by police."
>>> re.findall(r"\w+ly\b", text)
['carefully', 'quickly']

```

### Finding all Adverbs and their Positions[¶](https://docs.python.org/3/library/re.html#finding-all-adverbs-and-their-positions "Link to this heading")
If one wants more information about all matches of a pattern than the matched text, [`finditer()`](https://docs.python.org/3/library/re.html#re.finditer "re.finditer") is useful as it provides [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match") objects instead of strings. Continuing with the previous example, if a writer wanted to find all of the adverbs _and their positions_ in some text, they would use `finditer()` in the following manner:
Copy```
>>> text = "He was carefully disguised but captured quickly by police."
>>> for m in re.finditer(r"\w+ly\b", text):
...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
07-16: carefully
40-47: quickly

```

### Raw String Notation[¶](https://docs.python.org/3/library/re.html#raw-string-notation "Link to this heading")
Raw string notation (`r"text"`) keeps regular expressions sane. Without it, every backslash (`'\'`) in a regular expression would have to be prefixed with another one to escape it. For example, the two following lines of code are functionally identical:
Copy```
>>> re.match(r"\W(.)\1\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
>>> re.match("\\W(.)\\1\\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>

```

When one wants to match a literal backslash, it must be escaped in the regular expression. With raw string notation, this means `r"\\"`. Without raw string notation, one must use `"\\\\"`, making the following lines of code functionally identical:
Copy```
>>> re.match(r"\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>
>>> re.match("\\\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>

```

### Writing a Tokenizer[¶](https://docs.python.org/3/library/re.html#writing-a-tokenizer "Link to this heading")
A
The text categories are specified with regular expressions. The technique is to combine those into a single master regular expression and to loop over successive matches:
Copy```
from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)

```

The tokenizer produces the following output:
Copy```
Token(type='IF', value='IF', line=2, column=4)
Token(type='ID', value='quantity', line=2, column=7)
Token(type='THEN', value='THEN', line=2, column=16)
Token(type='ID', value='total', line=3, column=8)
Token(type='ASSIGN', value=':=', line=3, column=14)
Token(type='ID', value='total', line=3, column=17)
Token(type='OP', value='+', line=3, column=23)
Token(type='ID', value='price', line=3, column=25)
Token(type='OP', value='*', line=3, column=31)
Token(type='ID', value='quantity', line=3, column=33)
Token(type='END', value=';', line=3, column=41)
Token(type='ID', value='tax', line=4, column=8)
Token(type='ASSIGN', value=':=', line=4, column=12)
Token(type='ID', value='price', line=4, column=15)
Token(type='OP', value='*', line=4, column=21)
Token(type='NUMBER', value=0.05, line=4, column=23)
Token(type='END', value=';', line=4, column=27)
Token(type='ENDIF', value='ENDIF', line=5, column=4)
Token(type='END', value=';', line=5, column=9)

```

[[Frie09](https://docs.python.org/3/library/re.html#id1)]
Friedl, Jeffrey. Mastering Regular Expressions. 3rd ed., O’Reilly Media, 2009. The third edition of the book no longer covers Python at all, but the first edition covered writing good regular expression patterns in great detail.
### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html "previous chapter")
#### Next topic
[`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=re+%E2%80%94+Regular+expression+operations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fre.html&pagesource=library%2Fre.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/difflib.html "difflib — Helpers for computing deltas") |
  * [previous](https://docs.python.org/3/library/string.templatelib.html "string.templatelib — Support for template string literals") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`re` — Regular expression operations](https://docs.python.org/3/library/re.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
