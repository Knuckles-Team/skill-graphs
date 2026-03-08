# create a raw socket and bind it to the 'vcan0' interface
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0',))

while True:
    cf, addr = s.recvfrom(can_frame_size)

    print('Received: can_id=%x, can_dlc=%x, data=%s' % dissect_can_frame(cf))

    try:
        s.send(cf)
    except OSError:
        print('Error sending CAN frame')

    try:
        s.send(build_can_frame(0x01, b'\x01\x02\x03'))
    except OSError:
        print('Error sending CAN frame')

```

Running an example several times with too small delay between executions, could lead to this error:
Copy```
OSError: [Errno 98] Address already in use

```

This is because the previous execution has left the socket in a `TIME_WAIT` state, and can’t be immediately reused.
There is a `socket` flag to set, in order to prevent this, `socket.SO_REUSEADDR`:
Copy```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

```

the `SO_REUSEADDR` flag tells the kernel to reuse a local socket in `TIME_WAIT` state, without waiting for its natural timeout to expire.
See also
For an introduction to socket programming (in C), see the following papers:
  * _An Introductory 4.3BSD Interprocess Communication Tutorial_ , by Stuart Sechrest
  * _An Advanced 4.3BSD Interprocess Communication Tutorial_ , by Samuel J. Leffler et al,


both in the UNIX Programmer’s Manual, Supplementary Documents 1 (sections PS1:7 and PS1:8). The platform-specific reference material for the various socket-related system calls are also a valuable source of information on the details of socket semantics. For Unix, refer to the manual pages; for Windows, see the WinSock (or Winsock 2) specification. For IPv6-ready APIs, readers may want to refer to
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html)
    * [Socket families](https://docs.python.org/3/library/socket.html#socket-families)
    * [Module contents](https://docs.python.org/3/library/socket.html#module-contents)
      * [Exceptions](https://docs.python.org/3/library/socket.html#exceptions)
      * [Constants](https://docs.python.org/3/library/socket.html#constants)
      * [Functions](https://docs.python.org/3/library/socket.html#functions)
        * [Creating sockets](https://docs.python.org/3/library/socket.html#creating-sockets)
        * [Other functions](https://docs.python.org/3/library/socket.html#other-functions)
    * [Socket Objects](https://docs.python.org/3/library/socket.html#socket-objects)
    * [Notes on socket timeouts](https://docs.python.org/3/library/socket.html#notes-on-socket-timeouts)
      * [Timeouts and the `connect` method](https://docs.python.org/3/library/socket.html#timeouts-and-the-connect-method)
      * [Timeouts and the `accept` method](https://docs.python.org/3/library/socket.html#timeouts-and-the-accept-method)
    * [Example](https://docs.python.org/3/library/socket.html#example)


#### Previous topic
[Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html "previous chapter")
#### Next topic
[`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=socket+%E2%80%94+Low-level+networking+interface&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsocket.html&pagesource=library%2Fsocket.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects") |
  * [previous](https://docs.python.org/3/library/asyncio-dev.html "Developing with asyncio") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html)
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
