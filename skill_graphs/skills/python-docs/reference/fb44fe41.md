## Older high-level API[¶](https://docs.python.org/3/library/subprocess.html#older-high-level-api "Link to this heading")
Prior to Python 3.5, these three functions comprised the high level API to subprocess. You can now use [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") in many cases, but lots of existing code calls these functions.

subprocess.call(_args_ , _*_ , _stdin =None_, _stdout =None_, _stderr =None_, _shell =False_, _cwd =None_, _timeout =None_, _** other_popen_kwargs_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.call "Link to this definition")

Run the command described by _args_. Wait for command to complete, then return the [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute.
Code needing to capture stdout or stderr should use [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") instead:
Copy```
run(...).returncode

```

To suppress stdout or stderr, supply a value of [`DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL").
The arguments shown above are merely some common ones. The full function signature is the same as that of the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") constructor - this function passes all supplied arguments other than _timeout_ directly through to that interface.
Note
Do not use `stdout=PIPE` or `stderr=PIPE` with this function. The child process will block if it generates enough output to a pipe to fill up the OS pipe buffer as the pipes are not being read from.
Changed in version 3.3: _timeout_ was added.
Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

subprocess.check_call(_args_ , _*_ , _stdin =None_, _stdout =None_, _stderr =None_, _shell =False_, _cwd =None_, _timeout =None_, _** other_popen_kwargs_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.check_call "Link to this definition")

Run command with arguments. Wait for command to complete. If the return code was zero then return, otherwise raise [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "subprocess.CalledProcessError"). The `CalledProcessError` object will have the return code in the [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.returncode "subprocess.CalledProcessError.returncode") attribute. If `check_call()` was unable to start the process it will propagate the exception that was raised.
Code needing to capture stdout or stderr should use [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") instead:
Copy```
run(..., check=True)

```

To suppress stdout or stderr, supply a value of [`DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL").
The arguments shown above are merely some common ones. The full function signature is the same as that of the [`Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") constructor - this function passes all supplied arguments other than _timeout_ directly through to that interface.
Note
Do not use `stdout=PIPE` or `stderr=PIPE` with this function. The child process will block if it generates enough output to a pipe to fill up the OS pipe buffer as the pipes are not being read from.
Changed in version 3.3: _timeout_ was added.
Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

subprocess.check_output(_args_ , _*_ , _stdin =None_, _stderr =None_, _shell =False_, _cwd =None_, _encoding =None_, _errors =None_, _universal_newlines =None_, _timeout =None_, _text =None_, _** other_popen_kwargs_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "Link to this definition")

Run command with arguments and return its output.
If the return code was non-zero it raises a [`CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError "subprocess.CalledProcessError"). The `CalledProcessError` object will have the return code in the [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.returncode "subprocess.CalledProcessError.returncode") attribute and any output in the [`output`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError.output "subprocess.CalledProcessError.output") attribute.
This is equivalent to:
Copy```
run(..., check=True, stdout=PIPE).stdout

```

The arguments shown above are merely some common ones. The full function signature is largely the same as that of [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") - most arguments are passed directly through to that interface. One API deviation from `run()` behavior exists: passing `input=None` will behave the same as `input=b''` (or `input=''`, depending on other arguments) rather than using the parent’s standard input file handle.
By default, this function will return the data as encoded bytes. The actual encoding of the output data may depend on the command being invoked, so the decoding to text will often need to be handled at the application level.
This behaviour may be overridden by setting _text_ , _encoding_ , _errors_ , or _universal_newlines_ to `True` as described in [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments) and [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run").
To also capture standard error in the result, use `stderr=subprocess.STDOUT`:
Copy```
>>> subprocess.check_output(
...     "ls non_existent_file; exit 0",
...     stderr=subprocess.STDOUT,
...     shell=True)
'ls: non_existent_file: No such file or directory\n'

```

Added in version 3.1.
Changed in version 3.3: _timeout_ was added.
Changed in version 3.4: Support for the _input_ keyword argument was added.
Changed in version 3.6: _encoding_ and _errors_ were added. See [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") for details.
Added in version 3.7: _text_ was added as a more readable alias for _universal_newlines_.
Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.
