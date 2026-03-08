## Match Objects[¶](https://docs.python.org/3/library/re.html#match-objects "Link to this heading")
Match objects always have a boolean value of `True`. Since [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match") and [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") return `None` when there is no match, you can test whether there was a match with a simple `if` statement:
Copy```
match = re.search(pattern, string)
if match:
    process(match)

```


_class_ re.Match[¶](https://docs.python.org/3/library/re.html#re.Match "Link to this definition")

Match object returned by successful `match`es and `search`es.
Changed in version 3.9: [`re.Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match") supports `[]` to indicate a Unicode (str) or bytes match. See [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

Match.expand(_template_)[¶](https://docs.python.org/3/library/re.html#re.Match.expand "Link to this definition")

Return the string obtained by doing backslash substitution on the template string _template_ , as done by the [`sub()`](https://docs.python.org/3/library/re.html#re.Pattern.sub "re.Pattern.sub") method. Escapes such as `\n` are converted to the appropriate characters, and numeric backreferences (`\1`, `\2`) and named backreferences (`\g<1>`, `\g<name>`) are replaced by the contents of the corresponding group. The backreference `\g<0>` will be replaced by the entire match.
Changed in version 3.5: Unmatched groups are replaced with an empty string.

Match.group([_group1_ , _..._])[¶](https://docs.python.org/3/library/re.html#re.Match.group "Link to this definition")

Returns one or more subgroups of the match. If there is a single argument, the result is a single string; if there are multiple arguments, the result is a tuple with one item per argument. Without arguments, _group1_ defaults to zero (the whole match is returned). If a _groupN_ argument is zero, the corresponding return value is the entire matching string; if it is a positive integer, it is the string matching the corresponding parenthesized group. If a group number is negative or larger than the number of groups defined in the pattern, an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") exception is raised. If a group is contained in a part of the pattern that did not match, the corresponding result is `None`. If a group is contained in a part of the pattern that matched multiple times, the last match is returned.
Copy```
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m.group(0)       # The entire match
'Isaac Newton'
>>> m.group(1)       # The first parenthesized subgroup.
'Isaac'
>>> m.group(2)       # The second parenthesized subgroup.
'Newton'
>>> m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')

```

If the regular expression uses the `(?P<name>...)` syntax, the _groupN_ arguments may also be strings identifying groups by their group name. If a string argument is not used as a group name in the pattern, an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") exception is raised.
A moderately complicated example:
Copy```
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.group('first_name')
'Malcolm'
>>> m.group('last_name')
'Reynolds'

```

Named groups can also be referred to by their index:
Copy```
>>> m.group(1)
'Malcolm'
>>> m.group(2)
'Reynolds'

```

If a group matches multiple times, only the last match is accessible:
Copy```
>>> m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
>>> m.group(1)                        # Returns only the last match.
'c3'

```


Match.__getitem__(_g_)[¶](https://docs.python.org/3/library/re.html#re.Match.__getitem__ "Link to this definition")

This is identical to `m.group(g)`. This allows easier access to an individual group from a match:
Copy```
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m[0]       # The entire match
'Isaac Newton'
>>> m[1]       # The first parenthesized subgroup.
'Isaac'
>>> m[2]       # The second parenthesized subgroup.
'Newton'

```

Named groups are supported as well:
Copy```
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Isaac Newton")
>>> m['first_name']
'Isaac'
>>> m['last_name']
'Newton'

```

Added in version 3.6.

Match.groups(_default =None_)[¶](https://docs.python.org/3/library/re.html#re.Match.groups "Link to this definition")

Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern. The _default_ argument is used for groups that did not participate in the match; it defaults to `None`.
For example:
Copy```
>>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
>>> m.groups()
('24', '1632')

```

If we make the decimal place and everything after it optional, not all groups might participate in the match. These groups will default to `None` unless the _default_ argument is given:
Copy```
>>> m = re.match(r"(\d+)\.?(\d+)?", "24")
>>> m.groups()      # Second group defaults to None.
('24', None)
>>> m.groups('0')   # Now, the second group defaults to '0'.
('24', '0')

```


Match.groupdict(_default =None_)[¶](https://docs.python.org/3/library/re.html#re.Match.groupdict "Link to this definition")

Return a dictionary containing all the _named_ subgroups of the match, keyed by the subgroup name. The _default_ argument is used for groups that did not participate in the match; it defaults to `None`. For example:
Copy```
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.groupdict()
{'first_name': 'Malcolm', 'last_name': 'Reynolds'}

```


Match.start([_group_])[¶](https://docs.python.org/3/library/re.html#re.Match.start "Link to this definition")


Match.end([_group_])[¶](https://docs.python.org/3/library/re.html#re.Match.end "Link to this definition")

Return the indices of the start and end of the substring matched by _group_ ; _group_ defaults to zero (meaning the whole matched substring). Return `-1` if _group_ exists but did not contribute to the match. For a match object _m_ , and a group _g_ that did contribute to the match, the substring matched by group _g_ (equivalent to `m.group(g)`) is
Copy```
m.string[m.start(g):m.end(g)]

```

Note that `m.start(group)` will equal `m.end(group)` if _group_ matched a null string. For example, after `m = re.search('b(c?)', 'cba')`, `m.start(0)` is 1, `m.end(0)` is 2, `m.start(1)` and `m.end(1)` are both 2, and `m.start(2)` raises an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") exception.
An example that will remove _remove_this_ from email addresses:
Copy```
>>> email = "tony@tiremove_thisger.net"
>>> m = re.search("remove_this", email)
>>> email[:m.start()] + email[m.end():]
'tony@tiger.net'

```


Match.span([_group_])[¶](https://docs.python.org/3/library/re.html#re.Match.span "Link to this definition")

For a match _m_ , return the 2-tuple `(m.start(group), m.end(group))`. Note that if _group_ did not contribute to the match, this is `(-1, -1)`. _group_ defaults to zero, the entire match.

Match.pos[¶](https://docs.python.org/3/library/re.html#re.Match.pos "Link to this definition")

The value of _pos_ which was passed to the [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") or [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match") method of a [regex object](https://docs.python.org/3/library/re.html#re-objects). This is the index into the string at which the RE engine started looking for a match.

Match.endpos[¶](https://docs.python.org/3/library/re.html#re.Match.endpos "Link to this definition")

The value of _endpos_ which was passed to the [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") or [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match") method of a [regex object](https://docs.python.org/3/library/re.html#re-objects). This is the index into the string beyond which the RE engine will not go.

Match.lastindex[¶](https://docs.python.org/3/library/re.html#re.Match.lastindex "Link to this definition")

The integer index of the last matched capturing group, or `None` if no group was matched at all. For example, the expressions `(a)b`, `((a)(b))`, and `((ab))` will have `lastindex == 1` if applied to the string `'ab'`, while the expression `(a)(b)` will have `lastindex == 2`, if applied to the same string.

Match.lastgroup[¶](https://docs.python.org/3/library/re.html#re.Match.lastgroup "Link to this definition")

The name of the last matched capturing group, or `None` if the group didn’t have a name, or if no group was matched at all.

Match.re[¶](https://docs.python.org/3/library/re.html#re.Match.re "Link to this definition")

The [regular expression object](https://docs.python.org/3/library/re.html#re-objects) whose [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match") or [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") method produced this match instance.

Match.string[¶](https://docs.python.org/3/library/re.html#re.Match.string "Link to this definition")

The string passed to [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match") or [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search").
Changed in version 3.7: Added support of [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy") and [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy"). Match objects are considered atomic.
