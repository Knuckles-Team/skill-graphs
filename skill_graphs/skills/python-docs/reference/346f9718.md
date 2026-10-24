Added in version 3.3.
Changed in version 3.9: Added `CLD_KILLED` and `CLD_STOPPED` values.

os.waitstatus_to_exitcode(_status_)[¶](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "Link to this definition")

Convert a wait status to an exit code.
On Unix:
  * If the process exited normally (if `WIFEXITED(status)` is true), return the process exit status (return `WEXITSTATUS(status)`): result greater than or equal to 0.
  * If the process was terminated by a signal (if `WIFSIGNALED(status)` is true), return `-signum` where _signum_ is the number of the signal that caused the process to terminate (return `-WTERMSIG(status)`): result less than 0.
  * Otherwise, raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").


On Windows, return _status_ shifted right by 8 bits.
On Unix, if the process is being traced or if [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") was called with [`WUNTRACED`](https://docs.python.org/3/library/os.html#os.WUNTRACED "os.WUNTRACED") option, the caller must first check if `WIFSTOPPED(status)` is true. This function must not be called if `WIFSTOPPED(status)` is true.
See also
[`WIFEXITED()`](https://docs.python.org/3/library/os.html#os.WIFEXITED "os.WIFEXITED"), [`WEXITSTATUS()`](https://docs.python.org/3/library/os.html#os.WEXITSTATUS "os.WEXITSTATUS"), [`WIFSIGNALED()`](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "os.WIFSIGNALED"), [`WTERMSIG()`](https://docs.python.org/3/library/os.html#os.WTERMSIG "os.WTERMSIG"), [`WIFSTOPPED()`](https://docs.python.org/3/library/os.html#os.WIFSTOPPED "os.WIFSTOPPED"), [`WSTOPSIG()`](https://docs.python.org/3/library/os.html#os.WSTOPSIG "os.WSTOPSIG") functions.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.
Added in version 3.9.
The following functions take a process status code as returned by [`system()`](https://docs.python.org/3/library/os.html#os.system "os.system"), [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait"), or [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") as a parameter. They may be used to determine the disposition of a process.

os.WCOREDUMP(_status_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.WCOREDUMP "Link to this definition")

Return `True` if a core dump was generated for the process, otherwise return `False`.
This function should be employed only if [`WIFSIGNALED()`](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "os.WIFSIGNALED") is true.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WIFCONTINUED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFCONTINUED "Link to this definition")

Return `True` if a stopped child has been resumed by delivery of [`SIGCONT`](https://docs.python.org/3/library/signal.html#signal.SIGCONT "signal.SIGCONT") (if the process has been continued from a job control stop), otherwise return `False`.
See [`WCONTINUED`](https://docs.python.org/3/library/os.html#os.WCONTINUED "os.WCONTINUED") option.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WIFSTOPPED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFSTOPPED "Link to this definition")

Return `True` if the process was stopped by delivery of a signal, otherwise return `False`.
`WIFSTOPPED()` only returns `True` if the [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") call was done using [`WUNTRACED`](https://docs.python.org/3/library/os.html#os.WUNTRACED "os.WUNTRACED") option or when the process is being traced (see
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WIFSIGNALED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "Link to this definition")

Return `True` if the process was terminated by a signal, otherwise return `False`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WIFEXITED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFEXITED "Link to this definition")

Return `True` if the process exited terminated normally, that is, by calling `exit()` or `_exit()`, or by returning from `main()`; otherwise return `False`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WEXITSTATUS(_status_)[¶](https://docs.python.org/3/library/os.html#os.WEXITSTATUS "Link to this definition")

Return the process exit status.
This function should be employed only if [`WIFEXITED()`](https://docs.python.org/3/library/os.html#os.WIFEXITED "os.WIFEXITED") is true.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WSTOPSIG(_status_)[¶](https://docs.python.org/3/library/os.html#os.WSTOPSIG "Link to this definition")

Return the signal which caused the process to stop.
This function should be employed only if [`WIFSTOPPED()`](https://docs.python.org/3/library/os.html#os.WIFSTOPPED "os.WIFSTOPPED") is true.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.

os.WTERMSIG(_status_)[¶](https://docs.python.org/3/library/os.html#os.WTERMSIG "Link to this definition")

Return the number of the signal that caused the process to terminate.
This function should be employed only if [`WIFSIGNALED()`](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "os.WIFSIGNALED") is true.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
