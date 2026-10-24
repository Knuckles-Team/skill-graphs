[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [XML Processing Modules](https://docs.python.org/3/library/xml.html)
    * [XML security](https://docs.python.org/3/library/xml.html#xml-vulnerabilities)


#### Previous topic
[`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html "previous chapter")
#### Next topic
[`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=XML+Processing+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.html&pagesource=library%2Fxml.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.etree.elementtree.html "xml.etree.ElementTree — The ElementTree XML API") |
  * [previous](https://docs.python.org/3/library/html.entities.html "html.entities — Definitions of HTML general entities") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [XML Processing Modules](https://docs.python.org/3/library/xml.html)
  * |
  * Theme  Auto Light Dark |


# XML Processing Modules[¶](https://docs.python.org/3/library/xml.html#module-xml "Link to this heading")
**Source code:**
* * *
Python’s interfaces for processing XML are grouped in the `xml` package.
Note
If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security).
It is important to note that modules in the `xml` package require that there be at least one SAX-compliant XML parser available. The Expat parser is included with Python, so the [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") module will always be available.
The documentation for the [`xml.dom`](https://docs.python.org/3/library/xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python.") and [`xml.sax`](https://docs.python.org/3/library/xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions.") packages are the definition of the Python bindings for the DOM and SAX interfaces.
The XML handling submodules are:
  * [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API."): the ElementTree API, a simple and lightweight XML processor


  * [`xml.dom`](https://docs.python.org/3/library/xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python."): the DOM API definition
  * [`xml.dom.minidom`](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom "xml.dom.minidom: Minimal Document Object Model \(DOM\) implementation."): a minimal DOM implementation
  * [`xml.dom.pulldom`](https://docs.python.org/3/library/xml.dom.pulldom.html#module-xml.dom.pulldom "xml.dom.pulldom: Support for building partial DOM trees from SAX events."): support for building partial DOM trees


  * [`xml.sax`](https://docs.python.org/3/library/xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions."): SAX2 base classes and convenience functions
  * [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser."): the Expat parser binding


## XML security[¶](https://docs.python.org/3/library/xml.html#xml-vulnerabilities "Link to this heading")
An attacker can abuse XML features to carry out denial of service attacks, access local files, generate network connections to other machines, or circumvent firewalls when attacker-controlled XML is being parsed, in Python or elsewhere.
The built-in XML parsers of Python rely on the library
By default, Expat itself does not access local files or create network connections.
Expat versions lower than 2.7.2 may be vulnerable to the “billion laughs”, “quadratic blowup” and “large tokens” vulnerabilities, or to disproportional use of dynamic memory. Python bundles a copy of Expat, and whether Python uses the bundled or a system-wide Expat, depends on how the Python interpreter [`has been configured`](https://docs.python.org/3/using/configure.html#cmdoption-with-system-expat) in your environment. Python may be vulnerable if it uses such older versions of Expat. Check `pyexpat.EXPAT_VERSION`.
[`xmlrpc`](https://docs.python.org/3/library/xmlrpc.html#module-xmlrpc "xmlrpc: Server and client modules implementing XML-RPC.") is **vulnerable** to the “decompression bomb” attack.

billion laughs / exponential entity expansion

The

quadratic blowup entity expansion

A quadratic blowup attack is similar to a

decompression bomb

Decompression bombs (aka

large tokens

Expat needs to re-parse unfinished tokens; without the protection introduced in Expat 2.6.0, this can lead to quadratic runtime that can be used to cause denial of service in the application parsing XML. The issue is known as
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [XML Processing Modules](https://docs.python.org/3/library/xml.html)
    * [XML security](https://docs.python.org/3/library/xml.html#xml-vulnerabilities)


#### Previous topic
[`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html "previous chapter")
#### Next topic
[`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=XML+Processing+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.html&pagesource=library%2Fxml.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.etree.elementtree.html "xml.etree.ElementTree — The ElementTree XML API") |
  * [previous](https://docs.python.org/3/library/html.entities.html "html.entities — Definitions of HTML general entities") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [XML Processing Modules](https://docs.python.org/3/library/xml.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
