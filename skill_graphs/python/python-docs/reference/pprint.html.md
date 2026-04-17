[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html)
    * [Functions](https://docs.python.org/3/library/pprint.html#functions)
    * [PrettyPrinter Objects](https://docs.python.org/3/library/pprint.html#prettyprinter-objects)
    * [Example](https://docs.python.org/3/library/pprint.html#example)


#### Previous topic
[`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html "previous chapter")
#### Next topic
[`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pprint+%E2%80%94+Data+pretty+printer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpprint.html&pagesource=library%2Fpprint.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/reprlib.html "reprlib — Alternate repr\(\) implementation") |
  * [previous](https://docs.python.org/3/library/copy.html "copy — Shallow and deep copy operations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html)
  * |
  * Theme  Auto Light Dark |


#  `pprint` — Data pretty printer[¶](https://docs.python.org/3/library/pprint.html#module-pprint "Link to this heading")
**Source code:**
* * *
The `pprint` module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter. If the formatted structures include objects which are not fundamental Python types, the representation may not be loadable. This may be the case if objects such as files, sockets or classes are included, as well as many other objects which are not representable as Python literals.
The formatted representation keeps objects on a single line if it can, and breaks them onto multiple lines if they don’t fit within the allowed width, adjustable by the _width_ parameter defaulting to 80 characters.
Changed in version 3.9: Added support for pretty-printing [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace").
Changed in version 3.10: Added support for pretty-printing [`dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass").
## Functions[¶](https://docs.python.org/3/library/pprint.html#functions "Link to this heading")

pprint.pp(_object_ , _stream =None_, _indent =1_, _width =80_, _depth =None_, _*_ , _compact =False_, _sort_dicts =False_, _underscore_numbers =False_)[¶](https://docs.python.org/3/library/pprint.html#pprint.pp "Link to this definition")

Prints the formatted representation of _object_ , followed by a newline. This function may be used in the interactive interpreter instead of the [`print()`](https://docs.python.org/3/library/functions.html#print "print") function for inspecting values. Tip: you can reassign `print = pprint.pp` for use within a scope.

Parameters:

  * **object** – The object to be printed.
  * **stream** ([file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) | None) – A file-like object to which the output will be written by calling its `write()` method. If `None` (the default), [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") is used.
  * **indent** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The amount of indentation added for each nesting level.
  * **width** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The desired maximum number of characters per line in the output. If a structure cannot be formatted within the width constraint, a best effort will be made.
  * **depth** ([_int_](https://docs.python.org/3/library/functions.html#int "int") _|__None_) – The number of nesting levels which may be printed. If the data structure being printed is too deep, the next contained level is replaced by `...`. If `None` (the default), there is no constraint on the depth of the objects being formatted.
  * **compact** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Control the way long [sequences](https://docs.python.org/3/glossary.html#term-sequence) are formatted. If `False` (the default), each item of a sequence will be formatted on a separate line, otherwise as many items as will fit within the _width_ will be formatted on each output line.
  * **sort_dicts** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True`, dictionaries will be formatted with their keys sorted, otherwise they will be displayed in insertion order (the default).
  * **underscore_numbers** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True`, integers will be formatted with the `_` character for a thousands separator, otherwise underscores are not displayed (the default).


Copy```
>>> import pprint
>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> stuff.insert(0, stuff)
>>> pprint.pp(stuff)
[<Recursion on list with id=...>,
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']

```

Added in version 3.8.

pprint.pprint(_object_ , _stream =None_, _indent =1_, _width =80_, _depth =None_, _*_ , _compact =False_, _sort_dicts =True_, _underscore_numbers =False_)[¶](https://docs.python.org/3/library/pprint.html#pprint.pprint "Link to this definition")

Alias for [`pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp") with _sort_dicts_ set to `True` by default, which would automatically sort the dictionaries’ keys, you might want to use `pp()` instead where it is `False` by default.

pprint.pformat(_object_ , _indent =1_, _width =80_, _depth =None_, _*_ , _compact =False_, _sort_dicts =True_, _underscore_numbers =False_)[¶](https://docs.python.org/3/library/pprint.html#pprint.pformat "Link to this definition")

Return the formatted representation of _object_ as a string. _indent_ , _width_ , _depth_ , _compact_ , _sort_dicts_ and _underscore_numbers_ are passed to the [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") constructor as formatting parameters and their meanings are as described in the documentation above.

pprint.isreadable(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.isreadable "Link to this definition")

Determine if the formatted representation of _object_ is “readable”, or can be used to reconstruct the value using [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"). This always returns `False` for recursive objects.
Copy```
>>> pprint.isreadable(stuff)
False

```


pprint.isrecursive(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.isrecursive "Link to this definition")

Determine if _object_ requires a recursive representation. This function is subject to the same limitations as noted in [`saferepr()`](https://docs.python.org/3/library/pprint.html#pprint.saferepr "pprint.saferepr") below and may raise an [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError") if it fails to detect a recursive object.

pprint.saferepr(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.saferepr "Link to this definition")

Return a string representation of _object_ , protected against recursion in some common data structures, namely instances of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") or subclasses whose `__repr__` has not been overridden. If the representation of object exposes a recursive entry, the recursive reference will be represented as `<Recursion on typename with id=number>`. The representation is not otherwise formatted.
Copy```
>>> pprint.saferepr(stuff)
"[<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']"

```

## PrettyPrinter Objects[¶](https://docs.python.org/3/library/pprint.html#prettyprinter-objects "Link to this heading")

_class_ pprint.PrettyPrinter(_indent =1_, _width =80_, _depth =None_, _stream =None_, _*_ , _compact =False_, _sort_dicts =True_, _underscore_numbers =False_)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "Link to this definition")

Construct a `PrettyPrinter` instance.
Arguments have the same meaning as for [`pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp"). Note that they are in a different order, and that _sort_dicts_ defaults to `True`.
Copy```
>>> import pprint
>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> stuff.insert(0, stuff[:])
>>> pp = pprint.PrettyPrinter(indent=4)
>>> pp.pprint(stuff)
[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']
>>> pp = pprint.PrettyPrinter(width=41, compact=True)
>>> pp.pprint(stuff)
[['spam', 'eggs', 'lumberjack',
  'knights', 'ni'],
 'spam', 'eggs', 'lumberjack', 'knights',
 'ni']
>>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
... ('parrot', ('fresh fruit',))))))))
>>> pp = pprint.PrettyPrinter(depth=6)
>>> pp.pprint(tup)
('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))

```

Changed in version 3.4: Added the _compact_ parameter.
Changed in version 3.8: Added the _sort_dicts_ parameter.
Changed in version 3.10: Added the _underscore_numbers_ parameter.
Changed in version 3.11: No longer attempts to write to `sys.stdout` if it is `None`.
[`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") instances have the following methods:

PrettyPrinter.pformat(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.pformat "Link to this definition")

Return the formatted representation of _object_. This takes into account the options passed to the [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") constructor.

PrettyPrinter.pprint(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.pprint "Link to this definition")

Print the formatted representation of _object_ on the configured stream, followed by a newline.
The following methods provide the implementations for the corresponding functions of the same names. Using these methods on an instance is slightly more efficient since new [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") objects don’t need to be created.

PrettyPrinter.isreadable(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.isreadable "Link to this definition")

Determine if the formatted representation of the object is “readable,” or can be used to reconstruct the value using [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"). Note that this returns `False` for recursive objects. If the _depth_ parameter of the [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") is set and the object is deeper than allowed, this returns `False`.

PrettyPrinter.isrecursive(_object_)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.isrecursive "Link to this definition")

Determine if the object requires a recursive representation.
This method is provided as a hook to allow subclasses to modify the way objects are converted to strings. The default implementation uses the internals of the [`saferepr()`](https://docs.python.org/3/library/pprint.html#pprint.saferepr "pprint.saferepr") implementation.

PrettyPrinter.format(_object_ , _context_ , _maxlevels_ , _level_)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.format "Link to this definition")

Returns three values: the formatted version of _object_ as a string, a flag indicating whether the result is readable, and a flag indicating whether recursion was detected. The first argument is the object to be presented. The second is a dictionary which contains the [`id()`](https://docs.python.org/3/library/functions.html#id "id") of objects that are part of the current presentation context (direct and indirect containers for _object_ that are affecting the presentation) as the keys; if an object needs to be presented which is already represented in _context_ , the third return value should be `True`. Recursive calls to the `format()` method should add additional entries for containers to this dictionary. The third argument, _maxlevels_ , gives the requested limit to recursion; this will be `0` if there is no requested limit. This argument should be passed unmodified to recursive calls. The fourth argument, _level_ , gives the current level; recursive calls should be passed a value less than that of the current call.
## Example[¶](https://docs.python.org/3/library/pprint.html#example "Link to this heading")
To demonstrate several uses of the [`pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp") function and its parameters, let’s fetch information about a project from
Copy```
>>> import json
>>> import pprint
>>> from urllib.request import urlopen
>>> with urlopen('https://pypi.org/pypi/sampleproject/1.2.0/json') as resp:
...     project_info = json.load(resp)['info']

```

In its basic form, [`pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp") shows the whole object:
Copy```
>>> pprint.pp(project_info)
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': ['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Software Development :: Build Tools'],
 'description': 'A sample Python project\n'
                '=======================\n'
                '\n'
                'This is the description file for the project.\n'
                '\n'
                'The file should use UTF-8 encoding and be written using '
                'ReStructured Text. It\n'
                'will be used to generate the project webpage on PyPI, and '
                'should be written for\n'
                'that purpose.\n'
                '\n'
                'Typical contents for this file would include an overview of '
                'the project, basic\n'
                'usage examples, etc. Generally, including the project '
                'changelog in here is not\n'
                'a good idea, although a simple "What\'s New" section for the '
                'most recent version\n'
                'may be appropriate.',
 'description_content_type': None,
 'docs_url': None,
 'download_url': 'UNKNOWN',
 'downloads': {'last_day': -1, 'last_month': -1, 'last_week': -1},
 'home_page': 'https://github.com/pypa/sampleproject',
 'keywords': 'sample setuptools development',
 'license': 'MIT',
 'maintainer': None,
 'maintainer_email': None,
 'name': 'sampleproject',
 'package_url': 'https://pypi.org/project/sampleproject/',
 'platform': 'UNKNOWN',
 'project_url': 'https://pypi.org/project/sampleproject/',
 'project_urls': {'Download': 'UNKNOWN',
                  'Homepage': 'https://github.com/pypa/sampleproject'},
 'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
 'requires_dist': None,
 'requires_python': None,
 'summary': 'A sample Python project',
 'version': '1.2.0'}

```

The result can be limited to a certain _depth_ (ellipsis is used for deeper contents):
Copy```
>>> pprint.pp(project_info, depth=1)
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': [...],
 'description': 'A sample Python project\n'
                '=======================\n'
                '\n'
                'This is the description file for the project.\n'
                '\n'
                'The file should use UTF-8 encoding and be written using '
                'ReStructured Text. It\n'
                'will be used to generate the project webpage on PyPI, and '
                'should be written for\n'
                'that purpose.\n'
                '\n'
                'Typical contents for this file would include an overview of '
                'the project, basic\n'
                'usage examples, etc. Generally, including the project '
                'changelog in here is not\n'
                'a good idea, although a simple "What\'s New" section for the '
                'most recent version\n'
                'may be appropriate.',
 'description_content_type': None,
 'docs_url': None,
 'download_url': 'UNKNOWN',
 'downloads': {...},
 'home_page': 'https://github.com/pypa/sampleproject',
 'keywords': 'sample setuptools development',
 'license': 'MIT',
 'maintainer': None,
 'maintainer_email': None,
 'name': 'sampleproject',
 'package_url': 'https://pypi.org/project/sampleproject/',
 'platform': 'UNKNOWN',
 'project_url': 'https://pypi.org/project/sampleproject/',
 'project_urls': {...},
 'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
 'requires_dist': None,
 'requires_python': None,
 'summary': 'A sample Python project',
 'version': '1.2.0'}

```

Additionally, maximum character _width_ can be suggested. If a long object cannot be split, the specified width will be exceeded:
Copy```
>>> pprint.pp(project_info, depth=1, width=60)
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': [...],
 'description': 'A sample Python project\n'
                '=======================\n'
                '\n'
                'This is the description file for the '
                'project.\n'
                '\n'
                'The file should use UTF-8 encoding and be '
                'written using ReStructured Text. It\n'
                'will be used to generate the project '
                'webpage on PyPI, and should be written '
                'for\n'
                'that purpose.\n'
                '\n'
                'Typical contents for this file would '
                'include an overview of the project, '
                'basic\n'
                'usage examples, etc. Generally, including '
                'the project changelog in here is not\n'
                'a good idea, although a simple "What\'s '
                'New" section for the most recent version\n'
                'may be appropriate.',
 'description_content_type': None,
 'docs_url': None,
 'download_url': 'UNKNOWN',
 'downloads': {...},
 'home_page': 'https://github.com/pypa/sampleproject',
 'keywords': 'sample setuptools development',
 'license': 'MIT',
 'maintainer': None,
 'maintainer_email': None,
 'name': 'sampleproject',
 'package_url': 'https://pypi.org/project/sampleproject/',
 'platform': 'UNKNOWN',
 'project_url': 'https://pypi.org/project/sampleproject/',
 'project_urls': {...},
 'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
 'requires_dist': None,
 'requires_python': None,
 'summary': 'A sample Python project',
 'version': '1.2.0'}

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html)
    * [Functions](https://docs.python.org/3/library/pprint.html#functions)
    * [PrettyPrinter Objects](https://docs.python.org/3/library/pprint.html#prettyprinter-objects)
    * [Example](https://docs.python.org/3/library/pprint.html#example)


#### Previous topic
[`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html "previous chapter")
#### Next topic
[`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pprint+%E2%80%94+Data+pretty+printer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpprint.html&pagesource=library%2Fpprint.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/reprlib.html "reprlib — Alternate repr\(\) implementation") |
  * [previous](https://docs.python.org/3/library/copy.html "copy — Shallow and deep copy operations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html)
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
