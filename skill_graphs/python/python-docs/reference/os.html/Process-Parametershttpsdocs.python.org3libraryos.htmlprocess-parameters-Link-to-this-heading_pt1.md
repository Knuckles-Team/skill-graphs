## Process Parameters[¶](https://docs.python.org/3/library/os.html#process-parameters "Link to this heading")
These functions and data items provide information and operate on the current process and user.

os.ctermid()[¶](https://docs.python.org/3/library/os.html#os.ctermid "Link to this definition")

Return the filename corresponding to the controlling terminal of the process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.environ[¶](https://docs.python.org/3/library/os.html#os.environ "Link to this definition")

A [mapping](https://docs.python.org/3/glossary.html#term-mapping) object where keys and values are strings that represent the process environment. For example, `environ['HOME']` is the pathname of your home directory (on some platforms), and is equivalent to `getenv("HOME")` in C.
This mapping is captured the first time the `os` module is imported, typically during Python startup as part of processing `site.py`. Changes to the environment made after this time are not reflected in [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ"), except for changes made by modifying `os.environ` directly.
This mapping may be used to modify the environment as well as query the environment. [`putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv") will be called automatically when the mapping is modified.
On Unix, keys and values use [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") and `'surrogateescape'` error handler. Use [`environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb") if you would like to use a different encoding.
On Windows, the keys are converted to uppercase. This also applies when getting, setting, or deleting an item. For example, `environ['monty'] = 'python'` maps the key `'MONTY'` to the value `'python'`.
Note
Calling [`putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv") directly does not change [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ"), so it’s better to modify `os.environ`.
Note
On some platforms, including FreeBSD and macOS, setting `environ` may cause memory leaks. Refer to the system documentation for `putenv()`.
You can delete items in this mapping to unset environment variables. [`unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv") will be called automatically when an item is deleted from [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ"), and when one of the `pop()` or `clear()` methods is called.
See also
The [`os.reload_environ()`](https://docs.python.org/3/library/os.html#os.reload_environ "os.reload_environ") function.
Changed in version 3.9: Updated to support [**PEP 584**](https://peps.python.org/pep-0584/)’s merge (`|`) and update (`|=`) operators.

os.environb[¶](https://docs.python.org/3/library/os.html#os.environb "Link to this definition")

Bytes version of [`environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ"): a [mapping](https://docs.python.org/3/glossary.html#term-mapping) object where both keys and values are [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects representing the process environment. `environ` and `environb` are synchronized (modifying `environb` updates `environ`, and vice versa).
`environb` is only available if [`supports_bytes_environ`](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "os.supports_bytes_environ") is `True`.
Added in version 3.2.
Changed in version 3.9: Updated to support [**PEP 584**](https://peps.python.org/pep-0584/)’s merge (`|`) and update (`|=`) operators.

os.reload_environ()[¶](https://docs.python.org/3/library/os.html#os.reload_environ "Link to this definition")

The [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") and [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb") mappings are a cache of environment variables at the time that Python started. As such, changes to the current process environment are not reflected if made outside Python, or by [`os.putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv") or [`os.unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv"). Use `os.reload_environ()` to update `os.environ` and `os.environb` with any such changes to the current process environment.
Warning
This function is not thread-safe. Calling it while the environment is being modified in another thread is an undefined behavior. Reading from [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") or [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb"), or calling [`os.getenv()`](https://docs.python.org/3/library/os.html#os.getenv "os.getenv") while reloading, may return an empty result.
Added in version 3.14.

os.chdir(_path_)


os.fchdir(_fd_)


os.getcwd()

These functions are described in [Files and Directories](https://docs.python.org/3/library/os.html#os-file-dir).

os.fsencode(_filename_)[¶](https://docs.python.org/3/library/os.html#os.fsencode "Link to this definition")

Encode [path-like](https://docs.python.org/3/glossary.html#term-path-like-object) _filename_ to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler); return [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") unchanged.
[`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode") is the reverse function.
Added in version 3.2.
Changed in version 3.6: Support added to accept objects implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface.

os.fsdecode(_filename_)[¶](https://docs.python.org/3/library/os.html#os.fsdecode "Link to this definition")

Decode the [path-like](https://docs.python.org/3/glossary.html#term-path-like-object) _filename_ from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler); return [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") unchanged.
[`fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode") is the reverse function.
Added in version 3.2.
Changed in version 3.6: Support added to accept objects implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface.

os.fspath(_path_)[¶](https://docs.python.org/3/library/os.html#os.fspath "Link to this definition")

Return the file system representation of the path.
If [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") is passed in, it is returned unchanged. Otherwise [`__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__") is called and its value is returned as long as it is a `str` or `bytes` object. In all other cases, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.
Added in version 3.6.

_class_ os.PathLike[¶](https://docs.python.org/3/library/os.html#os.PathLike "Link to this definition")

An [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class) for objects representing a file system path, e.g. [`pathlib.PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath").
Added in version 3.6.

_abstractmethod_ __fspath__()[¶](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "Link to this definition")

Return the file system path representation of the object.
The method should only return a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object, with the preference being for `str`.

os.getenv(_key_ , _default =None_)[¶](https://docs.python.org/3/library/os.html#os.getenv "Link to this definition")

Return the value of the environment variable _key_ as a string if it exists, or _default_ if it doesn’t. _key_ is a string. Note that since `getenv()` uses [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ"), the mapping of `getenv()` is similarly also captured on import, and the function may not reflect future environment changes.
On Unix, keys and values are decoded with [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") and `'surrogateescape'` error handler. Use [`os.getenvb()`](https://docs.python.org/3/library/os.html#os.getenvb "os.getenvb") if you would like to use a different encoding.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

os.getenvb(_key_ , _default =None_)[¶](https://docs.python.org/3/library/os.html#os.getenvb "Link to this definition")

Return the value of the environment variable _key_ as bytes if it exists, or _default_ if it doesn’t. _key_ must be bytes. Note that since `getenvb()` uses [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb"), the mapping of `getenvb()` is similarly also captured on import, and the function may not reflect future environment changes.
`getenvb()` is only available if [`supports_bytes_environ`](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "os.supports_bytes_environ") is `True`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.2.

os.get_exec_path(_env =None_)[¶](https://docs.python.org/3/library/os.html#os.get_exec_path "Link to this definition")

Returns the list of directories that will be searched for a named executable, similar to a shell, when launching a process. _env_ , when specified, should be an environment variable dictionary to lookup the PATH in. By default, when _env_ is `None`, [`environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") is used.
Added in version 3.2.

os.getegid()[¶](https://docs.python.org/3/library/os.html#os.getegid "Link to this definition")

Return the effective group id of the current process. This corresponds to the “set id” bit on the file being executed in the current process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.geteuid()[¶](https://docs.python.org/3/library/os.html#os.geteuid "Link to this definition")

Return the current process’s effective user id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.getgid()[¶](https://docs.python.org/3/library/os.html#os.getgid "Link to this definition")

Return the real group id of the current process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

os.getgrouplist(_user_ , _group_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.getgrouplist "Link to this definition")

Return list of group ids that _user_ belongs to. If _group_ is not in the list, it is included; typically, _group_ is specified as the group ID field from the password record for _user_ , because that group ID will otherwise be potentially omitted.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.3.

os.getgroups()[¶](https://docs.python.org/3/library/os.html#os.getgroups "Link to this definition")

Return list of supplemental group ids associated with the current process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Note
On macOS, `getgroups()` behavior differs somewhat from other Unix platforms. If the Python interpreter was built with a deployment target of `10.5` or earlier, `getgroups()` returns the list of effective group ids associated with the current user process; this list is limited to a system-defined number of entries, typically 16, and may be modified by calls to [`setgroups()`](https://docs.python.org/3/library/os.html#os.setgroups "os.setgroups") if suitably privileged. If built with a deployment target greater than `10.5`, `getgroups()` returns the current group access list for the user associated with the effective user id of the process; the group access list may change over the lifetime of the process, it is not affected by calls to `setgroups()`, and its length is not limited to 16. The deployment target value, `MACOSX_DEPLOYMENT_TARGET`, can be obtained with [`sysconfig.get_config_var()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var").

os.getlogin()[¶](https://docs.python.org/3/library/os.html#os.getlogin "Link to this definition")

Return the name of the user logged in on the controlling terminal of the process. For most purposes, it is more useful to use [`getpass.getuser()`](https://docs.python.org/3/library/getpass.html#getpass.getuser "getpass.getuser") since the latter checks the environment variables `LOGNAME` or `USERNAME` to find out who the user is, and falls back to `pwd.getpwuid(os.getuid())[0]` to get the login name of the current real user id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI.

os.getpgid(_pid_)[¶](https://docs.python.org/3/library/os.html#os.getpgid "Link to this definition")

Return the process group id of the process with process id _pid_. If _pid_ is 0, the process group id of the current process is returned.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.getpgrp()[¶](https://docs.python.org/3/library/os.html#os.getpgrp "Link to this definition")

Return the id of the current process group.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.getpid()[¶](https://docs.python.org/3/library/os.html#os.getpid "Link to this definition")

Return the current process id.
The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

os.getppid()[¶](https://docs.python.org/3/library/os.html#os.getppid "Link to this definition")

Return the parent’s process id. When the parent process has exited, on Unix the id returned is the one of the init process (1), on Windows it is still the same id, which may be already reused by another process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI.
Changed in version 3.2: Added support for Windows.

os.getpriority(_which_ , _who_)[¶](https://docs.python.org/3/library/os.html#os.getpriority "Link to this definition")

Get program scheduling priority. The value _which_ is one of [`PRIO_PROCESS`](https://docs.python.org/3/library/os.html#os.PRIO_PROCESS "os.PRIO_PROCESS"), [`PRIO_PGRP`](https://docs.python.org/3/library/os.html#os.PRIO_PGRP "os.PRIO_PGRP"), or [`PRIO_USER`](https://docs.python.org/3/library/os.html#os.PRIO_USER "os.PRIO_USER"), and _who_ is interpreted relative to _which_ (a process identifier for `PRIO_PROCESS`, process group identifier for `PRIO_PGRP`, and a user ID for `PRIO_USER`). A zero value for _who_ denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.3.

os.PRIO_PROCESS[¶](https://docs.python.org/3/library/os.html#os.PRIO_PROCESS "Link to this definition")


os.PRIO_PGRP[¶](https://docs.python.org/3/library/os.html#os.PRIO_PGRP "Link to this definition")


os.PRIO_USER[¶](https://docs.python.org/3/library/os.html#os.PRIO_USER "Link to this definition")

Parameters for the [`getpriority()`](https://docs.python.org/3/library/os.html#os.getpriority "os.getpriority") and [`setpriority()`](https://docs.python.org/3/library/os.html#os.setpriority "os.setpriority") functions.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.3.

os.PRIO_DARWIN_THREAD[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_THREAD "Link to this definition")


os.PRIO_DARWIN_PROCESS[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_PROCESS "Link to this definition")


os.PRIO_DARWIN_BG[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_BG "Link to this definition")


os.PRIO_DARWIN_NONUI[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_NONUI "Link to this definition")

Parameters for the [`getpriority()`](https://docs.python.org/3/library/os.html#os.getpriority "os.getpriority") and [`setpriority()`](https://docs.python.org/3/library/os.html#os.setpriority "os.setpriority") functions.
[Availability](https://docs.python.org/3/library/intro.html#availability): macOS
Added in version 3.12.

os.getresuid()[¶](https://docs.python.org/3/library/os.html#os.getresuid "Link to this definition")

Return a tuple (ruid, euid, suid) denoting the current process’s real, effective, and saved user ids.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.2.

os.getresgid()[¶](https://docs.python.org/3/library/os.html#os.getresgid "Link to this definition")

Return a tuple (rgid, egid, sgid) denoting the current process’s real, effective, and saved group ids.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.2.

os.getuid()[¶](https://docs.python.org/3/library/os.html#os.getuid "Link to this definition")

Return the current process’s real user id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

os.initgroups(_username_ , _gid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.initgroups "Link to this definition")

Call the system `initgroups()` to initialize the group access list with all of the groups of which the specified username is a member, plus the specified group id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.
Added in version 3.2.

os.putenv(_key_ , _value_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.putenv "Link to this definition")

Set the environment variable named _key_ to the string _value_. Such changes to the environment affect subprocesses started with [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system"), [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") or [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") and [`execv()`](https://docs.python.org/3/library/os.html#os.execv "os.execv").
Assignments to items in [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") are automatically translated into corresponding calls to `putenv()`; however, calls to `putenv()` don’t update `os.environ`, so it is actually preferable to assign to items of `os.environ`. This also applies to [`getenv()`](https://docs.python.org/3/library/os.html#os.getenv "os.getenv") and [`getenvb()`](https://docs.python.org/3/library/os.html#os.getenvb "os.getenvb"), which respectively use `os.environ` and [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb") in their implementations.
See also the [`os.reload_environ()`](https://docs.python.org/3/library/os.html#os.reload_environ "os.reload_environ") function.
Note
On some platforms, including FreeBSD and macOS, setting `environ` may cause memory leaks. Refer to the system documentation for `putenv()`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.putenv` with arguments `key`, `value`.
Changed in version 3.9: The function is now always available.

os.setegid(_egid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setegid "Link to this definition")

Set the current process’s effective group id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.

os.seteuid(_euid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.seteuid "Link to this definition")

Set the current process’s effective user id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.

os.setgid(_gid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setgid "Link to this definition")

Set the current process’ group id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.

os.setgroups(_groups_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setgroups "Link to this definition")

Set the list of supplemental group ids associated with the current process to _groups_. _groups_ must be a sequence, and each element must be an integer identifying a group. This operation is typically available only to the superuser.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Note
On macOS, the length of _groups_ may not exceed the system-defined maximum number of effective group ids, typically 16. See the documentation for [`getgroups()`](https://docs.python.org/3/library/os.html#os.getgroups "os.getgroups") for cases where it may not return the same group list set by calling setgroups().

os.setns(_fd_ , _nstype =0_)[¶](https://docs.python.org/3/library/os.html#os.setns "Link to this definition")

Reassociate the current thread with a Linux namespace. See the
If _fd_ refers to a `/proc/_pid_/ns/`link,`setns()` reassociates the calling thread with the namespace associated with that link, and _nstype_ may be set to one of the [CLONE_NEW* constants](https://docs.python.org/3/library/os.html#os-unshare-clone-flags) to impose constraints on the operation (`0` means no constraints).
Since Linux 5.8, _fd_ may refer to a PID file descriptor obtained from [`pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open"). In this case, `setns()` reassociates the calling thread into one or more of the same namespaces as the thread referred to by _fd_. This is subject to any constraints imposed by _nstype_ , which is a bit mask combining one or more of the [CLONE_NEW* constants](https://docs.python.org/3/library/os.html#os-unshare-clone-flags), e.g. `setns(fd, os.CLONE_NEWUTS | os.CLONE_NEWPID)`. The caller’s memberships in unspecified namespaces are left unchanged.
_fd_ can be any object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method, or a raw file descriptor.
This example reassociates the thread with the `init` process’s network namespace:
Copy```
fd = os.open("/proc/1/ns/net", os.O_RDONLY)
os.setns(fd, os.CLONE_NEWNET)
os.close(fd)

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.0 with glibc >= 2.14.
Added in version 3.12.
See also
The [`unshare()`](https://docs.python.org/3/library/os.html#os.unshare "os.unshare") function.

os.setpgrp()[¶](https://docs.python.org/3/library/os.html#os.setpgrp "Link to this definition")

Call the system call `setpgrp()` or `setpgrp(0, 0)` depending on which version is implemented (if any). See the Unix manual for the semantics.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.setpgid(_pid_ , _pgrp_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setpgid "Link to this definition")

Call the system call `setpgid()` to set the process group id of the process with id _pid_ to the process group with id _pgrp_. See the Unix manual for the semantics.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.setpriority(_which_ , _who_ , _priority_)[¶](https://docs.python.org/3/library/os.html#os.setpriority "Link to this definition")

Set program scheduling priority. The value _which_ is one of [`PRIO_PROCESS`](https://docs.python.org/3/library/os.html#os.PRIO_PROCESS "os.PRIO_PROCESS"), [`PRIO_PGRP`](https://docs.python.org/3/library/os.html#os.PRIO_PGRP "os.PRIO_PGRP"), or [`PRIO_USER`](https://docs.python.org/3/library/os.html#os.PRIO_USER "os.PRIO_USER"), and _who_ is interpreted relative to _which_ (a process identifier for `PRIO_PROCESS`, process group identifier for `PRIO_PGRP`, and a user ID for `PRIO_USER`). A zero value for _who_ denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process. _priority_ is a value in the range -20 to 19. The default priority is 0; lower priorities cause more favorable scheduling.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.3.

os.setregid(_rgid_ , _egid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setregid "Link to this definition")
