# 3 handler functions
def start_element(name, attrs):
    print('Start element:', name, attrs)
def end_element(name):
    print('End element:', name)
def char_data(data):
    print('Character data:', repr(data))

p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

p.Parse("""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>""", 1)

```

The output from this program is:
Copy```
Start element: parent {'id': 'top'}
Start element: child1 {'name': 'paul'}
Character data: 'Text goes here'
End element: child1
Character data: '\n'
Start element: child2 {'name': 'fred'}
Character data: 'More text'
End element: child2
Character data: '\n'
End element: parent

```

## Content Model Descriptions[¶](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.model "Link to this heading")
Content models are described using nested tuples. Each tuple contains four values: the type, the quantifier, the name, and a tuple of children. Children are simply additional content model descriptions.
The values of the first two fields are constants defined in the `xml.parsers.expat.model` module. These constants can be collected in two groups: the model type group and the quantifier group.
The constants in the model type group are:

xml.parsers.expat.model.XML_CTYPE_ANY

The element named by the model name was declared to have a content model of `ANY`.

xml.parsers.expat.model.XML_CTYPE_CHOICE

The named element allows a choice from a number of options; this is used for content models such as `(A | B | C)`.

xml.parsers.expat.model.XML_CTYPE_EMPTY

Elements which are declared to be `EMPTY` have this model type.

xml.parsers.expat.model.XML_CTYPE_MIXED


xml.parsers.expat.model.XML_CTYPE_NAME


xml.parsers.expat.model.XML_CTYPE_SEQ

Models which represent a series of models which follow one after the other are indicated with this model type. This is used for models such as `(A, B, C)`.
The constants in the quantifier group are:

xml.parsers.expat.model.XML_CQUANT_NONE

No modifier is given, so it can appear exactly once, as for `A`.

xml.parsers.expat.model.XML_CQUANT_OPT

The model is optional: it can appear once or not at all, as for `A?`.

xml.parsers.expat.model.XML_CQUANT_PLUS

The model must occur one or more times (like `A+`).

xml.parsers.expat.model.XML_CQUANT_REP

The model must occur zero or more times, as for `A*`.
## Expat error constants[¶](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.errors "Link to this heading")
The following constants are provided in the `xml.parsers.expat.errors` module. These constants are useful in interpreting some of the attributes of the `ExpatError` exception objects raised when an error has occurred. Since for backwards compatibility reasons, the constants’ value is the error _message_ and not the numeric error _code_ , you do this by comparing its [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") attribute with `errors.codes[errors.XML_ERROR__CONSTANT_NAME_]`.
The `errors` module has the following attributes:

xml.parsers.expat.errors.codes[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.codes "Link to this definition")

A dictionary mapping string descriptions to their error codes.
Added in version 3.2.

xml.parsers.expat.errors.messages[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.messages "Link to this definition")

A dictionary mapping numeric error codes to their string descriptions.
Added in version 3.2.

xml.parsers.expat.errors.XML_ERROR_ASYNC_ENTITY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ASYNC_ENTITY "Link to this definition")


xml.parsers.expat.errors.XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF "Link to this definition")

An entity reference in an attribute value referred to an external entity instead of an internal entity.

xml.parsers.expat.errors.XML_ERROR_BAD_CHAR_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_BAD_CHAR_REF "Link to this definition")

A character reference referred to a character which is illegal in XML (for example, character `0`, or ‘`&#0;`’).

xml.parsers.expat.errors.XML_ERROR_BINARY_ENTITY_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_BINARY_ENTITY_REF "Link to this definition")

An entity reference referred to an entity which was declared with a notation, so cannot be parsed.

xml.parsers.expat.errors.XML_ERROR_DUPLICATE_ATTRIBUTE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_DUPLICATE_ATTRIBUTE "Link to this definition")

An attribute was used more than once in a start tag.

xml.parsers.expat.errors.XML_ERROR_INCORRECT_ENCODING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INCORRECT_ENCODING "Link to this definition")


xml.parsers.expat.errors.XML_ERROR_INVALID_TOKEN[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INVALID_TOKEN "Link to this definition")

Raised when an input byte could not properly be assigned to a character; for example, a NUL byte (value `0`) in a UTF-8 input stream.

xml.parsers.expat.errors.XML_ERROR_JUNK_AFTER_DOC_ELEMENT[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_JUNK_AFTER_DOC_ELEMENT "Link to this definition")

Something other than whitespace occurred after the document element.

xml.parsers.expat.errors.XML_ERROR_MISPLACED_XML_PI[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_MISPLACED_XML_PI "Link to this definition")

An XML declaration was found somewhere other than the start of the input data.

xml.parsers.expat.errors.XML_ERROR_NO_ELEMENTS[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NO_ELEMENTS "Link to this definition")

The document contains no elements (XML requires all documents to contain exactly one top-level element)..

xml.parsers.expat.errors.XML_ERROR_NO_MEMORY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NO_MEMORY "Link to this definition")

Expat was not able to allocate memory internally.

xml.parsers.expat.errors.XML_ERROR_PARAM_ENTITY_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_PARAM_ENTITY_REF "Link to this definition")

A parameter entity reference was found where it was not allowed.

xml.parsers.expat.errors.XML_ERROR_PARTIAL_CHAR[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_PARTIAL_CHAR "Link to this definition")

An incomplete character was found in the input.

xml.parsers.expat.errors.XML_ERROR_RECURSIVE_ENTITY_REF[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RECURSIVE_ENTITY_REF "Link to this definition")

An entity reference contained another reference to the same entity; possibly via a different name, and possibly indirectly.

xml.parsers.expat.errors.XML_ERROR_SYNTAX[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_SYNTAX "Link to this definition")

Some unspecified syntax error was encountered.

xml.parsers.expat.errors.XML_ERROR_TAG_MISMATCH[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_TAG_MISMATCH "Link to this definition")

An end tag did not match the innermost open start tag.

xml.parsers.expat.errors.XML_ERROR_UNCLOSED_TOKEN[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNCLOSED_TOKEN "Link to this definition")

Some token (such as a start tag) was not closed before the end of the stream or the next token was encountered.

xml.parsers.expat.errors.XML_ERROR_UNDEFINED_ENTITY[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNDEFINED_ENTITY "Link to this definition")

A reference was made to an entity which was not defined.

xml.parsers.expat.errors.XML_ERROR_UNKNOWN_ENCODING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNKNOWN_ENCODING "Link to this definition")

The document encoding is not supported by Expat.

xml.parsers.expat.errors.XML_ERROR_UNCLOSED_CDATA_SECTION[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNCLOSED_CDATA_SECTION "Link to this definition")

A CDATA marked section was not closed.

xml.parsers.expat.errors.XML_ERROR_EXTERNAL_ENTITY_HANDLING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_EXTERNAL_ENTITY_HANDLING "Link to this definition")


xml.parsers.expat.errors.XML_ERROR_NOT_STANDALONE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NOT_STANDALONE "Link to this definition")

The parser determined that the document was not “standalone” though it declared itself to be in the XML declaration, and the `NotStandaloneHandler` was set and returned `0`.

xml.parsers.expat.errors.XML_ERROR_UNEXPECTED_STATE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNEXPECTED_STATE "Link to this definition")


xml.parsers.expat.errors.XML_ERROR_ENTITY_DECLARED_IN_PE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ENTITY_DECLARED_IN_PE "Link to this definition")


xml.parsers.expat.errors.XML_ERROR_FEATURE_REQUIRES_XML_DTD[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_FEATURE_REQUIRES_XML_DTD "Link to this definition")

An operation was requested that requires DTD support to be compiled in, but Expat was configured without DTD support. This should never be reported by a standard build of the `xml.parsers.expat` module.

xml.parsers.expat.errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING "Link to this definition")

A behavioral change was requested after parsing started that can only be changed before parsing has started. This is (currently) only raised by `UseForeignDTD()`.

xml.parsers.expat.errors.XML_ERROR_UNBOUND_PREFIX[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNBOUND_PREFIX "Link to this definition")

An undeclared prefix was found when namespace processing was enabled.

xml.parsers.expat.errors.XML_ERROR_UNDECLARING_PREFIX[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_UNDECLARING_PREFIX "Link to this definition")

The document attempted to remove the namespace declaration associated with a prefix.

xml.parsers.expat.errors.XML_ERROR_INCOMPLETE_PE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INCOMPLETE_PE "Link to this definition")

A parameter entity contained incomplete markup.

xml.parsers.expat.errors.XML_ERROR_XML_DECL[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_XML_DECL "Link to this definition")

The document contained no document element at all.

xml.parsers.expat.errors.XML_ERROR_TEXT_DECL[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_TEXT_DECL "Link to this definition")

There was an error parsing a text declaration in an external entity.

xml.parsers.expat.errors.XML_ERROR_PUBLICID[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_PUBLICID "Link to this definition")

Characters were found in the public id that are not allowed.

xml.parsers.expat.errors.XML_ERROR_SUSPENDED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_SUSPENDED "Link to this definition")

The requested operation was made on a suspended parser, but isn’t allowed. This includes attempts to provide additional input or to stop the parser.

xml.parsers.expat.errors.XML_ERROR_NOT_SUSPENDED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NOT_SUSPENDED "Link to this definition")

An attempt to resume the parser was made when the parser had not been suspended.

xml.parsers.expat.errors.XML_ERROR_ABORTED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_ABORTED "Link to this definition")

This should not be reported to Python applications.

xml.parsers.expat.errors.XML_ERROR_FINISHED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_FINISHED "Link to this definition")

The requested operation was made on a parser which was finished parsing input, but isn’t allowed. This includes attempts to provide additional input or to stop the parser.

xml.parsers.expat.errors.XML_ERROR_SUSPEND_PE[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_SUSPEND_PE "Link to this definition")


xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XML[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XML "Link to this definition")

An attempt was made to undeclare reserved namespace prefix `xml` or to bind it to another namespace URI.

xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XMLNS[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XMLNS "Link to this definition")

An attempt was made to declare or undeclare reserved namespace prefix `xmlns`.

xml.parsers.expat.errors.XML_ERROR_RESERVED_NAMESPACE_URI[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_RESERVED_NAMESPACE_URI "Link to this definition")

An attempt was made to bind the URI of one the reserved namespace prefixes `xml` and `xmlns` to another namespace prefix.

xml.parsers.expat.errors.XML_ERROR_INVALID_ARGUMENT[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_INVALID_ARGUMENT "Link to this definition")

This should not be reported to Python applications.

xml.parsers.expat.errors.XML_ERROR_NO_BUFFER[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NO_BUFFER "Link to this definition")

This should not be reported to Python applications.

xml.parsers.expat.errors.XML_ERROR_AMPLIFICATION_LIMIT_BREACH[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_AMPLIFICATION_LIMIT_BREACH "Link to this definition")

The limit on input amplification factor (from DTD and entities) has been breached.

xml.parsers.expat.errors.XML_ERROR_NOT_STARTED[¶](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.errors.XML_ERROR_NOT_STARTED "Link to this definition")

The parser was tried to be stopped or suspended before it started.
Added in version 3.14.
Footnotes
[[1](https://docs.python.org/3/library/pyexpat.html#id1)]
The encoding string included in XML output should conform to the appropriate standards. For example, “UTF-8” is valid, but “UTF8” is not. See
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html)
    * [XMLParser Objects](https://docs.python.org/3/library/pyexpat.html#xmlparser-objects)
    * [ExpatError Exceptions](https://docs.python.org/3/library/pyexpat.html#expaterror-exceptions)
    * [Example](https://docs.python.org/3/library/pyexpat.html#example)
    * [Content Model Descriptions](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.model)
    * [Expat error constants](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat.errors)


#### Previous topic
[`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html "previous chapter")
#### Next topic
[Internet Protocols and Support](https://docs.python.org/3/library/internet.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.parsers.expat+%E2%80%94+Fast+XML+parsing+using+Expat&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpyexpat.html&pagesource=library%2Fpyexpat.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/internet.html "Internet Protocols and Support") |
  * [previous](https://docs.python.org/3/library/xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
