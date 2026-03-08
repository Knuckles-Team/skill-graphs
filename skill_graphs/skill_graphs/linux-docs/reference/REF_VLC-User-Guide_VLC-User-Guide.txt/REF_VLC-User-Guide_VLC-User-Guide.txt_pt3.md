
��*�cropright: number of pixels removed from the right of the video .

��*�hq: high quality transcoding (uses more CPU) .

��*�qmin: minimum video quantiser scale (VBR)

��*�qmax: maximum video quantiser scale (VBR) .


-----------------------------------------------------------------------------
4.4.3.5. es

 Make separate Elementary Streams .

Options:

��*�access_audio: how to send the audio track: file, udp, rtp or http .

��*�access_video: how to send the vid�o track: file, udp, rtp or http .

��*�access: if you want the audio and the video tracks to use the same
    access, use this option instead of the two above .

��*�mux_audio: which muxer (ie, which format) will be used for the audio
    track. It can be one of avi (for AVI format), ogg (for OGG format), ps
    (for MPEG2-PS format), ts (for MPEG2-TS format) .

��*�mux_video: which muxer (ie, which format) will be used for the video
    track. It can be one of avi (for AVI format), ogg (for OGG format), ps
    (for MPEG2-PS format), ts (for MPEG2-TS format) .

��*�mux: if you want the audio and the video tracks to use the same muxer,
    use this option instead of the two above .

��*�url_audio: if you use the file access, it will be the location where to
    store the audio track; if you use another access, it will be the unicast
    or multicast IP address where you want to stream .

��*�url_video: if you use the file access, it will be the location where to
    store the vid�o track; if you use another access, it will be the unicast
    or multicast IP address where you want to stream .

��*�url: if you want the audio and the video tracks to use the same url, use
    this option instead of the two above .


Note In the url options, if you use the file access, you can use the
     following macros in the filename:

     ��*�%n = stream number ;

     ��*�%c = FOURCC ;

     ��*�%m = muxer ;

     ��*�%a = access.


-----------------------------------------------------------------------------

4.4.3.6. Miscellaneous

 Here are a few additional global options

��*�--no-sout-audio disables audio stream output .

��*�--no-sout-video disables video stream output .


  The stream output also offers a simplified syntax, with which you can only
you use the standard module main options :
% vlc input_stream --sout access/mux:url

  where access, mux and url are as defined in the options of the standard
module .
-----------------------------------------------------------------------------

4.4.4. Examples

 To understand fully the complex syntax of VLC's stream output, please look
at the use cases of the VideoLAN HOWTO .
-----------------------------------------------------------------------------

4.5. Other Options

4.5.1. Audio options

��*�--noaudio disables audio output .

��*�--mono forces VLC to treat the stream in mono audio .

��*�--volume <integer> sets the level of audio output .

��*�--aout-rate <integer> sets the audio output frequency (Hz) .

��*�--desync <integer> compensates desynchronization of audio (ms) .

��*�--headphone activates headphone virtual spatialization effect .

��*�--headphone-dim sets headphone characteristic dimension .


-----------------------------------------------------------------------------
4.5.2. Video options

��*�--novideo disables video output .

��*�--greyscale turns video output into greyscale mode .

��*�--fullscreen sets fullscreen video .

��*�--nooverlay disables hardware acceleration for the video output .

��*�--width, --height <integer> sets the video window dimensions .

��*�--zoom <float> adds a zoom factor .

��*�--aspect-ratio <mode> forces source aspect ratio .

��*�--spumargin <integer> forces SPU subtitles position .


-----------------------------------------------------------------------------
4.5.3. Playlist options

��*�--playlist launches playlist on startup .

��*�--random plays files randomly forever .

��*�--enqueue enqueues items in playlist .

��*�--loop loops playlist on end .


-----------------------------------------------------------------------------
4.5.4. Network options

��*�--server-port <integer> sets server port .

��*�--iface <string> specifies the network interface to use .

��*�--iface-addr <string> specifies your network interface IP address .

��*�--mtu <integer> specifies the MTU of the network interface .

��*�--ipv6 forces IPv6 .

��*�--ipv4 forces IPv4 .


-----------------------------------------------------------------------------
4.5.5. CPU options

��*�--nommx disables the use of MMX CPU extensions .

��*�--no3dn disables the use of 3D Now! CPU extensions .

��*�--nommxext disables the use of MMX Ext CPU extensions .

��*�--nosse disables the use of SSE CPU extensions .


-----------------------------------------------------------------------------
4.5.6. Miscellaneous options

��*�--quiet be quiet .

��*�--color displays color messages .

��*�--search-path <string> specifies interface default search path .

��*�--plugin-path <string> specifies plugin search path .

��*�--dvd <string> specifies the default VCD device .

��*�--vcd <string> specifies the default VCD device .

��*�--program <;integer> specifies program (SID) (for streams with several
    programs, like satellite ones) .

��*�--audio-type <integer> specifies the default audio type to use with dvds
    .

��*�--audio-channel <integer> specifies the default audio channel to use with
    dvds .

��*�--spu-channel <integer> specifies the default subtitle channel to use
    with dvds .


-----------------------------------------------------------------------------
4.5.7. Help options

��*�--verbose <verbosity> specifies verbosity level .

��*�--help gives you all available options .

��*�--longhelp gives you a detailed version of the available options .

��*�--version gives you information about the current VLC version .

��*�--list displays a list of available plugins .

��*�--module <module> displays help about specified module .


-----------------------------------------------------------------------------
Chapter 5. The Mozilla plugin

 VLC can also be embedded in a web browser ! For the moment, this function is
only available with [http://www.mozilla.org/] Mozilla under GNU/Linux .
-----------------------------------------------------------------------------

5.1. Install the plugin

5.1.1. GNU/Linux Debian

 You should already have the following lines in your /etc/apt/sources.list
file :
deb http://www.videolan.org/pub/videolan/debian $(ARCH)/
deb-src http://www.videolan.org/pub/videolan/debian sources/

 Install the mozilla-plugin-vlc package :
# apt-get update
# apt-get install mozilla-plugin-vlc
-----------------------------------------------------------------------------

5.1.2. Compile the sources yourself

Install the Mozilla development package (mozilla-dev under Debian) .

  Install the required libraries like for a normal VLC install (from the
sources, or from the packages with the development packages).

  Download the sources of the lastest release : get the file
vlc-version.tar.gz from the VLC sources download page. Uncompress-it,
configure-it, compile and install T�l�chargez les sources de la derni�re
version : r�cup�rez le fichier vlc-version.tar.gz depuis la page de
t�l�chargement des sources de VLC. D�compressez-le, configurez-le, compilez
et installez :
% tar xvzf vlc-version.tar.gz
% cd vlc-version
% ./configure --enable-mozilla
% make
% su
Password:  [Root Password]
# make install
-----------------------------------------------------------------------------

5.2. Build HTML pages that use the plugin

 Here are a few examples of HTML pages that use the Mozilla plugin .
-----------------------------------------------------------------------------

5.2.1. Example 1

 In this example, the plugin will read an HTTP stream inside the web page. If
the user goes fullscreen, he will have to press f to go back in normal view .
<html>
<head><title>Demo of VLC mozilla plugin</title></head>

<body>

<h1>Demo of VLC mozilla plugin - Example 1</h1>

<embed type="application/x-vlc-plugin"
         name="video1"
         autoplay="no" loop="yes" width="400" height="300"
         target="http://server.example.org/video1.vob" />
<br />
  <a href="javascript:;" onclick='document.video1.play()'>Play video1</a>
  <a href="javascript:;" onclick='document.video1.pause()'>Pause video1</a>
  <a href="javascript:;" onclick='document.video1.stop()'>Stop video1</a>
  <a href="javascript:;" onclick='document.video1.fullscreen()'>Fullscreen</a>

</body>
</html>
-----------------------------------------------------------------------------

5.2.2. Example 2

In this example, the plugin will read a multicast UDP stream in a dedicated
video output window .
<html>
<head><title>Demo of VLC mozilla plugin</title></head>

<body>

<h1>Demo of VLC mozilla plugin - Example 2</h1>

<embed type="application/x-vlc-plugin"
         name="video2"
         autoplay="no" loop="no" hidden="yes"
         target="udp:@239.255.12.42" />
<br />
  <a href="javascript:;" onclick='document.video2.play()'>Play video2</a>
  <a href="javascript:;" onclick='document.video2.stop()'>Stop video2</a>
  <a href="javascript:;" onclick='document.video2.fullscreen()'>Fullscreen</a>

</body>
</html>
-----------------------------------------------------------------------------

Appendix A. GNU Free Documentation License

Version 1.2, November 2002


    Copyright (C) 2000,2001,2002 Free Software Foundation, Inc. 59 Temple
    Place, Suite 330, Boston, MA 02111-1307 USA Everyone is permitted to copy
    and distribute verbatim copies of this license document, but changing it
    is not allowed.

-----------------------------------------------------------------------------
A.1. PREAMBLE

The purpose of this License is to make a manual, textbook, or other
functional and useful document "free" in the sense of freedom: to assure
everyone the effective freedom to copy and redistribute it, with or without
modifying it, either commercially or noncommercially. Secondarily, this
License preserves for the author and publisher a way to get credit for their
work, while not being considered responsible for modifications made by
others.

This License is a kind of "copyleft", which means that derivative works of
the document must themselves be free in the same sense. It complements the
GNU General Public License, which is a copyleft license designed for free
software.

We have designed this License in order to use it for manuals for free
software, because free software needs free documentation: a free program
should come with manuals providing the same freedoms that the software does.
But this License is not limited to software manuals; it can be used for any
textual work, regardless of subject matter or whether it is published as a
printed book. We recommend this License principally for works whose purpose
is instruction or reference.
-----------------------------------------------------------------------------

A.2. APPLICABILITY AND DEFINITIONS

This License applies to any manual or other work, in any medium, that
contains a notice placed by the copyright holder saying it can be distributed
under the terms of this License. Such a notice grants a world-wide,
royalty-free license, unlimited in duration, to use that work under the
conditions stated herein. The "Document", below, refers to any such manual or
work. Any member of the public is a licensee, and is addressed as "you". You
accept the license if you copy, modify or distribute the work in a way
requiring permission under copyright law.

A "Modified Version" of the Document means any work containing the Document
or a portion of it, either copied verbatim, or with modifications and/or
translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of the
Document that deals exclusively with the relationship of the publishers or
authors of the Document to the Document's overall subject (or to related
matters) and contains nothing that could fall directly within that overall
subject. (Thus, if the Document is in part a textbook of mathematics, a
Secondary Section may not explain any mathematics.) The relationship could be
a matter of historical connection with the subject or with related matters,
or of legal, commercial, philosophical, ethical or political position
regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are
designated, as being those of Invariant Sections, in the notice that says
that the Document is released under this License. If a section does not fit
the above definition of Secondary then it is not allowed to be designated as
Invariant. The Document may contain zero Invariant Sections. If the Document
does not identify any Invariant Sections then there are none.

The "Cover Texts" are certain short passages of text that are listed, as
Front-Cover Texts or Back-Cover Texts, in the notice that says that the
Document is released under this License. A Front-Cover Text may be at most 5
words, and a Back-Cover Text may be at most 25 words.

A "Transparent" copy of the Document means a machine-readable copy,
represented in a format whose specification is available to the general
public, that is suitable for revising the document straightforwardly with
generic text editors or (for images composed of pixels) generic paint
programs or (for drawings) some widely available drawing editor, and that is
suitable for input to text formatters or for automatic translation to a
variety of formats suitable for input to text formatters. A copy made in an
otherwise Transparent file format whose markup, or absence of markup, has
been arranged to thwart or discourage subsequent modification by readers is
not Transparent. An image format is not Transparent if used for any
substantial amount of text. A copy that is not "Transparent" is called
"Opaque".

Examples of suitable formats for Transparent copies include plain ASCII
without markup, Texinfo input format, LaTeX input format, SGML or XML using a
publicly available DTD, and standard-conforming simple HTML, PostScript or
PDF designed for human modification. Examples of transparent image formats
include PNG, XCF and JPG. Opaque formats include proprietary formats that can
be read and edited only by proprietary word processors, SGML or XML for which
the DTD and/or processing tools are not generally available, and the
machine-generated HTML, PostScript or PDF produced by some word processors
for output purposes only.

The "Title Page" means, for a printed book, the title page itself, plus such
following pages as are needed to hold, legibly, the material this License
requires to appear in the title page. For works in formats which do not have
any title page as such, "Title Page" means the text near the most prominent
appearance of the work's title, preceding the beginning of the body of the
text.

A section "Entitled XYZ" means a named subunit of the Document whose title
either is precisely XYZ or contains XYZ in parentheses following text that
translates XYZ in another language. (Here XYZ stands for a specific section
name mentioned below, such as "Acknowledgements", "Dedications",
"Endorsements", or "History".) To "Preserve the Title" of such a section when
you modify the Document means that it remains a section "Entitled XYZ"
according to this definition.

The Document may include Warranty Disclaimers next to the notice which states
that this License applies to the Document. These Warranty Disclaimers are
considered to be included by reference in this License, but only as regards
disclaiming warranties: any other implication that these Warranty Disclaimers
may have is void and has no effect on the meaning of this License.
-----------------------------------------------------------------------------

A.3. VERBATIM COPYING

You may copy and distribute the Document in any medium, either commercially
or noncommercially, provided that this License, the copyright notices, and
the license notice saying this License applies to the Document are reproduced
in all copies, and that you add no other conditions whatsoever to those of
this License. You may not use technical measures to obstruct or control the
reading or further copying of the copies you make or distribute. However, you
may accept compensation in exchange for copies. If you distribute a large
enough number of copies you must also follow the conditions in section 3.

You may also lend copies, under the same conditions stated above, and you may
publicly display copies.
-----------------------------------------------------------------------------

A.4. COPYING IN QUANTITY

If you publish printed copies (or copies in media that commonly have printed
covers) of the Document, numbering more than 100, and the Document's license
notice requires Cover Texts, you must enclose the copies in covers that
carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the
front cover, and Back-Cover Texts on the back cover. Both covers must also
clearly and legibly identify you as the publisher of these copies. The front
cover must present the full title with all words of the title equally
prominent and visible. You may add other material on the covers in addition.
Copying with changes limited to the covers, as long as they preserve the
title of the Document and satisfy these conditions, can be treated as
verbatim copying in other respects.

If the required texts for either cover are too voluminous to fit legibly, you
should put the first ones listed (as many as fit reasonably) on the actual
cover, and continue the rest onto adjacent pages.

If you publish or distribute Opaque copies of the Document numbering more
than 100, you must either include a machine-readable Transparent copy along
with each Opaque copy, or state in or with each Opaque copy a
computer-network location from which the general network-using public has
access to download using public-standard network protocols a complete
Transparent copy of the Document, free of added material. If you use the
latter option, you must take reasonably prudent steps, when you begin
distribution of Opaque copies in quantity, to ensure that this Transparent
copy will remain thus accessible at the stated location until at least one
year after the last time you distribute an Opaque copy (directly or through
your agents or retailers) of that edition to the public.

It is requested, but not required, that you contact the authors of the
Document well before redistributing any large number of copies, to give them
a chance to provide you with an updated version of the Document.
-----------------------------------------------------------------------------

A.5. MODIFICATIONS

You may copy and distribute a Modified Version of the Document under the
conditions of sections 2 and 3 above, provided that you release the Modified
Version under precisely this License, with the Modified Version filling the
role of the Document, thus licensing distribution and modification of the
Modified Version to whoever possesses a copy of it. In addition, you must do
these things in the Modified Version:

 A. Use in the Title Page (and on the covers, if any) a title distinct from
    that of the Document, and from those of previous versions (which should,
    if there were any, be listed in the History section of the Document). You
    may use the same title as a previous version if the original publisher of
    that version gives permission.

 B. List on the Title Page, as authors, one or more persons or entities
    responsible for authorship of the modifications in the Modified Version,
    together with at least five of the principal authors of the Document (all
    of its principal authors, if it has fewer than five), unless they release
    you from this requirement.

 C. State on the Title page the name of the publisher of the Modified
    Version, as the publisher.

 D. Preserve all the copyright notices of the Document.

 E. Add an appropriate copyright notice for your modifications adjacent to
    the other copyright notices.

 F. Include, immediately after the copyright notices, a license notice giving
    the public permission to use the Modified Version under the terms of this
    License, in the form shown in the Addendum below.

 G. Preserve in that license notice the full lists of Invariant Sections and
    required Cover Texts given in the Document's license notice.

 H. Include an unaltered copy of this License.

 I. Preserve the section Entitled "History", Preserve its Title, and add to
    it an item stating at least the title, year, new authors, and publisher
    of the Modified Version as given on the Title Page. If there is no
    section Entitled "History" in the Document, create one stating the title,
    year, authors, and publisher of the Document as given on its Title Page,
    then add an item describing the Modified Version as stated in the
    previous sentence.

 J. Preserve the network location, if any, given in the Document for public
    access to a Transparent copy of the Document, and likewise the network
    locations given in the Document for previous versions it was based on.
    These may be placed in the "History" section. You may omit a network
    location for a work that was published at least four years before the
    Document itself, or if the original publisher of the version it refers to
    gives permission.

 K. For any section Entitled "Acknowledgements" or "Dedications", Preserve
    the Title of the section, and preserve in the section all the substance
    and tone of each of the contributor acknowledgements and/or dedications
    given therein.

 L. Preserve all the Invariant Sections of the Document, unaltered in their
    text and in their titles. Section numbers or the equivalent are not
