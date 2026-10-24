          using DocBook please read Section D.6

   Acknowledgments
          Give credit where credit is due. For more information about
          when to give credit, read Section 6.3.

   License and Copyright
          The LDP distributes documents, however, the author maintains
          the copyright on the document. All documents accepted by the
          LDP must contain a license and copyright notice. You can read
          more about this in Section 6.2.1. You may also want to add a
          Disclaimer, but this is optional. More about this in Section
          6.2.2.

   Validate the Markup
          If you are submitting a DocBook or LinuxDoc document, make
          sure the markup is valid. Read why in Section B.3.1.

   Obtain Peer Reviews
          You may want to have others review your document before
          submitting it to the LDP. Ask people for a Peer Review and/or
          a Technical Accuracy Review. Since not all mailing lists will
          respond favorably to attachments, you may wish to set up a
          temporary web site which houses your document. Note: this is
          absolutely not required.
     ________________________________________________________________

6.2. Licensing and Copyright

   In order for a document to be accepted by the LDP, it must be
   licensed and conform to the "LICENSE REQUIREMENTS" section of the LDP
   Manifesto located at [http://www.tldp.org/manifesto.html]
   http://www.tldp.org/manifesto.html.

   We recommend using the GNU Free Documentation License (GFDL), one of
   the Creative Commons Licenses
   ([http://creativecommons.org/licenses/sa/1.0/] Share-Alike, or
   [http://creativecommons.org/licenses/by-sa/2.0/]
   Attribution-Share-Alike), or the LDP license (currently under
   review). The full text of the license must be included in your
   document, including the title and version of the license you are
   using. The LDP will not accept new documents that do not meet
   licensing requirements.

   Warning Debian-compatible licenses


   The Debian package maintainer for LDP documents has divided the LDP
   documents into those with a "free" license and those with a
   "non-free" license. For a summary of this list, please read
   [http://www.debian.org/legal/licenses/byname] Debian License
   Summaries. Currently the Artistic License, BSD License and the GNU
   General Public License are listed as "free". These licenses will also
   be accepted by the LDP. The definition of "non-free" has not been
   made transparent. By choosing another license that has any kind of
   restriction on redistribution or whether or not the document may be
   modified, your document may be put into the "non-free" package
   instead of the "free" package. We are working with Debian to clarify
   how these decisions are made.

   You can get DocBook markups of both the GNU GPL and the GNU FDL from
   [http://developer.gnome.org/projects/gdp/licenses.html] the GNOME
   Documentation Project. You can then merely include the license in its
   entirety in your document. A DocBook-formatted copy of the license is
   available in Appendix A.

   For more information about open source documentation and licensing,
   please check .
     ________________________________________________________________

6.2.1. Copyright

   As an author, you may retain the copyright and add other restrictions
   (for example: require approval for any translations or derivative
   works). If you are a new maintainer of an already-existing HOWTO, you
   must include the previous copyright statements of the previous
   author(s) and the dates they maintained that document.
     ________________________________________________________________

6.2.2. Disclaimer

   If you would like to include a disclaimer, you may choose to use the
   following:

     No liability for the contents of this document can be accepted.
     Use the concepts, examples and information at your own risk. There
     may be errors and inaccuracies, that could be damaging to your
     system. Proceed with caution, and although it is highly unlikely
     that accidents will happen because of following advice or
     procedures described in this document, the author(s) do not take
     any responsibility for any damage claimed to be caused by doing
     so.

     All copyrights are held by their by their respective owners,
     unless specifically noted otherwise. Use of a term in this
     document should not be regarded as affecting the validity of any
     trademark or service mark. Naming of particular products or brands
     should not be seen as endorsements.
     ________________________________________________________________

6.2.3. Licensing source code

   If your HOWTO includes bits of source code that you want others to
   use, you may choose to release the source code under GPL.
     ________________________________________________________________

6.3. Acknowledgments

   Your document should have an "Acknowledgments" section, in which you
   mention everyone who has contributed to your document in any
   meaningful way. You should include translators and converters, as
   well as people who have sent you lots of good feedback, perhaps the
   person who taught you the knowledge you are now passing on, and
   anybody else who was instrumental in making the document what it is.
   Most authors put this section at the end of their document.

   When someone else assists in the production of an LDP document, you
   should give them proper attribution, and there are DocBook tags
   designed to do this. This section will show you the tags you should
   use, as well as other ways of giving credit where credit is due.
   Crediting editors is easy - there is already an <editor>tag in
   DocBook. But there are two special cases where you need to credit
   someone, but DocBook doesn't provide a special tag. These are
   translators and converters.

   A converter is someone who performs a source code conversion, for
   instance from HTML to DocBook XML. Source code conversions help the
   LDP achieve long term goals for meta-data, and allow us to distribute
   documentation in many different formats.

   Translators take your original document and translate it into other
   human-readable languages, from English to Japanese for example, or
   from German to English. Each translation allows many more people all
   over the world to make use of your document and of the Linux
   operating system!

   We recommend that you acknowledge converters in the comment for the
   initial version released in the new format, and we recommend that you
   credit translators in each version which they have translated.

   Note Acknowledgments translated in DocBook


   For more information on how to add these credits using DocBook please
   read Section D.6
     ________________________________________________________________

6.4. TLDP Review Process

   Before your document is accepted to the LDP collection it will
   undergo at least three formal reviews. These reviews include a
   technical accuracy review, a language review and a metadata review.
   All new documents must pass these reviews before being accepted into
   the collection.

   When you feel your document is finished, email a copy to the submit
   mailing list (<submit@en.tldp.org>). Please include the title of your
   document and "Final Review Required" in the subject line of your
   email. A team of volunteers will be assigned to your document for
   each of the reviews. It may take up to a week to gather a team who is
   qualified to review your document. Typically the technical review
   happens first, followed by the language review and finally the
   metadata review. Your reviewers will read your document give you
   feedback on whether or not they think your document is ready for
   publication in the LDP collection.

   Your reviewers may have specific points that must be changed. Once
   you have made the changes submit your document back to your review
   team. They will review the document again and advise you on whether
   or not your document is ready for inclusion in the LDP collection.
   You may need to undergo several edits before your document is ready.
   Or it may not require any additional work. Be prepared to make at
   least one round of changes for both the technical and language
   reviews. Ideally this exchange will happen in the LDP's
   [http://cvs.tldp.org] CVS to better track each of the changes that
   are made, and keep track of the most current version of your
   document.

   Once your document has passed both the technical and language
   reviews, you may submit it by following the instructions in Section
   6.5.

   Tip Comparing Two Source Files


   Your reviewer may make changes directly to your source file, or they
   may put their suggestions in a separate email. If they are working
   with the source file directly, and your document is using DocBook
   XML, you may find XMLdiff useful to see the changes that your
   reviewer has made to your source file. It is a python tool that
   figures out the differences between two similar XML files, in the
   same way the diff utility compares text files.

   XMLdiff is available from [http://www.logilab.org/projects/xmldiff]
   http://www.logilab.org/projects/xmldiff.

   For more information on what the reviewers will be looking for,
   please read the
   [http://www.tldp.org/HOWTO/LDP-Reviewer-HOWTO/index.html] Linux
   Documentation Project Reviewer HOWTO.
     ________________________________________________________________

6.5. Submission to LDP for publication

   Note The final step


   This section contains information on what to do after your document
   has received both a technical and language review by the LDP
   volunteers.

   As part of the review process a Review Coordinator will add your
   document to the CVS (including any associated image files) and notify
   the submit mailing list that your document is ready for publication.

   If you do not already have a CVS account, please apply for one when
   your document is submitted for publication. You can apply for an
   account contacting LDP CVS master Sergiusz [mailto:ser@gnu.org]
   mailto:ser@gnu.org
     ________________________________________________________________

Chapter 7. Maintenance

7.1. Maintaining Your Document

   Just because your document has now been published does not mean your
   job is done. Linux documentation needs regular maintenance to make
   sure it is up to date, and to improve it in response to readers'
   ideas and suggestions. TLDP is a living, growing body of knowledge,
   not just a publish-and-forget-it static entity.

   Add relevant mailing lists to your document where people can get
   support. If you have the time, follow these mailing lists yourself to
   stay up-to-date on the latest information.

   Put your email address in the document, and politely request feedback
   from your readers. Once you are officially published, you will begin
   to receive notes with suggestions. Some of these emails will be very
   valuable. Create a folder in your mail program for incoming
   suggestions--when the time is right review the folder and make
   updates to your document. If you are following a related mailing list
   you may also choose to save a copy of important emails from the list
   to this folder.

   Note We are not a free support service, but...


   Some people who email you will request personal assistance. You
   should feel free to decline personal assistance if you cannot spare
   the time. Writing a contribution to the LDP does not commit you to a
   lifetime of free support for anyone on the net; however, do try to
   reply to all requests and suggest a mailing list that will
   (hopefully) be able to provide support to your reader.
     ________________________________________________________________

7.2. Fixing Errors

7.2.1. Fixing Your Own Documents

   If you find an error in your own document, please fix it and
   re-submit the document. You can re-submit your files by emailing them
   to <submit@en.tldp.org>.

   If you have been using the CVS, you can submit your changes to the
   CVS tree and then send a note to the submit mailing list
   (<submit@en.tldp.org>). In your email please give the exact path of
   your document in the CVS tree.

   Remember to update the revision history at the top of the document.
     ________________________________________________________________

7.2.2. Fixing Other Documents in the Collection

   If you find an error in someone else's document please contact the
   author of the document with the correction. If you do not hear back
   from the author within a "reasonable" amount of time, please email
   the LDP coordinator at <discuss@en.tldp.org>
   ([http://tldp.org/mailinfo.html#maillists] subscription required) and
   describe the problem and how you think it needs to be fixed. If the
   license permits, you may be asked to make the change directly to the
   document. If the problems are serious, the document may be removed
   from the collection, or moved to the "Unmaintained" section.

   Note Taking over unmaintained documentation


   For more information on how to deal with unmaintained documents,
   please read: [http://www.tldp.org/authors/unmaint.html] Unmaintained
   (includes a list of steps to take to take over "ownership" of
   unmaintained documents, and a list of unmaintained documents).
     ________________________________________________________________

References

Markup and general information

   Secret Life of Markup, The,
   [http://hotwired.lycos.com/webmonkey/02/42/index4a.html]
   http://hotwired.lycos.com/webmonkey/02/42/index4a.html, Steve
   Champeon.

   Progressive Enhancement and the Future of Web Design: Where We Are
   Now , [http://hotwired.lycos.com/webmonkey/03/21/index3a_page2.html]
   http://hotwired.lycos.com/webmonkey/03/21/index3a_page2.html, Steve
   Champeon.

   SGML, [http://www.w3.org/MarkUp/SGML/]
   http://www.w3.org/MarkUp/SGML/.
     ________________________________________________________________

DocBook References

   DocBook XML 4.1.2 Quick Start Guide,
   [http://www.jimweller.net/jim/dbxmlqs/index.html]
   http://www.jimweller.net/jim/dbxmlqs/index.html, Jim Weller.



   Describes how to install, configure and use the tools and resources
   for DocBook XML 4.1.2. The purpose of this quick start guide is to
   get new docbook authors, editors, and contributors up and running
   fast with the DoocBook tools. These are powerful tool in the hands of
   an author. It assumes a fair knowledge of building and installing
   source packages. There are probably a million and one ways to
   accomplish my ultimate goal of installing and using these tools. This
   one works well for me.

   --Jim Weller

   Installing And Using An XML/SGML DocBook Editing Suite Setting Up A
   Free XML/SGML DocBook Editing Suite For Windows And Unix/Linux/BSD,
   [http://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/bu
   ild/tutorials/docbooksys/docbooksys.html]
   http://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/bui
   ld/tutorials/docbooksys/docbooksys.html , Ashley J.S. Mills, 2002.

   Getting Upto Speed With DocBook,
   [http://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/bu
   ild/tutorials/UniDocBook/UniDocBook.html]
   http://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/bui
   ld/tutorials/UniDocBook/UniDocBook.html, Ashley J.S. Mills, 2002.

   DocBook: The Definitive Guide, [http://www.docbook.org/]
   http://www.docbook.org/, Norman Walsh, Leonard Muellner, 1999,
   1-56592-580-7, O'Reilly & Associates, Inc..

   This book was released by O'Reilly in October 1999, and is a great
   reference to DocBook. I have not found it to be a great practical
   book. You can pick it up at the book vendor of choice, and the entire
   book is also available online (in HTML and SGML formats) at the above
   URL.

   Simplified DocBook: The Definitive Guide,
   [http://www.docbook.org/tdg/simple/en/html/sdocbook.html]
   http://www.docbook.org/tdg/simple/en/html/sdocbook.html, Norman
   Walsh, Leonard Muellner, 1999.

   Simplified DocBook, [http://www.oasis-open.org/docbook/xml/simple/]
   http://www.oasis-open.org/docbook/xml/simple/.

   XML Matters: Getting started with the DocBook XML dialect,
   [http://www-106.ibm.com/developerworks/xml/library/xml-matters3.html]
   http://www-106.ibm.com/developerworks/xml/library/xml-matters3.html.

   FAQ for DocBook markup,
   [http://www.dpawson.co.uk/docbook/markup.html]
   http://www.dpawson.co.uk/docbook/markup.html.

   Single-Source Publishing with DocBook XML, , [
   http://www.lodestar2.com/people/dyork/talks/2002/ols/docbook-tutorial
   /frames/frames.html]
   http://www.lodestar2.com/people/dyork/talks/2002/ols/docbook-tutorial
   /frames/frames.html, Dan York, 2002.

   DocBook Install mini-HOWTO,
   [http://tldp.org/HOWTO/mini/DocBook-Install/]
   http://tldp.org/HOWTO/mini/DocBook-Install/, Robert Easter.

   Exploring SGML DocBook, [http://lwn.net/2000/features/DocBook/]
   http://lwn.net/2000/features/DocBook/, Giorgio Zoppi.
     ________________________________________________________________

LinuxDoc

   Howtos-with-LinuxDoc-mini-HOWTO,
   [http://www.tldp.org/HOWTO/Howtos-with-LinuxDoc.html]
   http://www.tldp.org/HOWTO/Howtos-with-LinuxDoc.html, David Lawyer.

   LinuxDoc-SGML User's Guide, [http://www.nmt.edu/tcc/doc/guide.html]
   http://www.nmt.edu/tcc/doc/guide.html.
     ________________________________________________________________

Converting Other Formats to DocBook

   Converting HTML to Docbook SGML/XML Using html2db,
   [http://www.cise.ufl.edu/~ppadala/tidy/]
   http://www.cise.ufl.edu/~ppadala/tidy/.

   5-Minute Review: Using LyX for Creating DocBook,
   [http://www.teledyn.com/help/XML/lyx2db/t1.html]
   http://www.teledyn.com/help/XML/lyx2db/t1.html.

   Document processing with LyX and SGML,
   [http://www.karakas-online.de/mySGML/]
   http://www.karakas-online.de/mySGML/.
     ________________________________________________________________

LDP templates, tools & links

   LDP Templates, , [http://www.tldp.org/authors/index.html#resources]
   http://www.tldp.org/authors/index.html#resources .

   Contains links to SGML templates and their resulting HTML output to
   help you see what your document will look like. Many of the tags just
   need to be replaced with information unique to your HOWTO. Also
   contains links to tools and other useful information.

   Linux Documentation Project HOWTO Generator, The,
   [http://www.nyx.net/~sgjoen/The_LDP_HOWTO_Generator.html]
   http://www.nyx.net/~sgjoen/The_LDP_HOWTO_Generator.html.

   This is a standalone web page with a number of fields to fill in and
   a few buttons. When ready the compile button starts the compilation
   of all the input fields and wraps it all in proper LinuxDoc SGML,
   ready to process with the LinuxDoc SGML tools.

   The compiled output is outputted to a read-only text area near the
   bottom of the webpage, so the text has to be copied and pasted into a
   file for compilation.

   DocBook is not currently supported.
     ________________________________________________________________

DocBook Transformations

   DocBook XML/SGML Processing Using OpenJade, ,
   [http://tldp.org/HOWTO/DocBook-OpenJade-SGML-XML-HOWTO/]
   http://tldp.org/HOWTO/DocBook-OpenJade-SGML-XML-HOWTO/, Saqib Ali.
     ________________________________________________________________

General Writing Links and Style Guides

   Guide to Grammar and Style,
   [http://newark.rutgers.edu/~jlynch/Writing/]
   http://newark.rutgers.edu/~jlynch/Writing/, Jack Lynch.

   Purdue's Online Writing Lab, [http://owl.english.purdue.edu/]
   http://owl.english.purdue.edu/.

   Chicago Manual of Style, [http://www.chicagomanualofstyle.org/]
   http://www.chicagomanualofstyle.org/.

   Plain Language Resources,
   [http://www.plainlanguagenetwork.org/Resources/]
   http://www.plainlanguagenetwork.org/Resources/.

   Writing User-Friendly Documents,
   [http://www.blm.gov/nhp/NPR/pe_toc.html]
   http://www.blm.gov/nhp/NPR/pe_toc.html.

   This is quite useful. It includes before and after writing samples.

   PlainTrain Writing Tutorial,
   [http://www.web.net/~plain/PlainTrain/IntroducingPlainLanguage.html]
   http://www.web.net/~plain/PlainTrain/IntroducingPlainLanguage.html.

   Writing for the Web, [http://www.useit.com/papers/webwriting/]
   http://www.useit.com/papers/webwriting/.

   Information Pollution, [http://useit.com/alertbox/20030811.html]
   http://useit.com/alertbox/20030811.html.

   Be Succinct! (Writing for the Web),
   [http://useit.com/alertbox/9703b.html]
   http://useit.com/alertbox/9703b.html.

   Politics and the English Language,
   [http://www.k-1.com/Orwell/index.cgi/work/essays/language.html]
   http://www.k-1.com/Orwell/index.cgi/work/essays/language.html, George
   Orwell.

   A classic text on writing.

   Elements of Style, The, [http://www.bartleby.com/141/]
   http://www.bartleby.com/141/, Strunk and White.

   A classic text on writing.

   A Short Handbook and Style Sheet,
   [http://newark.rutgers.edu/~jlynch/Writing/m.html#mechanics]
   http://newark.rutgers.edu/~jlynch/Writing/m.html#mechanics, Thomas
   Pinney.

   Technical Writing Links, [http://www.techcomplus.com/tips.htm]
   http://www.techcomplus.com/tips.htm.

   Technical Writing Tutorial,
   [http://psdam.mit.edu/rise/tutorials/writing/technical-writing.html]
   http://psdam.mit.edu/rise/tutorials/writing/technical-writing.html.

   Strategies to succeed in technical writing,
   [http://www.school-for-champions.com/techwriting.htm]
   http://www.school-for-champions.com/techwriting.htm.

   User Guides Online Tutorial,
   [http://www.klariti.com/technical-writing/User-Guides-Tutorial.shtml]
   http://www.klariti.com/technical-writing/User-Guides-Tutorial.shtml.

   DMOZ Technical Writing Links,
   [http://dmoz.org/Arts/Writers_Resources/Non-Fiction/Technical_Writing
   /]
   http://dmoz.org/Arts/Writers_Resources/Non-Fiction/Technical_Writing/
   .

   techwr-L, [http://www.raycomm.com/techwhirl/magazine/]
   http://www.raycomm.com/techwhirl/magazine/.

   Technical Writing Links,
   [http://academic.middlesex.cc.ma.us/PeterHarbeson/links.html]
   http://academic.middlesex.cc.ma.us/PeterHarbeson/links.html.

   An omnibus of links--scrounge for goodies.
     ________________________________________________________________

Related TLDP Documents

   Linux Documentation Project (LDP) FAQ,
   [http://tldp.org/FAQ/LDP-FAQ/index.html]
   http://tldp.org/FAQ/LDP-FAQ/index.html, Rahul Sundaram.

   LDP HOWTO-INDEX, [http://tldp.org/HOWTO/HOWTO-INDEX/]
   http://tldp.org/HOWTO/HOWTO-INDEX/, Guylhem Aznar, Joshua Drake, Greg
   Ferguson.
     ________________________________________________________________

Software: CVS

   CVS: Project Management, [http://doc.cs.byu.edu/programming/cvs/]
   http://doc.cs.byu.edu/programming/cvs/, Byron Clark.

   CVS,
   [http://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/bu
   ild/tutorials/cvstute/cvstute.html]
   http://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/bui
   ld/tutorials/cvstute/cvstute.html, Ashley J.S. Mills, Alan P. Sexton.

   CVS--Concurrent Versions System,
   [http://www.loria.fr/~molli/cvs/doc/cvs_toc.html]
   http://www.loria.fr/~molli/cvs/doc/cvs_toc.html, Pascal Molli.

   Learning About CVS , [http://cvshome.org/docs/]
   http://cvshome.org/docs/.
     ________________________________________________________________

Software: Emacs

   Information about PSGML ,
   [http://www.lysator.liu.se/~lenst/about_psgml/]
   http://www.lysator.liu.se/~lenst/about_psgml/.

   Emacs: The Free Software IDE,
   [http://www.linuxjournal.com/article.php?sid=576]
   http://www.linuxjournal.com/article.php?sid=576.

   Emacs/PSGML Quick Reference,
   [http://www.snee.com/bob/sgmlfree/psgmqref.html]
   http://www.snee.com/bob/sgmlfree/psgmqref.html, Bob Ducharme.

   NT Emacs Installation, [http://www.charlescurley.com/emacs.html]
   http://www.charlescurley.com/emacs.html, Charles Curley.

   Cygwin Packages for DocBook Authoring,
   [http://www.docbook.org/wiki/moin.cgi/CygwinPackages/]
   http://www.docbook.org/wiki/moin.cgi/CygwinPackages/.

   SGML for Windows NT: Setting up a free SGML/XML editing and
   publishing system on Windows/Cygwin ,
   [http://ourworld.compuserve.com/homepages/hoenicka_markus/cygbook1.ht
   ml]
   http://ourworld.compuserve.com/homepages/hoenicka_markus/cygbook1.htm
   l, Markus Hoenicka, 2000.

   Vim, [http://www.newriders.com/books/opl/ebooks/0735710015.html]
   http://www.newriders.com/books/opl/ebooks/0735710015.html, Steve
   Oualline.
     ________________________________________________________________

XML Authoring Tools

   Saqib's list of XML Authoring Tools,
   [http://www.xml-dev.com/xml/editors.html]
   http://www.xml-dev.com/xml/editors.html.
     ________________________________________________________________

Documentation Licenses

   Licensing HOWTO, [http://www.catb.org/~esr/Licensing-HOWTO.html]
   http://www.catb.org/~esr/Licensing-HOWTO.html, Eric Raymond,
   Catherine Raymond.



   This document explains how U.S. copyright and licensing law applies
   to open-source software projects. It compares the strengths and
   weaknesses of the existing open-source licenses, and gives guidance
   on how to choose a license for your project. It also explains the
