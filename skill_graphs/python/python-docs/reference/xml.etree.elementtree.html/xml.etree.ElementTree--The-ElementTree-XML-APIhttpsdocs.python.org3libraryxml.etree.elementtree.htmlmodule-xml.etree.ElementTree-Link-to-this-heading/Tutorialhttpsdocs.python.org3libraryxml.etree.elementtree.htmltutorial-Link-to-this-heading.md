## Tutorial[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#tutorial "Link to this heading")
This is a short tutorial for using `xml.etree.ElementTree` (`ET` in short). The goal is to demonstrate some of the building blocks and basic concepts of the module.
### XML tree and elements[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xml-tree-and-elements "Link to this heading")
XML is an inherently hierarchical data format, and the most natural way to represent it is with a tree. `ET` has two classes for this purpose - [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") represents the whole XML document as a tree, and [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") represents a single node in this tree. Interactions with the whole document (reading and writing to/from files) are usually done on the `ElementTree` level. Interactions with a single XML element and its sub-elements are done on the `Element` level.
### Parsing XML[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml "Link to this heading")
We’ll be using the fictive `country_data.xml` XML document as the sample data for this section:
```
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

```

We can import this data by reading from a file:
Copy```
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

```

Or directly from a string:
Copy```
root = ET.fromstring(country_data_as_string)

```

[`fromstring()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstring "xml.etree.ElementTree.fromstring") parses XML from a string directly into an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element"), which is the root element of the parsed tree. Other parsing functions may create an [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree"). Check the documentation to be sure.
As an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element"), `root` has a tag and a dictionary of attributes:
Copy```
>>> root.tag
'data'
>>> root.attrib
{}

```

It also has children nodes over which we can iterate:
Copy```
>>> for child in root:
...     print(child.tag, child.attrib)
...
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}

```

Children are nested, and we can access specific child nodes by index:
Copy```
>>> root[0][1].text
'2008'

```

Note
Not all elements of the XML input will end up as elements of the parsed tree. Currently, this module skips over any XML comments, processing instructions, and document type declarations in the input. Nevertheless, trees built using this module’s API rather than parsing from XML text can have comments and processing instructions in them; they will be included when generating XML output. A document type declaration may be accessed by passing a custom [`TreeBuilder`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder "xml.etree.ElementTree.TreeBuilder") instance to the [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") constructor.
### Pull API for non-blocking parsing[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#pull-api-for-non-blocking-parsing "Link to this heading")
Most parsing functions provided by this module require the whole document to be read at once before returning any result. It is possible to use an [`XMLParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser") and feed data into it incrementally, but it is a push API that calls methods on a callback target, which is too low-level and inconvenient for most needs. Sometimes what the user really wants is to be able to parse XML incrementally, without blocking operations, while enjoying the convenience of fully constructed [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") objects.
The most powerful tool for doing this is [`XMLPullParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser "xml.etree.ElementTree.XMLPullParser"). It does not require a blocking read to obtain the XML data, and is instead fed with data incrementally with [`XMLPullParser.feed()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.feed "xml.etree.ElementTree.XMLPullParser.feed") calls. To get the parsed XML elements, call [`XMLPullParser.read_events()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.read_events "xml.etree.ElementTree.XMLPullParser.read_events"). Here is an example:
Copy```
>>> parser = ET.XMLPullParser(['start', 'end'])
>>> parser.feed('<mytag>sometext')
>>> list(parser.read_events())
[('start', <Element 'mytag' at 0x7fa66db2be58>)]
>>> parser.feed(' more text</mytag>')
>>> for event, elem in parser.read_events():
...     print(event)
...     print(elem.tag, 'text=', elem.text)
...
end
mytag text= sometext more text

```

The obvious use case is applications that operate in a non-blocking fashion where the XML data is being received from a socket or read incrementally from some storage device. In such cases, blocking reads are unacceptable.
Because it’s so flexible, [`XMLPullParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser "xml.etree.ElementTree.XMLPullParser") can be inconvenient to use for simpler use-cases. If you don’t mind your application blocking on reading XML data but would still like to have incremental parsing capabilities, take a look at [`iterparse()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse "xml.etree.ElementTree.iterparse"). It can be useful when you’re reading a large XML document and don’t want to hold it wholly in memory.
Where _immediate_ feedback through events is wanted, calling method [`XMLPullParser.flush()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.flush "xml.etree.ElementTree.XMLPullParser.flush") can help reduce delay; please make sure to study the related security notes.
### Finding interesting elements[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#finding-interesting-elements "Link to this heading")
[`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") has some useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on). For example, [`Element.iter()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iter "xml.etree.ElementTree.Element.iter"):
Copy```
>>> for neighbor in root.iter('neighbor'):
...     print(neighbor.attrib)
...
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}

```

[`Element.findall()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findall "xml.etree.ElementTree.Element.findall") finds only elements with a tag which are direct children of the current element. [`Element.find()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.find "xml.etree.ElementTree.Element.find") finds the _first_ child with a particular tag, and [`Element.text`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.text "xml.etree.ElementTree.Element.text") accesses the element’s text content. [`Element.get()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.get "xml.etree.ElementTree.Element.get") accesses the element’s attributes:
Copy```
>>> for country in root.findall('country'):
...     rank = country.find('rank').text
...     name = country.get('name')
...     print(name, rank)
...
Liechtenstein 1
Singapore 4
Panama 68

```

More sophisticated specification of which elements to look for is possible by using [XPath](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath).
### Modifying an XML File[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#modifying-an-xml-file "Link to this heading")
[`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") provides a simple way to build XML documents and write them to files. The [`ElementTree.write()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write "xml.etree.ElementTree.ElementTree.write") method serves this purpose.
Once created, an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") object may be manipulated by directly changing its fields (such as [`Element.text`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.text "xml.etree.ElementTree.Element.text")), adding and modifying attributes ([`Element.set()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.set "xml.etree.ElementTree.Element.set") method), as well as adding new children (for example with [`Element.append()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.append "xml.etree.ElementTree.Element.append")).
Let’s say we want to add one to each country’s rank, and add an `updated` attribute to the rank element:
Copy```
>>> for rank in root.iter('rank'):
...     new_rank = int(rank.text) + 1
...     rank.text = str(new_rank)
...     rank.set('updated', 'yes')
...
>>> tree.write('output.xml')

```

Our XML now looks like this:
```
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

```

We can remove elements using [`Element.remove()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.remove "xml.etree.ElementTree.Element.remove"). Let’s say we want to remove all countries with a rank higher than 50:
Copy```
>>> for country in root.findall('country'):
...     # using root.findall() to avoid removal during traversal
...     rank = int(country.find('rank').text)
...     if rank > 50:
...         root.remove(country)
...
>>> tree.write('output.xml')

```

Note that concurrent modification while iterating can lead to problems, just like when iterating and modifying Python lists or dicts. Therefore, the example first collects all matching elements with `root.findall()`, and only then iterates over the list of matches.
Our XML now looks like this:
```
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
</data>

```

### Building XML documents[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#building-xml-documents "Link to this heading")
The [`SubElement()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.SubElement "xml.etree.ElementTree.SubElement") function also provides a convenient way to create new sub-elements for a given element:
Copy```
>>> a = ET.Element('a')
>>> b = ET.SubElement(a, 'b')
>>> c = ET.SubElement(a, 'c')
>>> d = ET.SubElement(c, 'd')
>>> ET.dump(a)
<a><b /><c><d /></c></a>

```

### Parsing XML with Namespaces[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces "Link to this heading")
If the XML input has `prefix:sometag` get expanded to `{uri}sometag` where the _prefix_ is replaced by the full _URI_. Also, if there is a
Here is an XML example that incorporates two namespaces, one with the prefix “fictional” and the other serving as the default namespace:
```
<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>

```

One way to search and explore this XML example is to manually add the URI to every tag or attribute in the xpath of a [`find()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.find "xml.etree.ElementTree.Element.find") or [`findall()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.findall "xml.etree.ElementTree.Element.findall"):
Copy```
root = fromstring(xml_text)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)

```

A better way to search the namespaced XML example is to create a dictionary with your own prefixes and use those in the search functions:
Copy```
ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)

```

These two approaches both output:
Copy```
John Cleese
 |--> Lancelot
 |--> Archie Leach
Eric Idle
 |--> Sir Robin
 |--> Gunther
 |--> Commander Clement

```
