[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`warnings` — Warning control](https://docs.python.org/3/library/warnings.html)
    * [Warning Categories](https://docs.python.org/3/library/warnings.html#warning-categories)
    * [The Warnings Filter](https://docs.python.org/3/library/warnings.html#the-warnings-filter)
      * [Repeated Warning Suppression Criteria](https://docs.python.org/3/library/warnings.html#repeated-warning-suppression-criteria)
      * [Describing Warning Filters](https://docs.python.org/3/library/warnings.html#describing-warning-filters)
      * [Default Warning Filter](https://docs.python.org/3/library/warnings.html#default-warning-filter)
      * [Overriding the default filter](https://docs.python.org/3/library/warnings.html#overriding-the-default-filter)
    * [Temporarily Suppressing Warnings](https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings)
    * [Testing Warnings](https://docs.python.org/3/library/warnings.html#testing-warnings)
    * [Updating Code For New Versions of Dependencies](https://docs.python.org/3/library/warnings.html#updating-code-for-new-versions-of-dependencies)
    * [Available Functions](https://docs.python.org/3/library/warnings.html#available-functions)
    * [Available Context Managers](https://docs.python.org/3/library/warnings.html#available-context-managers)
    * [Concurrent safety of Context Managers](https://docs.python.org/3/library/warnings.html#concurrent-safety-of-context-managers)


#### Previous topic
[`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html "previous chapter")
#### Next topic
[`dataclasses` — Data Classes](https://docs.python.org/3/library/dataclasses.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=warnings+%E2%80%94+Warning+control&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwarnings.html&pagesource=library%2Fwarnings.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/dataclasses.html "dataclasses — Data Classes") |
  * [previous](https://docs.python.org/3/library/__main__.html "__main__ — Top-level code environment") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`warnings` — Warning control](https://docs.python.org/3/library/warnings.html#concurrent-safety-of-context-managers)
  * |
  * Theme  Auto Light Dark |


#  `warnings` — Warning control[¶](https://docs.python.org/3/library/warnings.html#module-warnings "Link to this heading")
**Source code:**
* * *
Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program, where that condition (normally) doesn’t warrant raising an exception and terminating the program. For example, one might want to issue a warning when a program uses an obsolete module.
Python programmers issue warnings by calling the [`warn()`](https://docs.python.org/3/library/warnings.html#warnings.warn "warnings.warn") function defined in this module. (C programmers use [`PyErr_WarnEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnEx "PyErr_WarnEx"); see [Exception Handling](https://docs.python.org/3/c-api/exceptions.html#exceptionhandling) for details).
Warning messages are normally written to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"), but their disposition can be changed flexibly, from ignoring all warnings to turning them into exceptions. The disposition of warnings can vary based on the [warning category](https://docs.python.org/3/library/warnings.html#warning-categories), the text of the warning message, and the source location where it is issued. Repetitions of a particular warning for the same source location are typically suppressed.
There are two stages in warning control: first, each time a warning is issued, a determination is made whether a message should be issued or not; next, if a message is to be issued, it is formatted and printed using a user-settable hook.
The determination whether to issue a warning message is controlled by the [warning filter](https://docs.python.org/3/library/warnings.html#warning-filter), which is a sequence of matching rules and actions. Rules can be added to the filter by calling [`filterwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings") and reset to its default state by calling [`resetwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.resetwarnings "warnings.resetwarnings").
The printing of warning messages is done by calling [`showwarning()`](https://docs.python.org/3/library/warnings.html#warnings.showwarning "warnings.showwarning"), which may be overridden; the default implementation of this function formats the message by calling [`formatwarning()`](https://docs.python.org/3/library/warnings.html#warnings.formatwarning "warnings.formatwarning"), which is also available for use by custom implementations.
See also
[`logging.captureWarnings()`](https://docs.python.org/3/library/logging.html#logging.captureWarnings "logging.captureWarnings") allows you to handle all warnings with the standard logging infrastructure.
## Warning Categories[¶](https://docs.python.org/3/library/warnings.html#warning-categories "Link to this heading")
There are a number of built-in exceptions that represent warning categories. This categorization is useful to be able to filter out groups of warnings.
While these are technically [built-in exceptions](https://docs.python.org/3/library/exceptions.html#warning-categories-as-exceptions), they are documented here, because conceptually they belong to the warnings mechanism.
User code can define additional warning categories by subclassing one of the standard warning categories. A warning category must always be a subclass of the [`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning") class.
The following warnings category classes are currently defined:
Class | Description
---|---
[`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning") | This is the base class of all warning category classes. It is a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").
[`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "UserWarning") | The default category for [`warn()`](https://docs.python.org/3/library/warnings.html#warnings.warn "warnings.warn").
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") | Base category for warnings about deprecated features when those warnings are intended for other Python developers (ignored by default, unless triggered by code in `__main__`).
[`SyntaxWarning`](https://docs.python.org/3/library/exceptions.html#SyntaxWarning "SyntaxWarning") | Base category for warnings about dubious syntactic features (typically emitted when compiling Python source code, and hence may not be suppressed by runtime filters)
[`RuntimeWarning`](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "RuntimeWarning") | Base category for warnings about dubious runtime features.
[`FutureWarning`](https://docs.python.org/3/library/exceptions.html#FutureWarning "FutureWarning") | Base category for warnings about deprecated features when those warnings are intended for end users of applications that are written in Python.
[`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning") | Base category for warnings about features that will be deprecated in the future (ignored by default).
[`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") | Base category for warnings triggered during the process of importing a module (ignored by default).
[`UnicodeWarning`](https://docs.python.org/3/library/exceptions.html#UnicodeWarning "UnicodeWarning") | Base category for warnings related to Unicode.
[`BytesWarning`](https://docs.python.org/3/library/exceptions.html#BytesWarning "BytesWarning") | Base category for warnings related to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").
[`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") | Base category for warnings related to resource usage (ignored by default).
Changed in version 3.7: Previously [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") and [`FutureWarning`](https://docs.python.org/3/library/exceptions.html#FutureWarning "FutureWarning") were distinguished based on whether a feature was being removed entirely or changing its behaviour. They are now distinguished based on their intended audience and the way they’re handled by the default warnings filters.
## The Warnings Filter[¶](https://docs.python.org/3/library/warnings.html#the-warnings-filter "Link to this heading")
The warnings filter controls whether warnings are ignored, displayed, or turned into errors (raising an exception).
Conceptually, the warnings filter maintains an ordered list of filter specifications; any specific warning is matched against each filter specification in the list in turn until a match is found; the filter determines the disposition of the match. Each entry is a tuple of the form (_action_ , _message_ , _category_ , _module_ , _lineno_), where:
  * _action_ is one of the following strings:
Value | Disposition
---|---
`"default"` | print the first occurrence of matching warnings for each location (module + line number) where the warning is issued
`"error"` | turn matching warnings into exceptions
`"ignore"` | never print matching warnings
`"always"` | always print matching warnings
`"all"` | alias to “always”
`"module"` | print the first occurrence of matching warnings for each module where the warning is issued (regardless of line number)
`"once"` | print only the first occurrence of matching warnings, regardless of location
  * _message_ is a string containing a regular expression that the start of the warning message must match, case-insensitively. In [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) and [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS), _message_ is a literal string that the start of the warning message must contain (case-insensitively), ignoring any whitespace at the start or end of _message_.
  * _category_ is a class (a subclass of [`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning")) of which the warning category must be a subclass in order to match.
  * _module_ is a string containing a regular expression that the start of the fully qualified module name must match, case-sensitively. In [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) and [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS), _module_ is a literal string that the fully qualified module name must be equal to (case-sensitively), ignoring any whitespace at the start or end of _module_.
  * _lineno_ is an integer that the line number where the warning occurred must match, or `0` to match all line numbers.


Since the [`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning") class is derived from the built-in [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") class, to turn a warning into an error we simply raise `category(message)`.
If a warning is reported and doesn’t match any registered filter then the “default” action is applied (hence its name).
### Repeated Warning Suppression Criteria[¶](https://docs.python.org/3/library/warnings.html#repeated-warning-suppression-criteria "Link to this heading")
The filters that suppress repeated warnings apply the following criteria to determine if a warning is considered a repeat:
  * `"default"`: A warning is considered a repeat only if the (_message_ , _category_ , _module_ , _lineno_) are all the same.
  * `"module"`: A warning is considered a repeat if the (_message_ , _category_ , _module_) are the same, ignoring the line number.
  * `"once"`: A warning is considered a repeat if the (_message_ , _category_) are the same, ignoring the module and line number.


### Describing Warning Filters[¶](https://docs.python.org/3/library/warnings.html#describing-warning-filters "Link to this heading")
The warnings filter is initialized by [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) options passed to the Python interpreter command line and the [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable. The interpreter saves the arguments for all supplied entries without interpretation in [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions"); the `warnings` module parses these when it is first imported (invalid options are ignored, after printing a message to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")).
Individual warnings filters are specified as a sequence of fields separated by colons:
Copy```
action:message:category:module:line

```

The meaning of each of these fields is as described in [The Warnings Filter](https://docs.python.org/3/library/warnings.html#warning-filter). When listing multiple filters on a single line (as for [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS)), the individual filters are separated by commas and the filters listed later take precedence over those listed before them (as they’re applied left-to-right, and the most recently applied filters take precedence over earlier ones).
Commonly used warning filters apply to either all warnings, warnings in a particular category, or warnings raised by particular modules or packages. Some examples:
Copy```
default                      # Show all warnings (even those ignored by default)
ignore                       # Ignore all warnings
error                        # Convert all warnings to errors
error::ResourceWarning       # Treat ResourceWarning messages as errors
default::DeprecationWarning  # Show DeprecationWarning messages
ignore,default:::mymodule    # Only report warnings triggered by "mymodule"
error:::mymodule             # Convert warnings to errors in "mymodule"

```

### Default Warning Filter[¶](https://docs.python.org/3/library/warnings.html#default-warning-filter "Link to this heading")
By default, Python installs several warning filters, which can be overridden by the [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) command-line option, the [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable and calls to [`filterwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings").
In regular release builds, the default warning filter has the following entries (in order of precedence):
Copy```
default::DeprecationWarning:__main__
ignore::DeprecationWarning
ignore::PendingDeprecationWarning
ignore::ImportWarning
ignore::ResourceWarning

```

In a [debug build](https://docs.python.org/3/using/configure.html#debug-build), the list of default warning filters is empty.
Changed in version 3.2: [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") is now ignored by default in addition to [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning").
Changed in version 3.7: [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") is once again shown by default when triggered directly by code in `__main__`.
Changed in version 3.7: [`BytesWarning`](https://docs.python.org/3/library/exceptions.html#BytesWarning "BytesWarning") no longer appears in the default filter list and is instead configured via [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions") when [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b) is specified twice.
### Overriding the default filter[¶](https://docs.python.org/3/library/warnings.html#overriding-the-default-filter "Link to this heading")
Developers of applications written in Python may wish to hide _all_ Python level warnings from their users by default, and only display them when running tests or otherwise working on the application. The [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions") attribute used to pass filter configurations to the interpreter can be used as a marker to indicate whether or not warnings should be disabled:
Copy```
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

```

Developers of test runners for Python code are advised to instead ensure that _all_ warnings are displayed by default for the code under test, using code like:
Copy```
import sys

if not sys.warnoptions:
    import os, warnings
    warnings.simplefilter("default") # Change the filter in this process
    os.environ["PYTHONWARNINGS"] = "default" # Also affect subprocesses

```

Finally, developers of interactive shells that run user code in a namespace other than `__main__` are advised to ensure that [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") messages are made visible by default, using code like the following (where `user_ns` is the module used to execute code entered interactively):
Copy```
import warnings
warnings.filterwarnings("default", category=DeprecationWarning,
                                   module=user_ns.get("__name__"))

```

## Temporarily Suppressing Warnings[¶](https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings "Link to this heading")
If you are using code that you know will raise a warning, such as a deprecated function, but do not want to see the warning (even when warnings have been explicitly configured via the command line), then it is possible to suppress the warning using the [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") context manager:
Copy```
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

```

While within the context manager all warnings will simply be ignored. This allows you to use known-deprecated code without having to see the warning while not suppressing the warning for other code that might not be aware of its use of deprecated code.
> Note
> See [Concurrent safety of Context Managers](https://docs.python.org/3/library/warnings.html#warning-concurrent-safe) for details on the concurrency-safety of the [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") context manager when used in programs using multiple threads or async functions.
## Testing Warnings[¶](https://docs.python.org/3/library/warnings.html#testing-warnings "Link to this heading")
To test warnings raised by code, use the [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") context manager. With it you can temporarily mutate the warnings filter to facilitate your testing. For instance, do the following to capture all raised warnings to check:
Copy```
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings(record=True) as w:
    # Cause all warnings to always be triggered.
    warnings.simplefilter("always")
    # Trigger a warning.
    fxn()
    # Verify some things
    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)
    assert "deprecated" in str(w[-1].message)

```

One can also cause all warnings to be exceptions by using `error` instead of `always`. One thing to be aware of is that if a warning has already been raised because of a `once`/`default` rule, then no matter what filters are set the warning will not be seen again unless the warnings registry related to the warning has been cleared.
Once the context manager exits, the warnings filter is restored to its state when the context was entered. This prevents tests from changing the warnings filter in unexpected ways between tests and leading to indeterminate test results.
> Note
> See [Concurrent safety of Context Managers](https://docs.python.org/3/library/warnings.html#warning-concurrent-safe) for details on the concurrency-safety of the [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") context manager when used in programs using multiple threads or async functions.
When testing multiple operations that raise the same kind of warning, it is important to test them in a manner that confirms each operation is raising a new warning (e.g. set warnings to be raised as exceptions and check the operations raise exceptions, check that the length of the warning list continues to increase after each operation, or else delete the previous entries from the warnings list before each new operation).
## Updating Code For New Versions of Dependencies[¶](https://docs.python.org/3/library/warnings.html#updating-code-for-new-versions-of-dependencies "Link to this heading")
Warning categories that are primarily of interest to Python developers (rather than end users of applications written in Python) are ignored by default.
Notably, this “ignored by default” list includes [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") (for every module except `__main__`), which means developers should make sure to test their code with typically ignored warnings made visible in order to receive timely notifications of future breaking API changes (whether in the standard library or third party packages).
In the ideal case, the code will have a suitable test suite, and the test runner will take care of implicitly enabling all warnings when running tests (the test runner provided by the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") module does this).
In less ideal cases, applications can be checked for use of deprecated interfaces by passing [`-Wd`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) to the Python interpreter (this is shorthand for `-W default`) or setting `PYTHONWARNINGS=default` in the environment. This enables default handling for all warnings, including those that are ignored by default. To change what action is taken for encountered warnings you can change what argument is passed to `-W` (e.g. `-W error`). See the `-W` flag for more details on what is possible.
## Available Functions[¶](https://docs.python.org/3/library/warnings.html#available-functions "Link to this heading")

warnings.warn(_message_ , _category =None_, _stacklevel =1_, _source =None_, _*_ , _skip_file_prefixes =()_)[¶](https://docs.python.org/3/library/warnings.html#warnings.warn "Link to this definition")

Issue a warning, or maybe ignore it or raise an exception. The _category_ argument, if given, must be a [warning category class](https://docs.python.org/3/library/warnings.html#warning-categories); it defaults to [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "UserWarning"). Alternatively, _message_ can be a [`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning") instance, in which case _category_ will be ignored and `message.__class__` will be used. In this case, the message text will be `str(message)`. This function raises an exception if the particular warning issued is changed into an error by the [warnings filter](https://docs.python.org/3/library/warnings.html#warning-filter). The _stacklevel_ argument can be used by wrapper functions written in Python, like this:
Copy```
def deprecated_api(message):
    warnings.warn(message, DeprecationWarning, stacklevel=2)

```

This makes the warning refer to `deprecated_api`’s caller, rather than to the source of `deprecated_api` itself (since the latter would defeat the purpose of the warning message).
The _skip_file_prefixes_ keyword argument can be used to indicate which stack frames are ignored when counting stack levels. This can be useful when you want the warning to always appear at call sites outside of a package when a constant _stacklevel_ does not fit all call paths or is otherwise challenging to maintain. If supplied, it must be a tuple of strings. When prefixes are supplied, stacklevel is implicitly overridden to be `max(2, stacklevel)`. To cause a warning to be attributed to the caller from outside of the current package you might write:
Copy```
# example/lower.py
_warn_skips = (os.path.dirname(__file__),)

def one_way(r_luxury_yacht=None, t_wobbler_mangrove=None):
    if r_luxury_yacht:
        warnings.warn("Please migrate to t_wobbler_mangrove=.",
                      skip_file_prefixes=_warn_skips)

# example/higher.py
from . import lower

def another_way(**kw):
    lower.one_way(**kw)

```

This makes the warning refer to both the `example.lower.one_way()` and `example.higher.another_way()` call sites only from calling code living outside of `example` package.
_source_ , if supplied, is the destroyed object which emitted a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning").
Changed in version 3.6: Added _source_ parameter.
Changed in version 3.12: Added _skip_file_prefixes_.

warnings.warn_explicit(_message_ , _category_ , _filename_ , _lineno_ , _module =None_, _registry =None_, _module_globals =None_, _source =None_)[¶](https://docs.python.org/3/library/warnings.html#warnings.warn_explicit "Link to this definition")

This is a low-level interface to the functionality of [`warn()`](https://docs.python.org/3/library/warnings.html#warnings.warn "warnings.warn"), passing in explicitly the message, category, filename and line number, and optionally other arguments. _message_ must be a string and _category_ a subclass of [`Warning`](https://docs.python.org/3/library/exceptions.html#Warning "Warning") or _message_ may be a `Warning` instance, in which case _category_ will be ignored.
_module_ , if supplied, should be the module name. If no module is passed, the filename with `.py` stripped is used.
_registry_ , if supplied, should be the `__warningregistry__` dictionary of the module. If no registry is passed, each warning is treated as the first occurrence, that is, filter actions `"default"`, `"module"` and `"once"` are handled as `"always"`.
_module_globals_ , if supplied, should be the global namespace in use by the code for which the warning is issued. (This argument is used to support displaying source for modules found in zipfiles or other non-filesystem import sources).
_source_ , if supplied, is the destroyed object which emitted a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning").
Changed in version 3.6: Add the _source_ parameter.

warnings.showwarning(_message_ , _category_ , _filename_ , _lineno_ , _file =None_, _line =None_)[¶](https://docs.python.org/3/library/warnings.html#warnings.showwarning "Link to this definition")

Write a warning to a file. The default implementation calls `formatwarning(message, category, filename, lineno, line)` and writes the resulting string to _file_ , which defaults to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"). You may replace this function with any callable by assigning to `warnings.showwarning`. _line_ is a line of source code to be included in the warning message; if _line_ is not supplied, `showwarning()` will try to read the line specified by _filename_ and _lineno_.

warnings.formatwarning(_message_ , _category_ , _filename_ , _lineno_ , _line =None_)[¶](https://docs.python.org/3/library/warnings.html#warnings.formatwarning "Link to this definition")

Format a warning the standard way. This returns a string which may contain embedded newlines and ends in a newline. _line_ is a line of source code to be included in the warning message; if _line_ is not supplied, `formatwarning()` will try to read the line specified by _filename_ and _lineno_.

warnings.filterwarnings(_action_ , _message =''_, _category =Warning_, _module =''_, _lineno =0_, _append =False_)[¶](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "Link to this definition")

Insert an entry into the list of [warnings filter specifications](https://docs.python.org/3/library/warnings.html#warning-filter). The entry is inserted at the front by default; if _append_ is true, it is inserted at the end. This checks the types of the arguments, compiles the _message_ and _module_ regular expressions, and inserts them as a tuple in the list of warnings filters. Entries closer to the front of the list override entries later in the list, if both match a particular warning. Omitted arguments default to a value that matches everything.

warnings.simplefilter(_action_ , _category =Warning_, _lineno =0_, _append =False_)[¶](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "Link to this definition")

Insert a simple entry into the list of [warnings filter specifications](https://docs.python.org/3/library/warnings.html#warning-filter). The meaning of the function parameters is as for [`filterwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings"), but regular expressions are not needed as the filter inserted always matches any message in any module as long as the category and line number match.

warnings.resetwarnings()[¶](https://docs.python.org/3/library/warnings.html#warnings.resetwarnings "Link to this definition")

Reset the warnings filter. This discards the effect of all previous calls to [`filterwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings"), including that of the [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) command line options and calls to [`simplefilter()`](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter").

@warnings.deprecated(_msg_ , _*_ , _category =DeprecationWarning_, _stacklevel =1_)[¶](https://docs.python.org/3/library/warnings.html#warnings.deprecated "Link to this definition")

Decorator to indicate that a class, function or overload is deprecated.
When this decorator is applied to an object, deprecation warnings may be emitted at runtime when the object is used. [static type checkers](https://docs.python.org/3/glossary.html#term-static-type-checker) will also generate a diagnostic on usage of the deprecated object.
Usage:
Copy```
from warnings import deprecated
from typing import overload

@deprecated("Use B instead")
class A:
    pass

@deprecated("Use g instead")
def f():
    pass

@overload
@deprecated("int support is deprecated")
def g(x: int) -> int: ...
@overload
def g(x: str) -> int: ...

```

The warning specified by _category_ will be emitted at runtime on use of deprecated objects. For functions, that happens on calls; for classes, on instantiation and on creation of subclasses. If the _category_ is `None`, no warning is emitted at runtime. The _stacklevel_ determines where the warning is emitted. If it is `1` (the default), the warning is emitted at the direct caller of the deprecated object; if it is higher, it is emitted further up the stack. Static type checker behavior is not affected by the _category_ and _stacklevel_ arguments.
The deprecation message passed to the decorator is saved in the `__deprecated__` attribute on the decorated object. If applied to an overload, the decorator must be after the [`@~typing.overload`](https://docs.python.org/3/library/typing.html#typing.overload "typing.overload") decorator for the attribute to exist on the overload as returned by [`typing.get_overloads()`](https://docs.python.org/3/library/typing.html#typing.get_overloads "typing.get_overloads").
Added in version 3.13: See [**PEP 702**](https://peps.python.org/pep-0702/).
## Available Context Managers[¶](https://docs.python.org/3/library/warnings.html#available-context-managers "Link to this heading")

_class_ warnings.catch_warnings(_*_ , _record =False_, _module =None_, _action =None_, _category =Warning_, _lineno =0_, _append =False_)[¶](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "Link to this definition")

A context manager that copies and, upon exit, restores the warnings filter and the [`showwarning()`](https://docs.python.org/3/library/warnings.html#warnings.showwarning "warnings.showwarning") function. If the _record_ argument is [`False`](https://docs.python.org/3/library/constants.html#False "False") (the default) the context manager returns [`None`](https://docs.python.org/3/library/constants.html#None "None") on entry. If _record_ is [`True`](https://docs.python.org/3/library/constants.html#True "True"), a list is returned that is progressively populated with objects as seen by a custom `showwarning()` function (which also suppresses output to `sys.stdout`). Each object in the list has attributes with the same names as the arguments to `showwarning()`.
The _module_ argument takes a module that will be used instead of the module returned when you import `warnings` whose filter will be protected. This argument exists primarily for testing the `warnings` module itself.
If the _action_ argument is not `None`, the remaining arguments are passed to [`simplefilter()`](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter") as if it were called immediately on entering the context.
See [The Warnings Filter](https://docs.python.org/3/library/warnings.html#warning-filter) for the meaning of the _category_ and _lineno_ parameters.
Note
See [Concurrent safety of Context Managers](https://docs.python.org/3/library/warnings.html#warning-concurrent-safe) for details on the concurrency-safety of the `catch_warnings` context manager when used in programs using multiple threads or async functions.
Changed in version 3.11: Added the _action_ , _category_ , _lineno_ , and _append_ parameters.
## Concurrent safety of Context Managers[¶](https://docs.python.org/3/library/warnings.html#concurrent-safety-of-context-managers "Link to this heading")
The behavior of [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") context manager depends on the [`sys.flags.context_aware_warnings`](https://docs.python.org/3/library/sys.html#sys.flags.context_aware_warnings "sys.flags.context_aware_warnings") flag. If the flag is true, the context manager behaves in a concurrent-safe fashion and otherwise not. Concurrent-safe means that it is both thread-safe and safe to use within [asyncio coroutines](https://docs.python.org/3/library/asyncio-task.html#coroutine) and tasks. Being thread-safe means that behavior is predictable in a multi-threaded program. The flag defaults to true for free-threaded builds and false otherwise.
If the [`context_aware_warnings`](https://docs.python.org/3/library/sys.html#sys.flags.context_aware_warnings "sys.flags.context_aware_warnings") flag is false, then [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") will modify the global attributes of the `warnings` module. This is not safe if used within a concurrent program (using multiple threads or using asyncio coroutines). For example, if two or more threads use the `catch_warnings` class at the same time, the behavior is undefined.
If the flag is true, [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") will not modify global attributes and will instead use a [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar") to store the newly established warning filtering state. A context variable provides thread-local storage and it makes the use of `catch_warnings` thread-safe.
The _record_ parameter of the context handler also behaves differently depending on the value of the flag. When _record_ is true and the flag is false, the context manager works by replacing and then later restoring the module’s [`showwarning()`](https://docs.python.org/3/library/warnings.html#warnings.showwarning "warnings.showwarning") function. That is not concurrent-safe.
When _record_ is true and the flag is true, the [`showwarning()`](https://docs.python.org/3/library/warnings.html#warnings.showwarning "warnings.showwarning") function is not replaced. Instead, the recording status is indicated by an internal property in the context variable. In this case, the `showwarning()` function will not be restored when exiting the context handler.
The [`context_aware_warnings`](https://docs.python.org/3/library/sys.html#sys.flags.context_aware_warnings "sys.flags.context_aware_warnings") flag can be set the [`-X context_aware_warnings`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command-line option or by the [`PYTHON_CONTEXT_AWARE_WARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS) environment variable.
> Note
> It is likely that most programs that desire thread-safe behaviour of the warnings module will also want to set the [`thread_inherit_context`](https://docs.python.org/3/library/sys.html#sys.flags.thread_inherit_context "sys.flags.thread_inherit_context") flag to true. That flag causes threads created by [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") to start with a copy of the context variables from the thread starting it. When true, the context established by [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") in one thread will also apply to new threads started by it. If false, new threads will start with an empty warnings context variable, meaning that any filtering that was established by a `catch_warnings` context manager will no longer be active.
Changed in version 3.14: Added the [`sys.flags.context_aware_warnings`](https://docs.python.org/3/library/sys.html#sys.flags.context_aware_warnings "sys.flags.context_aware_warnings") flag and the use of a context variable for [`catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings") if the flag is true. Previous versions of Python acted as if the flag was always set to false.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`warnings` — Warning control](https://docs.python.org/3/library/warnings.html)
    * [Warning Categories](https://docs.python.org/3/library/warnings.html#warning-categories)
    * [The Warnings Filter](https://docs.python.org/3/library/warnings.html#the-warnings-filter)
      * [Repeated Warning Suppression Criteria](https://docs.python.org/3/library/warnings.html#repeated-warning-suppression-criteria)
      * [Describing Warning Filters](https://docs.python.org/3/library/warnings.html#describing-warning-filters)
      * [Default Warning Filter](https://docs.python.org/3/library/warnings.html#default-warning-filter)
      * [Overriding the default filter](https://docs.python.org/3/library/warnings.html#overriding-the-default-filter)
    * [Temporarily Suppressing Warnings](https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings)
    * [Testing Warnings](https://docs.python.org/3/library/warnings.html#testing-warnings)
    * [Updating Code For New Versions of Dependencies](https://docs.python.org/3/library/warnings.html#updating-code-for-new-versions-of-dependencies)
    * [Available Functions](https://docs.python.org/3/library/warnings.html#available-functions)
    * [Available Context Managers](https://docs.python.org/3/library/warnings.html#available-context-managers)
    * [Concurrent safety of Context Managers](https://docs.python.org/3/library/warnings.html#concurrent-safety-of-context-managers)


#### Previous topic
[`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html "previous chapter")
#### Next topic
[`dataclasses` — Data Classes](https://docs.python.org/3/library/dataclasses.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=warnings+%E2%80%94+Warning+control&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwarnings.html&pagesource=library%2Fwarnings.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/dataclasses.html "dataclasses — Data Classes") |
  * [previous](https://docs.python.org/3/library/__main__.html "__main__ — Top-level code environment") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`warnings` — Warning control](https://docs.python.org/3/library/warnings.html#concurrent-safety-of-context-managers)
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
