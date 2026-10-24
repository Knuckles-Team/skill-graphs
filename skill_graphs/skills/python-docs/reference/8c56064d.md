## Regular Expression Syntax[¶](https://docs.python.org/3/library/re.html#regular-expression-syntax "Link to this heading")
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).
Regular expressions can be concatenated to form new regular expressions; if _A_ and _B_ are both regular expressions, then _AB_ is also a regular expression. In general, if a string _p_ matches _A_ and another string _q_ matches _B_ , the string _pq_ will match AB. This holds unless _A_ or _B_ contain low precedence operations; boundary conditions between _A_ and _B_ ; or have numbered group references. Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here. For details of the theory and implementation of regular expressions, consult the Friedl book [[Frie09]](https://docs.python.org/3/library/re.html#frie09), or almost any textbook about compiler construction.
A brief explanation of the format of regular expressions follows. For further information and a gentler presentation, consult the [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html#regex-howto).
Regular expressions can contain both special and ordinary characters. Most ordinary characters, like `'A'`, `'a'`, or `'0'`, are the simplest regular expressions; they simply match themselves. You can concatenate ordinary characters, so `last` matches the string `'last'`. (In the rest of this section, we’ll write RE’s in `this special style`, usually without quotes, and strings to be matched `'in single quotes'`.)
Some characters, like `'|'` or `'('`, are special. Special characters either stand for classes of ordinary characters, or affect how the regular expressions around them are interpreted.
Repetition operators or quantifiers (`*`, `+`, `?`, `{m,n}`, etc) cannot be directly nested. This avoids ambiguity with the non-greedy modifier suffix `?`, and with other modifiers in other implementations. To apply a second repetition to an inner repetition, parentheses may be used. For example, the expression `(?:a{6})*` matches any multiple of six `'a'` characters.
The special characters are:

`.`

(Dot.) In the default mode, this matches any character except a newline. If the [`DOTALL`](https://docs.python.org/3/library/re.html#re.DOTALL "re.DOTALL") flag has been specified, this matches any character including a newline. `(?s:.)` matches any character regardless of flags.

`^`

(Caret.) Matches the start of the string, and in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode also matches immediately after each newline.

`$`

Matches the end of the string or just before the newline at the end of the string, and in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode also matches before a newline. `foo` matches both ‘foo’ and ‘foobar’, while the regular expression `foo$` matches only ‘foo’. More interestingly, searching for `foo.$` in `'foo1\nfoo2\n'` matches ‘foo2’ normally, but ‘foo1’ in `MULTILINE` mode; searching for a single `$` in `'foo\n'` will find two (empty) matches: one just before the newline, and one at the end of the string.

`*`

Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. `ab*` will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

`+`

Causes the resulting RE to match 1 or more repetitions of the preceding RE. `ab+` will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

`?`

Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. `ab?` will match either ‘a’ or ‘ab’.

`*?`, `+?`, `??`

The `'*'`, `'+'`, and `'?'` quantifiers are all _greedy_ ; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE `<.*>` is matched against `'<a> b <c>'`, it will match the entire string, and not just `'<a>'`. Adding `?` after the quantifier makes it perform the match in _non-greedy_ or _minimal_ fashion; as _few_ characters as possible will be matched. Using the RE `<.*?>` will match only `'<a>'`.

`*+`, `++`, `?+`

Like the `'*'`, `'+'`, and `'?'` quantifiers, those where `'+'` is appended also match as many times as possible. However, unlike the true greedy quantifiers, these do not allow back-tracking when the expression following it fails to match. These are known as _possessive_ quantifiers. For example, `a*a` will match `'aaaa'` because the `a*` will match all 4 `'a'`s, but, when the final `'a'` is encountered, the expression is backtracked so that in the end the `a*` ends up matching 3 `'a'`s total, and the fourth `'a'` is matched by the final `'a'`. However, when `a*+a` is used to match `'aaaa'`, the `a*+` will match all 4 `'a'`, but when the final `'a'` fails to find any more characters to match, the expression cannot be backtracked and will thus fail to match. `x*+`, `x++` and `x?+` are equivalent to `(?>x*)`, `(?>x+)` and `(?>x?)` correspondingly.
Added in version 3.11.

`{m}`

Specifies that exactly _m_ copies of the previous RE should be matched; fewer matches cause the entire RE not to match. For example, `a{6}` will match exactly six `'a'` characters, but not five.

`{m,n}`

Causes the resulting RE to match from _m_ to _n_ repetitions of the preceding RE, attempting to match as many repetitions as possible. For example, `a{3,5}` will match from 3 to 5 `'a'` characters. Omitting _m_ specifies a lower bound of zero, and omitting _n_ specifies an infinite upper bound. As an example, `a{4,}b` will match `'aaaab'` or a thousand `'a'` characters followed by a `'b'`, but not `'aaab'`. The comma may not be omitted or the modifier would be confused with the previously described form.

`{m,n}?`

Causes the resulting RE to match from _m_ to _n_ repetitions of the preceding RE, attempting to match as _few_ repetitions as possible. This is the non-greedy version of the previous quantifier. For example, on the 6-character string `'aaaaaa'`, `a{3,5}` will match 5 `'a'` characters, while `a{3,5}?` will only match 3 characters.

`{m,n}+`

Causes the resulting RE to match from _m_ to _n_ repetitions of the preceding RE, attempting to match as many repetitions as possible _without_ establishing any backtracking points. This is the possessive version of the quantifier above. For example, on the 6-character string `'aaaaaa'`, `a{3,5}+aa` attempt to match 5 `'a'` characters, then, requiring 2 more `'a'`s, will need more characters than available and thus fail, while `a{3,5}aa` will match with `a{3,5}` capturing 5, then 4 `'a'`s by backtracking and then the final 2 `'a'`s are matched by the final `aa` in the pattern. `x{m,n}+` is equivalent to `(?>x{m,n})`.
Added in version 3.11.

`\`

Either escapes special characters (permitting you to match characters like `'*'`, `'?'`, and so forth), or signals a special sequence; special sequences are discussed below.
If you’re not using a raw string to express the pattern, remember that Python also uses the backslash as an escape sequence in string literals; if the escape sequence isn’t recognized by Python’s parser, the backslash and subsequent character are included in the resulting string. However, if Python would recognize the resulting sequence, the backslash should be repeated twice. This is complicated and hard to understand, so it’s highly recommended that you use raw strings for all but the simplest expressions.

`[]`

Used to indicate a set of characters. In a set:
  * Characters can be listed individually, e.g. `[amk]` will match `'a'`, `'m'`, or `'k'`.


  * Ranges of characters can be indicated by giving two characters and separating them by a `'-'`, for example `[a-z]` will match any lowercase ASCII letter, `[0-5][0-9]` will match all the two-digits numbers from `00` to `59`, and `[0-9A-Fa-f]` will match any hexadecimal digit. If `-` is escaped (e.g. `[a\-z]`) or if it’s placed as the first or last character (e.g. `[-a]` or `[a-]`), it will match a literal `'-'`.
  * Special characters except backslash lose their special meaning inside sets. For example, `[(+*)]` will match any of the literal characters `'('`, `'+'`, `'*'`, or `')'`.


  * Backslash either escapes characters which have special meaning in a set such as `'-'`, `']'`, `'^'` and `'\\'` itself or signals a special sequence which represents a single character such as `\xa0` or `\n` or a character class such as `\w` or `\S` (defined below). Note that `\b` represents a single “backspace” character, not a word boundary as outside a set, and numeric escapes such as `\1` are always octal escapes, not group references. Special sequences which do not match a single character such as `\A` and `\z` are not allowed.


  * Characters that are not within a range can be matched by _complementing_ the set. If the first character of the set is `'^'`, all the characters that are _not_ in the set will be matched. For example, `[^5]` will match any character except `'5'`, and `[^^]` will match any character except `'^'`. `^` has no special meaning if it’s not the first character in the set.
  * To match a literal `']'` inside a set, precede it with a backslash, or place it at the beginning of the set. For example, both `[()[\]{}]` and `[]()[{}]` will match a right bracket, as well as left bracket, braces, and parentheses.


  * Support of nested sets and set operations as in [`FutureWarning`](https://docs.python.org/3/library/exceptions.html#FutureWarning "FutureWarning") will be raised in ambiguous cases for the time being. That includes sets starting with a literal `'['` or containing literal character sequences `'--'`, `'&&'`, `'~~'`, and `'||'`. To avoid a warning escape them with a backslash.


Changed in version 3.7: [`FutureWarning`](https://docs.python.org/3/library/exceptions.html#FutureWarning "FutureWarning") is raised if a character set contains constructs that will change semantically in the future.

`|`

`A|B`, where _A_ and _B_ can be arbitrary REs, creates a regular expression that will match either _A_ or _B_. An arbitrary number of REs can be separated by the `'|'` in this way. This can be used inside groups (see below) as well. As the target string is scanned, REs separated by `'|'` are tried from left to right. When one pattern completely matches, that branch is accepted. This means that once _A_ matches, _B_ will not be tested further, even if it would produce a longer overall match. In other words, the `'|'` operator is never greedy. To match a literal `'|'`, use `\|`, or enclose it inside a character class, as in `[|]`.

`(...)`

Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the `\number` special sequence, described below. To match the literals `'('` or `')'`, use `\(` or `\)`, or enclose them inside a character class: `[(]`, `[)]`.

`(?...)`

This is an extension notation (a `'?'` following a `'('` is not meaningful otherwise). The first character after the `'?'` determines what the meaning and further syntax of the construct is. Extensions usually do not create a new group; `(?P<name>...)` is the only exception to this rule. Following are the currently supported extensions.

`(?aiLmsux)`

(One or more letters from the set `'a'`, `'i'`, `'L'`, `'m'`, `'s'`, `'u'`, `'x'`.) The group matches the empty string; the letters set the corresponding flags for the entire regular expression:
  * [`re.A`](https://docs.python.org/3/library/re.html#re.A "re.A") (ASCII-only matching)
  * [`re.I`](https://docs.python.org/3/library/re.html#re.I "re.I") (ignore case)
  * [`re.L`](https://docs.python.org/3/library/re.html#re.L "re.L") (locale dependent)
  * [`re.M`](https://docs.python.org/3/library/re.html#re.M "re.M") (multi-line)
  * [`re.S`](https://docs.python.org/3/library/re.html#re.S "re.S") (dot matches all)
  * [`re.U`](https://docs.python.org/3/library/re.html#re.U "re.U") (Unicode matching)
  * [`re.X`](https://docs.python.org/3/library/re.html#re.X "re.X") (verbose)


(The flags are described in [Module Contents](https://docs.python.org/3/library/re.html#contents-of-module-re).) This is useful if you wish to include the flags as part of the regular expression, instead of passing a _flag_ argument to the [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile") function. Flags should be used first in the expression string.
Changed in version 3.11: This construction can only be used at the start of the expression.

`(?:...)`

A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group _cannot_ be retrieved after performing a match or referenced later in the pattern.

`(?aiLmsux-imsx:...)`

(Zero or more letters from the set `'a'`, `'i'`, `'L'`, `'m'`, `'s'`, `'u'`, `'x'`, optionally followed by `'-'` followed by one or more letters from the `'i'`, `'m'`, `'s'`, `'x'`.) The letters set or remove the corresponding flags for the part of the expression:
  * [`re.A`](https://docs.python.org/3/library/re.html#re.A "re.A") (ASCII-only matching)
  * [`re.I`](https://docs.python.org/3/library/re.html#re.I "re.I") (ignore case)
  * [`re.L`](https://docs.python.org/3/library/re.html#re.L "re.L") (locale dependent)
  * [`re.M`](https://docs.python.org/3/library/re.html#re.M "re.M") (multi-line)
  * [`re.S`](https://docs.python.org/3/library/re.html#re.S "re.S") (dot matches all)
  * [`re.U`](https://docs.python.org/3/library/re.html#re.U "re.U") (Unicode matching)
  * [`re.X`](https://docs.python.org/3/library/re.html#re.X "re.X") (verbose)


(The flags are described in [Module Contents](https://docs.python.org/3/library/re.html#contents-of-module-re).)
The letters `'a'`, `'L'` and `'u'` are mutually exclusive when used as inline flags, so they can’t be combined or follow `'-'`. Instead, when one of them appears in an inline group, it overrides the matching mode in the enclosing group. In Unicode patterns `(?a:...)` switches to ASCII-only matching, and `(?u:...)` switches to Unicode matching (default). In bytes patterns `(?L:...)` switches to locale dependent matching, and `(?a:...)` switches to ASCII-only matching (default). This override is only in effect for the narrow inline group, and the original matching mode is restored outside of the group.
Added in version 3.6.
Changed in version 3.7: The letters `'a'`, `'L'` and `'u'` also can be used in a group.

`(?>...)`

Attempts to match `...` as if it was a separate regular expression, and if successful, continues to match the rest of the pattern following it. If the subsequent pattern fails to match, the stack can only be unwound to a point _before_ the `(?>...)` because once exited, the expression, known as an _atomic group_ , has thrown away all stack points within itself. Thus, `(?>.*).` would never match anything because first the `.*` would match all characters possible, then, having nothing left to match, the final `.` would fail to match. Since there are no stack points saved in the Atomic Group, and there is no stack point before it, the entire expression would thus fail to match.
Added in version 3.11.

`(?P<name>...)`

Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name _name_. Group names must be valid Python identifiers, and in [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") patterns they can only contain bytes in the ASCII range. Each group name must be defined only once within a regular expression. A symbolic group is also a numbered group, just as if the group were not named.
Named groups can be referenced in three contexts. If the pattern is `(?P<quote>['"]).*?(?P=quote)` (i.e. matching a string quoted with either single or double quotes):
Context of reference to group “quote” | Ways to reference it
---|---
in the same pattern itself |
  * `(?P=quote)` (as shown)
  * `\1`


when processing match object _m_ |
  * `m.group('quote')`
  * `m.end('quote')` (etc.)


in a string passed to the _repl_ argument of `re.sub()` |
  * `\g<quote>`
  * `\g<1>`
  * `\1`


Changed in version 3.12: In [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") patterns, group _name_ can only contain bytes in the ASCII range (`b'\x00'`-`b'\x7f'`).

`(?P=name)`

A backreference to a named group; it matches whatever text was matched by the earlier group named _name_.

`(?#...)`

A comment; the contents of the parentheses are simply ignored.

`(?=...)`

Matches if `...` matches next, but doesn’t consume any of the string. This is called a _lookahead assertion_. For example, `Isaac (?=Asimov)` will match `'Isaac '` only if it’s followed by `'Asimov'`.

`(?!...)`

Matches if `...` doesn’t match next. This is a _negative lookahead assertion_. For example, `Isaac (?!Asimov)` will match `'Isaac '` only if it’s _not_ followed by `'Asimov'`.

`(?<=...)`

Matches if the current position in the string is preceded by a match for `...` that ends at the current position. This is called a _positive lookbehind assertion_. `(?<=abc)def` will find a match in `'abcdef'`, since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must only match strings of some fixed length, meaning that `abc` or `a|b` are allowed, but `a*` and `a{3,4}` are not. Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search") function rather than the [`match()`](https://docs.python.org/3/library/re.html#re.match "re.match") function:
Copy```
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'

```

This example looks for a word following a hyphen:
Copy```
>>> m = re.search(r'(?<=-)\w+', 'spam-egg')
>>> m.group(0)
'egg'

```

Changed in version 3.5: Added support for group references of fixed length.

`(?<!...)`

Matches if the current position in the string is not preceded by a match for `...`. This is called a _negative lookbehind assertion_. Similar to positive lookbehind assertions, the contained pattern must only match strings of some fixed length. Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.

`(?(id/name)yes-pattern|no-pattern)`

Will try to match with `yes-pattern` if the group with given _id_ or _name_ exists, and with `no-pattern` if it doesn’t. `no-pattern` is optional and can be omitted. For example, `(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)` is a poor email matching pattern, which will match with `'<user@host.com>'` as well as `'user@host.com'`, but not with `'<user@host.com'` nor `'user@host.com>'`.
Changed in version 3.12: Group _id_ can only contain ASCII digits. In [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") patterns, group _name_ can only contain bytes in the ASCII range (`b'\x00'`-`b'\x7f'`).
The special sequences consist of `'\'` and a character from the list below. If the ordinary character is not an ASCII digit or an ASCII letter, then the resulting RE will match the second character. For example, `\$` matches the character `'$'`.

`\number`

Matches the contents of the group of the same number. Groups are numbered starting from 1. For example, `(.+) \1` matches `'the the'` or `'55 55'`, but not `'thethe'` (note the space after the group). This special sequence can only be used to match one of the first 99 groups. If the first digit of _number_ is 0, or _number_ is 3 octal digits long, it will not be interpreted as a group match, but as the character with octal value _number_. Inside the `'['` and `']'` of a character class, all numeric escapes are treated as characters.

`\A`

Matches only at the start of the string.

`\b`

Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of word characters. Note that formally, `\b` is defined as the boundary between a `\w` and a `\W` character (or vice versa), or between `\w` and the beginning or end of the string. This means that `r'\bat\b'` matches `'at'`, `'at.'`, `'(at)'`, and `'as at ay'` but not `'attempt'` or `'atlas'`.
The default word characters in Unicode (str) patterns are Unicode alphanumerics and the underscore, but this can be changed by using the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag. Word boundaries are determined by the current locale if the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag is used.
Note
Inside a character range, `\b` represents the backspace character, for compatibility with Python’s string literals.

`\B`

Matches the empty string, but only when it is _not_ at the beginning or end of a word. This means that `r'at\B'` matches `'athens'`, `'atom'`, `'attorney'`, but not `'at'`, `'at.'`, or `'at!'`. `\B` is the opposite of `\b`, so word characters in Unicode (str) patterns are Unicode alphanumerics or the underscore, although this can be changed by using the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag. Word boundaries are determined by the current locale if the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag is used.
Changed in version 3.14: `\B` now matches empty input string.

`\d`


For Unicode (str) patterns:

Matches any Unicode decimal digit (that is, any character in Unicode character category `[0-9]`, and also many other digit characters.
Matches `[0-9]` if the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used.

For 8-bit (bytes) patterns:

Matches any decimal digit in the ASCII character set; this is equivalent to `[0-9]`.

`\D`

Matches any character which is not a decimal digit. This is the opposite of `\d`.
Matches `[^0-9]` if the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used.

`\s`


For Unicode (str) patterns:

Matches Unicode whitespace characters (as defined by [`str.isspace()`](https://docs.python.org/3/library/stdtypes.html#str.isspace "str.isspace")). This includes `[ \t\n\r\f\v]`, and also many other characters, for example the non-breaking spaces mandated by typography rules in many languages.
Matches `[ \t\n\r\f\v]` if the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used.

For 8-bit (bytes) patterns:

Matches characters considered whitespace in the ASCII character set; this is equivalent to `[ \t\n\r\f\v]`.

`\S`

Matches any character which is not a whitespace character. This is the opposite of `\s`.
Matches `[^ \t\n\r\f\v]` if the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used.

`\w`


For Unicode (str) patterns:

Matches Unicode word characters; this includes all Unicode alphanumeric characters (as defined by [`str.isalnum()`](https://docs.python.org/3/library/stdtypes.html#str.isalnum "str.isalnum")), as well as the underscore (`_`).
Matches `[a-zA-Z0-9_]` if the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used.

For 8-bit (bytes) patterns:

Matches characters considered alphanumeric in the ASCII character set; this is equivalent to `[a-zA-Z0-9_]`. If the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag is used, matches characters considered alphanumeric in the current locale and the underscore.

`\W`

Matches any character which is not a word character. This is the opposite of `\w`. By default, matches non-underscore (`_`) characters for which [`str.isalnum()`](https://docs.python.org/3/library/stdtypes.html#str.isalnum "str.isalnum") returns `False`.
Matches `[^a-zA-Z0-9_]` if the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used.
If the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag is used, matches characters which are neither alphanumeric in the current locale nor the underscore.

`\z`

Matches only at the end of the string.
Added in version 3.14.

`\Z`

The same as `\z`. For compatibility with old Python versions.
Most of the [escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences) supported by Python string literals are also accepted by the regular expression parser:
Copy```
\a      \b      \f      \n
\N      \r      \t      \u
\U      \v      \x      \\

```

(Note that `\b` is used to represent word boundaries, and means “backspace” only inside character classes.)
`'\u'`, `'\U'`, and `'\N'` escape sequences are only recognized in Unicode (str) patterns. In bytes patterns they are errors. Unknown escapes of ASCII letters are reserved for future use and treated as errors.
Octal escapes are included in a limited form. If the first digit is a 0, or if there are three octal digits, it is considered an octal escape. Otherwise, it is a group reference. As for string literals, octal escapes are always at most three digits in length.
