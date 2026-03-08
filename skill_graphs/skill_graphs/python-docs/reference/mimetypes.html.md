[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html)
    * [MimeTypes objects](https://docs.python.org/3/library/mimetypes.html#mimetypes-objects)
    * [Command-line usage](https://docs.python.org/3/library/mimetypes.html#command-line-usage)
    * [Command-line example](https://docs.python.org/3/library/mimetypes.html#command-line-example)


#### Previous topic
[`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3/library/mailbox.html "previous chapter")
#### Next topic
[`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=mimetypes+%E2%80%94+Map+filenames+to+MIME+types&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmimetypes.html&pagesource=library%2Fmimetypes.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
  * [previous](https://docs.python.org/3/library/mailbox.html "mailbox — Manipulate mailboxes in various formats") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html)
  * |
  * Theme  Auto Light Dark |


#  `mimetypes` — Map filenames to MIME types[¶](https://docs.python.org/3/library/mimetypes.html#module-mimetypes "Link to this heading")
**Source code:**
* * *
The `mimetypes` module converts between a filename or URL and the MIME type associated with the filename extension. Conversions are provided from filename to MIME type and from MIME type to filename extension; encodings are not supported for the latter conversion.
The module provides one class and a number of convenience functions. The functions are the normal interface to this module, but some applications may be interested in the class as well.
The functions described below provide the primary interface for this module. If the module has not been initialized, they will call [`init()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.init "mimetypes.init") if they rely on the information `init()` sets up.

mimetypes.guess_type(_url_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "Link to this definition")

Guess the type of a file based on its filename, path or URL, given by _url_. URL can be a string or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
The return value is a tuple `(type, encoding)` where _type_ is `None` if the type can’t be guessed (missing or unknown suffix) or a string of the form `'type/subtype'`, usable for a MIME _content-type_ header.
_encoding_ is `None` for no encoding or the name of the program used to encode (e.g. **compress** or **gzip**). The encoding is suitable for use as a _Content-Encoding_ header, **not** as a _Content-Transfer-Encoding_ header. The mappings are table driven. Encoding suffixes are case sensitive; type suffixes are first tried case sensitively, then case insensitively.
The optional _strict_ argument is a flag specifying whether the list of known MIME types is limited to only the official types _strict_ is `True` (the default), only the IANA types are supported; when _strict_ is `False`, some additional non-standard but commonly used MIME types are also recognized.
Changed in version 3.8: Added support for _url_ being a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Deprecated since version 3.13: Passing a file path instead of URL is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated). Use [`guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type") for this.

mimetypes.guess_file_type(_path_ , _*_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "Link to this definition")

Guess the type of a file based on its path, given by _path_. Similar to the [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function, but accepts a path instead of URL. Path can be a string, a bytes object or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Added in version 3.13.

mimetypes.guess_all_extensions(_type_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_all_extensions "Link to this definition")

Guess the extensions for a file based on its MIME type, given by _type_. The return value is a list of strings giving all possible filename extensions, including the leading dot (`'.'`). The extensions are not guaranteed to have been associated with any particular data stream, but would be mapped to the MIME type _type_ by [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") and [`guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type").
The optional _strict_ argument has the same meaning as with the [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function.

mimetypes.guess_extension(_type_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_extension "Link to this definition")

Guess the extension for a file based on its MIME type, given by _type_. The return value is a string giving a filename extension, including the leading dot (`'.'`). The extension is not guaranteed to have been associated with any particular data stream, but would be mapped to the MIME type _type_ by [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") and [`guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type"). If no extension can be guessed for _type_ , `None` is returned.
The optional _strict_ argument has the same meaning as with the [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function.
Some additional functions and data items are available for controlling the behavior of the module.

mimetypes.init(_files =None_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.init "Link to this definition")

Initialize the internal data structures. If given, _files_ must be a sequence of file names which should be used to augment the default type map. If omitted, the file names to use are taken from [`knownfiles`](https://docs.python.org/3/library/mimetypes.html#mimetypes.knownfiles "mimetypes.knownfiles"); on Windows, the current registry settings are loaded. Each file named in _files_ or `knownfiles` takes precedence over those named before it. Calling `init()` repeatedly is allowed.
Specifying an empty list for _files_ will prevent the system defaults from being applied: only the well-known values will be present from a built-in list.
If _files_ is `None` the internal data structure is completely rebuilt to its initial default value. This is a stable operation and will produce the same results when called multiple times.
Changed in version 3.2: Previously, Windows registry settings were ignored.

mimetypes.read_mime_types(_filename_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.read_mime_types "Link to this definition")

Load the type map given in the file _filename_ , if it exists. The type map is returned as a dictionary mapping filename extensions, including the leading dot (`'.'`), to strings of the form `'type/subtype'`. If the file _filename_ does not exist or cannot be read, `None` is returned.

mimetypes.add_type(_type_ , _ext_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.add_type "Link to this definition")

Add a mapping from the MIME type _type_ to the extension _ext_. When the extension is already known, the new type will replace the old one. When the type is already known the extension will be added to the list of known extensions.
When _strict_ is `True` (the default), the mapping will be added to the official MIME types, otherwise to the non-standard ones.

mimetypes.inited[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.inited "Link to this definition")

Flag indicating whether or not the global data structures have been initialized. This is set to `True` by [`init()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.init "mimetypes.init").

mimetypes.knownfiles[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.knownfiles "Link to this definition")

List of type map file names commonly installed. These files are typically named `mime.types` and are installed in different locations by different packages.

mimetypes.suffix_map[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.suffix_map "Link to this definition")

Dictionary mapping suffixes to suffixes. This is used to allow recognition of encoded files for which the encoding and the type are indicated by the same extension. For example, the `.tgz` extension is mapped to `.tar.gz` to allow the encoding and type to be recognized separately.

mimetypes.encodings_map[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.encodings_map "Link to this definition")

Dictionary mapping filename extensions to encoding types.

mimetypes.types_map[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.types_map "Link to this definition")

Dictionary mapping filename extensions to MIME types.

mimetypes.common_types[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.common_types "Link to this definition")

Dictionary mapping filename extensions to non-standard, but commonly found MIME types.
An example usage of the module:
Copy```
>>> import mimetypes
>>> mimetypes.init()
>>> mimetypes.knownfiles
['/etc/mime.types', '/etc/httpd/mime.types', ... ]
>>> mimetypes.suffix_map['.tgz']
'.tar.gz'
>>> mimetypes.encodings_map['.gz']
'gzip'
>>> mimetypes.types_map['.tgz']
'application/x-tar-gz'

```

## MimeTypes objects[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes-objects "Link to this heading")
The [`MimeTypes`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes "mimetypes.MimeTypes") class may be useful for applications which may want more than one MIME-type database; it provides an interface similar to the one of the `mimetypes` module.

_class_ mimetypes.MimeTypes(_filenames =()_, _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes "Link to this definition")

This class represents a MIME-types database. By default, it provides access to the same database as the rest of this module. The initial database is a copy of that provided by the module, and may be extended by loading additional `mime.types`-style files into the database using the [`read()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.read "mimetypes.MimeTypes.read") or [`readfp()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.readfp "mimetypes.MimeTypes.readfp") methods. The mapping dictionaries may also be cleared before loading additional data if the default data is not desired.
The optional _filenames_ parameter can be used to cause additional files to be loaded “on top” of the default database.

suffix_map[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.suffix_map "Link to this definition")

Dictionary mapping suffixes to suffixes. This is used to allow recognition of encoded files for which the encoding and the type are indicated by the same extension. For example, the `.tgz` extension is mapped to `.tar.gz` to allow the encoding and type to be recognized separately. This is initially a copy of the global [`suffix_map`](https://docs.python.org/3/library/mimetypes.html#mimetypes.suffix_map "mimetypes.suffix_map") defined in the module.

encodings_map[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.encodings_map "Link to this definition")

Dictionary mapping filename extensions to encoding types. This is initially a copy of the global [`encodings_map`](https://docs.python.org/3/library/mimetypes.html#mimetypes.encodings_map "mimetypes.encodings_map") defined in the module.

types_map[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.types_map "Link to this definition")

Tuple containing two dictionaries, mapping filename extensions to MIME types: the first dictionary is for the non-standards types and the second one is for the standard types. They are initialized by [`common_types`](https://docs.python.org/3/library/mimetypes.html#mimetypes.common_types "mimetypes.common_types") and [`types_map`](https://docs.python.org/3/library/mimetypes.html#mimetypes.types_map "mimetypes.types_map").

types_map_inv[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.types_map_inv "Link to this definition")

Tuple containing two dictionaries, mapping MIME types to a list of filename extensions: the first dictionary is for the non-standards types and the second one is for the standard types. They are initialized by [`common_types`](https://docs.python.org/3/library/mimetypes.html#mimetypes.common_types "mimetypes.common_types") and [`types_map`](https://docs.python.org/3/library/mimetypes.html#mimetypes.types_map "mimetypes.types_map").

guess_extension(_type_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.guess_extension "Link to this definition")

Similar to the [`guess_extension()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_extension "mimetypes.guess_extension") function, using the tables stored as part of the object.

guess_type(_url_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.guess_type "Link to this definition")

Similar to the [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type") function, using the tables stored as part of the object.

guess_file_type(_path_ , _*_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.guess_file_type "Link to this definition")

Similar to the [`guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type") function, using the tables stored as part of the object.
Added in version 3.13.

guess_all_extensions(_type_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.guess_all_extensions "Link to this definition")

Similar to the [`guess_all_extensions()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_all_extensions "mimetypes.guess_all_extensions") function, using the tables stored as part of the object.

read(_filename_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.read "Link to this definition")

Load MIME information from a file named _filename_. This uses [`readfp()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.readfp "mimetypes.MimeTypes.readfp") to parse the file.
If _strict_ is `True`, information will be added to list of standard types, else to the list of non-standard types.

readfp(_fp_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.readfp "Link to this definition")

Load MIME type information from an open file _fp_. The file must have the format of the standard `mime.types` files.
If _strict_ is `True`, information will be added to the list of standard types, else to the list of non-standard types.

read_windows_registry(_strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.read_windows_registry "Link to this definition")

Load MIME type information from the Windows registry.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
If _strict_ is `True`, information will be added to the list of standard types, else to the list of non-standard types.
Added in version 3.2.

add_type(_type_ , _ext_ , _strict =True_)[¶](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.add_type "Link to this definition")

Add a mapping from the MIME type _type_ to the extension _ext_. Valid extensions start with a ‘.’ or are empty. When the extension is already known, the new type will replace the old one. When the type is already known the extension will be added to the list of known extensions.
When _strict_ is `True` (the default), the mapping will be added to the official MIME types, otherwise to the non-standard ones.
Deprecated since version 3.14, will be removed in version 3.16: Invalid, undotted extensions will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") in Python 3.16.
## Command-line usage[¶](https://docs.python.org/3/library/mimetypes.html#command-line-usage "Link to this heading")
The `mimetypes` module can be executed as a script from the command line.
Copy```
python -m mimetypes [-h] [-e] [-l] type [type ...]

```

The following options are accepted:

-h[¶](https://docs.python.org/3/library/mimetypes.html#cmdoption-mimetypes-h "Link to this definition")


--help[¶](https://docs.python.org/3/library/mimetypes.html#cmdoption-mimetypes-help "Link to this definition")

Show the help message and exit.

-e[¶](https://docs.python.org/3/library/mimetypes.html#cmdoption-mimetypes-e "Link to this definition")


--extension[¶](https://docs.python.org/3/library/mimetypes.html#cmdoption-mimetypes-extension "Link to this definition")

Guess extension instead of type.

-l[¶](https://docs.python.org/3/library/mimetypes.html#cmdoption-mimetypes-l "Link to this definition")


--lenient[¶](https://docs.python.org/3/library/mimetypes.html#cmdoption-mimetypes-lenient "Link to this definition")

Additionally search for some common, but non-standard types.
By default the script converts MIME types to file extensions. However, if `--extension` is specified, it converts file extensions to MIME types.
For each `type` entry, the script writes a line into the standard output stream. If an unknown type occurs, it writes an error message into the standard error stream and exits with the return code `1`.
## Command-line example[¶](https://docs.python.org/3/library/mimetypes.html#command-line-example "Link to this heading")
Here are some examples of typical usage of the `mimetypes` command-line interface:
Copy```
$ # get a MIME type by a file name
$ python -m mimetypes filename.png
type: image/png encoding: None

$ # get a MIME type by a URL
$ python -m mimetypes https://example.com/filename.txt
type: text/plain encoding: None

$ # get a complex MIME type
$ python -m mimetypes filename.tar.gz
type: application/x-tar encoding: gzip

$ # get a MIME type for a rare file extension
$ python -m mimetypes filename.pict
error: unknown extension of filename.pict

$ # now look in the extended database built into Python
$ python -m mimetypes --lenient filename.pict
type: image/pict encoding: None

$ # get a file extension by a MIME type
$ python -m mimetypes --extension text/javascript
.js

$ # get a file extension by a rare MIME type
$ python -m mimetypes --extension text/xul
error: unknown type text/xul

$ # now look in the extended database again
$ python -m mimetypes --extension --lenient text/xul
.xul

$ # try to feed an unknown file extension
$ python -m mimetypes filename.sh filename.nc filename.xxx filename.txt
type: application/x-sh encoding: None
type: application/x-netcdf encoding: None
error: unknown extension of filename.xxx

$ # try to feed an unknown MIME type
$ python -m mimetypes --extension audio/aac audio/opus audio/future audio/x-wav
.aac
.opus
error: unknown type audio/future

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html)
    * [MimeTypes objects](https://docs.python.org/3/library/mimetypes.html#mimetypes-objects)
    * [Command-line usage](https://docs.python.org/3/library/mimetypes.html#command-line-usage)
    * [Command-line example](https://docs.python.org/3/library/mimetypes.html#command-line-example)


#### Previous topic
[`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3/library/mailbox.html "previous chapter")
#### Next topic
[`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=mimetypes+%E2%80%94+Map+filenames+to+MIME+types&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmimetypes.html&pagesource=library%2Fmimetypes.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
  * [previous](https://docs.python.org/3/library/mailbox.html "mailbox — Manipulate mailboxes in various formats") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html)
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
