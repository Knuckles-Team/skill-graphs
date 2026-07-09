(Note that the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module provides more powerful facilities for spawning new processes and retrieving their results; using that module is preferable to using these functions. Check especially the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3/library/subprocess.html#subprocess-replacements) section.)
If _mode_ is [`P_NOWAIT`](https://docs.python.org/3/library/os.html#os.P_NOWAIT "os.P_NOWAIT"), this function returns the process id of the new process; if _mode_ is [`P_WAIT`](https://docs.python.org/3/library/os.html#os.P_WAIT "os.P_WAIT"), returns the process’s exit code if it exits normally, or `-signal`, where _signal_ is the signal that killed the process. On Windows, the process id will actually be the process handle, so can be used with the [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") function.
Note on VxWorks, this function doesn’t return `-signal` when the new process is killed. Instead it raises OSError exception.
The “l” and “v” variants of the `spawn*` functions differ in how command-line arguments are passed. The “l” variants are perhaps the easiest to work with if the number of parameters is fixed when the code is written; the individual parameters simply become additional parameters to the `spawnl*()` functions. The “v” variants are good when the number of parameters is variable, with the arguments being passed in a list or tuple as the _args_ parameter. In either case, the arguments to the child process must start with the name of the command being run.
The variants which include a second “p” near the end (`spawnlp()`, `spawnlpe()`, `spawnvp()`, and `spawnvpe()`) will use the `PATH` environment variable to locate the program _file_. When the environment is being replaced (using one of the `spawn*e` variants, discussed in the next paragraph), the new environment is used as the source of the `PATH` variable. The other variants, `spawnl()`, `spawnle()`, `spawnv()`, and `spawnve()`, will not use the `PATH` variable to locate the executable; _path_ must contain an appropriate absolute or relative path.
For `spawnle()`, `spawnlpe()`, `spawnve()`, and `spawnvpe()` (note that these all end in “e”), the _env_ parameter must be a mapping which is used to define the environment variables for the new process (they are used instead of the current process’ environment); the functions `spawnl()`, `spawnlp()`, `spawnv()`, and `spawnvp()` all cause the new process to inherit the environment of the current process. Note that keys and values in the _env_ dictionary must be strings; invalid keys or values will cause the function to fail, with a return value of `127`.
As an example, the following calls to `spawnlp()` and `spawnvpe()` are equivalent:
Copy```
import os
os.spawnlp(os.P_WAIT, 'cp', 'cp', 'index.html', '/dev/null')

L = ['cp', 'index.html', '/dev/null']
os.spawnvpe(os.P_WAIT, 'cp', L, os.environ)

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.spawn` with arguments `mode`, `path`, `args`, `env`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.
`spawnlp()`, `spawnlpe()`, `spawnvp()` and `spawnvpe()` are not available on Windows. `spawnle()` and `spawnve()` are not thread-safe on Windows; we advise you to use the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module instead.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Deprecated since version 3.14: These functions are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated) and should no longer be used to write new code. The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module is recommended instead.

os.P_NOWAIT[¶](https://docs.python.org/3/library/os.html#os.P_NOWAIT "Link to this definition")


os.P_NOWAITO[¶](https://docs.python.org/3/library/os.html#os.P_NOWAITO "Link to this definition")

Possible values for the _mode_ parameter to the [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") family of functions. If either of these values is given, the `spawn*` functions will return as soon as the new process has been created, with the process id as the return value.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

os.P_WAIT[¶](https://docs.python.org/3/library/os.html#os.P_WAIT "Link to this definition")

Possible value for the _mode_ parameter to the [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") family of functions. If this is given as _mode_ , the `spawn*` functions will not return until the new process has run to completion and will return the exit code of the process the run is successful, or `-signal` if a signal kills the process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

os.P_DETACH[¶](https://docs.python.org/3/library/os.html#os.P_DETACH "Link to this definition")


os.P_OVERLAY[¶](https://docs.python.org/3/library/os.html#os.P_OVERLAY "Link to this definition")

Possible values for the _mode_ parameter to the [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") family of functions. These are less portable than those listed above. [`P_DETACH`](https://docs.python.org/3/library/os.html#os.P_DETACH "os.P_DETACH") is similar to [`P_NOWAIT`](https://docs.python.org/3/library/os.html#os.P_NOWAIT "os.P_NOWAIT"), but the new process is detached from the console of the calling process. If [`P_OVERLAY`](https://docs.python.org/3/library/os.html#os.P_OVERLAY "os.P_OVERLAY") is used, the current process will be replaced; the `spawn*` function will not return.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

os.startfile(_path_[, _operation_][, _arguments_][, _cwd_][, _show_cmd_])[¶](https://docs.python.org/3/library/os.html#os.startfile "Link to this definition")

Start a file with its associated application.
When _operation_ is not specified, this acts like double-clicking the file in Windows Explorer, or giving the file name as an argument to the **start** command from the interactive command shell: the file is opened with whatever application (if any) its extension is associated.
When another _operation_ is given, it must be a “command verb” that specifies what should be done with the file. Common verbs documented by Microsoft are `'open'`, `'print'` and `'edit'` (to be used on files) as well as `'explore'` and `'find'` (to be used on directories).
When launching an application, specify _arguments_ to be passed as a single string. This argument may have no effect when using this function to launch a document.
The default working directory is inherited, but may be overridden by the _cwd_ argument. This should be an absolute path. A relative _path_ will be resolved against this argument.
Use _show_cmd_ to override the default window style. Whether this has any effect will depend on the application being launched. Values are integers as supported by the Win32 `ShellExecute()` function.
`startfile()` returns as soon as the associated application is launched. There is no option to wait for the application to close, and no way to retrieve the application’s exit status. The _path_ parameter is relative to the current directory or _cwd_. If you want to use an absolute path, make sure the first character is not a slash (`'/'`) Use [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths") or the [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath") function to ensure that paths are properly encoded for Win32.
To reduce interpreter startup overhead, the Win32 `ShellExecute()` function is not resolved until this function is first called. If the function cannot be resolved, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") will be raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.startfile` with arguments `path`, `operation`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.startfile/2` with arguments `path`, `operation`, `arguments`, `cwd`, `show_cmd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Changed in version 3.10: Added the _arguments_ , _cwd_ and _show_cmd_ arguments, and the `os.startfile/2` audit event.

os.system(_command_)[¶](https://docs.python.org/3/library/os.html#os.system "Link to this definition")

Execute the command (a string) in a subshell. This is implemented by calling the Standard C function `system()`, and has the same limitations. Changes to [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin"), etc. are not reflected in the environment of the executed command. If _command_ generates any output, it will be sent to the interpreter standard output stream. The C standard does not specify the meaning of the return value of the C function, so the return value of the Python function is system-dependent.
On Unix, the return value is the exit status of the process encoded in the format specified for [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait").
On Windows, the return value is that returned by the system shell after running _command_. The shell is given by the Windows environment variable `COMSPEC`: it is usually **cmd.exe** , which returns the exit status of the command run; on systems using a non-native shell, consult your shell documentation.
The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module provides more powerful facilities for spawning new processes and retrieving their results; using that module is recommended to using this function. See the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3/library/subprocess.html#subprocess-replacements) section in the `subprocess` documentation for some helpful recipes.
On Unix, [`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the result (exit status) into an exit code. On Windows, the result is directly the exit code.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.system` with argument `command`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.

os.times()[¶](https://docs.python.org/3/library/os.html#os.times "Link to this definition")

Returns the current global process times. The return value is an object with five attributes:
  * `user` - user time
  * `system` - system time
  * `children_user` - user time of all child processes
  * `children_system` - system time of all child processes
  * `elapsed` - elapsed real time since a fixed point in the past


For backwards compatibility, this object also behaves like a five-tuple containing `user`, `system`, `children_user`, `children_system`, and `elapsed` in that order.
See the Unix manual page `user` and `system` are known; the other attributes are zero.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.3: Return type changed from a tuple to a tuple-like object with named attributes.

os.wait()[¶](https://docs.python.org/3/library/os.html#os.wait "Link to this definition")

Wait for completion of a child process, and return a tuple containing its pid and exit status indication: a 16-bit number, whose low byte is the signal number that killed the process, and whose high byte is the exit status (if the signal number is zero); the high bit of the low byte is set if a core file was produced.
If there are no children that could be waited for, [`ChildProcessError`](https://docs.python.org/3/library/exceptions.html#ChildProcessError "ChildProcessError") is raised.
[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the exit status into an exit code.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
See also
The other `wait*()` functions documented below can be used to wait for the completion of a specific child process and have more options. [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") is the only one also available on Windows.

os.waitid(_idtype_ , _id_ , _options_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.waitid "Link to this definition")

Wait for the completion of a child process.
_idtype_ can be [`P_PID`](https://docs.python.org/3/library/os.html#os.P_PID "os.P_PID"), [`P_PGID`](https://docs.python.org/3/library/os.html#os.P_PGID "os.P_PGID"), [`P_ALL`](https://docs.python.org/3/library/os.html#os.P_ALL "os.P_ALL"), or (on Linux) [`P_PIDFD`](https://docs.python.org/3/library/os.html#os.P_PIDFD "os.P_PIDFD"). The interpretation of _id_ depends on it; see their individual descriptions.
_options_ is an OR combination of flags. At least one of [`WEXITED`](https://docs.python.org/3/library/os.html#os.WEXITED "os.WEXITED"), [`WSTOPPED`](https://docs.python.org/3/library/os.html#os.WSTOPPED "os.WSTOPPED") or [`WCONTINUED`](https://docs.python.org/3/library/os.html#os.WCONTINUED "os.WCONTINUED") is required; [`WNOHANG`](https://docs.python.org/3/library/os.html#os.WNOHANG "os.WNOHANG") and [`WNOWAIT`](https://docs.python.org/3/library/os.html#os.WNOWAIT "os.WNOWAIT") are additional optional flags.
The return value is an object representing the data contained in the `siginfo_t` structure with the following attributes:
  * `si_pid` (process ID)
  * `si_uid` (real user ID of the child)
  * `si_signo` (always [`SIGCHLD`](https://docs.python.org/3/library/signal.html#signal.SIGCHLD "signal.SIGCHLD"))
  * `si_status` (the exit status or signal number, depending on `si_code`)
  * `si_code` (see [`CLD_EXITED`](https://docs.python.org/3/library/os.html#os.CLD_EXITED "os.CLD_EXITED") for possible values)


If [`WNOHANG`](https://docs.python.org/3/library/os.html#os.WNOHANG "os.WNOHANG") is specified and there are no matching children in the requested state, `None` is returned. Otherwise, if there are no matching children that could be waited for, [`ChildProcessError`](https://docs.python.org/3/library/exceptions.html#ChildProcessError "ChildProcessError") is raised.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
Added in version 3.3.
Changed in version 3.13: This function is now available on macOS as well.

os.waitpid(_pid_ , _options_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.waitpid "Link to this definition")

The details of this function differ on Unix and Windows.
On Unix: Wait for completion of a child process given by process id _pid_ , and return a tuple containing its process id and exit status indication (encoded as for [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait")). The semantics of the call are affected by the value of the integer _options_ , which should be `0` for normal operation.
If _pid_ is greater than `0`, `waitpid()` requests status information for that specific process. If _pid_ is `0`, the request is for the status of any child in the process group of the current process. If _pid_ is `-1`, the request pertains to any child of the current process. If _pid_ is less than `-1`, status is requested for any process in the process group `-pid` (the absolute value of _pid_).
_options_ is an OR combination of flags. If it contains [`WNOHANG`](https://docs.python.org/3/library/os.html#os.WNOHANG "os.WNOHANG") and there are no matching children in the requested state, `(0, 0)` is returned. Otherwise, if there are no matching children that could be waited for, [`ChildProcessError`](https://docs.python.org/3/library/exceptions.html#ChildProcessError "ChildProcessError") is raised. Other options that can be used are [`WUNTRACED`](https://docs.python.org/3/library/os.html#os.WUNTRACED "os.WUNTRACED") and [`WCONTINUED`](https://docs.python.org/3/library/os.html#os.WCONTINUED "os.WCONTINUED").
On Windows: Wait for completion of a process given by process handle _pid_ , and return a tuple containing _pid_ , and its exit status shifted left by 8 bits (shifting makes cross-platform use of the function easier). A _pid_ less than or equal to `0` has no special meaning on Windows, and raises an exception. The value of integer _options_ has no effect. _pid_ can refer to any process whose id is known, not necessarily a child process. The [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") functions called with [`P_NOWAIT`](https://docs.python.org/3/library/os.html#os.P_NOWAIT "os.P_NOWAIT") return suitable process handles.
[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the exit status into an exit code.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

os.wait3(_options_)[¶](https://docs.python.org/3/library/os.html#os.wait3 "Link to this definition")

Similar to [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid"), except no process id argument is given and a 3-element tuple containing the child’s process id, exit status indication, and resource usage information is returned. Refer to [`resource.getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage") for details on resource usage information. The _options_ argument is the same as that provided to `waitpid()` and [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4").
[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the exit status into an exitcode.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.wait4(_pid_ , _options_)[¶](https://docs.python.org/3/library/os.html#os.wait4 "Link to this definition")

Similar to [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid"), except a 3-element tuple, containing the child’s process id, exit status indication, and resource usage information is returned. Refer to [`resource.getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage") for details on resource usage information. The arguments to `wait4()` are the same as those provided to `waitpid()`.
[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the exit status into an exitcode.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.P_PID[¶](https://docs.python.org/3/library/os.html#os.P_PID "Link to this definition")


os.P_PGID[¶](https://docs.python.org/3/library/os.html#os.P_PGID "Link to this definition")


os.P_ALL[¶](https://docs.python.org/3/library/os.html#os.P_ALL "Link to this definition")


os.P_PIDFD[¶](https://docs.python.org/3/library/os.html#os.P_PIDFD "Link to this definition")

These are the possible values for _idtype_ in [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid"). They affect how _id_ is interpreted:
  * `P_PID` - wait for the child whose PID is _id_.
  * `P_PGID` - wait for any child whose progress group ID is _id_.
  * `P_ALL` - wait for any child; _id_ is ignored.
  * `P_PIDFD` - wait for the child identified by the file descriptor _id_ (a process file descriptor created with [`pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open")).


[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
Note
`P_PIDFD` is only available on Linux >= 5.4.
Added in version 3.3.
Added in version 3.9: The `P_PIDFD` constant.

os.WCONTINUED[¶](https://docs.python.org/3/library/os.html#os.WCONTINUED "Link to this definition")

This _options_ flag for [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid"), [`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3"), [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4"), and [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid") causes child processes to be reported if they have been continued from a job control stop since they were last reported.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WEXITED[¶](https://docs.python.org/3/library/os.html#os.WEXITED "Link to this definition")

This _options_ flag for [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid") causes child processes that have terminated to be reported.
The other `wait*` functions always report children that have terminated, so this option is not available for them.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
Added in version 3.3.

os.WSTOPPED[¶](https://docs.python.org/3/library/os.html#os.WSTOPPED "Link to this definition")

This _options_ flag for [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid") causes child processes that have been stopped by the delivery of a signal to be reported.
This option is not available for the other `wait*` functions.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
Added in version 3.3.

os.WUNTRACED[¶](https://docs.python.org/3/library/os.html#os.WUNTRACED "Link to this definition")

This _options_ flag for [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid"), [`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3"), and [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4") causes child processes to also be reported if they have been stopped but their current state has not been reported since they were stopped.
This option is not available for [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WNOHANG[¶](https://docs.python.org/3/library/os.html#os.WNOHANG "Link to this definition")

This _options_ flag causes [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid"), [`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3"), [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4"), and [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid") to return right away if no child process status is available immediately.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WNOWAIT[¶](https://docs.python.org/3/library/os.html#os.WNOWAIT "Link to this definition")

This _options_ flag causes [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid") to leave the child in a waitable state, so that a later `wait*()` call can be used to retrieve the child status information again.
This option is not available for the other `wait*` functions.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.CLD_EXITED[¶](https://docs.python.org/3/library/os.html#os.CLD_EXITED "Link to this definition")


os.CLD_KILLED[¶](https://docs.python.org/3/library/os.html#os.CLD_KILLED "Link to this definition")


os.CLD_DUMPED[¶](https://docs.python.org/3/library/os.html#os.CLD_DUMPED "Link to this definition")


os.CLD_TRAPPED[¶](https://docs.python.org/3/library/os.html#os.CLD_TRAPPED "Link to this definition")


os.CLD_STOPPED[¶](https://docs.python.org/3/library/os.html#os.CLD_STOPPED "Link to this definition")


os.CLD_CONTINUED[¶](https://docs.python.org/3/library/os.html#os.CLD_CONTINUED "Link to this definition")

These are the possible values for `si_code` in the result returned by [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
