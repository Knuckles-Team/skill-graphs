A short compilation later, PCI probing was working! We got some beer and
partied ;-)
-----------------------------------------------------------------------------

4.3. Ethernet: our first PCI device

Our board uses an Intel ethernet chip, called i82559er, which has a module
called eepro100. After compiling the module and booting, we discovered that
the module isn't working, although an ethernet device was found. We guessed
that it was an irq problem, and that the devices don't get the IRQs they
need. We modified a function called pmppc_map_irq() to map our ethernet
devices:
XXXX_map_irq(struct pci_dev *dev, unsigned char idsel, unsigned char pin) {
        static char pci_irq_table[][4] =
        /*
         *      PCI IDSEL/INTPIN->INTLINE
         *      A       B       C       D
         */
        {
                {22,    0,      0,      0},/* IDSEL 3 - Ethernet */
                {0,     0,      0,      0},/* IDSEL 4 - unused   */
                {0,     0,      0,      0},/* IDSEL 5 - unused   */
                {0,     0,      0,      0},/* IDSEL 6 - ????     */
                {0,     0,      0,      0},/* IDSEL 7 - unused   */
                {0,     0,      0,      0},/* IDSEL 8 - unused   */
                {0,     0,      0,      0},/* IDSEL 9 - unused   */
        };

        const long min_idsel = 3, max_idsel = 9, irqs_per_slot = 4;
        return PCI_IRQ_TABLE_LOOKUP;
}
The function maps IRQs according to IDselects, which means in the order on
the PCI bus by which the devices are set. This structure is a bit tricky:
min_idsel denotes the topleft corner of the array, and max_idsel is the
bottomleft corner. irqs_per_slot is the number of IRQs per line. The
structure is as follows:
each cell contains (IDSEL, SLOT#, IRQ)
                +----------------------------------------+
                | (3,0,22) | (3,1,0) | (3,2,0) | (3,3,0) |
                +----------------------------------------+
                | (4,0,0)  | (4,1,0) | (4,2,0) | (4,3,0) |
                +----------------------------------------+
                                                        ..........
                                                        ..........
                +----------------------------------------+
                | (9,0,0)  | (9,1,0) | (9,2,0) | (9,3,0) |
                +----------------------------------------+
As you can see, our i8559er needs IRQ 22, and is seated in IDselect 3. Of
course, we didn't know that at the start, so we wrote a small piece of code
that read all the vendor IDs in all the IDselects. Once done we compiled, but
the ethernet device still didn't work.

The next problem was that the module couldn't decide on a MAC address for the
device. The MAC address should be written on an EEPROM chip (connected to the
device), but we discovered that the hardware guys decided that i82559 doesn't
need the EEPROM, so they removed it. After hardcoding a MAC address inside
eepro100.c, the ethernet device finally worked. The final solution was to
make the module read the MAC address from NVRAM memory, and if no other
choice was available, to fall back to a default MAC address.

Note The next step was to mount a NFS root filesystem. For details see the
     documentation in Documentation/nfsroot.txt
-----------------------------------------------------------------------------

4.4. Some Miscellaneous Issues

We had new problems, some would say good problems. We didn't have a
bootloader yet, however we needed to pass a command line to the kernel at
boot time. We hard-coded the command line into the kernel inside the
parse_options(). After that was finished, we made console_init() and
serial_console_setup() work the way they should. They no longer ignored the
command line, but still RTS and DTR stay low.

Another important issue was memory mapping. The file arch/ppc/mm/init.c
contains a function called MMU_init(). This function is actually a big switch
statement, divided by the machine type. Each machine maps its memory using the
setbat() and ioremap() functions. The BAT mechanism is a way of translating
virtual addresses into physical ones. Thus, setbat() is used by specifying a
virtual address, a physical address and a page size. Not every size can be
used here; you should use one of the finite set of sizes, ranging from 128KB
to 256MB. We mapped our IO memory so that virtual equalled physical.

As mentioned, there is another way of mapping memory - ioremap(). ioremap()
is used to map physical addresses into virtual ones, making them available to
the kernel. The function does not allocate any memory, simply returns a
virtual address by which one can access the memory region. The following is a
snippet from MMU_init():
case _MACH_mymachine:
        setbat(0, LOW_IO_VIRT_BASE, LOW_IO_PHYS_BASE, LOW_IO_SIZE, IO_PAGE);
        ioremap(UNIVERSE_BASE,UNIVERSE_SIZE);      /* Universe VME */
        ioremap(EEPRO100_BASE,EEPRO100_SIZE);      /* Ethernet EEPRO100 */
        break;
As you can see, we don't take the return value of ioremap(). We don't need
it, since at this stage the kernel maps the addresses so that virtual address
== physical address.
-----------------------------------------------------------------------------

Chapter 5. Linux Is Booting ... What Now ?

5.1. The 64 bit barrier

The CPC700 has a "feature" which is supposed to make some memory access use
64 bit wide. This is a problem since some test-and-set registers on our board
might get set unintentionally, because we were trying to read something 16
bits lower. In order to solve this situation, we set the memory controller to
64 bit wide intervals. If you try to access those areas in another manner (8
or 16 bit access), the CPC700 simply throws them away. We had to be able to
read/write those areas, since important "discretes" (controlled by an Altera
device) were mapped there.

In order to access those areas, we needed a function that does a 64 bit
write. As far as I know, doing a 64 bit write on a PowerPC is possible in two
ways: using cache lines and using a floating point register. The floating
point register is a 64 bit sized register, so when we write it, the whole 64
bit get written. The problem is that you can't do floating point in the
kernel. Since the kernel doesn't save the floating point registers during
context switch, it doesn't allow FP, and will throw an exception if done in
the kernel.

After messing with cache lines, we decided to go the FP way, and added the
following function:
void out64(__u32 addr, long long *pVal) {
        __u32 flags, tmp_msr;

        save_flags(flags);
        cli();
        tmp_msr = __get_MSR();
        tmp_msr |= MSR_FP;
        tmp_msr &= ~(MSR_FE0 | MSR_FE1);
        __put_MSR(tmp_msr);

        sysOut64(addr, pVal);
        __put_MSR(flags & ~(MSR_EE));
        restore_flags(flags);
}
The function adds a floating point to the PowerPC MSR register, and makes
sure that no exceptions will be generated as a result of doing FP. Once done,
it uses an assembly code, described below in the sysOut64() to do the actual
floating-point operation. Note that the function turns off interrupts, but
this is acceptable here, since we use the function on rare occasion.
_GLOBAL(sysOut64)
stwu    r1, -DEPTH(r1)
mflr    r0
stw     r31, FP_LOC(r1)
stw     r0,  LR_LOC(r1)
mr              r31, r1
stfd    fr0, FPR_SAVE(r31)      /* save floating point reg contents */

lfd     fr0,0(r4)
stfd  fr0,0(r3)
eieio

lfd     fr0, FPR_SAVE(r31)      /* restore floating point value */
lwz     r4, 0(r1)               /* now restore the stack frame  */
lwz     r0, 4(r4)
mtlr    r0
lwz     r31, -4(r4)
mr      r1, r4
blr
-----------------------------------------------------------------------------

5.2. Booting from flash

While Linux was booting using an NFS filesystem, this was not enough. For an
actual field product, we needed Linux to boot from an independent device,
without the need for a network at all. We decided to create a special kind of
image, called initrd, which is basically a Linux kernel with a compressed
file. The compressed file includes a Linux filesystem. The filesystem is
unpacked to a ramdisk on boot, and mounted as the root filesystem.

During the boot process, the bootloader relocated the kernel image to address
zero - which was fine, and the initrd part to a higher address. The area to
which initrd was relocated was not mapped in our kernel's memory, and all we
got was a kernel error (access to bad area). After modifying the bootloader
to relocate initrd to a different address, all was fine and Linux booted
successfully.

Tip If your board has some NVRAM memory, it would be a good idea to use it
    for bootloader purposes. After writing a module for our NVRAM memory (out
    of scope for this paper), we modified the bootloader, so that the kernel
    command-line, and MAC address were saved in NVRAM. When the bootloader
    starts, it checks NVRAM and if it is initialized (by a certain magic
    number), the bootloader uses the command line written there. Otherwise,
    the bootloader reverts to a default command line, allowing the user to
    edit it.
-----------------------------------------------------------------------------

Appendix A. GNU Free Documentation License

Version 1.1, March 2000


    Copyright (C) 2000 Free Software Foundation, Inc. 59 Temple Place, Suite
    330, Boston, MA 02111-1307 USA Everyone is permitted to copy and
    distribute verbatim copies of this license document, but changing it is
    not allowed.

-----------------------------------------------------------------------------
A.1. PREAMBLE

The purpose of this License is to make a manual, textbook, or other written
document "free" in the sense of freedom: to assure everyone the effective
freedom to copy and redistribute it, with or without modifying it, either
commercially or noncommercially. Secondarily, this License preserves for the
author and publisher a way to get credit for their work, while not being
considered responsible for modifications made by others.

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

This License applies to any manual or other work that contains a notice
placed by the copyright holder saying it can be distributed under the terms
of this License. The "Document", below, refers to any such manual or work.
Any member of the public is a licensee, and is addressed as "you".

A "Modified Version" of the Document means any work containing the Document
or a portion of it, either copied verbatim, or with modifications and/or
translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of the
Document that deals exclusively with the relationship of the publishers or
authors of the Document to the Document's overall subject (or to related
matters) and contains nothing that could fall directly within that overall
subject. (For example, if the Document is in part a textbook of mathematics,
a Secondary Section may not explain any mathematics.) The relationship could
be a matter of historical connection with the subject or with related
matters, or of legal, commercial, philosophical, ethical or political
position regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are
designated, as being those of Invariant Sections, in the notice that says
that the Document is released under this License.

The "Cover Texts" are certain short passages of text that are listed, as
Front-Cover Texts or Back-Cover Texts, in the notice that says that the
Document is released under this License.

A "Transparent" copy of the Document means a machine-readable copy,
represented in a format whose specification is available to the general
public, whose contents can be viewed and edited directly and
straightforwardly with generic text editors or (for images composed of
pixels) generic paint programs or (for drawings) some widely available
drawing editor, and that is suitable for input to text formatters or for
automatic translation to a variety of formats suitable for input to text
formatters. A copy made in an otherwise Transparent file format whose markup
has been designed to thwart or discourage subsequent modification by readers
is not Transparent. A copy that is not "Transparent" is called "Opaque".

Examples of suitable formats for Transparent copies include plain ASCII
without markup, Texinfo input format, LaTeX input format, SGML or XML using a
publicly available DTD, and standard-conforming simple HTML designed for
human modification. Opaque formats include PostScript, PDF, proprietary
formats that can be read and edited only by proprietary word processors, SGML
or XML for which the DTD and/or processing tools are not generally available,
and the machine-generated HTML produced by some word processors for output
purposes only.

The "Title Page" means, for a printed book, the title page itself, plus such
following pages as are needed to hold, legibly, the material this License
requires to appear in the title page. For works in formats which do not have
any title page as such, "Title Page" means the text near the most prominent
appearance of the work's title, preceding the beginning of the body of the
text.
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

If you publish printed copies of the Document numbering more than 100, and
the Document's license notice requires Cover Texts, you must enclose the
copies in covers that carry, clearly and legibly, all these Cover Texts:
Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover.
Both covers must also clearly and legibly identify you as the publisher of
these copies. The front cover must present the full title with all words of
the title equally prominent and visible. You may add other material on the
covers in addition. Copying with changes limited to the covers, as long as
they preserve the title of the Document and satisfy these conditions, can be
treated as verbatim copying in other respects.

If the required texts for either cover are too voluminous to fit legibly, you
should put the first ones listed (as many as fit reasonably) on the actual
cover, and continue the rest onto adjacent pages.

If you publish or distribute Opaque copies of the Document numbering more
than 100, you must either include a machine-readable Transparent copy along
with each Opaque copy, or state in or with each Opaque copy a
publicly-accessible computer-network location containing a complete
Transparent copy of the Document, free of added material, which the general
network-using public has access to download anonymously at no charge using
public-standard network protocols. If you use the latter option, you must
take reasonably prudent steps, when you begin distribution of Opaque copies
in quantity, to ensure that this Transparent copy will remain thus accessible
at the stated location until at least one year after the last time you
distribute an Opaque copy (directly or through your agents or retailers) of
that edition to the public.

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
    of its principal authors, if it has less than five).

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

 I. Preserve the section entitled "History", and its title, and add to it an
    item stating at least the title, year, new authors, and publisher of the
    Modified Version as given on the Title Page. If there is no section
    entitled "History" in the Document, create one stating the title, year,
    authors, and publisher of the Document as given on its Title Page, then
    add an item describing the Modified Version as stated in the previous
    sentence.

 J. Preserve the network location, if any, given in the Document for public
    access to a Transparent copy of the Document, and likewise the network
    locations given in the Document for previous versions it was based on.
    These may be placed in the "History" section. You may omit a network
    location for a work that was published at least four years before the
    Document itself, or if the original publisher of the version it refers to
    gives permission.

 K. In any section entitled "Acknowledgements" or "Dedications", preserve the
    section's title, and preserve in the section all the substance and tone
    of each of the contributor acknowledgements and/or dedications given
    therein.

 L. Preserve all the Invariant Sections of the Document, unaltered in their
    text and in their titles. Section numbers or the equivalent are not
    considered part of the section titles.

 M. Delete any section entitled "Endorsements". Such a section may not be
    included in the Modified Version.

 N. Do not retitle any existing section as "Endorsements" or to conflict in
    title with any Invariant Section.


If the Modified Version includes new front-matter sections or appendices that
qualify as Secondary Sections and contain no material copied from the
Document, you may at your option designate some or all of these sections as
invariant. To do this, add their titles to the list of Invariant Sections in
the Modified Version's license notice. These titles must be distinct from any
other section titles.

You may add a section entitled "Endorsements", provided it contains nothing
but endorsements of your Modified Version by various parties--for example,
statements of peer review or that the text has been approved by an
organization as the authoritative definition of a standard.

You may add a passage of up to five words as a Front-Cover Text, and a
passage of up to 25 words as a Back-Cover Text, to the end of the list of
Cover Texts in the Modified Version. Only one passage of Front-Cover Text and
one of Back-Cover Text may be added by (or through arrangements made by) any
one entity. If the Document already includes a cover text for the same cover,
previously added by you or by arrangement made by the same entity you are
acting on behalf of, you may not add another; but you may replace the old
one, on explicit permission from the previous publisher that added the old
one.

The author(s) and publisher(s) of the Document do not by this License give
permission to use their names for publicity for or to assert or imply
endorsement of any Modified Version.
-----------------------------------------------------------------------------

A.6. COMBINING DOCUMENTS

You may combine the Document with other documents released under this
License, under the terms defined in section 4 above for modified versions,
provided that you include in the combination all of the Invariant Sections of
all of the original documents, unmodified, and list them all as Invariant
Sections of your combined work in its license notice.

The combined work need only contain one copy of this License, and multiple
identical Invariant Sections may be replaced with a single copy. If there are
multiple Invariant Sections with the same name but different contents, make
the title of each such section unique by adding at the end of it, in
parentheses, the name of the original author or publisher of that section if
known, or else a unique number. Make the same adjustment to the section
