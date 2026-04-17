[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html "previous chapter")
#### Next topic
[`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Generic+Operating+System+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fallos.html&pagesource=library%2Fallos.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/os.html "os — Miscellaneous operating system interfaces") |
  * [previous](https://docs.python.org/3/library/secrets.html "secrets — Generate secure random numbers for managing secrets") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html)
  * |
  * Theme  Auto Light Dark |


# Generic Operating System Services[¶](https://docs.python.org/3/library/allows.html#generic-operating-system-services "Link to this heading")
The modules described in this chapter provide interfaces to operating system features that are available on (almost) all operating systems, such as files and a clock. The interfaces are generally modeled after the Unix or C interfaces, but they are available on most other systems as well. Here’s an overview:
  * [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
    * [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3/library/os.html#file-names-command-line-arguments-and-environment-variables)
    * [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#python-utf-8-mode)
    * [Process Parameters](https://docs.python.org/3/library/os.html#process-parameters)
    * [File Object Creation](https://docs.python.org/3/library/os.html#file-object-creation)
    * [File Descriptor Operations](https://docs.python.org/3/library/os.html#file-descriptor-operations)
      * [Querying the size of a terminal](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal)
      * [Inheritance of File Descriptors](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors)
    * [Files and Directories](https://docs.python.org/3/library/os.html#files-and-directories)
      * [Timer File Descriptors](https://docs.python.org/3/library/os.html#timer-file-descriptors)
      * [Linux extended attributes](https://docs.python.org/3/library/os.html#linux-extended-attributes)
    * [Process Management](https://docs.python.org/3/library/os.html#process-management)
    * [Interface to the scheduler](https://docs.python.org/3/library/os.html#interface-to-the-scheduler)
    * [Miscellaneous System Information](https://docs.python.org/3/library/os.html#miscellaneous-system-information)
    * [Random numbers](https://docs.python.org/3/library/os.html#random-numbers)
  * [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html)
    * [Overview](https://docs.python.org/3/library/io.html#overview)
      * [Text I/O](https://docs.python.org/3/library/io.html#text-i-o)
      * [Binary I/O](https://docs.python.org/3/library/io.html#binary-i-o)
      * [Raw I/O](https://docs.python.org/3/library/io.html#raw-i-o)
    * [Text Encoding](https://docs.python.org/3/library/io.html#text-encoding)
      * [Opt-in EncodingWarning](https://docs.python.org/3/library/io.html#opt-in-encodingwarning)
    * [High-level Module Interface](https://docs.python.org/3/library/io.html#high-level-module-interface)
    * [Class hierarchy](https://docs.python.org/3/library/io.html#class-hierarchy)
      * [I/O Base Classes](https://docs.python.org/3/library/io.html#i-o-base-classes)
      * [Raw File I/O](https://docs.python.org/3/library/io.html#raw-file-i-o)
      * [Buffered Streams](https://docs.python.org/3/library/io.html#buffered-streams)
      * [Text I/O](https://docs.python.org/3/library/io.html#id1)
    * [Static Typing](https://docs.python.org/3/library/io.html#static-typing)
    * [Performance](https://docs.python.org/3/library/io.html#performance)
      * [Binary I/O](https://docs.python.org/3/library/io.html#id2)
      * [Text I/O](https://docs.python.org/3/library/io.html#id3)
      * [Multi-threading](https://docs.python.org/3/library/io.html#multi-threading)
      * [Reentrancy](https://docs.python.org/3/library/io.html#reentrancy)
  * [`time` — Time access and conversions](https://docs.python.org/3/library/time.html)
    * [Functions](https://docs.python.org/3/library/time.html#functions)
    * [Clock ID Constants](https://docs.python.org/3/library/time.html#clock-id-constants)
    * [Timezone Constants](https://docs.python.org/3/library/time.html#timezone-constants)
  * [`logging` — Logging facility for Python](https://docs.python.org/3/library/logging.html)
    * [Logger Objects](https://docs.python.org/3/library/logging.html#logger-objects)
    * [Logging Levels](https://docs.python.org/3/library/logging.html#logging-levels)
    * [Handler Objects](https://docs.python.org/3/library/logging.html#handler-objects)
    * [Formatter Objects](https://docs.python.org/3/library/logging.html#formatter-objects)
    * [Filter Objects](https://docs.python.org/3/library/logging.html#filter-objects)
    * [LogRecord Objects](https://docs.python.org/3/library/logging.html#logrecord-objects)
    * [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
    * [LoggerAdapter Objects](https://docs.python.org/3/library/logging.html#loggeradapter-objects)
    * [Thread Safety](https://docs.python.org/3/library/logging.html#thread-safety)
    * [Module-Level Functions](https://docs.python.org/3/library/logging.html#module-level-functions)
    * [Module-Level Attributes](https://docs.python.org/3/library/logging.html#module-level-attributes)
    * [Integration with the warnings module](https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module)
  * [`logging.config` — Logging configuration](https://docs.python.org/3/library/logging.config.html)
    * [Configuration functions](https://docs.python.org/3/library/logging.config.html#configuration-functions)
    * [Security considerations](https://docs.python.org/3/library/logging.config.html#security-considerations)
    * [Configuration dictionary schema](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema)
      * [Dictionary Schema Details](https://docs.python.org/3/library/logging.config.html#dictionary-schema-details)
      * [Incremental Configuration](https://docs.python.org/3/library/logging.config.html#incremental-configuration)
      * [Object connections](https://docs.python.org/3/library/logging.config.html#object-connections)
      * [User-defined objects](https://docs.python.org/3/library/logging.config.html#user-defined-objects)
      * [Handler configuration order](https://docs.python.org/3/library/logging.config.html#handler-configuration-order)
      * [Access to external objects](https://docs.python.org/3/library/logging.config.html#access-to-external-objects)
      * [Access to internal objects](https://docs.python.org/3/library/logging.config.html#access-to-internal-objects)
      * [Import resolution and custom importers](https://docs.python.org/3/library/logging.config.html#import-resolution-and-custom-importers)
      * [Configuring QueueHandler and QueueListener](https://docs.python.org/3/library/logging.config.html#configuring-queuehandler-and-queuelistener)
    * [Configuration file format](https://docs.python.org/3/library/logging.config.html#configuration-file-format)
  * [`logging.handlers` — Logging handlers](https://docs.python.org/3/library/logging.handlers.html)
    * [StreamHandler](https://docs.python.org/3/library/logging.handlers.html#streamhandler)
    * [FileHandler](https://docs.python.org/3/library/logging.handlers.html#filehandler)
    * [NullHandler](https://docs.python.org/3/library/logging.handlers.html#nullhandler)
    * [WatchedFileHandler](https://docs.python.org/3/library/logging.handlers.html#watchedfilehandler)
    * [BaseRotatingHandler](https://docs.python.org/3/library/logging.handlers.html#baserotatinghandler)
    * [RotatingFileHandler](https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler)
    * [TimedRotatingFileHandler](https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler)
    * [SocketHandler](https://docs.python.org/3/library/logging.handlers.html#sockethandler)
    * [DatagramHandler](https://docs.python.org/3/library/logging.handlers.html#datagramhandler)
    * [SysLogHandler](https://docs.python.org/3/library/logging.handlers.html#sysloghandler)
    * [NTEventLogHandler](https://docs.python.org/3/library/logging.handlers.html#nteventloghandler)
    * [SMTPHandler](https://docs.python.org/3/library/logging.handlers.html#smtphandler)
    * [MemoryHandler](https://docs.python.org/3/library/logging.handlers.html#memoryhandler)
    * [HTTPHandler](https://docs.python.org/3/library/logging.handlers.html#httphandler)
    * [QueueHandler](https://docs.python.org/3/library/logging.handlers.html#queuehandler)
    * [QueueListener](https://docs.python.org/3/library/logging.handlers.html#queuelistener)
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
  * [`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html)
  * [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
    * [ctypes tutorial](https://docs.python.org/3/library/ctypes.html#ctypes-tutorial)
      * [Loading dynamic link libraries](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries)
      * [Accessing functions from loaded dlls](https://docs.python.org/3/library/ctypes.html#accessing-functions-from-loaded-dlls)
      * [Calling functions](https://docs.python.org/3/library/ctypes.html#calling-functions)
      * [Fundamental data types](https://docs.python.org/3/library/ctypes.html#fundamental-data-types)
      * [Calling functions, continued](https://docs.python.org/3/library/ctypes.html#calling-functions-continued)
      * [Calling variadic functions](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions)
      * [Calling functions with your own custom data types](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types)
      * [Specifying the required argument types (function prototypes)](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes)
      * [Return types](https://docs.python.org/3/library/ctypes.html#return-types)
      * [Passing pointers (or: passing parameters by reference)](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference)
      * [Structures and unions](https://docs.python.org/3/library/ctypes.html#structures-and-unions)
      * [Structure/union layout, alignment and byte order](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order)
      * [Bit fields in structures and unions](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions)
      * [Arrays](https://docs.python.org/3/library/ctypes.html#arrays)
      * [Pointers](https://docs.python.org/3/library/ctypes.html#pointers)
      * [Thread safety without the GIL](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil)
      * [Type conversions](https://docs.python.org/3/library/ctypes.html#type-conversions)
      * [Incomplete Types](https://docs.python.org/3/library/ctypes.html#incomplete-types)
      * [Callback functions](https://docs.python.org/3/library/ctypes.html#callback-functions)
      * [Accessing values exported from dlls](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls)
      * [Surprises](https://docs.python.org/3/library/ctypes.html#surprises)
      * [Variable-sized data types](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types)
    * [ctypes reference](https://docs.python.org/3/library/ctypes.html#ctypes-reference)
      * [Finding shared libraries](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries)
      * [Listing loaded shared libraries](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries)
      * [Loading shared libraries](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries)
      * [Foreign functions](https://docs.python.org/3/library/ctypes.html#foreign-functions)
      * [Function prototypes](https://docs.python.org/3/library/ctypes.html#function-prototypes)
      * [Utility functions](https://docs.python.org/3/library/ctypes.html#utility-functions)
      * [Data types](https://docs.python.org/3/library/ctypes.html#data-types)
      * [Fundamental data types](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2)
      * [Structured data types](https://docs.python.org/3/library/ctypes.html#structured-data-types)
      * [Arrays and pointers](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers)
      * [Exceptions](https://docs.python.org/3/library/ctypes.html#exceptions)


#### Previous topic
[`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html "previous chapter")
#### Next topic
[`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Generic+Operating+System+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fallos.html&pagesource=library%2Fallos.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/os.html "os — Miscellaneous operating system interfaces") |
  * [previous](https://docs.python.org/3/library/secrets.html "secrets — Generate secure random numbers for managing secrets") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
