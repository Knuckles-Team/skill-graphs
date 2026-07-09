##  E.2.1. Open Office 1.0.x
OOo has been tested by LDP volunteers with mostly positive results. Thanks to Charles Curley (
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Check the version of your OpenOffice**
---|---
|  These notes may not apply to the version of OOo you are using.
  * To be able to export to DocBook, you must have a Java runtime environment (JRE) installed and registered with OOo--a minimum of version 4.2.x is recommended. The configuration instructions will depend on how you installed your JRE. Visit the OOo web site for help with your setup.
Contrary to the OOo documentation, the Linux OOo did not come with a JRE. I got one from Sun.
  * The exported file has lots of empty lines. My 54 line exported file had 5 lines of actual XML code.
  * There was no effort at pretty printing.
  * The header is: ` <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.1.2//EN" "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd"> `
  * The pull-down menu in the File->Save As dialog box for file format indicates that the export format is "DocBook (simplified)." There is no explanation of what that "simplified" indicates. Does OOo export a subset of DocBook? If so, which elements are ignored? Is there any way to enter any of them manually?
  * There is NO documentation on the DocBook export filter or whether OOo will import it again.


Conclusions: OOo 1.1RC is worth looking at if you want a word processor for preparing DocBook documents.
However, I hope they cure the lack of documentation. For one thing, it would be nice to know which native OOo styles map to which DocBook elements. It would also be nice to know how to map one's own OOo styles to DocBook elements.
* * *
