Copy```
os.access in os.supports_effective_ids

```

Currently _effective_ids_ is only supported on Unix platforms; it does not work on Windows.
Added in version 3.3.

os.supports_fd[¶](https://docs.python.org/3/library/os.html#os.supports_fd "Link to this definition")

A [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object indicating which functions in the `os` module permit specifying their _path_ parameter as an open file descriptor on the local platform. Different platforms provide different features, and the underlying functionality Python uses to accept open file descriptors as _path_ arguments is not available on all platforms Python supports.
To determine whether a particular function permits specifying an open file descriptor for its _path_ parameter, use the `in` operator on `supports_fd`. As an example, this expression evaluates to `True` if [`os.chdir()`](https://docs.python.org/3/library/os.html#os.chdir "os.chdir") accepts open file descriptors for _path_ on your local platform:
Copy```
os.chdir in os.supports_fd

```

Added in version 3.3.

os.supports_follow_symlinks[¶](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "Link to this definition")

A [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object indicating which functions in the `os` module accept `False` for their _follow_symlinks_ parameter on the local platform. Different platforms provide different features, and the underlying functionality Python uses to implement _follow_symlinks_ is not available on all platforms Python supports. For consistency’s sake, functions that may support _follow_symlinks_ always allow specifying the parameter, but will throw an exception if the functionality is used when it’s not locally available. (Specifying `True` for _follow_symlinks_ is always supported on all platforms.)
To check whether a particular function accepts `False` for its _follow_symlinks_ parameter, use the `in` operator on `supports_follow_symlinks`. As an example, this expression evaluates to `True` if you may specify `follow_symlinks=False` when calling [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") on the local platform:
Copy```
os.stat in os.supports_follow_symlinks

```

Added in version 3.3.

os.symlink(_src_ , _dst_ , _target_is_directory =False_, _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.symlink "Link to this definition")

Create a symbolic link pointing to _src_ named _dst_.
The _src_ parameter refers to the target of the link (the file or directory being linked to), and _dst_ is the name of the link being created.
On Windows, a symlink represents either a file or a directory, and does not morph to the target dynamically. If the target is present, the type of the symlink will be created to match. Otherwise, the symlink will be created as a directory if _target_is_directory_ is `True` or a file symlink (the default) otherwise. On non-Windows platforms, _target_is_directory_ is ignored.
This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
Note
On newer versions of Windows 10, unprivileged accounts can create symlinks if Developer Mode is enabled. When Developer Mode is not available/enabled, the _SeCreateSymbolicLinkPrivilege_ privilege is required, or the process must be run as an administrator.
[`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised when the function is called by an unprivileged user.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.symlink` with arguments `src`, `dst`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
Changed in version 3.2: Added support for Windows 6.0 (Vista) symbolic links.
Changed in version 3.3: Added the _dir_fd_ parameter, and now allow _target_is_directory_ on non-Windows platforms.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _src_ and _dst_.
Changed in version 3.8: Added support for unelevated symlinks on Windows with Developer Mode.

os.sync()[¶](https://docs.python.org/3/library/os.html#os.sync "Link to this definition")

Force write of everything to disk.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.truncate(_path_ , _length_)[¶](https://docs.python.org/3/library/os.html#os.truncate "Link to this definition")

Truncate the file corresponding to _path_ , so that it is at most _length_ bytes in size.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.truncate` with arguments `path`, `length`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Added in version 3.3.
Changed in version 3.5: Added support for Windows
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.unlink(_path_ , _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.unlink "Link to this definition")

Remove (delete) the file _path_. This function is semantically identical to [`remove()`](https://docs.python.org/3/library/os.html#os.remove "os.remove"); the `unlink` name is its traditional Unix name. Please see the documentation for `remove()` for further information.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.remove` with arguments `path`, `dir_fd`.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.utime(_path_ , _times=None_ , _*_ , [_ns_ , ]_dir_fd=None_ , _follow_symlinks=True_)[¶](https://docs.python.org/3/library/os.html#os.utime "Link to this definition")

Set the access and modified times of the file specified by _path_.
`utime()` takes two optional parameters, _times_ and _ns_. These specify the times set on _path_ and are used as follows:
  * If _ns_ is specified, it must be a 2-tuple of the form `(atime_ns, mtime_ns)` where each member is an int expressing nanoseconds.
  * If _times_ is not `None`, it must be a 2-tuple of the form `(atime, mtime)` where each member is an int or float expressing seconds.
  * If _times_ is `None` and _ns_ is unspecified, this is equivalent to specifying `ns=(atime_ns, mtime_ns)` where both times are the current time.


It is an error to specify tuples for both _times_ and _ns_.
Note that the exact times you set here may not be returned by a subsequent [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") call, depending on the resolution with which your operating system records access and modification times; see `stat()`. The best way to preserve exact times is to use the _st_atime_ns_ and _st_mtime_ns_ fields from the `os.stat()` result object with the _ns_ parameter to `utime()`.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd), [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.utime` with arguments `path`, `times`, `ns`, `dir_fd`.
Changed in version 3.3: Added support for specifying _path_ as an open file descriptor, and the _dir_fd_ , _follow_symlinks_ , and _ns_ parameters.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.walk(_top_ , _topdown =True_, _onerror =None_, _followlinks =False_)[¶](https://docs.python.org/3/library/os.html#os.walk "Link to this definition")

Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory _top_ (including _top_ itself), it yields a 3-tuple `(dirpath, dirnames, filenames)`.
_dirpath_ is a string, the path to the directory. _dirnames_ is a list of the names of the subdirectories in _dirpath_ (including symlinks to directories, and excluding `'.'` and `'..'`). _filenames_ is a list of the names of the non-directory files in _dirpath_. Note that the names in the lists contain no path components. To get a full path (which begins with _top_) to a file or directory in _dirpath_ , do `os.path.join(dirpath, name)`. Whether or not the lists are sorted depends on the file system. If a file is removed from or added to the _dirpath_ directory during generating the lists, whether a name for that file be included is unspecified.
If optional argument _topdown_ is `True` or not specified, the triple for a directory is generated before the triples for any of its subdirectories (directories are generated top-down). If _topdown_ is `False`, the triple for a directory is generated after the triples for all of its subdirectories (directories are generated bottom-up). No matter the value of _topdown_ , the list of subdirectories is retrieved before the tuples for the directory and its subdirectories are generated.
When _topdown_ is `True`, the caller can modify the _dirnames_ list in-place (perhaps using [`del`](https://docs.python.org/3/reference/simple_stmts.html#del) or slice assignment), and `walk()` will only recurse into the subdirectories whose names remain in _dirnames_ ; this can be used to prune the search, impose a specific order of visiting, or even to inform `walk()` about directories the caller creates or renames before it resumes `walk()` again. Modifying _dirnames_ when _topdown_ is `False` has no effect on the behavior of the walk, because in bottom-up mode the directories in _dirnames_ are generated before _dirpath_ itself is generated.
By default, errors from the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") call are ignored. If optional argument _onerror_ is specified, it should be a function; it will be called with one argument, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instance. It can report the error to continue with the walk, or raise the exception to abort the walk. Note that the filename is available as the `filename` attribute of the exception object.
By default, `walk()` will not walk down into symbolic links that resolve to directories. Set _followlinks_ to `True` to visit directories pointed to by symlinks, on systems that support them.
Note
Be aware that setting _followlinks_ to `True` can lead to infinite recursion if a link points to a parent directory of itself. `walk()` does not keep track of the directories it visited already.
Note
If you pass a relative pathname, don’t change the current working directory between resumptions of `walk()`. `walk()` never changes the current directory, and assumes that its caller doesn’t either.
This example displays the number of bytes taken by non-directory files in each directory under the starting directory, except that it doesn’t look under any `__pycache__` subdirectory:
Copy```
import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/xml'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')  # don't visit __pycache__ directories

```

In the next example (simple implementation of [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")), walking the tree bottom-up is essential, [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") doesn’t allow deleting a directory before the directory is empty:
Copy```
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.rmdir(top)

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.walk` with arguments `top`, `topdown`, `onerror`, `followlinks`.
Changed in version 3.5: This function now calls [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") instead of [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir"), making it faster by reducing the number of calls to [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat").
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.fwalk(_top ='.'_, _topdown =True_, _onerror =None_, _*_ , _follow_symlinks =False_, _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.fwalk "Link to this definition")

This behaves exactly like [`walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk"), except that it yields a 4-tuple `(dirpath, dirnames, filenames, dirfd)`, and it supports `dir_fd`.
_dirpath_ , _dirnames_ and _filenames_ are identical to [`walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk") output, and _dirfd_ is a file descriptor referring to the directory _dirpath_.
This function always supports [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks). Note however that, unlike other functions, the `fwalk()` default value for _follow_symlinks_ is `False`.
Note
Since `fwalk()` yields file descriptors, those are only valid until the next iteration step, so you should duplicate them (e.g. with [`dup()`](https://docs.python.org/3/library/os.html#os.dup "os.dup")) if you want to keep them longer.
This example displays the number of bytes taken by non-directory files in each directory under the starting directory, except that it doesn’t look under any `__pycache__` subdirectory:
Copy```
import os
for root, dirs, files, rootfd in os.fwalk('python/Lib/xml'):
    print(root, "consumes", end=" ")
    print(sum([os.stat(name, dir_fd=rootfd).st_size for name in files]),
          end=" ")
    print("bytes in", len(files), "non-directory files")
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')  # don't visit __pycache__ directories

```

In the next example, walking the tree bottom-up is essential: [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") doesn’t allow deleting a directory before the directory is empty:
Copy```
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
for root, dirs, files, rootfd in os.fwalk(top, topdown=False):
    for name in files:
        os.unlink(name, dir_fd=rootfd)
    for name in dirs:
        os.rmdir(name, dir_fd=rootfd)

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.fwalk` with arguments `top`, `topdown`, `onerror`, `follow_symlinks`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.7: Added support for [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") paths.

os.memfd_create(_name_[, _flags=os.MFD_CLOEXEC_])[¶](https://docs.python.org/3/library/os.html#os.memfd_create "Link to this definition")

Create an anonymous file and return a file descriptor that refers to it. _flags_ must be one of the `os.MFD_*` constants available on the system (or a bitwise ORed combination of them). By default, the new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
The name supplied in _name_ is used as a filename and will be displayed as the target of the corresponding symbolic link in the directory `/proc/self/fd/`. The displayed name is always prefixed with `memfd:` and serves only for debugging purposes. Names do not affect the behavior of the file descriptor, and as such multiple files can have the same name without any side effects.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.17 with glibc >= 2.27.
Added in version 3.8.

os.MFD_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.MFD_CLOEXEC "Link to this definition")


os.MFD_ALLOW_SEALING[¶](https://docs.python.org/3/library/os.html#os.MFD_ALLOW_SEALING "Link to this definition")


os.MFD_HUGETLB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGETLB "Link to this definition")


os.MFD_HUGE_SHIFT[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_SHIFT "Link to this definition")


os.MFD_HUGE_MASK[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_MASK "Link to this definition")


os.MFD_HUGE_64KB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_64KB "Link to this definition")


os.MFD_HUGE_512KB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_512KB "Link to this definition")


os.MFD_HUGE_1MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_1MB "Link to this definition")


os.MFD_HUGE_2MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_2MB "Link to this definition")


os.MFD_HUGE_8MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_8MB "Link to this definition")


os.MFD_HUGE_16MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_16MB "Link to this definition")


os.MFD_HUGE_32MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_32MB "Link to this definition")


os.MFD_HUGE_256MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_256MB "Link to this definition")


os.MFD_HUGE_512MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_512MB "Link to this definition")


os.MFD_HUGE_1GB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_1GB "Link to this definition")


os.MFD_HUGE_2GB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_2GB "Link to this definition")


os.MFD_HUGE_16GB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_16GB "Link to this definition")

These flags can be passed to [`memfd_create()`](https://docs.python.org/3/library/os.html#os.memfd_create "os.memfd_create").
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.17 with glibc >= 2.27
The `MFD_HUGE*` flags are only available since Linux 4.14.
Added in version 3.8.

os.eventfd(_initval_[, _flags=os.EFD_CLOEXEC_])[¶](https://docs.python.org/3/library/os.html#os.eventfd "Link to this definition")

Create and return an event file descriptor. The file descriptors supports raw [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read") and [`write()`](https://docs.python.org/3/library/os.html#os.write "os.write") with a buffer size of 8, [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select"), [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll") and similar. See man page [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
_initval_ is the initial value of the event counter. The initial value must be a 32 bit unsigned integer. Please note that the initial value is limited to a 32 bit unsigned int although the event counter is an unsigned 64 bit integer with a maximum value of 264-2.
_flags_ can be constructed from [`EFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.EFD_CLOEXEC "os.EFD_CLOEXEC"), [`EFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.EFD_NONBLOCK "os.EFD_NONBLOCK"), and [`EFD_SEMAPHORE`](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "os.EFD_SEMAPHORE").
If [`EFD_SEMAPHORE`](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "os.EFD_SEMAPHORE") is specified and the event counter is non-zero, [`eventfd_read()`](https://docs.python.org/3/library/os.html#os.eventfd_read "os.eventfd_read") returns 1 and decrements the counter by one.
If [`EFD_SEMAPHORE`](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "os.EFD_SEMAPHORE") is not specified and the event counter is non-zero, [`eventfd_read()`](https://docs.python.org/3/library/os.html#os.eventfd_read "os.eventfd_read") returns the current event counter value and resets the counter to zero.
If the event counter is zero and [`EFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.EFD_NONBLOCK "os.EFD_NONBLOCK") is not specified, [`eventfd_read()`](https://docs.python.org/3/library/os.html#os.eventfd_read "os.eventfd_read") blocks.
[`eventfd_write()`](https://docs.python.org/3/library/os.html#os.eventfd_write "os.eventfd_write") increments the event counter. Write blocks if the write operation would increment the counter to a value larger than 264-2.
Example:
Copy```
import os
