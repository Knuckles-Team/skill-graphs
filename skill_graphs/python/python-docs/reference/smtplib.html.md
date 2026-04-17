[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
    * [SMTP Objects](https://docs.python.org/3/library/smtplib.html#smtp-objects)
    * [SMTP Example](https://docs.python.org/3/library/smtplib.html#smtp-example)


#### Previous topic
[`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html "previous chapter")
#### Next topic
[`uuid` — UUID objects according to **RFC 9562**](https://docs.python.org/3/library/uuid.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=smtplib+%E2%80%94+SMTP+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsmtplib.html&pagesource=library%2Fsmtplib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/uuid.html "uuid — UUID objects according to RFC 9562") |
  * [previous](https://docs.python.org/3/library/imaplib.html "imaplib — IMAP4 protocol client") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
  * |
  * Theme  Auto Light Dark |


#  `smtplib` — SMTP protocol client[¶](https://docs.python.org/3/library/smtplib.html#module-smtplib "Link to this heading")
**Source code:**
* * *
The `smtplib` module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. For details of SMTP and ESMTP operation, consult
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

_class_ smtplib.SMTP(_host=''_ , _port=0_ , _local_hostname=None_ , [_timeout_ , ]_source_address=None_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "Link to this definition")

An `SMTP` instance encapsulates an SMTP connection. It has methods that support a full repertoire of SMTP and ESMTP operations. If the optional _host_ and _port_ parameters are given, the SMTP [`connect()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.connect "smtplib.SMTP.connect") method is called with those parameters during initialization. If specified, _local_hostname_ is used as the FQDN of the local host in the HELO/EHLO command. Otherwise, the local hostname is found using [`socket.getfqdn()`](https://docs.python.org/3/library/socket.html#socket.getfqdn "socket.getfqdn"). If the `connect()` call returns anything other than a success code, an [`SMTPConnectError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPConnectError "smtplib.SMTPConnectError") is raised. The optional _timeout_ parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). If the timeout expires, [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") is raised. The optional _source_address_ parameter allows binding to some specific source address in a machine with multiple network interfaces, and/or to some specific source TCP port. It takes a 2-tuple `(host, port)`, for the socket to bind to as its source address before connecting. If omitted (or if _host_ or _port_ are `''` and/or `0` respectively) the OS default behavior will be used.
For normal use, you should only require the initialization/connect, [`sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail"), and [`SMTP.quit()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.quit "smtplib.SMTP.quit") methods. An example is included below.
The `SMTP` class supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. When used like this, the SMTP `QUIT` command is issued automatically when the `with` statement exits. E.g.:
Copy```
>>> from smtplib import SMTP
>>> with SMTP("domain.org") as smtp:
...     smtp.noop()
...
(250, b'Ok')
>>>

```

All commands will raise an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `smtplib.SMTP.send` with arguments `self` and `data`, where `data` is the bytes about to be sent to the remote host.
Changed in version 3.3: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement was added.
Changed in version 3.3: _source_address_ argument was added.
Added in version 3.5: The SMTPUTF8 extension (
Changed in version 3.9: If the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to prevent the creation of a non-blocking socket.

_class_ smtplib.SMTP_SSL(_host=''_ , _port=0_ , _local_hostname=None_ , _*_ , [_timeout_ , ]_context=None_ , _source_address=None_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL "Link to this definition")

An `SMTP_SSL` instance behaves exactly the same as instances of [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP"). `SMTP_SSL` should be used for situations where SSL is required from the beginning of the connection and using [`starttls()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls "smtplib.SMTP.starttls") is not appropriate. If _host_ is not specified, the local host is used. If _port_ is zero, the standard SMTP-over-SSL port (465) is used. The optional arguments _local_hostname_ , _timeout_ and _source_address_ have the same meaning as they do in the `SMTP` class. _context_ , also optional, can contain a [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") and allows configuring various aspects of the secure connection. Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for best practices.
Changed in version 3.3: _context_ was added.
Changed in version 3.3: The _source_address_ argument was added.
Changed in version 3.4: The class now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")).
Changed in version 3.9: If the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to prevent the creation of a non-blocking socket
Changed in version 3.12: The deprecated _keyfile_ and _certfile_ parameters have been removed.

_class_ smtplib.LMTP(_host=''_ , _port=LMTP_PORT_ , _local_hostname=None_ , _source_address=None_[, _timeout_])[¶](https://docs.python.org/3/library/smtplib.html#smtplib.LMTP "Link to this definition")

The LMTP protocol, which is very similar to ESMTP, is heavily based on the standard SMTP client. It’s common to use Unix sockets for LMTP, so our [`connect()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.connect "smtplib.SMTP.connect") method must support that as well as a regular host:port server. The optional arguments _local_hostname_ and _source_address_ have the same meaning as they do in the [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP") class. To specify a Unix socket, you must use an absolute path for _host_ , starting with a ‘/’.
Authentication is supported, using the regular SMTP mechanism. When using a Unix socket, LMTP generally don’t support or require any authentication, but your mileage might vary.
Changed in version 3.9: The optional _timeout_ parameter was added.
A nice selection of exceptions is defined as well:

_exception_ smtplib.SMTPException[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPException "Link to this definition")

Subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") that is the base exception class for all the other exceptions provided by this module.
Changed in version 3.4: SMTPException became subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")

_exception_ smtplib.SMTPServerDisconnected[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPServerDisconnected "Link to this definition")

This exception is raised when the server unexpectedly disconnects, or when an attempt is made to use the [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP") instance before connecting it to a server.

_exception_ smtplib.SMTPResponseException[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPResponseException "Link to this definition")

Base class for all exceptions that include an SMTP error code. These exceptions are generated in some instances when the SMTP server returns an error code.

smtp_code[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPResponseException.smtp_code "Link to this definition")

The error code.

smtp_error[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPResponseException.smtp_error "Link to this definition")

The error message.

_exception_ smtplib.SMTPSenderRefused[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPSenderRefused "Link to this definition")

Sender address refused. In addition to the attributes set by on all [`SMTPResponseException`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPResponseException "smtplib.SMTPResponseException") exceptions, this sets ‘sender’ to the string that the SMTP server refused.

_exception_ smtplib.SMTPRecipientsRefused[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPRecipientsRefused "Link to this definition")

All recipient addresses refused.

recipients[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPRecipientsRefused.recipients "Link to this definition")

A dictionary of exactly the same sort as returned by [`SMTP.sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail") containing the errors for each recipient.

_exception_ smtplib.SMTPDataError[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPDataError "Link to this definition")

The SMTP server refused to accept the message data.

_exception_ smtplib.SMTPConnectError[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPConnectError "Link to this definition")

Error occurred during establishment of a connection with the server.

_exception_ smtplib.SMTPHeloError[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPHeloError "Link to this definition")

The server refused our `HELO` message.

_exception_ smtplib.SMTPNotSupportedError[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "Link to this definition")

The command or option attempted is not supported by the server.
Added in version 3.5.

_exception_ smtplib.SMTPAuthenticationError[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPAuthenticationError "Link to this definition")

SMTP authentication went wrong. Most probably the server didn’t accept the username/password combination provided.
See also
Protocol definition for SMTP. This document covers the model, operating procedure, and protocol details for SMTP.
Definition of the ESMTP extensions for SMTP. This describes a framework for extending SMTP with new commands, supporting dynamic discovery of the commands provided by the server, and defines a few additional commands.
## SMTP Objects[¶](https://docs.python.org/3/library/smtplib.html#smtp-objects "Link to this heading")
An [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP") instance has the following methods:

SMTP.set_debuglevel(_level_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.set_debuglevel "Link to this definition")

Set the debug output level. A value of 1 or `True` for _level_ results in debug messages for connection and for all messages sent to and received from the server. A value of 2 for _level_ results in these messages being timestamped.
Changed in version 3.5: Added debuglevel 2.

SMTP.docmd(_cmd_ , _args =''_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.docmd "Link to this definition")

Send a command _cmd_ to the server. The optional argument _args_ is simply concatenated to the command, separated by a space.
This returns a 2-tuple composed of a numeric response code and the actual response line (multiline responses are joined into one long line.)
In normal operation it should not be necessary to call this method explicitly. It is used to implement other methods and may be useful for testing private extensions.
If the connection to the server is lost while waiting for the reply, [`SMTPServerDisconnected`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPServerDisconnected "smtplib.SMTPServerDisconnected") will be raised.

SMTP.connect(_host ='localhost'_, _port =0_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.connect "Link to this definition")

Connect to a host on a given port. The defaults are to connect to the local host at the standard SMTP port (25). If the hostname ends with a colon (`':'`) followed by a number, that suffix will be stripped off and the number interpreted as the port number to use. This method is automatically invoked by the constructor if a host is specified during instantiation. Returns a 2-tuple of the response code and message sent by the server in its connection response.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `smtplib.connect` with arguments `self`, `host`, `port`.

SMTP.helo(_name =''_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.helo "Link to this definition")

Identify yourself to the SMTP server using `HELO`. The hostname argument defaults to the fully qualified domain name of the local host. The message returned by the server is stored as the [`helo_resp`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.helo_resp "smtplib.SMTP.helo_resp") attribute of the object.
In normal operation it should not be necessary to call this method explicitly. It will be implicitly called by the [`sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail") when necessary.

SMTP.ehlo(_name =''_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo "Link to this definition")

Identify yourself to an ESMTP server using `EHLO`. The hostname argument defaults to the fully qualified domain name of the local host. Examine the response for ESMTP option and store them for use by [`has_extn()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.has_extn "smtplib.SMTP.has_extn"). Also sets several informational attributes: the message returned by the server is stored as the [`ehlo_resp`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo_resp "smtplib.SMTP.ehlo_resp") attribute, [`does_esmtp`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.does_esmtp "smtplib.SMTP.does_esmtp") is set to `True` or `False` depending on whether the server supports ESMTP, and [`esmtp_features`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.esmtp_features "smtplib.SMTP.esmtp_features") will be a dictionary containing the names of the SMTP service extensions this server supports, and their parameters (if any).
Unless you wish to use [`has_extn()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.has_extn "smtplib.SMTP.has_extn") before sending mail, it should not be necessary to call this method explicitly. It will be implicitly called by [`sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail") when necessary.

SMTP.ehlo_or_helo_if_needed()[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo_or_helo_if_needed "Link to this definition")

This method calls [`ehlo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo "smtplib.SMTP.ehlo") and/or [`helo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.helo "smtplib.SMTP.helo") if there has been no previous `EHLO` or `HELO` command this session. It tries ESMTP `EHLO` first.

[`SMTPHeloError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPHeloError "smtplib.SMTPHeloError")

The server didn’t reply properly to the `HELO` greeting.

SMTP.has_extn(_name_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.has_extn "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if _name_ is in the set of SMTP service extensions returned by the server, [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise. Case is ignored.

SMTP.verify(_address_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.verify "Link to this definition")

Check the validity of an address on this server using SMTP `VRFY`. Returns a tuple consisting of code 250 and a full
Note
Many sites disable SMTP `VRFY` in order to foil spammers.

SMTP.login(_user_ , _password_ , _*_ , _initial_response_ok =True_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.login "Link to this definition")

Log in on an SMTP server that requires authentication. The arguments are the username and the password to authenticate with. If there has been no previous `EHLO` or `HELO` command this session, this method tries ESMTP `EHLO` first. This method will return normally if the authentication was successful, or may raise the following exceptions:

[`SMTPHeloError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPHeloError "smtplib.SMTPHeloError")

The server didn’t reply properly to the `HELO` greeting.

[`SMTPAuthenticationError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPAuthenticationError "smtplib.SMTPAuthenticationError")

The server didn’t accept the username/password combination.

[`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError")

The `AUTH` command is not supported by the server.

[`SMTPException`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPException "smtplib.SMTPException")

No suitable authentication method was found.
Each of the authentication methods supported by `smtplib` are tried in turn if they are advertised as supported by the server. See [`auth()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.auth "smtplib.SMTP.auth") for a list of supported authentication methods. _initial_response_ok_ is passed through to `auth()`.
Optional keyword argument _initial_response_ok_ specifies whether, for authentication methods that support it, an “initial response” as specified in `AUTH` command, rather than requiring a challenge/response.
Changed in version 3.5: [`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError") may be raised, and the _initial_response_ok_ parameter was added.

SMTP.auth(_mechanism_ , _authobject_ , _*_ , _initial_response_ok =True_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.auth "Link to this definition")

Issue an `SMTP` `AUTH` command for the specified authentication _mechanism_ , and handle the challenge response via _authobject_.
_mechanism_ specifies which authentication mechanism is to be used as argument to the `AUTH` command; the valid values are those listed in the `auth` element of [`esmtp_features`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.esmtp_features "smtplib.SMTP.esmtp_features").
_authobject_ must be a callable object taking an optional single argument:
Copy```
data = authobject(challenge=None)

```

If optional keyword argument _initial_response_ok_ is true, `authobject()` will be called first with no argument. It can return the `str` which will be encoded and sent with the `AUTH` command as below. If the `authobject()` does not support an initial response (e.g. because it requires a challenge), it should return `None` when called with `challenge=None`. If _initial_response_ok_ is false, then `authobject()` will not be called first with `None`.
If the initial response check returns `None`, or if _initial_response_ok_ is false, `authobject()` will be called to process the server’s challenge response; the _challenge_ argument it is passed will be a `bytes`. It should return ASCII `str` _data_ that will be base64 encoded and sent to the server.
The `SMTP` class provides `authobjects` for the `CRAM-MD5`, `PLAIN`, and `LOGIN` mechanisms; they are named `SMTP.auth_cram_md5`, `SMTP.auth_plain`, and `SMTP.auth_login` respectively. They all require that the `user` and `password` properties of the `SMTP` instance are set to appropriate values.
User code does not normally need to call `auth` directly, but can instead call the [`login()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.login "smtplib.SMTP.login") method, which will try each of the above mechanisms in turn, in the order listed. `auth` is exposed to facilitate the implementation of authentication methods not (or not yet) supported directly by `smtplib`.
Added in version 3.5.

SMTP.starttls(_*_ , _context =None_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls "Link to this definition")

Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted. You should then call [`ehlo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo "smtplib.SMTP.ehlo") again.
If _keyfile_ and _certfile_ are provided, they are used to create an [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext").
Optional _context_ parameter is an [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object; This is an alternative to using a keyfile and a certfile and if specified both _keyfile_ and _certfile_ should be `None`.
If there has been no previous `EHLO` or `HELO` command this session, this method tries ESMTP `EHLO` first.
Changed in version 3.12: The deprecated _keyfile_ and _certfile_ parameters have been removed.

[`SMTPHeloError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPHeloError "smtplib.SMTPHeloError")

The server didn’t reply properly to the `HELO` greeting.

[`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError")

The server does not support the STARTTLS extension.

[`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError")

SSL/TLS support is not available to your Python interpreter.
Changed in version 3.3: _context_ was added.
Changed in version 3.4: The method now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") and _Server Name Indicator_ (see [`HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")).
Changed in version 3.5: The error raised for lack of STARTTLS support is now the [`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError") subclass instead of the base [`SMTPException`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPException "smtplib.SMTPException").

SMTP.sendmail(_from_addr_ , _to_addrs_ , _msg_ , _mail_options =()_, _rcpt_options =()_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "Link to this definition")

Send mail. The required arguments are an `"8bitmime"`) to be used in `MAIL FROM` commands as _mail_options_. ESMTP options (such as `DSN` commands) that should be used with all `RCPT` commands can be passed as _rcpt_options_. Each option should be passed as a string containing the full text of the option, including any potential key (for instance, `"NOTIFY=SUCCESS,FAILURE"`). (If you need to use different ESMTP options to different recipients you have to use the low-level methods such as `mail()`, `rcpt()` and `data()` to send the message.)
Note
The _from_addr_ and _to_addrs_ parameters are used to construct the message envelope used by the transport agents. `sendmail` does not modify the message headers in any way.
_msg_ may be a string containing characters in the ASCII range, or a byte string. A string is encoded to bytes using the ascii codec, and lone `\r` and `\n` characters are converted to `\r\n` characters. A byte string is not modified.
If there has been no previous `EHLO` or `HELO` command this session, this method tries ESMTP `EHLO` first. If the server does ESMTP, message size and each of the specified options will be passed to it (if the option is in the feature set the server advertises). If `EHLO` fails, `HELO` will be tried and ESMTP options suppressed.
This method will return normally if the mail is accepted for at least one recipient. Otherwise it will raise an exception. That is, if this method does not raise an exception, then someone should get your mail. If this method does not raise an exception, it returns a dictionary, with one entry for each recipient that was refused. Each entry contains a tuple of the SMTP error code and the accompanying error message sent by the server.
If `SMTPUTF8` is included in _mail_options_ , and the server supports it, _from_addr_ and _to_addrs_ may contain non-ASCII characters.
This method may raise the following exceptions:

[`SMTPRecipientsRefused`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPRecipientsRefused "smtplib.SMTPRecipientsRefused")

All recipients were refused. Nobody got the mail.

[`SMTPHeloError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPHeloError "smtplib.SMTPHeloError")

The server didn’t reply properly to the `HELO` greeting.

[`SMTPSenderRefused`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPSenderRefused "smtplib.SMTPSenderRefused")

The server didn’t accept the _from_addr_.

[`SMTPDataError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPDataError "smtplib.SMTPDataError")

The server replied with an unexpected error code (other than a refusal of a recipient).

[`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError")

`SMTPUTF8` was given in the _mail_options_ but is not supported by the server.
Unless otherwise noted, the connection will be open even after an exception is raised.
Changed in version 3.2: _msg_ may be a byte string.
Changed in version 3.5: `SMTPUTF8` support added, and [`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError") may be raised if `SMTPUTF8` is specified but the server does not support it.

SMTP.send_message(_msg_ , _from_addr =None_, _to_addrs =None_, _mail_options =()_, _rcpt_options =()_)[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message "Link to this definition")

This is a convenience method for calling [`sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail") with the message represented by an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") object. The arguments have the same meaning as for `sendmail()`, except that _msg_ is a `Message` object.
If _from_addr_ is `None` or _to_addrs_ is `None`, `send_message` fills those arguments with addresses extracted from the headers of _msg_ as specified in _from_addr_ is set to the _Sender_ field if it is present, and otherwise to the _From_ field. _to_addrs_ combines the values (if any) of the _To_ , _Cc_ , and _Bcc_ fields from _msg_. If exactly one set of _Resent-*_ headers appear in the message, the regular headers are ignored and the _Resent-*_ headers are used instead. If the message contains more than one set of _Resent-*_ headers, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised, since there is no way to unambiguously detect the most recent set of _Resent-_ headers.
`send_message` serializes _msg_ using [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator") with `\r\n` as the _linesep_ , and calls [`sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail") to transmit the resulting message. Regardless of the values of _from_addr_ and _to_addrs_ , `send_message` does not transmit any _Bcc_ or _Resent-Bcc_ headers that may appear in _msg_. If any of the addresses in _from_addr_ and _to_addrs_ contain non-ASCII characters and the server does not advertise `SMTPUTF8` support, an [`SMTPNotSupportedError`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPNotSupportedError "smtplib.SMTPNotSupportedError") is raised. Otherwise the `Message` is serialized with a clone of its [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages") with the [`utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8") attribute set to `True`, and `SMTPUTF8` and `BODY=8BITMIME` are added to _mail_options_.
Added in version 3.2.
Added in version 3.5: Support for internationalized addresses (`SMTPUTF8`).

SMTP.quit()[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.quit "Link to this definition")

Terminate the SMTP session and close the connection. Return the result of the SMTP `QUIT` command.
Low-level methods corresponding to the standard SMTP/ESMTP commands `HELP`, `RSET`, `NOOP`, `MAIL`, `RCPT`, and `DATA` are also supported. Normally these do not need to be called directly, so they are not documented here. For details, consult the module code.
Additionally, an SMTP instance has the following attributes:

SMTP.helo_resp[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.helo_resp "Link to this definition")

The response to the `HELO` command, see [`helo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.helo "smtplib.SMTP.helo").

SMTP.ehlo_resp[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo_resp "Link to this definition")

The response to the `EHLO` command, see [`ehlo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo "smtplib.SMTP.ehlo").

SMTP.does_esmtp[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.does_esmtp "Link to this definition")

A boolean value indicating whether the server supports ESMTP, see [`ehlo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo "smtplib.SMTP.ehlo").

SMTP.esmtp_features[¶](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.esmtp_features "Link to this definition")

A dictionary of the names of SMTP service extensions supported by the server, see [`ehlo()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.ehlo "smtplib.SMTP.ehlo").
## SMTP Example[¶](https://docs.python.org/3/library/smtplib.html#smtp-example "Link to this heading")
This example prompts the user for addresses needed in the message envelope (‘To’ and ‘From’ addresses), and the message to be delivered. Note that the headers to be included with the message must be included in the message as entered; this example doesn’t do any processing of the
Copy```
import smtplib

def prompt(title):
    return input(title).strip()

from_addr = prompt("From: ")
to_addrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
lines = [f"From: {from_addr}", f"To: {', '.join(to_addrs)}", ""]
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        lines.append(line)

msg = "\r\n".join(lines)
print("Message length is", len(msg))

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(from_addr, to_addrs, msg)
server.quit()

```

Note
In general, you will want to use the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package’s features to construct an email message, which you can then send via [`send_message()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message "smtplib.SMTP.send_message"); see [email: Examples](https://docs.python.org/3/library/email.examples.html#email-examples).
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
    * [SMTP Objects](https://docs.python.org/3/library/smtplib.html#smtp-objects)
    * [SMTP Example](https://docs.python.org/3/library/smtplib.html#smtp-example)


#### Previous topic
[`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html "previous chapter")
#### Next topic
[`uuid` — UUID objects according to **RFC 9562**](https://docs.python.org/3/library/uuid.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=smtplib+%E2%80%94+SMTP+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsmtplib.html&pagesource=library%2Fsmtplib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/uuid.html "uuid — UUID objects according to RFC 9562") |
  * [previous](https://docs.python.org/3/library/imaplib.html "imaplib — IMAP4 protocol client") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
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
