   Binary to Decimal Conversion

   Binary: 00

   Decimal: 0

   Binary: 01

   Decimal: 1

   Binary: 10

   Decimal: 2
   Variable List
<variablelist>
   <varlistentry>
      <term>Entry 1</term>
      <listitem>
         <para>Description</para>
      </listitem>
   </varlistentry>
   <varlistentry>
      <term>Entry 2</term>
      <listitem>
         <para>Description</para>
      </listitem>
   </varlistentry>
</variablelist>

   Entry 1
          Description

   Entry 2
          Description

   Simple Lists
<simplelist type="horiz" columns="3">
   <member>1</member>
   <member>2</member>
   <member>3</member>
   <member>4</member>
   <member>5</member>
   <member>6</member>
</simplelist>
<simplelist type="inline">
   <member>A</member>
   <member>B</member>
   <member>C</member>
   <member>D</member>
   <member>E</member>
   <member>F</member>
</simplelist>

   1 2 3
   4 5 6

   A, B, C, D, E, F
   Pictures (NA) See Section D.5
   Glossary
<glossentry>
   <glossterm>Term</glossterm>
   <glossdef>
      <para>Definition</para>
   </glossdef>
</glossentry>

   (See the glossary at the end of this document)
   Crossed References
<section id="secao">
...
</section>
<section id="reference the other section">
...
<para>Please, see<xref linkend="secao" /> for more information.

   (NA)
   Notes:
   a. Text can be emphasized in a few ways. The most common ways are
   italics and bold. DocBook, however, supports only italics. The use of
   bold requires additional settings on the style sheet used.
     ________________________________________________________________

D.2. <section> and <sectN>: what's the difference?

   Note Acknowledgment


   These notes were provided by: [http://geekhavoc.com] John Daily and
   Saqib Ali (<saqib@seagate.com>).

   <section> versus <sectN> is largely a question of flexibility. The
   stylesheets can make a <section> in a <section> look just like a
   <sect2> within a <sect1>, so there's no output advantage.

   But, a <section> within a <section> can be extracted into its own
   top-level section, nested even more deeply, or moved to an entirely
   different part of the document, without it and its own <section>
   children being renamed. That is not true of the numbered section
   tags, which are very sensitive to rearrangements. This can be easier
   for authors who are new to DocBook than using <sectN>.

   The main idea behind creating structured data is that it should be
   easy to access and query. One should be able to retrieve a subsection
   of any structured data, by using querying languages for XML (XPath
   and XQuery). <sectN> are useful when traversing a document using
   XPath/XQuery. <sectN> gives more flexibility, and control while
   writing an XPath expression.

   A well-defined, valid and well-structured document makes it easier
   for one to write XPath/Query to retrieve "specific" data from a
   document. For example you can use XPath to retrieve information in
   the <sect3> block with certain attributes. However if you just used
   <section> for all subsections, it becomes harder to retrieve the
   block of information that you need.

   So which one should you use? The one you feel most comfortable with
   is a good place to start. This document is written with <section>s.
   You may, or may not, think this is a good idea. :)
     ________________________________________________________________

D.3. Command Prompts

   There are likely as many ways of doing this as there are DocBook
   authors; however, here are two ways that you might find useful.
   Thanks to [http://www.appaji.net/] Y Giridhar Appaji Nag and
   [http://linux-ip.net/] Martin Brown for the markup used here.

   Example D-1. Command Prompt with programlisting
<programlisting>
        <prompt># </prompt><userinput><command>cd</command> /some/dir</userinp
ut>
        <prompt># </prompt><userinput><command>ls</command> -l</userinput>
</programlisting>

   Displays as:
# cd /some/dir
# ls -l

   Example D-2. Command Prompt with screen

   First create a general entity in the internal subset at the very
   beginning of your document. This entity will define a name for the
   shortcut which you can use to display the full prompt at any point in
   your document. <!ENTITY prompt "<prompt>[user@machine
   ~/dir]$</prompt>">

   For more information about entities, read Section D.8.
<screen>
&prompt; <userinput>cd /some/dir</userinput>
&prompt; <userinput>ls -l</userinput> </screen>

   Displays as:

[user@machine ~/dir]$ cd /some/dir
[user@machine ~/dir]$ ls -l

   If you would like to add the output of your commands you can add
   <computeroutput> text</computeroutput> within the <screen> or
   <programlisting> as appropriate.
     ________________________________________________________________

D.4. Encoding Indexes

   The generation of indexes depends on the markups inserted in the
   text.

   Such markups will be processed afterwards by an external tool and
   will generate the index. An example of such a tool is the
   collateindex.pl script (see Section B.6.2). Details about the process
   used to generate these indexes are shown in Section B.6.2.

   The indexes have nesting levels. The markup of an index is done by
   the code Example D-3.

   Example D-3. Code for the generation of an index
<indexterm>
   <primary>Main level</primary>
   <secondary>Second level</secondary>
        <tertiary>Third level</tertiary>
        </indexterm>

   It is possible to refer to chapters, sections, and other parts of the
   document using the attribute zone.

   Example D-4. Use of the attribute zone
<section id="encoding-index">
<title>Encoding Indexes</title>
<indexterm zone="encoding-index">
<primary>edition</primary> <secondary>index</secondary>
</indexterm>

<para>
        The generation of indexes depend on the inserted markups on the text.
</para>

   The Example D-4 has the code used to generate the entry of this
   edition on the index. In fact, since the attribute zone is used, the
   index statement could be located anywhere in the document or even in
   a separate file.

   However, to facilitate maintenance the entries for the index were all
   placed after the text to which it refers.

   Example D-5. Usage of values startofrange and endofrange on the
   attributeclass
    <para>Typing the text normally
    sometimes there's the need of
   <indexterm class="startofrange"
   id="example-band-index">
      <primary>examples</primary> <secondary>index</secondary>
   </indexterm> mark large amounts of
   text.</para>

   <para>Keep inserting the paragraphs
   normally.</para>

   <para>Until the end of the section
   intended to be indexed.  <indexterm
   startref="example-band-index" class="endofrange">.
   </para>
     ________________________________________________________________

D.5. Inserting Pictures

   It is necessary to insert pictures formats for all possible finished
   document types. For example: JPG files for web pages and EPS for
   PostScript and PDF files.

   If you use the TeX format you'll need the images as a PostScript
   file. For on-line publishing you can use any kind of common image
   file, such as JPG, GIF or PNG.

   The easiest way to insert pictures is to use the fileref attribute.
   Usually pictures are generated in JPG and in PostScript (PS or EPS).

   Example D-6. Inserting a picture
<figure>
   <title>Picture's
   Title</title> <graphic fileref="images/file"></graphic>
</figure>

   Replacing <figure> by <informalfigure> eliminates the need to insert
   a title for the picture.

   There's still the float attribute on which the value 0 indicates that
   the picture should be placed exactly where the tag appears. The value
   1 allows the picture to be moved to a more convenient location (this
   location can be described on the style sheet, or it can be controlled
   by the application).
     ________________________________________________________________

D.5.1. Graphics formats

   When submitting graphics to the LDP, please submit one set of
   graphics in .eps, and another in .gif, .jpg or .png. The preferred
   format is .png or .jpg due to patent problems with .gif.

   You can use .jpg files for continuous-tone images such as photos or
   images with gradual changes in color. Use .png for simple images like
   diagrams, some screen shots, and images with a low number of colors.
     ________________________________________________________________

D.5.2. Alternative Methods

   The first alternative to Example D-6 is to eliminate the <figure> or
   <informalfigure> elements.

   Another interesting alternative when you have decided to publish the
   text on media where pictures are not accepted, is the use of a
   wrapper, <imageobject>.

   Example D-7. Using <imageobject>
<figure>
   <title>Title</title>
   <mediaobject>
      <imageobject>
         <imagedata fileref="images/file.eps" format="EPS">
      </imageobject>
   <imageobject>
         <imagedata fileref="images/file.jpg" format="JPG">
      </imageobject>
      <textobject>
         <phrase>Here there's an image of this example</phrase>
      </textobject>
   <caption>
   <para>Image Description. Optional. </para>
   </caption>
   </mediaobject>
</figure>

   Files using the following formats are available BMP, CGM-BINARY,
   CGM-CHAR, CGM-CLEAR, DITROFF, DVI, EPS, EQN, FAX, GIF, GIF87A,
   GIF89A, IGES, JPEG, JPG, LINESPECIFIC, PCX, PIC, PS, SGML, TBL, TEX,
   TIFF, WMF, WPG.

   This method presents an advantage: a better control of the
   application. The elements <imageobject> are consecutively tested
   until one of them is accepted. If the output format does not support
   images the <textobject> element will be used. However, the biggest
   advantage in usage of the format Example D-7 is that in DocBook 5.0,
   the <graphic> element will cease to exist.

   As a disadvantage, there is the need for more than one representation
   code of the same information. It is up to the author to decide how
   they will implement illustrations and pictures in the document, but
   for compatibility with future versions I recommend the use of this
   method for pictures and graphics.

   Warning Title page exception


   <mediaobject>s will not display if they are used on a title page. For
   more information read:
   [http://www.sagehill.net/docbookxsl/HtmlCustomEx.html#HTMLTitlePage]
   http://www.sagehill.net/docbookxsl/HtmlCustomEx.html#HTMLTitlePage

   Note ASCII Images


   You may also want to try converting your image to an ASCII
   representation of the file. JavE (Java ASCII Versatile Editor) can do
   this conversion for you. It can be downloaded from
   [http://www.jave.de/] http://www.jave.de/. It has an easy to use GUI
   interface.

   If you're more command-line oriented you may want to try: tgif
   ([http://bourbon.usc.edu:8001/tgif/]
   http://bourbon.usc.edu:8001/tgif/) and AA-Lib
   ([http://aa-project.sourceforge.net/]
   http://aa-project.sourceforge.net/).
     ________________________________________________________________

D.6. Markup for Metadata

D.6.1. Crediting Translators, Converters and Co-authors

   There are several ways that these folks, as well as other
   contributors to your document, can be given some recognition for the
   help they've given you.
     ________________________________________________________________

D.6.1.1. <othercredit>

   All translators, converters and co-authors should be credited with an
   <othercredit> tag entry. To properly credit a translator or
   converter, use the <othercredit> tag with the role attribute set to
   "converter" or "translator", as indicated in the example below:

   Example D-8. Other Credit
<othercredit role='converter'>
  <firstname>David</firstname>
  <surname>Merrill</surname>
  <contrib>Conversion from HTML to DocBook v3.1 (SGML).</contrib>
</othercredit>
     ________________________________________________________________

D.6.1.2. Crediting Editors and Reviewers

   To help track the review process all new documents must include a
   reference to the reviewers for the
   [http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/techreview.html]
   technical,
   [http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/languagereview.html]
   language and
   [http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/metadatareview.html]
   metadata reviews.

   Example D-9. Editor
<editor>
  <firstname>Tabatha</firstname>
  <surname>Marshall</surname>
  <contrib>Language review of version 0.8</contrib>
</editor>
     ________________________________________________________________

D.6.2. <revremark>s

   Within the <revision> tag hierarchy is a tag called <revremark>.
   Within this tag, you can make any brief notes you wish about each
   particular revision of your document.
     ________________________________________________________________

D.6.3. Revision History

   The <revhistory> tag should be used to denote the various revisions
   of the document. Specify the date, revision number and comments
   regarding what has changed.

   Revisions should be listed with the most-recent version at the top
   (list in descending order).
     ________________________________________________________________

D.6.4. Date formats

   The <pubdate> tag in your header should list the publication date of
   this particular version of the document (coincide with the revision
   date). It should be in the following format:
   <pubdate>2002-04-25</pubdate>

   The date is in the format YYYY-MM-DD, which is one of the
   [http://www.w3.org/TR/NOTE-datetime] ISO 8601 standard formats for
   representing dates. For you Yanks out there (me too), think of it as
   going from the largest unit of time to the smallest.
     ________________________________________________________________

D.6.5. Sample Article (or Book) Information Element

   Here is a sample of a complete DocBook (SGML or XML) <articleinfo>
   element which contains some of the items and constructs previously
   described.

   Example D-10. Sample Meta Data
<!--
   Above these lines in a typical DocBook article would be the article
   element (the immediate parent of the articleinfo element) and above
   that typically, the DOCTYPE declaration and internal subset.
  -->

<articleinfo>

  <!--
        Use "HOWTO", "mini HOWTO", "FAQ" in title, if appropriate
  -->

<title>Sample HOWTO</title>

<author>
        <firstname>Your Firstname</firstname>
        <surname>Your Surname</surname>
        <affiliation>
                <address><email>your email</email></address>
                </affiliation>
</author>

<editor>
  <firstname>Tabatha</firstname>
  <surname>Marshall</surname>
  <contrib>Language review of version 0.8</contrib>
</editor>

<othercredit role='converter'>
  <firstname>David</firstname>
  <surname>Merrill</surname>
  <contrib>Conversion from HTML to DocBook v3.1 (SGML).</contrib>
</othercredit>

   <pubdate>YYYY-MM-DD</pubdate>

        <revhistory>
                <revision>
                <revnumber>1.0</revnumber>
                <date>YYYY-MM-DD</date>
                <authorinitials>ABC</authorinitials>
                </revremark>first official release</revremark>
                </revision>

                <revision>
                <revnumber>0.9</revnumber>
                <date>YYYY-MM-DD</date>
                <authorinitials>ABC</authorinitials>
                <revremark>First draft</revremark>
                </revision>
        </revhistory>

   <!--
                Provide a good abstract; a couple of sentences is sufficient
   -->

  <abstract>
                <para>
       This is a sample DocBook (SGML or XML) HOWTO which has been
       constructed to serve as a template.
                </para>
        </abstract>

</articleinfo>
     ________________________________________________________________

D.7. Bibliographies

   Not everyone will choose to use the correct formatting for a
   bibliography. Most will use a list of some kind. And that's ok. But
   when you're ready to move to the next level, here's how to do it.

   Below are two examples of bibliographic entries. The first is a very
   simple entry. It has only a title, URL and possibly a short
   description (abstract). The second is a little more complex and is
   for a full entry (for instance a book) with an ISBN, publisher and
   copyright date.

   Note DocBook requirements for bibliographic references


   At least one element within <biblioentry> is required, but it doesn't
   matter which one you have. So you might have a <title>, or a URL
   (<bibliosource>), or an <author>, or, ...

   For a full list of all options, visit
   [http://docbook.org/tdg/en/html/biblioentry.html]
   http://docbook.org/tdg/en/html/biblioentry.html. For more examples
   visit [http://docbook.org/tdg/en/html/bibliography.html]
   http://docbook.org/tdg/en/html/bibliography.html.

   Caution Displaying <abstract> content


   By default <abstract>s do not display on web pages. You need to
   modify the biblio.xsl file. Do a search for the word "abstract" and
   then add this information inside the <xsl:template> tags. If that
   doesn't make sense, don't worry about it too much, but do be aware
   that it's required for the abstracts to show up.
<div xmlns="http://www.w3.org/1999/xhtml" class="{name(.)}">
    <xsl:apply-templates mode="bibliography.mode"/>
</div>

   Example D-11. A Bibliography
<bibliography>
<title>Bibliography title</title>

<bibliodiv>
<title>Section title</title>
<biblioentry>
<title>Book or Web Site Title</title>
<bibliosource><ulink url=""/></bibliosource>
<abstract></abstract>
</biblioentry>

<biblioentry>
<title></title>
<bibliosource><ulink url=""/></bibliosource>
<author><firstname></firstname><surname></surname></author>
<copyright><year></year>
<holder></holder></copyright>
<editor><firstname></firstname><surname></surname></editor>
<isbn></isbn>
<publisher>
<publishername></publishername>
</publisher>
<abstract></abstract>
</biblioentry>
</bibliodiv>
</bibliography>

   View References to see this in action.
     ________________________________________________________________

D.8. Entities (shortcuts, text macros and reusable text)

   There may be some segments of text, or markup that you want to use
   over and over again. Instead of typing it up multiple times (and then
   having to edit it multiple times if you want to make a change) you
   can use external entities. Entities can give you a short cut to:
   reusing whole documents, text snippets, and special markup. Some
   common ways to use an entity would be for:

     * text macros for markup. An example would be a company URL. By
       using a parameter entity you could refer simply to
       &my-company-url; instead of typing out the full <ulink
       url="http://foo.bar">Foo.bar</ulink> each time.
     * software license. Such as the GNU Free Documentation License: it
       is long. And must be included in full in each document. By
       leaving the license in a separate file you can easily include it
       in many documents without having to redo the markup each time.
     * repeated text. For instance an introduction to a topic which is
       included both as a summary in one section and as an introduction
       to the full information in another. Saves on editing time if you
       need to make changes to both sets of text.

   Example D-12. Adding Entities
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
"http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd" [
<-- I can add comments here -->
<!ENTITY shortcut "Replace 'shortcut' with this text.">

<!ENTITY sc-to-a-file SYSTEM "anotherfile.xml">
<-- note: the square bracket on the third line is closed on the next
line--> ]>

   To use these entities simply insert the name you gave the entity
   between a "&" (ampersand) and a ";" (semicolon). For example:
   "&shortcut;" would expand into "Replace 'shortcut' with this text";
   "&sc-to-a-file;" would include the full contents of whatever is in
   anotherfile.xml.

   An important feature while writing a text is the ability to check
   whether or not it will be presented in the final draft. It is common
   to have several parts of the text marked as draft, especially when
   updating an already existing document.

   With the use of parameter entities, you can include or eliminate
   these drafts by altering only one line at the beginning of a
   document.

   Example D-13. Use of parameter entities
<!ENTITY % review "INCLUDE"> ...
<![%review;[ <para>This paragraph will
be included on the draft when the entity "review" is defined with the
value "INCLUDE". </para> ]]>

   The entity review might have several texts defined, as in Example
   D-13. When the changes to the text are considered final, you need
   only to remove parts of the text between the 3^rd. and 6^th. lines.

   To keep the draft definitions and hide the text in the final draft,
   just alter the specification of the entity from INCLUDE to IGNORE.
     ________________________________________________________________

D.9. Customizing your HTML files

D.9.1. HTML file names

   By default, when separate HTML files are made, the SGML processor
   will assign arbitrary names to the resulting files. This can be
   confusing to readers who may bookmark a page only to have it change.
   Whatever your reasoning, here's how to make separate files named the
   way you want:

   In your first <article> tag (which should be the only one) include an
   id parameter and call it "index". This will make your tag look like
   this:
   <article id="index">

   Do not modify the first <chapter> tag, as it's usually an
   introduction and you want that on the first page. For each other
   <section> tag, include the id parameter and name it. A name should
   include only alphanumeric characters, and it should be short enough
   to understand what it is.

        <chapter id="tips">

   Note Pick section IDs intelligently


   We all know that Cool URIs Don't Change. This means your ids should
   not change either. Unless of course the content for the id has
   changed substantially and the id name is no longer relevant.

   Warning HTML file name generation using Jade


   If you are using Jade to transform your DocBook into HTML you must
   use the following parameter: -V %use-id-as-filename%.
     ________________________________________________________________

D.9.2. Headers and Footers

   There is no "easy" way to add headers and footers to your document.
   If you are using DocBook XSL and doing your own document
   transformations you may customize the XSL template to suit your
   needs. For more information read
   [http://www.sagehill.net/docbookxsl/HTMLHeaders.html]
   http://www.sagehill.net/docbookxsl/HTMLHeaders.html.
     ________________________________________________________________

Appendix E. Converting Documents to DocBook XML

   A variety of free and commercial tools exist for doing "up
   conversion" of non-XML formats to DocBook. A few are listed here for
   your convenience. A more comprehensive list is available from
   [http://wiki.docbook.org/topic/ConvertOtherFormatsToDocBook] Convert
   Other Formats to DocBook.
     ________________________________________________________________

E.1. Text to DocBook

   The txt2docbook tool allows one to convert a ascii (README-like) file
   to a valid docbook xml document. It simplifies the publishing of
   rather small papers significantly. The input format was inspired by
   the APT-Convert tool from [http://www.xmlmind.com/aptconvert.html]
   http://www.xmlmind.com/aptconvert.html.

   The script can be downloaded from
   [http://txt2docbook.sourceforge.net/]
   http://txt2docbook.sourceforge.net/.
     ________________________________________________________________

E.2. OpenOffice.org to DocBook

   As of [http://www.openoffice.org] OpenOffice.org (OOo) 1.1RC there
   has been support for exporting files to DocBook format.

   Although OOo uses the full DocBook document type declaration, it does
   not actually export the full list of DocBook elements. It uses a
   "simplified" DocBook tag set which is geared to on-the-fly rendering.
   (Although it is not the official Simplified DocBook which is
   described in Section B.5.) The OpenOffice simplified (or "special"
   docbook) is available from [http://www.chez.com/ebellot/ooo2sdbk/]
   http://www.chez.com/ebellot/ooo2sdbk/.
     ________________________________________________________________

E.2.1. Open Office 1.0.x

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
