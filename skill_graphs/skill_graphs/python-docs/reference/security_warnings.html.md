[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`xdrlib` — Encode and decode XDR data](https://docs.python.org/3/library/xdrlib.html "previous chapter")
#### Next topic
[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Security+Considerations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsecurity_warnings.html&pagesource=library%2Fsecurity_warnings.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/extending/index.html "Extending and Embedding the Python Interpreter") |
  * [previous](https://docs.python.org/3/library/xdrlib.html "xdrlib — Encode and decode XDR data") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Security Considerations](https://docs.python.org/3/library/security_warnings.html)
  * |
  * Theme  Auto Light Dark |


# Security Considerations[¶](https://docs.python.org/3/library/security_warnings.html#security-considerations "Link to this heading")
The following modules have specific security considerations:
  * [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85"): [base64 security considerations](https://docs.python.org/3/library/base64.html#base64-security) in
  * [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms."): [all constructors take a “usedforsecurity” keyword-only argument disabling known insecure and blocked algorithms](https://docs.python.org/3/library/hashlib.html#hashlib-usedforsecurity)
  * [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.") is not suitable for production use, only implementing basic security checks. See the [security considerations](https://docs.python.org/3/library/http.server.html#http-server-security).
  * [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications."): [Logging configuration uses eval()](https://docs.python.org/3/library/logging.config.html#logging-eval-security)
  * [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism."): [Connection.recv() uses pickle](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-recv-pickle-security)
  * [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."): [Restricting globals in pickle](https://docs.python.org/3/library/pickle.html#pickle-restrict)
  * [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") shouldn’t be used for security purposes, use [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.") instead
  * [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence."): [shelve is based on pickle and thus unsuitable for dealing with untrusted sources](https://docs.python.org/3/library/shelve.html#shelve-security)
  * [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects"): [SSL/TLS security considerations](https://docs.python.org/3/library/ssl.html#ssl-security)
  * [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management."): [Subprocess security considerations](https://docs.python.org/3/library/subprocess.html#subprocess-security)
  * [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories."): [mktemp is deprecated due to vulnerability to race conditions](https://docs.python.org/3/library/tempfile.html#tempfile-mktemp-deprecated)
  * [`xml`](https://docs.python.org/3/library/xml.html#module-xml "xml: Package containing XML processing modules"): [XML security](https://docs.python.org/3/library/xml.html#xml-security)
  * [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files."): [maliciously prepared .zip files can cause disk volume exhaustion](https://docs.python.org/3/library/zipfile.html#zipfile-resources-limitations)


The [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I) command line option can be used to run Python in isolated mode. When it cannot be used, the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P) option or the [`PYTHONSAFEPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable can be used to not prepend a potentially unsafe path to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") such as the current directory, the script’s directory or an empty string.
#### Previous topic
[`xdrlib` — Encode and decode XDR data](https://docs.python.org/3/library/xdrlib.html "previous chapter")
#### Next topic
[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Security+Considerations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsecurity_warnings.html&pagesource=library%2Fsecurity_warnings.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/extending/index.html "Extending and Embedding the Python Interpreter") |
  * [previous](https://docs.python.org/3/library/xdrlib.html "xdrlib — Encode and decode XDR data") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Security Considerations](https://docs.python.org/3/library/security_warnings.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
