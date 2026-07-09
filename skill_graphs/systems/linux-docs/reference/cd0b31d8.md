##  E.2.2. Open Office 1.1
> The first problem was when I tried to do everything on version 1.0.1. That was obviously a problem. I have RH8, and it was installed via rpm packages, so I ripped it out and did a full, new install of OpenOffice 1.1. It took a while to find out 1.1 was a requirement for XML to work.
> During the install process I believe I was offered the choice to install the XML features. I have a tendency to do full installs of my office programs, so I selected everything.
> I can't offer any advice to those trying to update their current OO 1.1. Their "3 ways" aren't documented very well at the site (
> Well, after I installed everything I had some configuration to do. I opened the application, and got started by opening a new file, choosing templates, then selecting the DocBook template. A nice menu of Paragraph Styles popped up for me, which are the names for all those tags, I noticed (you can see I don't use WYSIWYG often).
> With a blank doc before me (couldn't get to the XML Filter Settings menu unless some type of doc was opened), I went into Tools->XML Filter Settings, and edited the entry for DocBook file. I configured mine as follows:
>   * Doctype `**-//OASIS//DTD DocBook XML V4.2//EN**`
>   * DTD `**http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd**`
>   * XSLT for export `**/usr/local/OpenOffice.org1.1.0/share/xslt/docbook/ldp-html.xsl**`
>   * XSLT for import `**/usr/local/OpenOffice.org1.1.0/share/xslt/docbook/docbooktosoffheadings.xsl**` (this is the default)
>   * Template for import `**/home/tabatha/OpenOffice/user/template/DocBook File/DocBookTemplate.stw**`
>

> At first, if I opened an XML file that had even one parsing error, it would just open the file anyway and display the markup in OO. I have many XML files that use &copy; and other types of entities which show up as parse errors (depending on the encoding) even though they can be processed through. But today I was unable to open any of those files. I got input/output errors instead. Still investigating that one.
> However when you do successfully open a document (one parsing with no errors), it puts it automatically into WYSIWYG based on the markup, and you can then work from the paragraph styles menu like any other such editor.
> To validate the document, I used Tools->XML Filter Settings, then clicked the Test XSLTs button. On my screen, I set up the XSLT for export to be `ldp-html.xsl`. If you test and there are errors, a new window pops up with error messages at the bottom, and the lines that need to be changed up at the top. You can change them there and progress through the errors until they're all gone, and keep testing until they're gone.
> If you want to open a file to see the source instead of the processed results, go to Tools->XML Filter Settings->Test XSLTs, and then under the Import section, check the Display Source box. My import XSLT is currently `docbooktosoffheadings.xsl` (the default) and the template for import is `DocBookTemplate.stw` (also default).
> I think this might work for some people, but unfortunately not for me. I've never used WYSIWYG to edit markup. Emacs with PSGML can tell me what my next tag is no matter where I am, validate by moving through the trouble spots, and I can parse and process from command line.
> With OpenOffice, you have to visit
* * *
