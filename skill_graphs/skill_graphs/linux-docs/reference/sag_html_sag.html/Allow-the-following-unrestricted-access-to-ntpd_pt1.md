# Allow the following unrestricted access to ntpd

restrict aaa.bbb.ccc.ddd
restrict 127.0.0.1`
```

---
It is advised that you wait until you have NTP working properly before adding the restrict option. You can accidental restrict yourself from synchronizing and waste time debugging why.
NTP slowly corrects your systems time. Be patient! A simple test is to change your system clock by 10 minutes before you go to bed and then check it when you get up. The time should be correct.
Many people get the idea that instead of running the NTP daemon, they should just setup a **cron** job job to periodically run the **ntpdate** command. There are 2 main disadvantages of using using this method.
The first is that **ntpdate** does a "brute force" method of changing the time. So if your computer's time is off my 5 minutes, it immediately corrects it. In some environments, this can cause problems if time drastically changes. For example, if you are using time sensitive security software, you can inadvertently kill someones access. The NTP daemon slowly changes the time to avoid causing this kind of disruption.
The other reason is that the NTP daemon can be configured to try to learn your systems _time drift_ and then automatically adjust for it.
* * *
#  14.7. NTP Toolkit
There are a number of utilities available to check if NTP is doing it's job. The **ntpq -p** command will print out your system's current time status.
```
`#` `**ntpq -p**`
`     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*cudns.cit.corne ntp0.usno.navy.  2 u  832 1024  377   43.208    0.361   2.646
 LOCAL(0)        LOCAL(0)        10 l   13   64  377    0.000    0.000   0.008`
```

---
The **ntpdc -c loopinfo** will display how far off the system time is in seconds, based upon the last time the remote server was contacted.
```
`#` `**ntpdc -c loopinfo**`
`offset:               -0.004479 s
frequency:            133.625 ppm
poll adjust:          30
watchdog timer:       404 s`

```

---
**ntpdc -c kerninfo** will display the current remaining correction.
```
`#` `**ntpdc -c kerninfo**`
`pll offset:           -0.003917 s
pll frequency:        133.625 ppm
maximum error:        0.391414 s
estimated error:      0.003676 s
status:               0001  pll
pll time constant:    6
precision:            1e-06 s
frequency tolerance:  512 ppm
pps frequency:        0.000 ppm
pps stability:        512.000 ppm
pps jitter:           0.0002 s
calibration interval: 4 s
calibration cycles:   0
jitter exceeded:      0
stability exceeded:   0
calibration errors:   0`

```

---
A slightly more different version of **ntpdc -c kerninfo** is **ntptime**
```
`#` `**ntptime**`
`ntp_gettime() returns code 0 (OK)
  time c35e2cc7.879ba000  Thu, Nov 13 2003 11:16:07.529, (.529718),
  maximum error 425206 us, estimated error 3676 us
ntp_adjtime() returns code 0 (OK)
  modes 0x0 (),
  offset -3854.000 us, frequency 133.625 ppm, interval 4 s,
  maximum error 425206 us, estimated error 3676 us,
  status 0x1 (PLL),
  time constant 6, precision 1.000 us, tolerance 512 ppm,
  pps frequency 0.000 ppm, stability 512.000 ppm, jitter 200.000 us,
  intervals 0, jitter exceeded 0, stability exceeded 0, errors 0.`
```

---
Yet another way to see how well NTP is working is with the **ntpdate -d** command. This will contact an NTP server and determine the time difference but not change your system's time.
```
`#` `**ntpdate -d 132.236.56.250**`
`13 Nov 14:43:17 ntpdate[29631]: ntpdate 4.1.1c-rc1@1.836 Thu Feb 13 12:17:20 EST 2003 (1)
transmit(132.236.56.250)
receive(132.236.56.250)
transmit(132.236.56.250)
receive(132.236.56.250)
transmit(132.236.56.250)
receive(132.236.56.250)
transmit(132.236.56.250)
receive(132.236.56.250)
transmit(132.236.56.250)
server 132.236.56.250, port 123
stratum 2, precision -17, leap 00, trust 000
refid [192.5.41.209], delay 0.06372, dispersion 0.00044
transmitted 4, in filter 4
reference time:    c35e5998.4a46cfc8  Thu, Nov 13 2003 14:27:20.290
originate timestamp: c35e5d55.d69a6f82  Thu, Nov 13 2003 14:43:17.838
transmit timestamp:  c35e5d55.d16fc9bc  Thu, Nov 13 2003 14:43:17.818
filter delay:  0.06522  0.06372  0.06442  0.06442
         0.00000  0.00000  0.00000  0.00000
filter offset: 0.000036 0.001020 0.000527 0.000684
         0.000000 0.000000 0.000000 0.000000
delay 0.06372, dispersion 0.00044
offset 0.001020

13 Nov 14:43:17 ntpdate[29631]: adjust time server 132.236.56.250 offset 0.001020 sec`
```

---
If you want actually watch the system synchronize you can use **ntptrace**.
```
`#` `**ntptrace 132.236.56.250**`
`cudns.cit.cornell.edu: stratum 2, offset -0.003278, synch distance 0.02779
truetime.ntp.com: stratum 1, offset -0.014363, synch distance 0.00000, refid 'ACTS'`
```

---
If you need your system time synchronized immediately you can use the **ntpdate remote-servername** to force a synchronization. No waiting!
```
`#` `**ntpdate 132.236.56.250**`
13 Nov 14:56:28 ntpdate[29676]: adjust time server 132.236.56.250 offset -0.003151 sec
``
```

---
* * *
#  14.8. Some known NTP servers
A list of public NTP servers can be obtained from:
* * *
#  14.9. NTP Links
More detailed information on NTP can be obtained from the NTP homepage:
Or from
* * *
#  Chapter 15. System Logs --To Be Added
Log info, rotation, monitoring, etc..
* * *
#  Chapter 16. System Updates --To Be Added
> "A lie gets halfway around the world before the truth has a chance to get its pants on." Winston Churchill
Discussion on how and when to update the system.
* * *
#  Chapter 17. The Linux Kernel Source
> "Black holes are where God divided by zero. " Steven Wright
BASIC info on the kernel source and compiling it. It will also provide some info on kdb debugger. Refer to other kernel HOWTO's for more info.
* * *
#  Chapter 18. Finding Help
> "Help me if you can I'm feeling down. And I do appreciate you being 'round." - The Beatles
Help is out there. You just have to know where to look. With Linux there are an amazing number of places you can go. There are mailing lists, IRC channels, web pages with public forums, and many other resources available. This chapter will try to help you get the most out of your quest for help.
* * *
#  18.1. Newsgroups and Mailing Lists
This guide cannot teach you everything about Linux. There just isn't enough space. It is almost inevitable that at some point you will find something you need to do, that isn't covered in this (or any other) document at the LDP.
One of the nicest things about Linux is the large number of forums devoted to it. There are forums relating to almost all facets of Linux ranging from newbie FAQs to in depth kernel development issues. To receive the most from them, there are a few things you can do.
* * *
##  18.1.1. Finding The Right Forum
The first thing to do is to find an appropriate forum. There are many newsgroups and mailing lists devoted to Linux, so try to find and use the one which most closely matches your question. For example, there isn't much point in you asking a question about sendmail in a forum devoted to Linux kernel development. At best the people there will think you are stupid and you will get few responses, at worst you may receive lots of highly insulting replies (flames). A quick look through the newsgroups available finds comp.mail.sendmail, which looks like an appropriate place to ask a sendmail question. Your news client probably has a list of the newsgroups available to you, but if not then a full list of newsgroups is available at
* * *
##  18.1.2. Before You Post
Now that you have found your appropriate forum, you may think you are ready to post your question. Stop. You aren't ready yet. Have you already looked for the answer yourself? There are a huge number of HOWTOs and FAQs available, if any of them relate to the thing you are having a problem with then _read them first_. Even if they don't contain the answer to your problem, what they will do is give you a better understanding of the subject area, and that understanding will allow you to ask a more informed and sensible question. There are also archives of newsgroups and mailing lists and it is entirely possible that your question has been asked and answered previously. _before_ posting a question.
* * *
##  18.1.3. Writing Your Post
Okay, you have found your appropriate forum, you have read the relevant HOWTOs and FAQs, you have searched the web, but you still have not found the answer you need. Now you can start writing your post. It is always a good idea to make it clear that you already have read up on the subject by saying something like ``I have read the Winmodem-HOWTO and the PPP FAQ, but neither contained what I was looking for, searching for `Winmodem Linux PPP Setup' on google didn't return anything of use either''. This shows you to be someone who is willing to make an effort rather than a lazy idiot who requires spoonfeeding. The former is likely to receive help if anyone knows the answer, the latter is likely to meet with either stony silence or outright derision.
Write in clear, grammatical and correctly spelt English. This is incredibly important. It marks you as a precise and considered thinker. There are no such words as ``u'' or ``b4.'' Try to make yourself look like an educated and intelligent person rather than an idiot. It will help. I promise.
Similarly do not type in all capitals LIKE THIS. That is considered shouting and looks very rude.
Provide clear details stating what the problem is and what you have already tried to do to fix it. A question like ``My linux has stopped working, what can I do?'' is totally useless. Where has it stopped working? In what way has it stopped working? You need to be as precise as possible. There are limits however. Try not to include irrelevant information either. If you are having problems with your mail client it is unlikely that a dump of your kernel boot log (**dmesg**) would be of help.
Don't ask for replies by private email. The point of most Linux forums is that everybody can learn something from each other. Asking for private replies simply removes value from the newsgroup or mailing list.
* * *
##  18.1.4. Formatting Your Post
Do not post in HTML. Many Linux users have mail clients which can't easily read HTML email. Whilst with some effort, they _can_ read HTML email, they usually don't. If you send them HTML mail it often gets deleted unread. Send plain text emails, they will reach a wider audience that way.
* * *
##  18.1.5. Follow Up
After your problem has been solved, post a short followup explaining what the problem was and how you solved it. People will appreciate this as it not only gives a sense of closure about the problem but also helps the next time someone has a similar question. When they look at the archives of the newsgroup or mailing list, they will see you had the same problem, the discussion that followed your question and your final solution.
* * *
##  18.1.6. More Information
This short guide is simply a paraphrase and summary of the excellent (and more detailed) document ``How To Ask Questions The Smart Way'' by Eric S Raymond.
* * *
#  18.2. IRC
IRC (Internet Relay Chat) is not covered in the Eric Raymond document, but IRC can also be an excellent way of finding the answers you need. However it does require some practice in asking questions in the right way. Most IRC networks have busy #linux channels and if the answer to your question is contained in the man pages, or in the HOWTOs then expect to be told to go read them. The rule about typing in clear and grammatical English still applies.
Most of what has been said about newsgroups and mailing lists is still relevant for IRC, with a the following additions
* * *
##  18.2.1. Colours
Do not use colours, bold, underline or strange (non ASCII) characters. This breaks some older terminals and is just plain ugly to look at. If you arrive in a channel and start spewing colour or bold then expect to be kicked out.
* * *
##  18.2.2. Be Polite
Remember you are not entitled to an answer. If you ask the question in the right way then you will probably get one, but you have no right to get one. The people in Linux IRC channels are all there on their own time, nobody is paying them, especially not you.
Be polite. Treat others as you would like to be treated. If you think people are not being polite to you then don't start calling them names or getting annoyed, become even politer. This makes them look foolish rather than dragging you down to their level.
Don't go slapping anyone with large trouts. Would you believe this has been done before once or twice? And that we it wasn't funny the first time?
* * *
##  18.2.3. Type Properly, in English
Most #linux channels are English channels. Speak English whilst in them. Most of the larger IRC networks also have #linux channel in other languages, for example the French language channel might be called #linuxfr, the Spanish one might be #linuxes or #linuxlatino. If you can't find the right channel then asking in the main #linux channel (preferably in English) should help you find the one you are looking for.
Do not type like a ``1337 H4X0R d00d!!!''. Even if other people are. It looks silly and thereby makes you look silly. At best you will only look like an idiot, at worst you will be derided then kicked out.
* * *
##  18.2.4. Port scanning
Never _ever_ ask anyone to port scan you, or try to ``hack'' you. This is inviolable. There is no way of knowing that you are who you say you are, or that the IP that you are connected from belongs to you. Don't put people in the position where they have to say no to a request like this.
_Don't ever port scan anyone_ , even if they ask you to. You have no way to tell that they are who they say they are or that the IP they are connected from is their own IP. In some jurisdictions port scanning may be illegal and it is certainly against the Terms of Service of most ISPs. Most people log TCP connections, they will notice they are being scanned. Most people _will_ report you to your ISP for this (it is trivial to find out who that is).
* * *
##  18.2.5. Keep it in the Channel
Don't /msg anyone unless they ask you to. It diminishes the usefulness of the channel and some people just prefer that you not do it.
* * *
##  18.2.6. Stay On Topic
Stay on topic. The channel is a ``Linux'' channel, not a ``What Uncle Bob Got Up To Last Weekend'' channel. Even if you see other people being off topic, this does not mean that you should be. They are probably channel regulars and different conventions apply to them.
* * *
##  18.2.7. CTCPs
If you are thinking of mass CTCP pinging the channel or CTCP version or CTCP anything, then think again. It is liable to get you kicked out very quickly.
If you are not familiar with IRC, CTCP stands for Client To Client Protocol. It is a method whereby you can find out things about other peoples' clients. See the documentation for your IRC for more details.
* * *
##  18.2.8. Hacking, Cracking, Phreaking, Warezing
Don't ask about exploits, unless you are looking for a further way to be unceremoniously kicked out.
Don't be in hacker/cracker/phreaker/warezer channels whilst in a #linux channel. For some reason the people in charge of #linux channels seem to hate people who like causing destruction to people's machines or who like to steal software. Can't imagine why.
* * *
##  18.2.9. Round Up
Apologies if that seems like a lot of DON'Ts, and very few DOs. The DOs were already pretty much covered in the section on newsgroups and mailing lists.
Probably the best thing you can do is to go into a #linux channel, sit there and watch, getting the feel for a half hour before you say anything. This can help you to recognize the correct tone you should be using.
* * *
##  18.2.10. Further Reading
There are excellent FAQs about how to get the most of IRC #linux channels. Most #linux channels have an FAQ and/or set or channel rules. How to find this will usually be in the channel topic (which you can see at any time using the **/topic** command. Make sure you read the rules if there are any and follow them. One fairly generic set of rules and advice is the ``Undernet #linux FAQ'' which can be found at
* * *
#  Appendix A. GNU Free Documentation License
#  A.1. PREAMBLE
The purpose of this License is to make a manual, textbook, or other functional and useful document "free" in the sense of freedom: to assure everyone the effective freedom to copy and redistribute it, with or without modifying it, either commercially or noncommercially. Secondarily, this License preserves for the author and publisher a way to get credit for their work, while not being considered responsible for modifications made by others.
This License is a kind of "copyleft", which means that derivative works of the document must themselves be free in the same sense. It complements the GNU General Public License, which is a copyleft license designed for free software.
We have designed this License in order to use it for manuals for free software, because free software needs free documentation: a free program should come with manuals providing the same freedoms that the software does. But this License is not limited to software manuals; it can be used for any textual work, regardless of subject matter or whether it is published as a printed book. We recommend this License principally for works whose purpose is instruction or reference.
* * *
#  A.2. APPLICABILITY AND DEFINITIONS
This License applies to any manual or other work, in any medium, that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. Such a notice grants a world-wide, royalty-free license, unlimited in duration, to use that work under the conditions stated herein. The "Document", below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you". You accept the license if you copy, modify or distribute the work in a way requiring permission under copyright law.
A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.
A "Secondary Section" is a named appendix or a front-matter section of the Document that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (Thus, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical or political position regarding them.
The "Invariant Sections" are certain Secondary Sections whose titles are designated, as being those of Invariant Sections, in the notice that says that the Document is released under this License. If a section does not fit the above definition of Secondary then it is not allowed to be designated as Invariant. The Document may contain zero Invariant Sections. If the Document does not identify any Invariant Sections then there are none.
The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the Document is released under this License. A Front-Cover Text may be at most 5 words, and a Back-Cover Text may be at most 25 words.
A "Transparent" copy of the Document means a machine-readable copy, represented in a format whose specification is available to the general public, that is suitable for revising the document straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup, or absence of markup, has been arranged to thwart or discourage subsequent modification by readers is not Transparent. An image format is not Transparent if used for any substantial amount of text. A copy that is not "Transparent" is called "Opaque".
Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML, PostScript or PDF designed for human modification. Examples of transparent image formats include PNG, XCF and JPG. Opaque formats include proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML, PostScript or PDF produced by some word processors for output purposes only.
The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.
A section "Entitled XYZ" means a named subunit of the Document whose title either is precisely XYZ or contains XYZ in parentheses following text that translates XYZ in another language. (Here XYZ stands for a specific section name mentioned below, such as "Acknowledgements", "Dedications", "Endorsements", or "History".) To "Preserve the Title" of such a section when you modify the Document means that it remains a section "Entitled XYZ" according to this definition.
The Document may include Warranty Disclaimers next to the notice which states that this License applies to the Document. These Warranty Disclaimers are considered to be included by reference in this License, but only as regards disclaiming warranties: any other implication that these Warranty Disclaimers may have is void and has no effect on the meaning of this License.
* * *
#  A.3. VERBATIM COPYING
You may copy and distribute the Document in any medium, either commercially or noncommercially, provided that this License, the copyright notices, and the license notice saying this License applies to the Document are reproduced in all copies, and that you add no other conditions whatsoever to those of this License. You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute. However, you may accept compensation in exchange for copies. If you distribute a large enough number of copies you must also follow the conditions in section 3.
You may also lend copies, under the same conditions stated above, and you may publicly display copies.
* * *
#  A.4. COPYING IN QUANTITY
If you publish printed copies (or copies in media that commonly have printed covers) of the Document, numbering more than 100, and the Document's license notice requires Cover Texts, you must enclose the copies in covers that carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly and legibly identify you as the publisher of these copies. The front cover must present the full title with all words of the title equally prominent and visible. You may add other material on the covers in addition. Copying with changes limited to the covers, as long as they preserve the title of the Document and satisfy these conditions, can be treated as verbatim copying in other respects.
If the required texts for either cover are too voluminous to fit legibly, you should put the first ones listed (as many as fit reasonably) on the actual cover, and continue the rest onto adjacent pages.
If you publish or distribute Opaque copies of the Document numbering more than 100, you must either include a machine-readable Transparent copy along with each Opaque copy, or state in or with each Opaque copy a computer-network location from which the general network-using public has access to download using public-standard network protocols a complete Transparent copy of the Document, free of added material. If you use the latter option, you must take reasonably prudent steps, when you begin distribution of Opaque copies in quantity, to ensure that this Transparent copy will remain thus accessible at the stated location until at least one year after the last time you distribute an Opaque copy (directly or through your agents or retailers) of that edition to the public.
It is requested, but not required, that you contact the authors of the Document well before redistributing any large number of copies, to give them a chance to provide you with an updated version of the Document.
* * *
#  A.5. MODIFICATIONS
You may copy and distribute a Modified Version of the Document under the conditions of sections 2 and 3 above, provided that you release the Modified Version under precisely this License, with the Modified Version filling the role of the Document, thus licensing distribution and modification of the Modified Version to whoever possesses a copy of it. In addition, you must do these things in the Modified Version:
**GNU FDL Modification Conditions**
  1. Use in the Title Page (and on the covers, if any) a title distinct from that of the Document, and from those of previous versions (which should, if there were any, be listed in the History section of the Document). You may use the same title as a previous version if the original publisher of that version gives permission.
