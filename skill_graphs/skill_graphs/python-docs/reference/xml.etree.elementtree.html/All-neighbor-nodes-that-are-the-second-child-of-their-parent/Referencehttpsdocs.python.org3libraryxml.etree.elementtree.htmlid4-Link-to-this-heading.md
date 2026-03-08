## Reference[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#id4 "Link to this heading")
### Functions[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#elementinclude-functions "Link to this heading")

xml.etree.ElementInclude.default_loader(_href_ , _parse_ , _encoding =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementInclude.default_loader "Link to this definition")

Default loader. This default loader reads an included resource from disk. _href_ is a URL. _parse_ is for parse mode either “xml” or “text”. _encoding_ is an optional text encoding. If not given, encoding is `utf-8`. Returns the expanded resource. If the parse mode is `"xml"`, this is an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance. If the parse mode is `"text"`, this is a string. If the loader fails, it can return `None` or raise an exception.

xml.etree.ElementInclude.include(_elem_ , _loader =None_, _base_url =None_, _max_depth =6_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementInclude.include "Link to this definition")

This function expands XInclude directives in-place in tree pointed by _elem_. _elem_ is either the root [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") or an [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") instance to find such element. _loader_ is an optional resource loader. If omitted, it defaults to [`default_loader()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementInclude.default_loader "xml.etree.ElementInclude.default_loader"). If given, it should be a callable that implements the same interface as `default_loader()`. _base_url_ is base URL of the original file, to resolve relative include file references. _max_depth_ is the maximum number of recursive inclusions. Limited to reduce the risk of malicious content explosion. Pass `None` to disable the limitation.
Changed in version 3.9: Added the _base_url_ and _max_depth_ parameters.
### Element Objects[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#element-objects "Link to this heading")

_class_ xml.etree.ElementTree.Element(_tag_ , _attrib ={}_, _** extra_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "Link to this definition")

Element class. This class defines the Element interface, and provides a reference implementation of this interface.
The element name, attribute names, and attribute values can be either bytestrings or Unicode strings. _tag_ is the element name. _attrib_ is an optional dictionary, containing element attributes. _extra_ contains additional attributes, given as keyword arguments.

tag[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.tag "Link to this definition")

A string identifying what kind of data this element represents (the element type, in other words).

text[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.text "Link to this definition")


tail[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.tail "Link to this definition")

These attributes can be used to hold additional data associated with the element. Their values are usually strings but may be any application-specific object. If the element is created from an XML file, the _text_ attribute holds either the text between the element’s start tag and its first child or end tag, or `None`, and the _tail_ attribute holds either the text between the element’s end tag and the next tag, or `None`. For the XML data
```
<a><b>1<c>2<d/>3</c></b>4</a>

```

the _a_ element has `None` for both _text_ and _tail_ attributes, the _b_ element has _text_ `"1"` and _tail_ `"4"`, the _c_ element has _text_ `"2"` and _tail_ `None`, and the _d_ element has _text_ `None` and _tail_ `"3"`.
To collect the inner text of an element, see [`itertext()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.itertext "xml.etree.ElementTree.Element.itertext"), for example `"".join(element.itertext())`.
Applications may store arbitrary objects in these attributes.

attrib[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.attrib "Link to this definition")

A dictionary containing the element’s attributes. Note that while the _attrib_ value is always a real mutable Python dictionary, an ElementTree implementation may choose to use another internal representation, and create the dictionary only if someone asks for it. To take advantage of such implementations, use the dictionary methods below whenever possible.
The following dictionary-like methods work on the element attributes.

clear()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.clear "Link to this definition")

Resets an element. This function removes all subelements, clears all attributes, and sets the text and tail attributes to `None`.

get(_key_ , _default =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.get "Link to this definition")

Gets the element attribute named _key_.
Returns the attribute value, or _default_ if the attribute was not found.

items()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.items "Link to this definition")

Returns the element attributes as a sequence of (name, value) pairs. The attributes are returned in an arbitrary order.

keys()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.keys "Link to this definition")

Returns the elements attribute names as a list. The names are returned in an arbitrary order.

set(_key_ , _value_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.set "Link to this definition")

Set the attribute _key_ on the element to _value_.
The following methods work on the element’s children (subelements).

append(_subelement_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.append "Link to this definition")

Adds the element _subelement_ to the end of this element’s internal list of subelements. Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _subelement_ is not an `Element`.

extend(_subelements_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.extend "Link to this definition")

Appends _subelements_ from an iterable of elements. Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if a subelement is not an `Element`.
Added in version 3.2.

find(_match_ , _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.find "Link to this definition")

Finds the first subelement matching _match_. _match_ may be a tag name or a [path](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath). Returns an element instance or `None`. _namespaces_ is an optional mapping from namespace prefix to full name. Pass `''` as prefix to move all unprefixed tag names in the expression into the given namespace.

findall(_match_ , _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findall "Link to this definition")

Finds all matching subelements, by tag name or [path](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath). Returns a list containing all matching elements in document order. _namespaces_ is an optional mapping from namespace prefix to full name. Pass `''` as prefix to move all unprefixed tag names in the expression into the given namespace.

findtext(_match_ , _default =None_, _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findtext "Link to this definition")

Finds text for the first subelement matching _match_. _match_ may be a tag name or a [path](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath). Returns the text content of the first matching element, or _default_ if no element was found. Note that if the matching element has no text content an empty string is returned. _namespaces_ is an optional mapping from namespace prefix to full name. Pass `''` as prefix to move all unprefixed tag names in the expression into the given namespace.

insert(_index_ , _subelement_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.insert "Link to this definition")

Inserts _subelement_ at the given position in this element. Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _subelement_ is not an `Element`.

iter(_tag =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iter "Link to this definition")

Creates a tree [iterator](https://docs.python.org/3/glossary.html#term-iterator) with the current element as the root. The iterator iterates over this element and all elements below it, in document (depth first) order. If _tag_ is not `None` or `'*'`, only elements whose tag equals _tag_ are returned from the iterator. If the tree structure is modified during iteration, the result is undefined.
Added in version 3.2.

iterfind(_match_ , _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iterfind "Link to this definition")

Finds all matching subelements, by tag name or [path](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath). Returns an iterable yielding all matching elements in document order. _namespaces_ is an optional mapping from namespace prefix to full name.
Added in version 3.2.

itertext()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.itertext "Link to this definition")

Creates a text iterator. The iterator loops over this element and all subelements, in document order, and returns all inner text.
Added in version 3.2.

makeelement(_tag_ , _attrib_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.makeelement "Link to this definition")

Creates a new element object of the same type as this element. Do not call this method, use the [`SubElement()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.SubElement "xml.etree.ElementTree.SubElement") factory function instead.

remove(_subelement_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.remove "Link to this definition")

Removes _subelement_ from the element. Unlike the find* methods this method compares elements based on the instance identity, not on tag value or contents.
`Element` objects also support the following sequence type methods for working with subelements: [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__"), [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__"), [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__"), [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__").
Caution: Elements with no subelements will test as `False`. In a future release of Python, all elements will test as `True` regardless of whether subelements exist. Instead, prefer explicit `len(elem)` or `elem is not None` tests.:
Copy```
element = root.find('foo')

if not element:  # careful!
    print("element not found, or element has no subelements")

if element is None:
    print("element not found")

```

Changed in version 3.12: Testing the truth value of an Element emits [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning").
Prior to Python 3.8, the serialisation order of the XML attributes of elements was artificially made predictable by sorting the attributes by their name. Based on the now guaranteed ordering of dicts, this arbitrary reordering was removed in Python 3.8 to preserve the order in which attributes were originally parsed or created by user code.
In general, user code should try not to depend on a specific ordering of attributes, given that the [`canonicalize()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.canonicalize "xml.etree.ElementTree.canonicalize") function.
In cases where canonical output is not applicable but a specific attribute order is still desirable on output, code should aim for creating the attributes directly in the desired order, to avoid perceptual mismatches for readers of the code. In cases where this is difficult to achieve, a recipe like the following can be applied prior to serialisation to enforce an order independently from the Element creation:
Copy```
def reorder_attributes(root):
    for el in root.iter():
        attrib = el.attrib
        if len(attrib) > 1:
            # adjust attribute order, e.g. by sorting
            attribs = sorted(attrib.items())
            attrib.clear()
            attrib.update(attribs)

```

### ElementTree Objects[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-objects "Link to this heading")

_class_ xml.etree.ElementTree.ElementTree(_element =None_, _file =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "Link to this definition")

ElementTree wrapper class. This class represents an entire element hierarchy, and adds some extra support for serialization to and from standard XML.
_element_ is the root element. The tree is initialized with the contents of the XML _file_ if given.

_setroot(_element_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree._setroot "Link to this definition")

Replaces the root element for this tree. This discards the current contents of the tree, and replaces it with the given element. Use with care. _element_ is an element instance.

find(_match_ , _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.find "Link to this definition")

Same as [`Element.find()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.find "xml.etree.ElementTree.Element.find"), starting at the root of the tree.

findall(_match_ , _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.findall "Link to this definition")

Same as [`Element.findall()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findall "xml.etree.ElementTree.Element.findall"), starting at the root of the tree.

findtext(_match_ , _default =None_, _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.findtext "Link to this definition")

Same as [`Element.findtext()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findtext "xml.etree.ElementTree.Element.findtext"), starting at the root of the tree.

getroot()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.getroot "Link to this definition")

Returns the root element for this tree.

iter(_tag =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.iter "Link to this definition")

Creates and returns a tree iterator for the root element. The iterator loops over all elements in this tree, in section order. _tag_ is the tag to look for (default is to return all elements).

iterfind(_match_ , _namespaces =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.iterfind "Link to this definition")

Same as [`Element.iterfind()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iterfind "xml.etree.ElementTree.Element.iterfind"), starting at the root of the tree.
Added in version 3.2.

parse(_source_ , _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.parse "Link to this definition")

Loads an external XML section into this element tree. _source_ is a file name or [file object](https://docs.python.org/3/glossary.html#term-file-object). _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. Returns the section root element.

write(_file_ , _encoding ='us-ascii'_, _xml_declaration =None_, _default_namespace =None_, _method ='xml'_, _*_ , _short_empty_elements =True_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write "Link to this definition")

Writes the element tree to a file, as XML. _file_ is a file name, or a [file object](https://docs.python.org/3/glossary.html#term-file-object) opened for writing. _encoding_ [[1]](https://docs.python.org/3/library/xml.etree.elementtree.html#id9) is the output encoding (default is US-ASCII). _xml_declaration_ controls if an XML declaration should be added to the file. Use `False` for never, `True` for always, `None` for only if not US-ASCII or UTF-8 or Unicode (default is `None`). _default_namespace_ sets the default XML namespace (for “xmlns”). _method_ is either `"xml"`, `"html"` or `"text"` (default is `"xml"`). The keyword-only _short_empty_elements_ parameter controls the formatting of elements that contain no content. If `True` (the default), they are emitted as a single self-closed tag, otherwise they are emitted as a pair of start/end tags.
The output is either a string ([`str`](https://docs.python.org/3/library/stdtypes.html#str "str")) or binary ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")). This is controlled by the _encoding_ argument. If _encoding_ is `"unicode"`, the output is a string; otherwise, it’s binary. Note that this may conflict with the type of _file_ if it’s an open [file object](https://docs.python.org/3/glossary.html#term-file-object); make sure you do not try to write a string to a binary stream and vice versa.
Changed in version 3.4: Added the _short_empty_elements_ parameter.
Changed in version 3.8: The `write()` method now preserves the attribute order specified by the user.
This is the XML file that is going to be manipulated:
Copy```
<html>
    <head>
        <title>Example page</title>
    </head>
    <body>
        <p>Moved to <a href="http://example.org/">example.org</a>
        or <a href="http://example.com/">example.com</a>.</p>
    </body>
</html>

```

Example of changing the attribute “target” of every link in first paragraph:
Copy```
>>> from xml.etree.ElementTree import ElementTree
>>> tree = ElementTree()
>>> tree.parse("index.xhtml")
<Element 'html' at 0xb77e6fac>
>>> p = tree.find("body/p")     # Finds first occurrence of tag p in body
>>> p
<Element 'p' at 0xb77ec26c>
>>> links = list(p.iter("a"))   # Returns list of all links
>>> links
[<Element 'a' at 0xb77ec2ac>, <Element 'a' at 0xb77ec1cc>]
>>> for i in links:             # Iterates through all found links
...     i.attrib["target"] = "blank"
...
>>> tree.write("output.xhtml")

```

### QName Objects[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#qname-objects "Link to this heading")

_class_ xml.etree.ElementTree.QName(_text_or_uri_ , _tag =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.QName "Link to this definition")

QName wrapper. This can be used to wrap a QName attribute value, in order to get proper namespace handling on output. _text_or_uri_ is a string containing the QName value, in the form {uri}local, or, if the tag argument is given, the URI part of a QName. If _tag_ is given, the first argument is interpreted as a URI, and this argument is interpreted as a local name. `QName` instances are opaque.
### TreeBuilder Objects[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#treebuilder-objects "Link to this heading")

_class_ xml.etree.ElementTree.TreeBuilder(_element_factory =None_, _*_ , _comment_factory =None_, _pi_factory =None_, _insert_comments =False_, _insert_pis =False_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder "Link to this definition")

Generic element structure builder. This builder converts a sequence of start, data, end, comment and pi method calls to a well-formed element structure. You can use this class to build an element structure using a custom XML parser, or a parser for some other XML-like format.
_element_factory_ , when given, must be a callable accepting two positional arguments: a tag and a dict of attributes. It is expected to return a new element instance.
The _comment_factory_ and _pi_factory_ functions, when given, should behave like the [`Comment()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Comment "xml.etree.ElementTree.Comment") and [`ProcessingInstruction()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ProcessingInstruction "xml.etree.ElementTree.ProcessingInstruction") functions to create comments and processing instructions. When not given, the default factories will be used. When _insert_comments_ and/or _insert_pis_ is true, comments/pis will be inserted into the tree if they appear within the root element (but not outside of it).

close()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.close "Link to this definition")

Flushes the builder buffers, and returns the toplevel document element. Returns an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance.

data(_data_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.data "Link to this definition")

Adds text to the current element. _data_ is a string. This should be either a bytestring, or a Unicode string.

end(_tag_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.end "Link to this definition")

Closes the current element. _tag_ is the element name. Returns the closed element.

start(_tag_ , _attrs_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.start "Link to this definition")

Opens a new element. _tag_ is the element name. _attrs_ is a dictionary containing element attributes. Returns the opened element.

comment(_text_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.comment "Link to this definition")

Creates a comment with the given _text_. If `insert_comments` is true, this will also add it to the tree.
Added in version 3.8.

pi(_target_ , _text_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.pi "Link to this definition")

Creates a process instruction with the given _target_ name and _text_. If `insert_pis` is true, this will also add it to the tree.
Added in version 3.8.
In addition, a custom `TreeBuilder` object can provide the following methods:

doctype(_name_ , _pubid_ , _system_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.doctype "Link to this definition")

Handles a doctype declaration. _name_ is the doctype name. _pubid_ is the public identifier. _system_ is the system identifier. This method does not exist on the default `TreeBuilder` class.
Added in version 3.2.

start_ns(_prefix_ , _uri_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.start_ns "Link to this definition")

Is called whenever the parser encounters a new namespace declaration, before the `start()` callback for the opening element that defines it. _prefix_ is `''` for the default namespace and the declared namespace prefix name otherwise. _uri_ is the namespace URI.
Added in version 3.8.

end_ns(_prefix_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.end_ns "Link to this definition")

Is called after the `end()` callback of an element that declared a namespace prefix mapping, with the name of the _prefix_ that went out of scope.
Added in version 3.8.

_class_ xml.etree.ElementTree.C14NWriterTarget(_write_ , _*_ , _with_comments =False_, _strip_text =False_, _rewrite_prefixes =False_, _qname_aware_tags =None_, _qname_aware_attrs =None_, _exclude_attrs =None_, _exclude_tags =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.C14NWriterTarget "Link to this definition")

A [`canonicalize()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.canonicalize "xml.etree.ElementTree.canonicalize") function. This class does not build a tree but translates the callback events directly into a serialised form using the _write_ function.
Added in version 3.8.
### XMLParser Objects[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xmlparser-objects "Link to this heading")

_class_ xml.etree.ElementTree.XMLParser(_*_ , _target =None_, _encoding =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "Link to this definition")

This class is the low-level building block of the module. It uses [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") for efficient, event-based parsing of XML. It can be fed XML data incrementally with the [`feed()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.feed "xml.etree.ElementTree.XMLParser.feed") method, and parsing events are translated to a push API - by invoking callbacks on the _target_ object. If _target_ is omitted, the standard [`TreeBuilder`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder "xml.etree.ElementTree.TreeBuilder") is used. If _encoding_ [[1]](https://docs.python.org/3/library/xml.etree.elementtree.html#id9) is given, the value overrides the encoding specified in the XML file.
Changed in version 3.8: Parameters are now [keyword-only](https://docs.python.org/3/glossary.html#keyword-only-parameter). The _html_ argument is no longer supported.

close()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.close "Link to this definition")

Finishes feeding data to the parser. Returns the result of calling the `close()` method of the _target_ passed during construction; by default, this is the toplevel document element.

feed(_data_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.feed "Link to this definition")

Feeds data to the parser. _data_ is encoded data.

flush()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.flush "Link to this definition")

Triggers parsing of any previously fed unparsed data, which can be used to ensure more immediate feedback, in particular with Expat >=2.6.0. The implementation of `flush()` temporarily disables reparse deferral with Expat (if currently enabled) and triggers a reparse. Disabling reparse deferral has security consequences; please see [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled") for details.
Note that `flush()` has been backported to some prior releases of CPython as a security fix. Check for availability of `flush()` using [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") if used in code running across a variety of Python versions.
Added in version 3.13.
[`XMLParser.feed()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.feed "xml.etree.ElementTree.XMLParser.feed") calls _target_ 's `start(tag, attrs_dict)` method for each opening tag, its `end(tag)` method for each closing tag, and data is processed by method `data(data)`. For further supported callback methods, see the [`TreeBuilder`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder "xml.etree.ElementTree.TreeBuilder") class. [`XMLParser.close()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.close "xml.etree.ElementTree.XMLParser.close") calls _target_ 's method `close()`. `XMLParser` can be used not only for building a tree structure. This is an example of counting the maximum depth of an XML file:
Copy```
>>> from xml.etree.ElementTree import XMLParser
>>> class MaxDepth:                     # The target object of the parser
...     maxDepth = 0
...     depth = 0
...     def start(self, tag, attrib):   # Called for each opening tag.
...         self.depth += 1
...         if self.depth > self.maxDepth:
...             self.maxDepth = self.depth
...     def end(self, tag):             # Called for each closing tag.
...         self.depth -= 1
...     def data(self, data):
...         pass            # We do not need to do anything with data.
...     def close(self):    # Called when all data has been parsed.
...         return self.maxDepth
...
>>> target = MaxDepth()
>>> parser = XMLParser(target=target)
>>> exampleXml = """
... <a>
...   <b>
...   </b>
...   <b>
...     <c>
...       <d>
...       </d>
...     </c>
...   </b>
... </a>"""
>>> parser.feed(exampleXml)
>>> parser.close()
4

```

### XMLPullParser Objects[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xmlpullparser-objects "Link to this heading")

_class_ xml.etree.ElementTree.XMLPullParser(_events =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser "Link to this definition")

A pull parser suitable for non-blocking applications. Its input-side API is similar to that of [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser"), but instead of pushing calls to a callback target, `XMLPullParser` collects an internal list of parsing events and lets the user read from it. _events_ is a sequence of events to report back. The supported events are the strings `"start"`, `"end"`, `"comment"`, `"pi"`, `"start-ns"` and `"end-ns"` (the “ns” events are used to get detailed namespace information). If _events_ is omitted, only `"end"` events are reported.

feed(_data_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.feed "Link to this definition")

Feed the given bytes data to the parser.

flush()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.flush "Link to this definition")

Triggers parsing of any previously fed unparsed data, which can be used to ensure more immediate feedback, in particular with Expat >=2.6.0. The implementation of `flush()` temporarily disables reparse deferral with Expat (if currently enabled) and triggers a reparse. Disabling reparse deferral has security consequences; please see [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled") for details.
Note that `flush()` has been backported to some prior releases of CPython as a security fix. Check for availability of `flush()` using [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") if used in code running across a variety of Python versions.
Added in version 3.13.

close()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.close "Link to this definition")

Signal the parser that the data stream is terminated. Unlike [`XMLParser.close()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.close "xml.etree.ElementTree.XMLParser.close"), this method always returns [`None`](https://docs.python.org/3/library/constants.html#None "None"). Any events not yet retrieved when the parser is closed can still be read with [`read_events()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.read_events "xml.etree.ElementTree.XMLPullParser.read_events").

read_events()[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.read_events "Link to this definition")

Return an iterator over the events which have been encountered in the data fed to the parser. The iterator yields `(event, elem)` pairs, where _event_ is a string representing the type of event (e.g. `"end"`) and _elem_ is the encountered [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") object, or other context value as follows.
  * `start`, `end`: the current Element.
  * `comment`, `pi`: the current comment / processing instruction
  * `start-ns`: a tuple `(prefix, uri)` naming the declared namespace mapping.
  * `end-ns`: [`None`](https://docs.python.org/3/library/constants.html#None "None") (this may change in a future version)


Events provided in a previous call to `read_events()` will not be yielded again. Events are consumed from the internal queue only when they are retrieved from the iterator, so multiple readers iterating in parallel over iterators obtained from `read_events()` will have unpredictable results.
Note
`XMLPullParser` only guarantees that it has seen the “>” character of a starting tag when it emits a “start” event, so the attributes are defined, but the contents of the text and tail attributes are undefined at that point. The same applies to the element children; they may or may not be present.
If you need a fully populated element, look for “end” events instead.
Added in version 3.4.
Changed in version 3.8: The `comment` and `pi` events were added.
### Exceptions[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#exceptions "Link to this heading")

_class_ xml.etree.ElementTree.ParseError[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ParseError "Link to this definition")

XML parse error, raised by the various parsing methods in this module when parsing fails. The string representation of an instance of this exception will contain a user-friendly error message. In addition, it will have the following attributes available:

code[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ParseError.code "Link to this definition")

A numeric error code from the expat parser. See the documentation of [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") for the list of error codes and their meanings.

position[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ParseError.position "Link to this definition")

A tuple of _line_ , _column_ numbers, specifying where the error occurred.
Footnotes
[1] ([1](https://docs.python.org/3/library/xml.etree.elementtree.html#id1),[2](https://docs.python.org/3/library/xml.etree.elementtree.html#id2),[3](https://docs.python.org/3/library/xml.etree.elementtree.html#id6),[4](https://docs.python.org/3/library/xml.etree.elementtree.html#id8))
The encoding string included in XML output should conform to the appropriate standards. For example, “UTF-8” is valid, but “UTF8” is not. See
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)
    * [Tutorial](https://docs.python.org/3/library/xml.etree.elementtree.html#tutorial)
      * [XML tree and elements](https://docs.python.org/3/library/xml.etree.elementtree.html#xml-tree-and-elements)
      * [Parsing XML](https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml)
      * [Pull API for non-blocking parsing](https://docs.python.org/3/library/xml.etree.elementtree.html#pull-api-for-non-blocking-parsing)
      * [Finding interesting elements](https://docs.python.org/3/library/xml.etree.elementtree.html#finding-interesting-elements)
      * [Modifying an XML File](https://docs.python.org/3/library/xml.etree.elementtree.html#modifying-an-xml-file)
      * [Building XML documents](https://docs.python.org/3/library/xml.etree.elementtree.html#building-xml-documents)
      * [Parsing XML with Namespaces](https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces)
    * [XPath support](https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support)
      * [Example](https://docs.python.org/3/library/xml.etree.elementtree.html#example)
      * [Supported XPath syntax](https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax)
    * [Reference](https://docs.python.org/3/library/xml.etree.elementtree.html#reference)
      * [Functions](https://docs.python.org/3/library/xml.etree.elementtree.html#functions)
    * [XInclude support](https://docs.python.org/3/library/xml.etree.elementtree.html#xinclude-support)
      * [Example](https://docs.python.org/3/library/xml.etree.elementtree.html#id3)
    * [Reference](https://docs.python.org/3/library/xml.etree.elementtree.html#id4)
      * [Functions](https://docs.python.org/3/library/xml.etree.elementtree.html#elementinclude-functions)
      * [Element Objects](https://docs.python.org/3/library/xml.etree.elementtree.html#element-objects)
      * [ElementTree Objects](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-objects)
      * [QName Objects](https://docs.python.org/3/library/xml.etree.elementtree.html#qname-objects)
      * [TreeBuilder Objects](https://docs.python.org/3/library/xml.etree.elementtree.html#treebuilder-objects)
      * [XMLParser Objects](https://docs.python.org/3/library/xml.etree.elementtree.html#xmlparser-objects)
      * [XMLPullParser Objects](https://docs.python.org/3/library/xml.etree.elementtree.html#xmlpullparser-objects)
      * [Exceptions](https://docs.python.org/3/library/xml.etree.elementtree.html#exceptions)


#### Previous topic
[XML Processing Modules](https://docs.python.org/3/library/xml.html "previous chapter")
#### Next topic
[`xml.dom` — The Document Object Model API](https://docs.python.org/3/library/xml.dom.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.etree.ElementTree+%E2%80%94+The+ElementTree+XML+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.etree.elementtree.html&pagesource=library%2Fxml.etree.elementtree.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.dom.html "xml.dom — The Document Object Model API") |
  * [previous](https://docs.python.org/3/library/xml.html "XML Processing Modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html#reference)
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
