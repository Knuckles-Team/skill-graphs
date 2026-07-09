#  `subprocess` — Subprocess management[¶](https://docs.python.org/3/library/subprocess.html#module-subprocess "Link to this heading")
**Source code:**
* * *
The `subprocess` module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:
Copy```
os.system
os.spawn*

```

Information about how the `subprocess` module can be used to replace these modules and functions can be found in the following sections.
See also
[**PEP 324**](https://peps.python.org/pep-0324/) – PEP proposing the subprocess module
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
## Using the `subprocess` Module[¶](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module "Link to this heading")
The recommended approach to invoking subprocesses is to use the [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") function for all use cases it can handle. For more advanced use cases, the underlying [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") interface can be used directly.

subprocess.run(_args_ , _*_ , _stdin =None_, _input =None_, _stdout =None_, _stderr =None_, _capture_output =False_, _shell =False_, _cwd =None_, _timeout =None_, _check =False_, _encoding =None_, _errors =None_, _text =None_, _env =None_, _universal_newlines =None_, _** other_popen_kwargs_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.run "Link to this definition")

Run the command described by _args_. Wait for command to complete, then return a [`CompletedProcess`](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess "subprocess.CompletedProcess") instance.
The arguments shown above are merely the most common ones, described below in [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments) (hence the use of keyword-only notation in the abbreviated signature). The full function signature is largely the same as that of the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") constructor - most of the arguments to this function are passed through to that interface. (_timeout_ , _input_ , _check_ , and _capture_output_ are not.)
If _capture_output_ is true, stdout and stderr will be captured. When used, the internal [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") object is automatically created with _stdout_ and _stderr_ both set to [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"). The _stdout_ and _stderr_ arguments may not be supplied at the same time as _capture_output_. If you wish to capture and combine both streams into one, set _stdout_ to `PIPE` and _stderr_ to [`STDOUT`](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "subprocess.STDOUT"), instead of using _capture_output_.
A _timeout_ may be specified in seconds, it is internally passed on to [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate"). If the timeout expires, the child process will be killed and waited for. The [`TimeoutExpired`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exception will be re-raised after the child process has terminated. The initial process creation itself cannot be interrupted on many platform APIs so you are not guaranteed to see a timeout exception until at least after however long process creation takes.
The _input_ argument is passed to [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") and thus to the subprocess’s stdin. If used it must be a byte sequence, or a string if _encoding_ or _errors_ is specified or _text_ is true. When used, the internal [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") object is automatically created with _stdin_ set to [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"), and the _stdin_ argument may not be used as well.
If _check_ is true, and the process exits with a non-zero exit code, a [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "subprocess.CalledProcessError") exception will be raised. Attributes of that exception hold the arguments, the exit code, and stdout and stderr if they were captured.
If _encoding_ or _errors_ are specified, or _text_ is true, file objects for stdin, stdout and stderr are opened in text mode using the specified _encoding_ and _errors_ or the [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") default. The _universal_newlines_ argument is equivalent to _text_ and is provided for backwards compatibility. By default, file objects are opened in binary mode.
If _env_ is not `None`, it must be a mapping that defines the environment variables for the new process; these are used instead of the default behavior of inheriting the current process’ environment. It is passed directly to [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen"). This mapping can be str to str on any platform or bytes to bytes on POSIX platforms much like [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") or [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb").
Examples:
Copy```
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')

```

Added in version 3.5.
Changed in version 3.6: Added _encoding_ and _errors_ parameters
Changed in version 3.7: Added the _text_ parameter, as a more understandable alias of _universal_newlines_. Added the _capture_output_ parameter.
Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

_class_ subprocess.CompletedProcess[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess "Link to this definition")

The return value from [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run"), representing a process that has finished.

args[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.args "Link to this definition")

The arguments used to launch the process. This may be a list or a string.

returncode[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.returncode "Link to this definition")

Exit status of the child process. Typically, an exit status of 0 indicates that it ran successfully.
A negative value `-N` indicates that the child was terminated by signal `N` (POSIX only).

stdout[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.stdout "Link to this definition")

Captured stdout from the child process. A bytes sequence, or a string if [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") was called with an encoding, errors, or text=True. `None` if stdout was not captured.
If you ran the process with `stderr=subprocess.STDOUT`, stdout and stderr will be combined in this attribute, and [`stderr`](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.stderr "subprocess.CompletedProcess.stderr") will be `None`.

stderr[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.stderr "Link to this definition")

Captured stderr from the child process. A bytes sequence, or a string if [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") was called with an encoding, errors, or text=True. `None` if stderr was not captured.

check_returncode()[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.check_returncode "Link to this definition")

If [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess.returncode "subprocess.CompletedProcess.returncode") is non-zero, raise a [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "subprocess.CalledProcessError").
Added in version 3.5.

subprocess.DEVNULL[¶](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "Link to this definition")

Special value that can be used as the _stdin_ , _stdout_ or _stderr_ argument to [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") and indicates that the special file [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull") will be used.
Added in version 3.3.

subprocess.PIPE[¶](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "Link to this definition")

Special value that can be used as the _stdin_ , _stdout_ or _stderr_ argument to [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") and indicates that a pipe to the standard stream should be opened. Most useful with [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate").

subprocess.STDOUT[¶](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "Link to this definition")

Special value that can be used as the _stderr_ argument to [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") and indicates that standard error should go into the same handle as standard output.

_exception_ subprocess.SubprocessError[¶](https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError "Link to this definition")

Base class for all other exceptions from this module.
Added in version 3.3.

_exception_ subprocess.TimeoutExpired[¶](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "Link to this definition")

Subclass of [`SubprocessError`](https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError "subprocess.SubprocessError"), raised when a timeout expires while waiting for a child process.

cmd[¶](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired.cmd "Link to this definition")

Command that was used to spawn the child process.

timeout[¶](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired.timeout "Link to this definition")

Timeout in seconds.

output[¶](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired.output "Link to this definition")

Output of the child process if it was captured by [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") or [`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output"). Otherwise, `None`. This is always [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") when any output was captured regardless of the `text=True` setting. It may remain `None` instead of `b''` when no output was observed.

stdout[¶](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired.stdout "Link to this definition")

Alias for output, for symmetry with [`stderr`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired.stderr "subprocess.TimeoutExpired.stderr").

stderr[¶](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired.stderr "Link to this definition")

Stderr output of the child process if it was captured by [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run"). Otherwise, `None`. This is always [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") when stderr output was captured regardless of the `text=True` setting. It may remain `None` instead of `b''` when no stderr output was observed.
Added in version 3.3.
Changed in version 3.5: _stdout_ and _stderr_ attributes added

_exception_ subprocess.CalledProcessError[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "Link to this definition")

Subclass of [`SubprocessError`](https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError "subprocess.SubprocessError"), raised when a process run by [`check_call()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_call "subprocess.check_call"), [`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output"), or [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") (with `check=True`) returns a non-zero exit status.

returncode[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.returncode "Link to this definition")

Exit status of the child process. If the process exited due to a signal, this will be the negative signal number.

cmd[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.cmd "Link to this definition")

Command that was used to spawn the child process.

output[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.output "Link to this definition")

Output of the child process if it was captured by [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") or [`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output"). Otherwise, `None`.

stdout[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.stdout "Link to this definition")

Alias for output, for symmetry with [`stderr`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.stderr "subprocess.CalledProcessError.stderr").

stderr[¶](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.stderr "Link to this definition")

Stderr output of the child process if it was captured by [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run"). Otherwise, `None`.
Changed in version 3.5: _stdout_ and _stderr_ attributes added
### Frequently Used Arguments[¶](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments "Link to this heading")
To support a wide variety of use cases, the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") constructor (and the convenience functions) accept a large number of optional arguments. For most typical use cases, many of these arguments can be safely left at their default values. The arguments that are most commonly needed are:
> _args_ is required for all calls and should be a string, or a sequence of program arguments. Providing a sequence of arguments is generally preferred, as it allows the module to take care of any required escaping and quoting of arguments (e.g. to permit spaces in file names). If passing a single string, either _shell_ must be [`True`](https://docs.python.org/3/library/constants.html#True "True") (see below) or else the string must simply name the program to be executed without specifying any arguments.
> _stdin_ , _stdout_ and _stderr_ specify the executed program’s standard input, standard output and standard error file handles, respectively. Valid values are `None`, [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"), [`DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL"), an existing file descriptor (a positive integer), and an existing [file object](https://docs.python.org/3/glossary.html#term-file-object) with a valid file descriptor. With the default settings of `None`, no redirection will occur. `PIPE` indicates that a new pipe to the child should be created. `DEVNULL` indicates that the special file [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull") will be used. Additionally, _stderr_ can be [`STDOUT`](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "subprocess.STDOUT"), which indicates that the stderr data from the child process should be captured into the same file handle as for _stdout_.
> If _encoding_ or _errors_ are specified, or _text_ (also known as _universal_newlines_) is true, the file objects _stdin_ , _stdout_ and _stderr_ will be opened in text mode using the _encoding_ and _errors_ specified in the call or the defaults for [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper").
> For _stdin_ , line ending characters `'\n'` in the input will be converted to the default line separator [`os.linesep`](https://docs.python.org/3/library/os.html#os.linesep "os.linesep"). For _stdout_ and _stderr_ , all line endings in the output will be converted to `'\n'`. For more information see the documentation of the [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") class when the _newline_ argument to its constructor is `None`.
> If text mode is not used, _stdin_ , _stdout_ and _stderr_ will be opened as binary streams. No encoding or line ending conversion is performed.
> Changed in version 3.6: Added the _encoding_ and _errors_ parameters.
> Changed in version 3.7: Added the _text_ parameter as an alias for _universal_newlines_.
> Note
> The newlines attribute of the file objects [`Popen.stdin`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stdin "subprocess.Popen.stdin"), [`Popen.stdout`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stdout "subprocess.Popen.stdout") and [`Popen.stderr`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stderr "subprocess.Popen.stderr") are not updated by the [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") method.
> If _shell_ is `True`, the specified command will be executed through the shell. This can be useful if you are using Python primarily for the enhanced control flow it offers over most system shells and still want convenient access to other shell features such as shell pipes, filename wildcards, environment variable expansion, and expansion of `~` to a user’s home directory. However, note that Python itself offers implementations of many shell-like features (in particular, [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion."), [`fnmatch`](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching."), [`os.walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk"), [`os.path.expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars"), [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser"), and [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")).
> Changed in version 3.3: When _universal_newlines_ is `True`, the class uses the encoding [`locale.getpreferredencoding(False)`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding") instead of `locale.getpreferredencoding()`. See the [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") class for more information on this change.
> Note
> Read the [Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations) section before using `shell=True`.
These options, along with all of the other options, are described in more detail in the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") constructor documentation.
### Popen Constructor[¶](https://docs.python.org/3/library/subprocess.html#popen-constructor "Link to this heading")
The underlying process creation and management in this module is handled by the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") class. It offers a lot of flexibility so that developers are able to handle the less common cases not covered by the convenience functions.

_class_ subprocess.Popen(_args_ , _bufsize =-1_, _executable =None_, _stdin =None_, _stdout =None_, _stderr =None_, _preexec_fn =None_, _close_fds =True_, _shell =False_, _cwd =None_, _env =None_, _universal_newlines =None_, _startupinfo =None_, _creationflags =0_, _restore_signals =True_, _start_new_session =False_, _pass_fds =()_, _*_ , _group =None_, _extra_groups =None_, _user =None_, _umask =-1_, _encoding =None_, _errors =None_, _text =None_, _pipesize =-1_, _process_group =None_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "Link to this definition")

Execute a child program in a new process. On POSIX, the class uses [`os.execvpe()`](https://docs.python.org/3/library/os.html#os.execvpe "os.execvpe")-like behavior to execute the child program. On Windows, the class uses the Windows `CreateProcess()` function. The arguments to `Popen` are as follows.
_args_ should be a sequence of program arguments or else a single string or [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). By default, the program to execute is the first item in _args_ if _args_ is a sequence. If _args_ is a string, the interpretation is platform-dependent and described below. See the _shell_ and _executable_ arguments for additional differences from the default behavior. Unless otherwise stated, it is recommended to pass _args_ as a sequence.
Warning
For maximum reliability, use a fully qualified path for the executable. To search for an unqualified name on `PATH`, use [`shutil.which()`](https://docs.python.org/3/library/shutil.html#shutil.which "shutil.which"). On all platforms, passing [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable") is the recommended way to launch the current Python interpreter again, and use the `-m` command-line format to launch an installed module.
Resolving the path of _executable_ (or the first item of _args_) is platform dependent. For POSIX, see [`os.execvpe()`](https://docs.python.org/3/library/os.html#os.execvpe "os.execvpe"), and note that when resolving or searching for the executable path, _cwd_ overrides the current working directory and _env_ can override the `PATH` environment variable. For Windows, see the documentation of the `lpApplicationName` and `lpCommandLine` parameters of WinAPI `CreateProcess`, and note that when resolving or searching for the executable path with `shell=False`, _cwd_ does not override the current working directory and _env_ cannot override the `PATH` environment variable. Using a full path avoids all of these variations.
An example of passing some arguments to an external program as a sequence is:
Copy```
Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])

```

On POSIX, if _args_ is a string, the string is interpreted as the name or path of the program to execute. However, this can only be done if not passing arguments to the program.
Note
It may not be obvious how to break a shell command into a sequence of arguments, especially in complex cases. [`shlex.split()`](https://docs.python.org/3/library/shlex.html#shlex.split "shlex.split") can illustrate how to determine the correct tokenization for _args_ :
Copy```
>>> import shlex, subprocess
>>> command_line = input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print(args)
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args) # Success!

```

Note in particular that options (such as _-input_) and arguments (such as _eggs.txt_) that are separated by whitespace in the shell go in separate list elements, while arguments that need quoting or backslash escaping when used in the shell (such as filenames containing spaces or the _echo_ command shown above) are single list elements.
On Windows, if _args_ is a sequence, it will be converted to a string in a manner described in [Converting an argument sequence to a string on Windows](https://docs.python.org/3/library/subprocess.html#converting-argument-sequence). This is because the underlying `CreateProcess()` operates on strings.
Changed in version 3.6: _args_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) if _shell_ is `False` and a sequence containing path-like objects on POSIX.
Changed in version 3.8: _args_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) if _shell_ is `False` and a sequence containing bytes and path-like objects on Windows.
The _shell_ argument (which defaults to `False`) specifies whether to use the shell as the program to execute. If _shell_ is `True`, it is recommended to pass _args_ as a string rather than as a sequence.
On POSIX with `shell=True`, the shell defaults to `/bin/sh`. If _args_ is a string, the string specifies the command to execute through the shell. This means that the string must be formatted exactly as it would be when typed at the shell prompt. This includes, for example, quoting or backslash escaping filenames with spaces in them. If _args_ is a sequence, the first item specifies the command string, and any additional items will be treated as additional arguments to the shell itself. That is to say, `Popen` does the equivalent of:
Copy```
Popen(['/bin/sh', '-c', args[0], args[1], ...])

```

On Windows with `shell=True`, the `COMSPEC` environment variable specifies the default shell. The only time you need to specify `shell=True` on Windows is when the command you wish to execute is built into the shell (e.g. **dir** or **copy**). You do not need `shell=True` to run a batch file or console-based executable.
Note
Read the [Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations) section before using `shell=True`.
_bufsize_ will be supplied as the corresponding argument to the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function when creating the stdin/stdout/stderr pipe file objects:
  * `0` means unbuffered (read and write are one system call and can return short)
  * `1` means line buffered (only usable if `text=True` or `universal_newlines=True`)
  * any other positive value means use a buffer of approximately that size
  * negative bufsize (the default) means the system default of io.DEFAULT_BUFFER_SIZE will be used.


Changed in version 3.3.1: _bufsize_ now defaults to -1 to enable buffering by default to match the behavior that most code expects. In versions prior to Python 3.2.4 and 3.3.1 it incorrectly defaulted to `0` which was unbuffered and allowed short reads. This was unintentional and did not match the behavior of Python 2 as most code expected.
The _executable_ argument specifies a replacement program to execute. It is very seldom needed. When `shell=False`, _executable_ replaces the program to execute specified by _args_. However, the original _args_ is still passed to the program. Most programs treat the program specified by _args_ as the command name, which can then be different from the program actually executed. On POSIX, the _args_ name becomes the display name for the executable in utilities such as **ps**. If `shell=True`, on POSIX the _executable_ argument specifies a replacement shell for the default `/bin/sh`.
Changed in version 3.6: _executable_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) on POSIX.
Changed in version 3.8: _executable_ parameter accepts a bytes and [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) on Windows.
Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.
_stdin_ , _stdout_ and _stderr_ specify the executed program’s standard input, standard output and standard error file handles, respectively. Valid values are `None`, [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE"), [`DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL"), an existing file descriptor (a positive integer), and an existing [file object](https://docs.python.org/3/glossary.html#term-file-object) with a valid file descriptor. With the default settings of `None`, no redirection will occur. `PIPE` indicates that a new pipe to the child should be created. `DEVNULL` indicates that the special file [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull") will be used. Additionally, _stderr_ can be [`STDOUT`](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "subprocess.STDOUT"), which indicates that the stderr data from the applications should be captured into the same file handle as for _stdout_.
If _preexec_fn_ is set to a callable object, this object will be called in the child process just before the child is executed. (POSIX only)
Warning
The _preexec_fn_ parameter is NOT SAFE to use in the presence of threads in your application. The child process could deadlock before exec is called.
Note
If you need to modify the environment for the child use the _env_ parameter rather than doing it in a _preexec_fn_. The _start_new_session_ and _process_group_ parameters should take the place of code using _preexec_fn_ to call [`os.setsid()`](https://docs.python.org/3/library/os.html#os.setsid "os.setsid") or [`os.setpgid()`](https://docs.python.org/3/library/os.html#os.setpgid "os.setpgid") in the child.
Changed in version 3.8: The _preexec_fn_ parameter is no longer supported in subinterpreters. The use of the parameter in a subinterpreter raises [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"). The new restriction may affect applications that are deployed in mod_wsgi, uWSGI, and other embedded environments.
If _close_fds_ is true, all file descriptors except `0`, `1` and `2` will be closed before the child process is executed. Otherwise when _close_fds_ is false, file descriptors obey their inheritable flag as described in [Inheritance of File Descriptors](https://docs.python.org/3/library/os.html#fd-inheritance).
On Windows, if _close_fds_ is true then no handles will be inherited by the child process unless explicitly passed in the `handle_list` element of [`STARTUPINFO.lpAttributeList`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO.lpAttributeList "subprocess.STARTUPINFO.lpAttributeList"), or by standard handle redirection.
Changed in version 3.2: The default for _close_fds_ was changed from [`False`](https://docs.python.org/3/library/constants.html#False "False") to what is described above.
Changed in version 3.7: On Windows the default for _close_fds_ was changed from [`False`](https://docs.python.org/3/library/constants.html#False "False") to [`True`](https://docs.python.org/3/library/constants.html#True "True") when redirecting the standard handles. It’s now possible to set _close_fds_ to `True` when redirecting the standard handles.
_pass_fds_ is an optional sequence of file descriptors to keep open between the parent and child. Providing any _pass_fds_ forces _close_fds_ to be [`True`](https://docs.python.org/3/library/constants.html#True "True"). (POSIX only)
Changed in version 3.2: The _pass_fds_ parameter was added.
If _cwd_ is not `None`, the function changes the working directory to _cwd_ before executing the child. _cwd_ can be a string, bytes or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object) object. On POSIX, the function looks for _executable_ (or for the first item in _args_) relative to _cwd_ if the executable path is a relative path.
Changed in version 3.6: _cwd_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) on POSIX.
Changed in version 3.7: _cwd_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) on Windows.
Changed in version 3.8: _cwd_ parameter accepts a bytes object on Windows.
If _restore_signals_ is true (the default) all signals that Python has set to SIG_IGN are restored to SIG_DFL in the child process before the exec. Currently this includes the SIGPIPE, SIGXFZ and SIGXFSZ signals. (POSIX only)
Changed in version 3.2: _restore_signals_ was added.
If _start_new_session_ is true the `setsid()` system call will be made in the child process prior to the execution of the subprocess.
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX
Changed in version 3.2: _start_new_session_ was added.
If _process_group_ is a non-negative integer, the `setpgid(0, value)` system call will be made in the child process prior to the execution of the subprocess.
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX
Changed in version 3.11: _process_group_ was added.
If _group_ is not `None`, the setregid() system call will be made in the child process prior to the execution of the subprocess. If the provided value is a string, it will be looked up via [`grp.getgrnam()`](https://docs.python.org/3/library/grp.html#grp.getgrnam "grp.getgrnam") and the value in `gr_gid` will be used. If the value is an integer, it will be passed verbatim. (POSIX only)
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX
Added in version 3.9.
If _extra_groups_ is not `None`, the setgroups() system call will be made in the child process prior to the execution of the subprocess. Strings provided in _extra_groups_ will be looked up via [`grp.getgrnam()`](https://docs.python.org/3/library/grp.html#grp.getgrnam "grp.getgrnam") and the values in `gr_gid` will be used. Integer values will be passed verbatim. (POSIX only)
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX
Added in version 3.9.
If _user_ is not `None`, the setreuid() system call will be made in the child process prior to the execution of the subprocess. If the provided value is a string, it will be looked up via [`pwd.getpwnam()`](https://docs.python.org/3/library/pwd.html#pwd.getpwnam "pwd.getpwnam") and the value in `pw_uid` will be used. If the value is an integer, it will be passed verbatim. (POSIX only)
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX
Added in version 3.9.
If _umask_ is not negative, the umask() system call will be made in the child process prior to the execution of the subprocess.
[Availability](https://docs.python.org/3/library/intro.html#availability): POSIX
Added in version 3.9.
If _env_ is not `None`, it must be a mapping that defines the environment variables for the new process; these are used instead of the default behavior of inheriting the current process’ environment. This mapping can be str to str on any platform or bytes to bytes on POSIX platforms much like [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") or [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb").
Note
If specified, _env_ must provide any variables required for the program to execute. On Windows, in order to run a _env_ **must** include a valid `%SystemRoot%`.
If _encoding_ or _errors_ are specified, or _text_ is true, the file objects _stdin_ , _stdout_ and _stderr_ are opened in text mode with the specified _encoding_ and _errors_ , as described above in [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments). The _universal_newlines_ argument is equivalent to _text_ and is provided for backwards compatibility. By default, file objects are opened in binary mode.
Added in version 3.6: _encoding_ and _errors_ were added.
Added in version 3.7: _text_ was added as a more readable alias for _universal_newlines_.
If given, _startupinfo_ will be a [`STARTUPINFO`](https://docs.python.org/3/library/subprocess.html#subprocess.STARTUPINFO "subprocess.STARTUPINFO") object, which is passed to the underlying `CreateProcess` function.
If given, _creationflags_ , can be one or more of the following flags:
  * [`CREATE_NEW_CONSOLE`](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NEW_CONSOLE "subprocess.CREATE_NEW_CONSOLE")
  * [`CREATE_NEW_PROCESS_GROUP`](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NEW_PROCESS_GROUP "subprocess.CREATE_NEW_PROCESS_GROUP")
  * [`ABOVE_NORMAL_PRIORITY_CLASS`](https://docs.python.org/3/library/subprocess.html#subprocess.ABOVE_NORMAL_PRIORITY_CLASS "subprocess.ABOVE_NORMAL_PRIORITY_CLASS")
  * [`BELOW_NORMAL_PRIORITY_CLASS`](https://docs.python.org/3/library/subprocess.html#subprocess.BELOW_NORMAL_PRIORITY_CLASS "subprocess.BELOW_NORMAL_PRIORITY_CLASS")
  * [`HIGH_PRIORITY_CLASS`](https://docs.python.org/3/library/subprocess.html#subprocess.HIGH_PRIORITY_CLASS "subprocess.HIGH_PRIORITY_CLASS")
  * [`IDLE_PRIORITY_CLASS`](https://docs.python.org/3/library/subprocess.html#subprocess.IDLE_PRIORITY_CLASS "subprocess.IDLE_PRIORITY_CLASS")
  * [`NORMAL_PRIORITY_CLASS`](https://docs.python.org/3/library/subprocess.html#subprocess.NORMAL_PRIORITY_CLASS "subprocess.NORMAL_PRIORITY_CLASS")
  * [`REALTIME_PRIORITY_CLASS`](https://docs.python.org/3/library/subprocess.html#subprocess.REALTIME_PRIORITY_CLASS "subprocess.REALTIME_PRIORITY_CLASS")
  * [`CREATE_NO_WINDOW`](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_NO_WINDOW "subprocess.CREATE_NO_WINDOW")
  * [`DETACHED_PROCESS`](https://docs.python.org/3/library/subprocess.html#subprocess.DETACHED_PROCESS "subprocess.DETACHED_PROCESS")
  * [`CREATE_DEFAULT_ERROR_MODE`](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_DEFAULT_ERROR_MODE "subprocess.CREATE_DEFAULT_ERROR_MODE")
  * [`CREATE_BREAKAWAY_FROM_JOB`](https://docs.python.org/3/library/subprocess.html#subprocess.CREATE_BREAKAWAY_FROM_JOB "subprocess.CREATE_BREAKAWAY_FROM_JOB")


_pipesize_ can be used to change the size of the pipe when [`PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE") is used for _stdin_ , _stdout_ or _stderr_. The size of the pipe is only changed on platforms that support this (only Linux at this time of writing). Other platforms will ignore this parameter.
Changed in version 3.10: Added the _pipesize_ parameter.
Popen objects are supported as context managers via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement: on exit, standard file descriptors are closed, and the process is waited for.
Copy```
with Popen(["ifconfig"], stdout=PIPE) as proc:
    log.write(proc.stdout.read())

```

Popen and the other functions in this module that use it raise an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `subprocess.Popen` with arguments `executable`, `args`, `cwd`, and `env`. The value for `args` may be a single string or a list of strings, depending on platform.
Changed in version 3.2: Added context manager support.
Changed in version 3.6: Popen destructor now emits a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") warning if the child process is still running.
Changed in version 3.8: Popen can use [`os.posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn") in some cases for better performance. On Windows Subsystem for Linux and QEMU User Emulation, Popen constructor using `os.posix_spawn()` no longer raise an exception on errors like missing program, but the child process fails with a non-zero [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode").
### Exceptions[¶](https://docs.python.org/3/library/subprocess.html#exceptions "Link to this heading")
Exceptions raised in the child process, before the new program has started to execute, will be re-raised in the parent.
The most common exception raised is [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). This occurs, for example, when trying to execute a non-existent file. Applications should prepare for `OSError` exceptions. Note that, when `shell=True`, `OSError` will be raised by the child only if the selected shell itself was not found. To determine if the shell failed to find the requested application, it is necessary to check the return code or output from the subprocess.
A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised if [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") is called with invalid arguments.
[`check_call()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_call "subprocess.check_call") and [`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output") will raise [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "subprocess.CalledProcessError") if the called process returns a non-zero return code.
All of the functions and methods that accept a _timeout_ parameter, such as [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") and [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") will raise [`TimeoutExpired`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "subprocess.TimeoutExpired") if the timeout expires before the process exits.
Exceptions defined in this module all inherit from [`SubprocessError`](https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError "subprocess.SubprocessError").
Added in version 3.3: The [`SubprocessError`](https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError "subprocess.SubprocessError") base class was added.
