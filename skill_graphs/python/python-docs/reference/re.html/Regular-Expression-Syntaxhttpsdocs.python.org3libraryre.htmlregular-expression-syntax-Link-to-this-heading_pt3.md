
```


Pattern.match(_string_[, _pos_[, _endpos_]])[¶](https://docs.python.org/3/library/re.html#re.Pattern.match "Link to this definition")

If zero or more characters at the _beginning_ of _string_ match this regular expression, return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if the string does not match the pattern; note that this is different from a zero-length match.
The optional _pos_ and _endpos_ parameters have the same meaning as for the [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") method.
Copy```
>>> pattern = re.compile("o")
>>> pattern.match("dog")      # No match as "o" is not at the start of "dog".
>>> pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
<re.Match object; span=(1, 2), match='o'>

```

If you want to locate a match anywhere in _string_ , use [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") instead (see also [search() vs. match()](https://docs.python.org/3/library/re.html#search-vs-match)).

Pattern.fullmatch(_string_[, _pos_[, _endpos_]])[¶](https://docs.python.org/3/library/re.html#re.Pattern.fullmatch "Link to this definition")

If the whole _string_ matches this regular expression, return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if the string does not match the pattern; note that this is different from a zero-length match.
The optional _pos_ and _endpos_ parameters have the same meaning as for the [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") method.
Copy```
>>> pattern = re.compile("o[gh]")
>>> pattern.fullmatch("dog")      # No match as "o" is not at the start of "dog".
>>> pattern.fullmatch("ogre")     # No match as not the full string matches.
>>> pattern.fullmatch("doggie", 1, 3)   # Matches within given limits.
<re.Match object; span=(1, 3), match='og'>

```

Added in version 3.4.

Pattern.split(_string_ , _maxsplit =0_)[¶](https://docs.python.org/3/library/re.html#re.Pattern.split "Link to this definition")

Identical to the [`split()`](https://docs.python.org/3/library/re.html#re.split "re.split") function, using the compiled pattern.

Pattern.findall(_string_[, _pos_[, _endpos_]])[¶](https://docs.python.org/3/library/re.html#re.Pattern.findall "Link to this definition")

Similar to the [`findall()`](https://docs.python.org/3/library/re.html#re.findall "re.findall") function, using the compiled pattern, but also accepts optional _pos_ and _endpos_ parameters that limit the search region like for [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search").

Pattern.finditer(_string_[, _pos_[, _endpos_]])[¶](https://docs.python.org/3/library/re.html#re.Pattern.finditer "Link to this definition")

Similar to the [`finditer()`](https://docs.python.org/3/library/re.html#re.finditer "re.finditer") function, using the compiled pattern, but also accepts optional _pos_ and _endpos_ parameters that limit the search region like for [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search").

Pattern.sub(_repl_ , _string_ , _count =0_)[¶](https://docs.python.org/3/library/re.html#re.Pattern.sub "Link to this definition")

Identical to the [`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub") function, using the compiled pattern.

Pattern.subn(_repl_ , _string_ , _count =0_)[¶](https://docs.python.org/3/library/re.html#re.Pattern.subn "Link to this definition")

Identical to the [`subn()`](https://docs.python.org/3/library/re.html#re.subn "re.subn") function, using the compiled pattern.

Pattern.flags[¶](https://docs.python.org/3/library/re.html#re.Pattern.flags "Link to this definition")

The regex matching flags. This is a combination of the flags given to [`compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile"), any `(?...)` inline flags in the pattern, and implicit flags such as [`UNICODE`](https://docs.python.org/3/library/re.html#re.UNICODE "re.UNICODE") if the pattern is a Unicode string.

Pattern.groups[¶](https://docs.python.org/3/library/re.html#re.Pattern.groups "Link to this definition")

The number of capturing groups in the pattern.

Pattern.groupindex[¶](https://docs.python.org/3/library/re.html#re.Pattern.groupindex "Link to this definition")

A dictionary mapping any symbolic group names defined by `(?P<id>)` to group numbers. The dictionary is empty if no symbolic groups were used in the pattern.

Pattern.pattern[¶](https://docs.python.org/3/library/re.html#re.Pattern.pattern "Link to this definition")

The pattern string from which the pattern object was compiled.
Changed in version 3.7: Added support of [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy") and [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy"). Compiled regular expression objects are considered atomic.
