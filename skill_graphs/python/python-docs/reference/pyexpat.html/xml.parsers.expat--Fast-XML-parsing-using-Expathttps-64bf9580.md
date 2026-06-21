#  `xml.parsers.expat` — Fast XML parsing using Expat[¶](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "Link to this heading")
* * *
Note
If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security).
The `xml.parsers.expat` module is a Python interface to the Expat non-validating XML parser. The module provides a single extension type, `xmlparser`, that represents the current state of an XML parser. After an `xmlparser` object has been created, various attributes of the object can be set to handler functions. When an XML document is then fed to the parser, the handler functions are called for the character data and markup in the XML document.
This module uses the `pyexpat` module to provide access to the Expat parser. Direct use of the `pyexpat` module is deprecated.
This module provides one exception and one type object:

_exception_ xml.parsers.expat.ExpatError[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "Link to this definition")

The exception raised when Expat reports an error. See section [ExpatError Exceptions](https://docs.python.org/3/library/pyexpat.html#expaterror-objects) for more information on interpreting Expat errors.

_exception_ xml.parsers.expat.error[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.error "Link to this definition")

Alias for [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError").

xml.parsers.expat.XMLParserType[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.XMLParserType "Link to this definition")

The type of the return values from the [`ParserCreate()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ParserCreate "xml.parsers.expat.ParserCreate") function.
The `xml.parsers.expat` module contains two functions:

xml.parsers.expat.ErrorString(_errno_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ErrorString "Link to this definition")

Returns an explanatory string for a given error number _errno_.

xml.parsers.expat.ParserCreate(_encoding =None_, _namespace_separator =None_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ParserCreate "Link to this definition")

Creates and returns a new `xmlparser` object. _encoding_ , if specified, must be a string naming the encoding used by the XML data. Expat doesn’t support as many encodings as Python does, and its repertoire of encodings can’t be extended; it supports UTF-8, UTF-16, ISO-8859-1 (Latin1), and ASCII. If _encoding_ [[1]](https://docs.python.org/3/library/pyexpat.html#id3) is given it will override the implicit or explicit encoding of the document.
Parsers created through `ParserCreate()` are called “root” parsers, in the sense that they do not have any parent parser attached. Non-root parsers are created by [`parser.ExternalEntityParserCreate`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityParserCreate "xml.parsers.expat.xmlparser.ExternalEntityParserCreate").
Expat can optionally do XML namespace processing for you, enabled by providing a value for _namespace_separator_. The value must be a one-character string; a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised if the string has an illegal length (`None` is considered the same as omission). When namespace processing is enabled, element type names and attribute names that belong to a namespace will be expanded. The element name passed to the element handlers `StartElementHandler` and `EndElementHandler` will be the concatenation of the namespace URI, the namespace separator character, and the local part of the name. If the namespace separator is a zero byte (`chr(0)`) then the namespace URI and the local part will be concatenated without any separator.
For example, if _namespace_separator_ is set to a space character (`' '`) and the following document is parsed:
```
<?xml version="1.0"?>
<root xmlns    = "http://default-namespace.org/"
      xmlns:py = "http://www.python.org/ns/">
  <py:elem1 />
  <elem2 xmlns="" />
</root>

```

`StartElementHandler` will receive the following strings for each element:
Copy```
http://default-namespace.org/ root
http://www.python.org/ns/ elem1
elem2

```

Due to limitations in the `Expat` library used by `pyexpat`, the `xmlparser` instance returned can only be used to parse a single XML document. Call `ParserCreate` for each document to provide unique parser instances.
See also
Home page of the Expat project.
## XMLParser Objects[¶](https://docs.python.org/3/library/pyexpat.html#xmlparser-objects "Link to this heading")
`xmlparser` objects have the following methods:

xmlparser.Parse(_data_[, _isfinal_])[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.Parse "Link to this definition")

Parses the contents of the string _data_ , calling the appropriate handler functions to process the parsed data. _isfinal_ must be true on the final call to this method; it allows the parsing of a single file in fragments, not the submission of multiple files. _data_ can be the empty string at any time.

xmlparser.ParseFile(_file_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ParseFile "Link to this definition")

Parse XML data reading from the object _file_. _file_ only needs to provide the `read(nbytes)` method, returning the empty string when there’s no more data.

xmlparser.SetBase(_base_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBase "Link to this definition")

Sets the base to be used for resolving relative URIs in system identifiers in declarations. Resolving relative identifiers is left to the application: this value will be passed through as the _base_ argument to the [`ExternalEntityRefHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler"), [`NotationDeclHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.NotationDeclHandler "xml.parsers.expat.xmlparser.NotationDeclHandler"), and [`UnparsedEntityDeclHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler "xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler") functions.

xmlparser.GetBase()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetBase "Link to this definition")

Returns a string containing the base set by a previous call to [`SetBase()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase"), or `None` if `SetBase()` hasn’t been called.

xmlparser.GetInputContext()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetInputContext "Link to this definition")

Returns the input data that generated the current event as a string. The data is in the encoding of the entity which contains the text. When called while an event handler is not active, the return value is `None`.

xmlparser.ExternalEntityParserCreate(_context_[, _encoding_])[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityParserCreate "Link to this definition")

Create a “child” parser which can be used to parse an external parsed entity referred to by content parsed by the parent parser. The _context_ parameter should be the string passed to the [`ExternalEntityRefHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler") handler function, described below. The child parser is created with the [`ordered_attributes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes") and [`specified_attributes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.specified_attributes "xml.parsers.expat.xmlparser.specified_attributes") set to the values of this parser.

xmlparser.SetParamEntityParsing(_flag_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetParamEntityParsing "Link to this definition")

Control parsing of parameter entities (including the external DTD subset). Possible _flag_ values are `XML_PARAM_ENTITY_PARSING_NEVER`, `XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE` and `XML_PARAM_ENTITY_PARSING_ALWAYS`. Return true if setting the flag was successful.

xmlparser.UseForeignDTD([_flag_])[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.UseForeignDTD "Link to this definition")

Calling this with a true value for _flag_ (the default) will cause Expat to call the [`ExternalEntityRefHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler") with [`None`](https://docs.python.org/3/library/constants.html#None "None") for all arguments to allow an alternate DTD to be loaded. If the document does not contain a document type declaration, the `ExternalEntityRefHandler` will still be called, but the [`StartDoctypeDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartDoctypeDeclHandler "xml.parsers.expat.xmlparser.StartDoctypeDeclHandler") and [`EndDoctypeDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndDoctypeDeclHandler "xml.parsers.expat.xmlparser.EndDoctypeDeclHandler") will not be called.
Passing a false value for _flag_ will cancel a previous call that passed a true value, but otherwise has no effect.
This method can only be called before the [`Parse()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.Parse "xml.parsers.expat.xmlparser.Parse") or [`ParseFile()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ParseFile "xml.parsers.expat.xmlparser.ParseFile") methods are called; calling it after either of those have been called causes [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") to be raised with the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") attribute set to `errors.codes[errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING]`.

xmlparser.SetReparseDeferralEnabled(_enabled_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "Link to this definition")

Warning
Calling `SetReparseDeferralEnabled(False)` has security implications, as detailed below; please make sure to understand these consequences prior to using the `SetReparseDeferralEnabled` method.
Expat 2.6.0 introduced a security mechanism called “reparse deferral” where instead of causing denial of service through quadratic runtime from reparsing large tokens, reparsing of unfinished tokens is now delayed by default until a sufficient amount of input is reached. Due to this delay, registered handlers may — depending of the sizing of input chunks pushed to Expat — no longer be called right after pushing new input to the parser. Where immediate feedback and taking over responsibility of protecting against denial of service from large tokens are both wanted, calling `SetReparseDeferralEnabled(False)` disables reparse deferral for the current Expat parser instance, temporarily or altogether. Calling `SetReparseDeferralEnabled(True)` allows re-enabling reparse deferral.
Note that `SetReparseDeferralEnabled()` has been backported to some prior releases of CPython as a security fix. Check for availability of `SetReparseDeferralEnabled()` using [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") if used in code running across a variety of Python versions.
Added in version 3.13.

xmlparser.GetReparseDeferralEnabled()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled "Link to this definition")

Returns whether reparse deferral is currently enabled for the given Expat parser instance.
Added in version 3.13.
`xmlparser` objects have the following methods to mitigate some common XML vulnerabilities.

xmlparser.SetAllocTrackerActivationThreshold(_threshold_ , _/_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "Link to this definition")

Sets the number of allocated bytes of dynamic memory needed to activate protection against disproportionate use of RAM.
By default, parser objects have an allocation activation threshold of 64 MiB, or equivalently 67,108,864 bytes.
An [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") is raised if this method is called on a [non-root](https://docs.python.org/3/library/pyexpat.html#xmlparser-non-root) parser. The corresponding [`lineno`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno") and [`offset`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset") should not be used as they may have no special meaning.
Added in version 3.14.1.

xmlparser.SetAllocTrackerMaximumAmplification(_max_factor_ , _/_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerMaximumAmplification "Link to this definition")

Sets the maximum amplification factor between direct input and bytes of dynamic memory allocated.
The amplification factor is calculated as `allocated / direct` while parsing, where `direct` is the number of bytes read from the primary document in parsing and `allocated` is the number of bytes of dynamic memory allocated in the parser hierarchy.
The _max_factor_ value must be a non-NaN [`float`](https://docs.python.org/3/library/functions.html#float "float") value greater than or equal to 1.0. Amplification factors greater than 100.0 can be observed near the start of parsing even with benign files in practice. In particular, the activation threshold should be carefully chosen to avoid false positives.
By default, parser objects have a maximum amplification factor of 100.0.
An [`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") is raised if this method is called on a [non-root](https://docs.python.org/3/library/pyexpat.html#xmlparser-non-root) parser or if _max_factor_ is outside the valid range. The corresponding [`lineno`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno") and [`offset`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset") should not be used as they may have no special meaning.
Note
The maximum amplification factor is only considered if the threshold that can be adjusted by [`SetAllocTrackerActivationThreshold()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold") is exceeded.
Added in version 3.14.1.
`xmlparser` objects have the following attributes:

xmlparser.buffer_size[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_size "Link to this definition")

The size of the buffer used when [`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") is true. A new buffer size can be set by assigning a new integer value to this attribute. When the size is changed, the buffer will be flushed.

xmlparser.buffer_text[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "Link to this definition")

Setting this to true causes the `xmlparser` object to buffer textual content returned by Expat to avoid multiple calls to the [`CharacterDataHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CharacterDataHandler "xml.parsers.expat.xmlparser.CharacterDataHandler") callback whenever possible. This can improve performance substantially since Expat normally breaks character data into chunks at every line ending. This attribute is false by default, and may be changed at any time. Note that when it is false, data that does not contain newlines may be chunked too.

xmlparser.buffer_used[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_used "Link to this definition")

If [`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") is enabled, the number of bytes stored in the buffer. These bytes represent UTF-8 encoded text. This attribute has no meaningful interpretation when `buffer_text` is false.

xmlparser.ordered_attributes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ordered_attributes "Link to this definition")

Setting this attribute to a non-zero integer causes the attributes to be reported as a list rather than a dictionary. The attributes are presented in the order found in the document text. For each attribute, two list entries are presented: the attribute name and the attribute value. (Older versions of this module also used this format.) By default, this attribute is false; it may be changed at any time.

xmlparser.specified_attributes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.specified_attributes "Link to this definition")

If set to a non-zero integer, the parser will report only those attributes which were specified in the document instance and not those which were derived from attribute declarations. Applications which set this need to be especially careful to use what additional information is available from the declarations as needed to comply with the standards for the behavior of XML processors. By default, this attribute is false; it may be changed at any time.
The following attributes contain values relating to the most recent error encountered by an `xmlparser` object, and will only have correct values once a call to `Parse()` or `ParseFile()` has raised an [`xml.parsers.expat.ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") exception.

xmlparser.ErrorByteIndex[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorByteIndex "Link to this definition")

Byte index at which an error occurred.

xmlparser.ErrorCode[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorCode "Link to this definition")

Numeric code specifying the problem. This value can be passed to the [`ErrorString()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ErrorString "xml.parsers.expat.ErrorString") function, or compared to one of the constants defined in the `errors` object.

xmlparser.ErrorColumnNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorColumnNumber "Link to this definition")

Column number at which an error occurred.

xmlparser.ErrorLineNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ErrorLineNumber "Link to this definition")

Line number at which an error occurred.
The following attributes contain values relating to the current parse location in an `xmlparser` object. During a callback reporting a parse event they indicate the location of the first of the sequence of characters that generated the event. When called outside of a callback, the position indicated will be just past the last parse event (regardless of whether there was an associated callback).

xmlparser.CurrentByteIndex[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CurrentByteIndex "Link to this definition")

Current byte index in the parser input.

xmlparser.CurrentColumnNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CurrentColumnNumber "Link to this definition")

Current column number in the parser input.

xmlparser.CurrentLineNumber[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CurrentLineNumber "Link to this definition")

Current line number in the parser input.
Here is the list of handlers that can be set. To set a handler on an `xmlparser` object _o_ , use `o.handlername = func`. _handlername_ must be taken from the following list, and _func_ must be a callable object accepting the correct number of arguments. The arguments are all strings, unless otherwise stated.

xmlparser.XmlDeclHandler(_version_ , _encoding_ , _standalone_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.XmlDeclHandler "Link to this definition")

Called when the XML declaration is parsed. The XML declaration is the (optional) declaration of the applicable version of the XML recommendation, the encoding of the document text, and an optional “standalone” declaration. _version_ and _encoding_ will be strings, and _standalone_ will be `1` if the document is declared standalone, `0` if it is declared not to be standalone, or `-1` if the standalone clause was omitted. This is only available with Expat version 1.95.0 or newer.

xmlparser.StartDoctypeDeclHandler(_doctypeName_ , _systemId_ , _publicId_ , _has_internal_subset_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartDoctypeDeclHandler "Link to this definition")

Called when Expat begins parsing the document type declaration (`<!DOCTYPE ...`). The _doctypeName_ is provided exactly as presented. The _systemId_ and _publicId_ parameters give the system and public identifiers if specified, or `None` if omitted. _has_internal_subset_ will be true if the document contains an internal document declaration subset. This requires Expat version 1.2 or newer.

xmlparser.EndDoctypeDeclHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndDoctypeDeclHandler "Link to this definition")

Called when Expat is done parsing the document type declaration. This requires Expat version 1.2 or newer.

xmlparser.ElementDeclHandler(_name_ , _model_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ElementDeclHandler "Link to this definition")

Called once for each element type declaration. _name_ is the name of the element type, and _model_ is a representation of the content model.

xmlparser.AttlistDeclHandler(_elname_ , _attname_ , _type_ , _default_ , _required_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.AttlistDeclHandler "Link to this definition")

Called for each declared attribute for an element type. If an attribute list declaration declares three attributes, this handler is called three times, once for each attribute. _elname_ is the name of the element to which the declaration applies and _attname_ is the name of the attribute declared. The attribute type is a string passed as _type_ ; the possible values are `'CDATA'`, `'ID'`, `'IDREF'`, … _default_ gives the default value for the attribute used when the attribute is not specified by the document instance, or `None` if there is no default value (`#IMPLIED` values). If the attribute is required to be given in the document instance, _required_ will be true. This requires Expat version 1.95.0 or newer.

xmlparser.StartElementHandler(_name_ , _attributes_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartElementHandler "Link to this definition")

Called for the start of every element. _name_ is a string containing the element name, and _attributes_ is the element attributes. If [`ordered_attributes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes") is true, this is a list (see `ordered_attributes` for a full description). Otherwise it’s a dictionary mapping names to values.

xmlparser.EndElementHandler(_name_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndElementHandler "Link to this definition")

Called for the end of every element.

xmlparser.ProcessingInstructionHandler(_target_ , _data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ProcessingInstructionHandler "Link to this definition")

Called for every processing instruction.

xmlparser.CharacterDataHandler(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CharacterDataHandler "Link to this definition")

Called for character data. This will be called for normal character data, CDATA marked content, and ignorable whitespace. Applications which must distinguish these cases can use the [`StartCdataSectionHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartCdataSectionHandler "xml.parsers.expat.xmlparser.StartCdataSectionHandler"), [`EndCdataSectionHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndCdataSectionHandler "xml.parsers.expat.xmlparser.EndCdataSectionHandler"), and [`ElementDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ElementDeclHandler "xml.parsers.expat.xmlparser.ElementDeclHandler") callbacks to collect the required information. Note that the character data may be chunked even if it is short and so you may receive more than one call to `CharacterDataHandler()`. Set the [`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") instance attribute to `True` to avoid that.

xmlparser.UnparsedEntityDeclHandler(_entityName_ , _base_ , _systemId_ , _publicId_ , _notationName_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler "Link to this definition")

Called for unparsed (NDATA) entity declarations. This is only present for version 1.2 of the Expat library; for more recent versions, use [`EntityDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EntityDeclHandler "xml.parsers.expat.xmlparser.EntityDeclHandler") instead. (The underlying function in the Expat library has been declared obsolete.)

xmlparser.EntityDeclHandler(_entityName_ , _is_parameter_entity_ , _value_ , _base_ , _systemId_ , _publicId_ , _notationName_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EntityDeclHandler "Link to this definition")

Called for all entity declarations. For parameter and internal entities, _value_ will be a string giving the declared contents of the entity; this will be `None` for external entities. The _notationName_ parameter will be `None` for parsed entities, and the name of the notation for unparsed entities. _is_parameter_entity_ will be true if the entity is a parameter entity or false for general entities (most applications only need to be concerned with general entities). This is only available starting with version 1.95.0 of the Expat library.

xmlparser.NotationDeclHandler(_notationName_ , _base_ , _systemId_ , _publicId_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.NotationDeclHandler "Link to this definition")

Called for notation declarations. _notationName_ , _base_ , and _systemId_ , and _publicId_ are strings if given. If the public identifier is omitted, _publicId_ will be `None`.

xmlparser.StartNamespaceDeclHandler(_prefix_ , _uri_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartNamespaceDeclHandler "Link to this definition")

Called when an element contains a namespace declaration. Namespace declarations are processed before the [`StartElementHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartElementHandler "xml.parsers.expat.xmlparser.StartElementHandler") is called for the element on which declarations are placed.

xmlparser.EndNamespaceDeclHandler(_prefix_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndNamespaceDeclHandler "Link to this definition")

Called when the closing tag is reached for an element that contained a namespace declaration. This is called once for each namespace declaration on the element in the reverse of the order for which the [`StartNamespaceDeclHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartNamespaceDeclHandler "xml.parsers.expat.xmlparser.StartNamespaceDeclHandler") was called to indicate the start of each namespace declaration’s scope. Calls to this handler are made after the corresponding [`EndElementHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndElementHandler "xml.parsers.expat.xmlparser.EndElementHandler") for the end of the element.

xmlparser.CommentHandler(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.CommentHandler "Link to this definition")

Called for comments. _data_ is the text of the comment, excluding the leading `'<!-``-'` and trailing `'-``->'`.

xmlparser.StartCdataSectionHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.StartCdataSectionHandler "Link to this definition")

Called at the start of a CDATA section. This and [`EndCdataSectionHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndCdataSectionHandler "xml.parsers.expat.xmlparser.EndCdataSectionHandler") are needed to be able to identify the syntactical start and end for CDATA sections.

xmlparser.EndCdataSectionHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.EndCdataSectionHandler "Link to this definition")

Called at the end of a CDATA section.

xmlparser.DefaultHandler(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandler "Link to this definition")

Called for any characters in the XML document for which no applicable handler has been specified. This means characters that are part of a construct which could be reported, but for which no handler has been supplied.

xmlparser.DefaultHandlerExpand(_data_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandlerExpand "Link to this definition")

This is the same as the [`DefaultHandler()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandler "xml.parsers.expat.xmlparser.DefaultHandler"), but doesn’t inhibit expansion of internal entities. The entity reference will not be passed to the default handler.

xmlparser.NotStandaloneHandler()[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.NotStandaloneHandler "Link to this definition")

Called if the XML document hasn’t been declared as being a standalone document. This happens when there is an external subset or a reference to a parameter entity, but the XML declaration does not set standalone to `yes` in an XML declaration. If this handler returns `0`, then the parser will raise an `XML_ERROR_NOT_STANDALONE` error. If this handler is not set, no exception is raised by the parser for this condition.

xmlparser.ExternalEntityRefHandler(_context_ , _base_ , _systemId_ , _publicId_)[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "Link to this definition")

Warning
Implementing a handler that accesses local files and/or the network may create a vulnerability to `xmlparser` is used with user-provided XML content. Please reflect on your
Called for references to external entities. _base_ is the current base, as set by a previous call to [`SetBase()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase"). The public and system identifiers, _systemId_ and _publicId_ , are strings if given; if the public identifier is not given, _publicId_ will be `None`. The _context_ value is opaque and should only be used as described below.
For external entities to be parsed, this handler must be implemented. It is responsible for creating the sub-parser using `ExternalEntityParserCreate(context)`, initializing it with the appropriate callbacks, and parsing the entity. This handler should return an integer; if it returns `0`, the parser will raise an `XML_ERROR_EXTERNAL_ENTITY_HANDLING` error, otherwise parsing will continue.
If this handler is not provided, external entities are reported by the [`DefaultHandler`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.DefaultHandler "xml.parsers.expat.xmlparser.DefaultHandler") callback, if provided.
## ExpatError Exceptions[¶](https://docs.python.org/3/library/pyexpat.html#expaterror-exceptions "Link to this heading")
[`ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") exceptions have a number of interesting attributes:

ExpatError.code[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.code "Link to this definition")

Expat’s internal error number for the specific error. The [`errors.messages`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.messages "xml.parsers.expat.errors.messages") dictionary maps these error numbers to Expat’s error messages. For example:
Copy```
from xml.parsers.expat import ParserCreate, ExpatError, errors

p = ParserCreate()
try:
    p.Parse(some_xml_document)
except ExpatError as err:
    print("Error:", errors.messages[err.code])

```

The [`errors`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.errors "xml.parsers.expat.errors") module also provides error message constants and a dictionary [`codes`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.codes "xml.parsers.expat.errors.codes") mapping these messages back to the error codes, see below.

ExpatError.lineno[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.lineno "Link to this definition")

Line number on which the error was detected. The first line is numbered `1`.

ExpatError.offset[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError.offset "Link to this definition")

Character offset into the line where the error occurred. The first column is numbered `0`.
## Example[¶](https://docs.python.org/3/library/pyexpat.html#example "Link to this heading")
The following program defines three handlers that just print out their arguments.
Copy```
import xml.parsers.expat
