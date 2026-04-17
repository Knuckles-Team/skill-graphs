[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html "previous chapter")
#### Next topic
[`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.sax.saxutils+%E2%80%94+SAX+Utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.sax.utils.html&pagesource=library%2Fxml.sax.utils.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
  * [previous](https://docs.python.org/3/library/xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html)
  * |
  * Theme  Auto Light Dark |


#  `xml.sax.saxutils` — SAX Utilities[¶](https://docs.python.org/3/library/xml.sax.utils.html#module-xml.sax.saxutils "Link to this heading")
**Source code:**
* * *
The module `xml.sax.saxutils` contains a number of classes and functions that are commonly useful when creating SAX applications, either in direct use, or as base classes.

xml.sax.saxutils.escape(_data_ , _entities ={}_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.escape "Link to this definition")

Escape `'&'`, `'<'`, and `'>'` in a string of data.
You can escape other strings of data by passing a dictionary as the optional _entities_ parameter. The keys and values must all be strings; each key will be replaced with its corresponding value. The characters `'&'`, `'<'` and `'>'` are always escaped, even if _entities_ is provided.
Note
This function should only be used to escape characters that can’t be used directly in XML. Do not use this function as a general string translation function.

xml.sax.saxutils.unescape(_data_ , _entities ={}_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.unescape "Link to this definition")

Unescape `'&amp;'`, `'&lt;'`, and `'&gt;'` in a string of data.
You can unescape other strings of data by passing a dictionary as the optional _entities_ parameter. The keys and values must all be strings; each key will be replaced with its corresponding value. `'&amp;'`, `'&lt;'`, and `'&gt;'` are always unescaped, even if _entities_ is provided.

xml.sax.saxutils.quoteattr(_data_ , _entities ={}_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.quoteattr "Link to this definition")

Similar to [`escape()`](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.escape "xml.sax.saxutils.escape"), but also prepares _data_ to be used as an attribute value. The return value is a quoted version of _data_ with any additional required replacements. `quoteattr()` will select a quote character based on the content of _data_ , attempting to avoid encoding any quote characters in the string. If both single- and double-quote characters are already in _data_ , the double-quote characters will be encoded and _data_ will be wrapped in double-quotes. The resulting string can be used directly as an attribute value:
Copy```
>>> print("<element attr=%s>" % quoteattr("ab ' cd \" ef"))
<element attr="ab ' cd &quot; ef">

```

This function is useful when generating attribute values for HTML or any SGML using the reference concrete syntax.

_class_ xml.sax.saxutils.XMLGenerator(_out =None_, _encoding ='iso-8859-1'_, _short_empty_elements =False_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.XMLGenerator "Link to this definition")

This class implements the [`ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler") interface by writing SAX events back into an XML document. In other words, using an `XMLGenerator` as the content handler will reproduce the original document being parsed. _out_ should be a file-like object which will default to _sys.stdout_. _encoding_ is the encoding of the output stream which defaults to `'iso-8859-1'`. _short_empty_elements_ controls the formatting of elements that contain no content: if `False` (the default) they are emitted as a pair of start/end tags, if set to `True` they are emitted as a single self-closed tag.
Changed in version 3.2: Added the _short_empty_elements_ parameter.

_class_ xml.sax.saxutils.XMLFilterBase(_base_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.XMLFilterBase "Link to this definition")

This class is designed to sit between an [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") and the client application’s event handlers. By default, it does nothing but pass requests up to the reader and events on to the handlers unmodified, but subclasses can override specific methods to modify the event stream or the configuration requests as they pass through.

xml.sax.saxutils.prepare_input_source(_source_ , _base =''_)[¶](https://docs.python.org/3/library/xml.sax.utils.html#xml.sax.saxutils.prepare_input_source "Link to this definition")

This function takes an input source and an optional base URL and returns a fully resolved [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") object ready for reading. The input source can be given as a string, a file-like object, or an `InputSource` object; parsers will use this function to implement the polymorphic _source_ argument to their [`parse()`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.parse "xml.sax.xmlreader.XMLReader.parse") method.
#### Previous topic
[`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html "previous chapter")
#### Next topic
[`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.sax.saxutils+%E2%80%94+SAX+Utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.sax.utils.html&pagesource=library%2Fxml.sax.utils.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
  * [previous](https://docs.python.org/3/library/xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
