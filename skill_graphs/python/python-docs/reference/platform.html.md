[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html)
    * [Cross platform](https://docs.python.org/3/library/platform.html#cross-platform)
    * [Java platform](https://docs.python.org/3/library/platform.html#java-platform)
    * [Windows platform](https://docs.python.org/3/library/platform.html#windows-platform)
    * [macOS platform](https://docs.python.org/3/library/platform.html#macos-platform)
    * [iOS platform](https://docs.python.org/3/library/platform.html#ios-platform)
    * [Unix platforms](https://docs.python.org/3/library/platform.html#unix-platforms)
    * [Linux platforms](https://docs.python.org/3/library/platform.html#linux-platforms)
    * [Android platform](https://docs.python.org/3/library/platform.html#android-platform)
    * [Command-line usage](https://docs.python.org/3/library/platform.html#command-line-usage)


#### Previous topic
[`logging.handlers` — Logging handlers](https://docs.python.org/3/library/logging.handlers.html "previous chapter")
#### Next topic
[`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=platform+%E2%80%94++Access+to+underlying+platform%E2%80%99s+identifying+data&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fplatform.html&pagesource=library%2Fplatform.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/errno.html "errno — Standard errno system symbols") |
  * [previous](https://docs.python.org/3/library/logging.handlers.html "logging.handlers — Logging handlers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html)
  * |
  * Theme  Auto Light Dark |


#  `platform` — Access to underlying platform’s identifying data[¶](https://docs.python.org/3/library/platform.html#module-platform "Link to this heading")
**Source code:**
* * *
Note
Specific platforms listed alphabetically, with Linux included in the Unix section.
## Cross platform[¶](https://docs.python.org/3/library/platform.html#cross-platform "Link to this heading")

platform.architecture(_executable =sys.executable_, _bits =''_, _linkage =''_)[¶](https://docs.python.org/3/library/platform.html#platform.architecture "Link to this definition")

Queries the given executable (defaults to the Python interpreter binary) for various architecture information.
Returns a tuple `(bits, linkage)` which contain information about the bit architecture and the linkage format used for the executable. Both values are returned as strings.
Values that cannot be determined are returned as given by the parameter presets. If bits is given as `''`, the `sizeof(pointer)` (or `sizeof(long)` on Python version < 1.5.2) is used as indicator for the supported pointer size.
The function relies on the system’s `file` command to do the actual work. This is available on most if not all Unix platforms and some non-Unix platforms and then only if the executable points to the Python interpreter. Reasonable defaults are used when the above needs are not met.
Note
On macOS (and perhaps other platforms), executable files may be universal files containing multiple architectures.
To get at the “64-bitness” of the current interpreter, it is more reliable to query the [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize") attribute:
Copy```
is_64bits = sys.maxsize > 2**32

```


platform.machine()[¶](https://docs.python.org/3/library/platform.html#platform.machine "Link to this definition")

Returns the machine type, e.g. `'AMD64'`. An empty string is returned if the value cannot be determined.
The output is platform-dependent and may differ in casing and naming conventions.

platform.node()[¶](https://docs.python.org/3/library/platform.html#platform.node "Link to this definition")

Returns the computer’s network name (may not be fully qualified!). An empty string is returned if the value cannot be determined.

platform.platform(_aliased =False_, _terse =False_)[¶](https://docs.python.org/3/library/platform.html#platform.platform "Link to this definition")

Returns a single string identifying the underlying platform with as much useful information as possible.
The output is intended to be _human readable_ rather than machine parseable. It may look different on different platforms and this is intended.
If _aliased_ is true, the function will use aliases for various platforms that report system names which differ from their common names, for example SunOS will be reported as Solaris. The [`system_alias()`](https://docs.python.org/3/library/platform.html#platform.system_alias "platform.system_alias") function is used to implement this.
Setting _terse_ to true causes the function to return only the absolute minimum information needed to identify the platform.
Changed in version 3.8: On macOS, the function now uses [`mac_ver()`](https://docs.python.org/3/library/platform.html#platform.mac_ver "platform.mac_ver"), if it returns a non-empty release string, to get the macOS version rather than the darwin version.

platform.processor()[¶](https://docs.python.org/3/library/platform.html#platform.processor "Link to this definition")

Returns the (real) processor name, e.g. `'amdk6'`.
An empty string is returned if the value cannot be determined. Note that many platforms do not provide this information or simply return the same value as for [`machine()`](https://docs.python.org/3/library/platform.html#platform.machine "platform.machine"). NetBSD does this.

platform.python_build()[¶](https://docs.python.org/3/library/platform.html#platform.python_build "Link to this definition")

Returns a tuple `(buildno, builddate)` stating the Python build number and date as strings.

platform.python_compiler()[¶](https://docs.python.org/3/library/platform.html#platform.python_compiler "Link to this definition")

Returns a string identifying the compiler used for compiling Python.

platform.python_branch()[¶](https://docs.python.org/3/library/platform.html#platform.python_branch "Link to this definition")

Returns a string identifying the Python implementation SCM branch.

platform.python_implementation()[¶](https://docs.python.org/3/library/platform.html#platform.python_implementation "Link to this definition")

Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.

platform.python_revision()[¶](https://docs.python.org/3/library/platform.html#platform.python_revision "Link to this definition")

Returns a string identifying the Python implementation SCM revision.

platform.python_version()[¶](https://docs.python.org/3/library/platform.html#platform.python_version "Link to this definition")

Returns the Python version as string `'major.minor.patchlevel'`.
Note that unlike the Python `sys.version`, the returned value will always include the patchlevel (it defaults to 0).

platform.python_version_tuple()[¶](https://docs.python.org/3/library/platform.html#platform.python_version_tuple "Link to this definition")

Returns the Python version as tuple `(major, minor, patchlevel)` of strings.
Note that unlike the Python `sys.version`, the returned value will always include the patchlevel (it defaults to `'0'`).

platform.release()[¶](https://docs.python.org/3/library/platform.html#platform.release "Link to this definition")

Returns the system’s release, e.g. `'2.2.0'` or `'NT'`. An empty string is returned if the value cannot be determined.

platform.system()[¶](https://docs.python.org/3/library/platform.html#platform.system "Link to this definition")

Returns the system/OS name, such as `'Linux'`, `'Darwin'`, `'Java'`, `'Windows'`. An empty string is returned if the value cannot be determined.
On iOS and Android, this returns the user-facing OS name (i.e, `'iOS`, `'iPadOS'` or `'Android'`). To obtain the kernel name (`'Darwin'` or `'Linux'`), use [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname").

platform.system_alias(_system_ , _release_ , _version_)[¶](https://docs.python.org/3/library/platform.html#platform.system_alias "Link to this definition")

Returns `(system, release, version)` aliased to common marketing names used for some systems. It also does some reordering of the information in some cases where it would otherwise cause confusion.

platform.version()[¶](https://docs.python.org/3/library/platform.html#platform.version "Link to this definition")

Returns the system’s release version, e.g. `'#3 on degas'`. An empty string is returned if the value cannot be determined.
On iOS and Android, this is the user-facing OS version. To obtain the Darwin or Linux kernel version, use [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname").

platform.uname()[¶](https://docs.python.org/3/library/platform.html#platform.uname "Link to this definition")

Fairly portable uname interface. Returns a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") containing six attributes: [`system`](https://docs.python.org/3/library/platform.html#platform.system "platform.system"), [`node`](https://docs.python.org/3/library/platform.html#platform.node "platform.node"), [`release`](https://docs.python.org/3/library/platform.html#platform.release "platform.release"), [`version`](https://docs.python.org/3/library/platform.html#platform.version "platform.version"), [`machine`](https://docs.python.org/3/library/platform.html#platform.machine "platform.machine"), and [`processor`](https://docs.python.org/3/library/platform.html#platform.processor "platform.processor").
[`processor`](https://docs.python.org/3/library/platform.html#platform.processor "platform.processor") is resolved late, on demand.
Note: the first two attribute names differ from the names presented by [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname"), where they are named `sysname` and `nodename`.
Entries which cannot be determined are set to `''`.
Changed in version 3.3: Result changed from a tuple to a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple").
Changed in version 3.9: [`processor`](https://docs.python.org/3/library/platform.html#platform.processor "platform.processor") is resolved late instead of immediately.

platform.invalidate_caches()[¶](https://docs.python.org/3/library/platform.html#platform.invalidate_caches "Link to this definition")

Clear out the internal cache of information, such as the [`uname()`](https://docs.python.org/3/library/platform.html#platform.uname "platform.uname"). This is typically useful when the platform’s [`node()`](https://docs.python.org/3/library/platform.html#platform.node "platform.node") is changed by an external process and one needs to retrieve the updated value.
Added in version 3.14.
## Java platform[¶](https://docs.python.org/3/library/platform.html#java-platform "Link to this heading")

platform.java_ver(_release =''_, _vendor =''_, _vminfo =('', '', '')_, _osinfo =('', '', '')_)[¶](https://docs.python.org/3/library/platform.html#platform.java_ver "Link to this definition")

Version interface for Jython.
Returns a tuple `(release, vendor, vminfo, osinfo)` with _vminfo_ being a tuple `(vm_name, vm_release, vm_vendor)` and _osinfo_ being a tuple `(os_name, os_version, os_arch)`. Values which cannot be determined are set to the defaults given as parameters (which all default to `''`).
Deprecated since version 3.13, will be removed in version 3.15: It was largely untested, had a confusing API, and was only useful for Jython support.
## Windows platform[¶](https://docs.python.org/3/library/platform.html#windows-platform "Link to this heading")

platform.win32_ver(_release =''_, _version =''_, _csd =''_, _ptype =''_)[¶](https://docs.python.org/3/library/platform.html#platform.win32_ver "Link to this definition")

Get additional version information from the Windows Registry and return a tuple `(release, version, csd, ptype)` referring to OS release, version number, CSD level (service pack) and OS type (multi/single processor). Values which cannot be determined are set to the defaults given as parameters (which all default to an empty string).
As a hint: _ptype_ is `'Uniprocessor Free'` on single processor NT machines and `'Multiprocessor Free'` on multi processor machines. The `'Free'` refers to the OS version being free of debugging code. It could also state `'Checked'` which means the OS version uses debugging code, i.e. code that checks arguments, ranges, etc.

platform.win32_edition()[¶](https://docs.python.org/3/library/platform.html#platform.win32_edition "Link to this definition")

Returns a string representing the current Windows edition, or `None` if the value cannot be determined. Possible values include but are not limited to `'Enterprise'`, `'IoTUAP'`, `'ServerStandard'`, and `'nanoserver'`.
Added in version 3.8.

platform.win32_is_iot()[¶](https://docs.python.org/3/library/platform.html#platform.win32_is_iot "Link to this definition")

Return `True` if the Windows edition returned by [`win32_edition()`](https://docs.python.org/3/library/platform.html#platform.win32_edition "platform.win32_edition") is recognized as an IoT edition.
Added in version 3.8.
## macOS platform[¶](https://docs.python.org/3/library/platform.html#macos-platform "Link to this heading")

platform.mac_ver(_release =''_, _versioninfo =('', '', '')_, _machine =''_)[¶](https://docs.python.org/3/library/platform.html#platform.mac_ver "Link to this definition")

Get macOS version information and return it as tuple `(release, versioninfo, machine)` with _versioninfo_ being a tuple `(version, dev_stage, non_release_version)`.
Entries which cannot be determined are set to `''`. All tuple entries are strings.
## iOS platform[¶](https://docs.python.org/3/library/platform.html#ios-platform "Link to this heading")

platform.ios_ver(_system =''_, _release =''_, _model =''_, _is_simulator =False_)[¶](https://docs.python.org/3/library/platform.html#platform.ios_ver "Link to this definition")

Get iOS version information and return it as a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") with the following attributes:
  * `system` is the OS name; either `'iOS'` or `'iPadOS'`.
  * `release` is the iOS version number as a string (e.g., `'17.2'`).
  * `model` is the device model identifier; this will be a string like `'iPhone13,2'` for a physical device, or `'iPhone'` on a simulator.
  * `is_simulator` is a boolean describing if the app is running on a simulator or a physical device.


Entries which cannot be determined are set to the defaults given as parameters.
## Unix platforms[¶](https://docs.python.org/3/library/platform.html#unix-platforms "Link to this heading")

platform.libc_ver(_executable =sys.executable_, _lib =''_, _version =''_, _chunksize =16384_)[¶](https://docs.python.org/3/library/platform.html#platform.libc_ver "Link to this definition")

Tries to determine the libc version against which the file executable (defaults to the Python interpreter) is linked. Returns a tuple of strings `(lib, version)` which default to the given parameters in case the lookup fails.
Note that this function has intimate knowledge of how different libc versions add symbols to the executable is probably only usable for executables compiled using **gcc**.
The file is read and scanned in chunks of _chunksize_ bytes.
## Linux platforms[¶](https://docs.python.org/3/library/platform.html#linux-platforms "Link to this heading")

platform.freedesktop_os_release()[¶](https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release "Link to this definition")

Get operating system identification from `os-release` file and return it as a dict. The `os-release` file is a
Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") or subclass when neither `/etc/os-release` nor `/usr/lib/os-release` can be read.
On success, the function returns a dictionary where keys and values are strings. Values have their special characters like `"` and `$` unquoted. The fields `NAME`, `ID`, and `PRETTY_NAME` are always defined according to the standard. All other fields are optional. Vendors may include additional fields.
Note that fields like `NAME`, `VERSION`, and `VARIANT` are strings suitable for presentation to users. Programs should use fields like `ID`, `ID_LIKE`, `VERSION_ID`, or `VARIANT_ID` to identify Linux distributions.
Example:
Copy```
def get_like_distro():
    info = platform.freedesktop_os_release()
    ids = [info["ID"]]
    if "ID_LIKE" in info:
        # ids are space separated and ordered by precedence
        ids.extend(info["ID_LIKE"].split())
    return ids

```

Added in version 3.10.
## Android platform[¶](https://docs.python.org/3/library/platform.html#android-platform "Link to this heading")

platform.android_ver(_release =''_, _api_level =0_, _manufacturer =''_, _model =''_, _device =''_, _is_emulator =False_)[¶](https://docs.python.org/3/library/platform.html#platform.android_ver "Link to this definition")

Get Android device information. Returns a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") with the following attributes. Values which cannot be determined are set to the defaults given as parameters.
  * `release` - Android version, as a string (e.g. `"14"`).
  * `api_level` - API level of the running device, as an integer (e.g. `34` for Android 14). To get the API level which Python was built against, see [`sys.getandroidapilevel()`](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "sys.getandroidapilevel").
  * `manufacturer` -
  * `model` -
  * `device` -
  * `is_emulator` - `True` if the device is an emulator; `False` if it’s a physical device.


Google maintains a
Added in version 3.13.
## Command-line usage[¶](https://docs.python.org/3/library/platform.html#command-line-usage "Link to this heading")
`platform` can also be invoked directly using the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) switch of the interpreter:
Copy```
python -m platform [--terse] [--nonaliased] [{nonaliased,terse} ...]

```

The following options are accepted:

--terse[¶](https://docs.python.org/3/library/platform.html#cmdoption-platform-terse "Link to this definition")

Print terse information about the platform. This is equivalent to calling [`platform.platform()`](https://docs.python.org/3/library/platform.html#platform.platform "platform.platform") with the _terse_ argument set to `True`.

--nonaliased[¶](https://docs.python.org/3/library/platform.html#cmdoption-platform-nonaliased "Link to this definition")

Print platform information without system/OS name aliasing. This is equivalent to calling [`platform.platform()`](https://docs.python.org/3/library/platform.html#platform.platform "platform.platform") with the _aliased_ argument set to `True`.
You can also pass one or more positional arguments (`terse`, `nonaliased`) to explicitly control the output format. These behave similarly to their corresponding options.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html)
    * [Cross platform](https://docs.python.org/3/library/platform.html#cross-platform)
    * [Java platform](https://docs.python.org/3/library/platform.html#java-platform)
    * [Windows platform](https://docs.python.org/3/library/platform.html#windows-platform)
    * [macOS platform](https://docs.python.org/3/library/platform.html#macos-platform)
    * [iOS platform](https://docs.python.org/3/library/platform.html#ios-platform)
    * [Unix platforms](https://docs.python.org/3/library/platform.html#unix-platforms)
    * [Linux platforms](https://docs.python.org/3/library/platform.html#linux-platforms)
    * [Android platform](https://docs.python.org/3/library/platform.html#android-platform)
    * [Command-line usage](https://docs.python.org/3/library/platform.html#command-line-usage)


#### Previous topic
[`logging.handlers` — Logging handlers](https://docs.python.org/3/library/logging.handlers.html "previous chapter")
#### Next topic
[`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=platform+%E2%80%94++Access+to+underlying+platform%E2%80%99s+identifying+data&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fplatform.html&pagesource=library%2Fplatform.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/errno.html "errno — Standard errno system symbols") |
  * [previous](https://docs.python.org/3/library/logging.handlers.html "logging.handlers — Logging handlers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
