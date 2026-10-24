## Concrete paths[¶](https://docs.python.org/3/library/pathlib.html#concrete-paths "Link to this heading")
Concrete paths are subclasses of the pure path classes. In addition to operations provided by the latter, they also provide methods to do system calls on path objects. There are three ways to instantiate concrete paths:

_class_ pathlib.Path(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path "Link to this definition")

A subclass of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"), this class represents concrete paths of the system’s path flavour (instantiating it creates either a [`PosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath "pathlib.PosixPath") or a [`WindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath "pathlib.WindowsPath")):
Copy```
>>> Path('setup.py')
PosixPath('setup.py')

```

_pathsegments_ is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").

_class_ pathlib.PosixPath(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath "Link to this definition")

A subclass of [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") and [`PurePosixPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePosixPath "pathlib.PurePosixPath"), this class represents concrete non-Windows filesystem paths:
Copy```
>>> PosixPath('/etc/hosts')
PosixPath('/etc/hosts')

```

_pathsegments_ is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").
Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") on Windows. In previous versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised instead.

_class_ pathlib.WindowsPath(_* pathsegments_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath "Link to this definition")

A subclass of [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") and [`PureWindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "pathlib.PureWindowsPath"), this class represents concrete Windows filesystem paths:
Copy```
>>> WindowsPath('c:/', 'Users', 'Ximénez')
WindowsPath('c:/Users/Ximénez')

```

_pathsegments_ is specified similarly to [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").
Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") on non-Windows platforms. In previous versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised instead.
You can only instantiate the class flavour that corresponds to your system (allowing system calls on non-compatible path flavours could lead to bugs or failures in your application):
Copy```
>>> import os
>>> os.name
'posix'
>>> Path('setup.py')
PosixPath('setup.py')
>>> PosixPath('setup.py')
PosixPath('setup.py')
>>> WindowsPath('setup.py')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pathlib.py", line 798, in __new__
    % (cls.__name__,))
UnsupportedOperation: cannot instantiate 'WindowsPath' on your system

```

Some concrete path methods can raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if a system call fails (for example because the path doesn’t exist).
### Parsing and generating URIs[¶](https://docs.python.org/3/library/pathlib.html#parsing-and-generating-uris "Link to this heading")
Concrete path objects can be created from, and represented as, ‘file’ URIs conforming to
Note
File URIs are not portable across machines with different [filesystem encodings](https://docs.python.org/3/library/os.html#filesystem-encoding).

_classmethod_ Path.from_uri(_uri_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.from_uri "Link to this definition")

Return a new path object from parsing a ‘file’ URI. For example:
Copy```
>>> p = Path.from_uri('file:///etc/hosts')
PosixPath('/etc/hosts')

```

On Windows, DOS device and UNC paths may be parsed from URIs:
Copy```
>>> p = Path.from_uri('file:///c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file://server/share')
WindowsPath('//server/share')

```

Several variant forms are supported:
Copy```
>>> p = Path.from_uri('file:////server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file://///server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file:c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file:/c|/windows')
WindowsPath('c:/windows')

```

[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the URI does not start with `file:`, or the parsed path isn’t absolute.
Added in version 3.13.
Changed in version 3.14: The URL authority is discarded if it matches the local hostname. Otherwise, if the authority isn’t empty or `localhost`, then on Windows a UNC path is returned (as before), and on other platforms a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

Path.as_uri()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.as_uri "Link to this definition")

Represent the path as a ‘file’ URI. [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the path isn’t absolute.
Copy```
>>> p = PosixPath('/etc/passwd')
>>> p.as_uri()
'file:///etc/passwd'
>>> p = WindowsPath('c:/Windows')
>>> p.as_uri()
'file:///c:/Windows'

```

Deprecated since version 3.14, will be removed in version 3.19: Calling this method from [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") rather than [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") is possible but deprecated. The method’s use of [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode") makes it strictly impure.
### Expanding and resolving paths[¶](https://docs.python.org/3/library/pathlib.html#expanding-and-resolving-paths "Link to this heading")

_classmethod_ Path.home()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home "Link to this definition")

Return a new path object representing the user’s home directory (as returned by [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") with `~` construct). If the home directory can’t be resolved, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.
Copy```
>>> Path.home()
PosixPath('/home/antoine')

```

Added in version 3.5.

Path.expanduser()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser "Link to this definition")

Return a new path with expanded `~` and `~user` constructs, as returned by [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser"). If a home directory can’t be resolved, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.
Copy```
>>> p = PosixPath('~/films/Monty Python')
>>> p.expanduser()
PosixPath('/home/eric/films/Monty Python')

```

Added in version 3.5.

_classmethod_ Path.cwd()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd "Link to this definition")

Return a new path object representing the current directory (as returned by [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd "os.getcwd")):
Copy```
>>> Path.cwd()
PosixPath('/home/antoine/pathlib')

```


Path.absolute()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "Link to this definition")

Make the path absolute, without normalization or resolving symlinks. Returns a new path object:
Copy```
>>> p = Path('tests')
>>> p
PosixPath('tests')
>>> p.absolute()
PosixPath('/home/antoine/pathlib/tests')

```


Path.resolve(_strict =False_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve "Link to this definition")

Make the path absolute, resolving any symlinks. A new path object is returned:
Copy```
>>> p = Path()
>>> p
PosixPath('.')
>>> p.resolve()
PosixPath('/home/antoine/pathlib')

```

“`..`” components are also eliminated (this is the only method to do so):
Copy```
>>> p = Path('docs/../setup.py')
>>> p.resolve()
PosixPath('/home/antoine/pathlib/setup.py')

```

If a path doesn’t exist or a symlink loop is encountered, and _strict_ is `True`, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised. If _strict_ is `False`, the path is resolved as far as possible and any remainder is appended without checking whether it exists.
Changed in version 3.6: The _strict_ parameter was added (pre-3.6 behavior is strict).
Changed in version 3.13: Symlink loops are treated like other errors: [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised in strict mode, and no exception is raised in non-strict mode. In previous versions, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised no matter the value of _strict_.

Path.readlink()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.readlink "Link to this definition")

Return the path to which the symbolic link points (as returned by [`os.readlink()`](https://docs.python.org/3/library/os.html#os.readlink "os.readlink")):
Copy```
>>> p = Path('mylink')
>>> p.symlink_to('setup.py')
>>> p.readlink()
PosixPath('setup.py')

```

Added in version 3.9.
Changed in version 3.13: Raises [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation") if [`os.readlink()`](https://docs.python.org/3/library/os.html#os.readlink "os.readlink") is not available. In previous versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") was raised.
### Querying file type and status[¶](https://docs.python.org/3/library/pathlib.html#querying-file-type-and-status "Link to this heading")
Changed in version 3.8: [`exists()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "pathlib.Path.exists"), [`is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "pathlib.Path.is_dir"), [`is_file()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "pathlib.Path.is_file"), [`is_mount()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_mount "pathlib.Path.is_mount"), [`is_symlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink "pathlib.Path.is_symlink"), [`is_block_device()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_block_device "pathlib.Path.is_block_device"), [`is_char_device()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_char_device "pathlib.Path.is_char_device"), [`is_fifo()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_fifo "pathlib.Path.is_fifo"), [`is_socket()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_socket "pathlib.Path.is_socket") now return `False` instead of raising an exception for paths that contain characters unrepresentable at the OS level.
Changed in version 3.14: The methods given above now return `False` instead of raising any [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception from the operating system. In previous versions, some kinds of `OSError` exception are raised, and others suppressed. The new behaviour is consistent with [`os.path.exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists "os.path.exists"), [`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir "os.path.isdir"), etc. Use [`stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to retrieve the file status without suppressing exceptions.

Path.stat(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "Link to this definition")

Return an [`os.stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") object containing information about this path, like [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"). The result is looked up at each call to this method.
This method normally follows symlinks; to stat a symlink add the argument `follow_symlinks=False`, or use [`lstat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat "pathlib.Path.lstat").
Copy```
>>> p = Path('setup.py')
>>> p.stat().st_size
956
>>> p.stat().st_mtime
1327883547.852554

```

Changed in version 3.10: The _follow_symlinks_ parameter was added.

Path.lstat()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat "Link to this definition")

Like [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") but, if the path points to a symbolic link, return the symbolic link’s information rather than its target’s.

Path.exists(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "Link to this definition")

Return `True` if the path points to an existing file or directory. `False` will be returned if the path is invalid, inaccessible or missing. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.
This method normally follows symlinks; to check if a symlink exists, add the argument `follow_symlinks=False`.
Copy```
>>> Path('.').exists()
True
>>> Path('setup.py').exists()
True
>>> Path('/etc').exists()
True
>>> Path('nonexistentfile').exists()
False

```

Changed in version 3.12: The _follow_symlinks_ parameter was added.

Path.is_file(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "Link to this definition")

Return `True` if the path points to a regular file. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a regular file. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.
This method normally follows symlinks; to exclude symlinks, add the argument `follow_symlinks=False`.
Changed in version 3.13: The _follow_symlinks_ parameter was added.

Path.is_dir(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "Link to this definition")

Return `True` if the path points to a directory. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a directory. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.
This method normally follows symlinks; to exclude symlinks to directories, add the argument `follow_symlinks=False`.
Changed in version 3.13: The _follow_symlinks_ parameter was added.

Path.is_symlink()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink "Link to this definition")

Return `True` if the path points to a symbolic link, even if that symlink is broken. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a symbolic link. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.

Path.is_junction()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_junction "Link to this definition")

Return `True` if the path points to a junction, and `False` for any other type of file. Currently only Windows supports junctions.
Added in version 3.12.

Path.is_mount()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_mount "Link to this definition")

Return `True` if the path is a _mount point_ : a point in a file system where a different file system has been mounted. On POSIX, the function checks whether _path_ ’s parent, `path/..`, is on a different device than _path_ , or whether `path/..` and _path_ point to the same i-node on the same device — this should detect mount points for all Unix and POSIX variants. On Windows, a mount point is considered to be a drive letter root (e.g. `c:\`), a UNC share (e.g. `\\server\share`), or a mounted filesystem directory.
Added in version 3.7.
Changed in version 3.12: Windows support was added.

Path.is_socket()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_socket "Link to this definition")

Return `True` if the path points to a Unix socket. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a Unix socket. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.

Path.is_fifo()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_fifo "Link to this definition")

Return `True` if the path points to a FIFO. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a FIFO. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.

Path.is_block_device()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_block_device "Link to this definition")

Return `True` if the path points to a block device. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a block device. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.

Path.is_char_device()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_char_device "Link to this definition")

Return `True` if the path points to a character device. `False` will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a character device. Use [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") to distinguish between these cases.

Path.samefile(_other_path_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.samefile "Link to this definition")

Return whether this path points to the same file as _other_path_ , which can be either a Path object, or a string. The semantics are similar to [`os.path.samefile()`](https://docs.python.org/3/library/os.path.html#os.path.samefile "os.path.samefile") and [`os.path.samestat()`](https://docs.python.org/3/library/os.path.html#os.path.samestat "os.path.samestat").
An [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") can be raised if either file cannot be accessed for some reason.
Copy```
>>> p = Path('spam')
>>> q = Path('eggs')
>>> p.samefile(q)
False
>>> p.samefile('spam')
True

```

Added in version 3.5.

Path.info[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.info "Link to this definition")

A [`PathInfo`](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo "pathlib.types.PathInfo") object that supports querying file type information. The object exposes methods that cache their results, which can help reduce the number of system calls needed when switching on file type. For example:
Copy```
>>> p = Path('src')
>>> if p.info.is_symlink():
...     print('symlink')
... elif p.info.is_dir():
...     print('directory')
... elif p.info.exists():
...     print('something else')
... else:
...     print('not found')
...
directory

```

If the path was generated from [`Path.iterdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir "pathlib.Path.iterdir") then this attribute is initialized with some information about the file type gleaned from scanning the parent directory. Merely accessing `Path.info` does not perform any filesystem queries.
To fetch up-to-date information, it’s best to call [`Path.is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "pathlib.Path.is_dir"), [`is_file()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "pathlib.Path.is_file") and [`is_symlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink "pathlib.Path.is_symlink") rather than methods of this attribute. There is no way to reset the cache; instead you can create a new path object with an empty info cache via `p = Path(p)`.
Added in version 3.14.
### Reading and writing files[¶](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files "Link to this heading")

Path.open(_mode ='r'_, _buffering =-1_, _encoding =None_, _errors =None_, _newline =None_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open "Link to this definition")

Open the file pointed to by the path, like the built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open") function does:
Copy```
>>> p = Path('setup.py')
>>> with p.open() as f:
...     f.readline()
...
'#!/usr/bin/env python3\n'

```


Path.read_text(_encoding =None_, _errors =None_, _newline =None_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text "Link to this definition")

Return the decoded contents of the pointed-to file as a string:
Copy```
>>> p = Path('my_text_file')
>>> p.write_text('Text file contents')
18
>>> p.read_text()
'Text file contents'

```

The file is opened and then closed. The optional parameters have the same meaning as in [`open()`](https://docs.python.org/3/library/functions.html#open "open").
Added in version 3.5.
Changed in version 3.13: The _newline_ parameter was added.

Path.read_bytes()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes "Link to this definition")

Return the binary contents of the pointed-to file as a bytes object:
Copy```
>>> p = Path('my_binary_file')
>>> p.write_bytes(b'Binary file contents')
20
>>> p.read_bytes()
b'Binary file contents'

```

Added in version 3.5.

Path.write_text(_data_ , _encoding =None_, _errors =None_, _newline =None_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text "Link to this definition")

Open the file pointed to in text mode, write _data_ to it, and close the file:
Copy```
>>> p = Path('my_text_file')
>>> p.write_text('Text file contents')
18
>>> p.read_text()
'Text file contents'

```

An existing file of the same name is overwritten. The optional parameters have the same meaning as in [`open()`](https://docs.python.org/3/library/functions.html#open "open").
Added in version 3.5.
Changed in version 3.10: The _newline_ parameter was added.

Path.write_bytes(_data_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes "Link to this definition")

Open the file pointed to in bytes mode, write _data_ to it, and close the file:
Copy```
>>> p = Path('my_binary_file')
>>> p.write_bytes(b'Binary file contents')
20
>>> p.read_bytes()
b'Binary file contents'

```

An existing file of the same name is overwritten.
Added in version 3.5.
### Reading directories[¶](https://docs.python.org/3/library/pathlib.html#reading-directories "Link to this heading")

Path.iterdir()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir "Link to this definition")

When the path points to a directory, yield path objects of the directory contents:
Copy```
>>> p = Path('docs')
>>> for child in p.iterdir(): child
...
PosixPath('docs/conf.py')
PosixPath('docs/_templates')
PosixPath('docs/make.bat')
PosixPath('docs/index.rst')
PosixPath('docs/_build')
PosixPath('docs/_static')
PosixPath('docs/Makefile')

```

The children are yielded in arbitrary order, and the special entries `'.'` and `'..'` are not included. If a file is removed from or added to the directory after creating the iterator, it is unspecified whether a path object for that file is included.
If the path is not a directory or otherwise inaccessible, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.

Path.glob(_pattern_ , _*_ , _case_sensitive =None_, _recurse_symlinks =False_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "Link to this definition")

Glob the given relative _pattern_ in the directory represented by this path, yielding all matching files (of any kind):
Copy```
>>> sorted(Path('.').glob('*.py'))
[PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]
>>> sorted(Path('.').glob('*/*.py'))
[PosixPath('docs/conf.py')]
>>> sorted(Path('.').glob('**/*.py'))
[PosixPath('build/lib/pathlib.py'),
