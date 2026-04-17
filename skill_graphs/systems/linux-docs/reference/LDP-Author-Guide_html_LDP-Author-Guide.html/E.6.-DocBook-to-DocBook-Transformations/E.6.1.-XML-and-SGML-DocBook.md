##  E.6.1. XML and SGML DocBook
There are a few changes between DocBook XML and SGML. Handling these differences should be relatively easy for most small documents, and many authors will not need to make any changes to convert their documents other than the XML and DocBook declarations at the start of their document.
For others, here is a list of what you should keep in mind when converting your documents from SGML to XML.
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Differences between XML and SGML elements**
---|---
|  An XML element typically has three parts: the start tag, the content (your words) and the end tag. Qualifiers are added in the start tag and are known as attributes. They will always have a name and a quoted value. | ```

<filename class="directory">/usr/local<filename>

```

---
The start tag contains one attribute (class) with a value of "directory". The end tag (also filename) must not contain any attributes.
  * Element names (tags) and their attributes are case-dependent--typically lowercase. The following will not validate because the end tag <PARA> is uppercase:
```

<para>This part will fail XML validation</PARA>

```

---
  * All attributes in the start tag must be "quoted". This can be either single (') or double (") quotes, but not reverse (`) or "smart quotes". The quote used to start a name="value" pair must be the same quote used at the end of the value. In other words: "this" would validate, but 'that" would not.
  * Tags that have a start tag, but no end tag are referred to as "empty" because they do not contain (wrap around) anything. These tags must still be closed with a trailing slash (/). For example: `xref` must be written as <xref linkend="software"/>. You may not have any spaces between the / and >. (Although you may have a space after the final attribute: <xref linkend="foo" />.)
  * Processing instructions that get sent to the transformation engine (DSSSL or XSLT) and must have a question mark at the end of the tag. All processing instructions are removed from the output stream. The XML version of this tag would look like this:
```

<?dbhtml filename="foo"?>

```

---
  * If you're converting from SGML to XML, be sure file names refer to .xml files instead of .sgml. Some tools may get confused if a .sgml file contains XML.
  * Tag minimizations were used in SGML instead of writing out the element name in the end tag. Example: `<para>`This is foo.`</>` Tag minimizations are not supported in XML and their use is discouraged in DocBook.


* * *
##  E.6.2. Changing DTDs
The significant changes between version changes in the DTD involve changes to the elements (tags). Elements may be: deprecated (which means they will be removed in future versions); removed; modified; or added. Almost all authors will run into a changed or deprecated tag when going from a lower version of DocBook to a higher version.
_DocBook: The Definitive Guide_ does an excellent job of showing you how elements fit together. For each element it tells you what an element must contain (its content model) and what is may be contained in (who its parents are). For example: a `note` must contain a `para`. If you try to write <note>Content in a note</note> your document will not validate. Learning how elements are assembled will make it a lot easier to understand any validation errors that are thrown at you. If you get truly stuck you can also email the LDP's docbook mailing list for extra hints. Information on subscribing is available from [Section 2.2](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#mailinglists)
All tags that have been deprecated or changed for 4.x are listed in _DocBook: The definitive guide_ , published by O'Reilly and Associates. This book is also available on-line from
* * *
###  E.6.2.1. Differences between version 3.x and 4.x
Here are a few elements that are of particular relevance to LDP authors:
  * **`artheader`. **has been changed to `articleinfo`. Most other header elements have been renamed to info.
  * **`graphic`. **has been deprecated and will be removed as of DocBook 5.x. To prepare for this, start using `mediaobject`. There is more information about `mediaobject` in [Section D.5](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#inserting-pictures).
  * **`imagedata`. **file formats must now be written in UPPERCASE letters. If you use lowercase or mixed-case spellings for your file formats, it will fail.
Valid:
```

<imagedata format="EPS" fileref="foo.eps">

```

---
Invalid:
```

<imagedata format="eps" fileref="foo.eps">

```

---


#  Glossary

**Abiword**

Open Source word processor.

**aspell**

Spell check program.

**attribute**

An attribute makes available extra information regarding the element on which it appears. The attributes always appear as a name-value pair on the initialization pointers (i.e. the "start tag"). Example of an attribute is `_id="identification"_` , which gives the attribute `_id_` the value `_identification_`.

**Cascading Style Sheet ( CSS)**

Set of overlay rules that are read by your HTML browser, which uses these rules for doing the display, layout and formatting of the XML-generated HTML file(s). CSS allows for fast changes in look and feel without having to plunge in the HTML file(s).

**Catalog**

Helper file for the display and transformation tools, which maps public identifiers and URLs to the local file system.

**Concurrent Versions System ( CVS)**

A common document management system used by the LDP.

**DocBook**

An SGML (and XML) application, describing a document format that allows easy management of documentation.

**docbook-utils**

Software package easing XML conversions.

**Document Type Definition ( DTD)**

A group of statements that define element names and their attributes specifying the rules for combinations and sequences. It's the DTD that defines which elements can or cannot be inserted in the given context.

**DSSSL**

DSSSL stands for Document Style Semantics and Specification Language. It's an ISO standard (ISO/IEC 10179:1996). The DSSSL standard is internationally used as a language for documents style sheets pages for SGML.

**element**

The elements describe the content's structure in a document. Most elements contain a start tag, content and a closing tag. For example a paragraph element includes all of the following `<para>`This is the paragraph.`</para>`. Some elements are "empty" and do not contain content and a closing tag. An example of this is a link to an external document where the URL is printed to the page. This element would include only the following `<ulink url="http://google.com/>`.

**Emacs**

Popular text editor, especially on UNIX systems or alikes.

**entity**

An entity is a name designated for some part of data so that it can be referenced by a name. The data could be anything from from simple characters to chapters to sets of statements in a DTD. Entity parameters can be generic, external, internal or SGML data. An entity is similar to a variable in a programming language, or a macro.

**epcEdit**

Cross-platform XML editor.

**external entity**

An external entity points to an external document. External entities are used to include texts on certain locations of a SGML document. It could be used to include sample screens, legal notes, and chapters for example.

**float**

Objects such as side bars, pictures, tables, and charts are called floats when they don't have a fixed placement on the text. For printed text, a chart can appear either at the top or at the bottom of the page. It can also be placed on the next page if it is too large.

**Frequently Asked Questions ( FAQ)**

LDP hosts a number of documents that are a list in the form of questions and answers. These documents are called FAQs. A FAQ is usually a single-page document.

**generic entities**

An entity referenced by a name, which starts with "&" and ends with semicolon is a generic entity. Most of the time this type of entity is used in the document and not on the DTD. There are two types of entities: external and internal. They can refer to special characters or to text objects such as repeated sentences, names or chapters.

**GNU Free Documentation License ( GFDL)**

Like the GNU Public License for free software, but with specifics for written text and documentation with software.

**GNU Public License ( GPL)**

License type for software that guarantees that the software remains freely distributable, that the source code is available, that you can make changes to it and redistribute those changes if you want, on the condition that you keep on using the same license for your derived works.

**Guide**

TLDP documents that are too long to be a HOWTO are usually stored as guides. These are more like entire books that treat a particular subject in-dept.

**HOWTO**

Documents that discuss how to do something with a system or application. Most documents hosted at TLDP are HOWTOs, explaining how to install, configure or manage tens of applications on a variety of systems. HOWTOs are typically 10-25 pages.

**internal entity**

An internal entity refers to part of the text and is often used as a shortcut for frequently repeated text.

**ispell**

Spell check program.

**Jade**

An application which applies the rules defined in a DSSSL style sheet to an SGML or XML document, transforming the document into the desired output.

**Markup, markup language ( ML)**

Code added to the content of a document, describing its structure.

**Metadata**

Text in your document that is not important for understanding the subject, but that should be there anyway, such as version information, co-authors, credits to people etc.

**nedit**

Text editor oriented to programmers.

**nsgmls, onsgmls**

SGML document parser and validator program.

**OpenOffice ( OOo)**

Open Source office suite, compatible with Microsoft Office.

**parameter entity**

An entity type often used in the DTD or a document's internal subset. The entity's name starts with a percent sign (%) and ends with a semicolon.

**PSGML**

Emacs _major mode_ that customizes Emacs for editing SGML documents.

**Organization for the Advancement of Structured Information Standards ( OASIS)**

OASIS is a non-profit, global consortium that drives the development, convergence and adoption of e-business standards.

**Outline**

Draft of your document that conceptualizes the subject and scope. Summary and To-Do list for the work to come.

**Portable Document Format ( PDF)**

Standard document type supported on a wide range of operating systems.

**processing instruction**

A processing instruction is a command passed to the document formatting tool. It starts with "<?". This document uses processing instructions for naming files when it is rendered into HTML: `<?dbhtml filename="file.html">`

**PostScript ( PS)**

Document format designed for printable documents. PS is the standard print format on UNIX(-alikes).

**Reviewer, review process**

TLDP doesn't accept just anything. Once you submit a document, it will be checked for consistency, grammar, spelling and style by a reviewer, a volunteer assigned by the review coordinator.

**SGML**

_Standard Generalized Markup Language_. It is an international standard (ISO8879) that specifies rules for the creation of electronic documents in markup systems, regardless of the platform used.

**Subject and scope**

Obviously, the subject is what your documentation is about. The scope defines which areas of the subject you are going to discuss, and how much detail will be involved.

**tag**

An SGML element bounded by the marks "<" and ">". Tags are used to mark the semantic or logical structure of a document. A sample is the tag _`< title>`_ to mark the beginning of a title.

**TeX**

Popular UNIX text formatting and typesetting tool.

**Transformation**

The process of converting a document from its original DocBook XML form to another format, such as PDF, HTML or PostScript.

**Validation**

The process of checking your XML code to ensure it complies with the XML DTD you declared at the top of your document.

**vi Improved ( vIm)**

Popular text editor on UNIX and alike systems.

**WordPerfect ( WP)**

Popular word processor, runs on many systems.

**XML**

eXtensible Markup Language. A sub-product of SGML created specifically for Internet use.

**xmllint**

Command line XML parser and validator.

**XMLmind XML Editor ( XXE)**

Free but not Open XML editor.

**xmlto**

Command line XML transformation program.

**XSL**

XML Style Language. XSL is to a XML document what a DSSSL style is for a SGML document. The XSL is written in XML.

**Extensible Stylesheet Transformation ( XSLT)**

Framework for managing documents, consisting of the XSLT transformation language, the XPath expression language and XSL formatting objects.
* * *
#  Appendix F. GNU Free Documentation License
#  F.1. 0. PREAMBLE
The purpose of this License is to make a manual, textbook, or other written document "free" in the sense of freedom: to assure everyone the effective freedom to copy and redistribute it, with or without modifying it, either commercially or noncommercially. Secondarily, this License preserves for the author and publisher a way to get credit for their work, while not being considered responsible for modifications made by others.
This License is a kind of "copyleft", which means that derivative works of the document must themselves be free in the same sense. It complements the GNU General Public License, which is a copyleft license designed for free software.
We have designed this License in order to use it for manuals for free software, because free software needs free documentation: a free program should come with manuals providing the same freedoms that the software does. But this License is not limited to software manuals; it can be used for any textual work, regardless of subject matter or whether it is published as a printed book. We recommend this License principally for works whose purpose is instruction or reference.
* * *
#  F.2. 1. APPLICABILITY AND DEFINITIONS
This License applies to any manual or other work that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. The "Document", below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you".
A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.
A "Secondary Section" is a named appendix or a front-matter section of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (For example, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical or political position regarding them.
The "Invariant Sections" are certain [ Secondary Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-secondary) whose titles are designated, as being those of Invariant Sections, in the notice that says that the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) is released under this License.
The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) is released under this License.
A "Transparent" copy of the [ Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) means a machine-readable copy, represented in a format whose specification is available to the general public, whose contents can be viewed and edited directly and straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup has been designed to thwart or discourage subsequent modification by readers is not Transparent. A copy that is not "Transparent" is called "Opaque".
Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML designed for human modification. Opaque formats include PostScript, PDF, proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML produced by some word processors for output purposes only.
The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.
* * *
#  F.3. 2. VERBATIM COPYING
You may copy and distribute the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) in any medium, either commercially or noncommercially, provided that this License, the copyright notices, and the license notice saying this License applies to the Document are reproduced in all copies, and that you add no other conditions whatsoever to those of this License. You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute. However, you may accept compensation in exchange for copies. If you distribute a large enough number of copies you must also follow the conditions in [section 3](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section3).
You may also lend copies, under the same conditions stated above, and you may publicly display copies.
* * *
#  F.4. 3. COPYING IN QUANTITY
If you publish printed copies of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) numbering more than 100, and the Document's license notice requires [Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts), you must enclose the copies in covers that carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly and legibly identify you as the publisher of these copies. The front cover must present the full title with all words of the title equally prominent and visible. You may add other material on the covers in addition. Copying with changes limited to the covers, as long as they preserve the title of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) and satisfy these conditions, can be treated as verbatim copying in other respects.
If the required texts for either cover are too voluminous to fit legibly, you should put the first ones listed (as many as fit reasonably) on the actual cover, and continue the rest onto adjacent pages.
If you publish or distribute [Opaque](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-transparent) copies of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) numbering more than 100, you must either include a machine-readable [Transparent](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-transparent) copy along with each Opaque copy, or state in or with each Opaque copy a publicly-accessible computer-network location containing a complete Transparent copy of the Document, free of added material, which the general network-using public has access to download anonymously at no charge using public-standard network protocols. If you use the latter option, you must take reasonably prudent steps, when you begin distribution of Opaque copies in quantity, to ensure that this Transparent copy will remain thus accessible at the stated location until at least one year after the last time you distribute an Opaque copy (directly or through your agents or retailers) of that edition to the public.
It is requested, but not required, that you contact the authors of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) well before redistributing any large number of copies, to give them a chance to provide you with an updated version of the Document.
* * *
#  F.5. 4. MODIFICATIONS
You may copy and distribute a [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified) of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) under the conditions of sections [2](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section2) and [3](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section3) above, provided that you release the Modified Version under precisely this License, with the Modified Version filling the role of the Document, thus licensing distribution and modification of the Modified Version to whoever possesses a copy of it. In addition, you must do these things in the Modified Version:
  * **A.** Use in the [Title Page](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-title-page) (and on the covers, if any) a title distinct from that of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document), and from those of previous versions (which should, if there were any, be listed in the History section of the Document). You may use the same title as a previous version if the original publisher of that version gives permission.
  * **B.** List on the [Title Page](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-title-page), as authors, one or more persons or entities responsible for authorship of the modifications in the [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified), together with at least five of the principal authors of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) (all of its principal authors, if it has less than five).
  * **C.** State on the [Title Page](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-title-page) the name of the publisher of the [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified), as the publisher.
  * **D.** Preserve all the copyright notices of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document).
  * **E.** Add an appropriate copyright notice for your modifications adjacent to the other copyright notices.
  * **F.** Include, immediately after the copyright notices, a license notice giving the public permission to use the [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified) under the terms of this License, in the form shown in the Addendum below.
  * **G.** Preserve in that license notice the full lists of [ Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) and required [Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts) given in the [Document's](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) license notice.
  * **H.** Include an unaltered copy of this License.
  * **I.** Preserve the section entitled "History", and its title, and add to it an item stating at least the title, year, new authors, and publisher of the [Modified Version ](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified)as given on the [Title Page](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-title-page). If there is no section entitled "History" in the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document), create one stating the title, year, authors, and publisher of the Document as given on its Title Page, then add an item describing the Modified Version as stated in the previous sentence.
  * **J.** Preserve the network location, if any, given in the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) for public access to a [Transparent](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-transparent) copy of the Document, and likewise the network locations given in the Document for previous versions it was based on. These may be placed in the "History" section. You may omit a network location for a work that was published at least four years before the Document itself, or if the original publisher of the version it refers to gives permission.
  * **K.** In any section entitled "Acknowledgements" or "Dedications", preserve the section's title, and preserve in the section all the substance and tone of each of the contributor acknowledgements and/or dedications given therein.
  * **L.** Preserve all the [Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document), unaltered in their text and in their titles. Section numbers or the equivalent are not considered part of the section titles.
  * **M.** Delete any section entitled "Endorsements". Such a section may not be included in the [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified).
  * **N.** Do not retitle any existing section as "Endorsements" or to conflict in title with any [Invariant Section](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant).


If the [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified) includes new front-matter sections or appendices that qualify as [Secondary Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-secondary) and contain no material copied from the Document, you may at your option designate some or all of these sections as invariant. To do this, add their titles to the list of [Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) in the Modified Version's license notice. These titles must be distinct from any other section titles.
You may add a section entitled "Endorsements", provided it contains nothing but endorsements of your [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified) by various parties--for example, statements of peer review or that the text has been approved by an organization as the authoritative definition of a standard.
You may add a passage of up to five words as a [Front-Cover Text](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts), and a passage of up to 25 words as a [Back-Cover Text](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts), to the end of the list of [Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts) in the [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified). Only one passage of Front-Cover Text and one of Back-Cover Text may be added by (or through arrangements made by) any one entity. If the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) already includes a cover text for the same cover, previously added by you or by arrangement made by the same entity you are acting on behalf of, you may not add another; but you may replace the old one, on explicit permission from the previous publisher that added the old one.
The author(s) and publisher(s) of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) do not by this License give permission to use their names for publicity for or to assert or imply endorsement of any [Modified Version ](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified).
* * *
#  F.6. 5. COMBINING DOCUMENTS
You may combine the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) with other documents released under this License, under the terms defined in [section 4](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section4) above for modified versions, provided that you include in the combination all of the [Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) of all of the original documents, unmodified, and list them all as Invariant Sections of your combined work in its license notice.
The combined work need only contain one copy of this License, and multiple identical [Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) may be replaced with a single copy. If there are multiple Invariant Sections with the same name but different contents, make the title of each such section unique by adding at the end of it, in parentheses, the name of the original author or publisher of that section if known, or else a unique number. Make the same adjustment to the section titles in the list of Invariant Sections in the license notice of the combined work.
In the combination, you must combine any sections entitled "History" in the various original documents, forming one section entitled "History"; likewise combine any sections entitled "Acknowledgements", and any sections entitled "Dedications". You must delete all sections entitled "Endorsements."
* * *
#  F.7. 6. COLLECTIONS OF DOCUMENTS
You may make a collection consisting of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) and other documents released under this License, and replace the individual copies of this License in the various documents with a single copy that is included in the collection, provided that you follow the rules of this License for verbatim copying of each of the documents in all other respects.
You may extract a single document from such a collection, and distribute it individually under this License, provided you insert a copy of this License into the extracted document, and follow this License in all other respects regarding verbatim copying of that document.
* * *
#  F.8. 7. AGGREGATION WITH INDEPENDENT WORKS
A compilation of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) or its derivatives with other separate and independent documents or works, in or on a volume of a storage or distribution medium, does not as a whole count as a [Modified Version](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-modified) of the Document, provided no compilation copyright is claimed for the compilation. Such a compilation is called an "aggregate", and this License does not apply to the other self-contained works thus compiled with the Document , on account of their being thus compiled, if they are not themselves derivative works of the Document. If the [Cover Text](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts) requirement of [section 3](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section3) is applicable to these copies of the Document, then if the Document is less than one quarter of the entire aggregate, the Document's Cover Texts may be placed on covers that surround only the Document within the aggregate. Otherwise they must appear on covers around the whole aggregate.
* * *
#  F.9. 8. TRANSLATION
Translation is considered a kind of modification, so you may distribute translations of the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) under the terms of [section 4](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section4). Replacing [ Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) with translations requires special permission from their copyright holders, but you may include translations of some or all Invariant Sections in addition to the original versions of these Invariant Sections. You may include a translation of this License provided that you also include the original English version of this License. In case of a disagreement between the translation and the original English version of this License, the original English version will prevail.
* * *
#  F.10. 9. TERMINATION
You may not copy, modify, sublicense, or distribute the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) except as expressly provided for under this License. Any other attempt to copy, modify, sublicense or distribute the Document is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.
* * *
#  F.11. 10. FUTURE REVISIONS OF THIS LICENSE
The
Each version of the License is given a distinguishing version number. If the [Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-document) specifies that a particular numbered version of this License "or any later version" applies to it, you have the option of following the terms and conditions either of that specified version or of any later version that has been published (not as a draft) by the Free Software Foundation. If the Document does not specify a version number of this License, you may choose any version ever published (not as a draft) by the Free Software Foundation.
* * *
#  F.12. Addendum
To use this License in a document you have written, include a copy of the License in the document and put the following copyright and license notices just after the title page:
> Copyright � YEAR YOUR NAME.
> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with the [Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant) being LIST THEIR TITLES, with the [Front-Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts) being LIST, and with the [Back-Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts) being LIST. A copy of the license is included in the section entitled "GNU Free Documentation License".
If you have no [Invariant Sections](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-invariant), write "with no Invariant Sections" instead of saying which ones are invariant. If you have no [Front-Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts), write "no Front-Cover Texts" instead of "Front-Cover Texts being LIST"; likewise for [Back-Cover Texts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-cover-texts).
If your document contains nontrivial examples of program code, we recommend releasing these examples in parallel under your choice of free software license, such as the
### Notes
[[1]](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN127) | Please, take a look at the [ source](http://cvsview.tldp.org/index.cgi/LDP/guide/docbook/LDP-Author-Guide/) to see how to get similar results on your documents. You should also remember that the way this appears to you depends on the format in which you are reading this document: online appearance is slightly different from the PostScript or PDF ones.
---|---
[[2]](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN2259) | In truth, "XSL" is actually comprised of three components: the _XSLT_ transformation language, the _XPath_ expression language (used by XSLT), and XSL Formatting Objects (FO) that are used for describing a page. The style sheets are actually written in XSLT and generate either HTML or (for print output) FO. The FO file is then run through a FO processor to create the actual print (PDF or PostScript) output. See the
[[3]](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN2280) | In XSL terminology, the process of generating multiple files is referred to as "chunking".
