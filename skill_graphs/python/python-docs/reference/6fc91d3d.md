Changed in version 3.3: The `'\u'` and `'\U'` escape sequences have been added.
Changed in version 3.6: Unknown escapes consisting of `'\'` and an ASCII letter now are errors.
Changed in version 3.8: The `'\N{_name_}'`escape sequence has been added. As in string literals, it expands to the named Unicode character (e.g.`'\N{EM DASH}'`).
## Module Contents[¶](https://docs.python.org/3/library/re.html#module-contents "Link to this heading")
The module defines several functions, constants, and an exception. Some of the functions are simplified versions of the full featured methods for compiled regular expressions. Most non-trivial applications always use the compiled form.
### Flags[¶](https://docs.python.org/3/library/re.html#flags "Link to this heading")
Changed in version 3.6: Flag constants are now instances of [`RegexFlag`](https://docs.python.org/3/library/re.html#re.RegexFlag "re.RegexFlag"), which is a subclass of [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag").

_class_ re.RegexFlag[¶](https://docs.python.org/3/library/re.html#re.RegexFlag "Link to this definition")

An [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") class containing the regex options listed below.
Added in version 3.11: - added to `__all__`

re.A[¶](https://docs.python.org/3/library/re.html#re.A "Link to this definition")


re.ASCII[¶](https://docs.python.org/3/library/re.html#re.ASCII "Link to this definition")

Make `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s` and `\S` perform ASCII-only matching instead of full Unicode matching. This is only meaningful for Unicode (str) patterns, and is ignored for bytes patterns.
Corresponds to the inline flag `(?a)`.
Note
The [`U`](https://docs.python.org/3/library/re.html#re.U "re.U") flag still exists for backward compatibility, but is redundant in Python 3 since matches are Unicode by default for `str` patterns, and Unicode matching isn’t allowed for bytes patterns. [`UNICODE`](https://docs.python.org/3/library/re.html#re.UNICODE "re.UNICODE") and the inline flag `(?u)` are similarly redundant.

re.DEBUG[¶](https://docs.python.org/3/library/re.html#re.DEBUG "Link to this definition")

Display debug information about compiled expression.
No corresponding inline flag.

re.I[¶](https://docs.python.org/3/library/re.html#re.I "Link to this definition")


re.IGNORECASE[¶](https://docs.python.org/3/library/re.html#re.IGNORECASE "Link to this definition")

Perform case-insensitive matching; expressions like `[A-Z]` will also match lowercase letters. Full Unicode matching (such as `Ü` matching `ü`) also works unless the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used to disable non-ASCII matches. The current locale does not change the effect of this flag unless the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag is also used.
Corresponds to the inline flag `(?i)`.
Note that when the Unicode patterns `[a-z]` or `[A-Z]` are used in combination with the [`IGNORECASE`](https://docs.python.org/3/library/re.html#re.IGNORECASE "re.IGNORECASE") flag, they will match the 52 ASCII letters and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital letter I with dot above), ‘ı’ (U+0131, Latin small letter dotless i), ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin sign). If the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used, only letters ‘a’ to ‘z’ and ‘A’ to ‘Z’ are matched.

re.L[¶](https://docs.python.org/3/library/re.html#re.L "Link to this definition")


re.LOCALE[¶](https://docs.python.org/3/library/re.html#re.LOCALE "Link to this definition")

Make `\w`, `\W`, `\b`, `\B` and case-insensitive matching dependent on the current locale. This flag can be used only with bytes patterns.
Corresponds to the inline flag `(?L)`.
Warning
This flag is discouraged; consider Unicode matching instead. The locale mechanism is very unreliable as it only handles one “culture” at a time and only works with 8-bit locales. Unicode matching is enabled by default for Unicode (str) patterns and it is able to handle different locales and languages.
Changed in version 3.6: [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") can be used only with bytes patterns and is not compatible with [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII").
Changed in version 3.7: Compiled regular expression objects with the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag no longer depend on the locale at compile time. Only the locale at matching time affects the result of matching.

re.M[¶](https://docs.python.org/3/library/re.html#re.M "Link to this definition")


re.MULTILINE[¶](https://docs.python.org/3/library/re.html#re.MULTILINE "Link to this definition")

When specified, the pattern character `'^'` matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character `'$'` matches at the end of the string and at the end of each line (immediately preceding each newline). By default, `'^'` matches only at the beginning of the string, and `'$'` only at the end of the string and immediately before the newline (if any) at the end of the string.
Corresponds to the inline flag `(?m)`.

re.NOFLAG[¶](https://docs.python.org/3/library/re.html#re.NOFLAG "Link to this definition")

Indicates no flag being applied, the value is `0`. This flag may be used as a default value for a function keyword argument or as a base value that will be conditionally ORed with other flags. Example of use as a default value:
Copy```
def myfunc(text, flag=re.NOFLAG):
    return re.match(text, flag)

```

Added in version 3.11.

re.S[¶](https://docs.python.org/3/library/re.html#re.S "Link to this definition")


re.DOTALL[¶](https://docs.python.org/3/library/re.html#re.DOTALL "Link to this definition")

Make the `'.'` special character match any character at all, including a newline; without this flag, `'.'` will match anything _except_ a newline.
Corresponds to the inline flag `(?s)`.

re.U[¶](https://docs.python.org/3/library/re.html#re.U "Link to this definition")


re.UNICODE[¶](https://docs.python.org/3/library/re.html#re.UNICODE "Link to this definition")

In Python 3, Unicode characters are matched by default for `str` patterns. This flag is therefore redundant with **no effect** and is only kept for backward compatibility.
See [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") to restrict matching to ASCII characters instead.

re.X[¶](https://docs.python.org/3/library/re.html#re.X "Link to this definition")


re.VERBOSE[¶](https://docs.python.org/3/library/re.html#re.VERBOSE "Link to this definition")

This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like `*?`, `(?:` or `(?P<...>`. For example, `(? :` and `* ?` are not allowed. When a line contains a `#` that is not in a character class and is not preceded by an unescaped backslash, all characters from the leftmost such `#` through the end of the line are ignored.
This means that the two following regular expression objects that match a decimal number are functionally equal:
Copy```
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

```

Corresponds to the inline flag `(?x)`.
### Functions[¶](https://docs.python.org/3/library/re.html#functions "Link to this heading")

re.compile(_pattern_ , _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.compile "Link to this definition")

Compile a regular expression pattern into a [regular expression object](https://docs.python.org/3/library/re.html#re-objects), which can be used for matching using its [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match"), [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") and other methods, described below.
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).
The sequence
Copy```
prog = re.compile(pattern)
result = prog.match(string)

```

is equivalent to
Copy```
result = re.match(pattern, string)

```

but using [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile") and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.
Note
The compiled versions of the most recent patterns passed to [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile") and the module-level matching functions are cached, so programs that use only a few regular expressions at a time needn’t worry about compiling regular expressions.

re.search(_pattern_ , _string_ , _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.search "Link to this definition")

Scan through _string_ looking for the first location where the regular expression _pattern_ produces a match, and return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).

re.match(_pattern_ , _string_ , _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.match "Link to this definition")

If zero or more characters at the beginning of _string_ match the regular expression _pattern_ , return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if the string does not match the pattern; note that this is different from a zero-length match.
Note that even in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode, [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match") will only match at the beginning of the string and not at the beginning of each line.
If you want to locate a match anywhere in _string_ , use [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") instead (see also [search() vs. match()](https://docs.python.org/3/library/re.html#search-vs-match)).
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).

re.fullmatch(_pattern_ , _string_ , _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.fullmatch "Link to this definition")

If the whole _string_ matches the regular expression _pattern_ , return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if the string does not match the pattern; note that this is different from a zero-length match.
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).
Added in version 3.4.

re.split(_pattern_ , _string_ , _maxsplit =0_, _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.split "Link to this definition")

Split _string_ by the occurrences of _pattern_. If capturing parentheses are used in _pattern_ , then the text of all groups in the pattern are also returned as part of the resulting list. If _maxsplit_ is nonzero, at most _maxsplit_ splits occur, and the remainder of the string is returned as the final element of the list.
Copy```
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', maxsplit=1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']

```

If there are capturing groups in the separator and it matches at the start of the string, the result will start with an empty string. The same holds for the end of the string:
Copy```
>>> re.split(r'(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']

```

That way, separator components are always found at the same relative indices within the result list.
Adjacent empty matches are not possible, but an empty match can occur immediately after a non-empty match.
Copy```
>>> re.split(r'\b', 'Words, words, words.')
['', 'Words', ', ', 'words', ', ', 'words', '.']
>>> re.split(r'\W*', '...words...')
['', '', 'w', 'o', 'r', 'd', 's', '', '']
>>> re.split(r'(\W*)', '...words...')
['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']

```

The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).
Changed in version 3.1: Added the optional flags argument.
Changed in version 3.7: Added support of splitting on a pattern that could match an empty string.
Deprecated since version 3.13: Passing _maxsplit_ and _flags_ as positional arguments is deprecated. In future Python versions they will be [keyword-only parameters](https://docs.python.org/3/glossary.html#keyword-only-parameter).

re.findall(_pattern_ , _string_ , _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.findall "Link to this definition")

Return all non-overlapping matches of _pattern_ in _string_ , as a list of strings or tuples. The _string_ is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.
The result depends on the number of capturing groups in the pattern. If there are no groups, return a list of strings matching the whole pattern. If there is exactly one group, return a list of strings matching that group. If multiple groups are present, return a list of tuples of strings matching the groups. Non-capturing groups do not affect the form of the result.
Copy```
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]

```

The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).
Changed in version 3.7: Non-empty matches can now start just after a previous empty match.

re.finditer(_pattern_ , _string_ , _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.finditer "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) yielding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match") objects over all non-overlapping matches for the RE _pattern_ in _string_. The _string_ is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).
Changed in version 3.7: Non-empty matches can now start just after a previous empty match.

re.sub(_pattern_ , _repl_ , _string_ , _count =0_, _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.sub "Link to this definition")

Return the string obtained by replacing the leftmost non-overlapping occurrences of _pattern_ in _string_ by the replacement _repl_. If the pattern isn’t found, _string_ is returned unchanged. _repl_ can be a string or a function; if it is a string, any backslash escapes in it are processed. That is, `\n` is converted to a single newline character, `\r` is converted to a carriage return, and so forth. Unknown escapes of ASCII letters are reserved for future use and treated as errors. Other unknown escapes such as `\&` are left alone. Backreferences, such as `\6`, are replaced with the substring matched by group 6 in the pattern. For example:
Copy```
>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')
'static PyObject*\npy_myfunc(void)\n{'

```

If _repl_ is a function, it is called for every non-overlapping occurrence of _pattern_. The function takes a single [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match") argument, and returns the replacement string. For example:
Copy```
>>> def dashrepl(matchobj):
...     if matchobj.group(0) == '-': return ' '
...     else: return '-'
...
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'
>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
'Baked Beans & Spam'

```

The pattern may be a string or a [`Pattern`](https://docs.python.org/3/library/re.html#re.Pattern "re.Pattern").
The optional argument _count_ is the maximum number of pattern occurrences to be replaced; _count_ must be a non-negative integer. If omitted or zero, all occurrences will be replaced.
Adjacent empty matches are not possible, but an empty match can occur immediately after a non-empty match. As a result, `sub('x*', '-', 'abxd')` returns `'-a-b--d-'` instead of `'-a-b-d-'`.
In string-type _repl_ arguments, in addition to the character escapes and backreferences described above, `\g<name>` will use the substring matched by the group named `name`, as defined by the `(?P<name>...)` syntax. `\g<number>` uses the corresponding group number; `\g<2>` is therefore equivalent to `\2`, but isn’t ambiguous in a replacement such as `\g<2>0`. `\20` would be interpreted as a reference to group 20, not a reference to group 2 followed by the literal character `'0'`. The backreference `\g<0>` substitutes in the entire substring matched by the RE.
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).
Changed in version 3.1: Added the optional flags argument.
Changed in version 3.5: Unmatched groups are replaced with an empty string.
Changed in version 3.6: Unknown escapes in _pattern_ consisting of `'\'` and an ASCII letter now are errors.
Changed in version 3.7: Unknown escapes in _repl_ consisting of `'\'` and an ASCII letter now are errors. An empty match can occur immediately after a non-empty match.
Changed in version 3.12: Group _id_ can only contain ASCII digits. In [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") replacement strings, group _name_ can only contain bytes in the ASCII range (`b'\x00'`-`b'\x7f'`).
Deprecated since version 3.13: Passing _count_ and _flags_ as positional arguments is deprecated. In future Python versions they will be [keyword-only parameters](https://docs.python.org/3/glossary.html#keyword-only-parameter).

re.subn(_pattern_ , _repl_ , _string_ , _count =0_, _flags =0_)[¶](https://docs.python.org/3/library/re.html#re.subn "Link to this definition")

Perform the same operation as [`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub"), but return a tuple `(new_string, number_of_subs_made)`.
The expression’s behaviour can be modified by specifying a _flags_ value. Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR (the `|` operator).

re.escape(_pattern_)[¶](https://docs.python.org/3/library/re.html#re.escape "Link to this definition")

Escape special characters in _pattern_. This is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it. For example:
Copy```
>>> print(re.escape('https://www.python.org'))
https://www\.python\.org

>>> legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
>>> print('[%s]+' % re.escape(legal_chars))
[abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+

>>> operators = ['+', '-', '*', '/', '**']
>>> print('|'.join(map(re.escape, sorted(operators, reverse=True))))
/|\-|\+|\*\*|\*

```

This function must not be used for the replacement string in [`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub") and [`subn()`](https://docs.python.org/3/library/re.html#re.subn "re.subn"), only backslashes should be escaped. For example:
Copy```
>>> digits_re = r'\d+'
>>> sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
>>> print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
/usr/sbin/sendmail - \d+ errors, \d+ warnings

```

Changed in version 3.3: The `'_'` character is no longer escaped.
Changed in version 3.7: Only characters that can have special meaning in a regular expression are escaped. As a result, `'!'`, `'"'`, `'%'`, `"'"`, `','`, `'/'`, `':'`, `';'`, `'<'`, `'='`, `'>'`, `'@'`, and `"`"` are no longer escaped.

re.purge()[¶](https://docs.python.org/3/library/re.html#re.purge "Link to this definition")

Clear the regular expression cache.
### Exceptions[¶](https://docs.python.org/3/library/re.html#exceptions "Link to this heading")

_exception_ re.PatternError(_msg_ , _pattern =None_, _pos =None_)[¶](https://docs.python.org/3/library/re.html#re.PatternError "Link to this definition")

Exception raised when a string passed to one of the functions here is not a valid regular expression (for example, it might contain unmatched parentheses) or when some other error occurs during compilation or matching. It is never an error if a string contains no match for a pattern. The `PatternError` instance has the following additional attributes:

msg[¶](https://docs.python.org/3/library/re.html#re.PatternError.msg "Link to this definition")

The unformatted error message.

pattern[¶](https://docs.python.org/3/library/re.html#re.PatternError.pattern "Link to this definition")

The regular expression pattern.

pos[¶](https://docs.python.org/3/library/re.html#re.PatternError.pos "Link to this definition")

The index in _pattern_ where compilation failed (may be `None`).

lineno[¶](https://docs.python.org/3/library/re.html#re.PatternError.lineno "Link to this definition")

The line corresponding to _pos_ (may be `None`).

colno[¶](https://docs.python.org/3/library/re.html#re.PatternError.colno "Link to this definition")

The column corresponding to _pos_ (may be `None`).
Changed in version 3.5: Added additional attributes.
Changed in version 3.13: `PatternError` was originally named `error`; the latter is kept as an alias for backward compatibility.
## Regular Expression Objects[¶](https://docs.python.org/3/library/re.html#regular-expression-objects "Link to this heading")

_class_ re.Pattern[¶](https://docs.python.org/3/library/re.html#re.Pattern "Link to this definition")

Compiled regular expression object returned by [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile").
Changed in version 3.9: [`re.Pattern`](https://docs.python.org/3/library/re.html#re.Pattern "re.Pattern") supports `[]` to indicate a Unicode (str) or bytes pattern. See [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

Pattern.search(_string_[, _pos_[, _endpos_]])[¶](https://docs.python.org/3/library/re.html#re.Pattern.search "Link to this definition")

Scan through _string_ looking for the first location where this regular expression produces a match, and return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
The optional second parameter _pos_ gives an index in the string where the search is to start; it defaults to `0`. This is not completely equivalent to slicing the string; the `'^'` pattern character matches at the real beginning of the string and at positions just after a newline, but not necessarily at the index where the search is to start.
The optional parameter _endpos_ limits how far the string will be searched; it will be as if the string is _endpos_ characters long, so only the characters from _pos_ to `endpos - 1` will be searched for a match. If _endpos_ is less than _pos_ , no match will be found; otherwise, if _rx_ is a compiled regular expression object, `rx.search(string, 0, 50)` is equivalent to `rx.search(string[:50], 0)`.
Copy```
>>> pattern = re.compile("d")
>>> pattern.search("dog")     # Match at index 0
<re.Match object; span=(0, 1), match='d'>
>>> pattern.search("dog", 1)  # No match; search doesn't include the "d"
