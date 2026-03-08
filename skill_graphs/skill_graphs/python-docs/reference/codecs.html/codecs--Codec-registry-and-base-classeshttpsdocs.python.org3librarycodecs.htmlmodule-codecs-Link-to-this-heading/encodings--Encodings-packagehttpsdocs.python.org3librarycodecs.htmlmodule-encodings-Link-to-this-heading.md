##  `encodings` — Encodings package[¶](https://docs.python.org/3/library/codecs.html#module-encodings "Link to this heading")
This module implements the following functions:

encodings.normalize_encoding(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "Link to this definition")

Normalize encoding name _encoding_.
Normalization works as follows: all non-alphanumeric characters except the dot used for Python package names are collapsed and replaced with a single underscore, leading and trailing underscores are removed. For example, `'  -;#'` becomes `'_'`.
Note that _encoding_ should be ASCII only.
Note
The following functions should not be used directly, except for testing purposes; [`codecs.lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup") should be used instead.

encodings.search_function(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#encodings.search_function "Link to this definition")

Search for the codec module corresponding to the given encoding name _encoding_.
This function first normalizes the _encoding_ using [`normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding"), then looks for a corresponding alias. It attempts to import a codec module from the encodings package using either the alias or the normalized name. If the module is found and defines a valid `getregentry()` function that returns a [`codecs.CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object, the codec is cached and returned.
If the codec module defines a `getaliases()` function any returned aliases are registered for future use.

encodings.win32_code_page_search_function(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#encodings.win32_code_page_search_function "Link to this definition")

Search for a Windows code page encoding _encoding_ of the form `cpXXXX`.
If the code page is valid and supported, return a [`codecs.CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object for it.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.14.
This module implements the following exception:

_exception_ encodings.CodecRegistryError[¶](https://docs.python.org/3/library/codecs.html#encodings.CodecRegistryError "Link to this definition")

Raised when a codec is invalid or incompatible.
