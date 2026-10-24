## Miscellaneous System Information[¶](https://docs.python.org/3/library/os.html#miscellaneous-system-information "Link to this heading")

os.confstr(_name_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.confstr "Link to this definition")

Return string-valued system configuration values. _name_ specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX, Unix 95, Unix 98, and others). Some platforms define additional names as well. The names known to the host operating system are given as the keys of the `confstr_names` dictionary. For configuration variables not included in that mapping, passing an integer for _name_ is also accepted.
If the configuration value specified by _name_ isn’t defined, `None` is returned.
If _name_ is a string and is not known, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. If a specific value for _name_ is not supported by the host system, even if it is included in `confstr_names`, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised with [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL") for the error number.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.confstr_names[¶](https://docs.python.org/3/library/os.html#os.confstr_names "Link to this definition")

Dictionary mapping names accepted by [`confstr()`](https://docs.python.org/3/library/os.html#os.confstr "os.confstr") to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.cpu_count()[¶](https://docs.python.org/3/library/os.html#os.cpu_count "Link to this definition")

Return the number of logical CPUs in the **system**. Returns `None` if undetermined.
The [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") function can be used to get the number of logical CPUs usable by the calling thread of the **current process**.
Added in version 3.4.
Changed in version 3.13: If [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) is given or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT) is set, `cpu_count()` returns the override value _n_.

os.getloadavg()[¶](https://docs.python.org/3/library/os.html#os.getloadavg "Link to this definition")

Return the number of processes in the system run queue averaged over the last 1, 5, and 15 minutes or raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the load average was unobtainable.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.process_cpu_count()[¶](https://docs.python.org/3/library/os.html#os.process_cpu_count "Link to this definition")

Get the number of logical CPUs usable by the calling thread of the **current process**. Returns `None` if undetermined. It can be less than [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count") depending on the CPU affinity.
The [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count") function can be used to get the number of logical CPUs in the **system**.
If [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) is given or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT) is set, `process_cpu_count()` returns the override value _n_.
See also the [`sched_getaffinity()`](https://docs.python.org/3/library/os.html#os.sched_getaffinity "os.sched_getaffinity") function.
Added in version 3.13.

os.sysconf(_name_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.sysconf "Link to this definition")

Return integer-valued system configuration values. If the configuration value specified by _name_ isn’t defined, `-1` is returned. The comments regarding the _name_ parameter for [`confstr()`](https://docs.python.org/3/library/os.html#os.confstr "os.confstr") apply here as well; the dictionary that provides information on the known names is given by `sysconf_names`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.sysconf_names[¶](https://docs.python.org/3/library/os.html#os.sysconf_names "Link to this definition")

Dictionary mapping names accepted by [`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Changed in version 3.11: Add `'SC_MINSIGSTKSZ'` name.
The following data values are used to support path manipulation operations. These are defined for all platforms.
Higher-level operations on pathnames are defined in the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") module.

os.curdir[¶](https://docs.python.org/3/library/os.html#os.curdir "Link to this definition")

The constant string used by the operating system to refer to the current directory. This is `'.'` for Windows and POSIX. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.pardir[¶](https://docs.python.org/3/library/os.html#os.pardir "Link to this definition")

The constant string used by the operating system to refer to the parent directory. This is `'..'` for Windows and POSIX. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.sep[¶](https://docs.python.org/3/library/os.html#os.sep "Link to this definition")

The character used by the operating system to separate pathname components. This is `'/'` for POSIX and `'\\'` for Windows. Note that knowing this is not sufficient to be able to parse or concatenate pathnames — use [`os.path.split()`](https://docs.python.org/3/library/os.path.html#os.path.split "os.path.split") and [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join") — but it is occasionally useful. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.altsep[¶](https://docs.python.org/3/library/os.html#os.altsep "Link to this definition")

An alternative character used by the operating system to separate pathname components, or `None` if only one separator character exists. This is set to `'/'` on Windows systems where `sep` is a backslash. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.extsep[¶](https://docs.python.org/3/library/os.html#os.extsep "Link to this definition")

The character which separates the base filename from the extension; for example, the `'.'` in `os.py`. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.pathsep[¶](https://docs.python.org/3/library/os.html#os.pathsep "Link to this definition")

The character conventionally used by the operating system to separate search path components (as in `PATH`), such as `':'` for POSIX or `';'` for Windows. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.defpath[¶](https://docs.python.org/3/library/os.html#os.defpath "Link to this definition")

The default search path used by [`exec*p*`](https://docs.python.org/3/library/os.html#os.execl "os.execl") and [`spawn*p*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") if the environment doesn’t have a `'PATH'` key. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.linesep[¶](https://docs.python.org/3/library/os.html#os.linesep "Link to this definition")

The string used to separate (or, rather, terminate) lines on the current platform. This may be a single character, such as `'\n'` for POSIX, or multiple characters, for example, `'\r\n'` for Windows. Do not use _os.linesep_ as a line terminator when writing files opened in text mode (the default); use a single `'\n'` instead, on all platforms.

os.devnull[¶](https://docs.python.org/3/library/os.html#os.devnull "Link to this definition")

The file path of the null device. For example: `'/dev/null'` for POSIX, `'nul'` for Windows. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").

os.RTLD_LAZY[¶](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "Link to this definition")


os.RTLD_NOW[¶](https://docs.python.org/3/library/os.html#os.RTLD_NOW "Link to this definition")


os.RTLD_GLOBAL[¶](https://docs.python.org/3/library/os.html#os.RTLD_GLOBAL "Link to this definition")


os.RTLD_LOCAL[¶](https://docs.python.org/3/library/os.html#os.RTLD_LOCAL "Link to this definition")


os.RTLD_NODELETE[¶](https://docs.python.org/3/library/os.html#os.RTLD_NODELETE "Link to this definition")


os.RTLD_NOLOAD[¶](https://docs.python.org/3/library/os.html#os.RTLD_NOLOAD "Link to this definition")


os.RTLD_DEEPBIND[¶](https://docs.python.org/3/library/os.html#os.RTLD_DEEPBIND "Link to this definition")

Flags for use with the [`setdlopenflags()`](https://docs.python.org/3/library/sys.html#sys.setdlopenflags "sys.setdlopenflags") and [`getdlopenflags()`](https://docs.python.org/3/library/sys.html#sys.getdlopenflags "sys.getdlopenflags") functions. See the Unix manual page
Added in version 3.3.
