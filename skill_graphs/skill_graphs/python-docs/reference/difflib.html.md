[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
    * [SequenceMatcher Objects](https://docs.python.org/3/library/difflib.html#sequencematcher-objects)
    * [SequenceMatcher Examples](https://docs.python.org/3/library/difflib.html#sequencematcher-examples)
    * [Differ Objects](https://docs.python.org/3/library/difflib.html#differ-objects)
    * [Differ Example](https://docs.python.org/3/library/difflib.html#differ-example)
    * [A command-line interface to difflib](https://docs.python.org/3/library/difflib.html#a-command-line-interface-to-difflib)
    * [ndiff example](https://docs.python.org/3/library/difflib.html#ndiff-example)


#### Previous topic
[`re` — Regular expression operations](https://docs.python.org/3/library/re.html "previous chapter")
#### Next topic
[`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=difflib+%E2%80%94+Helpers+for+computing+deltas&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdifflib.html&pagesource=library%2Fdifflib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/textwrap.html "textwrap — Text wrapping and filling") |
  * [previous](https://docs.python.org/3/library/re.html "re — Regular expression operations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
  * |
  * Theme  Auto Light Dark |


#  `difflib` — Helpers for computing deltas[¶](https://docs.python.org/3/library/difflib.html#module-difflib "Link to this heading")
**Source code:**
* * *
This module provides classes and functions for comparing sequences. It can be used for example, for comparing files, and can produce information about file differences in various formats, including HTML and context and unified diffs. For comparing directories and files, see also, the [`filecmp`](https://docs.python.org/3/library/filecmp.html#module-filecmp "filecmp: Compare files efficiently.") module.

_class_ difflib.SequenceMatcher

This is a flexible class for comparing pairs of sequences of any type, so long as the sequence elements are [hashable](https://docs.python.org/3/glossary.html#term-hashable). The basic algorithm predates, and is a little fancier than, an algorithm published in the late 1980’s by Ratcliff and Obershelp under the hyperbolic name “gestalt pattern matching.” The idea is to find the longest contiguous matching subsequence that contains no “junk” elements; these “junk” elements are ones that are uninteresting in some sense, such as blank lines or whitespace. (Handling junk is an extension to the Ratcliff and Obershelp algorithm.) The same idea is then applied recursively to the pieces of the sequences to the left and to the right of the matching subsequence. This does not yield minimal edit sequences, but does tend to yield matches that “look right” to people.
**Timing:** The basic Ratcliff-Obershelp algorithm is cubic time in the worst case and quadratic time in the expected case. [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") is quadratic time for the worst case and has expected-case behavior dependent in a complicated way on how many elements the sequences have in common; best case time is linear.
**Automatic junk heuristic:** [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") supports a heuristic that automatically treats certain sequence items as junk. The heuristic counts how many times each individual item appears in the sequence. If an item’s duplicates (after the first one) account for more than 1% of the sequence and the sequence is at least 200 items long, this item is marked as “popular” and is treated as junk for the purpose of sequence matching. This heuristic can be turned off by setting the `autojunk` argument to `False` when creating the `SequenceMatcher`.
Changed in version 3.2: Added the _autojunk_ parameter.

_class_ difflib.Differ[¶](https://docs.python.org/3/library/difflib.html#difflib.Differ "Link to this definition")

This is a class for comparing sequences of lines of text, and producing human-readable differences or deltas. Differ uses [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") both to compare sequences of lines, and to compare sequences of characters within similar (near-matching) lines.
Each line of a [`Differ`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ") delta begins with a two-letter code:
Code | Meaning
---|---
`'- '` | line unique to sequence 1
`'+ '` | line unique to sequence 2
`'  '` | line common to both sequences
`'? '` | line not present in either input sequence
Lines beginning with ‘`?`’ attempt to guide the eye to intraline differences, and were not present in either input sequence. These lines can be confusing if the sequences contain whitespace characters, such as spaces, tabs or line breaks.

_class_ difflib.HtmlDiff[¶](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff "Link to this definition")

This class can be used to create an HTML table (or a complete HTML file containing the table) showing a side by side, line by line comparison of text with inter-line and intra-line change highlights. The table can be generated in either full or contextual difference mode.
The constructor for this class is:

__init__(_tabsize =8_, _wrapcolumn =None_, _linejunk =None_, _charjunk =IS_CHARACTER_JUNK_)[¶](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff.__init__ "Link to this definition")

Initializes instance of `HtmlDiff`.
_tabsize_ is an optional keyword argument to specify tab stop spacing and defaults to `8`.
_wrapcolumn_ is an optional keyword to specify column number where lines are broken and wrapped, defaults to `None` where lines are not wrapped.
_linejunk_ and _charjunk_ are optional keyword arguments passed into [`ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff") (used by `HtmlDiff` to generate the side by side HTML differences). See `ndiff()` documentation for argument default values and descriptions.
The following methods are public:

make_file(_fromlines_ , _tolines_ , _fromdesc =''_, _todesc =''_, _context =False_, _numlines =5_, _*_ , _charset ='utf-8'_)[¶](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff.make_file "Link to this definition")

Compares _fromlines_ and _tolines_ (lists of strings) and returns a string which is a complete HTML file containing a table showing line by line differences with inter-line and intra-line changes highlighted.
_fromdesc_ and _todesc_ are optional keyword arguments to specify from/to file column header strings (both default to an empty string).
_context_ and _numlines_ are both optional keyword arguments. Set _context_ to `True` when contextual differences are to be shown, else the default is `False` to show the full files. _numlines_ defaults to `5`. When _context_ is `True` _numlines_ controls the number of context lines which surround the difference highlights. When _context_ is `False` _numlines_ controls the number of lines which are shown before a difference highlight when using the “next” hyperlinks (setting to zero would cause the “next” hyperlinks to place the next difference highlight at the top of the browser without any leading context).
Note
_fromdesc_ and _todesc_ are interpreted as unescaped HTML and should be properly escaped while receiving input from untrusted sources.
Changed in version 3.5: _charset_ keyword-only argument was added. The default charset of HTML document changed from `'ISO-8859-1'` to `'utf-8'`.

make_table(_fromlines_ , _tolines_ , _fromdesc =''_, _todesc =''_, _context =False_, _numlines =5_)[¶](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff.make_table "Link to this definition")

Compares _fromlines_ and _tolines_ (lists of strings) and returns a string which is a complete HTML table showing line by line differences with inter-line and intra-line changes highlighted.
The arguments for this method are the same as those for the [`make_file()`](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff.make_file "difflib.HtmlDiff.make_file") method.

difflib.context_diff(_a_ , _b_ , _fromfile =''_, _tofile =''_, _fromfiledate =''_, _tofiledate =''_, _n =3_, _lineterm ='\n'_)[¶](https://docs.python.org/3/library/difflib.html#difflib.context_diff "Link to this definition")

Compare _a_ and _b_ (lists of strings); return a delta (a [generator](https://docs.python.org/3/glossary.html#term-generator) generating the delta lines) in context diff format.
Context diffs are a compact way of showing just the lines that have changed plus a few lines of context. The changes are shown in a before/after style. The number of context lines is set by _n_ which defaults to three.
By default, the diff control lines (those with `***` or `---`) are created with a trailing newline. This is helpful so that inputs created from [`io.IOBase.readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") result in diffs that are suitable for use with [`io.IOBase.writelines()`](https://docs.python.org/3/library/io.html#io.IOBase.writelines "io.IOBase.writelines") since both the inputs and outputs have trailing newlines.
For inputs that do not have trailing newlines, set the _lineterm_ argument to `""` so that the output will be uniformly newline free.
The context diff format normally has a header for filenames and modification times. Any or all of these may be specified using strings for _fromfile_ , _tofile_ , _fromfiledate_ , and _tofiledate_. The modification times are normally expressed in the ISO 8601 format. If not specified, the strings default to blanks.
Copy```
>>> import sys
>>> from difflib import *
>>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
>>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
>>> sys.stdout.writelines(context_diff(s1, s2, fromfile='before.py',
...                        tofile='after.py'))
*** before.py
--- after.py
***************
*** 1,4 ****
! bacon
! eggs
! ham
  guido
--- 1,4 ----
! python
! eggy
! hamster
  guido

```

See [A command-line interface to difflib](https://docs.python.org/3/library/difflib.html#difflib-interface) for a more detailed example.

difflib.get_close_matches(_word_ , _possibilities_ , _n =3_, _cutoff =0.6_)[¶](https://docs.python.org/3/library/difflib.html#difflib.get_close_matches "Link to this definition")

Return a list of the best “good enough” matches. _word_ is a sequence for which close matches are desired (typically a string), and _possibilities_ is a list of sequences against which to match _word_ (typically a list of strings).
Optional argument _n_ (default `3`) is the maximum number of close matches to return; _n_ must be greater than `0`.
Optional argument _cutoff_ (default `0.6`) is a float in the range [0, 1]. Possibilities that don’t score at least that similar to _word_ are ignored.
The best (no more than _n_) matches among the possibilities are returned in a list, sorted by similarity score, most similar first.
Copy```
>>> get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
['apple', 'ape']
>>> import keyword
>>> get_close_matches('wheel', keyword.kwlist)
['while']
>>> get_close_matches('pineapple', keyword.kwlist)
[]
>>> get_close_matches('accept', keyword.kwlist)
['except']

```


difflib.ndiff(_a_ , _b_ , _linejunk =None_, _charjunk =IS_CHARACTER_JUNK_)[¶](https://docs.python.org/3/library/difflib.html#difflib.ndiff "Link to this definition")

Compare _a_ and _b_ (lists of strings); return a [`Differ`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ")-style delta (a [generator](https://docs.python.org/3/glossary.html#term-generator) generating the delta lines).
Optional keyword parameters _linejunk_ and _charjunk_ are filtering functions (or `None`):
_linejunk_ : A function that accepts a single string argument, and returns true if the string is junk, or false if not. The default is `None`. There is also a module-level function [`IS_LINE_JUNK()`](https://docs.python.org/3/library/difflib.html#difflib.IS_LINE_JUNK "difflib.IS_LINE_JUNK"), which filters out lines without visible characters, except for at most one hash character (`'#'`) – however the underlying [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") class does a dynamic analysis of which lines are so frequent as to constitute noise, and this usually works better than using this function.
_charjunk_ : A function that accepts a character (a string of length 1), and returns if the character is junk, or false if not. The default is module-level function [`IS_CHARACTER_JUNK()`](https://docs.python.org/3/library/difflib.html#difflib.IS_CHARACTER_JUNK "difflib.IS_CHARACTER_JUNK"), which filters out whitespace characters (a blank or tab; it’s a bad idea to include newline in this!).
Copy```
>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
...              'ore\ntree\nemu\n'.splitlines(keepends=True))
>>> print(''.join(diff), end="")
- one
?  ^
+ or
?  ^
- two
- three
?  -
+ tree
+ emu

```


difflib.restore(_sequence_ , _which_)[¶](https://docs.python.org/3/library/difflib.html#difflib.restore "Link to this definition")

Return one of the two sequences that generated a delta.
Given a _sequence_ produced by [`Differ.compare()`](https://docs.python.org/3/library/difflib.html#difflib.Differ.compare "difflib.Differ.compare") or [`ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff"), extract lines originating from file 1 or 2 (parameter _which_), stripping off line prefixes.
Example:
Copy```
>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
...              'ore\ntree\nemu\n'.splitlines(keepends=True))
>>> diff = list(diff) # materialize the generated delta into a list
>>> print(''.join(restore(diff, 1)), end="")
one
two
three
>>> print(''.join(restore(diff, 2)), end="")
or
tree
emu

```


difflib.unified_diff(_a_ , _b_ , _fromfile =''_, _tofile =''_, _fromfiledate =''_, _tofiledate =''_, _n =3_, _lineterm ='\n'_)[¶](https://docs.python.org/3/library/difflib.html#difflib.unified_diff "Link to this definition")

Compare _a_ and _b_ (lists of strings); return a delta (a [generator](https://docs.python.org/3/glossary.html#term-generator) generating the delta lines) in unified diff format.
Unified diffs are a compact way of showing just the lines that have changed plus a few lines of context. The changes are shown in an inline style (instead of separate before/after blocks). The number of context lines is set by _n_ which defaults to three.
By default, the diff control lines (those with `---`, `+++`, or `@@`) are created with a trailing newline. This is helpful so that inputs created from [`io.IOBase.readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") result in diffs that are suitable for use with [`io.IOBase.writelines()`](https://docs.python.org/3/library/io.html#io.IOBase.writelines "io.IOBase.writelines") since both the inputs and outputs have trailing newlines.
For inputs that do not have trailing newlines, set the _lineterm_ argument to `""` so that the output will be uniformly newline free.
The unified diff format normally has a header for filenames and modification times. Any or all of these may be specified using strings for _fromfile_ , _tofile_ , _fromfiledate_ , and _tofiledate_. The modification times are normally expressed in the ISO 8601 format. If not specified, the strings default to blanks.
Copy```
>>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
>>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
>>> sys.stdout.writelines(unified_diff(s1, s2, fromfile='before.py', tofile='after.py'))
--- before.py
+++ after.py
@@ -1,4 +1,4 @@
-bacon
-eggs
-ham
+python
+eggy
+hamster
 guido

```

See [A command-line interface to difflib](https://docs.python.org/3/library/difflib.html#difflib-interface) for a more detailed example.

difflib.diff_bytes(_dfunc_ , _a_ , _b_ , _fromfile =b''_, _tofile =b''_, _fromfiledate =b''_, _tofiledate =b''_, _n =3_, _lineterm =b'\n'_)[¶](https://docs.python.org/3/library/difflib.html#difflib.diff_bytes "Link to this definition")

Compare _a_ and _b_ (lists of bytes objects) using _dfunc_ ; yield a sequence of delta lines (also bytes) in the format returned by _dfunc_. _dfunc_ must be a callable, typically either [`unified_diff()`](https://docs.python.org/3/library/difflib.html#difflib.unified_diff "difflib.unified_diff") or [`context_diff()`](https://docs.python.org/3/library/difflib.html#difflib.context_diff "difflib.context_diff").
Allows you to compare data with unknown or inconsistent encoding. All inputs except _n_ must be bytes objects, not str. Works by losslessly converting all inputs (except _n_) to str, and calling `dfunc(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm)`. The output of _dfunc_ is then converted back to bytes, so the delta lines that you receive have the same unknown/inconsistent encodings as _a_ and _b_.
Added in version 3.5.

difflib.IS_LINE_JUNK(_line_)[¶](https://docs.python.org/3/library/difflib.html#difflib.IS_LINE_JUNK "Link to this definition")

Return `True` for ignorable lines. The line _line_ is ignorable if _line_ is blank or contains a single `'#'`, otherwise it is not ignorable. Used as a default for parameter _linejunk_ in [`ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff") in older versions.

difflib.IS_CHARACTER_JUNK(_ch_)[¶](https://docs.python.org/3/library/difflib.html#difflib.IS_CHARACTER_JUNK "Link to this definition")

Return `True` for ignorable characters. The character _ch_ is ignorable if _ch_ is a space or tab, otherwise it is not ignorable. Used as a default for parameter _charjunk_ in [`ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff").
See also
Discussion of a similar algorithm by John W. Ratcliff and D. E. Metzener. This was published in Dr. Dobb’s Journal in July, 1988.
## SequenceMatcher Objects[¶](https://docs.python.org/3/library/difflib.html#sequencematcher-objects "Link to this heading")
The [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") class has this constructor:

_class_ difflib.SequenceMatcher(_isjunk =None_, _a =''_, _b =''_, _autojunk =True_)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "Link to this definition")

Optional argument _isjunk_ must be `None` (the default) or a one-argument function that takes a sequence element and returns true if and only if the element is “junk” and should be ignored. Passing `None` for _isjunk_ is equivalent to passing `lambda x: False`; in other words, no elements are ignored. For example, pass:
Copy```
lambda x: x in " \t"

```

if you’re comparing lines as sequences of characters, and don’t want to synch up on blanks or hard tabs.
The optional arguments _a_ and _b_ are sequences to be compared; both default to empty strings. The elements of both sequences must be [hashable](https://docs.python.org/3/glossary.html#term-hashable).
The optional argument _autojunk_ can be used to disable the automatic junk heuristic.
Changed in version 3.2: Added the _autojunk_ parameter.
SequenceMatcher objects get three data attributes: _bjunk_ is the set of elements of _b_ for which _isjunk_ is `True`; _bpopular_ is the set of non-junk elements considered popular by the heuristic (if it is not disabled); _b2j_ is a dict mapping the remaining elements of _b_ to a list of positions where they occur. All three are reset whenever _b_ is reset with [`set_seqs()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seqs "difflib.SequenceMatcher.set_seqs") or [`set_seq2()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq2 "difflib.SequenceMatcher.set_seq2").
Added in version 3.2: The _bjunk_ and _bpopular_ attributes.
`SequenceMatcher` objects have the following methods:

set_seqs(_a_ , _b_)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seqs "Link to this definition")

Set the two sequences to be compared.
`SequenceMatcher` computes and caches detailed information about the second sequence, so if you want to compare one sequence against many sequences, use [`set_seq2()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq2 "difflib.SequenceMatcher.set_seq2") to set the commonly used sequence once and call [`set_seq1()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq1 "difflib.SequenceMatcher.set_seq1") repeatedly, once for each of the other sequences.

set_seq1(_a_)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq1 "Link to this definition")

Set the first sequence to be compared. The second sequence to be compared is not changed.

set_seq2(_b_)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.set_seq2 "Link to this definition")

Set the second sequence to be compared. The first sequence to be compared is not changed.

find_longest_match(_alo =0_, _ahi =None_, _blo =0_, _bhi =None_)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.find_longest_match "Link to this definition")

Find longest matching block in `a[also:ahi]` and `b[blo:bhi]`.
If _isjunk_ was omitted or `None`, `find_longest_match()` returns `(i, j, k)` such that `a[i:i+k]` is equal to `b[j:j+k]`, where `also <= i <= i+k <= ahi` and `blo <= j <= j+k <= bhi`. For all `(i', j', k')` meeting those conditions, the additional conditions `k >= k'`, `i <= i'`, and if `i == i'`, `j <= j'` are also met. In other words, of all maximal matching blocks, return one that starts earliest in _a_ , and of all those maximal matching blocks that start earliest in _a_ , return the one that starts earliest in _b_.
Copy```
>>> s = SequenceMatcher(None, " abcd", "abcd abcd")
>>> s.find_longest_match(0, 5, 0, 9)
Match(a=0, b=4, size=5)

```

If _isjunk_ was provided, first the longest matching block is determined as above, but with the additional restriction that no junk element appears in the block. Then that block is extended as far as possible by matching (only) junk elements on both sides. So the resulting block never matches on junk except as identical junk happens to be adjacent to an interesting match.
Here’s the same example as before, but considering blanks to be junk. That prevents `' abcd'` from matching the `' abcd'` at the tail end of the second sequence directly. Instead only the `'abcd'` can match, and matches the leftmost `'abcd'` in the second sequence:
Copy```
>>> s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
>>> s.find_longest_match(0, 5, 0, 9)
Match(a=1, b=0, size=4)

```

If no blocks match, this returns `(also, blo, 0)`.
This method returns a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) `Match(a, b, size)`.
Changed in version 3.9: Added default arguments.

get_matching_blocks()[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_matching_blocks "Link to this definition")

Return list of triples describing non-overlapping matching subsequences. Each triple is of the form `(i, j, n)`, and means that `a[i:i+n] == b[j:j+n]`. The triples are monotonically increasing in _i_ and _j_.
The last triple is a dummy, and has the value `(len(a), len(b), 0)`. It is the only triple with `n == 0`. If `(i, j, n)` and `(i', j', n')` are adjacent triples in the list, and the second is not the last triple in the list, then `i+n < i'` or `j+n < j'`; in other words, adjacent triples always describe non-adjacent equal blocks.
Copy```
>>> s = SequenceMatcher(None, "abxcd", "abcd")
>>> s.get_matching_blocks()
[Match(a=0, b=0, size=2), Match(a=3, b=2, size=2), Match(a=5, b=4, size=0)]

```


get_opcodes()[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes "Link to this definition")

Return list of 5-tuples describing how to turn _a_ into _b_. Each tuple is of the form `(tag, i1, i2, j1, j2)`. The first tuple has `i1 == j1 == 0`, and remaining tuples have _i1_ equal to the _i2_ from the preceding tuple, and, likewise, _j1_ equal to the previous _j2_.
The _tag_ values are strings, with these meanings:
Value | Meaning
---|---
`'replace'` | `a[i1:i2]` should be replaced by `b[j1:j2]`.
`'delete'` | `a[i1:i2]` should be deleted. Note that `j1 == j2` in this case.
`'insert'` | `b[j1:j2]` should be inserted at `a[i1:i1]`. Note that `i1 == i2` in this case.
`'equal'` | `a[i1:i2] == b[j1:j2]` (the sub-sequences are equal).
For example:
Copy```
>>> a = "qabxcd"
>>> b = "abycdf"
>>> s = SequenceMatcher(None, a, b)
>>> for tag, i1, i2, j1, j2 in s.get_opcodes():
...     print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
...         tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
delete    a[0:1] --> b[0:0]      'q' --> ''
equal     a[1:3] --> b[0:2]     'ab' --> 'ab'
replace   a[3:4] --> b[2:3]      'x' --> 'y'
equal     a[4:6] --> b[3:5]     'cd' --> 'cd'
insert    a[6:6] --> b[5:6]       '' --> 'f'

```


get_grouped_opcodes(_n =3_)[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_grouped_opcodes "Link to this definition")

Return a [generator](https://docs.python.org/3/glossary.html#term-generator) of groups with up to _n_ lines of context.
Starting with the groups returned by [`get_opcodes()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes "difflib.SequenceMatcher.get_opcodes"), this method splits out smaller change clusters and eliminates intervening ranges which have no changes.
The groups are returned in the same format as [`get_opcodes()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes "difflib.SequenceMatcher.get_opcodes").

ratio()[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio "Link to this definition")

Return a measure of the sequences’ similarity as a float in the range [0, 1].
Where T is the total number of elements in both sequences, and M is the number of matches, this is 2.0*M / T. Note that this is `1.0` if the sequences are identical, and `0.0` if they have nothing in common.
This is expensive to compute if [`get_matching_blocks()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_matching_blocks "difflib.SequenceMatcher.get_matching_blocks") or [`get_opcodes()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes "difflib.SequenceMatcher.get_opcodes") hasn’t already been called, in which case you may want to try [`quick_ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.quick_ratio "difflib.SequenceMatcher.quick_ratio") or [`real_quick_ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.real_quick_ratio "difflib.SequenceMatcher.real_quick_ratio") first to get an upper bound.
Note
Caution: The result of a `ratio()` call may depend on the order of the arguments. For instance:
Copy```
>>> SequenceMatcher(None, 'tide', 'diet').ratio()
0.25
>>> SequenceMatcher(None, 'diet', 'tide').ratio()
0.5

```


quick_ratio()[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.quick_ratio "Link to this definition")

Return an upper bound on [`ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio "difflib.SequenceMatcher.ratio") relatively quickly.

real_quick_ratio()[¶](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.real_quick_ratio "Link to this definition")

Return an upper bound on [`ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio "difflib.SequenceMatcher.ratio") very quickly.
The three methods that return the ratio of matching to total characters can give different results due to differing levels of approximation, although [`quick_ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.quick_ratio "difflib.SequenceMatcher.quick_ratio") and [`real_quick_ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.real_quick_ratio "difflib.SequenceMatcher.real_quick_ratio") are always at least as large as [`ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio "difflib.SequenceMatcher.ratio"):
Copy```
>>> s = SequenceMatcher(None, "abcd", "bcde")
>>> s.ratio()
0.75
>>> s.quick_ratio()
0.75
>>> s.real_quick_ratio()
1.0

```

## SequenceMatcher Examples[¶](https://docs.python.org/3/library/difflib.html#sequencematcher-examples "Link to this heading")
This example compares two strings, considering blanks to be “junk”:
Copy```
>>> s = SequenceMatcher(lambda x: x == " ",
...                     "private Thread currentThread;",
...                     "private volatile Thread currentThread;")

```

[`ratio()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio "difflib.SequenceMatcher.ratio") returns a float in [0, 1], measuring the similarity of the sequences. As a rule of thumb, a `ratio()` value over 0.6 means the sequences are close matches:
Copy```
>>> print(round(s.ratio(), 3))
0.866

```

If you’re only interested in where the sequences match, [`get_matching_blocks()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_matching_blocks "difflib.SequenceMatcher.get_matching_blocks") is handy:
Copy```
>>> for block in s.get_matching_blocks():
...     print("a[%d] and b[%d] match for %d elements" % block)
a[0] and b[0] match for 8 elements
a[8] and b[17] match for 21 elements
a[29] and b[38] match for 0 elements

```

Note that the last tuple returned by [`get_matching_blocks()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_matching_blocks "difflib.SequenceMatcher.get_matching_blocks") is always a dummy, `(len(a), len(b), 0)`, and this is the only case in which the last tuple element (number of elements matched) is `0`.
If you want to know how to change the first sequence into the second, use [`get_opcodes()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes "difflib.SequenceMatcher.get_opcodes"):
Copy```
>>> for opcode in s.get_opcodes():
...     print("%6s a[%d:%d] b[%d:%d]" % opcode)
 equal a[0:8] b[0:8]
insert a[8:8] b[8:17]
 equal a[8:29] b[17:38]

```

See also
  * The [`get_close_matches()`](https://docs.python.org/3/library/difflib.html#difflib.get_close_matches "difflib.get_close_matches") function in this module which shows how simple code building on [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher") can be used to do useful work.
  * [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher").


## Differ Objects[¶](https://docs.python.org/3/library/difflib.html#differ-objects "Link to this heading")
Note that [`Differ`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ")-generated deltas make no claim to be **minimal** diffs. To the contrary, minimal diffs are often counter-intuitive, because they synch up anywhere possible, sometimes accidental matches 100 pages apart. Restricting synch points to contiguous matches preserves some notion of locality, at the occasional cost of producing a longer diff.
The [`Differ`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ") class has this constructor:

_class_ difflib.Differ(_linejunk =None_, _charjunk =None_)

Optional keyword parameters _linejunk_ and _charjunk_ are for filter functions (or `None`):
_linejunk_ : A function that accepts a single string argument, and returns true if the string is junk. The default is `None`, meaning that no line is considered junk.
_charjunk_ : A function that accepts a single character argument (a string of length 1), and returns true if the character is junk. The default is `None`, meaning that no character is considered junk.
These junk-filtering functions speed up matching to find differences and do not cause any differing lines or characters to be ignored. Read the description of the [`find_longest_match()`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.find_longest_match "difflib.SequenceMatcher.find_longest_match") method’s _isjunk_ parameter for an explanation.
`Differ` objects are used (deltas generated) via a single method:

compare(_a_ , _b_)[¶](https://docs.python.org/3/library/difflib.html#difflib.Differ.compare "Link to this definition")

Compare two sequences of lines, and generate the delta (a sequence of lines).
Each sequence must contain individual single-line strings ending with newlines. Such sequences can be obtained from the [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") method of file-like objects. The delta generated also consists of newline-terminated strings, ready to be printed as-is via the [`writelines()`](https://docs.python.org/3/library/io.html#io.IOBase.writelines "io.IOBase.writelines") method of a file-like object.
## Differ Example[¶](https://docs.python.org/3/library/difflib.html#differ-example "Link to this heading")
This example compares two texts. First we set up the texts, sequences of individual single-line strings ending with newlines (such sequences can also be obtained from the [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") method of file-like objects):
Copy```
>>> text1 = '''  1. Beautiful is better than ugly.
...   2. Explicit is better than implicit.
...   3. Simple is better than complex.
...   4. Complex is better than complicated.
... '''.splitlines(keepends=True)
>>> len(text1)
4
>>> text1[0][-1]
'\n'
>>> text2 = '''  1. Beautiful is better than ugly.
...   3.   Simple is better than complex.
...   4. Complicated is better than complex.
...   5. Flat is better than nested.
... '''.splitlines(keepends=True)

```

Next we instantiate a Differ object:
Copy```
>>> d = Differ()

```

Note that when instantiating a [`Differ`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ") object we may pass functions to filter out line and character “junk.” See the [`Differ()`](https://docs.python.org/3/library/difflib.html#difflib.Differ "difflib.Differ") constructor for details.
Finally, we compare the two:
Copy```
>>> result = list(d.compare(text1, text2))

```

`result` is a list of strings, so let’s pretty-print it:
Copy```
>>> from pprint import pprint
>>> pprint(result)
['    1. Beautiful is better than ugly.\n',
 '-   2. Explicit is better than implicit.\n',
 '-   3. Simple is better than complex.\n',
 '+   3.   Simple is better than complex.\n',
 '?     ++\n',
 '-   4. Complex is better than complicated.\n',
 '?            ^                     ---- ^\n',
 '+   4. Complicated is better than complex.\n',
 '?           ++++ ^                      ^\n',
 '+   5. Flat is better than nested.\n']

```

As a single multi-line string it looks like this:
Copy```
>>> import sys
>>> sys.stdout.writelines(result)
    1. Beautiful is better than ugly.
-   2. Explicit is better than implicit.
-   3. Simple is better than complex.
+   3.   Simple is better than complex.
?     ++
-   4. Complex is better than complicated.
?            ^                     ---- ^
+   4. Complicated is better than complex.
?           ++++ ^                      ^
+   5. Flat is better than nested.

```

## A command-line interface to difflib[¶](https://docs.python.org/3/library/difflib.html#a-command-line-interface-to-difflib "Link to this heading")
This example shows how to use difflib to create a `diff`-like utility.
Copy```
""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""

import sys, os, difflib, argparse
from datetime import datetime, timezone

def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)
    return t.astimezone().isoformat()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', default=False,
                        help='Produce a context format diff (default)')
    parser.add_argument('-u', action='store_true', default=False,
                        help='Produce a unified format diff')
    parser.add_argument('-m', action='store_true', default=False,
                        help='Produce HTML side by side diff '
                             '(can use -c and -l in conjunction)')
    parser.add_argument('-n', action='store_true', default=False,
                        help='Produce a ndiff format diff')
    parser.add_argument('-l', '--lines', type=int, default=3,
                        help='Set number of context lines (default 3)')
    parser.add_argument('fromfile')
    parser.add_argument('tofile')
    options = parser.parse_args()

    n = options.lines
    fromfile = options.fromfile
    tofile = options.tofile

    fromdate = file_mtime(fromfile)
    todate = file_mtime(tofile)
    with open(fromfile) as ff:
        fromlines = ff.readlines()
    with open(tofile) as tf:
        tolines = tf.readlines()

    if options.u:
        diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)
    elif options.n:
        diff = difflib.ndiff(fromlines, tolines)
    elif options.m:
        diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile,context=options.c,numlines=n)
    else:
        diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)

    sys.stdout.writelines(diff)

if __name__ == '__main__':
    main()

```

## ndiff example[¶](https://docs.python.org/3/library/difflib.html#ndiff-example "Link to this heading")
This example shows how to use [`difflib.ndiff()`](https://docs.python.org/3/library/difflib.html#difflib.ndiff "difflib.ndiff").
Copy```
"""ndiff [-q] file1 file2
    or
ndiff (-r1 | -r2) < ndiff_output > file1_or_file2

Print a human-friendly file difference report to stdout.  Both inter-
and intra-line differences are noted.  In the second form, recreate file1
(-r1) or file2 (-r2) on stdout, from an ndiff report on stdin.

In the first form, if -q ("quiet") is not specified, the first two lines
of output are

-: file1
+: file2

Each remaining line begins with a two-letter code:

    "- "    line unique to file1
    "+ "    line unique to file2
    "  "    line common to both files
    "? "    line not present in either input file

Lines beginning with "? " attempt to guide the eye to intraline
differences, and were not present in either input file.  These lines can be
confusing if the source files contain tab characters.

The first file can be recovered by retaining only lines that begin with
"  " or "- ", and deleting those 2-character prefixes; use ndiff with -r1.

The second file can be recovered similarly, but by retaining only "  " and
"+ " lines; use ndiff with -r2; or, on Unix, the second file can be
recovered by piping the output through

    sed -n '/^[+ ] /s/^..//p'
"""

__version__ = 1, 7, 0

import difflib, sys

def fail(msg):
    out = sys.stderr.write
    out(msg + "\n\n")
    out(__doc__)
    return 0

# open a file & return the file object; gripe and return 0 if it
# couldn't be opened
def fopen(fname):
    try:
        return open(fname)
    except IOError as detail:
        return fail("couldn't open " + fname + ": " + str(detail))

# open two files & spray the diff to stdout; return false iff a problem
def fcompare(f1name, f2name):
    f1 = fopen(f1name)
    f2 = fopen(f2name)
    if not f1 or not f2:
        return 0

    a = f1.readlines(); f1.close()
    b = f2.readlines(); f2.close()
    for line in difflib.ndiff(a, b):
        print(line, end=' ')

    return 1

# crack args (sys.argv[1:] is normal) & compare;
# return false iff a problem

def main(args):
    import getopt
    try:
        opts, args = getopt.getopt(args, "qr:")
    except getopt.error as detail:
        return fail(str(detail))
    noisy = 1
    qseen = rseen = 0
    for opt, val in opts:
        if opt == "-q":
            qseen = 1
            noisy = 0
        elif opt == "-r":
            rseen = 1
            whichfile = val
    if qseen and rseen:
        return fail("can't specify both -q and -r")
    if rseen:
        if args:
            return fail("no args allowed with -r option")
        if whichfile in ("1", "2"):
            restore(whichfile)
            return 1
        return fail("-r value must be 1 or 2")
    if len(args) != 2:
        return fail("need 2 filename args")
    f1name, f2name = args
    if noisy:
        print('-:', f1name)
        print('+:', f2name)
    return fcompare(f1name, f2name)

# read ndiff output from stdin, and print file1 (which=='1') or
# file2 (which=='2') to stdout

def restore(which):
    restored = difflib.restore(sys.stdin.readlines(), which)
    sys.stdout.writelines(restored)

if __name__ == '__main__':
    main(sys.argv[1:])

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
    * [SequenceMatcher Objects](https://docs.python.org/3/library/difflib.html#sequencematcher-objects)
    * [SequenceMatcher Examples](https://docs.python.org/3/library/difflib.html#sequencematcher-examples)
    * [Differ Objects](https://docs.python.org/3/library/difflib.html#differ-objects)
    * [Differ Example](https://docs.python.org/3/library/difflib.html#differ-example)
    * [A command-line interface to difflib](https://docs.python.org/3/library/difflib.html#a-command-line-interface-to-difflib)
    * [ndiff example](https://docs.python.org/3/library/difflib.html#ndiff-example)


#### Previous topic
[`re` — Regular expression operations](https://docs.python.org/3/library/re.html "previous chapter")
#### Next topic
[`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=difflib+%E2%80%94+Helpers+for+computing+deltas&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdifflib.html&pagesource=library%2Fdifflib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/textwrap.html "textwrap — Text wrapping and filling") |
  * [previous](https://docs.python.org/3/library/re.html "re — Regular expression operations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
