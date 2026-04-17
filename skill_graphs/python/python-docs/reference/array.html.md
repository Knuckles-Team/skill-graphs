[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html "previous chapter")
#### Next topic
[`weakref` — Weak references](https://docs.python.org/3/library/weakref.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=array+%E2%80%94+Efficient+arrays+of+numeric+values&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Farray.html&pagesource=library%2Farray.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/weakref.html "weakref — Weak references") |
  * [previous](https://docs.python.org/3/library/bisect.html "bisect — Array bisection algorithm") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`array` — Efficient arrays of numeric values](https://docs.python.org/3/library/array.html)
  * |
  * Theme  Auto Light Dark |


#  `array` — Efficient arrays of numeric values[¶](https://docs.python.org/3/library/array.html#module-array "Link to this heading")
* * *
This module defines an object type which can compactly represent an array of basic values: characters, integers, floating-point numbers. Arrays are mutable [sequence](https://docs.python.org/3/glossary.html#term-sequence) types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a _type code_ , which is a single character. The following type codes are defined:
Type code | C Type | Python Type | Minimum size in bytes | Notes
---|---|---|---|---
`'b'` | signed char | int | 1 |
`'B'` | unsigned char | int | 1 |
`'u'` | wchar_t | Unicode character | 2 | (1)
`'w'` | Py_UCS4 | Unicode character | 4 | (2)
`'h'` | signed short | int | 2 |
`'H'` | unsigned short | int | 2 |
`'i'` | signed int | int | 2 |
`'I'` | unsigned int | int | 2 |
`'l'` | signed long | int | 4 |
`'L'` | unsigned long | int | 4 |
`'q'` | signed long long | int | 8 |
`'Q'` | unsigned long long | int | 8 |
`'f'` | float | float | 4 |
`'d'` | double | float | 8 |
Notes:
  1. It can be 16 bits or 32 bits depending on the platform.
Changed in version 3.9: `array('u')` now uses `wchar_t` as C type instead of deprecated `Py_UNICODE`. This change doesn’t affect its behavior because `Py_UNICODE` is alias of `wchar_t` since Python 3.3.
Deprecated since version 3.3, will be removed in version 3.16: Please migrate to `'w'` typecode.
  2. Added in version 3.13.


The actual representation of values is determined by the machine architecture (strictly speaking, by the C implementation). The actual size can be accessed through the [`array.itemsize`](https://docs.python.org/3/library/array.html#array.array.itemsize "array.array.itemsize") attribute.
The module defines the following item:

array.typecodes[¶](https://docs.python.org/3/library/array.html#array.typecodes "Link to this definition")

A string with all available type codes.
The module defines the following type:

_class_ array.array(_typecode_[, _initializer_])[¶](https://docs.python.org/3/library/array.html#array.array "Link to this definition")

A new array whose items are restricted by _typecode_ , and initialized from the optional _initializer_ value, which must be a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") object, a Unicode string, or iterable over elements of the appropriate type.
If given a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") object, the initializer is passed to the new array’s [`frombytes()`](https://docs.python.org/3/library/array.html#array.array.frombytes "array.array.frombytes") method; if given a Unicode string, the initializer is passed to the [`fromunicode()`](https://docs.python.org/3/library/array.html#array.array.fromunicode "array.array.fromunicode") method; otherwise, the initializer’s iterator is passed to the [`extend()`](https://docs.python.org/3/library/array.html#array.array.extend "array.array.extend") method to add initial items to the array.
Array objects support the ordinary [mutable](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) [sequence](https://docs.python.org/3/glossary.html#term-sequence) operations of indexing, slicing, concatenation, and multiplication. When using slice assignment, the assigned value must be an array object with the same type code; in all other cases, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised. Array objects also implement the buffer interface, and may be used wherever [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) are supported.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `array.__new__` with arguments `typecode`, `initializer`.

typecode[¶](https://docs.python.org/3/library/array.html#array.array.typecode "Link to this definition")

The typecode character used to create the array.

itemsize[¶](https://docs.python.org/3/library/array.html#array.array.itemsize "Link to this definition")

The length in bytes of one array item in the internal representation.

append(_x_)[¶](https://docs.python.org/3/library/array.html#array.array.append "Link to this definition")

Append a new item with value _x_ to the end of the array.

buffer_info()[¶](https://docs.python.org/3/library/array.html#array.array.buffer_info "Link to this definition")

Return a tuple `(address, length)` giving the current memory address and the length in elements of the buffer used to hold array’s contents. The size of the memory buffer in bytes can be computed as `array.buffer_info()[1] * array.itemsize`. This is occasionally useful when working with low-level (and inherently unsafe) I/O interfaces that require memory addresses, such as certain `ioctl()` operations. The returned numbers are valid as long as the array exists and no length-changing operations are applied to it.
Note
When using array objects from code written in C or C++ (the only way to effectively make use of this information), it makes more sense to use the buffer interface supported by array objects. This method is maintained for backward compatibility and should be avoided in new code. The buffer interface is documented in [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects).

byteswap()[¶](https://docs.python.org/3/library/array.html#array.array.byteswap "Link to this definition")

“Byteswap” all items of the array. This is only supported for values which are 1, 2, 4, or 8 bytes in size; for other types of values, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. It is useful when reading data from a file written on a machine with a different byte order.

count(_x_)[¶](https://docs.python.org/3/library/array.html#array.array.count "Link to this definition")

Return the number of occurrences of _x_ in the array.

extend(_iterable_)[¶](https://docs.python.org/3/library/array.html#array.array.extend "Link to this definition")

Append items from _iterable_ to the end of the array. If _iterable_ is another array, it must have _exactly_ the same type code; if not, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") will be raised. If _iterable_ is not an array, it must be iterable and its elements must be the right type to be appended to the array.

frombytes(_buffer_)[¶](https://docs.python.org/3/library/array.html#array.array.frombytes "Link to this definition")

Appends items from the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), interpreting its content as an array of machine values (as if it had been read from a file using the [`fromfile()`](https://docs.python.org/3/library/array.html#array.array.fromfile "array.array.fromfile") method).
Added in version 3.2: `fromstring()` is renamed to `frombytes()` for clarity.

fromfile(_f_ , _n_)[¶](https://docs.python.org/3/library/array.html#array.array.fromfile "Link to this definition")

Read _n_ items (as machine values) from the [file object](https://docs.python.org/3/glossary.html#term-file-object) _f_ and append them to the end of the array. If less than _n_ items are available, [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError") is raised, but the items that were available are still inserted into the array.

fromlist(_list_)[¶](https://docs.python.org/3/library/array.html#array.array.fromlist "Link to this definition")

Append items from the list. This is equivalent to `for x in list: a.append(x)` except that if there is a type error, the array is unchanged.

fromunicode(_s_)[¶](https://docs.python.org/3/library/array.html#array.array.fromunicode "Link to this definition")

Extends this array with data from the given Unicode string. The array must have type code `'u'` or `'w'`; otherwise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. Use `array.frombytes(unicodestring.encode(enc))` to append Unicode data to an array of some other type.

index(_x_[, _start_[, _stop_]])[¶](https://docs.python.org/3/library/array.html#array.array.index "Link to this definition")

Return the smallest _i_ such that _i_ is the index of the first occurrence of _x_ in the array. The optional arguments _start_ and _stop_ can be specified to search for _x_ within a subsection of the array. Raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _x_ is not found.
Changed in version 3.10: Added optional _start_ and _stop_ parameters.

insert(_i_ , _x_)[¶](https://docs.python.org/3/library/array.html#array.array.insert "Link to this definition")

Insert a new item with value _x_ in the array before position _i_. Negative values are treated as being relative to the end of the array.

pop([_i_])[¶](https://docs.python.org/3/library/array.html#array.array.pop "Link to this definition")

Removes the item with the index _i_ from the array and returns it. The optional argument defaults to `-1`, so that by default the last item is removed and returned.

remove(_x_)[¶](https://docs.python.org/3/library/array.html#array.array.remove "Link to this definition")

Remove the first occurrence of _x_ from the array.

clear()[¶](https://docs.python.org/3/library/array.html#array.array.clear "Link to this definition")

Remove all elements from the array.
Added in version 3.13.

reverse()[¶](https://docs.python.org/3/library/array.html#array.array.reverse "Link to this definition")

Reverse the order of the items in the array.

tobytes()[¶](https://docs.python.org/3/library/array.html#array.array.tobytes "Link to this definition")

Convert the array to an array of machine values and return the bytes representation (the same sequence of bytes that would be written to a file by the [`tofile()`](https://docs.python.org/3/library/array.html#array.array.tofile "array.array.tofile") method.)
Added in version 3.2: `tostring()` is renamed to `tobytes()` for clarity.

tofile(_f_)[¶](https://docs.python.org/3/library/array.html#array.array.tofile "Link to this definition")

Write all items (as machine values) to the [file object](https://docs.python.org/3/glossary.html#term-file-object) _f_.

tolist()[¶](https://docs.python.org/3/library/array.html#array.array.tolist "Link to this definition")

Convert the array to an ordinary list with the same items.

tounicode()[¶](https://docs.python.org/3/library/array.html#array.array.tounicode "Link to this definition")

Convert the array to a Unicode string. The array must have a type `'u'` or `'w'`; otherwise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. Use `array.tobytes().decode(enc)` to obtain a Unicode string from an array of some other type.
The string representation of array objects has the form `array(typecode, initializer)`. The _initializer_ is omitted if the array is empty, otherwise it is a Unicode string if the _typecode_ is `'u'` or `'w'`, otherwise it is a list of numbers. The string representation is guaranteed to be able to be converted back to an array with the same type and value using [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"), so long as the [`array`](https://docs.python.org/3/library/array.html#array.array "array.array") class has been imported using `from array import array`. Variables `inf` and `nan` must also be defined if it contains corresponding floating-point values. Examples:
Copy```
array('l')
array('w', 'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.14, -inf, nan])

```

See also

Module [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")

Packing and unpacking of heterogeneous binary data.
The NumPy package defines another array type.
#### Previous topic
[`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html "previous chapter")
#### Next topic
[`weakref` — Weak references](https://docs.python.org/3/library/weakref.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=array+%E2%80%94+Efficient+arrays+of+numeric+values&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Farray.html&pagesource=library%2Farray.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/weakref.html "weakref — Weak references") |
  * [previous](https://docs.python.org/3/library/bisect.html "bisect — Array bisection algorithm") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`array` — Efficient arrays of numeric values](https://docs.python.org/3/library/array.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
