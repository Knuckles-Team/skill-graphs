#  `xml.dom` — The Document Object Model API[¶](https://docs.python.org/3/library/xml.dom.html#module-xml.dom "Link to this heading")
**Source code:**
* * *
The Document Object Model, or “DOM,” is a cross-language API from the World Wide Web Consortium (W3C) for accessing and modifying XML documents. A DOM implementation presents an XML document as a tree structure, or allows client code to build such a structure from scratch. It then gives access to the structure through a set of objects which provided well-known interfaces.
The DOM is extremely useful for random-access applications. SAX only allows you a view of one bit of the document at a time. If you are looking at one SAX element, you have no access to another. If you are looking at a text node, you have no access to a containing element. When you write a SAX application, you need to keep track of your program’s position in the document somewhere in your own code. SAX does not do it for you. Also, if you need to look ahead in the XML document, you are just out of luck.
Some applications are simply impossible in an event driven model with no access to a tree. Of course you could build some sort of tree yourself in SAX events, but the DOM allows you to avoid writing that code. The DOM is a standard tree representation for XML data.
The Document Object Model is being defined by the W3C in stages, or “levels” in their terminology. The Python mapping of the API is substantially based on the DOM Level 2 recommendation.
DOM applications typically start by parsing some XML into a DOM. How this is accomplished is not covered at all by DOM Level 1, and Level 2 provides only limited improvements: There is a `DOMImplementation` object class which provides access to `Document` creation methods, but no way to access an XML reader/parser/Document builder in an implementation-independent way. There is also no well-defined way to access these methods without an existing `Document` object. In Python, each DOM implementation will provide a function [`getDOMImplementation()`](https://docs.python.org/3/library/xml.dom.html#xml.dom.getDOMImplementation "xml.dom.getDOMImplementation"). DOM Level 3 adds a Load/Store specification, which defines an interface to the reader, but this is not yet available in the Python standard library.
Once you have a DOM document object, you can access the parts of your XML document through its properties and methods. These properties are defined in the DOM specification; this portion of the reference manual describes the interpretation of the specification in Python.
The specification provided by the W3C defines the DOM API for Java, ECMAScript, and OMG IDL. The Python mapping defined here is based in large part on the IDL version of the specification, but strict compliance is not required (though implementations are free to support the strict mapping from IDL). See section [Conformance](https://docs.python.org/3/library/xml.dom.html#dom-conformance) for a detailed discussion of mapping requirements.
See also
The W3C recommendation upon which the Python DOM API is based.
The W3C recommendation for the DOM supported by [`xml.dom.minidom`](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom "xml.dom.minidom: Minimal Document Object Model \(DOM\) implementation.").
This specifies the mapping from OMG IDL to Python.
## Module Contents[¶](https://docs.python.org/3/library/xml.dom.html#module-contents "Link to this heading")
The `xml.dom` contains the following functions:

xml.dom.registerDOMImplementation(_name_ , _factory_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.registerDOMImplementation "Link to this definition")

Register the _factory_ function with the name _name_. The factory function should return an object which implements the `DOMImplementation` interface. The factory function can return the same object every time, or a new one for each call, as appropriate for the specific implementation (e.g. if that implementation supports some customization).

xml.dom.getDOMImplementation(_name =None_, _features =()_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.getDOMImplementation "Link to this definition")

Return a suitable DOM implementation. The _name_ is either well-known, the module name of a DOM implementation, or `None`. If it is not `None`, imports the corresponding module and returns a `DOMImplementation` object if the import succeeds. If no name is given, and if the environment variable `PYTHON_DOM` is set, this variable is used to find the implementation.
If name is not given, this examines the available implementations to find one with the required feature set. If no implementation can be found, raise an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError"). The features list must be a sequence of `(feature, version)` pairs which are passed to the `hasFeature()` method on available `DOMImplementation` objects.
Some convenience constants are also provided:

xml.dom.EMPTY_NAMESPACE[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.EMPTY_NAMESPACE "Link to this definition")

The value used to indicate that no namespace is associated with a node in the DOM. This is typically found as the `namespaceURI` of a node, or used as the _namespaceURI_ parameter to a namespaces-specific method.

xml.dom.XML_NAMESPACE[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.XML_NAMESPACE "Link to this definition")

The namespace URI associated with the reserved prefix `xml`, as defined by

xml.dom.XMLNS_NAMESPACE[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.XMLNS_NAMESPACE "Link to this definition")

The namespace URI for namespace declarations, as defined by

xml.dom.XHTML_NAMESPACE[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.XHTML_NAMESPACE "Link to this definition")

The URI of the XHTML namespace as defined by
In addition, `xml.dom` contains a base `Node` class and the DOM exception classes. The `Node` class provided by this module does not implement any of the methods or attributes defined by the DOM specification; concrete DOM implementations must provide those. The `Node` class provided as part of this module does provide the constants used for the `nodeType` attribute on concrete `Node` objects; they are located within the class rather than at the module level to conform with the DOM specifications.
## Objects in the DOM[¶](https://docs.python.org/3/library/xml.dom.html#objects-in-the-dom "Link to this heading")
The definitive documentation for the DOM is the DOM specification from the W3C.
Note that DOM attributes may also be manipulated as nodes instead of as simple strings. It is fairly rare that you must do this, however, so this usage is not yet documented.
Interface | Section | Purpose
---|---|---
`DOMImplementation` | [DOMImplementation Objects](https://docs.python.org/3/library/xml.dom.html#dom-implementation-objects) | Interface to the underlying implementation.
`Node` | [Node Objects](https://docs.python.org/3/library/xml.dom.html#dom-node-objects) | Base interface for most objects in a document.
`NodeList` | [NodeList Objects](https://docs.python.org/3/library/xml.dom.html#dom-nodelist-objects) | Interface for a sequence of nodes.
`DocumentType` | [DocumentType Objects](https://docs.python.org/3/library/xml.dom.html#dom-documenttype-objects) | Information about the declarations needed to process a document.
`Document` | [Document Objects](https://docs.python.org/3/library/xml.dom.html#dom-document-objects) | Object which represents an entire document.
`Element` | [Element Objects](https://docs.python.org/3/library/xml.dom.html#dom-element-objects) | Element nodes in the document hierarchy.
`Attr` | [Attr Objects](https://docs.python.org/3/library/xml.dom.html#dom-attr-objects) | Attribute value nodes on element nodes.
`Comment` | [Comment Objects](https://docs.python.org/3/library/xml.dom.html#dom-comment-objects) | Representation of comments in the source document.
`Text` | [Text and CDATASection Objects](https://docs.python.org/3/library/xml.dom.html#dom-text-objects) | Nodes containing textual content from the document.
`ProcessingInstruction` | [ProcessingInstruction Objects](https://docs.python.org/3/library/xml.dom.html#dom-pi-objects) | Processing instruction representation.
An additional section describes the exceptions defined for working with the DOM in Python.
### DOMImplementation Objects[¶](https://docs.python.org/3/library/xml.dom.html#domimplementation-objects "Link to this heading")
The `DOMImplementation` interface provides a way for applications to determine the availability of particular features in the DOM they are using. DOM Level 2 added the ability to create new `Document` and `DocumentType` objects using the `DOMImplementation` as well.

DOMImplementation.hasFeature(_feature_ , _version_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DOMImplementation.hasFeature "Link to this definition")

Return `True` if the feature identified by the pair of strings _feature_ and _version_ is implemented.

DOMImplementation.createDocument(_namespaceUri_ , _qualifiedName_ , _doctype_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DOMImplementation.createDocument "Link to this definition")

Return a new `Document` object (the root of the DOM), with a child `Element` object having the given _namespaceUri_ and _qualifiedName_. The _doctype_ must be a `DocumentType` object created by [`createDocumentType()`](https://docs.python.org/3/library/xml.dom.html#xml.dom.DOMImplementation.createDocumentType "xml.dom.DOMImplementation.createDocumentType"), or `None`. In the Python DOM API, the first two arguments can also be `None` in order to indicate that no `Element` child is to be created.

DOMImplementation.createDocumentType(_qualifiedName_ , _publicId_ , _systemId_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DOMImplementation.createDocumentType "Link to this definition")

Return a new `DocumentType` object that encapsulates the given _qualifiedName_ , _publicId_ , and _systemId_ strings, representing the information contained in an XML document type declaration.
### Node Objects[¶](https://docs.python.org/3/library/xml.dom.html#node-objects "Link to this heading")
All of the components of an XML document are subclasses of `Node`.

Node.nodeType[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.nodeType "Link to this definition")

An integer representing the node type. Symbolic constants for the types are on the `Node` object: `ELEMENT_NODE`, `ATTRIBUTE_NODE`, `TEXT_NODE`, `CDATA_SECTION_NODE`, `ENTITY_NODE`, `PROCESSING_INSTRUCTION_NODE`, `COMMENT_NODE`, `DOCUMENT_NODE`, `DOCUMENT_TYPE_NODE`, `NOTATION_NODE`. This is a read-only attribute.

Node.parentNode[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.parentNode "Link to this definition")

The parent of the current node, or `None` for the document node. The value is always a `Node` object or `None`. For `Element` nodes, this will be the parent element, except for the root element, in which case it will be the `Document` object. For `Attr` nodes, this is always `None`. This is a read-only attribute.

Node.attributes[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.attributes "Link to this definition")

A `NamedNodeMap` of attribute objects. Only elements have actual values for this; others provide `None` for this attribute. This is a read-only attribute.

Node.previousSibling[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.previousSibling "Link to this definition")

The node that immediately precedes this one with the same parent. For instance the element with an end-tag that comes just before the _self_ element’s start-tag. Of course, XML documents are made up of more than just elements so the previous sibling could be text, a comment, or something else. If this node is the first child of the parent, this attribute will be `None`. This is a read-only attribute.

Node.nextSibling[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.nextSibling "Link to this definition")

The node that immediately follows this one with the same parent. See also [`previousSibling`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.previousSibling "xml.dom.Node.previousSibling"). If this is the last child of the parent, this attribute will be `None`. This is a read-only attribute.

Node.childNodes[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.childNodes "Link to this definition")

A list of nodes contained within this node. This is a read-only attribute.

Node.firstChild[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.firstChild "Link to this definition")

The first child of the node, if there are any, or `None`. This is a read-only attribute.

Node.lastChild[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.lastChild "Link to this definition")

The last child of the node, if there are any, or `None`. This is a read-only attribute.

Node.localName[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.localName "Link to this definition")

The part of the `tagName` following the colon if there is one, else the entire `tagName`. The value is a string.

Node.prefix[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.prefix "Link to this definition")

The part of the `tagName` preceding the colon if there is one, else the empty string. The value is a string, or `None`.

Node.namespaceURI[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.namespaceURI "Link to this definition")

The namespace associated with the element name. This will be a string or `None`. This is a read-only attribute.

Node.nodeName[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.nodeName "Link to this definition")

This has a different meaning for each node type; see the DOM specification for details. You can always get the information you would get here from another property such as the `tagName` property for elements or the `name` property for attributes. For all node types, the value of this attribute will be either a string or `None`. This is a read-only attribute.

Node.nodeValue[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.nodeValue "Link to this definition")

This has a different meaning for each node type; see the DOM specification for details. The situation is similar to that with [`nodeName`](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.nodeName "xml.dom.Node.nodeName"). The value is a string or `None`.

Node.hasAttributes()[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.hasAttributes "Link to this definition")

Return `True` if the node has any attributes.

Node.hasChildNodes()[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.hasChildNodes "Link to this definition")

Return `True` if the node has any child nodes.

Node.isSameNode(_other_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.isSameNode "Link to this definition")

Return `True` if _other_ refers to the same node as this node. This is especially useful for DOM implementations which use any sort of proxy architecture (because more than one object can refer to the same node).
Note
This is based on a proposed DOM Level 3 API which is still in the “working draft” stage, but this particular interface appears uncontroversial. Changes from the W3C will not necessarily affect this method in the Python DOM interface (though any new W3C API for this would also be supported).

Node.appendChild(_newChild_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.appendChild "Link to this definition")

Add a new child node to this node at the end of the list of children, returning _newChild_. If the node was already in the tree, it is removed first.

Node.insertBefore(_newChild_ , _refChild_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.insertBefore "Link to this definition")

Insert a new child node before an existing child. It must be the case that _refChild_ is a child of this node; if not, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. _newChild_ is returned. If _refChild_ is `None`, it inserts _newChild_ at the end of the children’s list.

Node.removeChild(_oldChild_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.removeChild "Link to this definition")

Remove a child node. _oldChild_ must be a child of this node; if not, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. _oldChild_ is returned on success. If _oldChild_ will not be used further, its `unlink()` method should be called.

Node.replaceChild(_newChild_ , _oldChild_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.replaceChild "Link to this definition")

Replace an existing node with a new node. It must be the case that _oldChild_ is a child of this node; if not, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

Node.normalize()[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.normalize "Link to this definition")

Join adjacent text nodes so that all stretches of text are stored as single `Text` instances. This simplifies processing text from a DOM tree for many applications.

Node.cloneNode(_deep_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Node.cloneNode "Link to this definition")

Clone this node. Setting _deep_ means to clone all child nodes as well. This returns the clone.
### NodeList Objects[¶](https://docs.python.org/3/library/xml.dom.html#nodelist-objects "Link to this heading")
A `NodeList` represents a sequence of nodes. These objects are used in two ways in the DOM Core recommendation: an `Element` object provides one as its list of child nodes, and the `getElementsByTagName()` and `getElementsByTagNameNS()` methods of `Node` return objects with this interface to represent query results.
The DOM Level 2 recommendation defines one method and one attribute for these objects:

NodeList.item(_i_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NodeList.item "Link to this definition")

Return the _i_ ’th item from the sequence, if there is one, or `None`. The index _i_ is not allowed to be less than zero or greater than or equal to the length of the sequence.

NodeList.length[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NodeList.length "Link to this definition")

The number of nodes in the sequence.
In addition, the Python DOM interface requires that some additional support is provided to allow `NodeList` objects to be used as Python sequences. All `NodeList` implementations must include support for [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__") and [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__"); this allows iteration over the `NodeList` in [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) statements and proper support for the [`len()`](https://docs.python.org/3/library/functions.html#len "len") built-in function.
If a DOM implementation supports modification of the document, the `NodeList` implementation must also support the [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__") and [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__") methods.
### DocumentType Objects[¶](https://docs.python.org/3/library/xml.dom.html#documenttype-objects "Link to this heading")
Information about the notations and entities declared by a document (including the external subset if the parser uses it and can provide the information) is available from a `DocumentType` object. The `DocumentType` for a document is available from the `Document` object’s `doctype` attribute; if there is no `DOCTYPE` declaration for the document, the document’s `doctype` attribute will be set to `None` instead of an instance of this interface.
`DocumentType` is a specialization of `Node`, and adds the following attributes:

DocumentType.publicId[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.publicId "Link to this definition")

The public identifier for the external subset of the document type definition. This will be a string or `None`.

DocumentType.systemId[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.systemId "Link to this definition")

The system identifier for the external subset of the document type definition. This will be a URI as a string, or `None`.

DocumentType.internalSubset[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.internalSubset "Link to this definition")

A string giving the complete internal subset from the document. This does not include the brackets which enclose the subset. If the document has no internal subset, this should be `None`.

DocumentType.name[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.name "Link to this definition")

The name of the root element as given in the `DOCTYPE` declaration, if present.

DocumentType.entities[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.entities "Link to this definition")

This is a `NamedNodeMap` giving the definitions of external entities. For entity names defined more than once, only the first definition is provided (others are ignored as required by the XML recommendation). This may be `None` if the information is not provided by the parser, or if no entities are defined.

DocumentType.notations[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DocumentType.notations "Link to this definition")

This is a `NamedNodeMap` giving the definitions of notations. For notation names defined more than once, only the first definition is provided (others are ignored as required by the XML recommendation). This may be `None` if the information is not provided by the parser, or if no notations are defined.
### Document Objects[¶](https://docs.python.org/3/library/xml.dom.html#document-objects "Link to this heading")
A `Document` represents an entire XML document, including its constituent elements, attributes, processing instructions, comments etc. Remember that it inherits properties from `Node`.

Document.documentElement[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.documentElement "Link to this definition")

The one and only root element of the document.

Document.createElement(_tagName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createElement "Link to this definition")

Create and return a new element node. The element is not inserted into the document when it is created. You need to explicitly insert it with one of the other methods such as `insertBefore()` or `appendChild()`.

Document.createElementNS(_namespaceURI_ , _tagName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createElementNS "Link to this definition")

Create and return a new element with a namespace. The _tagName_ may have a prefix. The element is not inserted into the document when it is created. You need to explicitly insert it with one of the other methods such as `insertBefore()` or `appendChild()`.

Document.createTextNode(_data_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createTextNode "Link to this definition")

Create and return a text node containing the data passed as a parameter. As with the other creation methods, this one does not insert the node into the tree.

Document.createComment(_data_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createComment "Link to this definition")

Create and return a comment node containing the data passed as a parameter. As with the other creation methods, this one does not insert the node into the tree.

Document.createProcessingInstruction(_target_ , _data_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createProcessingInstruction "Link to this definition")

Create and return a processing instruction node containing the _target_ and _data_ passed as parameters. As with the other creation methods, this one does not insert the node into the tree.

Document.createAttribute(_name_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createAttribute "Link to this definition")

Create and return an attribute node. This method does not associate the attribute node with any particular element. You must use `setAttributeNode()` on the appropriate `Element` object to use the newly created attribute instance.

Document.createAttributeNS(_namespaceURI_ , _qualifiedName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.createAttributeNS "Link to this definition")

Create and return an attribute node with a namespace. The _tagName_ may have a prefix. This method does not associate the attribute node with any particular element. You must use `setAttributeNode()` on the appropriate `Element` object to use the newly created attribute instance.

Document.getElementsByTagName(_tagName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.getElementsByTagName "Link to this definition")

Search for all descendants (direct children, children’s children, etc.) with a particular element type name.

Document.getElementsByTagNameNS(_namespaceURI_ , _localName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Document.getElementsByTagNameNS "Link to this definition")

Search for all descendants (direct children, children’s children, etc.) with a particular namespace URI and localname. The localname is the part of the namespace after the prefix.
### Element Objects[¶](https://docs.python.org/3/library/xml.dom.html#element-objects "Link to this heading")
`Element` is a subclass of `Node`, so inherits all the attributes of that class.

Element.tagName[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.tagName "Link to this definition")

The element type name. In a namespace-using document it may have colons in it. The value is a string.

Element.getElementsByTagName(_tagName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.getElementsByTagName "Link to this definition")

Same as equivalent method in the `Document` class.

Element.getElementsByTagNameNS(_namespaceURI_ , _localName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.getElementsByTagNameNS "Link to this definition")

Same as equivalent method in the `Document` class.

Element.hasAttribute(_name_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.hasAttribute "Link to this definition")

Return `True` if the element has an attribute named by _name_.

Element.hasAttributeNS(_namespaceURI_ , _localName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.hasAttributeNS "Link to this definition")

Return `True` if the element has an attribute named by _namespaceURI_ and _localName_.

Element.getAttribute(_name_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.getAttribute "Link to this definition")

Return the value of the attribute named by _name_ as a string. If no such attribute exists, an empty string is returned, as if the attribute had no value.

Element.getAttributeNode(_attrname_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.getAttributeNode "Link to this definition")

Return the `Attr` node for the attribute named by _attrname_.

Element.getAttributeNS(_namespaceURI_ , _localName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.getAttributeNS "Link to this definition")

Return the value of the attribute named by _namespaceURI_ and _localName_ as a string. If no such attribute exists, an empty string is returned, as if the attribute had no value.

Element.getAttributeNodeNS(_namespaceURI_ , _localName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.getAttributeNodeNS "Link to this definition")

Return an attribute value as a node, given a _namespaceURI_ and _localName_.

Element.removeAttribute(_name_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.removeAttribute "Link to this definition")

Remove an attribute by name. If there is no matching attribute, a [`NotFoundErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotFoundErr "xml.dom.NotFoundErr") is raised.

Element.removeAttributeNode(_oldAttr_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.removeAttributeNode "Link to this definition")

Remove and return _oldAttr_ from the attribute list, if present. If _oldAttr_ is not present, [`NotFoundErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotFoundErr "xml.dom.NotFoundErr") is raised.

Element.removeAttributeNS(_namespaceURI_ , _localName_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.removeAttributeNS "Link to this definition")

Remove an attribute by name. Note that it uses a localName, not a qname. No exception is raised if there is no matching attribute.

Element.setAttribute(_name_ , _value_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.setAttribute "Link to this definition")

Set an attribute value from a string.

Element.setAttributeNode(_newAttr_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.setAttributeNode "Link to this definition")

Add a new attribute node to the element, replacing an existing attribute if necessary if the `name` attribute matches. If a replacement occurs, the old attribute node will be returned. If _newAttr_ is already in use, [`InuseAttributeErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InuseAttributeErr "xml.dom.InuseAttributeErr") will be raised.

Element.setAttributeNodeNS(_newAttr_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.setAttributeNodeNS "Link to this definition")

Add a new attribute node to the element, replacing an existing attribute if necessary if the `namespaceURI` and `localName` attributes match. If a replacement occurs, the old attribute node will be returned. If _newAttr_ is already in use, [`InuseAttributeErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InuseAttributeErr "xml.dom.InuseAttributeErr") will be raised.

Element.setAttributeNS(_namespaceURI_ , _qname_ , _value_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Element.setAttributeNS "Link to this definition")

Set an attribute value from a string, given a _namespaceURI_ and a _qname_. Note that a qname is the whole attribute name. This is different than above.
### Attr Objects[¶](https://docs.python.org/3/library/xml.dom.html#attr-objects "Link to this heading")
`Attr` inherits from `Node`, so inherits all its attributes.

Attr.name[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Attr.name "Link to this definition")

The attribute name. In a namespace-using document it may include a colon.

Attr.localName[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Attr.localName "Link to this definition")

The part of the name following the colon if there is one, else the entire name. This is a read-only attribute.

Attr.prefix[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Attr.prefix "Link to this definition")

The part of the name preceding the colon if there is one, else the empty string.

Attr.value[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Attr.value "Link to this definition")

The text value of the attribute. This is a synonym for the `nodeValue` attribute.
### NamedNodeMap Objects[¶](https://docs.python.org/3/library/xml.dom.html#namednodemap-objects "Link to this heading")
`NamedNodeMap` does _not_ inherit from `Node`.

NamedNodeMap.length[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NamedNodeMap.length "Link to this definition")

The length of the attribute list.

NamedNodeMap.item(_index_)[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NamedNodeMap.item "Link to this definition")

Return an attribute with a particular index. The order you get the attributes in is arbitrary but will be consistent for the life of a DOM. Each item is an attribute node. Get its value with the `value` attribute.
There are also experimental methods that give this class more mapping behavior. You can use them or you can use the standardized `getAttribute*()` family of methods on the `Element` objects.
### Comment Objects[¶](https://docs.python.org/3/library/xml.dom.html#comment-objects "Link to this heading")
`Comment` represents a comment in the XML document. It is a subclass of `Node`, but cannot have child nodes.

Comment.data[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Comment.data "Link to this definition")

The content of the comment as a string. The attribute contains all characters between the leading `<!-``-` and trailing `-``->`, but does not include them.
### Text and CDATASection Objects[¶](https://docs.python.org/3/library/xml.dom.html#text-and-cdatasection-objects "Link to this heading")
The `Text` interface represents text in the XML document. If the parser and DOM implementation support the DOM’s XML extension, portions of the text enclosed in CDATA marked sections are stored in `CDATASection` objects. These two interfaces are identical, but provide different values for the `nodeType` attribute.
These interfaces extend the `Node` interface. They cannot have child nodes.

Text.data[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.Text.data "Link to this definition")

The content of the text node as a string.
Note
The use of a `CDATASection` node does not indicate that the node represents a complete CDATA marked section, only that the content of the node was part of a CDATA section. A single CDATA section may be represented by more than one node in the document tree. There is no way to determine whether two adjacent `CDATASection` nodes represent different CDATA marked sections.
### ProcessingInstruction Objects[¶](https://docs.python.org/3/library/xml.dom.html#processinginstruction-objects "Link to this heading")
Represents a processing instruction in the XML document; this inherits from the `Node` interface and cannot have child nodes.

ProcessingInstruction.target[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.ProcessingInstruction.target "Link to this definition")

The content of the processing instruction up to the first whitespace character. This is a read-only attribute.

ProcessingInstruction.data[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.ProcessingInstruction.data "Link to this definition")

The content of the processing instruction following the first whitespace character.
### Exceptions[¶](https://docs.python.org/3/library/xml.dom.html#exceptions "Link to this heading")
The DOM Level 2 recommendation defines a single exception, [`DOMException`](https://docs.python.org/3/library/xml.dom.html#xml.dom.DOMException "xml.dom.DOMException"), and a number of constants that allow applications to determine what sort of error occurred. `DOMException` instances carry a [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") attribute that provides the appropriate value for the specific exception.
The Python DOM interface provides the constants, but also expands the set of exceptions so that a specific exception exists for each of the exception codes defined by the DOM. The implementations must raise the appropriate specific exception, each of which carries the appropriate value for the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") attribute.

_exception_ xml.dom.DOMException[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DOMException "Link to this definition")

Base exception class used for all specific DOM exceptions. This exception class cannot be directly instantiated.

_exception_ xml.dom.DomstringSizeErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.DomstringSizeErr "Link to this definition")

Raised when a specified range of text does not fit into a string. This is not known to be used in the Python DOM implementations, but may be received from DOM implementations not written in Python.

_exception_ xml.dom.HierarchyRequestErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.HierarchyRequestErr "Link to this definition")

Raised when an attempt is made to insert a node where the node type is not allowed.

_exception_ xml.dom.IndexSizeErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.IndexSizeErr "Link to this definition")

Raised when an index or size parameter to a method is negative or exceeds the allowed values.

_exception_ xml.dom.InuseAttributeErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.InuseAttributeErr "Link to this definition")

Raised when an attempt is made to insert an `Attr` node that is already present elsewhere in the document.

_exception_ xml.dom.InvalidAccessErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidAccessErr "Link to this definition")

Raised if a parameter or an operation is not supported on the underlying object.

_exception_ xml.dom.InvalidCharacterErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidCharacterErr "Link to this definition")

This exception is raised when a string parameter contains a character that is not permitted in the context it’s being used in by the XML 1.0 recommendation. For example, attempting to create an `Element` node with a space in the element type name will cause this error to be raised.

_exception_ xml.dom.InvalidModificationErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidModificationErr "Link to this definition")

Raised when an attempt is made to modify the type of a node.

_exception_ xml.dom.InvalidStateErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidStateErr "Link to this definition")

Raised when an attempt is made to use an object that is not defined or is no longer usable.

_exception_ xml.dom.NamespaceErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NamespaceErr "Link to this definition")

If an attempt is made to change any object in a way that is not permitted with regard to the

_exception_ xml.dom.NotFoundErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotFoundErr "Link to this definition")

Exception when a node does not exist in the referenced context. For example, `NamedNodeMap.removeNamedItem()` will raise this if the node passed in does not exist in the map.

_exception_ xml.dom.NotSupportedErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotSupportedErr "Link to this definition")

Raised when the implementation does not support the requested type of object or operation.

_exception_ xml.dom.NoDataAllowedErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NoDataAllowedErr "Link to this definition")

This is raised if data is specified for a node which does not support data.

_exception_ xml.dom.NoModificationAllowedErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.NoModificationAllowedErr "Link to this definition")

Raised on attempts to modify an object where modifications are not allowed (such as for read-only nodes).

_exception_ xml.dom.SyntaxErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.SyntaxErr "Link to this definition")

Raised when an invalid or illegal string is specified.

_exception_ xml.dom.WrongDocumentErr[¶](https://docs.python.org/3/library/xml.dom.html#xml.dom.WrongDocumentErr "Link to this definition")

Raised when a node is inserted in a different document than it currently belongs to, and the implementation does not support migrating the node from one document to the other.
The exception codes defined in the DOM recommendation map to the exceptions described above according to this table:
Constant | Exception
---|---
`DOMSTRING_SIZE_ERR` | [`DomstringSizeErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.DomstringSizeErr "xml.dom.DomstringSizeErr")
`HIERARCHY_REQUEST_ERR` | [`HierarchyRequestErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.HierarchyRequestErr "xml.dom.HierarchyRequestErr")
`INDEX_SIZE_ERR` | [`IndexSizeErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.IndexSizeErr "xml.dom.IndexSizeErr")
`INUSE_ATTRIBUTE_ERR` | [`InuseAttributeErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InuseAttributeErr "xml.dom.InuseAttributeErr")
`INVALID_ACCESS_ERR` | [`InvalidAccessErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidAccessErr "xml.dom.InvalidAccessErr")
`INVALID_CHARACTER_ERR` | [`InvalidCharacterErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidCharacterErr "xml.dom.InvalidCharacterErr")
`INVALID_MODIFICATION_ERR` | [`InvalidModificationErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidModificationErr "xml.dom.InvalidModificationErr")
`INVALID_STATE_ERR` | [`InvalidStateErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.InvalidStateErr "xml.dom.InvalidStateErr")
`NAMESPACE_ERR` | [`NamespaceErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NamespaceErr "xml.dom.NamespaceErr")
`NOT_FOUND_ERR` | [`NotFoundErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotFoundErr "xml.dom.NotFoundErr")
`NOT_SUPPORTED_ERR` | [`NotSupportedErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NotSupportedErr "xml.dom.NotSupportedErr")
`NO_DATA_ALLOWED_ERR` | [`NoDataAllowedErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NoDataAllowedErr "xml.dom.NoDataAllowedErr")
`NO_MODIFICATION_ALLOWED_ERR` | [`NoModificationAllowedErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.NoModificationAllowedErr "xml.dom.NoModificationAllowedErr")
`SYNTAX_ERR` | [`SyntaxErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.SyntaxErr "xml.dom.SyntaxErr")
`WRONG_DOCUMENT_ERR` | [`WrongDocumentErr`](https://docs.python.org/3/library/xml.dom.html#xml.dom.WrongDocumentErr "xml.dom.WrongDocumentErr")
## Conformance[¶](https://docs.python.org/3/library/xml.dom.html#conformance "Link to this heading")
This section describes the conformance requirements and relationships between the Python DOM API, the W3C DOM recommendations, and the OMG IDL mapping for Python.
### Type Mapping[¶](https://docs.python.org/3/library/xml.dom.html#type-mapping "Link to this heading")
The IDL types used in the DOM specification are mapped to Python types according to the following table.
IDL Type | Python Type
---|---
`boolean` | `bool` or `int`
`int` | `int`
`long int` | `int`
`unsigned int` | `int`
`DOMString` | `str` or `bytes`
`null` | `None`
### Accessor Methods[¶](https://docs.python.org/3/library/xml.dom.html#accessor-methods "Link to this heading")
The mapping from OMG IDL to Python defines accessor functions for IDL `attribute` declarations in much the way the Java mapping does. Mapping the IDL declarations
Copy```
readonly attribute string someValue;
         attribute string anotherValue;

```

yields three accessor functions: a “get” method for `someValue` (`_get_someValue()`), and “get” and “set” methods for `anotherValue` (`_get_anotherValue()` and `_set_anotherValue()`). The mapping, in particular, does not require that the IDL attributes are accessible as normal Python attributes: `object.someValue` is _not_ required to work, and may raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
The Python DOM API, however, _does_ require that normal attribute access work. This means that the typical surrogates generated by Python IDL compilers are not likely to work, and wrapper objects may be needed on the client if the DOM objects are accessed via CORBA. While this does require some additional consideration for CORBA DOM clients, the implementers with experience using DOM over CORBA from Python do not consider this a problem. Attributes that are declared `readonly` may not restrict write access in all DOM implementations.
In the Python DOM API, accessor functions are not required. If provided, they should take the form defined by the Python IDL mapping, but these methods are considered unnecessary since the attributes are accessible directly from Python. “Set” accessors should never be provided for `readonly` attributes.
The IDL definitions do not fully embody the requirements of the W3C DOM API, such as the notion of certain objects, such as the return value of `getElementsByTagName()`, being “live”. The Python DOM API does not require implementations to enforce such requirements.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xml.dom` — The Document Object Model API](https://docs.python.org/3/library/xml.dom.html)
    * [Module Contents](https://docs.python.org/3/library/xml.dom.html#module-contents)
    * [Objects in the DOM](https://docs.python.org/3/library/xml.dom.html#objects-in-the-dom)
      * [DOMImplementation Objects](https://docs.python.org/3/library/xml.dom.html#domimplementation-objects)
      * [Node Objects](https://docs.python.org/3/library/xml.dom.html#node-objects)
      * [NodeList Objects](https://docs.python.org/3/library/xml.dom.html#nodelist-objects)
      * [DocumentType Objects](https://docs.python.org/3/library/xml.dom.html#documenttype-objects)
      * [Document Objects](https://docs.python.org/3/library/xml.dom.html#document-objects)
      * [Element Objects](https://docs.python.org/3/library/xml.dom.html#element-objects)
      * [Attr Objects](https://docs.python.org/3/library/xml.dom.html#attr-objects)
      * [NamedNodeMap Objects](https://docs.python.org/3/library/xml.dom.html#namednodemap-objects)
      * [Comment Objects](https://docs.python.org/3/library/xml.dom.html#comment-objects)
      * [Text and CDATASection Objects](https://docs.python.org/3/library/xml.dom.html#text-and-cdatasection-objects)
      * [ProcessingInstruction Objects](https://docs.python.org/3/library/xml.dom.html#processinginstruction-objects)
      * [Exceptions](https://docs.python.org/3/library/xml.dom.html#exceptions)
    * [Conformance](https://docs.python.org/3/library/xml.dom.html#conformance)
      * [Type Mapping](https://docs.python.org/3/library/xml.dom.html#type-mapping)
      * [Accessor Methods](https://docs.python.org/3/library/xml.dom.html#accessor-methods)


#### Previous topic
[`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html "previous chapter")
#### Next topic
[`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/3/library/xml.dom.minidom.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xml.dom+%E2%80%94+The+Document+Object+Model+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxml.dom.html&pagesource=library%2Fxml.dom.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.dom.minidom.html "xml.dom.minidom — Minimal DOM implementation") |
  * [previous](https://docs.python.org/3/library/xml.etree.elementtree.html "xml.etree.ElementTree — The ElementTree XML API") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`xml.dom` — The Document Object Model API](https://docs.python.org/3/library/xml.dom.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
