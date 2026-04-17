## Template strings ($-strings)[¶](https://docs.python.org/3/library/string.html#template-strings-strings "Link to this heading")
Note
The feature described here was introduced in Python 2.4; a simple templating method based upon regular expressions. It predates [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"), [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings), and [template string literals](https://docs.python.org/3/library/string.templatelib.html#template-strings).
It is unrelated to template string literals (t-strings), which were introduced in Python 3.14. These evaluate to [`string.templatelib.Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template") objects, found in the [`string.templatelib`](https://docs.python.org/3/library/string.templatelib.html#module-string.templatelib "string.templatelib: Support for template string literals.") module.
Template strings provide simpler string substitutions as described in [**PEP 292**](https://peps.python.org/pep-0292/). A primary use case for template strings is for internationalization (i18n) since in that context, the simpler syntax and functionality makes it easier to translate than other built-in string formatting facilities in Python. As an example of a library built on template strings for i18n, see the
Template strings support `$`-based substitutions, using the following rules:
  * `$$` is an escape; it is replaced with a single `$`.
  * `$identifier` names a substitution placeholder matching a mapping key of `"identifier"`. By default, `"identifier"` is restricted to any case-insensitive ASCII alphanumeric string (including underscores) that starts with an underscore or ASCII letter. The first non-identifier character after the `$` character terminates this placeholder specification.
  * `${identifier}` is equivalent to `$identifier`. It is required when valid identifier characters follow the placeholder but are not part of the placeholder, such as `"${noun}ification"`.


Any other appearance of `$` in the string will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") being raised.
The `string` module provides a [`Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template") class that implements these rules. The methods of `Template` are:

_class_ string.Template(_template_)[¶](https://docs.python.org/3/library/string.html#string.Template "Link to this definition")

The constructor takes a single argument which is the template string.

substitute(_mapping ={}_, _/_ , _** kwds_)[¶](https://docs.python.org/3/library/string.html#string.Template.substitute "Link to this definition")

Performs the template substitution, returning a new string. _mapping_ is any dictionary-like object with keys that match the placeholders in the template. Alternatively, you can provide keyword arguments, where the keywords are the placeholders. When both _mapping_ and _kwds_ are given and there are duplicates, the placeholders from _kwds_ take precedence.

safe_substitute(_mapping ={}_, _/_ , _** kwds_)[¶](https://docs.python.org/3/library/string.html#string.Template.safe_substitute "Link to this definition")

Like [`substitute()`](https://docs.python.org/3/library/string.html#string.Template.substitute "string.Template.substitute"), except that if placeholders are missing from _mapping_ and _kwds_ , instead of raising a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception, the original placeholder will appear in the resulting string intact. Also, unlike with `substitute()`, any other appearances of the `$` will simply return `$` instead of raising [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
While other exceptions may still occur, this method is called “safe” because it always tries to return a usable string instead of raising an exception. In another sense, `safe_substitute()` may be anything other than safe, since it will silently ignore malformed templates containing dangling delimiters, unmatched braces, or placeholders that are not valid Python identifiers.

is_valid()[¶](https://docs.python.org/3/library/string.html#string.Template.is_valid "Link to this definition")

Returns `False` if the template has invalid placeholders that will cause [`substitute()`](https://docs.python.org/3/library/string.html#string.Template.substitute "string.Template.substitute") to raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
Added in version 3.11.

get_identifiers()[¶](https://docs.python.org/3/library/string.html#string.Template.get_identifiers "Link to this definition")

Returns a list of the valid identifiers in the template, in the order they first appear, ignoring any invalid identifiers.
Added in version 3.11.
`Template` instances also provide one public data attribute:

template[¶](https://docs.python.org/3/library/string.html#string.Template.template "Link to this definition")

This is the object passed to the constructor’s _template_ argument. In general, you shouldn’t change it, but read-only access is not enforced.
Here is an example of how to use a Template:
Copy```
>>> from string import Template
>>> s = Template('$who likes $what')
>>> s.substitute(who='tim', what='kung pao')
'tim likes kung pao'
>>> d = dict(who='tim')
>>> Template('Give $who $100').substitute(d)
Traceback (most recent call last):
...
ValueError: Invalid placeholder in string: line 1, col 11
>>> Template('$who likes $what').substitute(d)
Traceback (most recent call last):
...
KeyError: 'what'
>>> Template('$who likes $what').safe_substitute(d)
'tim likes $what'

```

Advanced usage: you can derive subclasses of [`Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template") to customize the placeholder syntax, delimiter character, or the entire regular expression used to parse template strings. To do this, you can override these class attributes:
  * _delimiter_ – This is the literal string describing a placeholder introducing delimiter. The default value is `$`. Note that this should _not_ be a regular expression, as the implementation will call [`re.escape()`](https://docs.python.org/3/library/re.html#re.escape "re.escape") on this string as needed. Note further that you cannot change the delimiter after class creation (i.e. a different delimiter must be set in the subclass’s class namespace).
  * _idpattern_ – This is the regular expression describing the pattern for non-braced placeholders. The default value is the regular expression `(?a:[_a-z][_a-z0-9]*)`. If this is given and _braceidpattern_ is `None` this pattern will also apply to braced placeholders.
Note
Since default _flags_ is `re.IGNORECASE`, pattern `[a-z]` can match with some non-ASCII characters. That’s why we use the local `a` flag here.
Changed in version 3.7: _braceidpattern_ can be used to define separate patterns used inside and outside the braces.
  * _braceidpattern_ – This is like _idpattern_ but describes the pattern for braced placeholders. Defaults to `None` which means to fall back to _idpattern_ (i.e. the same pattern is used both inside and outside braces). If given, this allows you to define different patterns for braced and unbraced placeholders.
Added in version 3.7.
  * _flags_ – The regular expression flags that will be applied when compiling the regular expression used for recognizing substitutions. The default value is `re.IGNORECASE`. Note that `re.VERBOSE` will always be added to the flags, so custom _idpattern_ s must follow conventions for verbose regular expressions.
Added in version 3.2.


Alternatively, you can provide the entire regular expression pattern by overriding the class attribute _pattern_. If you do this, the value must be a regular expression object with four named capturing groups. The capturing groups correspond to the rules given above, along with the invalid placeholder rule:
  * _escaped_ – This group matches the escape sequence, e.g. `$$`, in the default pattern.
  * _named_ – This group matches the unbraced placeholder name; it should not include the delimiter in capturing group.
  * _braced_ – This group matches the brace enclosed placeholder name; it should not include either the delimiter or braces in the capturing group.
  * _invalid_ – This group matches any other delimiter pattern (usually a single delimiter), and it should appear last in the regular expression.


The methods on this class will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the pattern matches the template without one of these named groups matching.
## Helper functions[¶](https://docs.python.org/3/library/string.html#helper-functions "Link to this heading")

string.capwords(_s_ , _sep =None_)[¶](https://docs.python.org/3/library/string.html#string.capwords "Link to this definition")

Split the argument into words using [`str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split "str.split"), capitalize each word using [`str.capitalize()`](https://docs.python.org/3/library/stdtypes.html#str.capitalize "str.capitalize"), and join the capitalized words using [`str.join()`](https://docs.python.org/3/library/stdtypes.html#str.join "str.join"). If the optional second argument _sep_ is absent or `None`, runs of whitespace characters are replaced by a single space and leading and trailing whitespace are removed, otherwise _sep_ is used to split and join the words.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`string` — Common string operations](https://docs.python.org/3/library/string.html)
    * [String constants](https://docs.python.org/3/library/string.html#string-constants)
    * [Custom String Formatting](https://docs.python.org/3/library/string.html#custom-string-formatting)
    * [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
      * [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
      * [Format examples](https://docs.python.org/3/library/string.html#format-examples)
    * [Template strings ($-strings)](https://docs.python.org/3/library/string.html#template-strings-strings)
    * [Helper functions](https://docs.python.org/3/library/string.html#helper-functions)


#### Previous topic
[Text Processing Services](https://docs.python.org/3/library/text.html "previous chapter")
#### Next topic
[`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=string+%E2%80%94+Common+string+operations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstring.html&pagesource=library%2Fstring.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/string.templatelib.html "string.templatelib — Support for template string literals") |
  * [previous](https://docs.python.org/3/library/text.html "Text Processing Services") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`string` — Common string operations](https://docs.python.org/3/library/string.html)
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
