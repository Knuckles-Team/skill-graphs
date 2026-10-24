[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
    * [Functions, Constants, and Exceptions](https://docs.python.org/3/library/ssl.html#functions-constants-and-exceptions)
      * [Socket creation](https://docs.python.org/3/library/ssl.html#socket-creation)
      * [Context creation](https://docs.python.org/3/library/ssl.html#context-creation)
      * [Exceptions](https://docs.python.org/3/library/ssl.html#exceptions)
      * [Random generation](https://docs.python.org/3/library/ssl.html#random-generation)
      * [Certificate handling](https://docs.python.org/3/library/ssl.html#certificate-handling)
      * [Constants](https://docs.python.org/3/library/ssl.html#constants)
    * [SSL Sockets](https://docs.python.org/3/library/ssl.html#ssl-sockets)
    * [SSL Contexts](https://docs.python.org/3/library/ssl.html#ssl-contexts)
    * [Certificates](https://docs.python.org/3/library/ssl.html#certificates)
      * [Certificate chains](https://docs.python.org/3/library/ssl.html#certificate-chains)
      * [CA certificates](https://docs.python.org/3/library/ssl.html#ca-certificates)
      * [Combined key and certificate](https://docs.python.org/3/library/ssl.html#combined-key-and-certificate)
      * [Self-signed certificates](https://docs.python.org/3/library/ssl.html#self-signed-certificates)
    * [Examples](https://docs.python.org/3/library/ssl.html#examples)
      * [Testing for SSL support](https://docs.python.org/3/library/ssl.html#testing-for-ssl-support)
      * [Client-side operation](https://docs.python.org/3/library/ssl.html#client-side-operation)
      * [Server-side operation](https://docs.python.org/3/library/ssl.html#server-side-operation)
    * [Notes on non-blocking sockets](https://docs.python.org/3/library/ssl.html#notes-on-non-blocking-sockets)
    * [Memory BIO Support](https://docs.python.org/3/library/ssl.html#memory-bio-support)
    * [SSL session](https://docs.python.org/3/library/ssl.html#ssl-session)
    * [Security considerations](https://docs.python.org/3/library/ssl.html#security-considerations)
      * [Best defaults](https://docs.python.org/3/library/ssl.html#best-defaults)
      * [Manual settings](https://docs.python.org/3/library/ssl.html#manual-settings)
        * [Verifying certificates](https://docs.python.org/3/library/ssl.html#verifying-certificates)
        * [Protocol versions](https://docs.python.org/3/library/ssl.html#protocol-versions)
        * [Cipher selection](https://docs.python.org/3/library/ssl.html#cipher-selection)
      * [Multi-processing](https://docs.python.org/3/library/ssl.html#multi-processing)
    * [TLS 1.3](https://docs.python.org/3/library/ssl.html#tls-1-3)


#### Previous topic
[`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html "previous chapter")
#### Next topic
[`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ssl+%E2%80%94+TLS%2FSSL+wrapper+for+socket+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fssl.html&pagesource=library%2Fssl.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/select.html "select — Waiting for I/O completion") |
  * [previous](https://docs.python.org/3/library/socket.html "socket — Low-level networking interface") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
  * |
  * Theme  Auto Light Dark |
