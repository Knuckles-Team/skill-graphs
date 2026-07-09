# becomes
retcode = call("mycmd" + " myarg", shell=True)

```

Notes:
  * Calling the program through the shell is usually not required.
  * The [`call()`](https://docs.python.org/3/library/subprocess.html#subprocess.call "subprocess.call") return value is encoded differently to that of [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system").
  * The [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system") function ignores SIGINT and SIGQUIT signals while the command is running, but the caller must do this separately when using the `subprocess` module.


A more realistic example would look like this:
Copy```
try:
    retcode = call("mycmd" + " myarg", shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)

```

### Replacing the [`os.spawn`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") family[¶](https://docs.python.org/3/library/subprocess.html#replacing-the-os-spawn-family "Link to this heading")
P_NOWAIT example:
Copy```
pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
==>
pid = Popen(["/bin/mycmd", "myarg"]).pid

```

P_WAIT example:
Copy```
retcode = os.spawnlp(os.P_WAIT, "/bin/mycmd", "mycmd", "myarg")
==>
retcode = call(["/bin/mycmd", "myarg"])

```

Vector example:
Copy```
os.spawnvp(os.P_NOWAIT, path, args)
==>
Popen([path] + args[1:])

```

Environment example:
Copy```
os.spawnlpe(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg", env)
==>
Popen(["/bin/mycmd", "myarg"], env={"PATH": "/usr/bin"})

```

### Replacing [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")[¶](https://docs.python.org/3/library/subprocess.html#replacing-os-popen "Link to this heading")
Return code handling translates as follows:
Copy```
pipe = os.popen(cmd, 'w')
...
rc = pipe.close()
if rc is not None and rc >> 8:
    print("There were some errors")
==>
process = Popen(cmd, stdin=PIPE)
...
process.stdin.close()
if process.wait() != 0:
    print("There were some errors")

```

## Legacy Shell Invocation Functions[¶](https://docs.python.org/3/library/subprocess.html#legacy-shell-invocation-functions "Link to this heading")
This module also provides the following legacy functions from the 2.x `commands` module. These operations implicitly invoke the system shell and none of the guarantees described above regarding security and exception handling consistency are valid for these functions.

subprocess.getstatusoutput(_cmd_ , _*_ , _encoding =None_, _errors =None_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.getstatusoutput "Link to this definition")

Return `(exitcode, output)` of executing _cmd_ in a shell.
Execute the string _cmd_ in a shell with [`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output") and return a 2-tuple `(exitcode, output)`. _encoding_ and _errors_ are used to decode output; see the notes on [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments) for more details.
A trailing newline is stripped from the output. The exit code for the command can be interpreted as the return code of subprocess. Example:
Copy```
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')
>>> subprocess.getstatusoutput('cat /bin/junk')
(1, 'cat: /bin/junk: No such file or directory')
>>> subprocess.getstatusoutput('/bin/junk')
(127, 'sh: /bin/junk: not found')
>>> subprocess.getstatusoutput('/bin/kill $$')
(-15, '')

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.3.4: Windows support was added.
The function now returns (exitcode, output) instead of (status, output) as it did in Python 3.3.3 and earlier. exitcode has the same value as [`returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode").
Changed in version 3.11: Added the _encoding_ and _errors_ parameters.

subprocess.getoutput(_cmd_ , _*_ , _encoding =None_, _errors =None_)[¶](https://docs.python.org/3/library/subprocess.html#subprocess.getoutput "Link to this definition")

Return output (stdout and stderr) of executing _cmd_ in a shell.
Like [`getstatusoutput()`](https://docs.python.org/3/library/subprocess.html#subprocess.getstatusoutput "subprocess.getstatusoutput"), except the exit code is ignored and the return value is a string containing the command’s output. Example:
Copy```
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.3.4: Windows support added
Changed in version 3.11: Added the _encoding_ and _errors_ parameters.
## Notes[¶](https://docs.python.org/3/library/subprocess.html#notes "Link to this heading")
### Timeout Behavior[¶](https://docs.python.org/3/library/subprocess.html#timeout-behavior "Link to this heading")
When using the `timeout` parameter in functions like [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run"), [`Popen.wait()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "subprocess.Popen.wait"), or [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate"), users should be aware of the following behaviors:
  1. **Process Creation Delay** : The initial process creation itself cannot be interrupted on many platform APIs. This means that even when specifying a timeout, you are not guaranteed to see a timeout exception until at least after however long process creation takes.
  2. **Extremely Small Timeout Values** : Setting very small timeout values (such as a few milliseconds) may result in almost immediate [`TimeoutExpired`](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exceptions because process creation and system scheduling inherently require time.


### Converting an argument sequence to a string on Windows[¶](https://docs.python.org/3/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows "Link to this heading")
On Windows, an _args_ sequence is converted to a string that can be parsed using the following rules (which correspond to the rules used by the MS C runtime):
  1. Arguments are delimited by white space, which is either a space or a tab.
  2. A string surrounded by double quotation marks is interpreted as a single argument, regardless of white space contained within. A quoted string can be embedded in an argument.
  3. A double quotation mark preceded by a backslash is interpreted as a literal double quotation mark.
  4. Backslashes are interpreted literally, unless they immediately precede a double quotation mark.
  5. If backslashes immediately precede a double quotation mark, every pair of backslashes is interpreted as a literal backslash. If the number of backslashes is odd, the last backslash escapes the next double quotation mark as described in rule 3.


See also

[`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "shlex: Simple lexical analysis for Unix shell-like languages.")

Module which provides function to parse and escape command lines.
### Disable use of `posix_spawn()`[¶](https://docs.python.org/3/library/subprocess.html#disable-use-of-posix-spawn "Link to this heading")
On Linux, `subprocess` defaults to using the `vfork()` system call internally when it is safe to do so rather than `fork()`. This greatly improves performance.
Copy```
subprocess._USE_POSIX_SPAWN = False  # See CPython issue gh-NNNNNN.

```

It is safe to set this to false on any Python version. It will have no effect on older or newer versions where unsupported. Do not assume the attribute is available to read. Despite the name, a true value does not indicate the corresponding function will be used, only that it may be.
Please file issues any time you have to use these private knobs with a way to reproduce the issue you were seeing. Link to that issue from a comment in your code.
Added in version 3.8: `_USE_POSIX_SPAWN`
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)
    * [Using the `subprocess` Module](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)
      * [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments)
      * [Popen Constructor](https://docs.python.org/3/library/subprocess.html#popen-constructor)
      * [Exceptions](https://docs.python.org/3/library/subprocess.html#exceptions)
    * [Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations)
    * [Popen Objects](https://docs.python.org/3/library/subprocess.html#popen-objects)
    * [Windows Popen Helpers](https://docs.python.org/3/library/subprocess.html#windows-popen-helpers)
      * [Windows Constants](https://docs.python.org/3/library/subprocess.html#windows-constants)
    * [Older high-level API](https://docs.python.org/3/library/subprocess.html#older-high-level-api)
    * [Replacing Older Functions with the `subprocess` Module](https://docs.python.org/3/library/subprocess.html#replacing-older-functions-with-the-subprocess-module)
      * [Replacing **/bin/sh** shell command substitution](https://docs.python.org/3/library/subprocess.html#replacing-bin-sh-shell-command-substitution)
      * [Replacing shell pipeline](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline)
      * [Replacing `os.system()`](https://docs.python.org/3/library/subprocess.html#replacing-os-system)
      * [Replacing the `os.spawn` family](https://docs.python.org/3/library/subprocess.html#replacing-the-os-spawn-family)
      * [Replacing `os.popen()`](https://docs.python.org/3/library/subprocess.html#replacing-os-popen)
    * [Legacy Shell Invocation Functions](https://docs.python.org/3/library/subprocess.html#legacy-shell-invocation-functions)
    * [Notes](https://docs.python.org/3/library/subprocess.html#notes)
      * [Timeout Behavior](https://docs.python.org/3/library/subprocess.html#timeout-behavior)
      * [Converting an argument sequence to a string on Windows](https://docs.python.org/3/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows)
      * [Disable use of `posix_spawn()`](https://docs.python.org/3/library/subprocess.html#disable-use-of-posix-spawn)


#### Previous topic
[`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html "previous chapter")
#### Next topic
[`sched` — Event scheduler](https://docs.python.org/3/library/sched.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=subprocess+%E2%80%94+Subprocess+management&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsubprocess.html&pagesource=library%2Fsubprocess.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sched.html "sched — Event scheduler") |
  * [previous](https://docs.python.org/3/library/concurrent.interpreters.html "concurrent.interpreters — Multiple interpreters in the same process") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline)
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
