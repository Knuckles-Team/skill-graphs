[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
    * [Examples](https://docs.python.org/3/library/syslog.html#examples)
      * [Simple example](https://docs.python.org/3/library/syslog.html#simple-example)


#### Previous topic
[`resource` — Resource usage information](https://docs.python.org/3/library/resource.html "previous chapter")
#### Next topic
[Modules command-line interface (CLI)](https://docs.python.org/3/library/cmdline.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=syslog+%E2%80%94+Unix+syslog+library+routines&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsyslog.html&pagesource=library%2Fsyslog.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/cmdline.html "Modules command-line interface \(CLI\)") |
  * [previous](https://docs.python.org/3/library/resource.html "resource — Resource usage information") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
  * |
  * Theme  Auto Light Dark |


#  `syslog` — Unix syslog library routines[¶](https://docs.python.org/3/library/syslog.html#module-syslog "Link to this heading")
* * *
This module provides an interface to the Unix `syslog` library routines. Refer to the Unix manual pages for a detailed description of the `syslog` facility.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not iOS.
This module wraps the system `syslog` family of routines. A pure Python library that can speak to a syslog server is available in the [`logging.handlers`](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.") module as [`SysLogHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler "logging.handlers.SysLogHandler").
The module defines the following functions:

syslog.syslog(_message_)[¶](https://docs.python.org/3/library/syslog.html#syslog.syslog "Link to this definition")


syslog.syslog(_priority_ , _message_)

Send the string _message_ to the system logger. A trailing newline is added if necessary. Each message is tagged with a priority composed of a _facility_ and a _level_. The optional _priority_ argument, which defaults to [`LOG_INFO`](https://docs.python.org/3/library/syslog.html#syslog.LOG_INFO "syslog.LOG_INFO"), determines the message priority. If the facility is not encoded in _priority_ using logical-or (`LOG_INFO | LOG_USER`), the value given in the [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") call is used.
If [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") has not been called prior to the call to `syslog()`, `openlog()` will be called with no arguments.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `syslog.syslog` with arguments `priority`, `message`.
Changed in version 3.2: In previous versions, [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") would not be called automatically if it wasn’t called prior to the call to `syslog()`, deferring to the syslog implementation to call `openlog()`.
Changed in version 3.12: This function is restricted in subinterpreters. (Only code that runs in multiple interpreters is affected and the restriction is not relevant for most users.) [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") must be called in the main interpreter before `syslog()` may be used in a subinterpreter. Otherwise it will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").

syslog.openlog([_ident_[, _logoption_[, _facility_]]])[¶](https://docs.python.org/3/library/syslog.html#syslog.openlog "Link to this definition")

Logging options of subsequent [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines.") calls can be set by calling `openlog()`. `syslog()` will call `openlog()` with no arguments if the log is not currently open.
The optional _ident_ keyword argument is a string which is prepended to every message, and defaults to `sys.argv[0]` with leading path components stripped. The optional _logoption_ keyword argument (default is 0) is a bit field – see below for possible values to combine. The optional _facility_ keyword argument (default is [`LOG_USER`](https://docs.python.org/3/library/syslog.html#syslog.LOG_USER "syslog.LOG_USER")) sets the default facility for messages which do not have a facility explicitly encoded.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `syslog.openlog` with arguments `ident`, `logoption`, `facility`.
Changed in version 3.2: In previous versions, keyword arguments were not allowed, and _ident_ was required.
Changed in version 3.12: This function is restricted in subinterpreters. (Only code that runs in multiple interpreters is affected and the restriction is not relevant for most users.) This may only be called in the main interpreter. It will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if called in a subinterpreter.

syslog.closelog()[¶](https://docs.python.org/3/library/syslog.html#syslog.closelog "Link to this definition")

Reset the syslog module values and call the system library `closelog()`.
This causes the module to behave as it does when initially imported. For example, [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") will be called on the first [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines.") call (if `openlog()` hasn’t already been called), and _ident_ and other `openlog()` parameters are reset to defaults.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `syslog.closelog` with no arguments.
Changed in version 3.12: This function is restricted in subinterpreters. (Only code that runs in multiple interpreters is affected and the restriction is not relevant for most users.) This may only be called in the main interpreter. It will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if called in a subinterpreter.

syslog.setlogmask(_maskpri_)[¶](https://docs.python.org/3/library/syslog.html#syslog.setlogmask "Link to this definition")

Set the priority mask to _maskpri_ and return the previous mask value. Calls to [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines.") with a priority level not set in _maskpri_ are ignored. The default is to log all priorities. The function `LOG_MASK(pri)` calculates the mask for the individual priority _pri_. The function `LOG_UPTO(pri)` calculates the mask for all priorities up to and including _pri_.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `syslog.setlogmask` with argument `maskpri`.
The module defines the following constants:

syslog.LOG_EMERG[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_EMERG "Link to this definition")


syslog.LOG_ALERT[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_ALERT "Link to this definition")


syslog.LOG_CRIT[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_CRIT "Link to this definition")


syslog.LOG_ERR[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_ERR "Link to this definition")


syslog.LOG_WARNING[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_WARNING "Link to this definition")


syslog.LOG_NOTICE[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NOTICE "Link to this definition")


syslog.LOG_INFO[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_INFO "Link to this definition")


syslog.LOG_DEBUG[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_DEBUG "Link to this definition")

Priority levels (high to low).

syslog.LOG_AUTH[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_AUTH "Link to this definition")


syslog.LOG_AUTHPRIV[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_AUTHPRIV "Link to this definition")


syslog.LOG_CRON[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_CRON "Link to this definition")


syslog.LOG_DAEMON[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_DAEMON "Link to this definition")


syslog.LOG_FTP[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_FTP "Link to this definition")


syslog.LOG_INSTALL[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_INSTALL "Link to this definition")


syslog.LOG_KERN[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_KERN "Link to this definition")


syslog.LOG_LAUNCHD[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LAUNCHD "Link to this definition")


syslog.LOG_LPR[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LPR "Link to this definition")


syslog.LOG_MAIL[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_MAIL "Link to this definition")


syslog.LOG_NETINFO[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NETINFO "Link to this definition")


syslog.LOG_NEWS[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NEWS "Link to this definition")


syslog.LOG_RAS[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_RAS "Link to this definition")


syslog.LOG_REMOTEAUTH[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_REMOTEAUTH "Link to this definition")


syslog.LOG_SYSLOG[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_SYSLOG "Link to this definition")


syslog.LOG_USER[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_USER "Link to this definition")


syslog.LOG_UUCP[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_UUCP "Link to this definition")


syslog.LOG_LOCAL0[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL0 "Link to this definition")


syslog.LOG_LOCAL1[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL1 "Link to this definition")


syslog.LOG_LOCAL2[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL2 "Link to this definition")


syslog.LOG_LOCAL3[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL3 "Link to this definition")


syslog.LOG_LOCAL4[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL4 "Link to this definition")


syslog.LOG_LOCAL5[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL5 "Link to this definition")


syslog.LOG_LOCAL6[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL6 "Link to this definition")


syslog.LOG_LOCAL7[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL7 "Link to this definition")

Facilities, depending on availability in `<syslog.h>` for [`LOG_AUTHPRIV`](https://docs.python.org/3/library/syslog.html#syslog.LOG_AUTHPRIV "syslog.LOG_AUTHPRIV"), [`LOG_FTP`](https://docs.python.org/3/library/syslog.html#syslog.LOG_FTP "syslog.LOG_FTP"), [`LOG_NETINFO`](https://docs.python.org/3/library/syslog.html#syslog.LOG_NETINFO "syslog.LOG_NETINFO"), [`LOG_REMOTEAUTH`](https://docs.python.org/3/library/syslog.html#syslog.LOG_REMOTEAUTH "syslog.LOG_REMOTEAUTH"), [`LOG_INSTALL`](https://docs.python.org/3/library/syslog.html#syslog.LOG_INSTALL "syslog.LOG_INSTALL") and [`LOG_RAS`](https://docs.python.org/3/library/syslog.html#syslog.LOG_RAS "syslog.LOG_RAS").
Changed in version 3.13: Added [`LOG_FTP`](https://docs.python.org/3/library/syslog.html#syslog.LOG_FTP "syslog.LOG_FTP"), [`LOG_NETINFO`](https://docs.python.org/3/library/syslog.html#syslog.LOG_NETINFO "syslog.LOG_NETINFO"), [`LOG_REMOTEAUTH`](https://docs.python.org/3/library/syslog.html#syslog.LOG_REMOTEAUTH "syslog.LOG_REMOTEAUTH"), [`LOG_INSTALL`](https://docs.python.org/3/library/syslog.html#syslog.LOG_INSTALL "syslog.LOG_INSTALL"), [`LOG_RAS`](https://docs.python.org/3/library/syslog.html#syslog.LOG_RAS "syslog.LOG_RAS"), and [`LOG_LAUNCHD`](https://docs.python.org/3/library/syslog.html#syslog.LOG_LAUNCHD "syslog.LOG_LAUNCHD").

syslog.LOG_PID[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_PID "Link to this definition")


syslog.LOG_CONS[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_CONS "Link to this definition")


syslog.LOG_NDELAY[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NDELAY "Link to this definition")


syslog.LOG_ODELAY[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_ODELAY "Link to this definition")


syslog.LOG_NOWAIT[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NOWAIT "Link to this definition")


syslog.LOG_PERROR[¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_PERROR "Link to this definition")

Log options, depending on availability in `<syslog.h>` for [`LOG_ODELAY`](https://docs.python.org/3/library/syslog.html#syslog.LOG_ODELAY "syslog.LOG_ODELAY"), [`LOG_NOWAIT`](https://docs.python.org/3/library/syslog.html#syslog.LOG_NOWAIT "syslog.LOG_NOWAIT") and [`LOG_PERROR`](https://docs.python.org/3/library/syslog.html#syslog.LOG_PERROR "syslog.LOG_PERROR").
## Examples[¶](https://docs.python.org/3/library/syslog.html#examples "Link to this heading")
### Simple example[¶](https://docs.python.org/3/library/syslog.html#simple-example "Link to this heading")
A simple set of examples:
Copy```
import syslog

syslog.syslog('Processing started')
if error:
    syslog.syslog(syslog.LOG_ERR, 'Processing started')

```

An example of setting some log options, these would include the process ID in logged messages, and write the messages to the destination facility used for mail logging:
Copy```
syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
syslog.syslog('E-mail processing initiated...')

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
    * [Examples](https://docs.python.org/3/library/syslog.html#examples)
      * [Simple example](https://docs.python.org/3/library/syslog.html#simple-example)


#### Previous topic
[`resource` — Resource usage information](https://docs.python.org/3/library/resource.html "previous chapter")
#### Next topic
[Modules command-line interface (CLI)](https://docs.python.org/3/library/cmdline.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=syslog+%E2%80%94+Unix+syslog+library+routines&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsyslog.html&pagesource=library%2Fsyslog.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/cmdline.html "Modules command-line interface \(CLI\)") |
  * [previous](https://docs.python.org/3/library/resource.html "resource — Resource usage information") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
