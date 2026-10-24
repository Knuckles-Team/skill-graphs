```

LDP Author Guide

Jorge Godoy

   [http://www.conectiva.com] Conectiva S.A.
   Publishing Department

   <godoy@metalab.unc.edu>

Emma Jane Hogbin

   <emmajane@xtrinsic.com>

Mark F. Komarinski

   <mkomarinski@wayga.org>

David C. Merrill

   david -AT- lupercalia.net

   2005-03-04
   Revision History
   Revision 4.84.74.64.54.44.34.24.1
   2006-04-202005-03-042005-01-232004-07-142004-04-192004-04-042004-04-0
   22004-01-27 Revised by: MGejhejhejhejhejhejhejh
   Added notes about preferred submission formats, corrected links,
   packaged templates.Typo fixed in sample DocBook markup. Added new
   web-based authoring tool and information on LaTeX to DocBook
   conversions.Typos fixed in xmlto notes and book template. Copied
   information about DocBook-capable word processing tools into the
   "Converting Documents to DocBook XML" Appendix; added new XML
   editors; and information about tools to convert other formats to
   DocBook XML.Updated information regarding CVS accounts and connecting
   to the CVS server.Added editor credit requirements to the Using
   DocBook section. Updated the submission procedure. New documents can
   now only be added by one of the Review Coordinators after the
   successful completion of each of the required reviews.Removed the
   section Contributing to The LDP (replaced by Summary of The LDP
   Process).Added references for LyX to DocBook conversions in the
   bibliography.Updated the license requirements and added them to the
   table of contents (moved them out of the sub-section).

   This guide describes the process of submitting and publishing a
   document with The Linux Documentation Project (TLDP). It includes
   information about the tools, toolchains and formats used by TLDP. The
   document's primary audience is new TLDP authors, but it also contains
   information for seasoned documentation authors.
     ________________________________________________________________

   Table of Contents
   1. About this Guide

        1.1. About this Guide
        1.2. About The LDP
        1.3. Feedback
        1.4. Copyrights and Trademarks
        1.5. Acknowledgments and Thanks
        1.6. Document Conventions

   2. Authoring TLDP Documents: An Introduction

        2.1. Summary of The LDP Process
        2.2. Mailing Lists

   3. Writing Your Proposal

        3.1. Choosing a Subject
        3.2. Scope of Your Document
        3.3. Unmaintained and Out-of-date Documents
        3.4. Developing an Outline
        3.5. Research

   4. Write

        4.1. Writing the Text
        4.2. Edit and Proofread the Text
        4.3. Tools for Writing, Editing and Maintaining your Document

   5. Markup

        5.1. Markup: A General Overview
        5.2. DocBook: What it is and why we use it
        5.3. XML and SGML: Why we use XML
        5.4. Markup Languages Accepted by TLDP

   6. Distributing Your Documentation

        6.1. Before Distributing Your Documentation
        6.2. Licensing and Copyright
        6.3. Acknowledgments
        6.4. TLDP Review Process
        6.5. Submission to LDP for publication

   7. Maintenance

        7.1. Maintaining Your Document
        7.2. Fixing Errors

   References
   A. Templates

        A.1. Document Templates
        A.2. Style Sheets
        A.3. GNU Free Documentation License

   B. System Setup: Editors, Validation and Transformations

        B.1. Tools for your operating system
        B.2. Editing tools
        B.3. Validation
        B.4. Transformations
        B.5. DocBook DTD
        B.6. Formatting Documents

   C. Concurrent Version System (CVS)

        C.1. Getting a CVS account
        C.2. Using CVS
        C.3. CVS Resources

   D. DocBook: Sample Markup

        D.1. General Tips and Tricks
        D.2. <section> and <sectN>: what's the difference?
        D.3. Command Prompts
        D.4. Encoding Indexes
        D.5. Inserting Pictures
        D.6. Markup for Metadata
        D.7. Bibliographies
        D.8. Entities (shortcuts, text macros and reusable text)
        D.9. Customizing your HTML files

   E. Converting Documents to DocBook XML

        E.1. Text to DocBook
        E.2. OpenOffice.org to DocBook
        E.3. Microsoft Word to DocBook
        E.4. LaTeX to DocBook
        E.5. LyX to DocBook
        E.6. DocBook to DocBook Transformations

   Glossary
   F. GNU Free Documentation License

        F.1. 0. PREAMBLE
        F.2. 1. APPLICABILITY AND DEFINITIONS
        F.3. 2. VERBATIM COPYING
        F.4. 3. COPYING IN QUANTITY
        F.5. 4. MODIFICATIONS
        F.6. 5. COMBINING DOCUMENTS
        F.7. 6. COLLECTIONS OF DOCUMENTS
        F.8. 7. AGGREGATION WITH INDEPENDENT WORKS
        F.9. 8. TRANSLATION
        F.10. 9. TERMINATION
        F.11. 10. FUTURE REVISIONS OF THIS LICENSE
        F.12. Addendum

   List of Tables
   D-1. Useful markup

   List of Figures
   B-1. epcEdit screen shot
   B-2. nedit screen shot
   B-3. Adding shell commands to nedit
   B-4. nsgmls output on success

   List of Examples
   B-1. Setting the SGML_CATALOG_FILES and XML_CATALOG_FILES
          Environmental Variables

   B-2. Example of an SGML catalog
   B-3. Sample XML Catalog file
   B-4. Debugging example using xmllint
   B-5. "Installing" DSSSL style sheets
   B-6. Example creating HTML output
   B-7. "Installing" DocBook Document Type Definitions
   B-8. Style sheet to insert summaries in articles
   B-9. Configuring an external entity to include the index
   D-1. Command Prompt with programlisting
   D-2. Command Prompt with screen
   D-3. Code for the generation of an index
   D-4. Use of the attribute zone
   D-5. Usage of values startofrange and endofrange on the
          attributeclass

   D-6. Inserting a picture
   D-7. Using <imageobject>
   D-8. Other Credit
   D-9. Editor
   D-10. Sample Meta Data
   D-11. A Bibliography
   D-12. Adding Entities
   D-13. Use of parameter entities
     ________________________________________________________________

Chapter 1. About this Guide

1.1. About this Guide

   This document was started on Aug 26, 1999 by Mark F. Komarinski after
   two day's worth of frustration getting tools to work. If even one LDP
   author is helped by this, then I did my job.

   Version 4 of this document was released in early 2004 by Emma Jane
   Hogbin. A complete overhaul of the document was done to separate the
   authoring HOWTOs from the technical HOWTOs. The review took
   approximately eight months.

   The newest version of this document can be found at the LDP homepage
   [http://www.tldp.org/] http://www.tldp.org. The original DocBook,
   HTML, and other formats can be found there.

   There are many ways to contribute to the Linux movement that do not
   require the ability to produce software. One such way is to write
   documentation. The availability of easy-to-understand, technically
   accurate documentation can make a world of difference to someone who
   is struggling with Linux software. This Guide is designed to help you
   research and write a HOWTO which can be submitted to the LDP. The
   appendices also include sample templates, markup tips and information
   on how to transform your document from DocBook to another format
   (such as HTML) for easier proofreading.
     ________________________________________________________________

1.2. About The LDP

   The Linux Documentation Project (LDP) was started to provide new
   users a way of quickly getting information about a particular
   subject. It not only contains a series of books on administration,
   networking, and programming, but also has a large number of smaller
   works on individual subjects, written by those who have used it. If
   you want to find out about printing, you get the Printing HOWTO. If
   you want to do find out if your Ethernet card works with Linux, grab
   the Ethernet HOWTO, and so on.

   The LDP provides documents to the world in a variety of convenient
   formats and also accepts submissions in a number of formats. The
   current standard for storing the source documentation is a format
   known as DocBook, see Section 5.2.


   The Linux Documentation Project (LDP) is working on developing free,
   high-quality documentation for the GNU/Linux operating system. The
   overall goal of the LDP is to collaborate in all of the issues of
   Linux documentation. This includes the creation of "HOWTOs" and
   "Guides". We hope to establish a system of documentation for Linux
   that will be easy to use and search. This includes the integration of
   the manual pages, info docs, HOWTOs, and other documents.

   --LDP Manifesto located at [http://www.tldp.org/manifesto.html]
   http://www.tldp.org/manifesto.html

   The human readable version goes more like this: The LDP consists of a
   large group of volunteers who are working on documentation about
   Linux and the programs which run on the Linux kernel. These documents
   exist primarily as shorter HOWTOs and longer Guides. Both are
   available from [http://www.tldp.org/] http://www.tldp.org/. This
   Guide focuses primarily on how to write your own HOWTOs for
   submission to the LDP.
     ________________________________________________________________

1.3. Feedback

   Send feedback to <discuss@en.tldp.org>. Please reference the title of
   this document in your email. Please note: you must
   [http://tldp.org/mailinfo.html#maillists] be subscribed in order to
   send email to the list.
     ________________________________________________________________

1.4. Copyrights and Trademarks

   Copyright 1999-2002 Mark F. Komarinski, David C. Merrill, Jorge Godoy

   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.1 or
   any later version published by the Free Software Foundation; with no
   Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
   Texts. A copy of the license is included in the appendix entitled
   "GNU Free Documentation License."
     ________________________________________________________________

1.5. Acknowledgments and Thanks

1.5.1. Version 1 - Version 3

   Thanks to everyone that gave comments as I was writing this. This
   includes David Lawyer, Deb Richardson, Daniel Barlow, Greg Ferguson,
   Mark Craig and other members of the <discuss@en.tldp.org> list. Some
   sections I got from the [http://www.tldp.org/HOWTO/] HOWTO Index and
   the sgmltools documentation. The sections on network access to CVS
   was partially written by Sergiusz Pawlowicz (<ser@metalab.unc.edu>).
   Sections on DocBook were written by Jorge Godoy
   (<godoy@conectiva.com>). A great deal of thanks to both of them for
   their help.
     ________________________________________________________________

1.5.2. Version 4

   Thanks to Tabatha Marshall and Machtelt Garrels (Tille) for making
   sure I actually finished the document. Thanks to my reviewers:
   Charles Curley, Martin Brown and Tille; and to Saqib Ali for his
   on-line transformation and validation tools. I have also incorporated
   a number of useful emails from the LDP mailing lists. The original
   authors are credited within the document. Special personal thank yous
   are extended to Steve Champeon for getting me interested in markup
   languages and for being a wonderful mentor; and to my partner, Graig
   Kent, for being outrageously supportive. [EJH]
     ________________________________________________________________

1.6. Document Conventions

   This document uses the following conventions[1]:

   Descriptions Appearance
   Information requiring special attention

   Warning

   This is a warning.
   Caution

   Caution

   This cautions the reader.
   Hint

   Tip

   This is a hint.
   Notes

   Note

   This is a note.
   File Names file.extension
   Directory Names directory
   Commands to be typed command
   Applications Names application
   Prompt of users command under bash shell bash$
   Prompt of root users command under bash shell bash#
   Prompt of user command under tcsh shell tcsh$
   Environment Variables VARIABLE
   Emphasized word word
   Quoted text "quote"
   Code Example
   <para>Beginning and end of paragraph</para>
     ________________________________________________________________

Chapter 2. Authoring TLDP Documents: An Introduction

2.1. Summary of The LDP Process

   The following section outlines the process of creating and/or
   maintaining a document for the Linux Documentation Project. This
   section includes all steps--some of which may not be relevant to your
   specific document.

    1. Join the discuss mailing list. Authors who are interested in
       taking over the maintenance of someone else's document should
       also join this list. This is to make sure the LDP knows who is
       working on what documentation.
       If you have not yet written your documentation, please review our
       documents ([http://tldp.org/HOWTO/HOWTO-INDEX/howtos.html]
       current, [http://tldp.org/authors/unmaint.html] unmaintained and
       [] in progress) and submit a proposal to the list. Your proposal
       should include reasons why your document will be different than
       those already in the collection; or identify a subject that is
       currently missing from our documentation. For more information
       about writing proposals, please read Chapter 3.
       For more information about the mailing lists, please read Section
       2.2 or visit [http://lists.tldp.org] lists.tldp.org to subscribe.
       If your document has already been written, please submit a copy
       to the discuss list (or include the URL of where it can be
       found).
    2. Write your document. If your document has not yet been written,
       please be sure to email the discuss list before you start
       writing. You may choose whatever format you feel most comfortable
       in to write your document. If it is not one of the formats
       accepted by the LDP a volunteer will convert it for you. For more
       information on writing technical documentation, please read
       Chapter 4.
    3. If you are adding your own markup, you may also want to join the
       docbook mailing list. For more information about the LDP DocBook
       list please read Section 2.2. If you would like to start with a
       template, you may find the templates in Appendix A useful. There
       is also a general introduction to markup in Chapter 5 and a
       section full of examples at Appendix D.
    4. Submit your document for technical, language and metadata
       reviews. Do this by emailing your document to
       <submit@en.tldp.org>. In the subject line be sure give the title
       of the document. In the body of the email say that you are ready
       for the review process. Outline any additional reviews your
       document may have already received. You should be assigned a
       reviewer within the week. The reviews may take an additional week
       each. For more information about this process, please read
       Chapter 6.
       If your document is not already in DocBook or LinuxDoc format, a
       reviewer will convert it for you.
    5. Once your document has been through each of the reviews a Review
       Coordinator will add it to the CVS, update the version number to
       1.0 and have the document published on the public Web site. For
       more information about your final submission to the LDP, please
       read Section 6.5.

   Tip If you don't submit your document in DocBook format


   The volunteer adding markup to your document may choose any accepted
   markup language. The Author Guide, however, will refer only to
   DocBook. If you are submitting plain text or some other format,
   please let the LDP know if you prefer to maintain your document in
   either LinuxDoc or DocBook, which are the accepted formats for
   end-results.
     ________________________________________________________________

2.2. Mailing Lists

   You can subscribe to the following mailing lists:

     * First is <discuss@en.tldp.org>, which is the main discussion
       group of the LDP.
     * Another is the <docbook@en.tldp.org> list, which is for questions
       about DocBook use including markup and transformations. If you
       run into trouble with a particular markup tag, you can send your
       question here for answers.

   You can subscribe to either list by sending a request message to
   either <discuss-subscribe@en.tldp.org> or
   <docbook-subscribe@en.tldp.org>. The subject of your message should
   read "subscribe" (no quotes). To remove yourself from the list, send
   an E-mail with the subject of "unsubscribe" to
   <discuss-unsubscribe@en.tldp.org> or
   <docbook-unsubscribe@en.tldp.org>.

   If you are interested in DocBook beyond the simple markup of your LDP
   document, you may want to consider joining one of the
   [http://www.oasis-open.org/] OASIS DocBook mailing lists. Please see
   [http://docbook.org/mailinglist/index.html]
   http://docbook.org/mailinglist/index.html for more information.
     ________________________________________________________________

Chapter 3. Writing Your Proposal

3.1. Choosing a Subject

   It is likely that if you are reading the Author Guide, you already
   have a subject in mind. The idea may have come from your own
   frustrations in trying to get something to work; or maybe you are
   already writing or have written documentation for other purposes and
   you want to submit it to the LDP. For example, if you posted a
   question to a mailing list and it took many posts to resolve the
   problem -- that might be an incentive to write documentation.

   Regardless of how you picked your subject, it is important that the
   LDP community understand why your documentation should be included in
   its collection. If someone has requested documentation, or you worked
   with a mailing list to resolve a problem you should include the
   details in your proposal to the LDP discuss mailing list. It may help
   others to understand the need for your specific document.
     ________________________________________________________________

3.2. Scope of Your Document

   Now that you've got a subject, you will need to decide the scope of
   the document. The scope or subject area should be:

    1. Clearly defined. Define the boundaries of your subject area
       before you begin. Do not repeat information that is in another
       HOWTO and do not leave gaps of information between your HOWTO and
       someone else's HOWTO.
    2. Not too broad, and not too narrow. If you try to cover too much
       information you may sacrifice depth. It is better to cover a
       small subject area in detail than to cover a large subject area
       poorly. Linux tools are known for doing exactly one thing and
       doing that one thing well. Similarly, your HOWTO should cover one
       subject and cover it well.
       If the scope of your proposed document is very narrow, it might
       be better to include your information as part of another HOWTO.
       This makes it easier for readers to find the HOWTO they need.
       Search the LDP repository for topics which relate to your
       document. If you find a document which is a good match, email the
       author and ask them if they would like to include your
       contribution.
    3. Undocumented. Before documenting a particular subject, always do
       a web search (and specifically a search within the LDP documents)
       to see if your topic is already covered in another document. If
       it is, refer to the other document instead of duplicating the
       information within your own document. You may wish to include a
       brief summary of information that can be found in other
       documents.
       If the HOWTO already in place is insufficient or needs updating,
       contact the author and offer to help. See also Section 3.3 for
       taking over old or unmaintained documents.
       Most authors appreciate any help offered. Additionally, sending
       comments and remarks to the author is usually regarded both as a
       reassurance and a reward: to the author, feedback is the ultimate
       proof that writing the documentation was not a pointless effort.
    4. Pre-approved by the LDP. Before you proceed with your HOWTO, post
       to the discuss list and get some feedback from other LDP
       volunteers. Checking with the list before you begin can save you
       headaches later.

   Note Stay in touch!


   Joining the discuss list and following it regularly, even if you
   never post, is a good way to stay current on the activities, needs
   and policies of the LDP.
     ________________________________________________________________

3.2.1. Documentation Templates

   After you've decided the scope of your document you should start to
   consider the type of document that you will write. There are a number
   of different LDP documentation templates: Guides, HOWTOs, man pages
   and FAQs. Rahul Sundaram describes their scope in the Linux
   Documentation Project (LDP) FAQ. Here is a brief overview of what
   they are with pointers on how you can get started writing your own:

     * Guides. A guide covers a broad subject and is quite long. The
       Author Guide (this document) is a guide. Other guides include:
       Introduction to Linux: A hands on guide, The Linux Kernel Module
       Programming Guide, etc. A full list of guides is available from:
       Linux Project Documentation Guides. Guides use the "book"
       templates located in Appendix A.
     * HOWTOs. A HOWTO is typically a set of instructions that outlines,
       step-by-step, how a specific task is accomplished. Examples of
       HOWTOs are: [http://tldp.org/HOWTO/CDROM-HOWTO/index.html]
       CDROM-HOWTO [http://tldp.org/HOWTO/Module-HOWTO/index.html]
       Module-HOWTO. A full list of HOWTOs is available from: Single
       List of HOWTOs (warning: it's a BIG page). HOWTOs typically use
       the "article" template and are output to multiple HTML pages by
       default. Templates are available in Appendix A.
     * man pages. man (Manual) pages are the standard form of help
       available for many linux applications and utilities. They can be
       viewed by typing man applicationname at a prompt. A full list of
       man pages is available from: [http://tldp.org/docs.html#man]
       Linux Man Pages. Since man pages are bundled with software there
       is no LDP template at this time.
     * FAQs. FAQs (Frequently Asked Questions) are a list of questions
       and answers to help prevent new users from asking the same
       questions over and over again. A full list of FAQs is available
       from: Linux Documentation Project FAQs. FAQs typically use the
       "article" template with some specific DocBook elements to form
       the Question/Answer structure. You can find a template for
       writing a FAQ in Appendix A.

   Note mini-HOWTOs and HOWTOs


   The LDP no longer distinguishes between HOWTOs and mini-HOWTOs. All
   previously written mini-HOWTOs have been included in longer HOWTOs.
   All new documents must be at least HOWTO in length. This means the
   documents should cover a bigger subject area rather than a small one.
   If your document is very small you may wish to submit it for
   inclusion in another, larger HOWTO that already exists. If you're not
   sure what size your document is, email the discuss list and ask for
   feedback.
     ________________________________________________________________

3.3. Unmaintained and Out-of-date Documents

   If you wish to become the "owner" for an unmaintained document there
   are several steps you must go through.

     * Contact the author. Make sure the author no longer wishes to
       maintain the document in question. Note that the E-mail address
       shown may no longer be valid. In that case, try a
       [http://google.com] search for the author. If the original author
       of a document cannot be found after a "good-faith" effort, let us
       know (<discuss@en.tldp.org>--subscription required).
     * Determine if a more up-to-date copy of the document exists,
       outside of what is available on the LDP. If so, try to secure a
       copy for yourself to work on.
     * Inform the LDP which document you would like to maintain, so that
       we can track who is working on what and prevent duplication of
       effort. We also suggest that you join the LDP general discussion
       list (<discuss@en.tldp.org>). This step is also required for new
       documents.
     * Submit the document to the LDP with any intended modifications.
       Make sure to continue to reference the original author somewhere
       within the document (Credits, Revision History, etc.). Once the
       document is re-submitted, we will remove the entry from the list
       of unmaintained documents.

   Note Feedback wanted


   Some of unmaintained documents may be outdated, or the content may be
   covered in another (actively maintained) HOWTO. If that is the
   situation, contact us (preferably on the discuss mailing list) and
   let us know.
     ________________________________________________________________

3.4. Developing an Outline

   Before you actually begin writing, prepare an outline. An outline
   will help you to get a clear picture of the subject matter and allow
   you to concentrate on one small part of the HOWTO at a time.
