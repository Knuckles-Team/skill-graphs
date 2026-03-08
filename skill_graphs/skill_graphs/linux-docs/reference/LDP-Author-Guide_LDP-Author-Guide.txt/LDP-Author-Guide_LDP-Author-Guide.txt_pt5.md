
   No mention of text editors is complete without talking about vi. The
   VIM (Vi IMproved) editor has the functionality of regular vi and
   includes "syntax highlighting" of tags.
     ________________________________________________________________

B.2.2.5.1. Getting Started

   There are many versions of vi. New authors will likely want one of
   the more feature-packed versions for syntax highlighting and a
   graphical interface including mouse control.

   Red Hat users will want the following packages: vim-common,
   vim-minimal and vim-enhanced. Debian users will want the following
   package: vim. For an X interface (including GUI menus and mouse
   control) users will want gvim. The "g" in gvim is for "Graphical".

   VIM compiles very easy should you need to build your own. Both vim
   and gvim are built by default. Syntax highlighting is included but
   not enabled by default if you have to start from scratch; use the
   :syntax enable command in VIM to turn this feature on.
     ________________________________________________________________

B.2.2.5.2. Creating New DocBook XML Files

   In both vim and gvim, .xml files will be recognized and enter into
   "SGML mode". A series of known DocBook tags and attributes have been
   entered into vim and will be highlighted one color if the name is
   known and another if it is not (for this author the colors are yellow
   and blue).

   Having the correct document type declaration at the top of your
   document should add the syntax highlighting. If you do not see this
   highlighting you will need to force VIM into SGML mode (even for XML
   files) using the command :set ft=sgml. If you are working with
   multiple files for a single XML document you can add your document
   type in <-- comments --> to the top of the file to get the correct
   syntax highlighting (you will need to restart the program to see the
   change in highlighting). The top line of this file
   (tools-text-editors.xml) looks like this:

<!-- <!DOCTYPE book PUBLIC '-//OASIS//DTD DocBook XML V4.2//EN'> -->

     ________________________________________________________________

B.2.2.5.3. Spell Check

   As in Emacs, Vim, will work quite happily with aspell. It can be run
   from within Vim with the following: :! aspell -c %.

   For more sophisticated spell check alternatives, give
   [http://cream.sourceforge.net/] Cream or
   [http://www.vim.org/scripts/script_search_results.php?keywords=vimspe
   ll&script_type=&order_by=rating&direction=descending&search=search]
   vimspell a try.
     ________________________________________________________________

B.2.2.5.4. Tag Completion

   The following information is provided by
   [http://www.digitalhermit.com] Kwan Lowe.

   Vim has a DocBook helper script which can be easily copied into your
   .vimscripts directory and used to "auto complete" tags while writing
   DocBook documents. The script can be downloaded from:
   [http://www.vim.org/scripts/script.php?script_id=38]
   http://www.vim.org/scripts/script.php?script_id=38.

     Grab the file, then untar it. Copy the dbhelper.vim to your
     .vimscripts directory if you have one.

        $ mkdir .vimscripts
        $ cp dbhelper.vim .vimscripts

     You'll also have to convert the dbhelper.vim file to unix
     formatting:

        $ dos2unix dbhelper.vim

     Next, edit your .vimrc file and add the line: source
     /home/yourname/.vimscripts/dbhelper.vim

     To use the scripts, enter vi and go into insert mode. Press ,
     (comma) followed by the shortcut. For example: ,dtbk
     ________________________________________________________________

B.2.2.6. XMLForm

   [http://www.datamech.com/XMLForm/] http://www.datamech.com/XMLForm/

   This web-based application allows you to put in the URL for XML
   source, or copy and paste the XML directly into the web form. The
   application then breaks down your document into a series of form
   fields that hide the DocBook tags so that you may edit the content
   directly. Version 5 is available from
   [http://www.datamech.com/XMLForm/formGenerator5.html]
   http://www.datamech.com/XMLForm/formGenerator5.html. This application
   is best on shorter documents (less than 20 pages printed).

   As this is an on-line tool, it will be good for small updates only.
     ________________________________________________________________

B.2.2.7. XMLmind XML Editor (XXE)

   [http://www.xmlmind.com/xmleditor] http://www.xmlmind.com/xmleditor

   David Horton offers the following information:

     I am a big fan of XMLMind's XXE editor and XFC FO converter. It is
     "free as in beer," but not necessarily "free as in speech." Very
     liberal license for personal use however. It's Java-based so it
     works on all sorts of OS's.
     ________________________________________________________________

B.3. Validation

B.3.1. Why Validate Your Document

   The LDP uses a number of scripts to distribute your document. These
   scripts submit your document to the LDP's CVS (a free document
   version management system), and then they transform your document to
   other formats that users then read. Your document will also be
   mirrored on a number of sites worldwide (yet another set of scripts).

   In order for these scripts to work correctly, your document must be
   both "well formed" and use "valid markup". Well formed means your
   document follows the rules that XML is expecting: it complies with
   XML grammar rules. Valid markup means you only use elements or tags
   which are "valid" for your document: XML vocabulary rules are
   applied.

   If your document is not well formed or uses invalid markup, the
   scripts will not be able to process it. As a result, your revised
   document will not be distributed.

   Note The Docbook Section


   There is more information about how to validate your document in the
   DocBook section. Check out Section B.3 for more help with validating
   your document.
     ________________________________________________________________

B.3.2. Validation for the Faint of Heart

   Your life is already hard enough without having to install a full set
   of tools just to see if you validate as well. You can upload your raw
   XML files to a web site, then go to [http://validate.sf.net]
   http://validate.sf.net, enter the URL to your document, then validate
   it.

   Note External entities


   When this information was added to the Author Guide external entities
   were not supported. Follow the instructions provided on the Validate
   site if you have trouble.
     ________________________________________________________________

B.3.3. Validation for the Not So Faint Of Heart
     ________________________________________________________________

B.3.3.1. Catalogs

   XML and SGML files contain most of the information you need; however,
   there are sometimes entities which are specific to SGML in general.
   To match these entities to their actual values you need to use a
   catalog. The role of a catalog is to tell your system where to find
   the files it is looking for. You may want to think of a catalog as a
   guide book (or a map) for your tools.

   Most distributions (Red Hat/Fedora and Debian at least) have a common
   location for the main SGML catalog file, called /etc/sgml/catalog. In
   times past, it could also be found in /usr/lib/sgml/catalog.

   The structure of XML catalog files is not the same as SGML catalog
   files. The section on tailoring a catalog (see Section B.3.4) will
   give more details about what these files actually contain.

   If your system cannot find the catalog file, or you are using custom
   catalog files, you may need to set the SGML_CATALOG_FILES and
   XML_CATALOG_FILES environment variables. Using echo
   $SGML_CATALOG_FILES, check to see if it is currently set. If a blank
   line is returned, the variable has not been set. Use the same command
   to see if XML_CATALOG_FILES is set as well. If the variables are not
   set, use the following example to set them now.

   Example B-1. Setting the SGML_CATALOG_FILES and XML_CATALOG_FILES
   Environmental Variables

   bash$ export SGML_CATALOG_FILES="/etc/sgml/catalog"

   To make this change permanent, you can add the following lines to
   your ~/.bashrc file.
SGML_CATALOG_FILES="/etc/sgml/catalog"
export SGML_CATALOG_FILES

   If you installed XML tools via a RedHat or Debian package, you
   probably don't need to do this step. If you are using a custom XML
   catalog you will definitely need to do this. There is more on custom
   catalogs in the next section. To ensure my backup scripts grab this
   custom file, I have added mine in a sub-directory of my home
   directory named "docbook".

   bash$ export XML_CATALOG_FILES="/home/user/docbook/db-catalog.xml"

   You can also change your .bashrc if you want to save these changes.
XML_CATALOG_FILES="/home/user/docbook/db-catalog.xml"
export XML_CATALOG_FILES

   If you are adding the changes to your .bashrc you will not see the
   changes until you open a new terminal window. To make the changes
   immediate in the current terminal, "source" the configuration file.
     ________________________________________________________________

B.3.4. Creating and modifying catalogs

   In the previous section I mentioned a catalog is like a guide book
   for your tools. Specifically, a catalog maps the rules from the
   public identifier to your system's files.

   At the top of every DocBook (or indeed every XML) file there is a
   DOCTYPE which tells the processing tool what kind of document it is
   about to be processed. At a minimum this declaration will include a
   public identifier, such as -//OASIS//DTD DocBook V4.2//EN. This
   public identifier has a number of sections all separated by //. It
   contains the following information: ISO standard if any (- -- in this
   case there is no ISO standard), author (OASIS), type of document (DTD
   DocBook V4.2), language (English). Your DOCTYPE may also include a
   URL.

   A public identifier is useless to a processing tool, as it needs to
   be able to access the actual DTD. A URL is useless if the processing
   tool is off-line. To help your processor deal with these problems you
   can download all of the necessary files and then "map" them for your
   processing tools by using a catalog.

   If you are using SGML processing tools (for instance Jade), you will
   need an SGML catalog. If you are using XML processing tools (like
   XSLT), you will need an XML catalog. Information on both is included.
     ________________________________________________________________

B.3.4.1. SGML Catalogs

   Example B-2. Example of an SGML catalog
                                                            (1)
-- Catalog for the Conectiva Styles --

OVERRIDE YES
                                                           (2)
PUBLIC "-//Conectiva SA//DTD DocBook Conectiva variant V1.0//EN"
                        "/home/ldp/styles/books.dtd"

DELEGATE "-//OASIS"
                "/home/ldp/SGML/dtds/catalog.dtd"
                                                           (3)
DOCTYPE BOOK /home/ldp/SGML/dtds/docbook/db31/docbook.dtd

-- EOF --

   (1)
          Comment. Comments start with "--" and follow to the end of the
          line.
   (2)
          The public type association "-//Conectiva SA//DTD books
          V1.0//EN" with the file books.dtd on the directory
          /home/ldp/styles.
   (3)
          Comment signifying the end of the file.

   As in the example above, to associate an identifier to a file just
   follow the sequence shown:

    1. Copy the identifier PUBLIC
    2. Type the identifying text
    3. Indicate the path to the associated file
     ________________________________________________________________

B.3.4.1.1. Useful commands for catalogs

   The most common mappings to be used in catalogs are:

   PUBLIC
          The keyword PUBLIC maps public identifiers for identifiers on
          the system.

   SYSTEM
          The SYSTEM keyword maps system identifiers for files on the
          system.

          SYSTEM
          "http://nexus.conectiva/utilidades/publicacoes/livros.dtd"
          "publicacoes/livros.dtd"

   SGMLDECL
          The keyword SGMLDECL designates the system identifier of the
          SGML statement that should be used.

          SGMLDECL "publishings/books.dcl"

   DTDDECL
          Similar to the SGMLDECL the keyword DTDDECL identifies the
          SGML statement that should be used. DTDDECL makes the
          association of the statement with a public identifier to a
          DTD. Unfortunately, this association isn't supported by the
          open source tools available. The benefits of this statement
          can be achieved somehow with multiple catalog files.

          DTDDECL "-//Conectiva SA//DTD livros V1.0//EN"
          "publicacoes/livros.dcl"

   CATALOG
          The keyword CATALOG allows a catalog to be included inside
          another. This is a way to make use of several different
          catalogs without the need to alter them.

   OVERRIDE
          The keyword OVERRIDE informs whether an identifier has
          priority over a system identifier. The standard on most
          systems is that the system identifier has priority over the
          public one.

   DELEGATE
          The keyword DELEGATE allows the association of a catalog to a
          specific type of public identifier. The clause DELEGATE is
          very similar to the CATALOG, except for the fact that it
          doesn't do anything until a specific pattern is specified.

   DOCTYPE
          If a document starts with a type of document, but has no
          public identifier and no system identifier the clause DOCTYPE
          associates this document with a specific DTD.
     ________________________________________________________________

B.3.4.2. XML Catalogs

   The following sample catalog was provided by Martin A. Brown.

   Example B-3. Sample XML Catalog file
<?xml version="1.0"?>
<!DOCTYPE catalog PUBLIC "-//OASIS/DTD Entity Resolution XML Catalog V1.0//EN"
          "http://www.oasis-open.org/committees/entity/release/1.0/catalog.dtd
">

<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">

        <public publicId="-//OASIS//DTD DocBook XML V4.2//EN"
       uri="/home/mabrown/docbook/dtds/4.2/docbookx.dtd"/>
   <uri name="http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd"
       uri="/home/mabrown/docbook/dtds/4.2/docbookx.dtd"/>
   <uri name="http://docbook.sourceforge.net/release/xsl/current/xhtml/docbook
.xsl"
       uri="/home/mabrown/docbook/xsl/xhtml/docbook.xsl"/>
   <uri name="http://docbook.sourceforge.net/release/xsl/current/xhtml/chunk.x
sl"
       uri="/home/mabrown/docbook/xsl/xhtml/chunk.xsl"/>
   <uri name="http://docbook.sourceforge.net/release/xsl/current/xhtml/profile
-chunk.xsl"
       uri="/home/mabrown/docbook/xsl/xhtml/profile-chunk.xsl"/>
</catalog>
     ________________________________________________________________

B.3.5. Validating XML

B.3.5.1. nsgmls

   You can use nsgmls, which is part of the jade suite (on Debian
   apt-get the docbook-utils package, see Section B.4.2), to validate
   SGML or XML documents.
bash$ nsgmls -s HOWTO.xml

   If there are no issues, you'll just get your command prompt back. The
   -s tells nsgmls to show only the errors.

   Tip Function not found


   If you get errors about a function not being found, or something
   about an ISO character not having an authoritative source, you may
   need to point nsgmls to your xml.dcl file. For Red Hat 9, it will
   look like this: nsgmls -s /usr/share/sgml/xml.dcl HOWTO.xml

   For more information on processing files with Jade/OpenJade please
   read
   [http://www.tldp.org/HOWTO/DocBook-OpenJade-SGML-XML-HOWTO/index.html
   ] DocBook XML/SGML Processing Using OpenJade.
     ________________________________________________________________

B.3.5.2. onsgmls

   This is an alternative to nsgmls. It ships with the OpenJade package.
   This program gives more options than nsgmls and allows you to quietly
   ignore a number of problems that arise while trying to validate an
   XML file (as opposed to an SGML file). This also means you don't have
   to type out the location of your xml.dcl file each time.

   I was able to simply use the following to validate a file with only
   error messages that were related to my markup errors.
bash$ onsgmls -s HOWTO.xml

   According to Bob Stayton you can also turn off specific error
   messages. The following example turns off XML-specific error
   messages.
bash$ onsgmls -s -wxml -wno-explicit-sgml-decl HOWTO.xml
     ________________________________________________________________

B.3.5.3. xmllint

   You can also use the xmllint command-line tool from the libxml2
   package to validate your documents. This tool does a simple check on
   completeness of tags and whether all tags that are opened, are also
   closed again. By default xmllint will output a results tree. So if
   your document comes out until the last line, you know there are no
   heavy errors having to do with tag mismatches, opening and closing
   errors and the like.

   To prevent printing the entire document to your screen, add the
   --noout parameter.
bash$ xmllint --noout HOWTO.xml

   If nothing is returned, your document contains no syntax errors.
   Else, start with the first error that was reported. Fix that one
   error, and run the tool again on your document. If it still returns
   output, again fix the first error that you see, don't botter with the
   rest since further errors are usually generated because of the first
   one.

   If you would like to check your document for any errors which are
   specific to your Document Type Definition, add --valid.
bash$ xmllint --noout --valid HOWTO.xml

   The xmllint tool may also be used for checking errors in the XML
   catalogs, see the man pages for more info on how to set this
   behavior.

   If you are a Mac OSX or Windows user, you may also want to check out
   tkxmllint, a GUI version of xmllint. More information is available
   from: [http://tclxml.sourceforge.net/tkxmllint.html]
   http://tclxml.sourceforge.net/tkxmllint.html.

   Example B-4. Debugging example using xmllint

   The example below shows how you can use xmllint to check your
   documents. I've created some errors that I made a lot, as a beginning
   XML writer. At first, the document doesn't come through, and errors
   are shown:
bash$ xmllint ldp-history.xml
ldp-history.xml:22: error: Opening and ending tag mismatch: articlinfo line 6
and articleinfo
</articleinfo>
              ^
ldp-history.xml:37: error: Opening and ending tag mismatch: listitem line 36 a
nd orderedlist
</orderedlist>
              ^
ldp-history.xml:39: error: Opening and ending tag mismatch: orderedlist line 3
4 and sect2
</sect2>
        ^
ldp-history.xml:46: error: Opening and ending tag mismatch: sect1 line 41 and
para
for many authors to contribute their part in their area of specialization.</pa
ra

 ^
ldp-history.xml:57: error: Opening and ending tag mismatch: para line 55 and s
ect1
</sect1>
        ^
ldp-history.xml:59: error: Opening and ending tag mismatch: sect2 line 31 and
article
</article>
          ^
ldp-history.xml:61: error: Premature end of data in tag sect1 line 24

^
ldp-history.xml:61: error: Premature end of data in tag article line 5

^

   Now, as we already mentioned, don't worry about anything except the
   first error. The first error says there is an inconsistency between
   the tags on line 6 and line 22 in the file. Indeed, on line 6 we left
   out the "e" in "articleinfo". Fix the error, and run xmllint again.
   The first complaint now is about the offending line 37, where the
   closing tag for list items has been forgotten. Fix the error and run
   the validation tool again, until all errors are gone. Most common
   errors include forgetting to open or close the paragraph tag,
   spelling errors in tags and messed up sections.
     ________________________________________________________________

B.4. Transformations

   Warning TLDP will convert your document


   This section is about how to transform documents from DocBook to
   other formats. If you do not need to transform documents for your own
   web site, or to proof read the content, please skip this section.

   If you would like to transform your documents for proofreading
   purposes, please use the XML to HTML on-line converter. You will need
   to upload your XML file(s) to a web site. Then simply drop the URL
   into the form and click the submit button. Your document will be
   magically transformed into a beautiful (and legible) HTML document.
   External files are supported. You may use either absolute or relative
   URIs.

   Another easy-to-use package is xmlto. It is a front-end for xsltproc.
   It is available as a RedHat, Debian (etc) package or can be
   downloaded from [http://cyberelk.net/tim/xmlto/]
   http://cyberelk.net/tim/xmlto/. You can use it to convert documents
   with:
bash$ xmlto html mydoc.xml
bash$ xmlto txt mydoc.xml

   You do not ever need to transform documents before submitting to the
   LDP. The LDP volunteers have a system which transforms your DocBook
   file into HTML, PDF and plain text formats. There, you've been
   warned.

   Still here? Great! Transformations are a pretty basic requirement to
   get what you've written from a messy tag-soup into something that can
   be read. This section will help you get your system set up and ready
   to transform your latest document into other formats. This is very
   useful is you want to see your document before you release it to the
   world.

   There are currently two ways to transform your document: Document
   Style Semantics and Specification Language (DSSSL); and XML Style
   sheets (XSLT). Although the LDP web site uses DSSSL to convert
   documents you may use XSLT if you want. You only need to choose one
   of these methods. For more information about DSSSL read: Section
   B.4.1, for more information about XSLT read: Section B.4.3.
     ________________________________________________________________

B.4.1. DSSSL

   There are three basic requirements to transform a document using
   DSSSL:

     * The Document Style and Semantics Specification Language files
       (these are plain text files). Section B.4.1.1
     * The Document Type Definition file which matches the DOCTYPE of
       your document (this is a plain text file). Section B.5
     * A processor to do the actual work. Section B.4.1.2
     ________________________________________________________________

B.4.1.1. The Style Sheets

   There are two versions of the Document Style Semantics and
   Specification Language used by the LDP to transform documents from
   your raw DocBook files into other formats (which are then published
   on the Web). The LDP version of the style sheets requires the Norman
   Walsh version--which basically means if you're using DSSSL the Norman
   Walsh version can be considered a requirement for system setup.

   Norman Walsh DSSSL [http://docbook.sourceforge.net/projects/dsssl/]
   http://docbook.sourceforge.net/projects/dsssl/. The Document Style
   Semantics and Specification Language tells Jade (see Section B.4.1.2)
   how to render a DocBook document into print or on-line form. The
   DSSSL is what converts a title tag into an <h1> HTML tag, or to 14
   point bold Times Roman for RTF, for example. Documentation for DSSSL
   is located at the same site. Note that modifying the DSSSL doesn't
   modify DocBook itself. It merely changes the way the rendered text
   looks. The LDP uses a modified DSSSL (see below).

   LDP DSSSL [http://www.tldp.org/authors/tools/ldp.dsl]
   http://www.tldp.org/authors/tools/ldp.dsl. The LDP DSSSL requires the
   Norman Walsh version (see above) but is a slightly modified DSSSL to
   provide things like a table of contents.

   Example B-5. "Installing" DSSSL style sheets

   Create a base directory to store everything such as /usr/share/sgml/.
   Copy the DSSSL style sheets into a sub-directory named dsssl.
     ________________________________________________________________

B.4.1.2. DSSSL Processors

   There are two versions of the Jade processor: the original version by
   James Clark; and an open-source version of approximately the same
   program, OpenJade. You only need one of these programs. It should be
   installed after the DTD and DSSSL have been "installed."

   DSSSL Transformation Tools

   Jade
          [ftp://ftp.jclark.com/pub/jade/]
          ftp://ftp.jclark.com/pub/jade/

          Currently, the latest version of the package is
          jade-1.2.1.tar.gz.

          Jade is the front-end processor for SGML and XML. It uses the
          DSSSL and DocBook DTD to perform the verification and
          rendering from SGML and XML into the target format.

   OpenJade
          [http://openjade.sourceforge.net/]
          http://openjade.sourceforge.net/

          An extension of Jade written by the DSSSL community. Some
          applications require jade, but are being updated to support
          either software package.
     ________________________________________________________________

B.4.1.3. System Setup for DSSSL Transformations

    1. Tell your system where to find the SGML_CATALOG_FILES (yes, even
       if you are using XML). You can find an example of how to do this
       in Example B-1.
