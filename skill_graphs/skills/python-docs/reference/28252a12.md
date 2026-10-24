## Popen Objects[¶](https://docs.python.org/3/library/subprocess.html#popen-objects "Link to this heading")
Instances of the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") class have the following methods:

Popen.poll()[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.poll "Link to this definition")

Check if child process has terminated. Set and return [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute. Otherwise, returns `None`.

Popen.wait(_timeout =None_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "Link to this definition")

Wait for child process to terminate. Set and return [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute.
If the process does not terminate after _timeout_ seconds, raise a [`TimeoutExpired`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exception. It is safe to catch this exception and retry the wait.
Note
This will deadlock when using `stdout=PIPE` or `stderr=PIPE` and the child process generates enough output to a pipe such that it blocks waiting for the OS pipe buffer to accept more data. Use [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") when using pipes to avoid that.
Note
When the `timeout` parameter is not `None`, then (on POSIX) the function is implemented using a busy loop (non-blocking call and short sleeps). Use the [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module for an asynchronous wait: see [`asyncio.create_subprocess_exec`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec").
Changed in version 3.3: _timeout_ was added.

Popen.communicate(_input =None_, _timeout =None_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "Link to this definition")

Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate and set the [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute. The optional _input_ argument should be data to be sent to the child process, or `None`, if no data should be sent to the child. If streams were opened in text mode, _input_ must be a string. Otherwise, it must be bytes.
`communicate()` returns a tuple `(stdout_data, stderr_data)`. The data will be strings if streams were opened in text mode; otherwise, bytes.
Note that if you want to send data to the process’s stdin, you need to create the Popen object with `stdin=PIPE`. Similarly, to get anything other than `None` in the result tuple, you need to give `stdout=PIPE` and/or `stderr=PIPE` too.
If the process does not terminate after _timeout_ seconds, a [`TimeoutExpired`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exception will be raised. Catching this exception and retrying communication will not lose any output. Supplying _input_ to a subsequent post-timeout `communicate()` call is in undefined behavior and may become an error in the future.
The child process is not killed if the timeout expires, so in order to cleanup properly a well-behaved application should kill the child process and finish communication:
Copy```
proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()

```

After a call to `communicate()` raises [`TimeoutExpired`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "subprocess.TimeoutExpired"), do not call [`wait()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "subprocess.Popen.wait"). Use an additional `communicate()` call to finish handling pipes and populate the [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute.
Note
The data read is buffered in memory, so do not use this method if the data size is large or unlimited.
Changed in version 3.3: _timeout_ was added.

Popen.send_signal(_signal_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.send_signal "Link to this definition")

Sends the signal _signal_ to the child.
Do nothing if the process completed.
Note
On Windows, SIGTERM is an alias for [`terminate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.terminate "subprocess.Popen.terminate"). CTRL_C_EVENT and CTRL_BREAK_EVENT can be sent to processes started with a _creationflags_ parameter which includes `CREATE_NEW_PROCESS_GROUP`.

Popen.terminate()[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.terminate "Link to this definition")

Stop the child. On POSIX OSs the method sends [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM") to the child. On Windows the Win32 API function `TerminateProcess()` is called to stop the child.

Popen.kill()[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.kill "Link to this definition")

Kills the child. On POSIX OSs the function sends SIGKILL to the child. On Windows `kill()` is an alias for [`terminate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.terminate "subprocess.Popen.terminate").
The following attributes are also set by the class for you to access. Reassigning them to new values is unsupported:

Popen.args[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.args "Link to this definition")

The _args_ argument as it was passed to [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") – a sequence of program arguments or else a single string.
Added in version 3.3.

Popen.stdin[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stdin "Link to this definition")

If the _stdin_ argument was [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"), this attribute is a writeable stream object as returned by [`open()`](https://docs.python.org/3/library/functions.html#open "open"). If the _encoding_ or _errors_ arguments were specified or the _text_ or _universal_newlines_ argument was `True`, the stream is a text stream, otherwise it is a byte stream. If the _stdin_ argument was not `PIPE`, this attribute is `None`.

Popen.stdout[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stdout "Link to this definition")

If the _stdout_ argument was [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"), this attribute is a readable stream object as returned by [`open()`](https://docs.python.org/3/library/functions.html#open "open"). Reading from the stream provides output from the child process. If the _encoding_ or _errors_ arguments were specified or the _text_ or _universal_newlines_ argument was `True`, the stream is a text stream, otherwise it is a byte stream. If the _stdout_ argument was not `PIPE`, this attribute is `None`.

Popen.stderr[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stderr "Link to this definition")

If the _stderr_ argument was [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"), this attribute is a readable stream object as returned by [`open()`](https://docs.python.org/3/library/functions.html#open "open"). Reading from the stream provides error output from the child process. If the _encoding_ or _errors_ arguments were specified or the _text_ or _universal_newlines_ argument was `True`, the stream is a text stream, otherwise it is a byte stream. If the _stderr_ argument was not `PIPE`, this attribute is `None`.
Warning
Use [`communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") rather than [`.stdin.write`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stdin "subprocess.Popen.stdin"), [`.stdout.read`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stdout "subprocess.Popen.stdout") or [`.stderr.read`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stderr "subprocess.Popen.stderr") to avoid deadlocks due to any of the other OS pipe buffers filling up and blocking the child process.

Popen.pid[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.pid "Link to this definition")

The process ID of the child process.
Note that if you set the _shell_ argument to `True`, this is the process ID of the spawned shell.

Popen.returncode[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "Link to this definition")

The child return code. Initially `None`, [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode") is set by a call to the [`poll()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.poll "subprocess.Popen.poll"), [`wait()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "subprocess.Popen.wait"), or [`communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") methods if they detect that the process has terminated.
A `None` value indicates that the process hadn’t yet terminated at the time of the last method call.
A negative value `-N` indicates that the child was terminated by signal `N` (POSIX only).
## Windows Popen Helpers[¶](https://docs.python.org/3/library/subprocess.html#windows-popen-helpers "Link to this heading")
The [`STARTUPINFO`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO "subprocess.STARTUPINFO") class and following constants are only available on Windows.

_class_ subprocess.STARTUPINFO(_*_ , _dwFlags =0_, _hStdInput =None_, _hStdOutput =None_, _hStdError =None_, _wShowWindow =0_, _lpAttributeList =None_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO "Link to this definition")

Partial support of the Windows [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") creation. The following attributes can be set by passing them as keyword-only arguments.
Changed in version 3.7: Keyword-only argument support was added.

dwFlags[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "Link to this definition")

A bit field that determines whether certain `STARTUPINFO` attributes are used when the process creates a window.
Copy```
si = subprocess.STARTUPINFO()
si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW

```


hStdInput[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.hStdInput "Link to this definition")

If [`dwFlags`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESTDHANDLES`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_USESTDHANDLES "subprocess.STARTF_USESTDHANDLES"), this attribute is the standard input handle for the process. If `STARTF_USESTDHANDLES` is not specified, the default for standard input is the keyboard buffer.

hStdOutput[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.hStdOutput "Link to this definition")

If [`dwFlags`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESTDHANDLES`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_USESTDHANDLES "subprocess.STARTF_USESTDHANDLES"), this attribute is the standard output handle for the process. Otherwise, this attribute is ignored and the default for standard output is the console window’s buffer.

hStdError[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.hStdError "Link to this definition")

If [`dwFlags`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESTDHANDLES`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_USESTDHANDLES "subprocess.STARTF_USESTDHANDLES"), this attribute is the standard error handle for the process. Otherwise, this attribute is ignored and the default for standard error is the console window’s buffer.

wShowWindow[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.wShowWindow "Link to this definition")

If [`dwFlags`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESHOWWINDOW`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_USESHOWWINDOW "subprocess.STARTF_USESHOWWINDOW"), this attribute can be any of the values that can be specified in the `nCmdShow` parameter for the `SW_SHOWDEFAULT`. Otherwise, this attribute is ignored.
[`SW_HIDE`](https://docs.python.org/3/library/subprocess.html#subprocess.SW_HIDE "subprocess.SW_HIDE") is provided for this attribute. It is used when [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") is called with `shell=True`.

lpAttributeList[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.lpAttributeList "Link to this definition")

A dictionary of additional attributes for process creation as given in `STARTUPINFOEX`, see
Supported attributes:

**handle_list**

Sequence of handles that will be inherited. _close_fds_ must be true if non-empty.
The handles must be temporarily made inheritable by [`os.set_handle_inheritable()`](https://docs.python.org/3/library/os.html#os.set_handle_inheritable "os.set_handle_inheritable") when passed to the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") constructor, else [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised with Windows error `ERROR_INVALID_PARAMETER` (87).
Warning
In a multithreaded process, use caution to avoid leaking handles that are marked inheritable when combining this feature with concurrent calls to other process creation functions that inherit all handles such as [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system"). This also applies to standard handle redirection, which temporarily creates inheritable handles.
Added in version 3.7.
### Windows Constants[¶](https://docs.python.org/3/library/subprocess.html#windows-constants "Link to this heading")
The `subprocess` module exposes the following constants.

subprocess.STD_INPUT_HANDLE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STD_INPUT_HANDLE "Link to this definition")

The standard input device. Initially, this is the console input buffer, `CONIN$`.

subprocess.STD_OUTPUT_HANDLE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STD_OUTPUT_HANDLE "Link to this definition")

The standard output device. Initially, this is the active console screen buffer, `CONOUT$`.

subprocess.STD_ERROR_HANDLE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STD_ERROR_HANDLE "Link to this definition")

The standard error device. Initially, this is the active console screen buffer, `CONOUT$`.

subprocess.SW_HIDE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.SW_HIDE "Link to this definition")

Hides the window. Another window will be activated.

subprocess.STARTF_USESTDHANDLES[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_USESTDHANDLES "Link to this definition")

Specifies that the [`STARTUPINFO.hStdInput`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.hStdInput "subprocess.STARTUPINFO.hStdInput"), [`STARTUPINFO.hStdOutput`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.hStdOutput "subprocess.STARTUPINFO.hStdOutput"), and [`STARTUPINFO.hStdError`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.hStdError "subprocess.STARTUPINFO.hStdError") attributes contain additional information.

subprocess.STARTF_USESHOWWINDOW[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_USESHOWWINDOW "Link to this definition")

Specifies that the [`STARTUPINFO.wShowWindow`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.wShowWindow "subprocess.STARTUPINFO.wShowWindow") attribute contains additional information.

subprocess.STARTF_FORCEONFEEDBACK[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_FORCEONFEEDBACK "Link to this definition")

A [`STARTUPINFO.dwFlags`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") parameter to specify that the _Working in Background_ mouse cursor will be displayed while a process is launching. This is the default behavior for GUI processes.
Added in version 3.13.

subprocess.STARTF_FORCEOFFFEEDBACK[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STARTF_FORCEOFFFEEDBACK "Link to this definition")

A [`STARTUPINFO.dwFlags`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") parameter to specify that the mouse cursor will not be changed when launching a process.
Added in version 3.13.

subprocess.CREATE_NEW_CONSOLE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NEW_CONSOLE "Link to this definition")

The new process has a new console, instead of inheriting its parent’s console (the default).

subprocess.CREATE_NEW_PROCESS_GROUP[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NEW_PROCESS_GROUP "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process group will be created. This flag is necessary for using [`os.kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill") on the subprocess.
This flag is ignored if [`CREATE_NEW_CONSOLE`](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NEW_CONSOLE "subprocess.CREATE_NEW_CONSOLE") is specified.

subprocess.ABOVE_NORMAL_PRIORITY_CLASS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.ABOVE_NORMAL_PRIORITY_CLASS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have an above average priority.
Added in version 3.7.

subprocess.BELOW_NORMAL_PRIORITY_CLASS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.BELOW_NORMAL_PRIORITY_CLASS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have a below average priority.
Added in version 3.7.

subprocess.HIGH_PRIORITY_CLASS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.HIGH_PRIORITY_CLASS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have a high priority.
Added in version 3.7.

subprocess.IDLE_PRIORITY_CLASS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.IDLE_PRIORITY_CLASS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have an idle (lowest) priority.
Added in version 3.7.

subprocess.NORMAL_PRIORITY_CLASS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.NORMAL_PRIORITY_CLASS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have a normal priority. (default)
Added in version 3.7.

subprocess.REALTIME_PRIORITY_CLASS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.REALTIME_PRIORITY_CLASS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have realtime priority. You should almost never use REALTIME_PRIORITY_CLASS, because this interrupts system threads that manage mouse input, keyboard input, and background disk flushing. This class can be appropriate for applications that “talk” directly to hardware or that perform brief tasks that should have limited interruptions.
Added in version 3.7.

subprocess.CREATE_NO_WINDOW[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NO_WINDOW "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will not create a window.
Added in version 3.7.

subprocess.DETACHED_PROCESS[¶](https://docs.python.org/3/library/subprocess.html#subprocess.DETACHED_PROCESS "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will not inherit its parent’s console. This value cannot be used with CREATE_NEW_CONSOLE.
Added in version 3.7.

subprocess.CREATE_DEFAULT_ERROR_MODE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_DEFAULT_ERROR_MODE "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process does not inherit the error mode of the calling process. Instead, the new process gets the default error mode. This feature is particularly useful for multithreaded shell applications that run with hard errors disabled.
Added in version 3.7.

subprocess.CREATE_BREAKAWAY_FROM_JOB[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_BREAKAWAY_FROM_JOB "Link to this definition")

A [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process is not associated with the job.
Added in version 3.7.
