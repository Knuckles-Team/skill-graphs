[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html)
    * [POP3 Objects](https://docs.python.org/3/library/poplib.html#pop3-objects)
    * [POP3 Example](https://docs.python.org/3/library/poplib.html#pop3-example)


#### Previous topic
[`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html "previous chapter")
#### Next topic
[`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=poplib+%E2%80%94+POP3+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpoplib.html&pagesource=library%2Fpoplib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/imaplib.html "imaplib — IMAP4 protocol client") |
  * [previous](https://docs.python.org/3/library/ftplib.html "ftplib — FTP protocol client") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html)
  * |
  * Theme  Auto Light Dark |


#  `poplib` — POP3 protocol client[¶](https://docs.python.org/3/library/poplib.html#module-poplib "Link to this heading")
**Source code:**
* * *
This module defines a class, [`POP3`](https://docs.python.org/3/library/poplib.html#poplib.POP3 "poplib.POP3"), which encapsulates a connection to a POP3 server and implements the protocol as defined in `POP3` class supports both the minimal and optional command sets from `POP3` class also supports the `STLS` command introduced in
Additionally, this module provides a class [`POP3_SSL`](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL "poplib.POP3_SSL"), which provides support for connecting to POP3 servers that use SSL as an underlying protocol layer.
Note that POP3, though widely supported, is obsolescent. The implementation quality of POP3 servers varies widely, and too many are quite poor. If your mailserver supports IMAP, you would be better off using the [`imaplib.IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") class, as IMAP servers tend to be better implemented.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
The `poplib` module provides two classes:

_class_ poplib.POP3(_host_ , _port=POP3_PORT_[, _timeout_])[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3 "Link to this definition")

This class implements the actual POP3 protocol. The connection is created when the instance is initialized. If _port_ is omitted, the standard POP3 port (110) is used. The optional _timeout_ parameter specifies a timeout in seconds for the connection attempt (if not specified, the global default timeout setting will be used).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `poplib.connect` with arguments `self`, `host`, `port`.
All commands will raise an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `poplib.putline` with arguments `self` and `line`, where `line` is the bytes about to be sent to the remote host.
Changed in version 3.9: If the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to prevent the creation of a non-blocking socket.

_class_ poplib.POP3_SSL(_host_ , _port =POP3_SSL_PORT_, _*_ , _timeout =None_, _context =None_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL "Link to this definition")

This is a subclass of [`POP3`](https://docs.python.org/3/library/poplib.html#poplib.POP3 "poplib.POP3") that connects to the server over an SSL encrypted socket. If _port_ is not specified, 995, the standard POP3-over-SSL port is used. _timeout_ works as in the `POP3` constructor. _context_ is an optional [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object which allows bundling SSL configuration options, certificates and private keys into a single (potentially long-lived) structure. Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for best practices.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `poplib.connect` with arguments `self`, `host`, `port`.
All commands will raise an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `poplib.putline` with arguments `self` and `line`, where `line` is the bytes about to be sent to the remote host.
Changed in version 3.2: _context_ parameter added.
Changed in version 3.4: The class now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")).
Changed in version 3.9: If the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to prevent the creation of a non-blocking socket.
Changed in version 3.12: The deprecated _keyfile_ and _certfile_ parameters have been removed.
One exception is defined as an attribute of the `poplib` module:

_exception_ poplib.error_proto[¶](https://docs.python.org/3/library/poplib.html#poplib.error_proto "Link to this definition")

Exception raised on any errors from this module (errors from [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module are not caught). The reason for the exception is passed to the constructor as a string.
See also

Module [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client \(requires sockets\).")

The standard Python IMAP module.
The FAQ for the **fetchmail** POP/IMAP client collects information on POP3 server variations and RFC noncompliance that may be useful if you need to write an application based on the POP protocol.
## POP3 Objects[¶](https://docs.python.org/3/library/poplib.html#pop3-objects "Link to this heading")
All POP3 commands are represented by methods of the same name, in lowercase; most return the response text sent by the server.
A [`POP3`](https://docs.python.org/3/library/poplib.html#poplib.POP3 "poplib.POP3") instance has the following methods:

POP3.set_debuglevel(_level_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.set_debuglevel "Link to this definition")

Set the instance’s debugging level. This controls the amount of debugging output printed. The default, `0`, produces no debugging output. A value of `1` produces a moderate amount of debugging output, generally a single line per request. A value of `2` or higher produces the maximum amount of debugging output, logging each line sent and received on the control connection.

POP3.getwelcome()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.getwelcome "Link to this definition")

Returns the greeting string sent by the POP3 server.

POP3.capa()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.capa "Link to this definition")

Query the server’s capabilities as specified in `{'name': ['param'...]}`.
Added in version 3.4.

POP3.user(_username_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.user "Link to this definition")

Send user command, response should indicate that a password is required.

POP3.pass_(_password_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.pass_ "Link to this definition")

Send password, response includes message count and mailbox size. Note: the mailbox on the server is locked until [`quit()`](https://docs.python.org/3/library/poplib.html#poplib.POP3.quit "poplib.POP3.quit") is called.

POP3.apop(_user_ , _secret_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.apop "Link to this definition")

Use the more secure APOP authentication to log into the POP3 server.

POP3.rpop(_user_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.rpop "Link to this definition")

Use RPOP authentication (similar to UNIX r-commands) to log into POP3 server.

POP3.stat()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.stat "Link to this definition")

Get mailbox status. The result is a tuple of 2 integers: `(message count, mailbox size)`.

POP3.list([_which_])[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.list "Link to this definition")

Request message list, result is in the form `(response, ['mesg_num octets', ...], octets)`. If _which_ is set, it is the message to list.

POP3.retr(_which_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.retr "Link to this definition")

Retrieve whole message number _which_ , and set its seen flag. Result is in form `(response, ['line', ...], octets)`.

POP3.dele(_which_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.dele "Link to this definition")

Flag message number _which_ for deletion. On most servers deletions are not actually performed until QUIT (the major exception is Eudora QPOP, which deliberately violates the RFCs by doing pending deletes on any disconnect).

POP3.rset()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.rset "Link to this definition")

Remove any deletion marks for the mailbox.

POP3.noop()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.noop "Link to this definition")

Do nothing. Might be used as a keep-alive.

POP3.quit()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.quit "Link to this definition")

Signoff: commit changes, unlock mailbox, drop connection.

POP3.top(_which_ , _howmuch_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.top "Link to this definition")

Retrieves the message header plus _howmuch_ lines of the message after the header of message number _which_. Result is in form `(response, ['line', ...], octets)`.
The POP3 TOP command this method uses, unlike the RETR command, doesn’t set the message’s seen flag; unfortunately, TOP is poorly specified in the RFCs and is frequently broken in off-brand servers. Test this method by hand against the POP3 servers you will use before trusting it.

POP3.uidl(_which =None_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.uidl "Link to this definition")

Return message digest (unique id) list. If _which_ is specified, result contains the unique id for that message in the form `'response mesgnum uid`, otherwise result is list `(response, ['mesgnum uid', ...], octets)`.

POP3.utf8()[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.utf8 "Link to this definition")

Try to switch to UTF-8 mode. Returns the server response if successful, raises [`error_proto`](https://docs.python.org/3/library/poplib.html#poplib.error_proto "poplib.error_proto") if not. Specified in
Added in version 3.5.

POP3.stls(_context =None_)[¶](https://docs.python.org/3/library/poplib.html#poplib.POP3.stls "Link to this definition")

Start a TLS session on the active connection as specified in
_context_ parameter is a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object which allows bundling SSL configuration options, certificates and private keys into a single (potentially long-lived) structure. Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for best practices.
This method supports hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")).
Added in version 3.4.
Instances of [`POP3_SSL`](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL "poplib.POP3_SSL") have no additional methods. The interface of this subclass is identical to its parent.
## POP3 Example[¶](https://docs.python.org/3/library/poplib.html#pop3-example "Link to this heading")
Here is a minimal example (without error checking) that opens a mailbox and retrieves and prints all messages:
Copy```
import getpass, poplib

M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)

```

At the end of the module, there is a test section that contains a more extensive example of usage.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html)
    * [POP3 Objects](https://docs.python.org/3/library/poplib.html#pop3-objects)
    * [POP3 Example](https://docs.python.org/3/library/poplib.html#pop3-example)


#### Previous topic
[`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html "previous chapter")
#### Next topic
[`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=poplib+%E2%80%94+POP3+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpoplib.html&pagesource=library%2Fpoplib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/imaplib.html "imaplib — IMAP4 protocol client") |
  * [previous](https://docs.python.org/3/library/ftplib.html "ftplib — FTP protocol client") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html)
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
