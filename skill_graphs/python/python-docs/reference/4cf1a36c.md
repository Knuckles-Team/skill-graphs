## Pure paths[¶](https://docs.python.org/3/library/pathlib.html#pure-paths "Link to this heading")
Pure path objects provide path-handling operations which don’t actually access a filesystem. There are three ways to access these classes, which we also call _flavours_ :

_class_ pathlib.PurePath(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "Link to this definition")

A generic class that represents the system’s path flavour (instantiating it creates either a [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath") or a [`PureWindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "pathlib.PureWindowsPath")):
Copy```
>>> PurePath('setup.py')      # Running on a Unix machine
PurePosixPath('setup.py')

```

Each element of _pathsegments_ can be either a string representing a path segment, or an object implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface where the [`__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__") method returns a string, such as another path object:
Copy```
>>> PurePath('foo', 'some/path', 'bar')
PurePosixPath('foo/some/path/bar')
>>> PurePath(Path('foo'), Path('bar'))
PurePosixPath('foo/bar')

```

When _pathsegments_ is empty, the current directory is assumed:
Copy```
>>> PurePath()
PurePosixPath('.')

```

If a segment is an absolute path, all previous segments are ignored (like [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join")):
Copy```
>>> PurePath('/etc', '/usr', 'lib64')
PurePosixPath('/usr/lib64')
>>> PureWindowsPath('c:/Windows', 'd:bar')
PureWindowsPath('d:bar')

```

On Windows, the drive is not reset when a rooted relative path segment (e.g., `r'\foo'`) is encountered:
Copy```
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')

```

Spurious slashes and single dots are collapsed, but double dots (`'..'`) and leading double slashes (`'//'`) are not, since this would change the meaning of a path for various reasons (e.g. symbolic links, UNC paths):
Copy```
>>> PurePath('foo//bar')
PurePosixPath('foo/bar')
>>> PurePath('//foo/bar')
PurePosixPath('//foo/bar')
>>> PurePath('foo/./bar')
PurePosixPath('foo/bar')
>>> PurePath('foo/../bar')
PurePosixPath('foo/../bar')

```

(a naïve approach would make `PurePosixPath('foo/../bar')` equivalent to `PurePosixPath('bar')`, which is wrong if `foo` is a symbolic link to another directory)
Pure path objects implement the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface, allowing them to be used anywhere the interface is accepted.
Changed in version 3.6: Added support for the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface.

_class_ pathlib.PurePosixPath(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "Link to this definition")

A subclass of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"), this path flavour represents non-Windows filesystem paths:
Copy```
>>> PurePosixPath('/etc/hosts')
PurePosixPath('/etc/hosts')

```

_pathsegments_ is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").

_class_ pathlib.PureWindowsPath(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "Link to this definition")

A subclass of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"), this path flavour represents Windows filesystem paths, including
Copy```
>>> PureWindowsPath('c:/', 'Users', 'Ximénez')
PureWindowsPath('c:/Users/Ximénez')
>>> PureWindowsPath('//server/share/file')
PureWindowsPath('//server/share/file')

```

_pathsegments_ is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").
Regardless of the system you’re running on, you can instantiate all of these classes, since they don’t provide any operation that does system calls.
### General properties[¶](https://docs.python.org/3/library/pathlib.html#general-properties "Link to this heading")
Paths are immutable and [hashable](https://docs.python.org/3/glossary.html#term-hashable). Paths of a same flavour are comparable and orderable. These properties respect the flavour’s case-folding semantics:
Copy```
>>> PurePosixPath('foo') == PurePosixPath('FOO')
False
>>> PureWindowsPath('foo') == PureWindowsPath('FOO')
True
>>> PureWindowsPath('FOO') in { PureWindowsPath('foo') }
True
>>> PureWindowsPath('C:') < PureWindowsPath('d:')
True

```

Paths of a different flavour compare unequal and cannot be ordered:
Copy```
>>> PureWindowsPath('foo') == PurePosixPath('foo')
False
>>> PureWindowsPath('foo') < PurePosixPath('foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'PureWindowsPath' and 'PurePosixPath'

```

### Operators[¶](https://docs.python.org/3/library/pathlib.html#operators "Link to this heading")
The slash operator helps create child paths, like [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join"). If the argument is an absolute path, the previous path is ignored. On Windows, the drive is not reset when the argument is a rooted relative path (e.g., `r'\foo'`):
Copy```
>>> p = PurePath('/etc')
>>> p
PurePosixPath('/etc')
>>> p / 'init.d' / 'apache2'
PurePosixPath('/etc/init.d/apache2')
>>> q = PurePath('bin')
>>> '/usr' / q
PurePosixPath('/usr/bin')
>>> p / '/an_absolute_path'
PurePosixPath('/an_absolute_path')
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')

```

A path object can be used anywhere an object implementing [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") is accepted:
Copy```
>>> import os
>>> p = PurePath('/etc')
>>> os.fspath(p)
'/etc'

```

The string representation of a path is the raw filesystem path itself (in native form, e.g. with backslashes under Windows), which you can pass to any function taking a file path as a string:
Copy```
>>> p = PurePath('/etc')
>>> str(p)
'/etc'
>>> p = PureWindowsPath('c:/Program Files')
>>> str(p)
'c:\\Program Files'

```

Similarly, calling [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") on a path gives the raw filesystem path as a bytes object, as encoded by [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode"):
Copy```
>>> bytes(p)
b'/etc'

```

Note
Calling [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") is only recommended under Unix. Under Windows, the unicode form is the canonical representation of filesystem paths.
### Accessing individual parts[¶](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts "Link to this heading")
To access the individual “parts” (components) of a path, use the following property:

PurePath.parts[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parts "Link to this definition")

A tuple giving access to the path’s various components:
Copy```
>>> p = PurePath('/usr/bin/python3')
>>> p.parts
('/', 'usr', 'bin', 'python3')

>>> p = PureWindowsPath('c:/Program Files/PSF')
>>> p.parts
('c:\\', 'Program Files', 'PSF')

```

(note how the drive and local root are regrouped in a single part)
### Methods and properties[¶](https://docs.python.org/3/library/pathlib.html#methods-and-properties "Link to this heading")
Pure paths provide the following methods and properties:

PurePath.parser[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parser "Link to this definition")

The implementation of the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") module used for low-level path parsing and joining: either `posixpath` or `ntpath`.
Added in version 3.13.

PurePath.drive[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.drive "Link to this definition")

A string representing the drive letter or name, if any:
Copy```
>>> PureWindowsPath('c:/Program Files/').drive
'c:'
>>> PureWindowsPath('/Program Files/').drive
''
>>> PurePosixPath('/etc').drive
''

```

UNC shares are also considered drives:
Copy```
>>> PureWindowsPath('//host/share/foo.txt').drive
'\\\\host\\share'

```


PurePath.root[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.root "Link to this definition")

A string representing the (local or global) root, if any:
Copy```
>>> PureWindowsPath('c:/Program Files/').root
'\\'
>>> PureWindowsPath('c:Program Files/').root
''
>>> PurePosixPath('/etc').root
'/'

```

UNC shares always have a root:
Copy```
>>> PureWindowsPath('//host/share').root
'\\'

```

If the path starts with more than two successive slashes, [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath") collapses them:
Copy```
>>> PurePosixPath('//etc').root
'//'
>>> PurePosixPath('///etc').root
'/'
>>> PurePosixPath('////etc').root
'/'

```

Note
This behavior conforms to _The Open Group Base Specifications Issue 6_ , paragraph
_“A pathname that begins with two successive slashes may be interpreted in an implementation-defined manner, although more than two leading slashes shall be treated as a single slash.”_

PurePath.anchor[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.anchor "Link to this definition")

The concatenation of the drive and root:
Copy```
>>> PureWindowsPath('c:/Program Files/').anchor
'c:\\'
>>> PureWindowsPath('c:Program Files/').anchor
'c:'
>>> PurePosixPath('/etc').anchor
'/'
>>> PureWindowsPath('//host/share').anchor
'\\\\host\\share\\'

```


PurePath.parents[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parents "Link to this definition")

An immutable sequence providing access to the logical ancestors of the path:
Copy```
>>> p = PureWindowsPath('c:/foo/bar/setup.py')
>>> p.parents[0]
PureWindowsPath('c:/foo/bar')
>>> p.parents[1]
PureWindowsPath('c:/foo')
>>> p.parents[2]
PureWindowsPath('c:/')

```

Changed in version 3.10: The parents sequence now supports [slices](https://docs.python.org/3/glossary.html#term-slice) and negative index values.

PurePath.parent[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent "Link to this definition")

The logical parent of the path:
Copy```
>>> p = PurePosixPath('/a/b/c/d')
>>> p.parent
PurePosixPath('/a/b/c')

```

You cannot go past an anchor, or empty path:
Copy```
>>> p = PurePosixPath('/')
>>> p.parent
PurePosixPath('/')
>>> p = PurePosixPath('.')
>>> p.parent
PurePosixPath('.')

```

Note
This is a purely lexical operation, hence the following behaviour:
Copy```
>>> p = PurePosixPath('foo/..')
>>> p.parent
PurePosixPath('foo')

```

If you want to walk an arbitrary filesystem path upwards, it is recommended to first call [`Path.resolve()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve "pathlib.Path.resolve") so as to resolve symlinks and eliminate `".."` components.

PurePath.name[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name "Link to this definition")

A string representing the final path component, excluding the drive and root, if any:
Copy```
>>> PurePosixPath('my/library/setup.py').name
'setup.py'

```

UNC drive names are not considered:
Copy```
>>> PureWindowsPath('//some/share/setup.py').name
'setup.py'
>>> PureWindowsPath('//some/share').name
''

```


PurePath.suffix[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix "Link to this definition")

The last dot-separated portion of the final component, if any:
Copy```
>>> PurePosixPath('my/library/setup.py').suffix
'.py'
>>> PurePosixPath('my/library.tar.gz').suffix
'.gz'
>>> PurePosixPath('my/library').suffix
''

```

This is commonly called the file extension.
Changed in version 3.14: A single dot (”`.`”) is considered a valid suffix.

PurePath.suffixes[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffixes "Link to this definition")

A list of the path’s suffixes, often called file extensions:
Copy```
>>> PurePosixPath('my/library.tar.gar').suffixes
['.tar', '.gar']
>>> PurePosixPath('my/library.tar.gz').suffixes
['.tar', '.gz']
>>> PurePosixPath('my/library').suffixes
[]

```

Changed in version 3.14: A single dot (”`.`”) is considered a valid suffix.

PurePath.stem[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem "Link to this definition")

The final path component, without its suffix:
Copy```
>>> PurePosixPath('my/library.tar.gz').stem
'library.tar'
>>> PurePosixPath('my/library.tar').stem
'library'
>>> PurePosixPath('my/library').stem
'library'

```

Changed in version 3.14: A single dot (”`.`”) is considered a valid suffix.

PurePath.as_posix()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.as_posix "Link to this definition")

Return a string representation of the path with forward slashes (`/`):
Copy```
>>> p = PureWindowsPath('c:\\windows')
>>> str(p)
'c:\\windows'
>>> p.as_posix()
'c:/windows'

```


PurePath.is_absolute()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.is_absolute "Link to this definition")

Return whether the path is absolute or not. A path is considered absolute if it has both a root and (if the flavour allows) a drive:
Copy```
>>> PurePosixPath('/a/b').is_absolute()
True
>>> PurePosixPath('a/b').is_absolute()
False

>>> PureWindowsPath('c:/a/b').is_absolute()
True
>>> PureWindowsPath('/a/b').is_absolute()
False
>>> PureWindowsPath('c:').is_absolute()
False
>>> PureWindowsPath('//some/share').is_absolute()
True

```


PurePath.is_relative_to(_other_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.is_relative_to "Link to this definition")

Return whether or not this path is relative to the _other_ path.
Copy```
>>> p = PurePath('/etc/passwd')
>>> p.is_relative_to('/etc')
True
>>> p.is_relative_to('/usr')
False

```

This method is string-based; it neither accesses the filesystem nor treats “`..`” segments specially. The following code is equivalent:
Copy```
>>> u = PurePath('/usr')
>>> u == p or u in p.parents
False

```

Added in version 3.9.
Deprecated since version 3.12, removed in version 3.14: Passing additional arguments is deprecated; if supplied, they are joined with _other_.

PurePath.is_reserved()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.is_reserved "Link to this definition")

With [`PureWindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "pathlib.PureWindowsPath"), return `True` if the path is considered reserved under Windows, `False` otherwise. With [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath"), `False` is always returned.
Changed in version 3.13: Windows path names that contain a colon, or end with a dot or a space, are considered reserved. UNC paths may be reserved.
Deprecated since version 3.13, will be removed in version 3.15: This method is deprecated; use [`os.path.isreserved()`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved") to detect reserved paths on Windows.

PurePath.joinpath(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath "Link to this definition")

Calling this method is equivalent to combining the path with each of the given _pathsegments_ in turn:
Copy```
>>> PurePosixPath('/etc').joinpath('passwd')
PurePosixPath('/etc/passwd')
>>> PurePosixPath('/etc').joinpath(PurePosixPath('passwd'))
PurePosixPath('/etc/passwd')
>>> PurePosixPath('/etc').joinpath('init.d', 'apache2')
PurePosixPath('/etc/init.d/apache2')
>>> PureWindowsPath('c:').joinpath('/Program Files')
PureWindowsPath('c:/Program Files')

```


PurePath.full_match(_pattern_ , _*_ , _case_sensitive =None_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.full_match "Link to this definition")

Match this path against the provided glob-style pattern. Return `True` if matching is successful, `False` otherwise. For example:
Copy```
>>> PurePath('a/b.py').full_match('a/*.py')
True
>>> PurePath('a/b.py').full_match('*.py')
False
>>> PurePath('/a/b/c.py').full_match('/a/**')
True
>>> PurePath('/a/b/c.py').full_match('**/*.py')
True

```

See also
[Pattern language](https://docs.python.org/3/library/pathlib.html#pathlib-pattern-language) documentation.
As with other methods, case-sensitivity follows platform defaults:
Copy```
>>> PurePosixPath('b.py').full_match('*.PY')
False
>>> PureWindowsPath('b.py').full_match('*.PY')
True

```

Set _case_sensitive_ to `True` or `False` to override this behaviour.
Added in version 3.13.

PurePath.match(_pattern_ , _*_ , _case_sensitive =None_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.match "Link to this definition")

Match this path against the provided non-recursive glob-style pattern. Return `True` if matching is successful, `False` otherwise.
This method is similar to [`full_match()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.full_match "pathlib.PurePath.full_match"), but empty patterns aren’t allowed ([`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised), the recursive wildcard “`**`” isn’t supported (it acts like non-recursive “`*`”), and if a relative pattern is provided, then matching is done from the right:
Copy```
>>> PurePath('a/b.py').match('*.py')
True
>>> PurePath('/a/b/c.py').match('b/*.py')
True
>>> PurePath('/a/b/c.py').match('a/*.py')
False

```

Changed in version 3.12: The _pattern_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.12: The _case_sensitive_ parameter was added.

PurePath.relative_to(_other_ , _walk_up =False_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to "Link to this definition")

Compute a version of this path relative to the path represented by _other_. If it’s impossible, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised:
Copy```
>>> p = PurePosixPath('/etc/passwd')
>>> p.relative_to('/')
PurePosixPath('etc/passwd')
>>> p.relative_to('/etc')
PurePosixPath('passwd')
>>> p.relative_to('/usr')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 941, in relative_to
    raise ValueError(error_message.format(str(self), str(formatted)))
ValueError: '/etc/passwd' is not in the subpath of '/usr' OR one path is relative and the other is absolute.

```

When _walk_up_ is false (the default), the path must start with _other_. When the argument is true, `..` entries may be added to form the relative path. In all other cases, such as the paths referencing different drives, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.:
Copy```
>>> p.relative_to('/usr', walk_up=True)
PurePosixPath('../etc/passwd')
>>> p.relative_to('foo', walk_up=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 941, in relative_to
    raise ValueError(error_message.format(str(self), str(formatted)))
ValueError: '/etc/passwd' is not on the same drive as 'foo' OR one path is relative and the other is absolute.

```

Warning
This function is part of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") and works with strings. It does not check or access the underlying file structure. This can impact the _walk_up_ option as it assumes that no symlinks are present in the path; call [`resolve()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve "pathlib.Path.resolve") first if necessary to resolve symlinks.
Changed in version 3.12: The _walk_up_ parameter was added (old behavior is the same as `walk_up=False`).
Deprecated since version 3.12, removed in version 3.14: Passing additional positional arguments is deprecated; if supplied, they are joined with _other_.

PurePath.with_name(_name_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_name "Link to this definition")

Return a new path with the [`name`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name "pathlib.PurePath.name") changed. If the original path doesn’t have a name, ValueError is raised:
Copy```
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_name('setup.py')
PureWindowsPath('c:/Downloads/setup.py')
>>> p = PureWindowsPath('c:/')
>>> p.with_name('setup.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/antoine/cpython/default/Lib/pathlib.py", line 751, in with_name
    raise ValueError("%r has an empty name" % (self,))
ValueError: PureWindowsPath('c:/') has an empty name

```


PurePath.with_stem(_stem_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_stem "Link to this definition")

Return a new path with the [`stem`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem "pathlib.PurePath.stem") changed. If the original path doesn’t have a name, ValueError is raised:
Copy```
>>> p = PureWindowsPath('c:/Downloads/draft.txt')
>>> p.with_stem('final')
PureWindowsPath('c:/Downloads/final.txt')
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_stem('lib')
PureWindowsPath('c:/Downloads/lib.gz')
>>> p = PureWindowsPath('c:/')
>>> p.with_stem('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/antoine/cpython/default/Lib/pathlib.py", line 861, in with_stem
    return self.with_name(stem + self.suffix)
  File "/home/antoine/cpython/default/Lib/pathlib.py", line 851, in with_name
    raise ValueError("%r has an empty name" % (self,))
ValueError: PureWindowsPath('c:/') has an empty name

```

Added in version 3.9.

PurePath.with_suffix(_suffix_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_suffix "Link to this definition")

Return a new path with the [`suffix`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix "pathlib.PurePath.suffix") changed. If the original path doesn’t have a suffix, the new _suffix_ is appended instead. If the _suffix_ is an empty string, the original suffix is removed:
Copy```
>>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
>>> p.with_suffix('.bz2')
PureWindowsPath('c:/Downloads/pathlib.tar.bz2')
>>> p = PureWindowsPath('README')
>>> p.with_suffix('.txt')
PureWindowsPath('README.txt')
>>> p = PureWindowsPath('README.txt')
>>> p.with_suffix('')
PureWindowsPath('README')

```

Changed in version 3.14: A single dot (”`.`”) is considered a valid suffix. In previous versions, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if a single dot is supplied.

PurePath.with_segments(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_segments "Link to this definition")

Create a new path object of the same type by combining the given _pathsegments_. This method is called whenever a derivative path is created, such as from [`parent`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent "pathlib.PurePath.parent") and [`relative_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to "pathlib.PurePath.relative_to"). Subclasses may override this method to pass information to derivative paths, for example:
Copy```
from pathlib import PurePosixPath

class MyPath(PurePosixPath):
    def __init__(self, *pathsegments, session_id):
        super().__init__(*pathsegments)
        self.session_id = session_id

    def with_segments(self, *pathsegments):
        return type(self)(*pathsegments, session_id=self.session_id)

etc = MyPath('/etc', session_id=42)
hosts = etc / 'hosts'
print(hosts.session_id)  # 42

```

Added in version 3.12.
