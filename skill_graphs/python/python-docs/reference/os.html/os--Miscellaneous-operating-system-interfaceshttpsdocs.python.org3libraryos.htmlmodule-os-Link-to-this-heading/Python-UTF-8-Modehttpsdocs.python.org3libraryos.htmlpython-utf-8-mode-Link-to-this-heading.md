## Python UTF-8 Mode[¶](https://docs.python.org/3/library/os.html#python-utf-8-mode "Link to this heading")
Added in version 3.7: See [**PEP 540**](https://peps.python.org/pep-0540/) for more details.
The Python UTF-8 Mode ignores the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding) and forces the usage of the UTF-8 encoding:
  * Use UTF-8 as the [filesystem encoding](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler).
  * [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") returns `'utf-8'`.
  * [`locale.getpreferredencoding()`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding") returns `'utf-8'` (the _do_setlocale_ argument has no effect).
  * [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin"), [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout"), and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") all use UTF-8 as their text encoding, with the `surrogateescape` [error handler](https://docs.python.org/3/library/codecs.html#error-handlers) being enabled for `sys.stdin` and `sys.stdout` (`sys.stderr` continues to use `backslashreplace` as it does in the default locale-aware mode)
  * On Unix, [`os.device_encoding()`](https://docs.python.org/3/library/os.html#os.device_encoding "os.device_encoding") returns `'utf-8'` rather than the device encoding.


Note that the standard stream settings in UTF-8 mode can be overridden by [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING) (just as they can be in the default locale-aware mode).
As a consequence of the changes in those lower level APIs, other higher level APIs also exhibit different default behaviours:
  * Command line arguments, environment variables and filenames are decoded to text using the UTF-8 encoding.
  * [`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode") and [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode") use the UTF-8 encoding.
  * [`open()`](https://docs.python.org/3/library/functions.html#open "open"), [`io.open()`](https://docs.python.org/3/library/io.html#io.open "io.open"), and [`codecs.open()`](https://docs.python.org/3/library/codecs.html#codecs.open "codecs.open") use the UTF-8 encoding by default. However, they still use the strict error handler by default so that attempting to open a binary file in text mode is likely to raise an exception rather than producing nonsense data.


The [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) is enabled if the LC_CTYPE locale is `C` or `POSIX` at Python startup (see the [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read") function).
It can be enabled or disabled using the [`-X utf8`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command line option and the [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8) environment variable.
If the [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8) environment variable is not set at all, then the interpreter defaults to using the current locale settings, _unless_ the current locale is identified as a legacy ASCII-based locale (as described for [`PYTHONCOERCECLOCALE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCOERCECLOCALE)), and locale coercion is either disabled or fails. In such legacy locales, the interpreter will default to enabling UTF-8 mode unless explicitly instructed not to do so.
The Python UTF-8 Mode can only be enabled at the Python startup. Its value can be read from [`sys.flags.utf8_mode`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags").
See also the [UTF-8 mode on Windows](https://docs.python.org/3/using/windows.html#win-utf8-mode) and the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler).
See also

[**PEP 686**](https://peps.python.org/pep-0686/)

Python 3.15 will make [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) default.
