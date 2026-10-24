#  E.5. LyX to DocBook
This section is contributed by Chris Karakas.
You can use the LyX-to-X package to write your document conveniently in LyX (a visual editor originally developed as a graphical frontend to LaTeX), then export it to DocBook SGML and submit it to The LDP. This method is presented by
In the LyX-to-X project, LyX is used as a comfortable graphical SGML editor. Once the document is exported to SGML from LyX, it undergoes a series of transformations through sed and awk scripts that correct the SGML code, computes the Index, inserts the Bibliography and the Appendix and takes care of the correct invocation of openjade, pdftex, pdfjadetex and all the other necessary programs for the generation of HTML (chunked or not), PDF (with images, bookmarks, thumbnails and hyperlinks), PS, RTF and TXT versions.
All aspects of document processing are handled, including automatic Index generation, display of Mathematics in TeX quality both online and in print formats, as well as the use of bibliographic databases with
* * *
