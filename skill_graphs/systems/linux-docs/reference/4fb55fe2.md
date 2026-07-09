       article PUBLIC "-//OASIS//DTD DocBook XML V4.1.2//EN"
       "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd">
     * The pull-down menu in the File->Save As dialog box for file
       format indicates that the export format is "DocBook
       (simplified)." There is no explanation of what that "simplified"
       indicates. Does OOo export a subset of DocBook? If so, which
       elements are ignored? Is there any way to enter any of them
       manually?
     * There is NO documentation on the DocBook export filter or whether
       OOo will import it again.

   Conclusions: OOo 1.1RC is worth looking at if you want a word
   processor for preparing DocBook documents.

   However, I hope they cure the lack of documentation. For one thing,
   it would be nice to know which native OOo styles map to which DocBook
   elements. It would also be nice to know how to map one's own OOo
   styles to DocBook elements.
     ________________________________________________________________

E.2.2. Open Office 1.1

   [http://www.merlinmonroe.com] Tabatha Marshall offers the following
   additional information for OOo 1.1.

     The first problem was when I tried to do everything on version
     1.0.1. That was obviously a problem. I have RH8, and it was
     installed via rpm packages, so I ripped it out and did a full, new
     install of OpenOffice 1.1. It took a while to find out 1.1 was a
     requirement for XML to work.

     During the install process I believe I was offered the choice to
     install the XML features. I have a tendency to do full installs of
     my office programs, so I selected everything.

     I can't offer any advice to those trying to update their current
     OO 1.1. Their "3 ways" aren't documented very well at the site
     ([http://xml.openoffice.org] xml.openoffice.org) and as of this
     writing, I can't even find THAT on their site anymore. I think
     more current documentation is needed there to walk people through
     the process. Most of this was unclear and I had to pretty much
     experiment to get things working.

     Well, after I installed everything I had some configuration to do.
     I opened the application, and got started by opening a new file,
     choosing templates, then selecting the DocBook template. A nice
     menu of Paragraph Styles popped up for me, which are the names for
     all those tags, I noticed (you can see I don't use WYSIWYG often).

     With a blank doc before me (couldn't get to the XML Filter
     Settings menu unless some type of doc was opened), I went into
     Tools->XML Filter Settings, and edited the entry for DocBook file.
     I configured mine as follows:

     * Doctype -//OASIS//DTD DocBook XML V4.2//EN
     * DTD http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd
     * XSLT for export
       /usr/local/OpenOffice.org1.1.0/share/xslt/docbook/ldp-html.xsl
     * XSLT for import
       /usr/local/OpenOffice.org1.1.0/share/xslt/docbook/docbooktosoffhe
       adings.xsl (this is the default)
     * Template for import
       /home/tabatha/OpenOffice/user/template/DocBook
       File/DocBookTemplate.stw

     At first, if I opened an XML file that had even one parsing error,
     it would just open the file anyway and display the markup in OO. I
     have many XML files that use &copy; and other types of entities
     which show up as parse errors (depending on the encoding) even
     though they can be processed through. But today I was unable to
     open any of those files. I got input/output errors instead. Still
     investigating that one.

     However when you do successfully open a document (one parsing with
     no errors), it puts it automatically into WYSIWYG based on the
     markup, and you can then work from the paragraph styles menu like
     any other such editor.

     To validate the document, I used Tools->XML Filter Settings, then
     clicked the Test XSLTs button. On my screen, I set up the XSLT for
     export to be ldp-html.xsl. If you test and there are errors, a new
     window pops up with error messages at the bottom, and the lines
     that need to be changed up at the top. You can change them there
     and progress through the errors until they're all gone, and keep
     testing until they're gone.

     If you want to open a file to see the source instead of the
     processed results, go to Tools->XML Filter Settings->Test XSLTs,
     and then under the Import section, check the Display Source box.
     My import XSLT is currently docbooktosoffheadings.xsl (the
     default) and the template for import is DocBookTemplate.stw (also
     default).

     I think this might work for some people, but unfortunately not for
     me. I've never used WYSIWYG to edit markup. Emacs with PSGML can
     tell me what my next tag is no matter where I am, validate by
     moving through the trouble spots, and I can parse and process from
     command line.

     With OpenOffice, you have to visit
     [http://xml.openoffice.org/filters.html]
     http://xml.openoffice.org/filters.html to find conversion tools.
     ________________________________________________________________

E.3. Microsoft Word to DocBook

   Even if you want to use MS Word to write your documents, you may find
   [http://www.docsoft.com/w2xmlv2.htm] w2XML useful. Note that this is
   not free software--the cost is around $130USD. There is, however, a
   trial version of the software.
     ________________________________________________________________

E.4. LaTeX to DocBook

   Siep Kroonenberg reports that there is a package tex4ht
   [http://www.cse.ohio-state.edu/~gurari/TeX4ht/]
   http://www.cse.ohio-state.edu/~gurari/TeX4ht/ that converts TeX and
   LaTeX to various flavors of XML. Currently, its support for DocBook
   output is limited. If you want to use tex4ht in its current state for
   LDP you will probably have to hack your LaTeX source beforehand and
   the generated XML afterwards.
     ________________________________________________________________

E.5. LyX to DocBook

   This section is contributed by Chris Karakas.

   You can use the LyX-to-X package to write your document conveniently
   in LyX (a visual editor originally developed as a graphical frontend
   to LaTeX), then export it to DocBook SGML and submit it to The LDP.
   This method is presented by [http://www.karakas-online.de] Chris
   Karakas Document processing with LyX and SGML.

   In the LyX-to-X project, LyX is used as a comfortable graphical SGML
   editor. Once the document is exported to SGML from LyX, it undergoes
   a series of transformations through sed and awk scripts that correct
   the SGML code, computes the Index, inserts the Bibliography and the
   Appendix and takes care of the correct invocation of openjade,
   pdftex, pdfjadetex and all the other necessary programs for the
   generation of HTML (chunked or not), PDF (with images, bookmarks,
   thumbnails and hyperlinks), PS, RTF and TXT versions.

   All aspects of document processing are handled, including automatic
   Index generation, display of Mathematics in TeX quality both online
   and in print formats, as well as the use of bibliographic databases
   with [http://refdb.sourceforge.net/] RefDB. Special care is taken so
   that the document processing is as transparent to the user as
   possible - the aim being that the user writes in LyX, then presses a
   button, and the LyX-to-X script does the rest. Download the
   documentation and the LyX-to-X package from the
   [http://www.karakas-online.de/mySGML/formats.html] Formats section.
     ________________________________________________________________

E.6. DocBook to DocBook Transformations

E.6.1. XML and SGML DocBook

   There are a few changes between DocBook XML and SGML. Handling these
   differences should be relatively easy for most small documents, and
   many authors will not need to make any changes to convert their
   documents other than the XML and DocBook declarations at the start of
   their document.

   For others, here is a list of what you should keep in mind when
   converting your documents from SGML to XML.

   Note Differences between XML and SGML elements


   An XML element typically has three parts: the start tag, the content
   (your words) and the end tag. Qualifiers are added in the start tag
   and are known as attributes. They will always have a name and a
   quoted value.
<filename class="directory">/usr/local<filename>

   The start tag contains one attribute (class) with a value of
   "directory". The end tag (also filename) must not contain any
   attributes.

     * Element names (tags) and their attributes are
       case-dependent--typically lowercase. The following will not
       validate because the end tag <PARA> is uppercase:

<para>This part will fail XML validation</PARA>

     * All attributes in the start tag must be "quoted". This can be
       either single (') or double (") quotes, but not reverse (`) or
       "smart quotes". The quote used to start a name="value" pair must
       be the same quote used at the end of the value. In other words:
       "this" would validate, but 'that" would not.
     * Tags that have a start tag, but no end tag are referred to as
       "empty" because they do not contain (wrap around) anything. These
       tags must still be closed with a trailing slash (/). For example:
       xref must be written as <xref linkend="software"/>. You may not
       have any spaces between the / and >. (Although you may have a
       space after the final attribute: <xref linkend="foo" />.)
     * Processing instructions that get sent to the transformation
       engine (DSSSL or XSLT) and must have a question mark at the end
       of the tag. All processing instructions are removed from the
       output stream. The XML version of this tag would look like this:

<?dbhtml filename="foo"?>

     * If you're converting from SGML to XML, be sure file names refer
       to .xml files instead of .sgml. Some tools may get confused if a
       .sgml file contains XML.
     * Tag minimizations were used in SGML instead of writing out the
       element name in the end tag. Example: <para>This is foo.</> Tag
       minimizations are not supported in XML and their use is
       discouraged in DocBook.
     ________________________________________________________________

E.6.2. Changing DTDs

   The significant changes between version changes in the DTD involve
   changes to the elements (tags). Elements may be: deprecated (which
   means they will be removed in future versions); removed; modified; or
   added. Almost all authors will run into a changed or deprecated tag
   when going from a lower version of DocBook to a higher version.

   DocBook: The Definitive Guide does an excellent job of showing you
   how elements fit together. For each element it tells you what an
   element must contain (its content model) and what is may be contained
   in (who its parents are). For example: a note must contain a para. If
   you try to write <note>Content in a note</note> your document will
   not validate. Learning how elements are assembled will make it a lot
   easier to understand any validation errors that are thrown at you. If
   you get truly stuck you can also email the LDP's docbook mailing list
   for extra hints. Information on subscribing is available from Section
   2.2

   All tags that have been deprecated or changed for 4.x are listed in
   DocBook: The definitive guide, published by O'Reilly and Associates.
   This book is also available on-line from [http://www.docbook.org]
   http://www.docbook.org.
     ________________________________________________________________

E.6.2.1. Differences between version 3.x and 4.x

   Here are a few elements that are of particular relevance to LDP
   authors:

     * artheader. has been changed to articleinfo. Most other header
       elements have been renamed to info.
     * graphic. has been deprecated and will be removed as of DocBook
       5.x. To prepare for this, start using mediaobject. There is more
       information about mediaobject in Section D.5.
     * imagedata. file formats must now be written in UPPERCASE letters.
       If you use lowercase or mixed-case spellings for your file
       formats, it will fail.
       Valid:

<imagedata format="EPS" fileref="foo.eps">

       Invalid:

<imagedata format="eps" fileref="foo.eps">

Glossary

   Abiword
          Open Source word processor.

   aspell
          Spell check program.

   attribute
          An attribute makes available extra information regarding the
          element on which it appears. The attributes always appear as a
          name-value pair on the initialization pointers (i.e. the
          "start tag"). Example of an attribute is id="identification",
          which gives the attribute id the value identification.

   Cascading Style Sheet (CSS)
          Set of overlay rules that are read by your HTML browser, which
          uses these rules for doing the display, layout and formatting
          of the XML-generated HTML file(s). CSS allows for fast changes
          in look and feel without having to plunge in the HTML file(s).

   Catalog
          Helper file for the display and transformation tools, which
          maps public identifiers and URLs to the local file system.

   Concurrent Versions System (CVS)
          A common document management system used by the LDP.

   DocBook
          An SGML (and XML) application, describing a document format
          that allows easy management of documentation.

   docbook-utils
          Software package easing XML conversions.

   Document Type Definition (DTD)
          A group of statements that define element names and their
          attributes specifying the rules for combinations and
          sequences. It's the DTD that defines which elements can or
          cannot be inserted in the given context.

   DSSSL
          DSSSL stands for Document Style Semantics and Specification
          Language. It's an ISO standard (ISO/IEC 10179:1996). The DSSSL
          standard is internationally used as a language for documents
          style sheets pages for SGML.

   element
          The elements describe the content's structure in a document.
          Most elements contain a start tag, content and a closing tag.
          For example a paragraph element includes all of the following
          <para>This is the paragraph.</para>. Some elements are "empty"
          and do not contain content and a closing tag. An example of
          this is a link to an external document where the URL is
          printed to the page. This element would include only the
          following <ulink url="http://google.com/>.

   Emacs
          Popular text editor, especially on UNIX systems or alike.

   entity
          An entity is a name designated for some part of data so that
          it can be referenced by a name. The data could be anything
          from from simple characters to chapters to sets of statements
          in a DTD. Entity parameters can be generic, external, internal
          or SGML data. An entity is similar to a variable in a
          programming language, or a macro.

   epcEdit
          Cross-platform XML editor.

   external entity
          An external entity points to an external document. External
          entities are used to include texts on certain locations of a
          SGML document. It could be used to include sample screens,
          legal notes, and chapters for example.

   float
          Objects such as side bars, pictures, tables, and charts are
          called floats when they don't have a fixed placement on the
          text. For printed text, a chart can appear either at the top
          or at the bottom of the page. It can also be placed on the
          next page if it is too large.

   Frequently Asked Questions (FAQ)
          LDP hosts a number of documents that are a list in the form of
          questions and answers. These documents are called FAQs. A FAQ
          is usually a single-page document.

   generic entities
          An entity referenced by a name, which starts with "&" and ends
          with semicolon is a generic entity. Most of the time this type
          of entity is used in the document and not on the DTD. There
          are two types of entities: external and internal. They can
          refer to special characters or to text objects such as
          repeated sentences, names or chapters.

   GNU Free Documentation License (GFDL)
          Like the GNU Public License for free software, but with
          specifics for written text and documentation with software.

   GNU Public License (GPL)
          License type for software that guarantees that the software
          remains freely distributable, that the source code is
          available, that you can make changes to it and redistribute
          those changes if you want, on the condition that you keep on
          using the same license for your derived works.

   Guide
          TLDP documents that are too long to be a HOWTO are usually
          stored as guides. These are more like entire books that treat
          a particular subject in-dept.

   HOWTO
          Documents that discuss how to do something with a system or
          application. Most documents hosted at TLDP are HOWTOs,
          explaining how to install, configure or manage tens of
          applications on a variety of systems. HOWTOs are typically
          10-25 pages.

   internal entity
          An internal entity refers to part of the text and is often
          used as a shortcut for frequently repeated text.

   ispell
          Spell check program.

   Jade
          An application which applies the rules defined in a DSSSL
          style sheet to an SGML or XML document, transforming the
          document into the desired output.

   Markup, markup language (ML)
          Code added to the content of a document, describing its
          structure.

   Metadata
          Text in your document that is not important for understanding
          the subject, but that should be there anyway, such as version
          information, co-authors, credits to people etc.

   nedit
          Text editor oriented to programmers.

   nsgmls, onsgmls
          SGML document parser and validator program.

   OpenOffice (OOo)
          Open Source office suite, compatible with Microsoft Office.

   parameter entity
          An entity type often used in the DTD or a document's internal
          subset. The entity's name starts with a percent sign (%) and
          ends with a semicolon.

   PSGML
          Emacs major mode that customizes Emacs for editing SGML
          documents.

   Organization for the Advancement of Structured Information Standards
          (OASIS)
          OASIS is a non-profit, global consortium that drives the
          development, convergence and adoption of e-business standards.

   Outline
          Draft of your document that conceptualizes the subject and
          scope. Summary and To-Do list for the work to come.

   Portable Document Format (PDF)
          Standard document type supported on a wide range of operating
          systems.

   processing instruction
          A processing instruction is a command passed to the document
          formatting tool. It starts with "<?". This document uses
          processing instructions for naming files when it is rendered
          into HTML: <?dbhtml filename="file.html">

   PostScript (PS)
          Document format designed for printable documents. PS is the
          standard print format on UNIX(-alike).

   Reviewer, review process
          TLDP doesn't accept just anything. Once you submit a document,
          it will be checked for consistency, grammar, spelling and
          style by a reviewer, a volunteer assigned by the review
          coordinator.

   SGML
          Standard Generalized Markup Language. It is an international
          standard (ISO8879) that specifies rules for the creation of
          electronic documents in markup systems, regardless of the
          platform used.

   Subject and scope
          Obviously, the subject is what your documentation is about.
          The scope defines which areas of the subject you are going to
          discuss, and how much detail will be involved.

   tag
          An SGML element bounded by the marks "<" and ">". Tags are
          used to mark the semantic or logical structure of a document.
          A sample is the tag <title> to mark the beginning of a title.

   TeX
          Popular UNIX text formatting and typesetting tool.

   Transformation
          The process of converting a document from its original DocBook
          XML form to another format, such as PDF, HTML or PostScript.

   Validation
          The process of checking your XML code to ensure it complies
          with the XML DTD you declared at the top of your document.

   vi Improved (vIm)
          Popular text editor on UNIX and alike systems.

   WordPerfect (WP)
          Popular word processor, runs on many systems.

   XML
          eXtensible Markup Language. A sub-product of SGML created
          specifically for Internet use.

   xmllint
          Command line XML parser and validator.

   XMLmind XML Editor (XXE)
          Free but not Open XML editor.

   xmlto
          Command line XML transformation program.

   XSL
          XML Style Language. XSL is to a XML document what a DSSSL
          style is for a SGML document. The XSL is written in XML.

   Extensible Stylesheet Transformation (XSLT)
          Framework for managing documents, consisting of the XSLT
          transformation language, the XPath expression language and XSL
          formatting objects.
     ________________________________________________________________

Appendix F. GNU Free Documentation License

F.1. 0. PREAMBLE

   The purpose of this License is to make a manual, textbook, or other
   written document "free" in the sense of freedom: to assure everyone
   the effective freedom to copy and redistribute it, with or without
   modifying it, either commercially or noncommercially. Secondarily,
   this License preserves for the author and publisher a way to get
   credit for their work, while not being considered responsible for
   modifications made by others.

   This License is a kind of "copyleft", which means that derivative
   works of the document must themselves be free in the same sense. It
   complements the GNU General Public License, which is a copyleft
   license designed for free software.

   We have designed this License in order to use it for manuals for free
   software, because free software needs free documentation: a free
   program should come with manuals providing the same freedoms that the
   software does. But this License is not limited to software manuals;
   it can be used for any textual work, regardless of subject matter or
   whether it is published as a printed book. We recommend this License
   principally for works whose purpose is instruction or reference.
     ________________________________________________________________

F.2. 1. APPLICABILITY AND DEFINITIONS

   This License applies to any manual or other work that contains a
   notice placed by the copyright holder saying it can be distributed
   under the terms of this License. The "Document", below, refers to any
   such manual or work. Any member of the public is a licensee, and is
   addressed as "you".

   A "Modified Version" of the Document means any work containing the
   Document or a portion of it, either copied verbatim, or with
   modifications and/or translated into another language.

   A "Secondary Section" is a named appendix or a front-matter section
   of the Document that deals exclusively with the relationship of the
   publishers or authors of the Document to the Document's overall
   subject (or to related matters) and contains nothing that could fall
   directly within that overall subject. (For example, if the Document
   is in part a textbook of mathematics, a Secondary Section may not
   explain any mathematics.) The relationship could be a matter of
   historical connection with the subject or with related matters, or of
   legal, commercial, philosophical, ethical or political position
   regarding them.

   The "Invariant Sections" are certain Secondary Sections whose titles
   are designated, as being those of Invariant Sections, in the notice
   that says that the Document is released under this License.

   The "Cover Texts" are certain short passages of text that are listed,
   as Front-Cover Texts or Back-Cover Texts, in the notice that says
   that the Document is released under this License.

   A "Transparent" copy of the Document means a machine-readable copy,
   represented in a format whose specification is available to the
   general public, whose contents can be viewed and edited directly and
   straightforwardly with generic text editors or (for images composed
   of pixels) generic paint programs or (for drawings) some widely
   available drawing editor, and that is suitable for input to text
   formatters or for automatic translation to a variety of formats
   suitable for input to text formatters. A copy made in an otherwise
   Transparent file format whose markup has been designed to thwart or
   discourage subsequent modification by readers is not Transparent. A
