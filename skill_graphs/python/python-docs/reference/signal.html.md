[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
    * [General rules](https://docs.python.org/3/library/signal.html#general-rules)
      * [Execution of Python signal handlers](https://docs.python.org/3/library/signal.html#execution-of-python-signal-handlers)
      * [Signals and threads](https://docs.python.org/3/library/signal.html#signals-and-threads)
    * [Module contents](https://docs.python.org/3/library/signal.html#module-contents)
    * [Examples](https://docs.python.org/3/library/signal.html#examples)
    * [Note on SIGPIPE](https://docs.python.org/3/library/signal.html#note-on-sigpipe)
    * [Note on Signal Handlers and Exceptions](https://docs.python.org/3/library/signal.html#note-on-signal-handlers-and-exceptions)


#### Previous topic
[`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html "previous chapter")
#### Next topic
[`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=signal+%E2%80%94+Set+handlers+for+asynchronous+events&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsignal.html&pagesource=library%2Fsignal.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/mmap.html "mmap — Memory-mapped file support") |
  * [previous](https://docs.python.org/3/library/selectors.html "selectors — High-level I/O multiplexing") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
  * |
  * Theme  Auto Light Dark |


#  `signal` — Set handlers for asynchronous events[¶](https://docs.python.org/3/library/signal.html#module-signal "Link to this heading")
**Source code:**
* * *
This module provides mechanisms to use signal handlers in Python.
## General rules[¶](https://docs.python.org/3/library/signal.html#general-rules "Link to this heading")
The [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal") function allows defining custom handlers to be executed when a signal is received. A small number of default handlers are installed: [`SIGPIPE`](https://docs.python.org/3/library/signal.html#signal.SIGPIPE "signal.SIGPIPE") is ignored (so write errors on pipes and sockets can be reported as ordinary Python exceptions) and [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") is translated into a [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") exception if the parent process has not changed it.
A handler for a particular signal, once set, remains installed until it is explicitly reset (Python emulates the BSD style interface regardless of the underlying implementation), with the exception of the handler for [`SIGCHLD`](https://docs.python.org/3/library/signal.html#signal.SIGCHLD "signal.SIGCHLD"), which follows the underlying implementation.
On WebAssembly platforms, signals are emulated and therefore behave differently. Several functions and signals are not available on these platforms.
### Execution of Python signal handlers[¶](https://docs.python.org/3/library/signal.html#execution-of-python-signal-handlers "Link to this heading")
A Python signal handler does not get executed inside the low-level (C) signal handler. Instead, the low-level signal handler sets a flag which tells the [virtual machine](https://docs.python.org/3/glossary.html#term-virtual-machine) to execute the corresponding Python signal handler at a later point (for example, at the next [bytecode](https://docs.python.org/3/glossary.html#term-bytecode) instruction). This has consequences:
  * It makes little sense to catch synchronous errors like [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE") or [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV") that are caused by an invalid operation in C code. Python will return from the signal handler to the C code, which is likely to raise the same signal again, causing Python to apparently hang. From Python 3.3 onwards, you can use the [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.") module to report on synchronous errors.
  * A long-running calculation implemented purely in C (such as regular expression matching on a large body of text) may run uninterrupted for an arbitrary amount of time, regardless of any signals received. The Python signal handlers will be called when the calculation finishes.
  * If the handler raises an exception, it will be raised “out of thin air” in the main thread. See the [note below](https://docs.python.org/3/library/signal.html#handlers-and-exceptions) for a discussion.


### Signals and threads[¶](https://docs.python.org/3/library/signal.html#signals-and-threads "Link to this heading")
Python signal handlers are always executed in the main Python thread of the main interpreter, even if the signal was received in another thread. This means that signals can’t be used as a means of inter-thread communication. You can use the synchronization primitives from the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module instead.
Besides, only the main thread of the main interpreter is allowed to set a new signal handler.
Warning
Synchronization primitives such as [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") should not be used within signal handlers. Doing so can lead to unexpected deadlocks.
## Module contents[¶](https://docs.python.org/3/library/signal.html#module-contents "Link to this heading")
Changed in version 3.5: signal (SIG*), handler ([`SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL"), [`SIG_IGN`](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "signal.SIG_IGN")) and sigmask ([`SIG_BLOCK`](https://docs.python.org/3/library/signal.html#signal.SIG_BLOCK "signal.SIG_BLOCK"), [`SIG_UNBLOCK`](https://docs.python.org/3/library/signal.html#signal.SIG_UNBLOCK "signal.SIG_UNBLOCK"), [`SIG_SETMASK`](https://docs.python.org/3/library/signal.html#signal.SIG_SETMASK "signal.SIG_SETMASK")) related constants listed below were turned into [`enums`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") ([`Signals`](https://docs.python.org/3/library/signal.html#signal.Signals "signal.Signals"), [`Handlers`](https://docs.python.org/3/library/signal.html#signal.Handlers "signal.Handlers") and [`Sigmasks`](https://docs.python.org/3/library/signal.html#signal.Sigmasks "signal.Sigmasks") respectively). [`getsignal()`](https://docs.python.org/3/library/signal.html#signal.getsignal "signal.getsignal"), [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask"), [`sigpending()`](https://docs.python.org/3/library/signal.html#signal.sigpending "signal.sigpending") and [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait") functions return human-readable `enums` as `Signals` objects.
The signal module defines three enums:

_class_ signal.Signals[¶](https://docs.python.org/3/library/signal.html#signal.Signals "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of SIG* constants and the CTRL_* constants.
Added in version 3.5.

_class_ signal.Handlers[¶](https://docs.python.org/3/library/signal.html#signal.Handlers "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of the constants [`SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL") and [`SIG_IGN`](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "signal.SIG_IGN").
Added in version 3.5.

_class_ signal.Sigmasks[¶](https://docs.python.org/3/library/signal.html#signal.Sigmasks "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of the constants [`SIG_BLOCK`](https://docs.python.org/3/library/signal.html#signal.SIG_BLOCK "signal.SIG_BLOCK"), [`SIG_UNBLOCK`](https://docs.python.org/3/library/signal.html#signal.SIG_UNBLOCK "signal.SIG_UNBLOCK") and [`SIG_SETMASK`](https://docs.python.org/3/library/signal.html#signal.SIG_SETMASK "signal.SIG_SETMASK").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
Added in version 3.5.
The variables defined in the `signal` module are:

signal.SIG_DFL[¶](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "Link to this definition")

This is one of two standard signal handling options; it will simply perform the default function for the signal. For example, on most systems the default action for [`SIGQUIT`](https://docs.python.org/3/library/signal.html#signal.SIGQUIT "signal.SIGQUIT") is to dump core and exit, while the default action for [`SIGCHLD`](https://docs.python.org/3/library/signal.html#signal.SIGCHLD "signal.SIGCHLD") is to simply ignore it.

signal.SIG_IGN[¶](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "Link to this definition")

This is another standard signal handler, which will simply ignore the given signal.

signal.SIGABRT[¶](https://docs.python.org/3/library/signal.html#signal.SIGABRT "Link to this definition")

Abort signal from

signal.SIGALRM[¶](https://docs.python.org/3/library/signal.html#signal.SIGALRM "Link to this definition")

Timer signal from
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGBREAK[¶](https://docs.python.org/3/library/signal.html#signal.SIGBREAK "Link to this definition")

Interrupt from keyboard (CTRL + BREAK).
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

signal.SIGBUS[¶](https://docs.python.org/3/library/signal.html#signal.SIGBUS "Link to this definition")

Bus error (bad memory access).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGCHLD[¶](https://docs.python.org/3/library/signal.html#signal.SIGCHLD "Link to this definition")

Child process stopped or terminated.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGCLD[¶](https://docs.python.org/3/library/signal.html#signal.SIGCLD "Link to this definition")

Alias to [`SIGCHLD`](https://docs.python.org/3/library/signal.html#signal.SIGCHLD "signal.SIGCHLD").
[Availability](https://docs.python.org/3/library/intro.html#availability): not macOS.

signal.SIGCONT[¶](https://docs.python.org/3/library/signal.html#signal.SIGCONT "Link to this definition")

Continue the process if it is currently stopped
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGFPE[¶](https://docs.python.org/3/library/signal.html#signal.SIGFPE "Link to this definition")

Floating-point exception. For example, division by zero.
See also
[`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "ZeroDivisionError") is raised when the second argument of a division or modulo operation is zero.

signal.SIGHUP[¶](https://docs.python.org/3/library/signal.html#signal.SIGHUP "Link to this definition")

Hangup detected on controlling terminal or death of controlling process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGILL[¶](https://docs.python.org/3/library/signal.html#signal.SIGILL "Link to this definition")

Illegal instruction.

signal.SIGINT[¶](https://docs.python.org/3/library/signal.html#signal.SIGINT "Link to this definition")

Interrupt from keyboard (CTRL + C).
Default action is to raise [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt").

signal.SIGKILL[¶](https://docs.python.org/3/library/signal.html#signal.SIGKILL "Link to this definition")

Kill signal.
It cannot be caught, blocked, or ignored.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGPIPE[¶](https://docs.python.org/3/library/signal.html#signal.SIGPIPE "Link to this definition")

Broken pipe: write to pipe with no readers.
Default action is to ignore the signal.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGPROF[¶](https://docs.python.org/3/library/signal.html#signal.SIGPROF "Link to this definition")

Profiling timer expired.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGQUIT[¶](https://docs.python.org/3/library/signal.html#signal.SIGQUIT "Link to this definition")

Terminal quit signal.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGSEGV[¶](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "Link to this definition")

Segmentation fault: invalid memory reference.

signal.SIGSTOP[¶](https://docs.python.org/3/library/signal.html#signal.SIGSTOP "Link to this definition")

Stop executing (cannot be caught or ignored).

signal.SIGSTKFLT[¶](https://docs.python.org/3/library/signal.html#signal.SIGSTKFLT "Link to this definition")

Stack fault on coprocessor. The Linux kernel does not raise this signal: it can only be raised in user space.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux.
On architectures where the signal is available. See the man page
Added in version 3.11.

signal.SIGTERM[¶](https://docs.python.org/3/library/signal.html#signal.SIGTERM "Link to this definition")

Termination signal.

signal.SIGUSR1[¶](https://docs.python.org/3/library/signal.html#signal.SIGUSR1 "Link to this definition")

User-defined signal 1.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGUSR2[¶](https://docs.python.org/3/library/signal.html#signal.SIGUSR2 "Link to this definition")

User-defined signal 2.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGVTALRM[¶](https://docs.python.org/3/library/signal.html#signal.SIGVTALRM "Link to this definition")

Virtual timer expired.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGWINCH[¶](https://docs.python.org/3/library/signal.html#signal.SIGWINCH "Link to this definition")

Window resize signal.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.SIGXCPU[¶](https://docs.python.org/3/library/signal.html#signal.SIGXCPU "Link to this definition")

CPU time limit exceeded.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

SIG*

All the signal numbers are defined symbolically. For example, the hangup signal is defined as [`signal.SIGHUP`](https://docs.python.org/3/library/signal.html#signal.SIGHUP "signal.SIGHUP"); the variable names are identical to the names used in C programs, as found in `<signal.h>`. The Unix man page for ‘`signal`’ lists the existing signals (on some systems this is

signal.CTRL_C_EVENT[¶](https://docs.python.org/3/library/signal.html#signal.CTRL_C_EVENT "Link to this definition")

The signal corresponding to the `Ctrl`+`C` keystroke event. This signal can only be used with [`os.kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill").
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.2.

signal.CTRL_BREAK_EVENT[¶](https://docs.python.org/3/library/signal.html#signal.CTRL_BREAK_EVENT "Link to this definition")

The signal corresponding to the `Ctrl`+`Break` keystroke event. This signal can only be used with [`os.kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill").
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.2.

signal.NSIG[¶](https://docs.python.org/3/library/signal.html#signal.NSIG "Link to this definition")

One more than the number of the highest signal number. Use [`valid_signals()`](https://docs.python.org/3/library/signal.html#signal.valid_signals "signal.valid_signals") to get valid signal numbers.

signal.ITIMER_REAL[¶](https://docs.python.org/3/library/signal.html#signal.ITIMER_REAL "Link to this definition")

Decrements interval timer in real time, and delivers [`SIGALRM`](https://docs.python.org/3/library/signal.html#signal.SIGALRM "signal.SIGALRM") upon expiration.

signal.ITIMER_VIRTUAL[¶](https://docs.python.org/3/library/signal.html#signal.ITIMER_VIRTUAL "Link to this definition")

Decrements interval timer only when the process is executing, and delivers SIGVTALRM upon expiration.

signal.ITIMER_PROF[¶](https://docs.python.org/3/library/signal.html#signal.ITIMER_PROF "Link to this definition")

Decrements interval timer both when the process executes and when the system is executing on behalf of the process. Coupled with ITIMER_VIRTUAL, this timer is usually used to profile the time spent by the application in user and kernel space. SIGPROF is delivered upon expiration.

signal.SIG_BLOCK[¶](https://docs.python.org/3/library/signal.html#signal.SIG_BLOCK "Link to this definition")

A possible value for the _how_ parameter to [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask") indicating that signals are to be blocked.
Added in version 3.3.

signal.SIG_UNBLOCK[¶](https://docs.python.org/3/library/signal.html#signal.SIG_UNBLOCK "Link to this definition")

A possible value for the _how_ parameter to [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask") indicating that signals are to be unblocked.
Added in version 3.3.

signal.SIG_SETMASK[¶](https://docs.python.org/3/library/signal.html#signal.SIG_SETMASK "Link to this definition")

A possible value for the _how_ parameter to [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask") indicating that the signal mask is to be replaced.
Added in version 3.3.
The `signal` module defines one exception:

_exception_ signal.ItimerError[¶](https://docs.python.org/3/library/signal.html#signal.ItimerError "Link to this definition")

Raised to signal an error from the underlying [`setitimer()`](https://docs.python.org/3/library/signal.html#signal.setitimer "signal.setitimer") or [`getitimer()`](https://docs.python.org/3/library/signal.html#signal.getitimer "signal.getitimer") implementation. Expect this error if an invalid interval timer or a negative time is passed to `setitimer()`. This error is a subtype of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Added in version 3.3: This error used to be a subtype of [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError"), which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
The `signal` module defines the following functions:

signal.alarm(_time_)[¶](https://docs.python.org/3/library/signal.html#signal.alarm "Link to this definition")

If _time_ is non-zero, this function requests that a [`SIGALRM`](https://docs.python.org/3/library/signal.html#signal.SIGALRM "signal.SIGALRM") signal be sent to the process in _time_ seconds. Any previously scheduled alarm is canceled (only one alarm can be scheduled at any time). The returned value is then the number of seconds before any previously set alarm was to have been delivered. If _time_ is zero, no alarm is scheduled, and any scheduled alarm is canceled. If the return value is zero, no alarm is currently scheduled.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page

signal.getsignal(_signalnum_)[¶](https://docs.python.org/3/library/signal.html#signal.getsignal "Link to this definition")

Return the current signal handler for the signal _signalnum_. The returned value may be a callable Python object, or one of the special values [`signal.SIG_IGN`](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "signal.SIG_IGN"), [`signal.SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL") or [`None`](https://docs.python.org/3/library/constants.html#None "None"). Here, `signal.SIG_IGN` means that the signal was previously ignored, `signal.SIG_DFL` means that the default way of handling the signal was previously in use, and `None` means that the previous signal handler was not installed from Python.

signal.strsignal(_signalnum_)[¶](https://docs.python.org/3/library/signal.html#signal.strsignal "Link to this definition")

Returns the description of signal _signalnum_ , such as “Interrupt” for [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT"). Returns [`None`](https://docs.python.org/3/library/constants.html#None "None") if _signalnum_ has no description. Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _signalnum_ is invalid.
Added in version 3.8.

signal.valid_signals()[¶](https://docs.python.org/3/library/signal.html#signal.valid_signals "Link to this definition")

Return the set of valid signal numbers on this platform. This can be less than `range(1, NSIG)` if some signals are reserved by the system for internal use.
Added in version 3.8.

signal.pause()[¶](https://docs.python.org/3/library/signal.html#signal.pause "Link to this definition")

Cause the process to sleep until a signal is received; the appropriate handler will then be called. Returns nothing.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait"), [`sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo"), [`sigtimedwait()`](https://docs.python.org/3/library/signal.html#signal.sigtimedwait "signal.sigtimedwait") and [`sigpending()`](https://docs.python.org/3/library/signal.html#signal.sigpending "signal.sigpending").

signal.raise_signal(_signum_)[¶](https://docs.python.org/3/library/signal.html#signal.raise_signal "Link to this definition")

Sends a signal to the calling process. Returns nothing.
Added in version 3.8.

signal.pidfd_send_signal(_pidfd_ , _sig_ , _siginfo =None_, _flags =0_)[¶](https://docs.python.org/3/library/signal.html#signal.pidfd_send_signal "Link to this definition")

Send signal _sig_ to the process referred to by file descriptor _pidfd_. Python does not currently support the _siginfo_ parameter; it must be `None`. The _flags_ argument is provided for future extensions; no flag values are currently defined.
See the
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 5.1, Android >= [`build-time`](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "sys.getandroidapilevel") API level 31
Added in version 3.9.

signal.pthread_kill(_thread_id_ , _signalnum_)[¶](https://docs.python.org/3/library/signal.html#signal.pthread_kill "Link to this definition")

Send the signal _signalnum_ to the thread _thread_id_ , another thread in the same process as the caller. The target thread can be executing any code (Python or not). However, if the target thread is executing the Python interpreter, the Python signal handlers will be [executed by the main thread of the main interpreter](https://docs.python.org/3/library/signal.html#signals-and-threads). Therefore, the only point of sending a signal to a particular Python thread would be to force a running system call to fail with [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").
Use [`threading.get_ident()`](https://docs.python.org/3/library/threading.html#threading.get_ident "threading.get_ident") or the [`ident`](https://docs.python.org/3/library/threading.html#threading.Thread.ident "threading.Thread.ident") attribute of [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") objects to get a suitable value for _thread_id_.
If _signalnum_ is 0, then no signal is sent, but error checking is still performed; this can be used to check if the target thread is still running.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `signal.pthread_kill` with arguments `thread_id`, `signalnum`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`os.kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill").
Added in version 3.3.

signal.pthread_sigmask(_how_ , _mask_)[¶](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "Link to this definition")

Fetch and/or change the signal mask of the calling thread. The signal mask is the set of signals whose delivery is currently blocked for the caller. Return the old signal mask as a set of signals.
The behavior of the call is dependent on the value of _how_ , as follows.
  * [`SIG_BLOCK`](https://docs.python.org/3/library/signal.html#signal.SIG_BLOCK "signal.SIG_BLOCK"): The set of blocked signals is the union of the current set and the _mask_ argument.
  * [`SIG_UNBLOCK`](https://docs.python.org/3/library/signal.html#signal.SIG_UNBLOCK "signal.SIG_UNBLOCK"): The signals in _mask_ are removed from the current set of blocked signals. It is permissible to attempt to unblock a signal which is not blocked.
  * [`SIG_SETMASK`](https://docs.python.org/3/library/signal.html#signal.SIG_SETMASK "signal.SIG_SETMASK"): The set of blocked signals is set to the _mask_ argument.


_mask_ is a set of signal numbers (e.g. {[`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT"), [`signal.SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM")}). Use [`valid_signals()`](https://docs.python.org/3/library/signal.html#signal.valid_signals "signal.valid_signals") for a full mask including all signals.
For example, `signal.pthread_sigmask(signal.SIG_BLOCK, [])` reads the signal mask of the calling thread.
[`SIGKILL`](https://docs.python.org/3/library/signal.html#signal.SIGKILL "signal.SIGKILL") and [`SIGSTOP`](https://docs.python.org/3/library/signal.html#signal.SIGSTOP "signal.SIGSTOP") cannot be blocked.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`pause()`](https://docs.python.org/3/library/signal.html#signal.pause "signal.pause"), [`sigpending()`](https://docs.python.org/3/library/signal.html#signal.sigpending "signal.sigpending") and [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait").
Added in version 3.3.

signal.setitimer(_which_ , _seconds_ , _interval =0.0_)[¶](https://docs.python.org/3/library/signal.html#signal.setitimer "Link to this definition")

Sets given interval timer (one of [`signal.ITIMER_REAL`](https://docs.python.org/3/library/signal.html#signal.ITIMER_REAL "signal.ITIMER_REAL"), [`signal.ITIMER_VIRTUAL`](https://docs.python.org/3/library/signal.html#signal.ITIMER_VIRTUAL "signal.ITIMER_VIRTUAL") or [`signal.ITIMER_PROF`](https://docs.python.org/3/library/signal.html#signal.ITIMER_PROF "signal.ITIMER_PROF")) specified by _which_ to fire after _seconds_ (float is accepted, different from [`alarm()`](https://docs.python.org/3/library/signal.html#signal.alarm "signal.alarm")) and after that every _interval_ seconds (if _interval_ is non-zero). The interval timer specified by _which_ can be cleared by setting _seconds_ to zero.
When an interval timer fires, a signal is sent to the process. The signal sent is dependent on the timer being used; [`signal.ITIMER_REAL`](https://docs.python.org/3/library/signal.html#signal.ITIMER_REAL "signal.ITIMER_REAL") will deliver [`SIGALRM`](https://docs.python.org/3/library/signal.html#signal.SIGALRM "signal.SIGALRM"), [`signal.ITIMER_VIRTUAL`](https://docs.python.org/3/library/signal.html#signal.ITIMER_VIRTUAL "signal.ITIMER_VIRTUAL") sends [`SIGVTALRM`](https://docs.python.org/3/library/signal.html#signal.SIGVTALRM "signal.SIGVTALRM"), and [`signal.ITIMER_PROF`](https://docs.python.org/3/library/signal.html#signal.ITIMER_PROF "signal.ITIMER_PROF") will deliver [`SIGPROF`](https://docs.python.org/3/library/signal.html#signal.SIGPROF "signal.SIGPROF").
The old values are returned as a tuple: (delay, interval).
Attempting to pass an invalid interval timer will cause an [`ItimerError`](https://docs.python.org/3/library/signal.html#signal.ItimerError "signal.ItimerError").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.getitimer(_which_)[¶](https://docs.python.org/3/library/signal.html#signal.getitimer "Link to this definition")

Returns current value of a given interval timer specified by _which_.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

signal.set_wakeup_fd(_fd_ , _*_ , _warn_on_full_buffer =True_)[¶](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "Link to this definition")

Set the wakeup file descriptor to _fd_. When a signal your program has registered a signal handler for is received, the signal number is written as a single byte into the fd. If you haven’t registered a signal handler for the signals you care about, then nothing will be written to the wakeup fd. This can be used by a library to wakeup a poll or select call, allowing the signal to be fully processed.
The old wakeup fd is returned (or -1 if file descriptor wakeup was not enabled). If _fd_ is -1, file descriptor wakeup is disabled. If not -1, _fd_ must be non-blocking. It is up to the library to remove any bytes from _fd_ before calling poll or select again.
When threads are enabled, this function can only be called from [the main thread of the main interpreter](https://docs.python.org/3/library/signal.html#signals-and-threads); attempting to call it from other threads will cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception to be raised.
There are two common ways to use this function. In both approaches, you use the fd to wake up when a signal arrives, but then they differ in how they determine _which_ signal or signals have arrived.
In the first approach, we read the data out of the fd’s buffer, and the byte values give you the signal numbers. This is simple, but in rare cases it can run into a problem: generally the fd will have a limited amount of buffer space, and if too many signals arrive too quickly, then the buffer may become full, and some signals may be lost. If you use this approach, then you should set `warn_on_full_buffer=True`, which will at least cause a warning to be printed to stderr when signals are lost.
In the second approach, we use the wakeup fd _only_ for wakeups, and ignore the actual byte values. In this case, all we care about is whether the fd’s buffer is empty or non-empty; a full buffer doesn’t indicate a problem at all. If you use this approach, then you should set `warn_on_full_buffer=False`, so that your users are not confused by spurious warning messages.
Changed in version 3.5: On Windows, the function now also supports socket handles.
Changed in version 3.7: Added `warn_on_full_buffer` parameter.

signal.siginterrupt(_signalnum_ , _flag_)[¶](https://docs.python.org/3/library/signal.html#signal.siginterrupt "Link to this definition")

Change system call restart behaviour: if _flag_ is [`False`](https://docs.python.org/3/library/constants.html#False "False"), system calls will be restarted when interrupted by signal _signalnum_ , otherwise system calls will be interrupted. Returns nothing.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
Note that installing a signal handler with [`signal()`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") will reset the restart behaviour to interruptible by implicitly calling `siginterrupt()` with a true _flag_ value for the given signal.

signal.signal(_signalnum_ , _handler_)[¶](https://docs.python.org/3/library/signal.html#signal.signal "Link to this definition")

Set the handler for signal _signalnum_ to the function _handler_. _handler_ can be a callable Python object taking two arguments (see below), or one of the special values [`signal.SIG_IGN`](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "signal.SIG_IGN") or [`signal.SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL"). The previous signal handler will be returned (see the description of [`getsignal()`](https://docs.python.org/3/library/signal.html#signal.getsignal "signal.getsignal") above). (See the Unix man page
When threads are enabled, this function can only be called from [the main thread of the main interpreter](https://docs.python.org/3/library/signal.html#signals-and-threads); attempting to call it from other threads will cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception to be raised.
The _handler_ is called with two arguments: the signal number and the current stack frame (`None` or a frame object; for a description of frame objects, see the [description in the type hierarchy](https://docs.python.org/3/reference/datamodel.html#frame-objects) or see the attribute descriptions in the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.") module).
On Windows, `signal()` can only be called with [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT"), [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE"), [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL"), [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT"), [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV"), [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM"), or [`SIGBREAK`](https://docs.python.org/3/library/signal.html#signal.SIGBREAK "signal.SIGBREAK"). A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised in any other case. Note that not all systems define the same set of signal names; an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") will be raised if a signal name is not defined as `SIG*` module level constant.

signal.sigpending()[¶](https://docs.python.org/3/library/signal.html#signal.sigpending "Link to this definition")

Examine the set of signals that are pending for delivery to the calling thread (i.e., the signals which have been raised while blocked). Return the set of the pending signals.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`pause()`](https://docs.python.org/3/library/signal.html#signal.pause "signal.pause"), [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask") and [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait").
Added in version 3.3.

signal.sigwait(_sigset_)[¶](https://docs.python.org/3/library/signal.html#signal.sigwait "Link to this definition")

Suspend execution of the calling thread until the delivery of one of the signals specified in the signal set _sigset_. The function accepts the signal (removes it from the pending list of signals), and returns the signal number.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`pause()`](https://docs.python.org/3/library/signal.html#signal.pause "signal.pause"), [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask"), [`sigpending()`](https://docs.python.org/3/library/signal.html#signal.sigpending "signal.sigpending"), [`sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo") and [`sigtimedwait()`](https://docs.python.org/3/library/signal.html#signal.sigtimedwait "signal.sigtimedwait").
Added in version 3.3.

signal.sigwaitinfo(_sigset_)[¶](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "Link to this definition")

Suspend execution of the calling thread until the delivery of one of the signals specified in the signal set _sigset_. The function accepts the signal and removes it from the pending list of signals. If one of the signals in _sigset_ is already pending for the calling thread, the function will return immediately with information about that signal. The signal handler is not called for the delivered signal. The function raises an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") if it is interrupted by a signal that is not in _sigset_.
The return value is an object representing the data contained in the `siginfo_t` structure, namely: `si_signo`, `si_code`, `si_errno`, `si_pid`, `si_uid`, `si_status`, `si_band`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`pause()`](https://docs.python.org/3/library/signal.html#signal.pause "signal.pause"), [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait") and [`sigtimedwait()`](https://docs.python.org/3/library/signal.html#signal.sigtimedwait "signal.sigtimedwait").
Added in version 3.3.
Changed in version 3.5: The function is now retried if interrupted by a signal not in _sigset_ and the signal handler does not raise an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

signal.sigtimedwait(_sigset_ , _timeout_)[¶](https://docs.python.org/3/library/signal.html#signal.sigtimedwait "Link to this definition")

Like [`sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo"), but takes an additional _timeout_ argument specifying a timeout. If _timeout_ is specified as `0`, a poll is performed. Returns [`None`](https://docs.python.org/3/library/constants.html#None "None") if a timeout occurs.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
See the man page
See also [`pause()`](https://docs.python.org/3/library/signal.html#signal.pause "signal.pause"), [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait") and [`sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo").
Added in version 3.3.
Changed in version 3.5: The function is now retried with the recomputed _timeout_ if interrupted by a signal not in _sigset_ and the signal handler does not raise an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).
## Examples[¶](https://docs.python.org/3/library/signal.html#examples "Link to this heading")
Here is a minimal example program. It uses the [`alarm()`](https://docs.python.org/3/library/signal.html#signal.alarm "signal.alarm") function to limit the time spent waiting to open a file; this is useful if the file is for a serial device that may not be turned on, which would normally cause the [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") to hang indefinitely. The solution is to set a 5-second alarm before opening the file; if the operation takes too long, the alarm signal will be sent, and the handler raises an exception.
Copy```
import signal, os

def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f'Signal handler called with signal {signame} ({signum})')
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

```

## Note on SIGPIPE[¶](https://docs.python.org/3/library/signal.html#note-on-sigpipe "Link to this heading")
Piping output of your program to tools like [`SIGPIPE`](https://docs.python.org/3/library/signal.html#signal.SIGPIPE "signal.SIGPIPE") signal to be sent to your process when the receiver of its standard output closes early. This results in an exception like `BrokenPipeError: [Errno 32] Broken pipe`. To handle this case, wrap your entry point to catch this exception as follows:
Copy```
import os
import sys

def main():
    try:
        # simulate large output (your code replaces this loop)
        for x in range(10000):
            print("y")
        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.
        sys.stdout.flush()
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE

if __name__ == '__main__':
    main()

```

Do not set [`SIGPIPE`](https://docs.python.org/3/library/signal.html#signal.SIGPIPE "signal.SIGPIPE")’s disposition to [`SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL") in order to avoid [`BrokenPipeError`](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "BrokenPipeError"). Doing that would cause your program to exit unexpectedly whenever any socket connection is interrupted while your program is still writing to it.
## Note on Signal Handlers and Exceptions[¶](https://docs.python.org/3/library/signal.html#note-on-signal-handlers-and-exceptions "Link to this heading")
If a signal handler raises an exception, the exception will be propagated to the main thread and may be raised after any [bytecode](https://docs.python.org/3/glossary.html#term-bytecode) instruction. Most notably, a [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") may appear at any point during execution. Most Python code, including the standard library, cannot be made robust against this, and so a `KeyboardInterrupt` (or any other exception resulting from a signal handler) may on rare occasions put the program in an unexpected state.
To illustrate this issue, consider the following code:
Copy```
class SpamContext:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        # If KeyboardInterrupt occurs here, everything is fine
        self.lock.acquire()
        # If KeyboardInterrupt occurs here, __exit__ will not be called
        ...
        # KeyboardInterrupt could occur just before the function returns

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
        self.lock.release()

```

For many programs, especially those that merely want to exit on [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt"), this is not a problem, but applications that are complex or require high reliability should avoid raising exceptions from signal handlers. They should also avoid catching `KeyboardInterrupt` as a means of gracefully shutting down. Instead, they should install their own [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") handler. Below is an example of an HTTP server that avoids `KeyboardInterrupt`:
Copy```
import signal
import socket
from selectors import DefaultSelector, EVENT_READ
from http.server import HTTPServer, SimpleHTTPRequestHandler

interrupt_read, interrupt_write = socket.socketpair()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    interrupt_write.send(b'\0')
signal.signal(signal.SIGINT, handler)

def serve_forever(httpd):
    sel = DefaultSelector()
    sel.register(interrupt_read, EVENT_READ)
    sel.register(httpd, EVENT_READ)

    while True:
        for key, _ in sel.select():
            if key.fileobj == interrupt_read:
                interrupt_read.recv(1)
                return
            if key.fileobj == httpd:
                httpd.handle_request()

print("Serving on port 8000")
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
serve_forever(httpd)
print("Shutdown...")

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
    * [General rules](https://docs.python.org/3/library/signal.html#general-rules)
      * [Execution of Python signal handlers](https://docs.python.org/3/library/signal.html#execution-of-python-signal-handlers)
      * [Signals and threads](https://docs.python.org/3/library/signal.html#signals-and-threads)
    * [Module contents](https://docs.python.org/3/library/signal.html#module-contents)
    * [Examples](https://docs.python.org/3/library/signal.html#examples)
    * [Note on SIGPIPE](https://docs.python.org/3/library/signal.html#note-on-sigpipe)
    * [Note on Signal Handlers and Exceptions](https://docs.python.org/3/library/signal.html#note-on-signal-handlers-and-exceptions)


#### Previous topic
[`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html "previous chapter")
#### Next topic
[`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=signal+%E2%80%94+Set+handlers+for+asynchronous+events&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsignal.html&pagesource=library%2Fsignal.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/mmap.html "mmap — Memory-mapped file support") |
  * [previous](https://docs.python.org/3/library/selectors.html "selectors — High-level I/O multiplexing") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
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
