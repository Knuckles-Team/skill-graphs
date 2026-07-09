For `execve()` on some platforms, _path_ may also be specified as an open file descriptor. This functionality may not be supported on your platform; you can check whether or not it is available using [`os.supports_fd`](https://docs.python.org/3/library/os.html#os.supports_fd "os.supports_fd"). If it is unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.exec` with arguments `path`, `args`, `env`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.
Changed in version 3.3: Added support for specifying _path_ as an open file descriptor for `execve()`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os._exit(_n_)[¶](https://docs.python.org/3/library/os.html#os._exit "Link to this definition")

Exit the process with status _n_ , without calling cleanup handlers, flushing stdio buffers, etc.
Note
The standard way to exit is [`sys.exit(n)`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit"). `_exit()` should normally only be used in the child process after a [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork").
The following exit codes are defined and can be used with [`_exit()`](https://docs.python.org/3/library/os.html#os._exit "os._exit"), although they are not required. These are typically used for system programs written in Python, such as a mail server’s external command delivery program.
Note
Some of these may not be available on all Unix platforms, since there is some variation. These constants are defined where they are defined by the underlying platform.

os.EX_OK[¶](https://docs.python.org/3/library/os.html#os.EX_OK "Link to this definition")

Exit code that means no error occurred. May be taken from the defined value of `EXIT_SUCCESS` on some platforms. Generally has a value of zero.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

os.EX_USAGE[¶](https://docs.python.org/3/library/os.html#os.EX_USAGE "Link to this definition")

Exit code that means the command was used incorrectly, such as when the wrong number of arguments are given.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_DATAERR[¶](https://docs.python.org/3/library/os.html#os.EX_DATAERR "Link to this definition")

Exit code that means the input data was incorrect.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_NOINPUT[¶](https://docs.python.org/3/library/os.html#os.EX_NOINPUT "Link to this definition")

Exit code that means an input file did not exist or was not readable.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_NOUSER[¶](https://docs.python.org/3/library/os.html#os.EX_NOUSER "Link to this definition")

Exit code that means a specified user did not exist.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_NOHOST[¶](https://docs.python.org/3/library/os.html#os.EX_NOHOST "Link to this definition")

Exit code that means a specified host did not exist.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_UNAVAILABLE[¶](https://docs.python.org/3/library/os.html#os.EX_UNAVAILABLE "Link to this definition")

Exit code that means that a required service is unavailable.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_SOFTWARE[¶](https://docs.python.org/3/library/os.html#os.EX_SOFTWARE "Link to this definition")

Exit code that means an internal software error was detected.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_OSERR[¶](https://docs.python.org/3/library/os.html#os.EX_OSERR "Link to this definition")

Exit code that means an operating system error was detected, such as the inability to fork or create a pipe.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_OSFILE[¶](https://docs.python.org/3/library/os.html#os.EX_OSFILE "Link to this definition")

Exit code that means some system file did not exist, could not be opened, or had some other kind of error.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_CANTCREAT[¶](https://docs.python.org/3/library/os.html#os.EX_CANTCREAT "Link to this definition")

Exit code that means a user specified output file could not be created.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_IOERR[¶](https://docs.python.org/3/library/os.html#os.EX_IOERR "Link to this definition")

Exit code that means that an error occurred while doing I/O on some file.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_TEMPFAIL[¶](https://docs.python.org/3/library/os.html#os.EX_TEMPFAIL "Link to this definition")

Exit code that means a temporary failure occurred. This indicates something that may not really be an error, such as a network connection that couldn’t be made during a retryable operation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_PROTOCOL[¶](https://docs.python.org/3/library/os.html#os.EX_PROTOCOL "Link to this definition")

Exit code that means that a protocol exchange was illegal, invalid, or not understood.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_NOPERM[¶](https://docs.python.org/3/library/os.html#os.EX_NOPERM "Link to this definition")

Exit code that means that there were insufficient permissions to perform the operation (but not intended for file system problems).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_CONFIG[¶](https://docs.python.org/3/library/os.html#os.EX_CONFIG "Link to this definition")

Exit code that means that some kind of configuration error occurred.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.EX_NOTFOUND[¶](https://docs.python.org/3/library/os.html#os.EX_NOTFOUND "Link to this definition")

Exit code that means something like “an entry was not found”.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.fork()[¶](https://docs.python.org/3/library/os.html#os.fork "Link to this definition")

Fork a child process. Return `0` in the child and the child’s process id in the parent. If an error occurs [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
Note that some platforms including FreeBSD <= 6.3 and Cygwin have known issues when using `fork()` from a thread.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.fork` with no arguments.
Warning
If you use TLS sockets in an application calling `fork()`, see the warning in the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") documentation.
Warning
On macOS the use of this function is unsafe when mixed with using higher-level system APIs, and that includes using [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.").
Changed in version 3.8: Calling `fork()` in a subinterpreter is no longer supported ([`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised).
Changed in version 3.12: If Python is able to detect that your process has multiple threads, [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") now raises a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning").
We chose to surface this as a warning, when detectable, to better inform developers of a design problem that the POSIX platform specifically notes as not supported. Even in code that _appears_ to work, it has never been safe to mix threading with [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") on POSIX platforms. The CPython runtime itself has always made API calls that are not safe for use in the child process when threads existed in the parent (such as `malloc` and `free`).
Users of macOS or users of libc or malloc implementations other than those typically found in glibc to date are among those already more likely to experience deadlocks running such code.
See [this discussion on fork being incompatible with threads](https://discuss.python.org/t/33555) for technical details of why we’re surfacing this longstanding platform compatibility problem to developers.
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX, not WASI, not Android, not iOS.

os.forkpty()[¶](https://docs.python.org/3/library/os.html#os.forkpty "Link to this definition")

Fork a child process, using a new pseudo-terminal as the child’s controlling terminal. Return a pair of `(pid, fd)`, where _pid_ is `0` in the child, the new child’s process id in the parent, and _fd_ is the file descriptor of the master end of the pseudo-terminal. For a more portable approach, use the [`pty`](https://docs.python.org/3/library/pty.html#module-pty "pty: Pseudo-Terminal Handling for Unix.") module. If an error occurs [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.forkpty` with no arguments.
Warning
On macOS the use of this function is unsafe when mixed with using higher-level system APIs, and that includes using [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.").
Changed in version 3.8: Calling `forkpty()` in a subinterpreter is no longer supported ([`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised).
Changed in version 3.12: If Python is able to detect that your process has multiple threads, this now raises a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). See the longer explanation on [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.kill(_pid_ , _sig_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.kill "Link to this definition")

Send signal _sig_ to the process _pid_. Constants for the specific signals available on the host platform are defined in the [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") module.
Windows: The [`signal.CTRL_C_EVENT`](https://docs.python.org/3/library/signal.html#signal.CTRL_C_EVENT "signal.CTRL_C_EVENT") and [`signal.CTRL_BREAK_EVENT`](https://docs.python.org/3/library/signal.html#signal.CTRL_BREAK_EVENT "signal.CTRL_BREAK_EVENT") signals are special signals which can only be sent to console processes which share a common console window, e.g., some subprocesses. Any other value for _sig_ will cause the process to be unconditionally killed by the TerminateProcess API, and the exit code will be set to _sig_.
See also [`signal.pthread_kill()`](https://docs.python.org/3/library/signal.html#signal.pthread_kill "signal.pthread_kill").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.kill` with arguments `pid`, `sig`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI, not iOS.
Changed in version 3.2: Added Windows support.

os.killpg(_pgid_ , _sig_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.killpg "Link to this definition")

Send the signal _sig_ to the process group _pgid_.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.killpg` with arguments `pgid`, `sig`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not iOS.

os.nice(_increment_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.nice "Link to this definition")

Add _increment_ to the process’s “niceness”. Return the new niceness.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.pidfd_open(_pid_ , _flags =0_)[¶](https://docs.python.org/3/library/os.html#os.pidfd_open "Link to this definition")

Return a file descriptor referring to the process _pid_ with _flags_ set. This descriptor can be used to perform process management without races and signals.
See the
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 5.3, Android >= [`build-time`](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "sys.getandroidapilevel") API level 31
Added in version 3.9.

os.PIDFD_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.PIDFD_NONBLOCK "Link to this definition")

This flag indicates that the file descriptor will be non-blocking. If the process referred to by the file descriptor has not yet terminated, then an attempt to wait on the file descriptor using [`EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN") rather than blocking.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 5.10
Added in version 3.12.

os.plock(_op_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.plock "Link to this definition")

Lock program segments into memory. The value of _op_ (defined in `<sys/lock.h>`) determines which segments are locked.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not iOS.

os.popen(_cmd_ , _mode ='r'_, _buffering =-1_)[¶](https://docs.python.org/3/library/os.html#os.popen "Link to this definition")

Open a pipe to or from command _cmd_. The return value is an open file object connected to the pipe, which can be read or written depending on whether _mode_ is `'r'` (default) or `'w'`. The _buffering_ argument have the same meaning as the corresponding argument to the built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open") function. The returned file object reads or writes text strings rather than bytes.
The `close` method returns [`None`](https://docs.python.org/3/library/constants.html#None "None") if the subprocess exited successfully, or the subprocess’s return code if there was an error. On POSIX systems, if the return code is positive it represents the return value of the process left-shifted by one byte. If the return code is negative, the process was terminated by the signal given by the negated value of the return code. (For example, the return value might be `- signal.SIGKILL` if the subprocess was killed.) On Windows systems, the return value contains the signed integer return code from the child process.
On Unix, [`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the `close` method result (exit status) into an exit code if it is not `None`. On Windows, the `close` method result is directly the exit code (or `None`).
This is implemented using [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen"); see that class’s documentation for more powerful ways to manage and communicate with subprocesses.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI, not Android, not iOS.
Note
The [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) affects encodings used for _cmd_ and pipe contents.
`popen()` is a simple wrapper around [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen"). Use `subprocess.Popen` or [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") to control options like encodings.
Deprecated since version 3.14: The function is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated) and should no longer be used to write new code. The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module is recommended instead.

os.posix_spawn(_path_ , _argv_ , _env_ , _*_ , _file_actions =None_, _setpgroup =None_, _resetids =False_, _setsid =False_, _setsigmask =()_, _setsigdef =()_, _scheduler =None_)[¶](https://docs.python.org/3/library/os.html#os.posix_spawn "Link to this definition")

Wraps the `posix_spawn()` C library API for use from Python.
Most users should use [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") instead of `posix_spawn()`.
The positional-only arguments _path_ , _args_ , and _env_ are similar to [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve"). _env_ is allowed to be `None`, in which case current process’ environment is used.
The _path_ parameter is the path to the executable file. The _path_ should contain a directory. Use [`posix_spawnp()`](https://docs.python.org/3/library/os.html#os.posix_spawnp "os.posix_spawnp") to pass an executable file without directory.
The _file_actions_ argument may be a sequence of tuples describing actions to take on specific file descriptors in the child process between the C library implementation’s `fork()` and `exec()` steps. The first item in each tuple must be one of the three type indicator listed below describing the remaining tuple elements:

os.POSIX_SPAWN_OPEN[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_OPEN "Link to this definition")

(`os.POSIX_SPAWN_OPEN`, _fd_ , _path_ , _flags_ , _mode_)
Performs `os.dup2(os.open(path, flags, mode), fd)`.

os.POSIX_SPAWN_CLOSE[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_CLOSE "Link to this definition")

(`os.POSIX_SPAWN_CLOSE`, _fd_)
Performs `os.close(fd)`.

os.POSIX_SPAWN_DUP2[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_DUP2 "Link to this definition")

(`os.POSIX_SPAWN_DUP2`, _fd_ , _new_fd_)
Performs `os.dup2(fd, new_fd)`.

os.POSIX_SPAWN_CLOSEFROM[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_CLOSEFROM "Link to this definition")

(`os.POSIX_SPAWN_CLOSEFROM`, _fd_)
Performs `os.closerange(fd, INF)`.
These tuples correspond to the C library `posix_spawn_file_actions_addopen()`, `posix_spawn_file_actions_addclose()`, `posix_spawn_file_actions_adddup2()`, and `posix_spawn_file_actions_addclosefrom_np()` API calls used to prepare for the `posix_spawn()` call itself.
The _setpgroup_ argument will set the process group of the child to the value specified. If the value specified is 0, the child’s process group ID will be made the same as its process ID. If the value of _setpgroup_ is not set, the child will inherit the parent’s process group ID. This argument corresponds to the C library `POSIX_SPAWN_SETPGROUP` flag.
If the _resetids_ argument is `True` it will reset the effective UID and GID of the child to the real UID and GID of the parent process. If the argument is `False`, then the child retains the effective UID and GID of the parent. In either case, if the set-user-ID and set-group-ID permission bits are enabled on the executable file, their effect will override the setting of the effective UID and GID. This argument corresponds to the C library `POSIX_SPAWN_RESETIDS` flag.
If the _setsid_ argument is `True`, it will create a new session ID for `posix_spawn`. _setsid_ requires `POSIX_SPAWN_SETSID` or `POSIX_SPAWN_SETSID_NP` flag. Otherwise, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") is raised.
The _setsigmask_ argument will set the signal mask to the signal set specified. If the parameter is not used, then the child inherits the parent’s signal mask. This argument corresponds to the C library `POSIX_SPAWN_SETSIGMASK` flag.
The _sigdef_ argument will reset the disposition of all signals in the set specified. This argument corresponds to the C library `POSIX_SPAWN_SETSIGDEF` flag.
The _scheduler_ argument must be a tuple containing the (optional) scheduler policy and an instance of [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param") with the scheduler parameters. A value of `None` in the place of the scheduler policy indicates that is not being provided. This argument is a combination of the C library `POSIX_SPAWN_SETSCHEDPARAM` and `POSIX_SPAWN_SETSCHEDULER` flags.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.posix_spawn` with arguments `path`, `argv`, `env`.
Added in version 3.8.
Changed in version 3.13: _env_ parameter accepts `None`. `os.POSIX_SPAWN_CLOSEFROM` is available on platforms where `posix_spawn_file_actions_addclosefrom_np()` exists.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.posix_spawnp(_path_ , _argv_ , _env_ , _*_ , _file_actions =None_, _setpgroup =None_, _resetids =False_, _setsid =False_, _setsigmask =()_, _setsigdef =()_, _scheduler =None_)[¶](https://docs.python.org/3/library/os.html#os.posix_spawnp "Link to this definition")

Wraps the `posix_spawnp()` C library API for use from Python.
Similar to [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn") except that the system searches for the _executable_ file in the list of directories specified by the `PATH` environment variable (in the same way as for `execvp(3)`).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.posix_spawn` with arguments `path`, `argv`, `env`.
Added in version 3.8.
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX, not WASI, not Android, not iOS.
See [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn") documentation.

os.register_at_fork(_*_ , _before =None_, _after_in_parent =None_, _after_in_child =None_)[¶](https://docs.python.org/3/library/os.html#os.register_at_fork "Link to this definition")

Register callables to be executed when a new child process is forked using [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") or similar process cloning APIs. The parameters are optional and keyword-only. Each specifies a different call point.
  * _before_ is a function called before forking a child process.
  * _after_in_parent_ is a function called from the parent process after forking a child process.
  * _after_in_child_ is a function called from the child process.


These calls are only made if control is expected to return to the Python interpreter. A typical [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") launch will not trigger them as the child is not going to re-enter the interpreter.
Functions registered for execution before forking are called in reverse registration order. Functions registered for execution after forking (either in the parent or in the child) are called in registration order.
Note that `fork()` calls made by third-party C code may not call those functions, unless it explicitly calls [`PyOS_BeforeFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_BeforeFork "PyOS_BeforeFork"), [`PyOS_AfterFork_Parent()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Parent "PyOS_AfterFork_Parent") and [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child").
There is no way to unregister a function.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
Added in version 3.7.

os.spawnl(_mode_ , _path_ , _..._)[¶](https://docs.python.org/3/library/os.html#os.spawnl "Link to this definition")


os.spawnle(_mode_ , _path_ , _..._ , _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnle "Link to this definition")


os.spawnlp(_mode_ , _file_ , _..._)[¶](https://docs.python.org/3/library/os.html#os.spawnlp "Link to this definition")


os.spawnlpe(_mode_ , _file_ , _..._ , _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnlpe "Link to this definition")


os.spawnv(_mode_ , _path_ , _args_)[¶](https://docs.python.org/3/library/os.html#os.spawnv "Link to this definition")


os.spawnve(_mode_ , _path_ , _args_ , _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnve "Link to this definition")


os.spawnvp(_mode_ , _file_ , _args_)[¶](https://docs.python.org/3/library/os.html#os.spawnvp "Link to this definition")


os.spawnvpe(_mode_ , _file_ , _args_ , _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnvpe "Link to this definition")

Execute the program _path_ in a new process.
