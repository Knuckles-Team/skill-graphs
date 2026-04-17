
   Unless your HOWTO is exceptionally small, your outline will probably
   be multilevel. When developing a multilevel outline, the top level
   should contain general subject areas, and sub-headings should be more
   detailed and specific. Look at each level of your outline
   independently, and make sure it covers all key areas of the subject
   matter. Sub-headings should cover all key areas of the heading under
   which they fall.

   Each item in your outline should follow the item before it, and lead
   into the item that comes next. For example, a HOWTO about a
   particular program shouldn't have a section on configuration before
   one on installation.

   You may choose to use the following outline for a HOWTO about using a
   specific program:

     * development history
     * where to download the software from
     * how to install the software
     * how to configure the software
     * how to use the software

   You may find it helpful to try a little "card sorting" at this stage
   of the writing process. Write all of your mini subject areas onto
   pieces of paper. Now sort these pieces of paper into main headings
   and their sub-sections. It may help to shuffle the slips of paper
   before you start. This will help to give you a fresh set of eyes
   while working.

   When you are comfortable with your outline, look it over once more,
   with a critical eye. Have you covered every relevant topic in
   sufficient detail? Have you not wandered beyond the scope of the
   document? It is a good idea to show your outline to others (including
   The LDP discuss list) to get some feedback. Remember: it is much
   easier to reorganize your document at the outline stage than doing
   this after writing it.

   Tip Writing a HOWTO made easy


   For help writing your HOWTO outline, and getting a head start on the
   markup of your document, check out The LDP HOWTO Generator. Note that
   this is for generating HOWTOs. Templates for FAQs and Guides are
   available in Appendix A.

   Note You're not alone


   You might have noticed a theme developing here. Just like Free
   software, Free documentation is best when you "release early, release
   often." The discuss list includes many experienced LDP authors, and
   you would be wise to seek their advice when making decisions about
   your contribution.
     ________________________________________________________________

3.5. Research

   While you are working on your outline you will most likely research
   your topic--especially to confirm the document you are about to write
   does not yet exist! Here are a few pointers that will keep you from
   pulling out your hair later:

     * Compile your resources as you research. It is almost guaranteed
       you will not remember where to find a critical piece of
       information when you need it most. It will help to bookmark
       important (and even not so important) pages as you go. Make sure
       the bookmark's title reflects why the page is important to you.
       If there are multiple key ideas in one page, you may want to
       bookmark the same page with different titles.
     * Assume your most important resource will disappear. The dreaded
       "Error 404: Page not found". Even if you have bookmarked a page
       it may not be there when you return to it. If a page contains a
       really critical piece of information: make a copy. You may do
       this by creating a text file with the title of the document, the
       author's name, the page's URL and the text of the page into a
       text file on your computer. You might also choose to "print" the
       file to a PDF (save as or convert to PDF format will capture the
       original URL on the page if you're using a smart browser).
     * Start your "Resources" page now. As you find pages of interest
       add them to a Resources document. You may do this by exporting
       your bookmarks or by keeping a separate text file with the
       Resources sorted by sub-category. A little effort now will save
       you a lot of time later.
       There is more information about the DocBook markup of
       bibliographies in Section D.7.
     * Write down subject areas as you go. If you are card sorting you
       may find it particularly useful to write topic cards as you find
       pages that cover that specific topic. At the top of the card
       write the subject area. In the main area of the card write a few
       notes about what you might cover under this topic--include the
       titles of pages that contain important information. If a
       sub-topic gets too big you may want to divide it into multiple
       cards.
     * Separate generic information from version-specific information. A
       new version of the software that you describe might be released
       the day after you release your document. Other things, like where
       to download the software, won't change. Alternatively, you may
       choose to document old problems with specific software as a way
       of encouraging readers to upgrade to the latest version
       available: "Version X of the software is known for a specific
       bug. The bug was fixed as of Version Y."
     * Save all related emails. People will often have interesting
       insight into the problem that you are writing about. Any
       questions that are asked about your topic should be addressed in
       the final document. If you are writing about software make sure
       to ask people what system they are using. Add information in your
       document about which system configurations your instructions have
       been tested on. (Having lots of friends with moderately different
       configurations can be very beneficial!) All of these personal
       experiences can add greatly to your final documentation.
     ________________________________________________________________

Chapter 4. Write

4.1. Writing the Text

   By now you should have organized your document; you collected bits of
   raw information and inserted them into the outline. Your next
   challenge is to massage all of the raw data you've collected into a
   readable, entertaining and understandable whole. If you are working
   from an existing document make sure any new pieces of information are
   in the best possible places.

   It has taken quite a bit of work to get to the point where you can
   actually start writing, hasn't it? Well, the hard work begins to pay
   off for you now. At this stage, you can begin to really use your
   imagination and creativity to communicate this heap of information.
   Don't be too clever though! Your readers are already struggling with
   new concepts--do not make them struggle to understand your language
   as well.

   There are a number of classic guides to writing--many of which are
   available on-line. Their language will seem old, but the messages are
   still valuable to authors today. These are listed in . Also listed in
   the resources section are a variety of sites that have information
   specific to technical writing.

   The Author Guide wouldn't be complete without mentioning the Plain
   Language movement. Although directed at simplifying government
   documents, Writing user-friendly documents is quite useful. It
   includes before and after writing samples. There's also a PlainTrain
   writing tutorial.

   And any document that discusses writing for the web wouldn't be
   complete without a nod toward [http://www.useit.com] useit.com. The
   following articles may be of specific interest:

     * [http://www.useit.com/papers/webwriting/] Writing for the Web
     * [http://useit.com/alertbox/20030811.html] Information pollution
     * [http://useit.com/alertbox/9703b.html] Be Succinct! (Writing for
       the Web)

   There are many, many resources for writing web documents--a quick web
   search for "web writing" will find lots of resources. Don't get too
   distracted, though: the ultimate goal is to write, not to read about
   writing!
     ________________________________________________________________

4.1.1. Writing Style and Style Guides

   There are a number of industry style guides which define how language
   should be used in documents. A common example for American English is
   the Chicago Manual of Style. It defines things like: whether a period
   (.) should be inside or outside of "quotes"; and the format for
   citing another document. A style guide helps to keep documents
   consistent--most corporations will follow a style guide to format
   media releases and other promotional material. Style guides mays also
   define how words should be spelled (is it color or colour?).

   The LDP does not require a specific style guide; however, you should
   use a consistent style throughout your document. Your document should
   be spell checked for a single language (e.g. American English vs.
   British English). The [http://tldp.org/HOWTO/LDP-Reviewer-HOWTO/]
   Reviewer's HOWTO currently lists a number of conventions for LDP
   documents and it is as close as it gets to an official LDP Style
   Guide.

   Tip A personal glossary


   It helps to make a list of terms that you were new to you when you
   first started researching and writing your document. You can refer to
   this list while writing the text. You may also want to include it as
   a glossary in your final document.

   You can save yourself a lot of time in the editing phase if you
   decide how you will write your document ahead of time. If you are
   taking over someone else's document you may need to either: modify
   your own style to fit the current document; or edit the document so
   that it melds with the style you would like to use from now on.

   From a writing style perspective, use of the first-person in a HOWTO
   adds to its charm--an attribute most other documentation sorely
   lacks. Don't be afraid to speak for yourself--use the word "I" to
   describe your personal experiences and opinions.
     ________________________________________________________________

4.1.2. On-line Writing Resources

   In the section, you will find a list of resources that cover the
   subject better than this guide could hope to. Consult them, and
   follow their advice.
     ________________________________________________________________

4.2. Edit and Proofread the Text

   Once you've written the text of your HOWTO, it is time to polish and
   refine it. Good editing can make the difference between a good HOWTO
   and a great one.

   One of the goals of editing is to remove [extraneous] material that
   has crept its way into your document. You should go through your
   HOWTO carefully, and ruthlessly delete anything that does not
   contribute to the reader's understanding of the subject matter. It is
   natural for writers to go off on tangents while in the process of
   writing. Now is the time to correct that. It often helps to leave a
   bit of time between when you write a document and when you edit it.

   Make sure that the content of every section matches the title
   precisely. It's possible that your original subject heading is no
   longer relevant. If you've strayed from your original heading it
   could mean one of the following: the original title was poorly
   worded, the new material should actually go in a different section,
   or the new material is not really necessary for your document. If you
   need to change a title, check to see if the original subject heading
   is still important. If it is, make sure that topic is covered
   somewhere else in the document.

   When editing and proofing your work, check for obvious mistakes, such
   as spelling errors and typos. You should also check for deeper, but
   less obvious errors as well, such as "holes" in the information. If
   you are creating a set of instructions it may help to test them on a
   new machine. Sometimes there are packages that need to be installed
   which you've forgotten to mention in your documentation, for
   instance.

   When you are completely satisfied with the quality and accuracy of
   your work, forward it to someone else for third-party proofing. You
   will be too close to the work to see fundamental flaws. Have others
   test the instructions as well. Make sure they follow exactly what you
   have written. Ask anyone who tests your documentation to make
   specific notes in any places where they didn't follow your
   instructions (and the reason why they didn't follow them). For
   example: "I skipped step 2 because I already have the required
   packages installed."

   In a sense, editing is like code review in software development.
   Having a programmer review their own code doesn't make much sense,
   and neither does having a writer edit their own document. Recruit a
   friend, or write the discuss list to find a volunteer to proofread
   before submitting your document. You may also want to submit your
   document to a mailing list that is relevant to your document's topic.
   List members should be able to help check the facts, clarity of your
   instructions and language of the document.

   Note Native speaker?


   If you are writing in a language in which you are not fluent, find an
   editor who is. Technical documentation, more than any other type of
   writing, must use extremely precise grammar and vocabulary. Misuse of
   language makes your document less valuable.
     ________________________________________________________________

4.3. Tools for Writing, Editing and Maintaining your Document

   Caution Reminder


   You do not need to submit your initial document to the LDP in
   anything more than plain text! Other open submission formats are
   accepted as well, for instance OpenOffice documents, RTF files or
   HTML. The LDP volunteers will convert your document to DocBook for
   you. Once it has been converted you will need to maintain your
   document in DocBook format, but that should be obvious.
     ________________________________________________________________

4.3.1. Editing Tools

   You may use any word processing or text editing tool to write your
   initial document. When you get to the markup stage you may want to
   use a text editor which recognizes DocBook files. At a minimum a
   program which adds syntax highlighting to your markup will make life
   a lot easier. For a description of editors which can handle DocBook
   files please skip to Section B.2.
     ________________________________________________________________

4.3.2. Concurrent Versions System (CVS)

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

   For more information on how to use CVS to maintain your LDP
   documents, please read Appendix C.
     ________________________________________________________________

4.3.3. Spell Check

   Some writing tools will come with their own built-in spell check
   tools. This list is only if your application does not have a spell
   check option.

   Spell Check Software

   aspell [http://aspell.sourceforge.net] http://aspell.sourceforge.net
          This spell check application can work around XML tags. By
          distinguishing between content and markup aspell is able to
          check your content and ignore the bits it shouldn't be looking
          at. If you are getting spelling errors in your markup tags you
          may be using an old version and should upgrade.

          The aspell command comes with the aspell package, included on
          most Linux distributions. Use the command as follows:

          aspell -c file

          An interactive user interface allows for fast and easy
          correction of errors. Use the --help to read more about aspell
          features.

   ispell [http://www.cs.hmc.edu/~geoff/ispell.html]
          http://www.cs.hmc.edu/~geoff/ispell.html
          Similar to aspell, but tries to spell check your markup tags.
          If you have a choice, use aspell, if not, ispell is a very
          acceptable substitute.
     ________________________________________________________________

Chapter 5. Markup

5.1. Markup: A General Overview

   A markup language is a system for marking or tagging a document to
   define the structure of the document. You may add tags to your
   document to define which parts of your document are paragraphs,
   titles, sections, glossary items (the list goes on!). There are many
   markup languages in use today. XHTML and HTML will be familiar to
   those who author web documents. The LDP uses a markup language known
   as DocBook. Each of these markup languages uses its own "controlled
   vocabulary" to describe documents. For example: in XHTML a paragraph
   would be marked up with the tagset <p></p> while in DocBook a
   paragraph would be marked up with <para></para>. The tagsets are
   defined in a quasi dictionary known as a Document Type Definition
   (DTD).

   Markup languages also follow a set of rules on how a document can be
   assembled. The rules are either SGML (Standard Generalized Markup
   Language) or XML (eXtensible Markup Language). These rules are
   essentially the "grammar" of a document's markup. SGML and XML are
   very similar. XML is a sub-set of SGML, but XML requires more
   precise use of the tags when marking up a document. The LDP accepts
   both SGML and XML documents, but prefers XML.

   There are three components to an XML/SGML document which is read by a
   person.

     * Content. As a TLDP author it is good to remember that this is the
       most important piece. Many authors will write the content first
       and add their markup later. Content may include both plain text
       and graphics. This is the only part that is required of LDP
       authors!
     * Markup. To describe the structure of a document a controlled
       vocabulary is added on top of the content. It is used to
       distinguish different kinds of content: paragraphs, lists,
       tables, warnings (and so on). The markup must also conform to
       either SGML or XML rules. If you are not comfortable adding
       markup to your document, a TLDP volunteer will do it for you.
     * Transformation. Finally the document is transformed from DocBook
       to PDF, HTML, PostScript for display in digital or paper form.
       This transformation is controlled through the Document Style
       Semantics and Specification Language (DSSSL). The DSSSL tells the
       program doing the transformation how to convert the raw markup
       into something that a human can read. The LDP uses a series of
       scripts to automate these transformations. You are not required
       to transform your own documents.

   Note Content, markup and transformations


   Steve Champeon does a great job of explaining how content, markup
   languages, and transformations all fit together in his article The
   Secret Life of Markup. Although he is writing from an HTML
   perspective, the ideas are relevant and there is an example of
   DocBook markup.
     ________________________________________________________________

5.2. DocBook: What it is and why we use it

   According to the official DocBook web site,


   DocBook is a general purpose XML and SGML document type particularly
   well suited to books and papers about computer hardware and software
   (though it is by no means limited to these applications).

   --DocBook.org

   Tip For the impatient


   In the next sections we will be explaining about the theoretical side
   of DocBook, its origins, development, advantages and disadvantages.
   If you just want the practical side, check out these sections for an
   overview of HOWTO DocBook: , Appendix D, and Appendix E from this
   guide.

   Caution For the beginner


   We wish to stress again the fact that any open document format will
   be accepted. If you feel more comfortable with plain text, OpenOffice
   or HTML, that is fine with us. If you do not look forward to learning
   DocBook, LDP volunteerd will convert your document to DocBook XML. To
   us, the most important task for our authors is the actual writing,
   not the formatting, keep that in mind!

   From the point of submission onwards, however, you will have to
   maintain your document in this XML format, but that's a piece of
   cake. Promised.

   Although there are other DTDs used to write documentation, there are
   a few reasons not to use them.

     * DocBook is the most popular DTD, being used by more than a dozen
       major open source projects from GNOME to Python to FreeBSD.
     * The tools for DocBook are more developed than others. DocBook
       support is included in most Linux distributions, allowing you to
       send raw files to be processed at the receiver's end.
     * And finally, DocBook has an extensive set of tags (over 300 in
       all) which is very useful when you are trying to describe the
       content of a document. Fortunately for new authors the majority
       of them do not need to be used for simple documentation.

   Still not convinced? Eric Raymond has written a DocBook
   Demystification HOWTO which may help.

   Convinced, but still not comfortable with the thought of working with
   DocBook? Give David Lawyer's
   [http://tldp.org/HOWTO/Howtos-with-LinuxDoc.html]
   Howtos-with-LinuxDoc-mini-HOWTO a try.
     ________________________________________________________________

5.3. XML and SGML: Why we use XML

   DocBook comes in a couple of different flavors--including both XML
   and SGML formats. This means that you may use either the SGML
   grammar/rules when adding markup, or you may use the XML
   grammar/rules. Either way you may only use one set of rules
   throughout your document, and you must define which one you are using
   at the top of your document.

   The LDP prefers the XML flavor of DocBook. There are a number of
   reasons for this including the following:

    1. Libraries for handling XML files are developing at a rapid pace.
       These utilities may make it easier for new authoring tools to
       become available.
    2. Many popular word processing programs are now creating XML
       output. While it may not be DocBook XML, this does make it easier
       for application writers to either add DocBook XML support, or
       provide some method of translating between their format and
       DocBook XML.
    3. Everyone else is doing it. While this might not be a real reason,
       it allows the LDP to keep up-to-date with similar projects.
       Tools, procedures, and issues can be worked out in a common
       framework.

   Still not convinced? Fortunately the LDP does accept a number of
   other file formats for input. The list of accepted markup languages
   can be found in Section 5.4
     ________________________________________________________________

5.4. Markup Languages Accepted by TLDP

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

Chapter 6. Distributing Your Documentation

6.1. Before Distributing Your Documentation

   Before you distribute your documentation, there are a few more things
   that you will need to check and possibly add to your document.

   Spelling and Grammar Check
          You can read more about helper applications in Section 4.3.3.
          You should also check your document for its overall flow and
          clarity.

   Abstract and Other Meta Data
          Add a short paragraph which clearly defines the scope of your
          document. For more information on how to add this information
