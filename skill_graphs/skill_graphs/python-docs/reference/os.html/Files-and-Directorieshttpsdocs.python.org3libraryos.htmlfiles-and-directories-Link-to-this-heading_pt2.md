On some systems, _mode_ is ignored. Where it is used, the current umask value is first masked out. If bits other than the last 9 (i.e. the last 3 digits of the octal representation of the _mode_) are set, their meaning is platform-dependent. On some platforms, they are ignored and you should call [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod") explicitly to set them.
On Windows, a _mode_ of `0o700` is specifically handled to apply access control to the new directory such that only the current user and administrators have access. Other values of _mode_ are ignored.
This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
It is also possible to create temporary directories; see the [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories.") module’s [`tempfile.mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp") function.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.mkdir` with arguments `path`, `mode`, `dir_fd`.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.13: Windows now handles a _mode_ of `0o700`.

os.makedirs(_name_ , _mode =0o777_, _exist_ok =False_)[¶](https://docs.python.org/3/library/os.html#os.makedirs "Link to this definition")

Recursive directory creation function. Like [`mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir"), but makes all intermediate-level directories needed to contain the leaf directory.
The _mode_ parameter is passed to [`mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir") for creating the leaf directory; see [the mkdir() description](https://docs.python.org/3/library/os.html#mkdir-modebits) for how it is interpreted. To set the file permission bits of any newly created parent directories you can set the umask before invoking `makedirs()`. The file permission bits of existing parent directories are not changed.
If _exist_ok_ is `False` (the default), a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is raised if the target directory already exists.
Note
`makedirs()` will become confused if the path elements to create include [`pardir`](https://docs.python.org/3/library/os.html#os.pardir "os.pardir") (eg. “..” on UNIX systems).
This function handles UNC paths correctly.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.mkdir` with arguments `path`, `mode`, `dir_fd`.
Changed in version 3.2: Added the _exist_ok_ parameter.
Changed in version 3.4.1: Before Python 3.4.1, if _exist_ok_ was `True` and the directory existed, `makedirs()` would still raise an error if _mode_ did not match the mode of the existing directory. Since this behavior was impossible to implement safely, it was removed in Python 3.4.1. See [bpo-21082](https://bugs.python.org/issue?@action=redirect&bpo=21082).
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.7: The _mode_ argument no longer affects the file permission bits of newly created intermediate-level directories.

os.mkfifo(_path_ , _mode =0o666_, _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.mkfifo "Link to this definition")

Create a FIFO (a named pipe) named _path_ with numeric mode _mode_. The current umask value is first masked out from the mode.
This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
FIFOs are pipes that can be accessed like regular files. FIFOs exist until they are deleted (for example with [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink")). Generally, FIFOs are used as rendezvous between “client” and “server” type processes: the server opens the FIFO for reading, and the client opens it for writing. Note that `mkfifo()` doesn’t open the FIFO — it just creates the rendezvous point.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.mknod(_path_ , _mode =0o600_, _device =0_, _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.mknod "Link to this definition")

Create a filesystem node (file, device special file or named pipe) named _path_. _mode_ specifies both the permissions to use and the type of node to be created, being combined (bitwise OR) with one of `stat.S_IFREG`, `stat.S_IFCHR`, `stat.S_IFBLK`, and `stat.S_IFIFO` (those constants are available in [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat\(\), os.lstat\(\) and os.fstat\(\).")). For `stat.S_IFCHR` and `stat.S_IFBLK`, _device_ defines the newly created device special file (probably using [`os.makedev()`](https://docs.python.org/3/library/os.html#os.makedev "os.makedev")), otherwise it is ignored.
This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.major(_device_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.major "Link to this definition")

Extract the device major number from a raw device number (usually the `st_dev` or `st_rdev` field from `stat`).

os.minor(_device_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.minor "Link to this definition")

Extract the device minor number from a raw device number (usually the `st_dev` or `st_rdev` field from `stat`).

os.makedev(_major_ , _minor_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.makedev "Link to this definition")

Compose a raw device number from the major and minor device numbers.

os.pathconf(_path_ , _name_)[¶](https://docs.python.org/3/library/os.html#os.pathconf "Link to this definition")

Return system configuration information relevant to a named file. _name_ specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `pathconf_names` dictionary. For configuration variables not included in that mapping, passing an integer for _name_ is also accepted.
If _name_ is a string and is not known, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. If a specific value for _name_ is not supported by the host system, even if it is included in `pathconf_names`, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised with [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL") for the error number.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.pathconf_names[¶](https://docs.python.org/3/library/os.html#os.pathconf_names "Link to this definition")

Dictionary mapping names accepted by [`pathconf()`](https://docs.python.org/3/library/os.html#os.pathconf "os.pathconf") and [`fpathconf()`](https://docs.python.org/3/library/os.html#os.fpathconf "os.fpathconf") to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.readlink(_path_ , _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.readlink "Link to this definition")

Return a string representing the path to which the symbolic link points. The result may be either an absolute or relative pathname; if it is relative, it may be converted to an absolute pathname using `os.path.join(os.path.dirname(path), result)`.
If the _path_ is a string object (directly or indirectly through a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface), the result will also be a string object, and the call may raise a UnicodeDecodeError. If the _path_ is a bytes object (direct or indirectly), the result will be a bytes object.
This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
When trying to resolve a path that may contain links, use [`realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath") to properly handle recursion and platform differences.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.2: Added support for Windows 6.0 (Vista) symbolic links.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) on Unix.
Changed in version 3.8: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) and a bytes object on Windows.
Added support for directory junctions, and changed to return the substitution path (which typically includes `\\?\` prefix) rather than the optional “print name” field that was previously returned.

os.remove(_path_ , _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.remove "Link to this definition")

Remove (delete) the file _path_. If _path_ is a directory, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised. Use [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") to remove directories. If the file does not exist, a [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is raised.
This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
On Windows, attempting to remove a file that is in use causes an exception to be raised; on Unix, the directory entry is removed but the storage allocated to the file is not made available until the original file is no longer in use.
This function is semantically identical to [`unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.remove` with arguments `path`, `dir_fd`.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.removedirs(_name_)[¶](https://docs.python.org/3/library/os.html#os.removedirs "Link to this definition")

Remove directories recursively. Works like [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") except that, if the leaf directory is successfully removed, `removedirs()` tries to successively remove every parent directory mentioned in _path_ until an error is raised (which is ignored, because it generally means that a parent directory is not empty). For example, `os.removedirs('foo/bar/baz')` will first remove the directory `'foo/bar/baz'`, and then remove `'foo/bar'` and `'foo'` if they are empty. Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the leaf directory could not be successfully removed.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.remove` with arguments `path`, `dir_fd`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.rename(_src_ , _dst_ , _*_ , _src_dir_fd =None_, _dst_dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.rename "Link to this definition")

Rename the file or directory _src_ to _dst_. If _dst_ exists, the operation will fail with an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") subclass in a number of cases:
On Windows, if _dst_ exists a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is always raised. The operation may fail if _src_ and _dst_ are on different filesystems. Use [`shutil.move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move") to support moves to a different filesystem.
On Unix, if _src_ is a file and _dst_ is a directory or vice-versa, an [`IsADirectoryError`](https://docs.python.org/3/library/exceptions.html#IsADirectoryError "IsADirectoryError") or a [`NotADirectoryError`](https://docs.python.org/3/library/exceptions.html#NotADirectoryError "NotADirectoryError") will be raised respectively. If both are directories and _dst_ is empty, _dst_ will be silently replaced. If _dst_ is a non-empty directory, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised. If both are files, _dst_ will be replaced silently if the user has permission. The operation may fail on some Unix flavors if _src_ and _dst_ are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).
This function can support specifying _src_dir_fd_ and/or _dst_dir_fd_ to supply [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
If you want cross-platform overwriting of the destination, use [`replace()`](https://docs.python.org/3/library/os.html#os.replace "os.replace").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.
Changed in version 3.3: Added the _src_dir_fd_ and _dst_dir_fd_ parameters.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _src_ and _dst_.

os.renames(_old_ , _new_)[¶](https://docs.python.org/3/library/os.html#os.renames "Link to this definition")

Recursive directory or file renaming function. Works like [`rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename"), except creation of any intermediate directories needed to make the new pathname good is attempted first. After the rename, directories corresponding to rightmost path segments of the old name will be pruned away using [`removedirs()`](https://docs.python.org/3/library/os.html#os.removedirs "os.removedirs").
Note
This function can fail with the new directory structure made if you lack permissions needed to remove the leaf directory or file.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _old_ and _new_.

os.replace(_src_ , _dst_ , _*_ , _src_dir_fd =None_, _dst_dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.replace "Link to this definition")

Rename the file or directory _src_ to _dst_. If _dst_ is a non-empty directory, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised. If _dst_ exists and is a file, it will be replaced silently if the user has permission. The operation may fail if _src_ and _dst_ are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).
This function can support specifying _src_dir_fd_ and/or _dst_dir_fd_ to supply [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.
Added in version 3.3.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _src_ and _dst_.

os.rmdir(_path_ , _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.rmdir "Link to this definition")

Remove (delete) the directory _path_. If the directory does not exist or is not empty, a [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") or an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised respectively. In order to remove whole directory trees, [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree") can be used.
This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.rmdir` with arguments `path`, `dir_fd`.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.scandir(_path ='.'_)[¶](https://docs.python.org/3/library/os.html#os.scandir "Link to this definition")

Return an iterator of [`os.DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry") objects corresponding to the entries in the directory given by _path_. The entries are yielded in arbitrary order, and the special entries `'.'` and `'..'` are not included. If a file is removed from or added to the directory after creating the iterator, whether an entry for that file be included is unspecified.
Using `scandir()` instead of [`listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir") can significantly increase the performance of code that also needs file type or file attribute information, because [`os.DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry") objects expose this information if the operating system provides it when scanning a directory. All `os.DirEntry` methods may perform a system call, but [`is_dir()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_dir "os.DirEntry.is_dir") and [`is_file()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_file "os.DirEntry.is_file") usually only require a system call for symbolic links; [`os.DirEntry.stat()`](https://docs.python.org/3/library/os.html#os.DirEntry.stat "os.DirEntry.stat") always requires a system call on Unix but only requires one for symbolic links on Windows.
_path_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). If _path_ is of type `bytes` (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface), the type of the [`name`](https://docs.python.org/3/library/os.html#os.DirEntry.name "os.DirEntry.name") and [`path`](https://docs.python.org/3/library/os.html#os.DirEntry.path "os.DirEntry.path") attributes of each [`os.DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry") will be `bytes`; in all other circumstances, they will be of type `str`.
This function can also support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd); the file descriptor must refer to a directory.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.scandir` with argument `path`.
The `scandir()` iterator supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol and has the following method:

scandir.close()[¶](https://docs.python.org/3/library/os.html#os.scandir.close "Link to this definition")

Close the iterator and free acquired resources.
This is called automatically when the iterator is exhausted or garbage collected, or when an error happens during iterating. However it is advisable to call it explicitly or use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement.
Added in version 3.6.
The following example shows a simple use of `scandir()` to display all the files (excluding directories) in the given _path_ that don’t start with `'.'`. The `entry.is_file()` call will generally not make an additional system call:
Copy```
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

```

Note
On Unix-based systems, `scandir()` uses the system’s
Added in version 3.5.
Changed in version 3.6: Added support for the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol and the [`close()`](https://docs.python.org/3/library/os.html#os.scandir.close "os.scandir.close") method. If a `scandir()` iterator is neither exhausted nor explicitly closed a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") will be emitted in its destructor.
The function accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.7: Added support for [file descriptors](https://docs.python.org/3/library/os.html#path-fd) on Unix.

_class_ os.DirEntry[¶](https://docs.python.org/3/library/os.html#os.DirEntry "Link to this definition")

Object yielded by [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") to expose the file path and other file attributes of a directory entry.
[`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") will provide as much of this information as possible without making additional system calls. When a `stat()` or `lstat()` system call is made, the `os.DirEntry` object will cache the result.
`os.DirEntry` instances are not intended to be stored in long-lived data structures; if you know the file metadata has changed or if a long time has elapsed since calling [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir"), call `os.stat(entry.path)` to fetch up-to-date information.
Because the `os.DirEntry` methods can make operating system calls, they may also raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). If you need very fine-grained control over errors, you can catch `OSError` when calling one of the `os.DirEntry` methods and handle as appropriate.
To be directly usable as a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object), `os.DirEntry` implements the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface.
Attributes and methods on a `os.DirEntry` instance are as follows:

name[¶](https://docs.python.org/3/library/os.html#os.DirEntry.name "Link to this definition")

The entry’s base filename, relative to the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") _path_ argument.
The [`name`](https://docs.python.org/3/library/os.html#os.name "os.name") attribute will be `bytes` if the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") _path_ argument is of type `bytes` and `str` otherwise. Use [`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode") to decode byte filenames.

path[¶](https://docs.python.org/3/library/os.html#os.DirEntry.path "Link to this definition")

The entry’s full path name: equivalent to `os.path.join(scandir_path, entry.name)` where _scandir_path_ is the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") _path_ argument. The path is only absolute if the `scandir()` _path_ argument was absolute. If the `scandir()` _path_ argument was a [file descriptor](https://docs.python.org/3/library/os.html#path-fd), the [`path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") attribute is the same as the [`name`](https://docs.python.org/3/library/os.html#os.name "os.name") attribute.
The [`path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") attribute will be `bytes` if the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") _path_ argument is of type `bytes` and `str` otherwise. Use [`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode") to decode byte filenames.

inode()[¶](https://docs.python.org/3/library/os.html#os.DirEntry.inode "Link to this definition")

Return the inode number of the entry.
The result is cached on the `os.DirEntry` object. Use `os.stat(entry.path, follow_symlinks=False).st_ino` to fetch up-to-date information.
On the first, uncached call, a system call is required on Windows but not on Unix.

is_dir(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_dir "Link to this definition")

Return `True` if this entry is a directory or a symbolic link pointing to a directory; return `False` if the entry is or points to any other kind of file, or if it doesn’t exist anymore.
