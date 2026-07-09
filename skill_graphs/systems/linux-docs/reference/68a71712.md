    2. Download the DSSSL and DTD files and copy them into your working
       directory. You can find an example of how to do this in Example
       B-5 and Example B-7.
     ________________________________________________________________

B.4.1.4. Transformations with DSSSL

   Once your system is configured (see the previous section), you should
   be able to start using jade to transform your files from XML to
   XHTML.

   To create individual HTML files, point jade at the correct DSL (style
   sheet). The following example uses the LDP style sheet.
bash$ jade -t xml -i html \
        -d /usr/local/sgml/dsssl/docbook/html/ldp.dsl#html \
        HOWTO.xml

   If you would like to produce a single-file HTML page, add the -V
   nochunks parameter. You can specify the name of the final HTML file
   by appending the command with > output.html.
bash$ jade -t xml -i html -V nochunks \
        -d /usr/local/sgml/dsssl/stylesheets/ldp.dsl#html \
        HOWTO.sgml > output.html

   Note Not a function name errors


   If you get an error about "is not a function name", you will need to
   add a pointer to xml.dcl. It has to be listed immediately before the
   pointer to your XML document. Try one of the following locations:
   /usr/lib/sgml/declaration/xml.dcl, or
   /usr/share/sgml/declaration/xml.dcl. Use locate to find the file if
   it is not in either of those two places. The modified command would
   be as follows:
bash$ jade -t xml -i html \
        -d /usr/local/sgml/dsssl/docbook/html/ldp.dsl#html \
        /usr/lib/sgml/declaration/xml.dcl HOWTO.xml

   If you would like to create print-friendly files instead of HTML
   files, simply change the style sheet that you are using. In the file
   name above, note "html/ldp.dsl" at the end. Change this to
   "print/docbook.dsl", or if you want XHTML output, instead of HTML,
   change the file name to "xhtml/docbook.dsl".
     ________________________________________________________________

B.4.1.4.1. Changing CSS Files

   If you want your HTML files to use a specific CSS stylesheet, you
   will need to edit ldp.dsl. Immediately after ;; End of
   $verbatim-display$ redefinition add the following lines:
(define %stylesheet-type%
  ;; The type of the stylesheet to use
  "text/css")

(define %stylesheet%
  ;; Name of the css stylesheet to use, use value #f if you don't want to
  ;; use css stylesheets
  "base.css")

   Replace base.css with the name of the CSS file you would like to use.
     ________________________________________________________________

B.4.2. The docbook-utils Package

   The docbook-utils provide commands like db2html, db2pdf and db2ps,
   based on the jw scripts, that is a front-end to Jade. These tools
   ease the everyday management of documentation and add comfortable
   features.

   The package, originally created by RedHat and available from
   [http://sources.redhat.com/docbook-tools/]
   http://sources.redhat.com/docbook-tools/ can be installed on most
   systems.

   Example B-6. Example creating HTML output

   After validating your document, simply issue the command db2html
   mydoc.xml to create (a) HTML file(s). You can also use the
   docbook-utils as validation tools. Remember: when errors occur,
   always start by solving only the first problem. The rest of the
   problems may be fixed when you fix the first error.

   If you get errors about a function name, please read .
     ________________________________________________________________

B.4.2.1. Using CSS and DSL for pretty output

   You can define your own additional DSL instructions, which can
   include a pointer to a personalized CSS file. Sample DSL and CSS
   files are provided in Appendix A.

   The sample DSL file will create a table of contents, and have all
   HTML files start with the prefix intro2linux- and end with a suffix
   of .html. The %stylesheet% variable points to the CSS file which
   should be called by your HTML file.

   To use a specific DSL style sheet the following command should be
   used:

   db2html -d mystyle.dsl mydoc.xml

   You can compare the result here:
   [http://tille.xalasys.com/training/unix/]
   http://tille.xalasys.com/training/unix/ is a book formatted with the
   standard tools; [http://tille.xalasys.com/training/tldp/]
   http://tille.xalasys.com/training/tldp/ is one using personalized DSL
   and CSS files. Soft tones and special effects, for instance in
   buttons, were used to achieve maximum effect.
     ________________________________________________________________

B.4.3. XSL

   There are alternatives to DSSSL and Jade/OpenJade.

   When working with DocBook XML, the LDP offers a series of XSL[2]
   style sheets to process documents into HTML. These style sheets
   create output files using the XML tool set that are similar to those
   produced by the SGML tools using ldp.dsl.

   The major difference between using ldp.dsl and the XSL style sheets
   is the way that the generation of multiple files is handled, such as
   the creation of a separate file for each chapter, section and
   appendix. With the SGML tools, such as jade or openjade, the tool
   itself was responsible for generating the separate files. Because of
   this, only a single file, ldp.dsl was necessary as a customization
   layer for the standard DocBook DSSSL style sheets.

   With the DocBook XSL style sheets, generation of multiple files is
   controlled by the style sheet. If you want to generate a single file,
   you call one style sheet. If you want to generate multiple files, you
   call a different style sheet. For that reason the LDP XSL style sheet
   distribution is comprised of four files:

    1. tldp-html.xsl - style sheet called to generate a single file.
    2. tldp-html-chunk.xsl[3] - style sheet called to generate multiple
       files based on chapter, section and appendix elements.
    3. tldp-html-common.xsl - style sheet containing the actual XSLT
       transformations. It is called by the other two HTML style sheets
       and is never directly called.
    4. tldp-print.xsl - style sheet for generation of XSL Formatting
       Objects for print output.

   You can find the latest copy of the files at
   [http://my.core.com/~dhorton/docbook/tldp-xsl/]
   http://my.core.com/~dhorton/docbook/tldp-xsl/. The package includes
   installation instructions which are duplicated at
   [http://my.core.com/~dhorton/docbook/tldp-xsl/doc/tldp-xsl-howto.html
   ]
   http://my.core.com/~dhorton/docbook/tldp-xsl/doc/tldp-xsl-howto.html.
   The short version of the install instructions is as follows: Download
   and unzip the latest package from the web site. Take the files from
   the html directory of TLDP-XSL and put them in the html directory of
   Norman Walsh's stylesheets. Take the file from the TLDP-XSL fo
   directory and put it in the Norman Walsh fo directory.

   Once you have installed these files you can use xsltproc to generate
   HTML files from your XML documents. To transform your XML file(s)
   into a single-page HTML document use the following command:
bash$  xsltproc -o HOWTO.html /usr/local/sgml/stylesheets/tldp-html.xsl HOWTO.
xml

   To generate a set of linked HTML pages, with a separate page for each
   chapter, sect1 or appendix, use the following command:
bash$ xsltproc /usr/share/sgml/stylesheets/tldp-html-chunk.xsl HOWTO.xml

   Note that you never directly call the style sheet
   tldp-html-common.xsl. It is called by both of the other two style
   sheets.
     ________________________________________________________________

B.4.3.1. Changing CSS Files

   If you want your HTML files to use a specific CSS stylesheet, you
   will need to edit tldp-html-common.xsl. Look for a line that
   ressembles <xsl:param name="html.stylesheet" select="'style.css'"/>.

   Replace style.css with the name of the CSS file you would like to
   use.
     ________________________________________________________________

B.5. DocBook DTD

   The DocBook DTD defines the structure of a DocBook document. It
   contains rules about how the elements may be used; and what the
   elements ought to be describing. For example: it is the DocBook DTD
   which states all warnings are to warn the reader (this is the
   definition of the element); and may not contain plain text (this is
   the content model--and the bit which forces you to wrap your warning
   text in a para or perhaps a list).

   Caution Versions


   It is important that you download the version(s) that match your
   document. You may want to configure your system now to deal with
   "all" DocBook DTDs if you are going to be editing older LDP
   documents. If you are a new author, you only need the first one
   listed: XML DTD for DocBook version 4.2.

   The XML DTD is available from
   [http://www.oasis-open.org/docbook/xml/4.2]
   http://www.oasis-open.org/xml/4.2/. The LDP prefers this version of
   the DocBook DTD.

   If you are going to be working with SGML versions of DocBook you will
   need one (or both) of:
   [http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip]
   http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip or
   [http://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip]
   http://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip

   Example B-7. "Installing" DocBook Document Type Definitions

   Create a base directory to store everything such as /opt/local/sgml/.
   Copy the DTDs into a sub-directory named dtd.

   Warning Do not edit DTD files


   The DocBook standard is described in these files. If you change these
   files, you are no longer working with DocBook.
     ________________________________________________________________

B.6. Formatting Documents

B.6.1. Inserting a summary on the initial articles page

   A feature that might be valuable in some cases is the insertion of
   the summary on the initial page of an article. DocBook articles do
   not include it as a standard feature.

   To enable this, it is necessary to modify the style sheet file.

   Example B-8. Style sheet to insert summaries in articles
<!DOCTYPE style-sheet PUBLIC "-//James Clark//DTD DSSSL Style Sheet//EN" [
<!entity html-docbook PUBLIC "-//Norman Walsh//DOCUMENT DocBook HTML Styleshee
t//EN" CDATA DSSSL>
<!entity print-docbook PUBLIC "-//Norman Walsh//DOCUMENT DocBook Print Stylesh
eet//EN" CDATA DSSSL>
]>

<style-sheet>
<style-specification use="html">
<style-specification-body>

; Includes a summary at the beginning of an item.
(define %generate-article-toc% #t)

</style-specification-body>
</style-specification>
<style-specification use="print">
<style-specification-body>

; Includes a summary at the beginning of an item.
(define %generate-article-toc% #t)

</style-specification-body>
</style-specification>
<external-specification id="html" document="html-docbook">
<external-specification id="print" document="print-docbook">
</style-sheet>

     ________________________________________________________________

B.6.2. Inserting indexes automatically

   Although DocBook has markups for the composition of them, indexes are
   not generated automatically. The collateindex.pl command allows
   indexes to be generated from the source DocBook for inclusion into
   the finished/transformed document.

    1. Process the document with jade using the style to HTML with the
       option -V html-index.

bash$ jade -t sgml \
        -d html/docbook.dsl -V html-index document.sgml

    2. Generate the index.sgml file with collateindex.pl.

bash$  perl collateindex.pl \
        -o index.sgml HTML.index

   For the above example to work, it is necessary to define an external
   entity by calling the file index.sgml.

   Example B-9. Configuring an external entity to include the index
<!DOCTYPE article PUBLIC "-//OASIS//DTD
DocBook V3.1//EN" [

<!-- Insertion of the index --> <!entity index SYSTEM
"index.sgml"> ]>

   See also Section D.4 for information on how to insert necessary
   information on the text.

   Note Odd behavior generating indexes for print versions


   Remember that if you're trying to get Tables of Contents or Indexes
   on PS or PDF output you'll need to run jadetex or pdfjadetex at least
   three times. This is required by TeX but not by DocBook or related
   applications.
     ________________________________________________________________

Appendix C. Concurrent Version System (CVS)

   The LDP provides optional CVS access to its authors. This enables
   collaborative writing and has the following positive effects:

    1. CVS will keep an off-site backup of your documents. In the event
       that you hand over a document to another author, they can just
       retrieve the document from CVS and continue on. In the event you
       need to go back to a previous version of a document, you can
       retrieve it as well.
    2. However difficult from an organizational point of view, it's
       great to have multiple people working on the same document. CVS
       enables you to do this. You can have CVS tell you what changes
       were made by another author while you were editing your copy, and
       integrate those changes.
    3. CVS keeps a log of what changes were made. These logs (and a date
       stamp) can be placed automatically inside your documents when
       they are published.
    4. CVS can be combined with scripts to automatically update the LDP
       web site with new documentation as it's written and submitted.
       This is not in place yet, but it is a goal. Currently, CVS
       updates signal the HOWTO coordinator to update the LDP web page,
       meaning that if you use CVS, you're not required to e-mail your
       XML code. (Although you do still need to send the submit list an
       email when you are ready for your document to be published,
       because the whole publishing process has not been fully automated
       yet.)

   Note Access to our CVS repository


   Only authors with at least three submissions get access to our CVS,
   see Appendix C.

   You can browse the LDP CVS repository via the web at
   [http://cvs.tldp.org/] http://cvs.tldp.org/.
     ________________________________________________________________

C.1. Getting a CVS account

   Caution CVS accounts will not be granted to all applicants


   To be granted a CVS account you must qualify under one of the
   following categories:

     * authors with documents already in the collection who have made a
       minimum of three submits to the LDP through <submit@en.tldp.org>
     * technical and language reviewers approved by one of the Review
       Coordinators
     * new authors in the review process (also requires approval from
       one of the Review Coordinators)

   Please do not apply for a CVS account if you do not qualify.

   If you qualify for a CVS account you may apply for one contacting CVS
   master Sergiusz [mailto:ser@gnu.org] mailto:ser@gnu.org Include
   information about which documents you maintain.
     ________________________________________________________________

C.2. Using CVS

C.2.1. Setting Up Your CVS Account

   First you'll need to get an account at the LDP's CVS Repository.
   Please see the notes above on obtaining an account. This repository
   houses various documents including HOWTOs and Guides. Documents are
   sorted by the type of document (for example a HOWTO or a Guide), and
   by the markup language the document uses (for example DocBook or
   LinuxDoc).

   When your account is ready you can log in using one of the following
   commands. In all instances your_userid should be replaced by the user
   name you were issued in the response email. You will be prompted for
   a password after this first step.

   Initializing Your CVS Account

   Linux system
          cvs -d :pserver:your_userid@cvs.tldp.org:/cvsroot login

   Windows system
          set CVSROOT=":pserver:your_userid@cvs.tldp.org:/cvsroot"

          cvs -d %CVSROOT% login

   Wait patiently while the system tries to log you in. It can often
   take more that 10-20 seconds for the system to either accept (or
   reject) your password. Once you've used cvs login for the first time
   and have been given access to the system, your password is stored in
   .cvspass and you will not have to use cvs login again. Just set the
   CVSROOT with the export command listed above and continue on. If
   TLDP's CVS server is the only one you work with, you might also add
   an export CVSROOT line to your ~/.bashrc shell configuration file.
     ________________________________________________________________

C.2.2. Getting the Documents

   You can get the entire repository (about 150 MB) with: cvs checkout
   LDP

   Or you can get the source for your own document with: cvs checkout
   LDP/howto/docbook/YOUR-HOWTO.xml OR cvs checkout
   LDP/guide/docbook/YOURGUIDE

   Windows users will need to use a modified version of this command.
   Instead they should use: cvs -d %CVSROOT% checkout
   LDP/howto/docbook/YOUR-HOWTO.xml

   Note Keep an overview


   checkout will add the full directory structure from tldp.org on down.
   Although it doesn't really matter where you put these files on your
   local file system you may not want to bury the directories too
   deeply.
     ________________________________________________________________

C.2.3. CVS Commands

   CVS Commands: a brief reminder

   commit
          This CVS command will upload your changes to the CVS server.

          Please be sure to include a useful description of the changes
          that have been made to your document.

          If you want to bypass the editor screen you can use

          cvs commit -m "A description of the work done on this version
          of the document."

          Note Ready for publication warning


   You must still email <submit@en.tldp.org> when you are ready to have
   your changes appear on the live site. Your email should include the
   relative path to the file(s) in the LDP CVS tree that you wish to
   update.

   add
          You can add new files to your CVS repository. These may be
          image files or additional XML files. First check that your
          HOWTO is in its own directory. You may want to coordinate with
          the people at <submit@en.tldp.org> to ensure you can add
          graphics or other files to your HOWTO.

          Copy the files you want to add into your local CVS repository
          (where all of your downloaded/working files are). Then:

          cvs add filename

          After you've added the files, you still need to commit them to
          the repository (see above).

   remove

   $Id: cvs.xml,v 1.32 2011/01/14 16:24:52 serek Exp $
          While this is not a CVS "command" it can be used to
          automatically insert information about the file including the
          time and date it was last modified, the version number it was
          assigned by the CVS and the filename of this particular file.
          The output will look like this: $Id: cvs.xml,v 1.9 2002/04/21
          09:44:26 serek Exp $

   If you need to change a file name, you still need to use the add
   command. First remove the copy of the file from your local disk. Then
   remove it from the CVS tree with: cvs remove filename. As with the
   add command, you need to >commit your removed file. Finally, now that
   the old file has been removed, add your new file using the
   instructions above (first add and then commit the additional file).
     ________________________________________________________________

C.2.3.1. Recovering old versions

   There you are, typing away, when you screw up. Real bad. Doesn't
   matter what it is, but suffice it to say that you've toasted not only
   the version on your local drive, but created a new version on the CVS
   server. What you need to do is go back in time and resurrect an older
   version of your file.

   To do this, you'll need to know the version number of the file you
   want to retrieve. cvs diff will give a list of revisions if there are
   differences. You can pick the revision number, subtract one, and that
   is probably the revision you want to look at.

   The command

   cvs -Q update -p -r revision filename

   will output to stdout the contents of the revision version of
   filename. You can pipe it to more or redirect the output to a file.
   Conveniently, you can redirect stdout to a file called filename. Your
   local file is now the revision you want, and

   cvs update

   will update the CVS server with the new (old) version of filename.
     ________________________________________________________________

C.3. CVS Resources

   If you're completely new to CVS, there are a few web pages you may
   want to look at which can help you out:

     * [http://cvshome.org/docs/blandy.html]
       http://cvshome.org/docs/blandy.html
     * [http://www.loria.fr/~molli/cvs/doc/cvs_toc.html]
       http://www.loria.fr/~molli/cvs/doc/cvs_toc.html
     ________________________________________________________________

Appendix D. DocBook: Sample Markup

D.1. General Tips and Tricks

   For a general overview of what markup is all about, please read
   Chapter 5

     * An editor capable of inserting elements according to the DTD will
       help a lot since it will enforce the DTD. This way you can be
       sure that no invalid elements were added anywhere in your
       document.
     * In order to ensure that future changes are as easy as possible,
       authors should try to keep compatibility with the XML version of
       the DocBook DTD. This means keeping element names in lower case,
       using double quotes in all attributes, and not omitting end tags.
       Most tools that automatically insert elements (like psgml+emacs)
       follow these rules automatically or with some fine tuning.
     * Each type of document created has a specific structure. This
       document is in "book" format. Most authors, however, will want to
       use the shorter "article" format instead. Templates are available
       from Appendix A.
     ________________________________________________________________

D.1.1. Useful markup

   Table D-1 shows some markup that is useful for generating generic
   documents. Remember that some elements are valid only on some
   contexts.

   Tip Check several formats


   Sometimes the appearance of a particular tag changes from one
   conversion format to another. As a beginner in DocBook writing, you
   may wish to see how your document looks in several formats before you
   publish them. You are advised to look at how your document is
   presented in HTML, PDF and PostScript, since these formats will be
   made available by TLDP once you publish your document.

   Note Better too much than not enough


   Since the formatting depends on the output style chosen, it's
   recommended to use as much markup as possible. Even if the appearance
   of the output doesn't seem to change with the standard output style,
   there may be specific output formats that will make these tags stand
   out.

   Table D-1. Useful markup
   Description Sample markup Result
   E-mail address <email>address@domain</email> <address@domain>
   About the author <author>...</author> (see example below)
   Author's name
<firstname>Mary</firstname>
<othername>Margaret</othername>
<surname>O'Hara</surname>

   Mary Margaret O'Hara
   Keys' name (printings on the keyboard) <keycap>F1</keycap> F1
   Symbol represented by the keys <keysym>KEY_F1</keysym> KEY_F1
   Key's code <keycode>0x3B</keycode> 0x3B
   Combinations or sequences of keys
<keycombo>
   <keycap>Ctrl</keycap>
   <keycap>S</keycap>
</keycombo>

   Ctrl-S
   Program Menus <guimenu>File</guimenu> File
   Menu Items <guimenuitem>Save</guimenuitem> Save
   Menu Sequences
<menuchoice>
   <shortcut>
      <keycombo>
         <keycap>Ctrl</keycap>
         <keycap>S</keycap>
      </keycombo>
   </shortcut>
   <guimenu>File</guimenu>
   <guimenuitem>Save</guimenuitem>
</menuchoice>

   File->Save (Ctrl-S)
   Mouse Button <mousebutton>left</mousebutton> left
   Application Names <application>application</application> application
   Text Bibliographical Reference <citation>reference</citation>
   [reference]
   Quote
<blockquote>
   <attribution>Text Author</attribution>
   <para>Quote Text.</para>
</blockquote>



   Quote Text.

   --Text Author
   Index (NA) See Section D.4.
   File Names
   <filename>file</filename>

   file
   Directories
   <filename id="directory">directory</filename>

   directory/
   Emphasize Text[a]
   <emphasis>text</emphasis>

   text
   Footnotes
<footnote>
   <para>Footnote text</para>
</footnote>

   (See note at the end of this table for an example)
   URLs
   <ulink url="http://www.conectiva.com">Conectiva S.A.</>

   [http://www.conectiva.com] Conectiva S.A.
   Itemized (unnumbered) List
<itemizedlist>
   <listitem>
      <para>item</para>
   </listitem>
   <listitem>
      <para>item</para>
   </listitem>
</itemizedlist>

     * item
     * item

   Ordered (numbered) List
<orderedlist>
   <listitem>
      <para>item</para>
   </listitem>
   <listitem>
      <para>item</para>
   </listitem>
</orderedlist>

    1. item
    2. item

   Segmented List
<segmentedlist>
   <title>Binary to decimal conversion</title>
   <segtitle>Binary</segtitle>
   <segtitle>Decimal</segtitle>
   </seglistitem><seg>00</seg><seg>0</seg>
   </seglistitem>
   <seglistitem><seg>01</seg><seg>1</seg>
   </seglistitem>
   <seglistitem><seg>10</seg><seg>2</seg>
   </seglistitem>
</segmentedlist>
