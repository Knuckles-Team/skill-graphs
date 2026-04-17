## Reference[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#reference "Link to this heading")
### Functions[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#functions "Link to this heading")

xml.etree.ElementTree.canonicalize(_xml_data =None_, _*_ , _out =None_, _from_file =None_, _** options_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.canonicalize "Link to this definition")

Canonicalization is a way to normalise XML output in a way that allows byte-by-byte comparisons and digital signatures. It reduces the freedom that XML serializers have and instead generates a more constrained XML representation. The main restrictions regard the placement of namespace declarations, the ordering of attributes, and ignorable whitespace.
This function takes an XML data string (_xml_data_) or a file path or file-like object (_from_file_) as input, converts it to the canonical form, and writes it out using the _out_ file(-like) object, if provided, or returns it as a text string if not. The output file receives text, not bytes. It should therefore be opened in text mode with `utf-8` encoding.
Typical uses:
Copy```
xml_data = "<root>...</root>"
print(canonicalize(xml_data))

with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
    canonicalize(xml_data, out=out_file)

with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
    canonicalize(from_file="inputfile.xml", out=out_file)

```

The configuration _options_ are as follows:
  * _with_comments_ : set to true to include comments (default: false)
  *

_strip_text_ : set to true to strip whitespace before and after text content

(default: false)
  *

_rewrite_prefixes_ : set to true to replace namespace prefixes by “n{number}”

(default: false)
  *

_qname_aware_tags_ : a set of qname aware tag names in which prefixes

should be replaced in text content (default: empty)
  *

_qname_aware_attrs_ : a set of qname aware attribute names in which prefixes

should be replaced in text content (default: empty)
  * _exclude_attrs_ : a set of attribute names that should not be serialised
  * _exclude_tags_ : a set of tag names that should not be serialised


In the option list above, “a set” refers to any collection or iterable of strings, no ordering is expected.
Added in version 3.8.

xml.etree.ElementTree.Comment(_text =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Comment "Link to this definition")

Comment element factory. This factory function creates a special element that will be serialized as an XML comment by the standard serializer. The comment string can be either a bytestring or a Unicode string. _text_ is a string containing the comment string. Returns an element instance representing a comment.
Note that [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") skips over comments in the input instead of creating comment objects for them. An [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") will only contain comment nodes if they have been inserted into to the tree using one of the [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") methods.

xml.etree.ElementTree.dump(_elem_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.dump "Link to this definition")

Writes an element tree or element structure to sys.stdout. This function should be used for debugging only.
The exact output format is implementation dependent. In this version, it’s written as an ordinary XML file.
_elem_ is an element tree or an individual element.
Changed in version 3.8: The `dump()` function now preserves the attribute order specified by the user.

xml.etree.ElementTree.fromstring(_text_ , _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstring "Link to this definition")

Parses an XML section from a string constant. Same as [`XML()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML "xml.etree.ElementTree.XML"). _text_ is a string containing XML data. _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. Returns an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance.

xml.etree.ElementTree.fromstringlist(_sequence_ , _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstringlist "Link to this definition")

Parses an XML document from a sequence of string fragments. _sequence_ is a list or other sequence containing XML data fragments. _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. Returns an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance.
Added in version 3.2.

xml.etree.ElementTree.indent(_tree_ , _space =' '_, _level =0_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.indent "Link to this definition")

Appends whitespace to the subtree to indent the tree visually. This can be used to generate pretty-printed XML output. _tree_ can be an Element or ElementTree. _space_ is the whitespace string that will be inserted for each indentation level, two space characters by default. For indenting partial subtrees inside of an already indented tree, pass the initial indentation level as _level_.
Added in version 3.9.

xml.etree.ElementTree.iselement(_element_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.iselement "Link to this definition")

Check if an object appears to be a valid element object. _element_ is an element instance. Return `True` if this is an element object.

xml.etree.ElementTree.iterparse(_source_ , _events =None_, _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse "Link to this definition")

Parses an XML section into an element tree incrementally, and reports what’s going on to the user. _source_ is a filename or [file object](https://docs.python.org/3/glossary.html#term-file-object) containing XML data. _events_ is a sequence of events to report back. The supported events are the strings `"start"`, `"end"`, `"comment"`, `"pi"`, `"start-ns"` and `"end-ns"` (the “ns” events are used to get detailed namespace information). If _events_ is omitted, only `"end"` events are reported. _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. _parser_ must be a subclass of `XMLParser` and can only use the default [`TreeBuilder`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder "xml.etree.ElementTree.TreeBuilder") as a target. Returns an [iterator](https://docs.python.org/3/glossary.html#term-iterator) providing `(event, elem)` pairs; it has a `root` attribute that references the root element of the resulting XML tree once _source_ is fully read. The iterator has the `close()` method that closes the internal file object if _source_ is a filename.
Note that while `iterparse()` builds the tree incrementally, it issues blocking reads on _source_ (or the file it names). As such, it’s unsuitable for applications where blocking reads can’t be made. For fully non-blocking parsing, see [`XMLPullParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser "xml.etree.ElementTree.XMLPullParser").
Note
`iterparse()` only guarantees that it has seen the “>” character of a starting tag when it emits a “start” event, so the attributes are defined, but the contents of the text and tail attributes are undefined at that point. The same applies to the element children; they may or may not be present.
If you need a fully populated element, look for “end” events instead.
Deprecated since version 3.4: The _parser_ argument.
Changed in version 3.8: The `comment` and `pi` events were added.
Changed in version 3.13: Added the `close()` method.

xml.etree.ElementTree.parse(_source_ , _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.parse "Link to this definition")

Parses an XML section into an element tree. _source_ is a filename or file object containing XML data. _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. Returns an [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") instance.

xml.etree.ElementTree.ProcessingInstruction(_target_ , _text =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ProcessingInstruction "Link to this definition")

PI element factory. This factory function creates a special element that will be serialized as an XML processing instruction. _target_ is a string containing the PI target. _text_ is a string containing the PI contents, if given. Returns an element instance, representing a processing instruction.
Note that [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") skips over processing instructions in the input instead of creating PI objects for them. An [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") will only contain processing instruction nodes if they have been inserted into to the tree using one of the [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") methods.

xml.etree.ElementTree.register_namespace(_prefix_ , _uri_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.register_namespace "Link to this definition")

Registers a namespace prefix. The registry is global, and any existing mapping for either the given prefix or the namespace URI will be removed. _prefix_ is a namespace prefix. _uri_ is a namespace uri. Tags and attributes in this namespace will be serialized with the given prefix, if at all possible.
Added in version 3.2.

xml.etree.ElementTree.SubElement(_parent_ , _tag_ , _attrib ={}_, _** extra_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.SubElement "Link to this definition")

Subelement factory. This function creates an element instance, and appends it to an existing element.
The element name, attribute names, and attribute values can be either bytestrings or Unicode strings. _parent_ is the parent element. _tag_ is the subelement name. _attrib_ is an optional dictionary, containing element attributes. _extra_ contains additional attributes, given as keyword arguments. Returns an element instance.

xml.etree.ElementTree.tostring(_element_ , _encoding ='us-ascii'_, _method ='xml'_, _*_ , _xml_declaration =None_, _default_namespace =None_, _short_empty_elements =True_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring "Link to this definition")

Generates a string representation of an XML element, including all subelements. _element_ is an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance. _encoding_ [[1]](https://docs.python.org/3/library/xml.etree.elementtree.html#id9) is the output encoding (default is US-ASCII). Use `encoding="unicode"` to generate a Unicode string (otherwise, a bytestring is generated). _method_ is either `"xml"`, `"html"` or `"text"` (default is `"xml"`). _xml_declaration_ , _default_namespace_ and _short_empty_elements_ has the same meaning as in [`ElementTree.write()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write "xml.etree.ElementTree.ElementTree.write"). Returns an (optionally) encoded string containing the XML data.
Changed in version 3.4: Added the _short_empty_elements_ parameter.
Changed in version 3.8: Added the _xml_declaration_ and _default_namespace_ parameters.
Changed in version 3.8: The `tostring()` function now preserves the attribute order specified by the user.

xml.etree.ElementTree.tostringlist(_element_ , _encoding ='us-ascii'_, _method ='xml'_, _*_ , _xml_declaration =None_, _default_namespace =None_, _short_empty_elements =True_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostringlist "Link to this definition")

Generates a string representation of an XML element, including all subelements. _element_ is an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance. _encoding_ [[1]](https://docs.python.org/3/library/xml.etree.elementtree.html#id9) is the output encoding (default is US-ASCII). Use `encoding="unicode"` to generate a Unicode string (otherwise, a bytestring is generated). _method_ is either `"xml"`, `"html"` or `"text"` (default is `"xml"`). _xml_declaration_ , _default_namespace_ and _short_empty_elements_ has the same meaning as in [`ElementTree.write()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write "xml.etree.ElementTree.ElementTree.write"). Returns a list of (optionally) encoded strings containing the XML data. It does not guarantee any specific sequence, except that `b"".join(tostringlist(element)) == tostring(element)`.
Added in version 3.2.
Changed in version 3.4: Added the _short_empty_elements_ parameter.
Changed in version 3.8: Added the _xml_declaration_ and _default_namespace_ parameters.
Changed in version 3.8: The `tostringlist()` function now preserves the attribute order specified by the user.

xml.etree.ElementTree.XML(_text_ , _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML "Link to this definition")

Parses an XML section from a string constant. This function can be used to embed “XML literals” in Python code. _text_ is a string containing XML data. _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. Returns an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance.

xml.etree.ElementTree.XMLID(_text_ , _parser =None_)[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLID "Link to this definition")

Parses an XML section from a string constant, and also returns a dictionary which maps from element id:s to elements. _text_ is a string containing XML data. _parser_ is an optional parser instance. If not given, the standard [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") parser is used. Returns a tuple containing an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") instance and a dictionary.
## XInclude support[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xinclude-support "Link to this heading")
This module provides limited support for [`xml.etree.ElementInclude`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementInclude "xml.etree.ElementInclude") helper module. This module can be used to insert subtrees and text strings into element trees, based on information in the tree.
### Example[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#id3 "Link to this heading")
Here’s an example that demonstrates use of the XInclude module. To include an XML document in the current document, use the `{http://www.w3.org/2001/XInclude}include` element and set the **parse** attribute to `"xml"`, and use the **href** attribute to specify the document to include.
```
<?xml version="1.0"?>
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="source.xml" parse="xml" />
</document>

```

By default, the **href** attribute is treated as a file name. You can use custom loaders to override this behaviour. Also note that the standard helper does not support XPointer syntax.
To process this file, load it as usual, and pass the root element to the `xml.etree.ElementTree` module:
Copy```
from xml.etree import ElementTree, ElementInclude

tree = ElementTree.parse("document.xml")
root = tree.getroot()

ElementInclude.include(root)

```

The ElementInclude module replaces the `{http://www.w3.org/2001/XInclude}include` element with the root element from the **source.xml** document. The result might look something like this:
```
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  <para>This is a paragraph.</para>
</document>

```

If the **parse** attribute is omitted, it defaults to “xml”. The href attribute is required.
To include a text document, use the `{http://www.w3.org/2001/XInclude}include` element, and set the **parse** attribute to “text”:
```
<?xml version="1.0"?>
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  Copyright (c) <xi:include href="year.txt" parse="text" />.
</document>

```

The result might look something like:
```
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  Copyright (c) 2003.
</document>

```
