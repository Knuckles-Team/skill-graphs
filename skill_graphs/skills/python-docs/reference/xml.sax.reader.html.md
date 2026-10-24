[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html)
    * [XMLReader Objects](https://docs.python.org/3/library/xml.sax.reader.html#xmlreader-objects)
    * [IncrementalParser Objects](https://docs.python.org/3/library/xml.sax.reader.html#incrementalparser-objects)
    * [Locator Objects](https://docs.python.org/3/library/xml.sax.reader.html#locator-objects)
    * [InputSource Objects](https://docs.python.org/3/library/xml.sax.reader.html#inputsource-objects)
    * [The `Attributes` Interface](https://docs.python.org/3/library/xml.sax.reader.html#the-attributes-interface)
    * [The `AttributesNS` Interface](https://docs.python.org/3/library/xml.sax.reader.html#the-attributesns-interface)


#### Previous topic
[`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html "previous chapter")
#### Next topic
[`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.sax.xmlreader+%E2%80%94+Interface+for+XML+parsers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.sax.reader.html&pagesource=library%2Fxml.sax.reader.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
  * [previous](https://docs.python.org/3/library/xml.sax.utils.html "xml.sax.saxutils — SAX Utilities") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html)
  * |
  * Theme  Auto Light Dark |


#  `xml.sax.xmlreader` — Interface for XML parsers[¶](https://docs.python.org/3/library/xml.sax.reader.html#module-xml.sax.xmlreader "Link to this heading")
**Source code:**
* * *
SAX parsers implement the [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") interface. They are implemented in a Python module, which must provide a function `create_parser()`. This function is invoked by [`xml.sax.make_parser()`](https://docs.python.org/3/library/xml.sax.html#xml.sax.make_parser "xml.sax.make_parser") with no arguments to create a new parser object.

_class_ xml.sax.xmlreader.XMLReader[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "Link to this definition")

Base class which can be inherited by SAX parsers.

_class_ xml.sax.xmlreader.IncrementalParser[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.IncrementalParser "Link to this definition")

In some cases, it is desirable not to parse an input source at once, but to feed chunks of the document as they get available. Note that the reader will normally not read the entire file, but read it in chunks as well; still `parse()` won’t return until the entire document is processed. So these interfaces should be used if the blocking behaviour of `parse()` is not desirable.
When the parser is instantiated it is ready to begin accepting data from the feed method immediately. After parsing has been finished with a call to close the reset method must be called to make the parser ready to accept new data, either from feed or using the parse method.
Note that these methods must _not_ be called during parsing, that is, after parse has been called and before it returns.
By default, the class also implements the parse method of the XMLReader interface using the feed, close and reset methods of the IncrementalParser interface as a convenience to SAX 2.0 driver writers.

_class_ xml.sax.xmlreader.Locator[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator "Link to this definition")

Interface for associating a SAX event with a document location. A locator object will return valid results only during calls to DocumentHandler methods; at any other time, the results are unpredictable. If information is not available, methods may return `None`.

_class_ xml.sax.xmlreader.InputSource(_system_id =None_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "Link to this definition")

Encapsulation of the information needed by the [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") to read entities.
This class may include information about the public identifier, system identifier, byte stream (possibly with character encoding information) and/or the character stream of an entity.
Applications will create objects of this class for use in the [`XMLReader.parse()`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.parse "xml.sax.xmlreader.XMLReader.parse") method and for returning from EntityResolver.resolveEntity.
An `InputSource` belongs to the application, the [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") is not allowed to modify `InputSource` objects passed to it from the application, although it may make copies and modify those.

_class_ xml.sax.xmlreader.AttributesImpl(_attrs_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesImpl "Link to this definition")

This is an implementation of the `Attributes` interface (see section [The Attributes Interface](https://docs.python.org/3/library/xml.sax.reader.html#attributes-objects)). This is a dictionary-like object which represents the element attributes in a `startElement()` call. In addition to the most useful dictionary operations, it supports a number of other methods as described by the interface. Objects of this class should be instantiated by readers; _attrs_ must be a dictionary-like object containing a mapping from attribute names to attribute values.

_class_ xml.sax.xmlreader.AttributesNSImpl(_attrs_ , _qnames_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesNSImpl "Link to this definition")

Namespace-aware variant of [`AttributesImpl`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesImpl "xml.sax.xmlreader.AttributesImpl"), which will be passed to `startElementNS()`. It is derived from `AttributesImpl`, but understands attribute names as two-tuples of _namespaceURI_ and _localname_. In addition, it provides a number of methods expecting qualified names as they appear in the original document. This class implements the `AttributesNS` interface (see section [The AttributesNS Interface](https://docs.python.org/3/library/xml.sax.reader.html#attributes-ns-objects)).
## XMLReader Objects[¶](https://docs.python.org/3/library/xml.sax.reader.html#xmlreader-objects "Link to this heading")
The [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") interface supports the following methods:

XMLReader.parse(_source_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.parse "Link to this definition")

Process an input source, producing SAX events. The _source_ object can be a system identifier (a string identifying the input source – typically a file name or a URL), a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") or [path-like](https://docs.python.org/3/glossary.html#term-path-like-object) object, or an [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") object. When `parse()` returns, the input is completely processed, and the parser object can be discarded or reset.
Changed in version 3.5: Added support of character streams.
Changed in version 3.8: Added support of path-like objects.

XMLReader.getContentHandler()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.getContentHandler "Link to this definition")

Return the current [`ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler").

XMLReader.setContentHandler(_handler_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setContentHandler "Link to this definition")

Set the current [`ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler"). If no `ContentHandler` is set, content events will be discarded.

XMLReader.getDTDHandler()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.getDTDHandler "Link to this definition")

Return the current [`DTDHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.DTDHandler "xml.sax.handler.DTDHandler").

XMLReader.setDTDHandler(_handler_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setDTDHandler "Link to this definition")

Set the current [`DTDHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.DTDHandler "xml.sax.handler.DTDHandler"). If no `DTDHandler` is set, DTD events will be discarded.

XMLReader.getEntityResolver()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.getEntityResolver "Link to this definition")

Return the current [`EntityResolver`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.EntityResolver "xml.sax.handler.EntityResolver").

XMLReader.setEntityResolver(_handler_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setEntityResolver "Link to this definition")

Set the current [`EntityResolver`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.EntityResolver "xml.sax.handler.EntityResolver"). If no `EntityResolver` is set, attempts to resolve an external entity will result in opening the system identifier for the entity, and fail if it is not available.

XMLReader.getErrorHandler()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.getErrorHandler "Link to this definition")

Return the current [`ErrorHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler").

XMLReader.setErrorHandler(_handler_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setErrorHandler "Link to this definition")

Set the current error handler. If no [`ErrorHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler") is set, errors will be raised as exceptions, and warnings will be printed.

XMLReader.setLocale(_locale_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setLocale "Link to this definition")

Allow an application to set the locale for errors and warnings.
SAX parsers are not required to provide localization for errors and warnings; if they cannot support the requested locale, however, they must raise a SAX exception. Applications may request a locale change in the middle of a parse.

XMLReader.getFeature(_featurename_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.getFeature "Link to this definition")

Return the current setting for feature _featurename_. If the feature is not recognized, `SAXNotRecognizedException` is raised. The well-known featurenames are listed in the module [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.").

XMLReader.setFeature(_featurename_ , _value_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setFeature "Link to this definition")

Set the _featurename_ to _value_. If the feature is not recognized, `SAXNotRecognizedException` is raised. If the feature or its setting is not supported by the parser, _SAXNotSupportedException_ is raised.

XMLReader.getProperty(_propertyname_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.getProperty "Link to this definition")

Return the current setting for property _propertyname_. If the property is not recognized, a `SAXNotRecognizedException` is raised. The well-known propertynames are listed in the module [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.").

XMLReader.setProperty(_propertyname_ , _value_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setProperty "Link to this definition")

Set the _propertyname_ to _value_. If the property is not recognized, `SAXNotRecognizedException` is raised. If the property or its setting is not supported by the parser, _SAXNotSupportedException_ is raised.
## IncrementalParser Objects[¶](https://docs.python.org/3/library/xml.sax.reader.html#incrementalparser-objects "Link to this heading")
Instances of [`IncrementalParser`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.IncrementalParser "xml.sax.xmlreader.IncrementalParser") offer the following additional methods:

IncrementalParser.feed(_data_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.IncrementalParser.feed "Link to this definition")

Process a chunk of _data_.

IncrementalParser.close()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.IncrementalParser.close "Link to this definition")

Assume the end of the document. That will check well-formedness conditions that can be checked only at the end, invoke handlers, and may clean up resources allocated during parsing.

IncrementalParser.reset()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.IncrementalParser.reset "Link to this definition")

This method is called after close has been called to reset the parser so that it is ready to parse new documents. The results of calling parse or feed after close without calling reset are undefined.
## Locator Objects[¶](https://docs.python.org/3/library/xml.sax.reader.html#locator-objects "Link to this heading")
Instances of [`Locator`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator "xml.sax.xmlreader.Locator") provide these methods:

Locator.getColumnNumber()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator.getColumnNumber "Link to this definition")

Return the column number where the current event begins.

Locator.getLineNumber()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator.getLineNumber "Link to this definition")

Return the line number where the current event begins.

Locator.getPublicId()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator.getPublicId "Link to this definition")

Return the public identifier for the current event.

Locator.getSystemId()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator.getSystemId "Link to this definition")

Return the system identifier for the current event.
## InputSource Objects[¶](https://docs.python.org/3/library/xml.sax.reader.html#inputsource-objects "Link to this heading")

InputSource.setPublicId(_id_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.setPublicId "Link to this definition")

Sets the public identifier of this [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.getPublicId()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.getPublicId "Link to this definition")

Returns the public identifier of this [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.setSystemId(_id_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.setSystemId "Link to this definition")

Sets the system identifier of this [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.getSystemId()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.getSystemId "Link to this definition")

Returns the system identifier of this [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.setEncoding(_encoding_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.setEncoding "Link to this definition")

Sets the character encoding of this [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").
The encoding must be a string acceptable for an XML encoding declaration (see section 4.3.3 of the XML recommendation).
The encoding attribute of the [`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") is ignored if the `InputSource` also contains a character stream.

InputSource.getEncoding()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.getEncoding "Link to this definition")

Get the character encoding of this InputSource.

InputSource.setByteStream(_bytefile_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.setByteStream "Link to this definition")

Set the byte stream (a [binary file](https://docs.python.org/3/glossary.html#term-binary-file)) for this input source.
The SAX parser will ignore this if there is also a character stream specified, but it will use a byte stream in preference to opening a URI connection itself.
If the application knows the character encoding of the byte stream, it should set it with the setEncoding method.

InputSource.getByteStream()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.getByteStream "Link to this definition")

Get the byte stream for this input source.
The getEncoding method will return the character encoding for this byte stream, or `None` if unknown.

InputSource.setCharacterStream(_charfile_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.setCharacterStream "Link to this definition")

Set the character stream (a [text file](https://docs.python.org/3/glossary.html#term-text-file)) for this input source.
If there is a character stream specified, the SAX parser will ignore any byte stream and will not attempt to open a URI connection to the system identifier.

InputSource.getCharacterStream()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource.getCharacterStream "Link to this definition")

Get the character stream for this input source.
## The `Attributes` Interface[¶](https://docs.python.org/3/library/xml.sax.reader.html#the-attributes-interface "Link to this heading")
`Attributes` objects implement a portion of the [mapping protocol](https://docs.python.org/3/glossary.html#term-mapping), including the methods `copy()`, `get()`, [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__"), `items()`, `keys()`, and `values()`. The following methods are also provided:

Attributes.getLength()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Attributes.getLength "Link to this definition")

Return the number of attributes.

Attributes.getNames()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Attributes.getNames "Link to this definition")

Return the names of the attributes.

Attributes.getType(_name_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Attributes.getType "Link to this definition")

Returns the type of the attribute _name_ , which is normally `'CDATA'`.

Attributes.getValue(_name_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Attributes.getValue "Link to this definition")

Return the value of attribute _name_.
## The `AttributesNS` Interface[¶](https://docs.python.org/3/library/xml.sax.reader.html#the-attributesns-interface "Link to this heading")
This interface is a subtype of the `Attributes` interface (see section [The Attributes Interface](https://docs.python.org/3/library/xml.sax.reader.html#attributes-objects)). All methods supported by that interface are also available on `AttributesNS` objects.
The following methods are also available:

AttributesNS.getValueByQName(_name_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesNS.getValueByQName "Link to this definition")

Return the value for a qualified name.

AttributesNS.getNameByQName(_name_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesNS.getNameByQName "Link to this definition")

Return the `(namespace, localname)` pair for a qualified _name_.

AttributesNS.getQNameByName(_name_)[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesNS.getQNameByName "Link to this definition")

Return the qualified name for a `(namespace, localname)` pair.

AttributesNS.getQNames()[¶](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.AttributesNS.getQNames "Link to this definition")

Return the qualified names of all attributes.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html)
    * [XMLReader Objects](https://docs.python.org/3/library/xml.sax.reader.html#xmlreader-objects)
    * [IncrementalParser Objects](https://docs.python.org/3/library/xml.sax.reader.html#incrementalparser-objects)
    * [Locator Objects](https://docs.python.org/3/library/xml.sax.reader.html#locator-objects)
    * [InputSource Objects](https://docs.python.org/3/library/xml.sax.reader.html#inputsource-objects)
    * [The `Attributes` Interface](https://docs.python.org/3/library/xml.sax.reader.html#the-attributes-interface)
    * [The `AttributesNS` Interface](https://docs.python.org/3/library/xml.sax.reader.html#the-attributesns-interface)


#### Previous topic
[`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html "previous chapter")
#### Next topic
[`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.sax.xmlreader+%E2%80%94+Interface+for+XML+parsers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.sax.reader.html&pagesource=library%2Fxml.sax.reader.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
  * [previous](https://docs.python.org/3/library/xml.sax.utils.html "xml.sax.saxutils — SAX Utilities") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
