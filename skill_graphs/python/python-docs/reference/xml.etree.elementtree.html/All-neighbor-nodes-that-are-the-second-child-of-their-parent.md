# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")

```

For XML with namespaces, use the usual qualified `{namespace}tag` notation:
Copy```
# All dublin-core "title" tags in the document
root.findall(".//{http://purl.org/dc/elements/1.1/}title")

```

### Supported XPath syntax[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#supported-xpath-syntax "Link to this heading")
Syntax | Meaning
---|---
`tag` |  Selects all child elements with the given tag. For example, `spam` selects all child elements named `spam`, and `spam/egg` selects all grandchildren named `egg` in all children named `spam`. `{namespace}*` selects all tags in the given namespace, `{*}spam` selects tags named `spam` in any (or no) namespace, and `{}*` only selects tags that are not in a namespace. Changed in version 3.8: Support for star-wildcards was added.
`*` | Selects all child elements, including comments and processing instructions. For example, `*/egg` selects all grandchildren named `egg`.
`.` | Selects the current node. This is mostly useful at the beginning of the path, to indicate that it’s a relative path.
`//` | Selects all subelements, on all levels beneath the current element. For example, `.//egg` selects all `egg` elements in the entire tree.
`..` | Selects the parent element. Returns `None` if the path attempts to reach the ancestors of the start element (the element `find` was called on).
`[@attrib]` | Selects all elements that have the given attribute.
`[@attrib='value']` | Selects all elements for which the given attribute has the given value. The value cannot contain quotes.
`[@attrib!='value']` |  Selects all elements for which the given attribute does not have the given value. The value cannot contain quotes. Added in version 3.10.
`[tag]` | Selects all elements that have a child named `tag`. Only immediate children are supported.
`[.='text']` |  Selects all elements whose complete text content, including descendants, equals the given `text`. Added in version 3.7.
`[.!='text']` |  Selects all elements whose complete text content, including descendants, does not equal the given `text`. Added in version 3.10.
`[tag='text']` | Selects all elements that have a child named `tag` whose complete text content, including descendants, equals the given `text`.
`[tag!='text']` |  Selects all elements that have a child named `tag` whose complete text content, including descendants, does not equal the given `text`. Added in version 3.10.
`[position]` | Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression `last()` (for the last position), or a position relative to the last position (e.g. `last()-1`).
Predicates (expressions within square brackets) must be preceded by a tag name, an asterisk, or another predicate. `position` predicates must be preceded by a tag name.
