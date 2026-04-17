#  LDP Author Guide
###  Jorge Godoy

Publishing Department

`<`
###  Emma Jane Hogbin
`<`
###  Mark F. Komarinski
`<`
###  David C. Merrill
david -AT- lupercalia.net
2005-03-04

**Revision History**
---
Revision 4.84.74.64.54.44.34.24.1 | 2006-04-202005-03-042005-01-232004-07-142004-04-192004-04-042004-04-022004-01-27 | Revised by: MGejhejhejhejhejhejhejh
Added notes about preferred submission formats, corrected links, packaged templates.Typo fixed in sample DocBook markup. Added new web-based authoring tool and information on LaTeX to DocBook conversions.Typos fixed in xmlto notes and book template. Copied information about DocBook-capable word processing tools into the "Converting Documents to DocBook XML" Appendix; added new XML editors; and information about tools to convert other formats to DocBook XML.Updated information regarding CVS accounts and connecting to the CVS server.Added editor credit requirements to the Using DocBook section. Updated the submission procedure. New documents can now only be added by one of the Review Coordinators after the successful completion of each of the required reviews.Removed the section Contributing to The LDP (replaced by Summary of The LDP Process).Added references for LyX to DocBook conversions in the bibliography.Updated the license requirements and added them to the table of contents (moved them out of the sub-section).
This guide describes the process of submitting and publishing a document with The Linux Documentation Project (TLDP). It includes information about the tools, toolchains and formats used by TLDP. The document's primary audience is new TLDP authors, but it also contains information for seasoned documentation authors.
* * *

**Table of Contents**


1. [About this Guide](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#aboutthisguide)


1.1. [About this Guide](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#purpose)


1.2. [About The LDP](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#theldp)


1.3. [Feedback](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#feedback)


1.4. [Copyrights and Trademarks](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#copyrights)


1.5. [Acknowledgments and Thanks](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#acknowledgements)


1.6. [Document Conventions](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#conventions)


2. [Authoring TLDP Documents: An Introduction](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#introduction)


2.1. [Summary of The LDP Process](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#process)


2.2. [Mailing Lists](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#mailinglists)


3. [Writing Your Proposal](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#propose)


3.1. [Choosing a Subject](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sg-subject)


3.2. [Scope of Your Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#scope)


3.3. [Unmaintained and Out-of-date Documents](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#unmaintained)


3.4. [Developing an Outline](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sg-outline)


3.5. [Research](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#research)


4. [Write](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#write)


4.1. [Writing the Text](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sg-writingstyle)


4.2. [Edit and Proofread the Text](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sg-editing)


4.3. [Tools for Writing, Editing and Maintaining your Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools-writing)


5. [Markup](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ag-markup)


5.1. [Markup: A General Overview](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#markup)


5.2. [DocBook: What it is and why we use it](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#docbook-why)


5.3. [XML and SGML: Why we use XML](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#docbookxml)


5.4. [Markup Languages Accepted by TLDP](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#acceptedversions)


6. [Distributing Your Documentation](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#distribute)


6.1. [Before Distributing Your Documentation](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#pre-distribute)


6.2. [Licensing and Copyright](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#doc-licensing)


6.3. [Acknowledgments](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#crediting-ack)


6.4. [TLDP Review Process](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ag-review)


6.5. [Submission to LDP for publication](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#submission)


7. [Maintenance](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sg-maintaining)


7.1. [Maintaining Your Document](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sg-maintaining-support)


7.2. [Fixing Errors](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fixingerrors)


[References](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#bibliography)


A. [Templates](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#templates)


A.1. [Document Templates](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#templates-book)


A.2. [Style Sheets](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#templates-style)


A.3. [GNU Free Documentation License](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#templates-gdfl)


B. [System Setup: Editors, Validation and Transformations](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools)


B.1. [Tools for your operating system](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools-distro)


B.2. [Editing tools](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools-edit)


B.3. [Validation](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools-validate)


B.4. [Transformations](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#transformations)


B.5. [DocBook DTD](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#dtd)


B.6. [Formatting Documents](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#doc-components)


C. [Concurrent Version System (CVS)](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#cvs)


C.1. [Getting a CVS account](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#getaccount)


C.2. [Using CVS](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#usingcvs)


C.3. [CVS Resources](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#cvs-resources)


D. [DocBook: Sample Markup](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#using-docbook)


D.1. [General Tips and Tricks](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#writing-docbook)


D.2. [`<section>` and `<sectN>`: what's the difference?](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#section)


D.3. [Command Prompts](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#commandprompt)


D.4. [Encoding Indexes](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#encoding-index)


D.5. [Inserting Pictures](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#inserting-pictures)


D.6. [Markup for Metadata](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#metadata-markup)


D.7. [Bibliographies](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#doc-bib)


D.8. [Entities (shortcuts, text macros and reusable text)](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tools-entities)


D.9. [Customizing your HTML files](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#namedfiles)


E. [Converting Documents to DocBook XML](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#x2docbook)


E.1. [Text to DocBook](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#txt2docbook)


E.2. [OpenOffice.org to DocBook](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#oo2docbook)


E.3. [Microsoft Word to DocBook](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#word2docbook)


E.4. [LaTeX to DocBook](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#tex4ht)


E.5. [LyX to DocBook](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#lyx2docbook)


E.6. [DocBook to DocBook Transformations](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#docbook2docbook)


[Glossary](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#glossary)


F. [GNU Free Documentation License](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl)


F.1. [0. PREAMBLE](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-preamble)


F.2. [1. APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section1)


F.3. [2. VERBATIM COPYING](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section2)


F.4. [3. COPYING IN QUANTITY](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section3)


F.5. [4. MODIFICATIONS](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section4)


F.6. [5. COMBINING DOCUMENTS](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section5)


F.7. [6. COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section6)


F.8. [7. AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section7)


F.9. [8. TRANSLATION](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section8)


F.10. [9. TERMINATION](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section9)


F.11. [10. FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-section10)


F.12. [Addendum](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#fdl-using)


**List of Tables**


D-1. [Useful markup](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#table-useful-markup)


**List of Figures**


B-1. [epcEdit screen shot](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN1567)


B-2. [nedit screen shot](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN1598)


B-3. [Adding shell commands to nedit](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN1659)


B-4. [nsgmls output on success](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN1682)


**List of Examples**


B-1. [Setting the SGML_CATALOG_FILES and XML_CATALOG_FILES Environmental Variables](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-catalog-files)


B-2. [Example of an SGML catalog](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#example-catalog-sgml)


B-3. [Sample XML Catalog file](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-catalog-xml)


B-4. [Debugging example using xmllint](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#xmllint-example)


B-5. ["Installing" DSSSL style sheets](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-dsssl)


B-6. [Example creating HTML output](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-htmloutput)


B-7. ["Installing" DocBook Document Type Definitions](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-dtd)


B-8. [Style sheet to insert summaries in articles](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#AEN2358)


B-9. [Configuring an external entity to include the index](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-entity-external-index)


D-1. [Command Prompt with `programlisting`](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-programlisting)


D-2. [Command Prompt with `screen`](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-screen)


D-3. [Code for the generation of an index](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#example-code-index)


D-4. [Use of the attribute `zone`](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#index-zone)


D-5. [Usage of values `startofrange` and `endofrange` on the attribute`class`](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-index)


D-6. [Inserting a picture](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-picture-fileref)


D-7. [Using `<imageobject>`](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#former-figure-imageobject)


D-8. [Other Credit](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-othercredit)


D-9. [Editor](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-editor)


D-10. [Sample Meta Data](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#sample-metadata)


D-11. [A Bibliography](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-bib)


D-12. [Adding Entities](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-entities)


D-13. [Use of parameter entities](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-entity-parameters)

* * *
