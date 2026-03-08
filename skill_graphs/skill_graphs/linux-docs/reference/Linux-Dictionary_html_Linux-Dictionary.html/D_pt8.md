
**dnet-common**

Base package for Linux DECnet This is the base package for Linux DECnet. it contains the necessary configuration files and a script to set up the MAC address of your ethernet card(s) at boot-up. You will also need to be running a 2.4+ kernel and have DECnet either built as a module or compiled into the kernel. To do useful work with DECnet you will need the libdnet package and probably also dnet-progs. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnet-progs**

DECnet user programs and daemons These tools are the application layer interface for DECnet on Linux systems. They provide file/terminal access facilities between OpenVMS and Linux and remote execution of commands. Also included is a Linux version of the VMS "Phone" utility and a VMSMail to SMTP gateway. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNHR**

Dynamic Non Hierarchical Routing From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNI**

De.Newusers.Info (Usenet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNI**

DECnet Network Interface From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNIC**

Data Network Identification Code (X.121) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNQ**

De.Newusers.Questions (Usenet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNR**

Digital Noise Reduction From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNS**

DOMAIN Name System (Internet, RFC 1034/1035, DNS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNS**

See domain name system (DNS). From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNS (Domain Name System)**

Analogy: When calling somebody via the telephone, you can lookup their name in the phone book in order to find the telephone number. DNS is a similar directory service. When contacting a web site, your browser looks up the name in DNS in order to find the IP number. History: DNS is relatively new. When the Internet was small, every machine simply had a list of all other machines on the Internet (stored in /etc/hosts). Generally, people just had the IP addresses of machines memorized in much the same way that people memorize phone numbers today. Key point: DNS is not needed for communication. If a DNS server goes down, newbies will think that the entire network is down. Hackers frequently deal with raw IP addresses, and indeed often bypass DNS entirely as it may give off signs of an attack. Key point: The DNS hierarchy starts from the "top level domains" of .com, .net, .org, .edu, .giv, .mil, and the two-letter country codes (e.g. .us for United States, .jp for Japan). Misunderstanding: Both IP addresses and domain names use dots: "www.robertgraham.com" vs. "192.0.2.133". This has no significance; the usage of these dots is unrelated. Trying to match things up one-to-one is wrong (i.e. ".com" == "192."). Analogy: What is your phone number? If I asked you this, you could give me both your home number and your cell phone number. I can reach you at either one. In much the same way, the a domain name like http://www.yahoo.com/ can have multiple IP addresses. Every time you visit that site, you might go to a separate IP address. You can test this out yourself. Go to the command-line and type "ping www.yahoo.com". Notice how it comes back with an IP address that it pings. After that runs, try it again. Notice how the second time it is pinging a different IP address. Details: DNS provides a number of resource records (RR): A ^ The normal record that contain an name to IP address mapping. LOC ^ The geographic location containing latitude, longitude, altitude, and size. Altitude is meters above sea level. Size is the exponent in the in meters of the volumetric size of the object. Hackers sometimes use these records to find where you are located physically. Humor: The original name of this record was ICBM. HOST ^ HOST records can contain information about the machine, such as if it is a Windows or UNIX machine. Administrators probably should not fill them in; they are dangerous. PTR. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNS (Domain Name System)**

This system maps hostnames to IP numbers. DNS is the Domain Name System. DNS converts machine names to the IP addresses that all machines on the net have. It translates (or "maps" as the jargon would have it) from name to address and from address to name, and some other things. This HOWTO documents how to define such mappings using Unix system, with a few things specific to Linux. A mapping is simply an association between two things, in this case a machine name, like ftp.linux.org, and the machine's IP number (or address) 199.249.150.4. DNS also contains mappings the other way, from the IP number to the machine name; this is called a "reverse mapping". DNS is, to the uninitiated (you ;-), one of the more opaque areas of network administration. Fortunately DNS isn't really that hard. This HOWTO will try to make a few things clearer. It describes how to set up a simple DNS name server, starting with a caching only server and going on to setting up a primary DNS server for a domain. For more complex setups you can check the qanda section of this document. If it's not described there you will need to read the Real Documentation. I'll get back to what this Real Documentation consists of in the last chapter. Before you start on this you should configure your machine so that you can telnet in and out of it, and successfully make all kinds of connections to the net, and you should especially be able to do telnet 127.0.0.1 and get your own machine (test it now!). You also need good /etc/nsswitch.conf, /etc/resolv.conf and /etc/hosts files as a starting point, since I will not explain their function here. If you don't already have all this set up and working the Networking-HOWTO and/or the Networking-Overview-HOWTO explains how to set it up. Read them. When I say `your machine' I mean the machine you are trying to set up DNS on, not any other machine you might have that's involved in your networking effort. I assume you're not behind any kind of firewall that blocks name queries. If you are you will need a special configuration --- see the section on qanda. Name serving on Unix is done by a program called named. This is a part of the ``BIND'' package which is coordinated by The Internet Software Consortium. Named is included in most Linux distributions and is usually installed as /usr/sbin/named, usually from a package called BIND, in upper or lower case depending on the whim of the packager. If you have a named you can probably use it; if you don't have one you can get a binary off a Linux ftp site, or get the latest and greatest source from ftp://ftp.isc.org/isc/bind9/. This HOWTO is about BIND version 9. The old versions of the HOWTO, about BIND 4 and 8, is still available at http://langfeldt.net/DNS-HOWTO/ in case you use BIND 4 or 8 (incidentally, you will find this HOWTO there too). If the named man page talks about (at the very end, in the FILES section) named.conf you have BIND 8; if it talks about named.boot you have BIND 4. If you have 4 and are security conscious you really ought to upgrade to the latest version of BIND 8. Now. DNS is a net-wide database. Take care about what you put into it. If you put junk into it, you, and others, will get junk out of it. Keep your DNS tidy and consistent and you will get good service from it. Learn to use it, admin it, debug it and you will be another good admin keeping the net from falling to its knees by mismanagement. Tip: Make backup copies of all the files I instruct you to change if you already have them, so that if after going through this nothing works you can get it back to your old, working state. From DNS-HOWTO <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dns-browse**

Frontends to DNS search. This package provides two programs to make user lookups on DNS servers: dns_tree and dns_browse. dns_tree is a command-line-based front-end to dig. It replaces the several dig invocations necessary to fetch a zone, and it formats the output in a somewhat sensible hierarchical style (a tree). dns_browse is a GUI front-end to dns_tree. It allows point-and-click DNS browsing and makes it easy to expand/compress hierarchies in one or more DNS zones. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dns-helper**

Non-blocking name resolver interface. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnscvsutil**

Maintain DNS zone files under CVS control Maintain your DNS zone files under CVS control, and possibly automatically updating reverse zones. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnsdomainname**

show the system's DNS domain name From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnsmasq**

A caching DNS forwarder. Dnsmasq is lightweight, easy to configure DNS forwarder designed to provide DNS (domain name) services to a small network where using BIND would be overkill. It can be have its upstream DNS servers automatically configured by PPP or DHCP and it can serve the names of local machines which are not in the global DNS. It can integrate with the ISC DHCP daemon to serve the names of local machines which are configured using DHCP. Dnsmasq is ideal for networks behind NAT routers and connected via modem, ISDN, ADSL, or cable-modem. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNSO**

Defense Network Systems Organization (org., USA, mil.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNSO**

Domain Name Supporting Organization (org., ICANN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNSSEC**

A secure form of DNS. Its primary use is for updating DNS servers. TODO Algorithms: RSA, MD5. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnssec-keygen**

DNSSEC key generation tool From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnssec-makekeyset**

DNSSEC zone signing tool From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnssec-signkey**

DNSSEC key set signing tool From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnssec-signzone**

DNSSEC zone signing tool From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNSTAN**

Digitale NebenSTellenANlagen (Telekom), "DNStAn" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnstracer**

Trace DNS queries to the source dnstracer determines where a given Domain Name Server (DNS) gets its information from for a given hostname, and follows the chain of DNS servers back to the authoritative answer. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnsutils**

Clients provided with BIND This package delivers various client programs related to DNS that are derived from the BIND source tree. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dnswalk**

Checks dns zone information using nameserver lookups dnswalk is a DNS debugger. It performs zone transfers of specified domains, and checks the database in numerous ways for internal consistency, as well as accuracy. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNUG**

Deusche Notes User Group [e.v.] (org., user group, Lotus) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DNX**

Departmental Network eXchange [bridging router] (SNA, SDLC, Proteon) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DO**

Distributed Objects (NeXT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOAM**

Distributed Office Applications Model (ISO, IEC, DIS 10031-1 f.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**doc**

/dok/ n. Common spoken and written shorthand for `documentation'. Often used in the plural `docs' and in the construction `doc file' (i.e., documentation available on-line). From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOC**

De.Org.CCC (Usenet, CCC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**doc++**

A documentation system for C/C++, IDL and Java DOC++ is a documentation system for C/C++, IDL and Java generating both LaTeX output for high quality hardcopies and HTML output for sophisticated online browsing of your documentation. The documentation is extracted directly from the C/C++/IDL header/source files or Java class files. Here are a list of the highlights: - hierarchically structured documentation - automatic class graph generation (as Java applets for HTML) - cross references - high end formatting support including typesetting of equations For more information about DOC++ please take a look at it's home page at http://docpp.sourceforge.net/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**doc-base**

Utilities to manage online documentation This package contains utilities to manage online documentation on a Debian system. If you want to get additional information about doc-base please check out the `Debian doc-base Manual' included in this package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**doc-central**

web-based documentation browser Doc-Central is a tool to browse the documentation installed on your system using their doc-base entries. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**doc-debian**

Debian Project documentation, Debian FAQ and other documents The Debian Project is an association of individuals who have made common cause to create a free operating system. In this package, you will find: * Debian Linux Manifesto, * Constitution for the Debian Project, * Debian GNU/Linux Social Contract, * Debian Free Software Guidelines. Additionally provided are: * Debian GNU/Linux Frequently Asked Questions (FAQ), * Debian Bug Tracking System documentation, and * Introduction to the Debian mailing lists. All of these files are available at ftp://ftp.debian.org/debian/doc/ and mirrors thereof. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook**

SGML DTD for authors of technical documentation DocBook is an SGML vocabulary particularly well suited to books and papers about computer hardware and software (though it is by no means limited to these applications). It has emerged as an open, standard DTD in the software industry, and is used to document many free software projects. This package contains the SGML DTD for DocBook, which describes the formal structure of documents complying this format. If you wish to author XML documents, see the 'docbook-xml' package. It is a part of Debian's SGML/XML infrastructure, along with other DTDs, tools for parsing, validating, and styling, and formatting SGML and XML documents. This package includes the 2.4.1, 3.0, 3.1, 4.0, and 4.1 versions of the DocBook SGML DTD. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-dsssl**

Modular DocBook DSSSL stylesheets, for print and HTML This package enables the use of DSSSL styling (formatting for output) with DocBook SGML or XML files. This package contains two DocBook DSSSL stylesheets, one for "print" output and one for HTML. The print stylesheet can be used in conjunction with the RTF and the TeX back-ends that Jade provides to produce output suitable for printing. The HTML stylesheet can be used to convert DocBook documents into HTML. The stylesheets are modular in design so that you can extend and customize them. Author: Norman Walsh <ndw@nwalsh.com> Homepage: http://docbook.sourceforge.net/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-dtds**

The DocBook Document Type Definition (DTD) describes the syntax oftechnical documentation texts (articles, books and manual pages). This syntax is XML-compliant and is developed by the OASIS consortium. This package contains SGML and XML versions of the DocBook DTD up toand including version 4.1.2. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-style-dsssl**

This package contains DSSSL stylesheets for converting any DocBook document to another printed (for example, RTF or PostScript) or online (for example, HTML) format. These stylesheets are highly customizable. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-style-xsl**

These XSL stylesheets allow you to transform any DocBook XML document to other formats, such as HTML, FO, and XHTML. They are highly customizable. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-to-man**

Converter from DocBook SGML into roff -man macros. The docbook-to-man tool is a batch converter that transforms UNIX-style manpages from the DocBook SGML DTD into nroff/troff -man macros. This is not the original version by Fred Dalrymple, but one with the ANS modifications by David Bolen. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-utils**

Convert Docbook files to other formats (HTML, RTF, Postscript, PDF) The docbook-utils is a set of a few small programs intended to ease everyday use of technical documentation software and more generally use of SGML and XML. Tasks they currently accomplish are: * jw: convert Docbook files to other formats (HTML, RTF, Postscript, PDF). * sgmldiff: detect the differences in markup between two SGML files. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-utils**

This package contains scripts are for easy conversion from DocBookfiles to other formats (for example, HTML, RTF, and PostScript), andfor comparing SGML files. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-utils-pdf**

This package contains a script for converting DocBook documents to PDF format. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-website**

XML Website DTD and XSL Stylesheets A docbook-derived XML DTD for building web sites. This package includes the xsl stylesheets for this DTD. This version is a customization of the DocBook XML V4.1.2 DTD. Author: Norman Walsh <ndw@nwalsh.com> Homepage: http://sourceforge.net/projects/docbook/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-xml**

XML DTD for DocBook, also known as DocBk XML An XML representation of the DocBook DTD, which is sometimes referred to as DocBk XML. This is a DTD widely used for documenting software and other technical topics. This package ships with the newest DocBook XML DTD, as well as a select set of legacy DTDs for use with older documents. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-xsl**

Stylesheets for processing DocBook XML files to HTML and FO. These are modular XSL stylesheets for processing documents composed with the DocBook XML DTD and its derivatives ("Simplified" DocBook XML, JRefEntry DTD, etc.). The documentation is included in the package. The stylesheets provide XSLT transformations for both HTML and Formatting Object output. The latter can be further processed to a number of print formats using FOP or TeX-based tools. The stylesheets are modular in the sense that you can extend and, to some extent, customize them. Included are extension classes for the Saxon and Xalan2 XSLT processors. The documentation is included in this package. For quickstart instructions, see /usr/share/doc/docbook-xsl/README.Debian Author: Norman Walsh <ndw@nwalsh.com> Homepage: http://sourceforge.net/projects/docbook From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook-xsl-stylesheets**

Stylesheets for processing DocBook XML files to HTML and FO. These are modular XSL stylesheets for processing documents composed with the DocBook XML DTD and its derivatives ("Simplified" DocBook XML, JRefEntry DTD, etc.). The documentation is included in the package. The stylesheets provide XSLT transformations for both HTML and Formatting Object output. The latter can be further processed to a number of print formats using FOP or TeX-based tools. The stylesheets are modular in the sense that you can extend and, to some extent, customize them. The documentation is included in this package. Author: Norman Walsh <ndw@nwalsh.com> Homepage: http://sourceforge.net/projects/docbook From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2dvi**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2html**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2man**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2pdf**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2ps**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2rtf**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2tex**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2texi**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docbook2txt**

(Jade Wrapper) converts SGML files to other formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOCC**

DISA Operations Control Complex (DISA, mil., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**docdiff**

Compares two text files by character or by word/morpheme Compares two text files by character or by word/morpheme, and output the result in pseudo HTML format. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOCSIS**

Data Over Cable System Interface Specification From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**documentation**

n. The multiple kilograms of macerated, pounded, steamed, bleached, and pressed trees that accompany most modern software or hardware products (see also tree-killer). Hackers seldom read paper documentation and (too) often resist writing it; they prefer theirs to be terse and on-line. A common comment on this predilection is "You can't grep dead trees". See drool-proof paper, verbiage, treeware. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Documentation**

The instructions, tutorials, and reference information that provides you with the information you need to use a program or computer system effectively. Documentation can appear in printed form or in on-line help systems. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DODISS**

Department Of Defense Index of Specifications and Standards (mil., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOE**

Depends On Experience From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOE**

Distributed Objects Everywhere (Sun) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**dog**

Enhanced replacement for cat dog writes the contents of each given file, URL or standard input to standard output. It currently supports file, http and raw URLs. It is designed as a compatible, but enhanced replacement for cat. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOM**

Disk On Module From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOM**

Document Object Model (MS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**DOM (Document Object Model)**

An application programming interface (API) for HTML and XML documents. It defines the logical structure of documents and the way a document is accessed and manipulated. In the DOM specification, the term "document" is used in the broad sense - increasingly, XML is being used as a way of representing many different kinds of information that may be stored in diverse systems, and much of this would traditionally be seen as data rather than as documents. Nevertheless, XML presents this data as documents, and the DOM may be used to manage this data. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
