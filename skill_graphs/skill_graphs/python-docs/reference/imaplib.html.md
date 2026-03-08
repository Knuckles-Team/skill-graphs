[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html)
    * [IMAP4 Objects](https://docs.python.org/3/library/imaplib.html#imap4-objects)
    * [IMAP4 Example](https://docs.python.org/3/library/imaplib.html#imap4-example)


#### Previous topic
[`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html "previous chapter")
#### Next topic
[`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=imaplib+%E2%80%94+IMAP4+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimaplib.html&pagesource=library%2Fimaplib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/smtplib.html "smtplib — SMTP protocol client") |
  * [previous](https://docs.python.org/3/library/poplib.html "poplib — POP3 protocol client") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html)
  * |
  * Theme  Auto Light Dark |


#  `imaplib` — IMAP4 protocol client[¶](https://docs.python.org/3/library/imaplib.html#module-imaplib "Link to this heading")
**Source code:**
* * *
This module defines three classes, [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4"), [`IMAP4_SSL`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL "imaplib.IMAP4_SSL") and [`IMAP4_stream`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_stream "imaplib.IMAP4_stream"), which encapsulate a connection to an IMAP4 server and implement a large subset of the IMAP4rev1 client protocol as defined in `STATUS` command is not supported in IMAP4.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
Three classes are provided by the `imaplib` module, [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") is the base class:

_class_ imaplib.IMAP4(_host =''_, _port =IMAP4_PORT_, _timeout =None_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "Link to this definition")

This class implements the actual IMAP4 protocol. The connection is created and protocol version (IMAP4 or IMAP4rev1) is determined when the instance is initialized. If _host_ is not specified, `''` (the local host) is used. If _port_ is omitted, the standard IMAP4 port (143) is used. The optional _timeout_ parameter specifies a timeout in seconds for the connection attempt. If timeout is not given or is `None`, the global default socket timeout is used.
The `IMAP4` class supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. When used like this, the IMAP4 `LOGOUT` command is issued automatically when the `with` statement exits. E.g.:
Copy```
>>> from imaplib import IMAP4
>>> with IMAP4("domain.org") as M:
...     M.noop()
...
('OK', [b'Nothing Accomplished. d25if65hy903weo.87'])

```

Changed in version 3.5: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement was added.
Changed in version 3.9: The optional _timeout_ parameter was added.
Three exceptions are defined as attributes of the [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") class:

_exception_ IMAP4.error[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.error "Link to this definition")

Exception raised on any errors. The reason for the exception is passed to the constructor as a string.

_exception_ IMAP4.abort[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.abort "Link to this definition")

IMAP4 server errors cause this exception to be raised. This is a sub-class of [`IMAP4.error`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.error "imaplib.IMAP4.error"). Note that closing the instance and instantiating a new one will usually allow recovery from this exception.

_exception_ IMAP4.readonly[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.readonly "Link to this definition")

This exception is raised when a writable mailbox has its status changed by the server. This is a sub-class of [`IMAP4.error`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.error "imaplib.IMAP4.error"). Some other client now has write permission, and the mailbox will need to be re-opened to re-obtain write permission.
There’s also a subclass for secure connections:

_class_ imaplib.IMAP4_SSL(_host =''_, _port =IMAP4_SSL_PORT_, _*_ , _ssl_context =None_, _timeout =None_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL "Link to this definition")

This is a subclass derived from [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") that connects over an SSL encrypted socket (to use this class you need a socket module that was compiled with SSL support). If _host_ is not specified, `''` (the local host) is used. If _port_ is omitted, the standard IMAP4-over-SSL port (993) is used. _ssl_context_ is a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object which allows bundling SSL configuration options, certificates and private keys into a single (potentially long-lived) structure. Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for best practices.
The optional _timeout_ parameter specifies a timeout in seconds for the connection attempt. If timeout is not given or is `None`, the global default socket timeout is used.
Changed in version 3.3: _ssl_context_ parameter was added.
Changed in version 3.4: The class now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")).
Changed in version 3.9: The optional _timeout_ parameter was added.
Changed in version 3.12: The deprecated _keyfile_ and _certfile_ parameters have been removed.
The second subclass allows for connections created by a child process:

_class_ imaplib.IMAP4_stream(_command_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_stream "Link to this definition")

This is a subclass derived from [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") that connects to the `stdin/stdout` file descriptors created by passing _command_ to `subprocess.Popen()`.
The following utility functions are defined:

imaplib.Internaldate2tuple(_datestr_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.Internaldate2tuple "Link to this definition")

Parse an IMAP4 `INTERNALDATE` string and return corresponding local time. The return value is a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") tuple or `None` if the string has wrong format.

imaplib.Int2AP(_num_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.Int2AP "Link to this definition")

Converts an integer into a bytes representation using characters from the set [`A` .. `P`].

imaplib.ParseFlags(_flagstr_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.ParseFlags "Link to this definition")

Converts an IMAP4 `FLAGS` response to a tuple of individual flags.

imaplib.Time2Internaldate(_date_time_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.Time2Internaldate "Link to this definition")

Convert _date_time_ to an IMAP4 `INTERNALDATE` representation. The return value is a string in the form: `"DD-Mmm-YYYY HH:MM:SS +HHMM"` (including double-quotes). The _date_time_ argument can be a number (int or float) representing seconds since epoch (as returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time")), a 9-tuple representing local time an instance of [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") (as returned by [`time.localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")), an aware instance of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), or a double-quoted string. In the last case, it is assumed to already be in the correct format.
Note that IMAP4 message numbers change as the mailbox changes; in particular, after an `EXPUNGE` command performs deletions the remaining messages are renumbered. So it is highly advisable to use UIDs instead, with the UID command.
At the end of the module, there is a test section that contains a more extensive example of usage.
See also
Documents describing the protocol, sources for servers implementing it, by the University of Washington’s IMAP Information Center can all be found at (**Source Code**) **Not Maintained**).
## IMAP4 Objects[¶](https://docs.python.org/3/library/imaplib.html#imap4-objects "Link to this heading")
All IMAP4rev1 commands are represented by methods of the same name, either uppercase or lowercase.
All arguments to commands are converted to strings, except for `AUTHENTICATE`, and the last argument to `APPEND` which is passed as an IMAP4 literal. If necessary (the string contains IMAP4 protocol-sensitive characters and isn’t enclosed with either parentheses or double quotes) each string is quoted. However, the _password_ argument to the `LOGIN` command is always quoted. If you want to avoid having an argument string quoted (eg: the _flags_ argument to `STORE`) then enclose the string in parentheses (eg: `r'(\Deleted)'`).
Most commands return a tuple: `(type, [data, ...])` where _type_ is usually `'OK'` or `'NO'`, and _data_ is either the text from the command response, or mandated results from the command. Each _data_ is either a `bytes`, or a tuple. If a tuple, then the first part is the header of the response, and the second part contains the data (ie: ‘literal’ value).
The _message_set_ options to commands below is a string specifying one or more messages to be acted upon. It may be a simple message number (`'1'`), a range of message numbers (`'2:4'`), or a group of non-contiguous ranges separated by commas (`'1:3,6:9'`). A range can contain an asterisk to indicate an infinite upper bound (`'3:*'`).
An [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") instance has the following methods:

IMAP4.append(_mailbox_ , _flags_ , _date_time_ , _message_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.append "Link to this definition")

Append _message_ to named mailbox.

IMAP4.authenticate(_mechanism_ , _authobject_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.authenticate "Link to this definition")

Authenticate command — requires response processing.
_mechanism_ specifies which authentication mechanism is to be used - it should appear in the instance variable `capabilities` in the form `AUTH=mechanism`.
_authobject_ must be a callable object:
Copy```
data = authobject(response)

```

It will be called to process server continuation responses; the _response_ argument it is passed will be `bytes`. It should return `bytes` _data_ that will be base64 encoded and sent to the server. It should return `None` if the client abort response `*` should be sent instead.
Changed in version 3.5: string usernames and passwords are now encoded to `utf-8` instead of being limited to ASCII.

IMAP4.check()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.check "Link to this definition")

Checkpoint mailbox on server.

IMAP4.close()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.close "Link to this definition")

Close currently selected mailbox. Deleted messages are removed from writable mailbox. This is the recommended command before `LOGOUT`.

IMAP4.copy(_message_set_ , _new_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.copy "Link to this definition")

Copy _message_set_ messages onto end of _new_mailbox_.

IMAP4.create(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.create "Link to this definition")

Create new mailbox named _mailbox_.

IMAP4.delete(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.delete "Link to this definition")

Delete old mailbox named _mailbox_.

IMAP4.deleteacl(_mailbox_ , _who_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.deleteacl "Link to this definition")

Delete the ACLs (remove any rights) set for who on mailbox.

IMAP4.enable(_capability_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.enable "Link to this definition")

Enable _capability_ (see `UTF8=ACCEPT` capability is supported (see
Added in version 3.5: The `enable()` method itself, and

IMAP4.expunge()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.expunge "Link to this definition")

Permanently remove deleted items from selected mailbox. Generates an `EXPUNGE` response for each deleted message. Returned data contains a list of `EXPUNGE` message numbers in order received.

IMAP4.fetch(_message_set_ , _message_parts_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.fetch "Link to this definition")

Fetch (parts of) messages. _message_parts_ should be a string of message part names enclosed within parentheses, eg: `"(UID BODY[TEXT])"`. Returned data are tuples of message part envelope and data.

IMAP4.getacl(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.getacl "Link to this definition")

Get the `ACL`s for _mailbox_. The method is non-standard, but is supported by the `Cyrus` server.

IMAP4.getannotation(_mailbox_ , _entry_ , _attribute_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.getannotation "Link to this definition")

Retrieve the specified `ANNOTATION`s for _mailbox_. The method is non-standard, but is supported by the `Cyrus` server.

IMAP4.getquota(_root_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.getquota "Link to this definition")

Get the `quota` _root_ ’s resource usage and limits. This method is part of the IMAP4 QUOTA extension defined in rfc2087.

IMAP4.getquotaroot(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.getquotaroot "Link to this definition")

Get the list of `quota` `roots` for the named _mailbox_. This method is part of the IMAP4 QUOTA extension defined in rfc2087.

IMAP4.idle(_duration =None_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.idle "Link to this definition")

Return an `Idler`: an iterable context manager implementing the IMAP4 `IDLE` command as defined in
The returned object sends the `IDLE` command when activated by the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, produces IMAP untagged responses via the [iterator](https://docs.python.org/3/glossary.html#term-iterator) protocol, and sends `DONE` upon context exit.
All untagged responses that arrive after sending the `IDLE` command (including any that arrive before the server acknowledges the command) will be available via iteration. Any leftover responses (those not iterated in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) context) can be retrieved in the usual way after `IDLE` ends, using [`IMAP4.response()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.response "imaplib.IMAP4.response").
Responses are represented as `(type, [data, ...])` tuples, as described in [IMAP4 Objects](https://docs.python.org/3/library/imaplib.html#imap4-objects).
The _duration_ argument sets a maximum duration (in seconds) to keep idling, after which any ongoing iteration will stop. It can be an [`int`](https://docs.python.org/3/library/functions.html#int "int") or [`float`](https://docs.python.org/3/library/functions.html#float "float"), or `None` for no time limit. Callers wishing to avoid inactivity timeouts on servers that impose them should keep this at most 29 minutes (1740 seconds). Requires a socket connection; _duration_ must be `None` on [`IMAP4_stream`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_stream "imaplib.IMAP4_stream") connections.
Copy```
>>> with M.idle(duration=29 * 60) as idler:
...     for typ, data in idler:
...         print(typ, data)
...
EXISTS [b'1']
RECENT [b'1']

```


Idler.burst(_interval =0.1_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.Idler.burst "Link to this definition")

Yield a burst of responses no more than _interval_ seconds apart (expressed as an [`int`](https://docs.python.org/3/library/functions.html#int "int") or [`float`](https://docs.python.org/3/library/functions.html#float "float")).
This [generator](https://docs.python.org/3/glossary.html#term-generator) is an alternative to iterating one response at a time, intended to aid in efficient batch processing. It retrieves the next response along with any immediately available subsequent responses. (For example, a rapid series of `EXPUNGE` responses after a bulk delete.)
Requires a socket connection; does not work on [`IMAP4_stream`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_stream "imaplib.IMAP4_stream") connections.
Copy```
>>> with M.idle() as idler:
...     # get a response and any others following by < 0.1 seconds
...     batch = list(idler.burst())
...     print(f'processing {len(batch)} responses...')
...     print(batch)
...
processing 3 responses...
[('EXPUNGE', [b'2']), ('EXPUNGE', [b'1']), ('RECENT', [b'0'])]

```

Tip
The `IDLE` context’s maximum duration, as passed to `IMAP4.idle()`, is respected when waiting for the first response in a burst. Therefore, an expired `Idler` will cause this generator to return immediately without producing anything. Callers should consider this if using it in a loop.
Note
The iterator returned by `IMAP4.idle()` is usable only within a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. Before or after that context, unsolicited responses are collected internally whenever a command finishes, and can be retrieved with [`IMAP4.response()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.response "imaplib.IMAP4.response").
Note
The `Idler` class name and structure are internal interfaces, subject to change. Calling code can rely on its context management, iteration, and public method to remain stable, but should not subclass, instantiate, compare, or otherwise directly reference the class.
Added in version 3.14.

IMAP4.list([_directory_[, _pattern_]])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.list "Link to this definition")

List mailbox names in _directory_ matching _pattern_. _directory_ defaults to the top-level mail folder, and _pattern_ defaults to match anything. Returned data contains a list of `LIST` responses.

IMAP4.login(_user_ , _password_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.login "Link to this definition")

Identify the client using a plaintext password. The _password_ will be quoted.

IMAP4.login_cram_md5(_user_ , _password_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.login_cram_md5 "Link to this definition")

Force use of `CRAM-MD5` authentication when identifying the client to protect the password. Will only work if the server `CAPABILITY` response includes the phrase `AUTH=CRAM-MD5`.
Changed in version 3.14: An [`IMAP4.error`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.error "imaplib.IMAP4.error") is raised if MD5 support is not available.

IMAP4.logout()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.logout "Link to this definition")

Shutdown connection to server. Returns server `BYE` response.
Changed in version 3.8: The method no longer ignores silently arbitrary exceptions.

IMAP4.lsub(_directory ='""'_, _pattern ='*'_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.lsub "Link to this definition")

List subscribed mailbox names in directory matching pattern. _directory_ defaults to the top level directory and _pattern_ defaults to match any mailbox. Returned data are tuples of message part envelope and data.

IMAP4.myrights(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.myrights "Link to this definition")

Show my ACLs for a mailbox (i.e. the rights that I have on mailbox).

IMAP4.namespace()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.namespace "Link to this definition")

Returns IMAP namespaces as defined in

IMAP4.noop()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.noop "Link to this definition")

Send `NOOP` to server.

IMAP4.open(_host_ , _port_ , _timeout =None_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.open "Link to this definition")

Opens socket to _port_ at _host_. The optional _timeout_ parameter specifies a timeout in seconds for the connection attempt. If timeout is not given or is `None`, the global default socket timeout is used. Also note that if the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to reject creating a non-blocking socket. This method is implicitly called by the [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") constructor. The connection objects established by this method will be used in the [`IMAP4.read()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.read "imaplib.IMAP4.read"), [`IMAP4.readline()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.readline "imaplib.IMAP4.readline"), [`IMAP4.send()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.send "imaplib.IMAP4.send"), and [`IMAP4.shutdown()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.shutdown "imaplib.IMAP4.shutdown") methods. You may override this method.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `imaplib.open` with arguments `self`, `host`, `port`.
Changed in version 3.9: The _timeout_ parameter was added.

IMAP4.partial(_message_num_ , _message_part_ , _start_ , _length_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.partial "Link to this definition")

Fetch truncated part of a message. Returned data is a tuple of message part envelope and data.

IMAP4.proxyauth(_user_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.proxyauth "Link to this definition")

Assume authentication as _user_. Allows an authorised administrator to proxy into any user’s mailbox.

IMAP4.read(_size_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.read "Link to this definition")

Reads _size_ bytes from the remote server. You may override this method.

IMAP4.readline()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.readline "Link to this definition")

Reads one line from the remote server. You may override this method.

IMAP4.recent()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.recent "Link to this definition")

Prompt server for an update. Returned data is `None` if no new messages, else value of `RECENT` response.

IMAP4.rename(_oldmailbox_ , _newmailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.rename "Link to this definition")

Rename mailbox named _oldmailbox_ to _newmailbox_.

IMAP4.response(_code_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.response "Link to this definition")

Return data for response _code_ if received, or `None`. Returns the given code, instead of the usual type.

IMAP4.search(_charset_ , _criterion_[, _..._])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.search "Link to this definition")

Search mailbox for matching messages. _charset_ may be `None`, in which case no `CHARSET` will be specified in the request to the server. The IMAP protocol requires that at least one criterion be specified; an exception will be raised when the server returns an error. _charset_ must be `None` if the `UTF8=ACCEPT` capability was enabled using the [`enable()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.enable "imaplib.IMAP4.enable") command.
Example:
Copy```
# M is a connected IMAP4 instance...
typ, msgnums = M.search(None, 'FROM', '"LDJ"')

# or:
typ, msgnums = M.search(None, '(FROM "LDJ")')

```


IMAP4.select(_mailbox ='INBOX'_, _readonly =False_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.select "Link to this definition")

Select a mailbox. Returned data is the count of messages in _mailbox_ (`EXISTS` response). The default _mailbox_ is `'INBOX'`. If the _readonly_ flag is set, modifications to the mailbox are not allowed.

IMAP4.send(_data_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.send "Link to this definition")

Sends `data` to the remote server. You may override this method.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `imaplib.send` with arguments `self`, `data`.

IMAP4.setacl(_mailbox_ , _who_ , _what_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.setacl "Link to this definition")

Set an `ACL` for _mailbox_. The method is non-standard, but is supported by the `Cyrus` server.

IMAP4.setannotation(_mailbox_ , _entry_ , _attribute_[, _..._])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.setannotation "Link to this definition")

Set `ANNOTATION`s for _mailbox_. The method is non-standard, but is supported by the `Cyrus` server.

IMAP4.setquota(_root_ , _limits_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.setquota "Link to this definition")

Set the `quota` _root_ ’s resource _limits_. This method is part of the IMAP4 QUOTA extension defined in rfc2087.

IMAP4.shutdown()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.shutdown "Link to this definition")

Close connection established in `open`. This method is implicitly called by [`IMAP4.logout()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.logout "imaplib.IMAP4.logout"). You may override this method.

IMAP4.socket()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.socket "Link to this definition")

Returns socket instance used to connect to server.

IMAP4.sort(_sort_criteria_ , _charset_ , _search_criterion_[, _..._])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.sort "Link to this definition")

The `sort` command is a variant of `search` with sorting semantics for the results. Returned data contains a space separated list of matching message numbers.
Sort has two arguments before the _search_criterion_ argument(s); a parenthesized list of _sort_criteria_ , and the searching _charset_. Note that unlike `search`, the searching _charset_ argument is mandatory. There is also a `uid sort` command which corresponds to `sort` the way that `uid search` corresponds to `search`. The `sort` command first searches the mailbox for messages that match the given searching criteria using the charset argument for the interpretation of strings in the searching criteria. It then returns the numbers of matching messages.
This is an `IMAP4rev1` extension command.

IMAP4.starttls(_ssl_context =None_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.starttls "Link to this definition")

Send a `STARTTLS` command. The _ssl_context_ argument is optional and should be a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object. This will enable encryption on the IMAP connection. Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for best practices.
Added in version 3.2.
Changed in version 3.4: The method now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")).

IMAP4.status(_mailbox_ , _names_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.status "Link to this definition")

Request named status conditions for _mailbox_.

IMAP4.store(_message_set_ , _command_ , _flag_list_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.store "Link to this definition")

Alters flag dispositions for messages in mailbox. _command_ is specified by section 6.4.6 of
For example, to set the delete flag on all messages:
Copy```
typ, data = M.search(None, 'ALL')
for num in data[0].split():
   M.store(num, '+FLAGS', '\\Deleted')
M.expunge()

```

Note
Creating flags containing ‘]’ (for example: “[test]”) violates

IMAP4.subscribe(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.subscribe "Link to this definition")

Subscribe to new mailbox.

IMAP4.thread(_threading_algorithm_ , _charset_ , _search_criterion_[, _..._])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.thread "Link to this definition")

The `thread` command is a variant of `search` with threading semantics for the results. Returned data contains a space separated list of thread members.
Thread members consist of zero or more messages numbers, delimited by spaces, indicating successive parent and child.
Thread has two arguments before the _search_criterion_ argument(s); a _threading_algorithm_ , and the searching _charset_. Note that unlike `search`, the searching _charset_ argument is mandatory. There is also a `uid thread` command which corresponds to `thread` the way that `uid search` corresponds to `search`. The `thread` command first searches the mailbox for messages that match the given searching criteria using the _charset_ argument for the interpretation of strings in the searching criteria. It then returns the matching messages threaded according to the specified threading algorithm.
This is an `IMAP4rev1` extension command.

IMAP4.uid(_command_ , _arg_[, _..._])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.uid "Link to this definition")

Execute command args with messages identified by UID, rather than message number. Returns response appropriate to command. At least one argument must be supplied; if none are provided, the server will return an error and an exception will be raised.

IMAP4.unsubscribe(_mailbox_)[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.unsubscribe "Link to this definition")

Unsubscribe from old mailbox.

IMAP4.unselect()[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.unselect "Link to this definition")

[`imaplib.IMAP4.unselect()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.unselect "imaplib.IMAP4.unselect") frees server’s resources associated with the selected mailbox and returns the server to the authenticated state. This command performs the same actions as [`imaplib.IMAP4.close()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.close "imaplib.IMAP4.close"), except that no messages are permanently removed from the currently selected mailbox.
Added in version 3.9.

IMAP4.xatom(_name_[, _..._])[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.xatom "Link to this definition")

Allow simple extension commands notified by server in `CAPABILITY` response.
The following attributes are defined on instances of [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4"):

IMAP4.PROTOCOL_VERSION[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.PROTOCOL_VERSION "Link to this definition")

The most recent supported protocol in the `CAPABILITY` response from the server.

IMAP4.debug[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.debug "Link to this definition")

Integer value to control debugging output. The initialize value is taken from the module variable `Debug`. Values greater than three trace each command.

IMAP4.utf8_enabled[¶](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.utf8_enabled "Link to this definition")

Boolean value that is normally `False`, but is set to `True` if an [`enable()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.enable "imaplib.IMAP4.enable") command is successfully issued for the `UTF8=ACCEPT` capability.
Added in version 3.5.
## IMAP4 Example[¶](https://docs.python.org/3/library/imaplib.html#imap4-example "Link to this heading")
Here is a minimal example (without error checking) that opens a mailbox and retrieves and prints all messages:
Copy```
import getpass, imaplib

M = imaplib.IMAP4(host='example.org')
M.login(getpass.getuser(), getpass.getpass())
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html)
    * [IMAP4 Objects](https://docs.python.org/3/library/imaplib.html#imap4-objects)
    * [IMAP4 Example](https://docs.python.org/3/library/imaplib.html#imap4-example)


#### Previous topic
[`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html "previous chapter")
#### Next topic
[`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=imaplib+%E2%80%94+IMAP4+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimaplib.html&pagesource=library%2Fimaplib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/smtplib.html "smtplib — SMTP protocol client") |
  * [previous](https://docs.python.org/3/library/poplib.html "poplib — POP3 protocol client") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html)
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
