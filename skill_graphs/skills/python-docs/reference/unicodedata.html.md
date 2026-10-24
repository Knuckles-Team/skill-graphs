[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html "previous chapter")
#### Next topic
[`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unicodedata+%E2%80%94+Unicode+Database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funicodedata.html&pagesource=library%2Funicodedata.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/stringprep.html "stringprep — Internet String Preparation") |
  * [previous](https://docs.python.org/3/library/textwrap.html "textwrap — Text wrapping and filling") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
  * |
  * Theme  Auto Light Dark |


#  `unicodedata` — Unicode Database[¶](https://docs.python.org/3/library/unicodedata.html#module-unicodedata "Link to this heading")
* * *
This module provides access to the Unicode Character Database (UCD) which defines character properties for all Unicode characters. The data contained in this database is compiled from the
The module uses the same names and symbols as defined by Unicode Standard Annex #44,
See also
The [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto) for more information about Unicode and how to use this module.

unicodedata.lookup(_name_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.lookup "Link to this definition")

Look up character by name. If a character with the given name is found, return the corresponding character. If not found, [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised. For example:
Copy```
>>> unicodedata.lookup('LEFT CURLY BRACKET')
'{'

```

The characters returned by this function are the same as those produced by `\N` escape sequence in string literals. For example:
Copy```
>>> unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}'
True

```

Changed in version 3.3: Support for name aliases [[1]](https://docs.python.org/3/library/unicodedata.html#id3) and named sequences [[2]](https://docs.python.org/3/library/unicodedata.html#id4) has been added.

unicodedata.name(_chr_ , _default =None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.name "Link to this definition")

Returns the name assigned to the character _chr_ as a string. If no name is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. For example:
Copy```
>>> unicodedata.name('½')
'VULGAR FRACTION ONE HALF'
>>> unicodedata.name('\uFFFF', 'fallback')
'fallback'

```


unicodedata.decimal(_chr_ , _default =None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.decimal "Link to this definition")

Returns the decimal value assigned to the character _chr_ as integer. If no such value is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. For example:
Copy```
>>> unicodedata.decimal('\N{ARABIC-INDIC DIGIT NINE}')
9
>>> unicodedata.decimal('\N{SUPERSCRIPT NINE}', -1)
-1

```


unicodedata.digit(_chr_ , _default =None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.digit "Link to this definition")

Returns the digit value assigned to the character _chr_ as integer. If no such value is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised:
Copy```
>>> unicodedata.digit('\N{SUPERSCRIPT NINE}')
9

```


unicodedata.numeric(_chr_ , _default =None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.numeric "Link to this definition")

Returns the numeric value assigned to the character _chr_ as float. If no such value is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised:
Copy```
>>> unicodedata.numeric('½')
0.5

```


unicodedata.category(_chr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.category "Link to this definition")

Returns the general category assigned to the character _chr_ as string. General category names consist of two letters. See the
Copy```
>>> unicodedata.category('A')  # 'L'etter, 'u'ppercase
'Lu'

```


unicodedata.bidirectional(_chr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.bidirectional "Link to this definition")

Returns the bidirectional class assigned to the character _chr_ as string. If no such value is defined, an empty string is returned. See the
Copy```
>>> unicodedata.bidirectional('\N{ARABIC-INDIC DIGIT SEVEN}') # 'A'rabic, 'N'umber
'AN'

```


unicodedata.combining(_chr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.combining "Link to this definition")

Returns the canonical combining class assigned to the character _chr_ as integer. Returns `0` if no combining class is defined. See the

unicodedata.east_asian_width(_chr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.east_asian_width "Link to this definition")

Returns the east asian width assigned to the character _chr_ as string. For a list of widths and or more information, see the

unicodedata.mirrored(_chr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.mirrored "Link to this definition")

Returns the mirrored property assigned to the character _chr_ as integer. Returns `1` if the character has been identified as a “mirrored” character in bidirectional text, `0` otherwise. For example:
Copy```
>>> unicodedata.mirrored('>')
1

```


unicodedata.decomposition(_chr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.decomposition "Link to this definition")

Returns the character decomposition mapping assigned to the character _chr_ as string. An empty string is returned in case no such mapping is defined. For example:
Copy```
>>> unicodedata.decomposition('Ã')
'0041 0303'

```


unicodedata.normalize(_form_ , _unistr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "Link to this definition")

Return the normal form _form_ for the Unicode string _unistr_. Valid values for _form_ are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.
The Unicode standard defines various normalization forms of a Unicode string, based on the definition of canonical equivalence and compatibility equivalence. In Unicode, several characters can be expressed in various way. For example, the character U+00C7 (LATIN CAPITAL LETTER C WITH CEDILLA) can also be expressed as the sequence U+0043 (LATIN CAPITAL LETTER C) U+0327 (COMBINING CEDILLA).
For each character, there are two normal forms: normal form C and normal form D. Normal form D (NFD) is also known as canonical decomposition, and translates each character into its decomposed form. Normal form C (NFC) first applies a canonical decomposition, then composes pre-combined characters again.
In addition to these two forms, there are two additional normal forms based on compatibility equivalence. In Unicode, certain characters are supported which normally would be unified with other characters. For example, U+2160 (ROMAN NUMERAL ONE) is really the same thing as U+0049 (LATIN CAPITAL LETTER I). However, it is supported in Unicode for compatibility with existing character sets (for example, gb2312).
The normal form KD (NFKD) will apply the compatibility decomposition, that is, replace all compatibility characters with their equivalents. The normal form KC (NFKC) first applies the compatibility decomposition, followed by the canonical composition.
Even if two unicode strings are normalized and look the same to a human reader, if one has combining characters and the other doesn’t, they may not compare equal.

unicodedata.is_normalized(_form_ , _unistr_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.is_normalized "Link to this definition")

Return whether the Unicode string _unistr_ is in the normal form _form_. Valid values for _form_ are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.
Added in version 3.8.
In addition, the module exposes the following constant:

unicodedata.unidata_version[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.unidata_version "Link to this definition")

The version of the Unicode database used in this module.

unicodedata.ucd_3_2_0[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.ucd_3_2_0 "Link to this definition")

This is an object that has the same methods as the entire module, but uses the Unicode database version 3.2 instead, for applications that require this specific version of the Unicode database (such as IDNA).
Footnotes
[[1](https://docs.python.org/3/library/unicodedata.html#id1)] [[2](https://docs.python.org/3/library/unicodedata.html#id2)]
#### Previous topic
[`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html "previous chapter")
#### Next topic
[`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unicodedata+%E2%80%94+Unicode+Database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funicodedata.html&pagesource=library%2Funicodedata.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/stringprep.html "stringprep — Internet String Preparation") |
  * [previous](https://docs.python.org/3/library/textwrap.html "textwrap — Text wrapping and filling") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
