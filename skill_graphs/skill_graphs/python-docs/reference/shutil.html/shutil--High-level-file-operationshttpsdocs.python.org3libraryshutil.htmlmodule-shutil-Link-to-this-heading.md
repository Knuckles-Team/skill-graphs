#  `shutil` — High-level file operations[¶](https://docs.python.org/3/library/shutil.html#module-shutil "Link to this heading")
**Source code:**
* * *
The `shutil` module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module.
Warning
Even the higher-level file copying functions ([`shutil.copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy"), [`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2")) cannot copy all file metadata.
On POSIX platforms, this means that file owner and group are lost as well as ACLs. On Mac OS, the resource fork and other metadata are not used. This means that resources will be lost and file type and creator codes will not be correct. On Windows, file owners, ACLs and alternate data streams are not copied.
## Directory and files operations[¶](https://docs.python.org/3/library/shutil.html#directory-and-files-operations "Link to this heading")

shutil.copyfileobj(_fsrc_ , _fdst_[, _length_])[¶](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "Link to this definition")

Copy the contents of the [file-like object](https://docs.python.org/3/glossary.html#term-file-object) _fsrc_ to the file-like object _fdst_. The integer _length_ , if given, is the buffer size. In particular, a negative _length_ value means to copy the data without looping over the source data in chunks; by default the data is read in chunks to avoid uncontrolled memory consumption. Note that if the current file position of the _fsrc_ object is not 0, only the contents from the current file position to the end of the file will be copied.
`copyfileobj()` will _not_ guarantee that the destination stream has been flushed on completion of the copy. If you want to read from the destination at the completion of the copy operation (for example, reading the contents of a temporary file that has been copied from a HTTP stream), you must ensure that you have called [`flush()`](https://docs.python.org/3/library/io.html#io.IOBase.flush "io.IOBase.flush") or [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") on the file-like object before attempting to read the destination file.

shutil.copyfile(_src_ , _dst_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/shutil.html#shutil.copyfile "Link to this definition")

Copy the contents (no metadata) of the file named _src_ to a file named _dst_ and return _dst_ in the most efficient way possible. _src_ and _dst_ are [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object) or path names given as strings.
_dst_ must be the complete target file name; look at [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") for a copy that accepts a target directory path. If _src_ and _dst_ specify the same file, [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError") is raised.
The destination location must be writable; otherwise, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception will be raised. If _dst_ already exists, it will be replaced. Special files such as character or block devices and pipes cannot be copied with this function.
If _follow_symlinks_ is false and _src_ is a symbolic link, a new symbolic link will be created instead of copying the file _src_ points to.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.
Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised instead of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). Added _follow_symlinks_ argument. Now returns _dst_.
Changed in version 3.4: Raise [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError") instead of [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error"). Since the former is a subclass of the latter, this change is backward compatible.
Changed in version 3.8: Platform-specific fast-copy syscalls may be used internally in order to copy the file more efficiently. See [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section.

_exception_ shutil.SpecialFileError[¶](https://docs.python.org/3/library/shutil.html#shutil.SpecialFileError "Link to this definition")

This exception is raised when [`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") or [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree") attempt to copy a named pipe.
Added in version 2.7.

_exception_ shutil.SameFileError[¶](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "Link to this definition")

This exception is raised if source and destination in [`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") are the same file.
Added in version 3.4.

shutil.copymode(_src_ , _dst_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/shutil.html#shutil.copymode "Link to this definition")

Copy the permission bits from _src_ to _dst_. The file contents, owner, and group are unaffected. _src_ and _dst_ are [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object) or path names given as strings. If _follow_symlinks_ is false, and both _src_ and _dst_ are symbolic links, `copymode()` will attempt to modify the mode of _dst_ itself (rather than the file it points to). This functionality is not available on every platform; please see [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") for more information. If `copymode()` cannot modify symbolic links on the local platform, and it is asked to do so, it will do nothing and return.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copymode` with arguments `src`, `dst`.
Changed in version 3.3: Added _follow_symlinks_ argument.

shutil.copystat(_src_ , _dst_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/shutil.html#shutil.copystat "Link to this definition")

Copy the permission bits, last access time, last modification time, and flags from _src_ to _dst_. On Linux, `copystat()` also copies the “extended attributes” where possible. The file contents, owner, and group are unaffected. _src_ and _dst_ are [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object) or path names given as strings.
If _follow_symlinks_ is false, and _src_ and _dst_ both refer to symbolic links, `copystat()` will operate on the symbolic links themselves rather than the files the symbolic links refer to—reading the information from the _src_ symbolic link, and writing the information to the _dst_ symbolic link.
Note
Not all platforms provide the ability to examine and modify symbolic links. Python itself can tell you what functionality is locally available.
  * If `os.chmod in os.supports_follow_symlinks` is `True`, `copystat()` can modify the permission bits of a symbolic link.
  * If `os.utime in os.supports_follow_symlinks` is `True`, `copystat()` can modify the last access and modification times of a symbolic link.
  * If `os.chflags in os.supports_follow_symlinks` is `True`, `copystat()` can modify the flags of a symbolic link. (`os.chflags` is not available on all platforms.)


On platforms where some or all of this functionality is unavailable, when asked to modify a symbolic link, `copystat()` will copy everything it can. `copystat()` never returns failure.
Please see [`os.supports_follow_symlinks`](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "os.supports_follow_symlinks") for more information.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copystat` with arguments `src`, `dst`.
Changed in version 3.3: Added _follow_symlinks_ argument and support for Linux extended attributes.

shutil.copy(_src_ , _dst_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/shutil.html#shutil.copy "Link to this definition")

Copies the file _src_ to the file or directory _dst_. _src_ and _dst_ should be [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object) or strings. If _dst_ specifies a directory, the file will be copied into _dst_ using the base filename from _src_. If _dst_ specifies a file that already exists, it will be replaced. Returns the path to the newly created file.
If _follow_symlinks_ is false, and _src_ is a symbolic link, _dst_ will be created as a symbolic link. If _follow_symlinks_ is true and _src_ is a symbolic link, _dst_ will be a copy of the file _src_ refers to.
[`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") copies the file data and the file’s permission mode (see [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")). Other metadata, like the file’s creation and modification times, is not preserved. To preserve all file metadata from the original, use [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") instead.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copymode` with arguments `src`, `dst`.
Changed in version 3.3: Added _follow_symlinks_ argument. Now returns path to the newly created file.
Changed in version 3.8: Platform-specific fast-copy syscalls may be used internally in order to copy the file more efficiently. See [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section.

shutil.copy2(_src_ , _dst_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/shutil.html#shutil.copy2 "Link to this definition")

Identical to [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") except that `copy2()` also attempts to preserve file metadata.
When _follow_symlinks_ is false, and _src_ is a symbolic link, `copy2()` attempts to copy all metadata from the _src_ symbolic link to the newly created _dst_ symbolic link. However, this functionality is not available on all platforms. On platforms where some or all of this functionality is unavailable, `copy2()` will preserve all the metadata it can; `copy2()` never raises an exception because it cannot preserve file metadata.
`copy2()` uses [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") to copy the file metadata. Please see `copystat()` for more information about platform support for modifying symbolic link metadata.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copystat` with arguments `src`, `dst`.
Changed in version 3.3: Added _follow_symlinks_ argument, try to copy extended file system attributes too (currently Linux only). Now returns path to the newly created file.
Changed in version 3.8: Platform-specific fast-copy syscalls may be used internally in order to copy the file more efficiently. See [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section.

shutil.ignore_patterns(_* patterns_)[¶](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "Link to this definition")

This factory function creates a function that can be used as a callable for [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree")'s _ignore_ argument, ignoring files and directories that match one of the glob-style _patterns_ provided. See the example below.

shutil.copytree(_src_ , _dst_ , _symlinks =False_, _ignore =None_, _copy_function =copy2_, _ignore_dangling_symlinks =False_, _dirs_exist_ok =False_)[¶](https://docs.python.org/3/library/shutil.html#shutil.copytree "Link to this definition")

Recursively copy an entire directory tree rooted at _src_ to a directory named _dst_ and return the destination directory. All intermediate directories needed to contain _dst_ will also be created by default.
Permissions and times of directories are copied with [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat"), individual files are copied using [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2").
If _symlinks_ is true, symbolic links in the source tree are represented as symbolic links in the new tree and the metadata of the original links will be copied as far as the platform allows; if false or omitted, the contents and metadata of the linked files are copied to the new tree.
When _symlinks_ is false, if the file pointed to by the symlink doesn’t exist, an exception will be added in the list of errors raised in an [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error") exception at the end of the copy process. You can set the optional _ignore_dangling_symlinks_ flag to true if you want to silence this exception. Notice that this option has no effect on platforms that don’t support [`os.symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink").
If _ignore_ is given, it must be a callable that will receive as its arguments the directory being visited by `copytree()`, and a list of its contents, as returned by [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir"). Since `copytree()` is called recursively, the _ignore_ callable will be called once for each directory that is copied. The callable must return a sequence of directory and file names relative to the current directory (i.e. a subset of the items in its second argument); these names will then be ignored in the copy process. [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "shutil.ignore_patterns") can be used to create such a callable that ignores names based on glob-style patterns.
If exception(s) occur, an [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error") is raised with a list of reasons.
If _copy_function_ is given, it must be a callable that will be used to copy each file. It will be called with the source path and the destination path as arguments. By default, [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") is used, but any function that supports the same signature (like [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy")) can be used.
If _dirs_exist_ok_ is false (the default) and _dst_ already exists, a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is raised. If _dirs_exist_ok_ is true, the copying operation will continue if it encounters existing directories, and files within the _dst_ tree will be overwritten by corresponding files from the _src_ tree.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copytree` with arguments `src`, `dst`.
Changed in version 3.2: Added the _copy_function_ argument to be able to provide a custom copy function. Added the _ignore_dangling_symlinks_ argument to silence dangling symlinks errors when _symlinks_ is false.
Changed in version 3.3: Copy metadata when _symlinks_ is false. Now returns _dst_.
Changed in version 3.8: Platform-specific fast-copy syscalls may be used internally in order to copy the file more efficiently. See [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section.
Changed in version 3.8: Added the _dirs_exist_ok_ parameter.

shutil.rmtree(_path_ , _ignore_errors =False_, _onerror =None_, _*_ , _onexc =None_, _dir_fd =None_)[¶](https://docs.python.org/3/library/shutil.html#shutil.rmtree "Link to this definition")

Delete an entire directory tree; _path_ must point to a directory (but not a symbolic link to a directory). If _ignore_errors_ is true, errors resulting from failed removals will be ignored; if false or omitted, such errors are handled by calling a handler specified by _onexc_ or _onerror_ or, if both are omitted, exceptions are propagated to the caller.
This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
Note
On platforms that support the necessary fd-based functions a symlink attack resistant version of `rmtree()` is used by default. On other platforms, the `rmtree()` implementation is susceptible to a symlink attack: given proper timing and circumstances, attackers can manipulate symlinks on the filesystem to delete files they wouldn’t be able to access otherwise. Applications can use the [`rmtree.avoids_symlink_attacks`](https://docs.python.org/3/library/shutil.html#shutil.rmtree.avoids_symlink_attacks "shutil.rmtree.avoids_symlink_attacks") function attribute to determine which case applies.
If _onexc_ is provided, it must be a callable that accepts three parameters: _function_ , _path_ , and _excinfo_.
The first parameter, _function_ , is the function which raised the exception; it depends on the platform and implementation. The second parameter, _path_ , will be the path name passed to _function_. The third parameter, _excinfo_ , is the exception that was raised. Exceptions raised by _onexc_ will not be caught.
The deprecated _onerror_ is similar to _onexc_ , except that the third parameter it receives is the tuple returned from [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info").
See also
[rmtree example](https://docs.python.org/3/library/shutil.html#shutil-rmtree-example) for an example of handling the removal of a directory tree that contains read-only files.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.rmtree` with arguments `path`, `dir_fd`.
Changed in version 3.3: Added a symlink attack resistant version that is used automatically if platform supports fd-based functions.
Changed in version 3.8: On Windows, will no longer delete the contents of a directory junction before removing the junction.
Changed in version 3.11: Added the _dir_fd_ parameter.
Changed in version 3.12: Added the _onexc_ parameter, deprecated _onerror_.
Changed in version 3.13: `rmtree()` now ignores [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") exceptions for all but the top-level path. Exceptions other than [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") and subclasses of `OSError` are now always propagated to the caller.

rmtree.avoids_symlink_attacks[¶](https://docs.python.org/3/library/shutil.html#shutil.rmtree.avoids_symlink_attacks "Link to this definition")

Indicates whether the current platform and implementation provides a symlink attack resistant version of `rmtree()`. Currently this is only true for platforms supporting fd-based directory access functions.
Added in version 3.3.

shutil.move(_src_ , _dst_ , _copy_function =copy2_)[¶](https://docs.python.org/3/library/shutil.html#shutil.move "Link to this definition")

Recursively move a file or directory (_src_) to another location and return the destination.
If _dst_ is an existing directory or a symlink to a directory, then _src_ is moved inside that directory. The destination path in that directory must not already exist.
If _dst_ already exists but is not a directory, it may be overwritten depending on [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename") semantics.
If the destination is on the current filesystem, then [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename") is used. Otherwise, _src_ is copied to the destination using _copy_function_ and then removed. In case of symlinks, a new symlink pointing to the target of _src_ will be created as the destination and _src_ will be removed.
If _copy_function_ is given, it must be a callable that takes two arguments, _src_ and the destination, and will be used to copy _src_ to the destination if [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename") cannot be used. If the source is a directory, [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree") is called, passing it the _copy_function_. The default _copy_function_ is [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2"). Using [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") as the _copy_function_ allows the move to succeed when it is not possible to also copy the metadata, at the expense of not copying any of the metadata.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.move` with arguments `src`, `dst`.
Changed in version 3.3: Added explicit symlink handling for foreign filesystems, thus adapting it to the behavior of GNU’s **mv**. Now returns _dst_.
Changed in version 3.5: Added the _copy_function_ keyword argument.
Changed in version 3.8: Platform-specific fast-copy syscalls may be used internally in order to copy the file more efficiently. See [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations) section.
Changed in version 3.9: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for both _src_ and _dst_.

shutil.disk_usage(_path_)[¶](https://docs.python.org/3/library/shutil.html#shutil.disk_usage "Link to this definition")

Return disk usage statistics about the given path as a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) with the attributes _total_ , _used_ and _free_ , which are the amount of total, used and free space, in bytes. _path_ may be a file or a directory.
Note
On Unix filesystems, _path_ must point to a path within a **mounted** filesystem partition. On those platforms, CPython doesn’t attempt to retrieve disk usage information from non-mounted filesystems.
Added in version 3.3.
Changed in version 3.8: On Windows, _path_ can now be a file or directory.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

shutil.chown(_path_ , _user =None_, _group =None_, _*_ , _dir_fd =None_, _follow_symlinks =True_)[¶](https://docs.python.org/3/library/shutil.html#shutil.chown "Link to this definition")

Change owner _user_ and/or _group_ of the given _path_.
_user_ can be a system user name or a uid; the same applies to _group_. At least one argument is required.
See also [`os.chown()`](https://docs.python.org/3/library/os.html#os.chown "os.chown"), the underlying function.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.chown` with arguments `path`, `user`, `group`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.
Changed in version 3.13: Added _dir_fd_ and _follow_symlinks_ parameters.

shutil.which(_cmd_ , _mode =os.F_OK | os.X_OK_, _path =None_)[¶](https://docs.python.org/3/library/shutil.html#shutil.which "Link to this definition")

Return the path to an executable which would be run if the given _cmd_ was called. If no _cmd_ would be called, return `None`.
_mode_ is a permission mask passed to [`os.access()`](https://docs.python.org/3/library/os.html#os.access "os.access"), by default determining if the file exists and is executable.
_path_ is a “`PATH` string” specifying the directories to look in, delimited by [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep"). When no _path_ is specified, the `PATH` environment variable is read from [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ"), falling back to [`os.defpath`](https://docs.python.org/3/library/os.html#os.defpath "os.defpath") if it is not set.
If _cmd_ contains a directory component, `which()` only checks the specified path directly and does not search the directories listed in _path_ or in the system’s `PATH` environment variable.
On Windows, the current directory is prepended to the _path_ if _mode_ does not include `os.X_OK`. When the _mode_ does include `os.X_OK`, the Windows API `NeedCurrentDirectoryForExePathW` will be consulted to determine if the current directory should be prepended to _path_. To avoid consulting the current working directory for executables: set the environment variable `NoDefaultCurrentDirectoryInExePath`.
Also on Windows, the `PATHEXT` environment variable is used to resolve commands that may not already include an extension. For example, if you call `shutil.which("python")`, `which()` will search `PATHEXT` to know that it should look for `python.exe` within the _path_ directories. For example, on Windows:
Copy```
>>> shutil.which("python")
'C:\\Python33\\python.EXE'

```

This is also applied when _cmd_ is a path that contains a directory component:
Copy```
>>> shutil.which("C:\\Python33\\python")
'C:\\Python33\\python.EXE'

```

Added in version 3.3.
Changed in version 3.8: The [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") type is now accepted. If _cmd_ type is `bytes`, the result type is also `bytes`.
Changed in version 3.12: On Windows, the current directory is no longer prepended to the search path if _mode_ includes `os.X_OK` and WinAPI `NeedCurrentDirectoryForExePathW(cmd)` is false, else the current directory is prepended even if it is already in the search path; `PATHEXT` is used now even when _cmd_ includes a directory component or ends with an extension that is in `PATHEXT`; and filenames that have no extension can now be found.

_exception_ shutil.Error[¶](https://docs.python.org/3/library/shutil.html#shutil.Error "Link to this definition")

This exception collects exceptions that are raised during a multi-file operation. For [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), the exception argument is a list of 3-tuples (_srcname_ , _dstname_ , _exception_).
### Platform-dependent efficient copy operations[¶](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations "Link to this heading")
Starting from Python 3.8, all functions involving a file copy ([`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile"), [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy"), [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2"), [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), and [`move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move")) may use platform-specific “fast-copy” syscalls in order to copy the file more efficiently (see [bpo-33671](https://bugs.python.org/issue?@action=redirect&bpo=33671)). “fast-copy” means that the copying operation occurs within the kernel, avoiding the use of userspace buffers in Python as in “`outfd.write(infd.read())`”.
On macOS
On Linux [`os.copy_file_range()`](https://docs.python.org/3/library/os.html#os.copy_file_range "os.copy_file_range") or [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") is used.
On Solaris [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") is used.
On Windows [`shutil.copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") uses a bigger default buffer size (1 MiB instead of 64 KiB) and a [`memoryview()`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview")-based variant of [`shutil.copyfileobj()`](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "shutil.copyfileobj") is used.
If the fast-copy operation fails and no data was written in the destination file then shutil will silently fall back to less efficient [`copyfileobj()`](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "shutil.copyfileobj") function internally.
Changed in version 3.8.
Changed in version 3.14: Solaris now uses [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile").
Changed in version 3.14: Copy-on-write or server-side copy may be used internally via [`os.copy_file_range()`](https://docs.python.org/3/library/os.html#os.copy_file_range "os.copy_file_range") on supported Linux filesystems.
### copytree example[¶](https://docs.python.org/3/library/shutil.html#copytree-example "Link to this heading")
An example that uses the [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "shutil.ignore_patterns") helper:
Copy```
from shutil import copytree, ignore_patterns

copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

```

This will copy everything except `.pyc` files and files or directories whose name starts with `tmp`.
Another example that uses the _ignore_ argument to add a logging call:
Copy```
from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

copytree(source, destination, ignore=_logpath)

```

### rmtree example[¶](https://docs.python.org/3/library/shutil.html#rmtree-example "Link to this heading")
This example shows how to remove a directory tree on Windows where some of the files have their read-only bit set. It uses the onexc callback to clear the readonly bit and reattempt the remove. Any subsequent failure will propagate.
Copy```
import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree(directory, onexc=remove_readonly)

```

## Archiving operations[¶](https://docs.python.org/3/library/shutil.html#archiving-operations "Link to this heading")
Added in version 3.2.
Changed in version 3.5: Added support for the _xztar_ format.
High-level utilities to create and read compressed and archived files are also provided. They rely on the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") and [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.") modules.

shutil.make_archive(_base_name_ , _format_[, _root_dir_[, _base_dir_[, _verbose_[, _dry_run_[, _owner_[, _group_[, _logger_]]]]]]])[¶](https://docs.python.org/3/library/shutil.html#shutil.make_archive "Link to this definition")

Create an archive file (such as zip or tar) and return its name.
_base_name_ is the name of the file to create, including the path, minus any format-specific extension.
_format_ is the archive format: one of “zip” (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available), “tar”, “gztar” (if the `zlib` module is available), “bztar” (if the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is available), “xztar” (if the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module is available), or “zstdtar” (if the [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") module is available).
_root_dir_ is a directory that will be the root directory of the archive, all paths in the archive will be relative to it; for example, we typically chdir into _root_dir_ before creating the archive.
_base_dir_ is the directory where we start archiving from; i.e. _base_dir_ will be the common prefix of all files and directories in the archive. _base_dir_ must be given relative to _root_dir_. See [Archiving example with base_dir](https://docs.python.org/3/library/shutil.html#shutil-archiving-example-with-basedir) for how to use _base_dir_ and _root_dir_ together.
_root_dir_ and _base_dir_ both default to the current directory.
If _dry_run_ is true, no archive is created, but the operations that would be executed are logged to _logger_.
_owner_ and _group_ are used when creating a tar archive. By default, uses the current owner and group.
_logger_ must be an object compatible with [**PEP 282**](https://peps.python.org/pep-0282/), usually an instance of [`logging.Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger").
The _verbose_ argument is unused and deprecated.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.make_archive` with arguments `base_name`, `format`, `root_dir`, `base_dir`.
Note
This function is not thread-safe when custom archivers registered with [`register_archive_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "shutil.register_archive_format") do not support the _root_dir_ argument. In this case it temporarily changes the current working directory of the process to _root_dir_ to perform archiving.
Changed in version 3.8: The modern pax (POSIX.1-2001) format is now used instead of the legacy GNU format for archives created with `format="tar"`.
Changed in version 3.10.6: This function is now made thread-safe during creation of standard `.zip` and tar archives.

shutil.get_archive_formats()[¶](https://docs.python.org/3/library/shutil.html#shutil.get_archive_formats "Link to this definition")

Return a list of supported formats for archiving. Each element of the returned sequence is a tuple `(name, description)`.
By default `shutil` provides these formats:
  * _zip_ : ZIP file (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available).
  * _tar_ : Uncompressed tar file. Uses POSIX.1-2001 pax format for new archives.
  * _gztar_ : gzip’ed tar-file (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available).
  * _bztar_ : bzip2’ed tar-file (if the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is available).
  * _xztar_ : xz’ed tar-file (if the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module is available).
  * _zstdtar_ : Zstandard compressed tar-file (if the [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") module is available).


You can register new formats or provide your own archiver for any existing formats, by using [`register_archive_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "shutil.register_archive_format").

shutil.register_archive_format(_name_ , _function_[, _extra_args_[, _description_]])[¶](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "Link to this definition")

Register an archiver for the format _name_.
_function_ is the callable that will be used to unpack archives. The callable will receive the _base_name_ of the file to create, followed by the _base_dir_ (which defaults to [`os.curdir`](https://docs.python.org/3/library/os.html#os.curdir "os.curdir")) to start archiving from. Further arguments are passed as keyword arguments: _owner_ , _group_ , _dry_run_ and _logger_ (as passed in [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive")).
If _function_ has the custom attribute `function.supports_root_dir` set to `True`, the _root_dir_ argument is passed as a keyword argument. Otherwise the current working directory of the process is temporarily changed to _root_dir_ before calling _function_. In this case [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive") is not thread-safe.
If given, _extra_args_ is a sequence of `(name, value)` pairs that will be used as extra keywords arguments when the archiver callable is used.
_description_ is used by [`get_archive_formats()`](https://docs.python.org/3/library/shutil.html#shutil.get_archive_formats "shutil.get_archive_formats") which returns the list of archivers. Defaults to an empty string.
Changed in version 3.12: Added support for functions supporting the _root_dir_ argument.

shutil.unregister_archive_format(_name_)[¶](https://docs.python.org/3/library/shutil.html#shutil.unregister_archive_format "Link to this definition")

Remove the archive format _name_ from the list of supported formats.

shutil.unpack_archive(_filename_[, _extract_dir_[, _format_[, _filter_]]])[¶](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "Link to this definition")

Unpack an archive. _filename_ is the full path of the archive.
_extract_dir_ is the name of the target directory where the archive is unpacked. If not provided, the current working directory is used.
_format_ is the archive format: one of “zip”, “tar”, “gztar”, “bztar”, “xztar”, or “zstdtar”. Or any other format registered with [`register_unpack_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_unpack_format "shutil.register_unpack_format"). If not provided, `unpack_archive()` will use the archive file name extension and see if an unpacker was registered for that extension. In case none is found, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
The keyword-only _filter_ argument is passed to the underlying unpacking function. For zip files, _filter_ is not accepted. For tar files, it is recommended to use `'data'` (default since Python 3.14), unless using features specific to tar and UNIX-like filesystems. (See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) for details.)
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `shutil.unpack_archive` with arguments `filename`, `extract_dir`, `format`.
Warning
Never extract archives from untrusted sources without prior inspection. It is possible that files are created outside of the path specified in the _extract_dir_ argument, e.g. members that have absolute filenames starting with “/” or filenames with two dots “..”.
Since Python 3.14, the defaults for both built-in formats (zip and tar files) will prevent the most dangerous of such security issues, but will not prevent _all_ unintended behavior. Read the [Hints for further verification](https://docs.python.org/3/library/tarfile.html#tarfile-further-verification) section for tar-specific details.
Changed in version 3.7: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _filename_ and _extract_dir_.
Changed in version 3.12: Added the _filter_ argument.

shutil.register_unpack_format(_name_ , _extensions_ , _function_[, _extra_args_[, _description_]])[¶](https://docs.python.org/3/library/shutil.html#shutil.register_unpack_format "Link to this definition")

Registers an unpack format. _name_ is the name of the format and _extensions_ is a list of extensions corresponding to the format, like `.zip` for Zip files.
_function_ is the callable that will be used to unpack archives. The callable will receive:
  * the path of the archive, as a positional argument;
  * the directory the archive must be extracted to, as a positional argument;
  * possibly a _filter_ keyword argument, if it was given to [`unpack_archive()`](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "shutil.unpack_archive");
  * additional keyword arguments, specified by _extra_args_ as a sequence of `(name, value)` tuples.


_description_ can be provided to describe the format, and will be returned by the [`get_unpack_formats()`](https://docs.python.org/3/library/shutil.html#shutil.get_unpack_formats "shutil.get_unpack_formats") function.

shutil.unregister_unpack_format(_name_)[¶](https://docs.python.org/3/library/shutil.html#shutil.unregister_unpack_format "Link to this definition")

Unregister an unpack format. _name_ is the name of the format.

shutil.get_unpack_formats()[¶](https://docs.python.org/3/library/shutil.html#shutil.get_unpack_formats "Link to this definition")

Return a list of all registered formats for unpacking. Each element of the returned sequence is a tuple `(name, extensions, description)`.
By default `shutil` provides these formats:
  * _zip_ : ZIP file (unpacking compressed files works only if the corresponding module is available).
  * _tar_ : uncompressed tar file.
  * _gztar_ : gzip’ed tar-file (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available).
  * _bztar_ : bzip2’ed tar-file (if the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is available).
  * _xztar_ : xz’ed tar-file (if the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module is available).
  * _zstdtar_ : Zstandard compressed tar-file (if the [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") module is available).


You can register new formats or provide your own unpacker for any existing formats, by using [`register_unpack_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_unpack_format "shutil.register_unpack_format").
### Archiving example[¶](https://docs.python.org/3/library/shutil.html#archiving-example "Link to this heading")
In this example, we create a gzip’ed tar-file archive containing all files found in the `.ssh` directory of the user:
Copy```
>>> from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
>>> make_archive(archive_name, 'gztar', root_dir)
'/Users/tarek/myarchive.tar.gz'

```

The resulting archive contains:
Copy```
$ tar -tzvf /Users/tarek/myarchive.tar.gz
drwx------ tarek/staff       0 2010-02-01 16:23:40 ./
-rw-r--r-- tarek/staff     609 2008-06-09 13:26:54 ./authorized_keys
-rwxr-xr-x tarek/staff      65 2008-06-09 13:26:54 ./config
-rwx------ tarek/staff     668 2008-06-09 13:26:54 ./id_dsa
-rwxr-xr-x tarek/staff     609 2008-06-09 13:26:54 ./id_dsa.pub
-rw------- tarek/staff    1675 2008-06-09 13:26:54 ./id_rsa
-rw-r--r-- tarek/staff     397 2008-06-09 13:26:54 ./id_rsa.pub
-rw-r--r-- tarek/staff   37192 2010-02-06 18:23:10 ./known_hosts

```

### Archiving example with _base_dir_[¶](https://docs.python.org/3/library/shutil.html#archiving-example-with-base-dir "Link to this heading")
In this example, similar to the [one above](https://docs.python.org/3/library/shutil.html#shutil-archiving-example), we show how to use [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive"), but this time with the usage of _base_dir_. We now have the following directory structure:
Copy```
$ tree tmp
tmp
└── root
    └── structure
        ├── content
            └── please_add.txt
        └── do_not_add.txt

```

In the final archive, `please_add.txt` should be included, but `do_not_add.txt` should not. Therefore we use the following:
Copy```
>>> from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> make_archive(
...     archive_name,
...     'tar',
...     root_dir='tmp/root',
...     base_dir='structure/content',
... )
'/Users/tarek/myarchive.tar'

```

Listing the files in the resulting archive gives us:
Copy```
$ python -m tarfile -l /Users/tarek/myarchive.tar
structure/content/
structure/content/please_add.txt

```

## Querying the size of the output terminal[¶](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal "Link to this heading")

shutil.get_terminal_size(_fallback =(columns, lines)_)[¶](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "Link to this definition")

Get the size of the terminal window.
For each of the two dimensions, the environment variable, `COLUMNS` and `LINES` respectively, is checked. If the variable is defined and the value is a positive integer, it is used.
When `COLUMNS` or `LINES` is not defined, which is the common case, the terminal connected to [`sys.__stdout__`](https://docs.python.org/3/library/sys.html#sys.__stdout__ "sys.__stdout__") is queried by invoking [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size").
If the terminal size cannot be successfully queried, either because the system doesn’t support querying, or because we are not connected to a terminal, the value given in `fallback` parameter is used. `fallback` defaults to `(80, 24)` which is the default size used by many terminal emulators.
The value returned is a named tuple of type [`os.terminal_size`](https://docs.python.org/3/library/os.html#os.terminal_size "os.terminal_size").
See also: The Single UNIX Specification, Version 2,
Added in version 3.3.
Changed in version 3.11: The `fallback` values are also used if [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size") returns zeroes.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html)
    * [Directory and files operations](https://docs.python.org/3/library/shutil.html#directory-and-files-operations)
      * [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations)
      * [copytree example](https://docs.python.org/3/library/shutil.html#copytree-example)
      * [rmtree example](https://docs.python.org/3/library/shutil.html#rmtree-example)
    * [Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)
      * [Archiving example](https://docs.python.org/3/library/shutil.html#archiving-example)
      * [Archiving example with _base_dir_](https://docs.python.org/3/library/shutil.html#archiving-example-with-base-dir)
    * [Querying the size of the output terminal](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal)


#### Previous topic
[`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html "previous chapter")
#### Next topic
[Data Persistence](https://docs.python.org/3/library/persistence.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=shutil+%E2%80%94+High-level+file+operations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fshutil.html&pagesource=library%2Fshutil.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/persistence.html "Data Persistence") |
  * [previous](https://docs.python.org/3/library/linecache.html "linecache — Random access to text lines") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html)
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
