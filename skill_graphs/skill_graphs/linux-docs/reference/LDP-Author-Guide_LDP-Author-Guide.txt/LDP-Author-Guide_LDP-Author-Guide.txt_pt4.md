   legalities of changing a project's license. It suggests new practice
   for coping with today's high-threat legal environment--this part is a
   must-read for all project leaders.

   --Eric Raymond and Catherine Raymond

   OPL, [http://www.opencontent.org/openpub/]
   http://www.opencontent.org/openpub/.

   OpenContent officially closed June 30, 2003.

   Creative Commons, [http://creativecommons.org/licenses/by-sa/1.0/]
   http://creativecommons.org/licenses/by-sa/1.0/.

   GNU Free Documentation License,
   [http://www.gnu.org/copyleft/fdl.html]
   http://www.gnu.org/copyleft/fdl.html.

   GNU General Public License,
   [http://www.gnu.org/licenses/licenses.html#GPL]
   http://www.gnu.org/licenses/licenses.html#GPL.

   If you would like your documents to be included in the main Debian
   distribution, you should use this license. It is not, however, the
   LDP's license of choice.
     ________________________________________________________________

Appendix A. Templates

   The LDP stores its documents in the following markup languages:

    1. DocBook XML version 4.2 (preferred), 4.1.2
    2. DocBook SGML version 4.2, 4.1, or 3.x
    3. LinuxDoc SGML

   Note New Documents


   A new document may be submitted to the LDP in any format. Documents
   which are not in DocBook or LinuxDoc will be converted by a
   volunteer. The author is responsible for adding markup to any
   revisions which are made.
     ________________________________________________________________

A.1. Document Templates

    1. HOWTO (Article) [templates/ldp-howto.zip]
       templates/ldp-howto.zip. Most HOWTO documents will use this
       template.
    2. Guide (Book) [templates/ldp-guide.zip] templates/ldp-guide.zip.
       Use this template to create a full book (like this Author Guide,
       for instance). Templates provided by Tille Garrels.
    3. FAQ [templates/ldp-faq.zip] templates/ldp-faq.zip. A standard
       article for writing a FAQ (Frequently Asked Questions) list.
    4. LinuxDoc[templates/ldp-linuxdoc.zip] templates/ldp-linuxdoc.zip.
       A standard template both in HOWTO length and Guide length.
    5. Disclaimer [disclaimer.xml] disclaimer.xml. A standard disclaimer
       which warns readers that (1) your document may not be perfect and
       (2) you are not responsible if things end up broken because of
       it.
     ________________________________________________________________

A.2. Style Sheets

   The following style sheets can be used to make your document nicer to
   look at. Remember that the LDP will use its own style sheets to
   distribute your documentation.

    1. DSL Style Sheet [style.dsl] style.dsl. This DSL style sheet was
       provided by Tille and is to be used with DSSSL transformations.
    2. Cascading Style Sheet [style-ob.css] style-ob.css. This CSS file
       was provided by Saqib Ali and Emma Jane Hogbin. The "ob" is for
       "orange and blue". Use this CSS file with an HTML file.
       Instructions are included in the CSS file.
     ________________________________________________________________

A.3. GNU Free Documentation License

   The GFDL (GNU Free Documentation License) is available in XML format
   at [http://www.gnu.org/licenses/fdl.xml]
   http://www.gnu.org/licenses/fdl.xml. For a version in appendix format
   suitable for including in your document, you can see get the XML for
   this document from CVS at
   [http://cvsview.tldp.org/index.cgi/LDP/guide/docbook/LDP-Author-Guide
   /fdl-appendix.xml]
   http://cvsview.tldp.org/index.cgi/LDP/guide/docbook/LDP-Author-Guide/
   fdl-appendix.xml.

   TLDP template files for DocBook (XML and SGML) and Linuxdoc SGML are
   available from the TLDP website at
   [http://www.tldp.org/authors/index.html#resources]
   http://www.tldp.org/authors/index.html#resources.
     ________________________________________________________________

Appendix B. System Setup: Editors, Validation and Transformations

   In this section, we will cover some of the tools that you may want to
   use to create your own LDP documentation. If you use some other tool
   to assist you in writing documents for the LDP, please drop us a line
   and we'll add a blurb for it here. Section 1.3 has contact
   information.
     ________________________________________________________________

B.1. Tools for your operating system

   A few notes on setting up your system for DocBook publishing. These
   tools focus more on the transformation of documents from DocBook to
   XHTML (for example).

   Tools For Your Operating System

   Debian
          http://www.docbook.org/wiki/moin.cgi/DebianGnuLinuxPackages

          [http://www.surgo.net] Morgon Kanter suggests apt-get install
          docbook-xml docbook-xsl xsltproc as the minimum requirements.
          [http://lists.tldp.org/index.cgi?1:mss:4851]
          http://lists.tldp.org/index.cgi?1:mss:4851

   Fedora (aka the new RedHat)
          Notes contributed by Charles Curley.

          Tools for Docbook SGML and XML are included in the
          distribution. So are Emacs and PSGML mode, although you will
          have to customize your .emacs. If you are missing a package
          after installing Fedora, get familiar with yum or apt.

          Installation instructions: none; use Red Hat 9 until they are
          written:
          [http://www.redhat.com/docs/manuals/linux/RHL-9-Manual/]
          http://www.redhat.com/docs/manuals/linux/RHL-9-Manual/.

   Mandrake
          Notes contributed by [http://www.artemio.net] Artemio.

          In Mandrake (as of my current 9.2), all the stuff including
          openjade, xmlto, docbook-utils etc. comes as standard.

          So I just needed to get the TLDP XSL sheet and that's all.
          Didn't ever have any dependency or other problems, everything
          works fine (knock on wood :-)).

   RedHat
          According to Hal Burgiss, your system is likely already ready
          to edit and process DocBook documents without installing any
          additional packages.
     ________________________________________________________________

B.2. Editing tools

   Editing tools have come a long way in their support for XML (and
   specifically DocBook). There are two types of editors outlined in
   this section: text editors (emacs, vim, etc); and word processors
   (OpenOffice, AbiWord, etc). New authors who are not comfortable
   working with markup languages should probably choose a word processor
   that can output DocBook files. For this reason the word processors
   are listed first.

   Although many editors can also validate your DocBook files, this
   information has been separated into Section B.3.

   Note More info


   Check the resources section for more .
     ________________________________________________________________

B.2.1. Word Processors

   Even if you are not comfortable working DocBook's tagset in a text
   editor you can still produce valid DocBook documents using a word
   processor. Support at this point is very limited, but it does exist
   in the following programs. The up side, of course, is that things
   like spell check are built in to the program. In addition to this,
   support for DocBook (and XML) is constantly improving.

   Note Converting Microsoft Word documents


   Even if you want to use MS Word to write your documents, you may find
   [http://www.docsoft.com/w2xmlv2.htm] w2XML useful. Note that this is
   not free software--the cost is around $130USD. There is, however, a
   trial version of the software.

   Note Work on the content!


   Remember that all formatting changes you make to your document will
   be ignored when your document is released by the LDP. Instead of
   focusing on how your document looks, focus on the content.
     ________________________________________________________________

B.2.1.1. AbiWord

   Through word of mouth I've heard that AbiWord can work (natively)
   with DocBook documents. This will need to be tested by someone
   (possibly me) and should definitely be included if it is the case.
     ________________________________________________________________

B.2.1.2. OpenOffice.org

   [http://openoffice.org] http://openoffice.org

   As of OpenOffice.org (OOo) 1.1RC there has been support for exporting
   files to DocBook format.

   Although OOo uses the full DocBook document type declaration, it does
   not actually export the full list of DocBook elements. It uses a
   "simplified" DocBook tagset which is geared to on-the-fly rendering.
   (Although it is not the official Simplified DocBook which is
   described in Section B.5.) The OpenOffice simplified (or "special"
   docbook) is available from
   [http://xml.openoffice.org/xmerge/docbook/supported_tag_table.html]
   http://xml.openoffice.org/xmerge/docbook/supported_tag_table.html.
     ________________________________________________________________

B.2.1.2.1. Open Office 1.0.x

   OOo has been tested by LDP volunteers with mostly positive results.
   Thanks to Charles Curley ([http://www.charlescurley.com]
   charlescurley.com) for the following notes on using OOo version
   1.0.x:

   Note Check the version of your OpenOffice


   These notes may not apply to the version of OOo you are using.

     * To be able to export to DocBook, you must have a Java runtime
       environment (JRE) installed and registered with OOo--a minimum of
       version 4.2.x is recommended. The configuration instructions will
       depend on how you installed your JRE. Visit the OOo web site for
       help with your setup.
       Contrary to the OOo documentation, the Linux OOo did not come
       with a JRE. I got one from Sun.
     * The exported file has lots of empty lines. My 54 line exported
       file had 5 lines of actual XML code.
     * There was no effort at pretty printing.
     * The header is: <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE
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

B.2.1.2.2. Open Office 1.1

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

B.2.1.3. WordPerfect 9 (Corel Office 2000)

   [http://www.corel.com/] http://www.corel.com/

   WordPerfect 9 for the MS Windows platform has support for SGML and
   DocBook 3.0. WordPerfect 9 for Linux has no SGML capabilities.

   If you are using WordPerfect on the Linux operating system, please
   read: WordPerfect on Linux FAQ
     ________________________________________________________________

B.2.1.4. XMLmind's XML editor

   [http://www.xmlmind.com/xmleditor/] http://www.xmlmind.com/xmleditor/

   Although strictly speaking, it is not a word processor, XMLmind's XML
   editor allows authors to concentrate on the content, and not the
   markup. It has built in spelling and conversion utilities which allow
   you to transform your documents without having to install and
   configure an additional processing tool such as jade. There is a free
   "standard edition", which is a simplified version of their
   "professional edition."
     ________________________________________________________________

B.2.1.5. Conglomerate

   [http://www.conglomerate.org] http://www.conglomerate.org

   According to their web site, "Conglomerate aims to be an XML editor
   that everyone can use. In particular, our primary goal is to create
   the ultimate editor for DocBook and similar formats. It aims to hide
   the jargon and complexity of XML and present the information in your
   documents in a way that makes sense."
     ________________________________________________________________

B.2.1.6. Vex: a visual editor for XML

   [http://vex.sourceforge.net/] http://vex.sourceforge.net/

   According to their web site, "The visual part comes from the fact
   that Vex hides the raw XML tags from the user, providing instead a
   wordprocessor-like interface. Because of this, Vex is best suited for
   document-style XML documents such as XHTML and DocBook rather than
   data-style XML documents."
     ________________________________________________________________

B.2.2. Text Editors

   Caution For advanced writers


   The tools outlined in this section allow you to work with the DocBook
   tags directly. If you are not comfortable working with markup
   languages you may want to use a word processor instead. Word
   processors that support DocBook are described in Section B.2.1.

   If you are comfortable working with markup languages and text
   editors, you'll probably want to customize your current editor of
   choice to handle DocBook files. Below are some of the more common
   text editors that can, with some tweaking, handle DocBook files.
     ________________________________________________________________

B.2.2.1. Emacs (PSGML)

   http://www.lysator.liu.se/~lenst/about_psgml/

   Emacs has an SGML writing mode called psgml that is a major mode
   designed for editing SGML and XML documents. It provides:

     * "syntax highlighting" or "pretty printing" features that make the
       tags stand out
     * a way to insert tags other than typing them by hand
     * and the ability to validate your document while writing

   For users of Emacs, it's a great way to go. PSGML works with DocBook,
   LinuxDoc and other DTDs equally well.
     ________________________________________________________________

B.2.2.1.1. Verifying PSGML is Installed

   If you have installed a recent distribution, you may already have
   PSGML installed for use with Emacs. To check, start Emacs and look
   for the PSGML documentation (C-himpsgml).

   Tip Dependencies


   If you don't have PSGML installed now might be a good time to upgrade
   Emacs. The rest of these instructions will assume you have PSGML
   installed.
     ________________________________________________________________

B.2.2.1.2. Configuring Emacs for Use With PSGML

   If you want GNU Emacs to enter PSGML mode when you open an .xml file,
   it will need to be able to find the DocBook DTD files. If your
   distribution already had PSGML set up for use with GNU Emacs, you
   probably won't need to do anything.

   Note Tuning Emacs


   For more information on how to configure Emacs, check out .

   Once you've configured your system to use PSGML you will need to
   override Emacs' default sgml-mode with the psgml-mode. This can be
   done by configuring your .emacs file. After you've edited the
   configuration file you will need to restart Emacs.
     ________________________________________________________________

B.2.2.1.3. Creating New DocBook XML Files

   There are a number of steps to creating a new DocBook XML file in
   Emacs.

     * Create a new file with an xml extension.
     * On the first line of the file enter the doctype for the version
       of DocBook that you would like to use. If you're not sure what a
       doctype is all about, check Section B.5
     * Enter C-c C-p. If Emacs manages to parse your DTD, you will see
       Parsing prolog...done in the minibuffer.
     * Enter C-c C-e Enter to auto-magically insert the parent element
       for your document. (New authors are typically writing articles.)
     * If things are working correctly, you should see new tags for the
       parent element for your document right after the document type
       declaration. In other words you should now see two extra tags:
       <article> and </article> in your document.
     ________________________________________________________________

B.2.2.1.4. Spell Checking in Emacs

   Emacs can be configured to use aspell by adding the following to your
   ~/.emacs file. Thanks to [http://www.ertius.org] Rob Weir for this
   configuration information.
;; Use aspell
(setq-default ispell-program-name "aspell")
;;Setup some dictionary languages
(setq ispell-dictionary "british")
(setq flyspell-default-dictionary "british")
     ________________________________________________________________

B.2.2.2. epcEdit

   [http://www.tksgml.de/] http://www.tksgml.de

   The epcEdit program allows you to edit XML files. It has the
   advantages of not needing to know Emacs or vi before starting, and is
   cross-platform, working in both Windows and Linux. This is a
   commercial application, and pricing can be found at
   [http://www.tksgml.de/pricing.html] http://www.tksgml.de/pricing.html

   Along with visual editing, epcEdit will also validate documents on
   loading, and on demand by using the Document->Validate command.

   Figure B-1. epcEdit screen shot

   [sgeditscreenshot.jpg]
     ________________________________________________________________

B.2.2.3. Morphon XML editor

   [http://www.morphon.com/xmleditor/index.shtml]
   http://www.morphon.com/xmleditor/index.shtml

   This is a commercial application which is currently available for
   free (with an optional user registration). It is written in Java,
   allowing it to run on any platform that has a Java Virtual Machine
   (that is, works in both Windows and Linux).

   On the plus sides of XMLEditor is the left side of the screen shows
   the hierarchy of the document (starting with Book and so on).
   Selecting an item in the list brings you to that part of the document
   so you can edit it. The right part of the screen shows the text
   without any markup or tags being shown. If you have external files as
   ELEMENTS (as the LDP Author Guide does), XMLEditor will follow the
   links and load the files, so you always work on the entire work. On
   the minus side of this, you will get errors if a file is missing.
     ________________________________________________________________

B.2.2.4. nedit

   [http://nedit.org] http://nedit.org

   To be fair, nedit is more for programmers, so it might seem a bit of
   overkill for new users and especially non-programmers. All that
   aside, it's extremely powerful, allowing for syntax highlighting.
   Unlike epcEdit, nedit doesn't allow you to automatically insert tags
   or automatically validate your code. However, it does allow for shell
   commands to be run against the contents of the window (as opposed to
   saving the file, then checking).

   Figure B-2. nedit screen shot

   [neditscreenshot.jpg]
     ________________________________________________________________

B.2.2.4.1. Using nedit

   When you open your DocBook file, nedit should already have syntax
   highlighting enabled. If it does not you can turn it on explicitly
   using: Preferences->Language Mode->SGML HTML

   If you have line numbers turned on (using Preferences->Show Line
   Numbers) then finding validation errors is much simpler. nsgmls, the
   validation tool we'll use, lists errors by their line number.
     ________________________________________________________________

B.2.2.4.2. Configuring nedit

   Since you can feed the contents of your window to outside programs,
   you can easily extend nedit to perform repetitive functions. The
   example you'll see here is to validate your document using nsgmls.
   For more information about nsgmls and validating documents please
   read Section B.3.

     * Select Preferences->Default Settings->Customize Menus->Shell
       Menu.... This will bring up the Shell Command dialog box, with
       all the shell commands nedit has listed under the Shell menu.
     * Under Menu Entry, enter "Validate DocBook." This will be the
       entry you'll see on the screen.
     * Under Accelerator, press Alt-S. Once this menu item is set up,
       you can press Alt-S to have the Validate DocBook automatically
       run.
     * Under Command Input, select window, and under Command Output,
       select dialog.
     * Under Command to Execute, enter nsgmls -sv. Using -v outputs the
       version number is output to the screen so that you know the
       command has run.

       Note Check the PATH


   Note that nsgmls has to be in your PATH for this to work properly.

   Figure B-3. Adding shell commands to nedit

   [neditshellcommand.jpg]

     * Click OK and you'll now be back at the main nedit screen. Load up
       an XML file, and select Shell->Validate DocBook or press Alt-S.
     * The nedit program will fire up and check the contents of the
       window.
     * If all you see is a version number for nsgml then your document
       is valid. Any errors are reported by line number in your
       document.

   Figure B-4. nsgmls output on success

   [neditsuccess.jpg]
     ________________________________________________________________

B.2.2.5. VIM

   [http://www.vim.org] http://www.vim.org
