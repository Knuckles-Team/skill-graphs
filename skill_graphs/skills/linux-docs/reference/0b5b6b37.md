##  B.4.1. DSSSL
There are three basic requirements to transform a document using DSSSL:
  * The Document Style and Semantics Specification Language files (these are plain text files). [Section B.4.1.1](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#dsssl-files)
  * The Document Type Definition file which matches the DOCTYPE of your document (this is a plain text file). [Section B.5](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#dtd)
  * A processor to do the actual work. [Section B.4.1.2](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#dsssl-processors)


* * *
###  B.4.1.1. The Style Sheets
There are two versions of the Document Style Semantics and Specification Language used by the LDP to transform documents from your raw DocBook files into other formats (which are then published on the Web). The LDP version of the style sheets requires the Norman Walsh version--which basically means if you're using DSSSL the Norman Walsh version can be considered a requirement for system setup.
**Norman Walsh DSSSL** The Document Style Semantics and Specification Language tells Jade (see [Section B.4.1.2](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#dsssl-processors)) how to render a DocBook document into print or on-line form. The DSSSL is what converts a `title` tag into an <h1> HTML tag, or to 14 point bold Times Roman for RTF, for example. Documentation for DSSSL is located at the same site. Note that modifying the DSSSL doesn't modify DocBook itself. It merely changes the way the rendered text looks. The LDP uses a modified DSSSL (see below).
**LDP DSSSL<http://www.tldp.org/authors/tools/ldp.dsl>. **The LDP DSSSL requires the Norman Walsh version (see above) but is a slightly modified DSSSL to provide things like a table of contents.
**Example B-5. "Installing" DSSSL style sheets**
Create a base directory to store everything such as `/usr/share/sgml/`. Copy the DSSSL style sheets into a sub-directory named `dsssl`.
* * *
###  B.4.1.2. DSSSL Processors
There are two versions of the Jade processor: the original version by James Clark; and an open-source version of approximately the same program, OpenJade. You only need _one_ of these programs. It should be installed _after_ the DTD and DSSSL have been "installed."
**DSSSL Transformation Tools**

Jade

Currently, the latest version of the package is `jade-1.2.1.tar.gz`.
Jade is the front-end processor for SGML and XML. It uses the DSSSL and DocBook DTD to perform the verification and rendering from SGML and XML into the target format.

OpenJade

An extension of Jade written by the DSSSL community. Some applications require jade, but are being updated to support either software package.
* * *
###  B.4.1.3. System Setup for DSSSL Transformations
  1. Tell your system where to find the SGML_CATALOG_FILES (yes, even if you are using XML). You can find an example of how to do this in [Example B-1](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-catalog-files).
  2. Download the DSSSL and DTD files and copy them into your working directory. You can find an example of how to do this in [Example B-5](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-dsssl) and [Example B-7](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-dtd).


* * *
###  B.4.1.4. Transformations with DSSSL
Once your system is configured (see the previous section), you should be able to start using jade to transform your files from XML to XHTML.
To create individual HTML files, point jade at the correct DSL (style sheet). The following example uses the LDP style sheet.
```

`bash$ `**jade -t xml -i html \
	-d /usr/local/sgml/dsssl/docbook/html/ldp.dsl#html \
	`_HOWTO.xml_`**

```

---
If you would like to produce a single-file HTML page, add the `_-V nochunks_` parameter. You can specify the name of the final HTML file by appending the command with `_ > `_output.html_`_`.
```

`bash$ `**jade -t xml -i html -V nochunks \
	-d /usr/local/sgml/dsssl/stylesheets/ldp.dsl#html \
	`_HOWTO.sgml_` > output.html**

```

---
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **_Not a function name_ errors**
---|---
|  If you get an error about "is not a function name", you will need to add a pointer to `xml.dcl`. It has to be listed immediately before the pointer to your XML document. Try one of the following locations: `/usr/lib/sgml/declaration/xml.dcl`, or `/usr/share/sgml/declaration/xml.dcl`. Use locate to find the file if it is not in either of those two places. The modified command would be as follows:  | ```

`bash$ `**jade -t xml -i html \
	-d /usr/local/sgml/dsssl/docbook/html/ldp.dsl#html \
	/usr/lib/sgml/declaration/xml.dcl `_HOWTO.xml_`**

```

---
If you would like to create print-friendly files instead of HTML files, simply change the style sheet that you are using. In the file name above, note "html/ldp.dsl" at the end. Change this to "print/docbook.dsl", or if you want XHTML output, instead of HTML, change the file name to "xhtml/docbook.dsl".
* * *
####  B.4.1.4.1. Changing CSS Files
If you want your HTML files to use a specific CSS stylesheet, you will need to edit `ldp.dsl`. Immediately after `;; End of $verbatim-display$ redefinition` add the following lines:
```

(define %stylesheet-type%
  ;; The type of the stylesheet to use
  "text/css")

(define %stylesheet%
  ;; Name of the css stylesheet to use, use value #f if you don't want to
  ;; use css stylesheets
  "base.css")

```

---
Replace `base.css` with the name of the CSS file you would like to use.
* * *
##  B.4.2. The docbook-utils Package
The docbook-utils provide commands like **db2html** , **db2pdf** and **db2ps** , based on the **jw** scripts, that is a front-end to Jade. These tools ease the everyday management of documentation and add comfortable features.
The package, originally created by RedHat and available from
**Example B-6. Example creating HTML output**
After validating your document, simply issue the command **db2html` mydoc.xml`** to create (a) HTML file(s). You can also use the docbook-utils as validation tools. Remember: when errors occur, always start by solving only the first problem. The rest of the problems may be fixed when you fix the first error.
If you get errors about a function name, please read .
* * *
###  B.4.2.1. Using CSS and DSL for pretty output
You can define your own additional DSL instructions, which can include a pointer to a personalized CSS file. Sample DSL and CSS files are provided in [Appendix A](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#templates).
The sample DSL file will create a table of contents, and have all HTML files start with the prefix `intro2linux-` and end with a suffix of `.html`. The `%stylesheet%` variable points to the CSS file which should be called by your HTML file.
To use a specific DSL style sheet the following command should be used:
**db2html` -d` `mystyle.dsl` `mydoc.xml`**
You can compare the result here:
* * *
##  B.4.3. XSL
There are alternatives to DSSSL and Jade/OpenJade.
When working with DocBook XML, the LDP offers a series of XSL[[2]](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#FTN.AEN2259) style sheets to process documents into HTML. These style sheets create output files using the XML tool set that are similar to those produced by the SGML tools using [ldp.dsl](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#dsssl).
The major difference between using `ldp.dsl` and the XSL style sheets is the way that the generation of multiple files is handled, such as the creation of a separate file for each chapter, section and appendix. With the SGML tools, such as jade or openjade, the tool itself was responsible for generating the separate files. Because of this, only a single file, `ldp.dsl` was necessary as a customization layer for the standard DocBook DSSSL style sheets.
With the DocBook XSL style sheets, generation of multiple files is controlled _by the style sheet_. If you want to generate a single file, you call one style sheet. If you want to generate multiple files, you call a different style sheet. For that reason the LDP XSL style sheet distribution is comprised of four files:
  1. `tldp-html.xsl` - style sheet called to generate a _single_ file.
  2. `tldp-html-chunk.xsl`[[3]](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#FTN.AEN2280) - style sheet called to generate multiple files based on chapter, section and appendix elements.
  3. `tldp-html-common.xsl` - style sheet containing the actual XSLT transformations. It is called by the other two HTML style sheets and is _never_ directly called.
  4. `tldp-print.xsl` - style sheet for generation of XSL Formatting Objects for print output.


You can find the latest copy of the files at `html` directory of TLDP-XSL and put them in the `html` directory of Norman Walsh's stylesheets. Take the file from the TLDP-XSL `fo` directory and put it in the Norman Walsh `fo` directory.
Once you have installed these files you can use xsltproc to generate HTML files from your XML documents. To transform your XML file(s) into a single-page HTML document use the following command:
```

`bash$` ** xsltproc -o `_HOWTO.html_` /usr/local/sgml/stylesheets/tldp-html.xsl `_HOWTO.xml_`**

```

---
To generate a set of linked HTML pages, with a separate page for each `chapter`, `sect1` or `appendix`, use the following command:
```

`bash$ `**xsltproc /usr/share/sgml/stylesheets/tldp-html-chunk.xsl `_HOWTO.xml_`**

```

---
Note that you never directly call the style sheet `tldp-html-common.xsl`. It is called by both of the other two style sheets.
* * *
###  B.4.3.1. Changing CSS Files
If you want your HTML files to use a specific CSS stylesheet, you will need to edit `tldp-html-common.xsl`. Look for a line that ressembles `<xsl:param name="html.stylesheet" select="'style.css'"/>`.
Replace `style.css` with the name of the CSS file you would like to use.
* * *
#  B.5. DocBook DTD
The DocBook DTD defines the structure of a DocBook document. It contains rules about how the elements may be used; and what the elements ought to be describing. For example: it is the DocBook DTD which states all `warning`s are to _warn_ the reader (this is the definition of the element); and may not contain plain text (this is the content model--and the bit which forces you to wrap your warning text in a `para` or perhaps a list).
![Caution](https://tldp.org/LDP/LDP-Author-Guide/images/caution.gif) | **Versions**
---|---
|  It is important that you download the version(s) that match your document. You may want to configure your system now to deal with "all" DocBook DTDs if you are going to be editing older LDP documents. If you are a new author, you only need the first one listed: XML DTD for DocBook version 4.2.
The XML DTD is available from
If you are going to be working with SGML versions of DocBook you will need one (or both) of:
**Example B-7. "Installing" DocBook Document Type Definitions**
Create a base directory to store everything such as `/opt/local/sgml/`. Copy the DTDs into a sub-directory named `dtd`.
![Warning](https://tldp.org/LDP/LDP-Author-Guide/images/warning.gif) | **Do not edit DTD files**
---|---
|  The DocBook standard is described in these files. If you change these files, you are no longer working with DocBook.
* * *
#  B.6. Formatting Documents
##  B.6.1. Inserting a summary on the initial articles page
A feature that might be valuable in some cases is the insertion of the summary on the initial page of an article. DocBook articles do not include it as a standard feature.
To enable this, it is necessary to modify the style sheet file.
**Example B-8. Style sheet to insert summaries in articles**
```

<!DOCTYPE style-sheet PUBLIC "-//James Clark//DTD DSSSL Style Sheet//EN" [
<!entity html-docbook PUBLIC "-//Norman Walsh//DOCUMENT DocBook HTML Stylesheet//EN" CDATA DSSSL>
<!entity print-docbook PUBLIC "-//Norman Walsh//DOCUMENT DocBook Print Stylesheet//EN" CDATA DSSSL>
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


```

---
* * *
##  B.6.2. Inserting indexes automatically
Although DocBook has markups for the composition of them, indexes are not generated automatically. The **collateindex.pl** command allows indexes to be generated from the source DocBook for inclusion into the finished/transformed document.
  1. Process the document with jade using the style to _HTML_ with the option `-V html-index`.
```

`bash$` **jade** `-t sgml \
	-d html/docbook.dsl -V html-index document.sgml`

```

---
  2. Generate the `index.sgml` file with **collateindex.pl**.
```

`bash$ ` **perl** `collateindex.pl \
	-o index.sgml HTML.index`

```

---


For the above example to work, it is necessary to define an _external entity_ by calling the file `index.sgml`.
**Example B-9. Configuring an external entity to include the index**
```

`<!DOCTYPE article PUBLIC "-//OASIS//DTD
DocBook V3.1//EN" [

<!-- Insertion of the index --> <!entity index SYSTEM
"index.sgml"> ]>`

```

---
See also [Section D.4](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#encoding-index) for information on how to insert necessary information on the text.
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Odd behavior generating indexes for print versions**
---|---
| Remember that if you're trying to get Tables of Contents or Indexes on PS or PDF output you'll need to run jadetex or pdfjadetex at least three times. This is required by TeX but not by DocBook or related applications.
* * *
#  Appendix C. Concurrent Version System (CVS)
The LDP provides optional CVS access to its authors. This enables collaborative writing and has the following positive effects:
  1. CVS will keep an off-site backup of your documents. In the event that you hand over a document to another author, they can just retrieve the document from CVS and continue on. In the event you need to go back to a previous version of a document, you can retrieve it as well.
  2. However difficult from an organizational point of view, it's great to have multiple people working on the same document. CVS enables you to do this. You can have CVS tell you what changes were made by another author while you were editing your copy, and integrate those changes.
  3. CVS keeps a log of what changes were made. These logs (and a date stamp) can be placed automatically inside your documents when they are published.
  4. CVS can be combined with scripts to automatically update the LDP web site with new documentation as it's written and submitted. This is not in place yet, but it is a goal. Currently, CVS updates signal the HOWTO coordinator to update the LDP web page, meaning that if you use CVS, you're not required to e-mail your XML code. (Although you do still need to send the submit list an email when you are ready for your document to be published, because the whole publishing process has not been fully automated yet.)


![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Access to our CVS repository**
---|---
| Only authors with at least three submissions get access to our CVS, see [Appendix C](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#cvs).
You can browse the LDP CVS repository via the web at <http://cvs.tldp.org/>.
* * *
#  C.1. Getting a CVS account
![Caution](https://tldp.org/LDP/LDP-Author-Guide/images/caution.gif) | **CVS accounts will not be granted to all applicants**
---|---
|  To be granted a CVS account you must qualify under one of the following categories:
  * authors with documents already in the collection who have made a minimum of three submits to the LDP through `<`
  * technical and language reviewers approved by one of the Review Coordinators
  * new authors in the review process (also requires approval from one of the Review Coordinators)

Please do not apply for a CVS account if you do not qualify.
If you qualify for a CVS account you may apply for one contacting CVS master Sergiusz
* * *
#  C.2. Using CVS
##  C.2.1. Setting Up Your CVS Account
First you'll need to get an account at the LDP's CVS Repository. Please see the notes above on obtaining an account. This repository houses various documents including HOWTOs and Guides. Documents are sorted by the type of document (for example a HOWTO or a Guide), and by the markup language the document uses (for example DocBook or LinuxDoc).
When your account is ready you can log in using one of the following commands. In all instances `_your_userid_` should be replaced by the user name you were issued in the response email. You will be prompted for a password after this first step.
**Initializing Your CVS Account**

Linux system

**cvs` _-d :pserver:`_your_userid_` @cvs.tldp.org:/cvsroot_` login**

Windows system

**set` CVSROOT`=":pserver:`_your_userid_` @cvs.tldp.org:/cvsroot"**
**cvs` _-d %CVSROOT%_` login**
Wait patiently while the system tries to log you in. It can often take more that 10-20 seconds for the system to either accept (or reject) your password. Once you've used **cvs login** for the first time and have been given access to the system, your password is stored in `.cvspass` and you will not have to use **cvs login** again. Just set the CVSROOT with the export command listed above and continue on. If TLDP's CVS server is the only one you work with, you might also add an **export` CVSROOT`** line to your `~/.bashrc` shell configuration file.
* * *
##  C.2.2. Getting the Documents
You can get the entire repository (about 150 MB) with: **cvs checkout LDP**
Or you can get the source for your own document with: **cvs checkout LDP/howto/docbook/YOUR-HOWTO.xml** OR **cvs checkout LDP/guide/docbook/YOURGUIDE**
Windows users will need to use a modified version of this command. Instead they should use: **cvs -d %CVSROOT% checkout LDP/howto/docbook/YOUR-HOWTO.xml**
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Keep an overview**
---|---
|  **checkout** will add the full directory structure from tldp.org on down. Although it doesn't really matter where you put these files on your local file system you may not want to bury the directories too deeply.
* * *
##  C.2.3. CVS Commands
**CVS Commands: a brief reminder**

commit

This CVS command will upload your changes to the CVS server.
Please be sure to include a useful description of the changes that have been made to your document.
If you want to bypass the editor screen you can use
**cvs` commit` `-m "A description of the work done on this version of the document."` **
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Ready for publication warning**
---|---
| You must still email `<` when you are ready to have your changes appear on the live site. Your email should include the relative path to the file(s) in the LDP CVS tree that you wish to update.

add

You can add new files to your CVS repository. These may be image files or additional XML files. First check that your HOWTO is in its own directory. You may want to coordinate with the people at `<` to ensure you can add graphics or other files to your HOWTO.
Copy the files you want to add into your local CVS repository (where all of your downloaded/working files are). Then:
**cvs add` _filename_`**
After you've added the files, you still need to **commit** them to the repository (see above).

remove


$Id: cvs.xml,v 1.32 2011/01/14 16:24:52 serek Exp $

While this is not a CVS "command" it can be used to automatically insert information about the file including the time and date it was last modified, the version number it was assigned by the CVS and the filename of this particular file. The output will look like this: `$Id: cvs.xml,v 1.9 2002/04/21 09:44:26 serek Exp $`
If you need to change a file name, you still need to use the **add** command. First remove the copy of the file from your local disk. Then remove it from the CVS tree with: **cvs remove` _filename_`**. As with the **add** command, you need to **> commit** your removed file. Finally, now that the old file has been removed, add your new file using the instructions above (first **add** and then **commit** the additional file).
* * *
###  C.2.3.1. Recovering old versions
There you are, typing away, when you screw up. Real bad. Doesn't matter what it is, but suffice it to say that you've toasted not only the version on your local drive, but created a new version on the CVS server. What you need to do is go back in time and resurrect an older version of your file.
To do this, you'll need to know the version number of the file you want to retrieve. **cvs diff** will give a list of revisions if there are differences. You can pick the revision number, subtract one, and that is probably the revision you want to look at.
The command
**cvs -Q update -p -r` _revision_` `_filename_`**
will output to stdout the contents of the `_revision_` version of `_filename_`. You can pipe it to **more** or redirect the output to a file. Conveniently, you can redirect stdout to a file called `_filename_`. Your local file is now the revision you want, and
**cvs update**
will update the CVS server with the new (old) version of `_filename_`.
* * *
#  C.3. CVS Resources
If you're completely new to CVS, there are a few web pages you may want to look at which can help you out:
* * *
#  Appendix D. DocBook: Sample Markup
#  D.1. General Tips and Tricks
For a general overview of what markup is all about, please read [Chapter 5](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ag-markup)
  * An editor capable of inserting elements according to the DTD will help a lot since it will enforce the DTD. This way you can be sure that no invalid elements were added anywhere in your document.
  * In order to ensure that future changes are as easy as possible, authors should try to keep compatibility with the XML version of the DocBook DTD. This means keeping element names in lower case, using double quotes in all attributes, and not omitting end tags. Most tools that automatically insert elements (like psgml+emacs) follow these rules automatically or with some fine tuning.
  * Each type of document created has a specific structure. This document is in "book" format. Most authors, however, will want to use the shorter "article" format instead. Templates are available from [Appendix A](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#templates).


* * *
##  D.1.1. Useful markup
[Table D-1](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#table-useful-markup) shows some markup that is useful for generating generic documents. Remember that some elements are valid only on some contexts.
![Tip](https://tldp.org/LDP/LDP-Author-Guide/images/tip.gif) | **Check several formats**
---|---
| Sometimes the appearance of a particular tag changes from one conversion format to another. As a beginner in DocBook writing, you may wish to see how your document looks in several formats before you publish them. You are advised to look at how your document is presented in HTML, PDF and PostScript, since these formats will be made available by TLDP once you publish your document.
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Better too much than not enough**
---|---
| Since the formatting depends on the output style chosen, it's recommended to use as much markup as possible. Even if the appearance of the output doesn't seem to change with the standard output style, there may be specific output formats that will make these tags stand out.
**Table D-1. Useful markup**
Description | Sample markup | Result
---|---|---
E-mail address |  `<email>`address@domain`</email>` | `<`
About the author |  `<author>`...`</author>` | (see example below)
Author's name | | ```

`<firstname>`Mary`</firstname>`
`<othername>`Margaret`</othername>`
`<surname>`O'Hara`</surname>`

```

---
Mary Margaret O'Hara
Keys' name (printings on the keyboard) |  `<keycap>`F1`</keycap>` | **F1**
Symbol represented by the keys |  `<keysym>`KEY_F1`</keysym>` | KEY_F1
Key's code |  `<keycode>`0x3B`</keycode>` | 0x3B
Combinations or sequences of keys | | ```

`<keycombo>`
   `<keycap>`Ctrl`</keycap>`
   `<keycap>`S`</keycap>`
`</keycombo>`

```

---
**Ctrl** -**S**
Program Menus |  `<guimenu>`File`</guimenu>` | File
Menu Items |  `<guimenuitem>`Save`</guimenuitem>` | Save
Menu Sequences | | ```

`<menuchoice>`
   `<shortcut>`
      `<keycombo>`
         `<keycap>`Ctrl`</keycap>`
         `<keycap>`S`</keycap>`
      `</keycombo>`
   `</shortcut>`
   `<guimenu>`File`</guimenu>`
   `<guimenuitem>`Save`</guimenuitem>`
`</menuchoice>`

```

---
File->Save (****Ctrl** -**S****)
Mouse Button |  `<mousebutton>`left`</mousebutton>` | left
Application Names |  `<application>`application`</application>` | application
Text Bibliographical Reference |  `<citation>`reference`</citation>` | [reference]
Quote | | ```

`<blockquote>`
   `<attribution>`Text Author`</attribution>`
   `<para>`Quote Text.`</para>`
`</blockquote>`

```

---
|  | Quote Text. |
---|---|---
--Text Author |
Index | (NA) | See [Section D.4](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#encoding-index).
File Names | | ```

`<filename>`file`</filename>`
```

---
`file`
Directories | | ```

`<filename id="directory">`directory`</filename>`
```

---
`directory/`
Emphasize Text[[a]](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#FTN.AEN2768) | | ```

`<emphasis>`text`</emphasis>`
```

---
_text_
Footnotes | | ```

`<footnote>`
   `<para>`Footnote text`</para>`
`</footnote>`
```

---
(See note at the end of this table for an example)
URLs | | ```

`<ulink url="http://www.conectiva.com">`Conectiva S.A.`</>`
```

---
Itemized (unnumbered) List | | ```

`<itemizedlist>`
   `<listitem>`
      `<para>`item`</para>`
   `</listitem>`
   `<listitem>`
      `<para>`item`</para>`
   `</listitem>`
`</itemizedlist>`

```

---
  * item
  * item


Ordered (numbered) List | | ```

`<orderedlist>`
   `<listitem>`
      `<para>`item`</para>`
   `</listitem>`
   `<listitem>`
      `<para>`item`</para>`
   `</listitem>`
`</orderedlist>`

```

---
  1. item
  2. item


Segmented List | | ```

`<segmentedlist>`
   `<title>`Binary to decimal conversion`</title>`
   `<segtitle>`Binary`</segtitle>`
   `<segtitle>`Decimal`</segtitle>`
   `</seglistitem>``<seg>`00`</seg>``<seg>`0`</seg>`
   `</seglistitem>`
   `<seglistitem>``<seg>`01`</seg>``<seg>`1`</seg>`
   `</seglistitem>`
   `<seglistitem>``<seg>`10`</seg>``<seg>`2`</seg>`
   `</seglistitem>`
`</segmentedlist>`

```

---
**Binary to Decimal Conversion** **Binary:** 00 **Decimal:** 0 **Binary:** 01 **Decimal:** 1 **Binary:** 10 **Decimal:** 2
Variable List | | ```

`<variablelist>`
   `<varlistentry>`
      `<term>`Entry 1`</term>`
      `<listitem>`
         `<para>`Description`</para>`
      `</listitem>`
   `</varlistentry>`
   `<varlistentry>`
      `<term>`Entry 2`</term>`
      `<listitem>`
         `<para>`Description`</para>`
      `</listitem>`
   `</varlistentry>`
`</variablelist>`

```

---

Entry 1
    Description

Entry 2
    Description
Simple Lists | | ```

`<simplelist type="horiz" columns="3">`
   `<member>`1`</member>`
   `<member>`2`</member>`
   `<member>`3`</member>`
   `<member>`4`</member>`
   `<member>`5`</member>`
   `<member>`6`</member>`
`</simplelist>`
`<simplelist type="inline">`
   `<member>`A`</member>`
   `<member>`B`</member>`
   `<member>`C`</member>`
   `<member>`D`</member>`
   `<member>`E`</member>`
   `<member>`F`</member>`
`</simplelist>`

```

---
| 1 | 2 | 3
---|---|---
4 | 5 | 6
Pictures | (NA) | See [Section D.5](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#inserting-pictures)
Glossary | | ```

`<glossentry>`
   `<glossterm>`Term`</glossterm>`
   `<glossdef>`
      `<para>`Definition`</para>`
   `</glossdef>`
`</glossentry>`
```

---
(See the glossary at the end of this document)
Crossed References | | ```

`<section id="secao">`
...
`</section>`
`<section id="reference the other section">`
...
`<para>`Please, see`<xref linkend="secao" />` for more information.
```

---
(NA)
Notes:
a. Text can be emphasized in a few ways. The most common ways are italics and bold. DocBook, however, supports only italics. The use of bold requires additional settings on the style sheet used.

* * *
#  D.2. `<section>` and `<sectN>`: what's the difference?
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Acknowledgment**
---|---
|  These notes were provided by: `<`).
`<section>` versus `<sectN>` is largely a question of flexibility. The stylesheets can make a `<section>` in a `<section>` look just like a `<sect2>` within a `<sect1>`, so there's no output advantage.
But, a `<section>` within a `<section>` can be extracted into its own top-level section, nested even more deeply, or moved to an entirely different part of the document, without it and its own `<section>` children being renamed. That is not true of the numbered section tags, which are very sensitive to rearrangements. This can be easier for authors who are new to DocBook than using `<sectN>`.
The main idea behind creating structured data is that it should be easy to access and query. One should be able to retrieve a subsection of any structured data, by using querying languages for XML (XPath and XQuery). `<sectN>` are useful when traversing a document using XPath/XQuery. `<sectN>` gives more flexibility, and control while writing an XPath expression.
A well-defined, valid and well-structured document makes it easier for one to write XPath/Query to retrieve "specific" data from a document. For example you can use XPath to retrieve information in the `<sect3>` block with certain attributes. However if you just used `<section>` for all subsections, it becomes harder to retrieve the block of information that you need.
So which one should you use? The one you feel most comfortable with is a good place to start. This document is written with `<section>`s. You may, or may not, think this is a good idea. :)
* * *
#  D.3. Command Prompts
There are likely as many ways of doing this as there are DocBook authors; however, here are two ways that you might find useful. Thanks to
**Example D-1. Command Prompt with` programlisting`**
```

`<programlisting>`
	`<prompt>`# `</prompt>``<userinput>``<command>`cd`</command>` /some/dir`</userinput>`
	`<prompt>`# `</prompt>``<userinput>``<command>`ls`</command>` -l`</userinput>`
`</programlisting>`

```

---
Displays as:
```

`# ``****cd** /some/dir**`
`# ``****ls** -l**`

```

---
**Example D-2. Command Prompt with` screen`**
First create a general entity in the internal subset at the very beginning of your document. This entity will define a name for the shortcut which you can use to display the full prompt at any point in your document. `<!ENTITY prompt "<prompt>[user@machine ~/dir]$</prompt>">`
For more information about entities, read [Section D.8](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools-entities).
```

`<screen>`
&prompt; `<userinput>`cd /some/dir`</userinput>`
&prompt; `<userinput>`ls -l`</userinput>` `</screen>`

```

---
Displays as:
```

`[user@machine ~/dir]$ ``**cd /some/dir**`
`[user@machine ~/dir]$ ``**ls -l**`

```

---
If you would like to add the output of your commands you can add `<computeroutput>` text`</computeroutput>` within the `<screen>` or `<programlisting>` as appropriate.
* * *
#  D.4. Encoding Indexes
The generation of indexes depends on the markups inserted in the text.
Such markups will be processed afterwards by an external tool and will generate the index. An example of such a tool is the `collateindex.pl` script (see [Section B.6.2](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#automatic-indexes)). Details about the process used to generate these indexes are shown in [Section B.6.2](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#automatic-indexes).
The indexes have nesting levels. The markup of an index is done by the code [Example D-3](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#example-code-index).
**Example D-3. Code for the generation of an index**
```

`<indexterm>`
   `<primary>`Main level`</primary>`
   `<secondary>`Second level`</secondary>`
	`<tertiary>`Third level`</tertiary>`
	`</indexterm>`

```

---
It is possible to refer to chapters, sections, and other parts of the document using the _attribute_ `zone`.
**Example D-4. Use of the attribute` zone`**
```

`<section id="encoding-index">`
`<title>`Encoding Indexes`</title>`
`<indexterm zone="encoding-index">`
`<primary>`edition`</primary>` `<secondary>`index`</secondary>`
`</indexterm>`

`<para>`
	The generation of indexes depend on the inserted markups on the text.
`</para>`

```

---
The [Example D-4](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#index-zone) has the code used to generate the entry of this edition on the index. In fact, since the attribute `zone` is used, the index statement could be located anywhere in the document or even in a separate file.
However, to facilitate maintenance the entries for the index were all placed after the text to which it refers.
**Example D-5. Usage of values` startofrange` and `endofrange` on the attribute`class`**
```

    `<para>`Typing the text normally
    sometimes there's the need of
   `<indexterm class="startofrange"
   id="example-band-index">`
      `<primary>`examples`</primary>` `<secondary>`index`</secondary>`
   `</indexterm>` mark large amounts of
   text.`</para>`

   `<para>`Keep inserting the paragraphs
   normally.`</para>`

   `<para>`Until the end of the section
   intended to be indexed.  `<indexterm
   startref="example-band-index" class="endofrange">`.
   `</para>`
```

---
* * *
#  D.5. Inserting Pictures
It is necessary to insert pictures formats for all possible finished document types. For example: JPG files for web pages and EPS for PostScript and PDF files.
If you use the TeX format you'll need the images as a PostScript file. For on-line publishing you can use any kind of common image file, such as JPG, GIF or PNG.
The easiest way to insert pictures is to use the `fileref` attribute. Usually pictures are generated in JPG and in PostScript (PS or EPS).
**Example D-6. Inserting a picture**
```

`<figure>`
   `<title>`Picture's
   Title`</title>` `<graphic fileref="images/file">``</graphic>`
`</figure>`
```

---
Replacing `<figure>` by `<informalfigure>` eliminates the need to insert a title for the picture.
There's still the `float` attribute on which the value `0` indicates that the picture should be placed exactly where the tag appears. The value `1` allows the picture to be moved to a more convenient location (this location can be described on the style sheet, or it can be controlled by the application).
* * *
##  D.5.1. Graphics formats
When submitting graphics to the LDP, please submit one set of graphics in `.eps`, and another in `.gif`, `.jpg` or ` .png`. The preferred format is ` .png` or `.jpg` due to patent problems with `.gif`.
You can use `.jpg` files for continuous-tone images such as photos or images with gradual changes in color. Use `.png` for simple images like diagrams, some screen shots, and images with a low number of colors.
* * *
##  D.5.2. Alternative Methods
The first alternative to [Example D-6](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-picture-fileref) is to eliminate the `<figure>` or `<informalfigure>` elements.
Another interesting alternative when you have decided to publish the text on media where pictures are not accepted, is the use of a wrapper, `<imageobject>`.
**Example D-7. Using` <imageobject>`**
```

`<figure>`
   `<title>`Title`</title>`
   `<mediaobject>`
      `<imageobject>`
	 `<imagedata fileref="images/file.eps" format="EPS">`
      `</imageobject>`
   `<imageobject>`
	 `<imagedata fileref="images/file.jpg" format="JPG">`
      `</imageobject>`
      `<textobject>`
	 `<phrase>`Here there's an image of this example`</phrase>`
      `</textobject>`
   `<caption>`
   `<para>`Image Description. Optional. `</para>`
   `</caption>`
   `</mediaobject>`
`</figure>`
```

---
Files using the following formats are available BMP, CGM-BINARY, CGM-CHAR, CGM-CLEAR, DITROFF, DVI, EPS, EQN, FAX, GIF, GIF87A, GIF89A, IGES, JPEG, JPG, LINESPECIFIC, PCX, PIC, PS, SGML, TBL, TEX, TIFF, WMF, WPG.
This method presents an advantage: a better control of the application. The elements `<imageobject>` are consecutively tested until one of them is accepted. If the output format does not support images the `<textobject>` element will be used. However, the biggest advantage in usage of the format [Example D-7](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#former-figure-imageobject) is that in DocBook `5.0`, the `<graphic>` element will cease to exist.
As a disadvantage, there is the need for more than one representation code of the same information. It is up to the author to decide how they will implement illustrations and pictures in the document, but for compatibility with future versions _I recommend_ the use of this method for pictures and graphics.
![Warning](https://tldp.org/LDP/LDP-Author-Guide/images/warning.gif) | **Title page exception**
---|---
|  `<mediaobject>`s will not display if they are used on a title page. For more information read:
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **ASCII Images**
---|---
|  You may also want to try converting your image to an ASCII representation of the file. JavE (Java ASCII Versatile Editor) can do this conversion for you. It can be downloaded from  If you're more command-line oriented you may want to try: tgif (
* * *
#  D.6. Markup for Metadata
##  D.6.1. Crediting Translators, Converters and Co-authors
There are several ways that these folks, as well as other contributors to your document, can be given some recognition for the help they've given you.
* * *
###  D.6.1.1. `<othercredit>`
All translators, converters and co-authors should be credited with an `<othercredit>` tag entry. To properly credit a translator or converter, use the `<othercredit>` tag with the `role` attribute set to "converter" or "translator", as indicated in the example below:
**Example D-8. Other Credit**
```

`<othercredit role='converter'>`
  `<firstname>`David`</firstname>`
  `<surname>`Merrill`</surname>`
  `<contrib>`Conversion from HTML to DocBook v3.1 (SGML).`</contrib>`
`</othercredit>`

```

---
* * *
###  D.6.1.2. Crediting Editors and Reviewers
To help track the review process all new documents must include a reference to the reviewers for the [technical](http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/techreview.html), [language](http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/languagereview.html) and [metadata](http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/metadatareview.html) reviews.
**Example D-9. Editor**
```

`<editor>`
  `<firstname>`Tabatha`</firstname>`
  `<surname>`Marshall`</surname>`
  `<contrib>`Language review of version 0.8`</contrib>`
`</editor>`

```

---
* * *
##  D.6.2. `<revremark>`s
Within the `<revision>` tag hierarchy is a tag called `<revremark>`. Within this tag, you can make any brief notes you wish about each particular revision of your document.
* * *
##  D.6.3. Revision History
The `<revhistory>` tag should be used to denote the various revisions of the document. Specify the date, revision number and comments regarding what has changed.
Revisions should be listed with the most-recent version at the top (list in descending order).
* * *
##  D.6.4. Date formats
The `<pubdate>` tag in your header should list the publication date of this particular version of the document (coincide with the revision date). It should be in the following format:
```
`<pubdate>`2002-04-25`</pubdate>`
```

---
The date is in the format YYYY-MM-DD, which is one of the
* * *
##  D.6.5. Sample Article (or Book) Information Element
Here is a sample of a complete DocBook (SGML or XML) `<articleinfo>` element which contains some of the items and constructs previously described.
**Example D-10. Sample Meta Data**
```

<!--
   Above these lines in a typical DocBook article would be the article
   element (the immediate parent of the articleinfo element) and above
   that typically, the DOCTYPE declaration and internal subset.
  -->

`<articleinfo>`

  <!--
  	Use "HOWTO", "mini HOWTO", "FAQ" in title, if appropriate
  -->

`<title>`Sample HOWTO`</title>`

`<author>`
	`<firstname>`Your Firstname`</firstname>`
	`<surname>`Your Surname`</surname>`
	`<affiliation>`
		`<address>``<email>`your email`</email>``</address>`
		`</affiliation>`
`</author>`

`<editor>`
  `<firstname>`Tabatha`</firstname>`
  `<surname>`Marshall`</surname>`
  `<contrib>`Language review of version 0.8`</contrib>`
`</editor>`

`<othercredit role='converter'>`
  `<firstname>`David`</firstname>`
  `<surname>`Merrill`</surname>`
  `<contrib>`Conversion from HTML to DocBook v3.1 (SGML).`</contrib>`
`</othercredit>`

   `<pubdate>`YYYY-MM-DD`</pubdate>`

	`<revhistory>`
		`<revision>`
		`<revnumber>`1.0`</revnumber>`
		`<date>`YYYY-MM-DD`</date>`
		`<authorinitials>`ABC`</authorinitials>`
		`</revremark>`first official release`</revremark>`
		`</revision>`

		`<revision>`
		`<revnumber>`0.9`</revnumber>`
		`<date>`YYYY-MM-DD`</date>`
		`<authorinitials>`ABC`</authorinitials>`
		`<revremark>`First draft`</revremark>`
		`</revision>`
	`</revhistory>`

   <!--
		Provide a good abstract; a couple of sentences is sufficient
   -->

  `<abstract>`
		`<para>`
       This is a sample DocBook (SGML or XML) HOWTO which has been
       constructed to serve as a template.
		`</para>`
	`</abstract>`

`</articleinfo>`

```

---
* * *
#  D.7. Bibliographies
Not everyone will choose to use the correct formatting for a bibliography. Most will use a list of some kind. And that's ok. But when you're ready to move to the next level, here's how to do it.
Below are two examples of bibliographic entries. The first is a very simple entry. It has only a title, URL and possibly a short description (abstract). The second is a little more complex and is for a full entry (for instance a book) with an ISBN, publisher and copyright date.
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **DocBook requirements for bibliographic references**
---|---
|  At least one element within `<biblioentry>` is required, but it doesn't matter which one you have. So you might have a `<title>`, or a URL (`<bibliosource>`), or an `<author>`, or, ...  For a full list of all options, visit
![Caution](https://tldp.org/LDP/LDP-Author-Guide/images/caution.gif) | **Displaying` <abstract>` content**
---|---
|  By default `<abstract>`s do not display on web pages. You need to modify the `biblio.xsl` file. Do a search for the word "abstract" and then add this information inside the <xsl:template> tags. If that doesn't make sense, don't worry about it too much, but do be aware that it's required for the abstracts to show up.  | ```

<div xmlns="http://www.w3.org/1999/xhtml" class="{name(.)}">
    <xsl:apply-templates mode="bibliography.mode"/>
</div>

```

---
**Example D-11. A Bibliography**
```

`<bibliography>`
`<title>`Bibliography title`</title>`

`<bibliodiv>`
`<title>`Section title`</title>`
`<biblioentry>`
`<title>`Book or Web Site Title`</title>`
`<bibliosource>``<ulink url=""/>``</bibliosource>`
`<abstract>``</abstract>`
`</biblioentry>`

`<biblioentry>`
`<title>``</title>`
`<bibliosource>``<ulink url=""/>``</bibliosource>`
`<author>``<firstname>``</firstname>``<surname>``</surname>``</author>`
`<copyright>``<year>``</year>`
`<holder>``</holder>``</copyright>`
`<editor>``<firstname>``</firstname>``<surname>``</surname>``</editor>`
`<isbn>``</isbn>`
`<publisher>`
`<publishername>``</publishername>`
`</publisher>`
`<abstract>``</abstract>`
`</biblioentry>`
`</bibliodiv>`
`</bibliography>`

```

---
View [_References_](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#bibliography) to see this in action.
* * *
