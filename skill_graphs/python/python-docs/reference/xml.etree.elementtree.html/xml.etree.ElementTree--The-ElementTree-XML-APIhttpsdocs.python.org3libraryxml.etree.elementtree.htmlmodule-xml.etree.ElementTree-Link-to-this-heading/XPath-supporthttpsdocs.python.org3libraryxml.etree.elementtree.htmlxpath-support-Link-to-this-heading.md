## XPath support[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support "Link to this heading")
This module provides limited support for
### Example[¶](https://docs.python.org/3/library/xml.etree.elementtree.html#example "Link to this heading")
Here’s an example that demonstrates some of the XPath capabilities of the module. We’ll be using the `countrydata` XML document from the [Parsing XML](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-parsing-xml) section:
Copy```
import xml.etree.ElementTree as ET

root = ET.fromstring(countrydata)
