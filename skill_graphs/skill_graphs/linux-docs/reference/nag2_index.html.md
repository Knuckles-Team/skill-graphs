# Linux Network Administrators Guide
* * *

**Table of Contents**


[Preface](https://tldp.org/LDP/nag2/f3.html)


1. [Purpose and Audience for This Book](https://tldp.org/LDP/nag2/x12.html)


2. [Sources of Information](https://tldp.org/LDP/nag2/x16.html)


3. [File System Standards](https://tldp.org/LDP/nag2/x394.html)


4. [Standard Linux Base](https://tldp.org/LDP/nag2/x410.html)


5. [About This Book](https://tldp.org/LDP/nag2/x425.html)


6. [The Official Printed Version](https://tldp.org/LDP/nag2/x453.html)


7. [Overview](https://tldp.org/LDP/nag2/x-087-2-intro.outlook.html)


8. [Conventions Used in This Book](https://tldp.org/LDP/nag2/x523.html)


9. [Submitting Changes](https://tldp.org/LDP/nag2/x-087-2-submitchanges.html)


10. [Acknowledgments](https://tldp.org/LDP/nag2/x575.html)


1. [Introduction to Networking](https://tldp.org/LDP/nag2/x-087-2-intro.html)


1.1. [History](https://tldp.org/LDP/nag2/x-087-2-intro.history.html)


1.2. [TCP/IP Networks](https://tldp.org/LDP/nag2/x-087-2-intro.tcpip.html)


1.3. [UUCP Networks](https://tldp.org/LDP/nag2/x-087-2-intro.uucp.html)


1.4. [Linux Networking](https://tldp.org/LDP/nag2/x1312.html)


1.5. [Maintaining Your System](https://tldp.org/LDP/nag2/x1392.html)


2. [Issues of TCP/IP Networking](https://tldp.org/LDP/nag2/x-087-2-issues.html)


2.1. [Networking Interfaces](https://tldp.org/LDP/nag2/x-087-2-issues.interfaces.html)


2.2. [IP Addresses](https://tldp.org/LDP/nag2/x-087-2-issues.ip-addresses.html)


2.3. [Address Resolution](https://tldp.org/LDP/nag2/x-087-2-issues.arp.html)


2.4. [IP Routing](https://tldp.org/LDP/nag2/x-087-2-issues.routing.html)


2.5. [The Internet Control Message Protocol](https://tldp.org/LDP/nag2/x-087-2-issues.icmp.html)


2.6. [Resolving Host Names](https://tldp.org/LDP/nag2/x-087-2-issues.resolving.html)


3. [Configuringthe NetworkingHardware](https://tldp.org/LDP/nag2/x-087-2-hardware.html)


3.1. [Kernel Configuration](https://tldp.org/LDP/nag2/x-087-2-hardware.kernel.config.html)


3.2. [A Tour of Linux Network Devices](https://tldp.org/LDP/nag2/x-087-2-hwconfig.tour.html)


3.3. [Ethernet Installation](https://tldp.org/LDP/nag2/x-087-2-hardware.drivers.ethernet.html)


3.4. [The PLIP Driver](https://tldp.org/LDP/nag2/x-087-2-hardware.drivers.plip.html)


3.5. [The PPP and SLIP Drivers](https://tldp.org/LDP/nag2/x-087-2-hardware.drivers.slip.html)


3.6. [Other Network Types](https://tldp.org/LDP/nag2/x-087-2-hardware.other.html)


4. [Configuring the Serial Hardware](https://tldp.org/LDP/nag2/x-087-2-serial.html)


4.1. [Communications Software for Modem Links](https://tldp.org/LDP/nag2/x-087-2-serial.software.html)


4.2. [Introduction to Serial Devices](https://tldp.org/LDP/nag2/x-087-2-serial.ttys.html)


4.3. [Accessing Serial Devices](https://tldp.org/LDP/nag2/x-087-2-serial.devices.html)


4.4. [Serial Hardware](https://tldp.org/LDP/nag2/x-087-2-serial.hardware.html)


4.5. [Using the Configuration Utilities](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html)


4.6. [Serial Devices and the login: Prompt](https://tldp.org/LDP/nag2/x-087-2-serial.getty.html)


5. [Configuring TCP/IP Networking](https://tldp.org/LDP/nag2/x-087-2-iface.html)


5.1. [Mounting the /proc Filesystem](https://tldp.org/LDP/nag2/x-087-2-iface.procfs.html)


5.2. [Installing the Binaries](https://tldp.org/LDP/nag2/x-087-2-iface.binaries.html)


5.3. [Setting the Hostname](https://tldp.org/LDP/nag2/x-087-2-iface.hostname.html)


5.4. [Assigning IP Addresses](https://tldp.org/LDP/nag2/x-087-2-iface.addresses.html)


5.5. [Creating Subnets](https://tldp.org/LDP/nag2/x-087-2-create.subnets.html)


5.6. [Writing hosts and networks Files](https://tldp.org/LDP/nag2/x-087-2-iface.simple-resolv.html)


5.7. [Interface Configuration for IP](https://tldp.org/LDP/nag2/x-087-2-iface.interface.html)


5.8. [All About ifconfig](https://tldp.org/LDP/nag2/x-087-2-iface.ifconfig.html)


5.9. [The netstat Command](https://tldp.org/LDP/nag2/x-087-2-iface.netstat.html)


5.10. [Checking the ARP Tables](https://tldp.org/LDP/nag2/x-087-2-iface.verify.arp.html)


6. [Name Service and Resolver Configuration](https://tldp.org/LDP/nag2/x-087-2-resolv.html)


6.1. [The Resolver Library](https://tldp.org/LDP/nag2/x-087-2-resolv.library.html)


6.2. [How DNS Works](https://tldp.org/LDP/nag2/x-087-2-resolv.howdnsworks.html)


6.3. [Running named](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html)


7. [Serial Line IP](https://tldp.org/LDP/nag2/x-087-2-slip.html)


7.1. [General Requirements](https://tldp.org/LDP/nag2/x-087-2-slip.general.html)


7.2. [SLIP Operation](https://tldp.org/LDP/nag2/x-087-2-slip.operation.html)


7.3. [Dealing with Private IP Networks](https://tldp.org/LDP/nag2/x6009.html)


7.4. [Using dip](https://tldp.org/LDP/nag2/x-087-2-slip.dip.html)


7.5. [Running in Server Mode](https://tldp.org/LDP/nag2/x-087-2-slip.server.html)


8. [The Point-to-Point Protocol](https://tldp.org/LDP/nag2/x-087-2-ppp.html)


8.1. [PPP on Linux](https://tldp.org/LDP/nag2/x6507.html)


8.2. [Running pppd](https://tldp.org/LDP/nag2/x6560.html)


8.3. [Using Options Files](https://tldp.org/LDP/nag2/x-087-2-ppp.options.html)


8.4. [Using chat to Automate Dialing](https://tldp.org/LDP/nag2/x6675.html)


8.5. [IP Configuration Options](https://tldp.org/LDP/nag2/x-087-2-ipconfig.options.html)


8.6. [Link Control Options](https://tldp.org/LDP/nag2/x6968.html)


8.7. [General Security Considerations](https://tldp.org/LDP/nag2/x7037.html)


8.8. [Authentication with PPP](https://tldp.org/LDP/nag2/x-087-2-ppp.authentication.html)


8.9. [Debugging Your PPP Setup](https://tldp.org/LDP/nag2/x7261.html)


8.10. [More Advanced PPP Configurations](https://tldp.org/LDP/nag2/x7297.html)


9. [TCP/IP Firewall](https://tldp.org/LDP/nag2/x-087-2-firewall.html)


9.1. [Methods of Attack](https://tldp.org/LDP/nag2/x-082-2-firewall.attacks.html)


9.2. [What Is a Firewall?](https://tldp.org/LDP/nag2/x-087-2-firewall.introduction.html)


9.3. [What Is IP Filtering?](https://tldp.org/LDP/nag2/x-087-2-firewall.filtering.html)


9.4. [Setting Up Linux for Firewalling](https://tldp.org/LDP/nag2/x-087-2-firewall.howto.html)


9.5. [Three Ways We Can Do Filtering](https://tldp.org/LDP/nag2/x-087-2-firewall.filteringmethods.html)


9.6. [Original IP Firewall (2.0 Kernels)](https://tldp.org/LDP/nag2/x-087-2-firewall.original.html)


9.7. [IP Firewall Chains (2.2 Kernels)](https://tldp.org/LDP/nag2/x-087-2-firewall.fwchains.html)


9.8. [Netfilter and IP Tables (2.4 Kernels)](https://tldp.org/LDP/nag2/x-087-2-firewall.future.html)


9.9. [TOS Bit Manipulation](https://tldp.org/LDP/nag2/x-087-2-firewall.tos.manipulation.html)


9.10. [Testing a Firewall Configuration](https://tldp.org/LDP/nag2/x-087-2-firewall.checkingconf.html)


9.11. [A Sample Firewall Configuration](https://tldp.org/LDP/nag2/x-087-2-firewall.example.html)


10. [IP Accounting](https://tldp.org/LDP/nag2/x-087-2-accounting.html)


10.1. [Configuring the Kernel for IP Accounting](https://tldp.org/LDP/nag2/x-087-2-accounting.kernel.config.html)


10.2. [Configuring IP Accounting](https://tldp.org/LDP/nag2/x-087-2-accounting.ipfwadm.html)


10.3. [Using IP Accounting Results](https://tldp.org/LDP/nag2/x-087-2-accounting.viewing.results.html)


10.4. [Resetting the Counters](https://tldp.org/LDP/nag2/x-087-2-accounting.zeroing.counter.html)


10.5. [Flushing the Ruleset](https://tldp.org/LDP/nag2/x-087-2-accounting.flushing.rules.html)


10.6. [Passive Collection of Accounting Data](https://tldp.org/LDP/nag2/x-087-2-accounting.passive.collection.html)


11. [IP Masquerade and Network Address Translation](https://tldp.org/LDP/nag2/x-087-2-ipmasq.html)


11.1. [Side Effects and Fringe Benefits](https://tldp.org/LDP/nag2/x-087-2-masq.side.effects.html)


11.2. [Configuring the Kernel for IP Masquerade](https://tldp.org/LDP/nag2/x-087-2-masq.kernel.config.html)


11.3. [Configuring IP Masquerade](https://tldp.org/LDP/nag2/x-087-2-masq.configuration.html)


11.4. [Handling Name Server Lookups](https://tldp.org/LDP/nag2/x-087-2-masq.namelookups.html)


11.5. [More About Network Address Translation](https://tldp.org/LDP/nag2/x9803.html)


12. [ImportantNetwork Features](https://tldp.org/LDP/nag2/x-087-2-appl.html)


12.1. [The inetd Super Server](https://tldp.org/LDP/nag2/x-087-2-appl.inetd.html)


12.2. [The tcpd Access Control Facility](https://tldp.org/LDP/nag2/x-087-2-appl.tcpd.html)


12.3. [The Services and Protocols Files](https://tldp.org/LDP/nag2/x-087-2-appl.services.html)


12.4. [Remote Procedure Call](https://tldp.org/LDP/nag2/x-087-2-appl.rpc.html)


12.5. [Configuring Remote Loginand Execution](https://tldp.org/LDP/nag2/x-087-2-appl.remote.html)


13. [The Network Information System](https://tldp.org/LDP/nag2/x-087-2-nis.html)


13.1. [Getting Acquainted with NIS](https://tldp.org/LDP/nag2/x10579.html)


13.2. [NIS Versus NIS+](https://tldp.org/LDP/nag2/x-087-2-nis.nisplus.html)


13.3. [The Client Side of NIS](https://tldp.org/LDP/nag2/x-087-2-nis.clients.html)


13.4. [Running an NIS Server](https://tldp.org/LDP/nag2/x-087-2-nis.server.html)


13.5. [NIS Server Security](https://tldp.org/LDP/nag2/x-087-2-nis.securenets.html)


13.6. [Setting Up an NIS Client with GNU libc](https://tldp.org/LDP/nag2/x-087-2-nis.yp.html)


13.7. [Choosing the Right Maps](https://tldp.org/LDP/nag2/x-087-2-nis.nsswitch.html)


13.8. [Using the passwd and group Maps](https://tldp.org/LDP/nag2/x-087-2-nis.passwd.html)


13.9. [Using NIS with Shadow Support](https://tldp.org/LDP/nag2/x-087-2-nis.shadow.html)


14. [The NetworkFile System](https://tldp.org/LDP/nag2/x-087-2-nfs.html)


14.1. [Preparing NFS](https://tldp.org/LDP/nag2/x-087-2-nfs.nfsd.html)


14.2. [Mounting an NFS Volume](https://tldp.org/LDP/nag2/x-087-2-nfs.mountd.html)


14.3. [The NFS Daemons](https://tldp.org/LDP/nag2/x-087-2-nfs.daemons.html)


14.4. [The exports File](https://tldp.org/LDP/nag2/x-087-2-nfs.exports.html)


14.5. [Kernel-Based NFSv2 Server Support](https://tldp.org/LDP/nag2/x-087-2-nfs.kernelv2.html)


14.6. [Kernel-Based NFSv3 Server Support](https://tldp.org/LDP/nag2/x-087-2-nfs.kernelv3.html)


15. [IPX and the NCP Filesystem](https://tldp.org/LDP/nag2/x-087-2-ipx.html)


15.1. [Xerox, Novell, and History](https://tldp.org/LDP/nag2/x11684.html)


15.2. [IPX and Linux](https://tldp.org/LDP/nag2/x11757.html)


15.3. [Configuring the Kernel for IPXand NCPFS](https://tldp.org/LDP/nag2/x-087-2-ipx.kernel.html)


15.4. [Configuring IPX Interfaces](https://tldp.org/LDP/nag2/x-087-2-ipx.interfaces.html)


15.5. [Configuring an IPX Router](https://tldp.org/LDP/nag2/x-087-2-ipx.router.html)


15.6. [Mounting a Remote NetWare Volume](https://tldp.org/LDP/nag2/x-087-2-ipx.ncpfs.client.html)


15.7. [Exploring Some of the Other IPX Tools](https://tldp.org/LDP/nag2/x-087-2-ipx.othertools.html)


15.8. [Printing to a NetWare Print Queue](https://tldp.org/LDP/nag2/x-087-2-ipx.ncpfs.printing.html)


15.9. [NetWare Server Emulation](https://tldp.org/LDP/nag2/x-087-2-ipx.ncpfs.server.html)


16. [ManagingTaylor UUCP](https://tldp.org/LDP/nag2/x-087-2-uucp.html)


16.1. [UUCP Transfers and Remote Execution](https://tldp.org/LDP/nag2/x-087-2-uucp.intro.grades.html)


16.2. [UUCP Configuration Files](https://tldp.org/LDP/nag2/x-087-2-uucp.config.files.html)


16.3. [Controlling Access to UUCP Features](https://tldp.org/LDP/nag2/x-087-2-uucp.permissions.html)


16.4. [Setting Up Your System for Dialing In](https://tldp.org/LDP/nag2/x-087-2-uucp.dialin.html)


16.5. [UUCP Low-Level Protocols](https://tldp.org/LDP/nag2/x-087-2-uucp.protocols.html)


16.6. [Troubleshooting](https://tldp.org/LDP/nag2/x-087-2-uucp.misc.faq.html)


16.7. [Log Files and Debugging](https://tldp.org/LDP/nag2/x13819.html)


17. [Electronic Mail](https://tldp.org/LDP/nag2/x-087-2-mail.html)


17.1. [What Is a Mail Message?](https://tldp.org/LDP/nag2/x-087-2-mail.message-format.html)


17.2. [How Is Mail Delivered?](https://tldp.org/LDP/nag2/x-087-2-mail.delivery.html)


17.3. [Email Addresses](https://tldp.org/LDP/nag2/x-087-2-mail.address.html)


17.4. [How Does Mail Routing Work?](https://tldp.org/LDP/nag2/x-087-2-mail.routing.html)


17.5. [Configuring elm](https://tldp.org/LDP/nag2/x-087-2-mail.elm.html)


18. [Sendmail](https://tldp.org/LDP/nag2/x-087-2-sendmail.html)


18.1. [Introduction to sendmail](https://tldp.org/LDP/nag2/x14586.html)


18.2. [Installing sendmail](https://tldp.org/LDP/nag2/x14607.html)


18.3. [Overview of Configuration Files](https://tldp.org/LDP/nag2/x14644.html)


18.4. [The sendmail.cf and sendmail.mc Files](https://tldp.org/LDP/nag2/x14661.html)


18.5. [Generating the sendmail.cf File](https://tldp.org/LDP/nag2/x14903.html)


18.6. [Interpreting and Writing Rewrite Rules](https://tldp.org/LDP/nag2/x14923.html)


18.7. [Configuring sendmail Options](https://tldp.org/LDP/nag2/x15220.html)


18.8. [Some Useful sendmail Configurations](https://tldp.org/LDP/nag2/x15291.html)


18.9. [Testing Your Configuration](https://tldp.org/LDP/nag2/x15583.html)


18.10. [Running sendmail](https://tldp.org/LDP/nag2/x15649.html)


18.11. [Tips and Tricks](https://tldp.org/LDP/nag2/x15691.html)


19. [Getting EximUp and Running](https://tldp.org/LDP/nag2/x-087-2-exim.html)


19.1. [Running Exim](https://tldp.org/LDP/nag2/x15909.html)


19.2. [If Your Mail Doesn't Get Through](https://tldp.org/LDP/nag2/x15964.html)


19.3. [Compiling Exim](https://tldp.org/LDP/nag2/x15999.html)


19.4. [Mail Delivery Modes](https://tldp.org/LDP/nag2/x-087-2-exim.queue.html)


19.5. [Miscellaneous config Options](https://tldp.org/LDP/nag2/x-087-2-exim.options.html)


19.6. [Message Routing and Delivery](https://tldp.org/LDP/nag2/x-087-2-exim.delivery.html)


19.7. [Protecting Against Mail Spam](https://tldp.org/LDP/nag2/x16298.html)


19.8. [UUCP Setup](https://tldp.org/LDP/nag2/x-087-2-exim.simple.html)


20. [Netnews](https://tldp.org/LDP/nag2/x-087-2-news.html)


20.1. [Usenet History](https://tldp.org/LDP/nag2/x-087-2-news.history.html)


20.2. [What Is Usenet, Anyway?](https://tldp.org/LDP/nag2/x-087-2-news.usenet.html)


20.3. [How Does Usenet Handle News?](https://tldp.org/LDP/nag2/x-087-2-news.algorithm.html)


21. [C News](https://tldp.org/LDP/nag2/x-087-2-cnews.html)


21.1. [Delivering News](https://tldp.org/LDP/nag2/x-087-2-cnews.rnews.html)


21.2. [Installation](https://tldp.org/LDP/nag2/x16700.html)


21.3. [The sys File](https://tldp.org/LDP/nag2/x-087-2-cnews.sys.html)


21.4. [The active File](https://tldp.org/LDP/nag2/x-087-2-cnews.active.html)


21.5. [Article Batching](https://tldp.org/LDP/nag2/x-087-2-cnews.batcher.html)


21.6. [Expiring News](https://tldp.org/LDP/nag2/x-087-2-cnews.explist.html)


21.7. [Miscellaneous Files](https://tldp.org/LDP/nag2/x-087-2-cnews.misc.html)


21.8. [Control Messages](https://tldp.org/LDP/nag2/x-087-2-cnews.control.html)


21.9. [C News in an NFS Environment](https://tldp.org/LDP/nag2/x-087-2-cnews.nfs.html)


21.10. [Maintenance Tools and Tasks](https://tldp.org/LDP/nag2/x-087-2-cnews.maint.html)


22. [NNTP and thenntpd Daemon](https://tldp.org/LDP/nag2/x-087-2-nntp.html)


22.1. [The NNTP Protocol](https://tldp.org/LDP/nag2/x-087-2-nntp.protocol.html)


22.2. [Installing the NNTP Server](https://tldp.org/LDP/nag2/x-087-2-nntp.nntpd.html)


22.3. [Restricting NNTP Access](https://tldp.org/LDP/nag2/x-087-2-nntp.access.html)


22.4. [NNTP Authorization](https://tldp.org/LDP/nag2/x-087-2-nntp.authorize.html)


22.5. [nntpd Interaction with C News](https://tldp.org/LDP/nag2/x-087-2-nntp.interact.html)


23. [Internet News](https://tldp.org/LDP/nag2/x-087-2-inn.html)


23.1. [Some INN Internals](https://tldp.org/LDP/nag2/x18201.html)


23.2. [Newsreaders and INN](https://tldp.org/LDP/nag2/x18278.html)


23.3. [Installing INN](https://tldp.org/LDP/nag2/x18301.html)


23.4. [Configuring INN: the Basic Setup](https://tldp.org/LDP/nag2/x18326.html)


23.5. [INN Configuration Files](https://tldp.org/LDP/nag2/x18341.html)


23.6. [Running INN](https://tldp.org/LDP/nag2/x19004.html)


23.7. [Managing INN: The ctlinnd Command](https://tldp.org/LDP/nag2/x19030.html)


24. [Newsreader Configuration](https://tldp.org/LDP/nag2/x-087-2-newsreaders.html)


24.1. [tin Configuration](https://tldp.org/LDP/nag2/x-087-2-newsreaders.tin.html)


24.2. [trn Configuration](https://tldp.org/LDP/nag2/x-087-2-newsreaders.trn.html)


24.3. [nn Configuration](https://tldp.org/LDP/nag2/x-087-2-newsreaders.nn.html)


A. [Example Network:The Virtual Brewery](https://tldp.org/LDP/nag2/x-087-2-appendix.brewery.html)


A.1. [Connecting the Virtual Subsidiary Network](https://tldp.org/LDP/nag2/x19519.html)


B. [Useful Cable Configurations](https://tldp.org/LDP/nag2/x-087-2-appendix.cables.html)


B.1. [A PLIP Parallel Cable](https://tldp.org/LDP/nag2/x-087-2-cable.plip.html)


B.2. [A Serial NULL Modem Cable](https://tldp.org/LDP/nag2/x-087-2-cable.serial.html)


C. [Linux Network Administrator's Guide, Second Edition Copyright Information](https://tldp.org/LDP/nag2/x-087-2-appendix.gpl.html)


C.1. [0. Preamble](https://tldp.org/LDP/nag2/x19583.html)


C.2. [1. Applicability and Definitions](https://tldp.org/LDP/nag2/x19588.html)


C.3. [2. Verbatim Copying](https://tldp.org/LDP/nag2/x19598.html)


C.4. [3. Copying in Quantity](https://tldp.org/LDP/nag2/x19602.html)


C.5. [4. Modifications](https://tldp.org/LDP/nag2/x19608.html)


C.6. [5. Combining Documents](https://tldp.org/LDP/nag2/x19644.html)


C.7. [6. Collections of Documents](https://tldp.org/LDP/nag2/x19649.html)


C.8. [7. Aggregation with Independent Works](https://tldp.org/LDP/nag2/x19653.html)


C.9. [8. Translation](https://tldp.org/LDP/nag2/x19657.html)


C.10. [9. Termination](https://tldp.org/LDP/nag2/x19660.html)


C.11. [10. Future Revisions of this License](https://tldp.org/LDP/nag2/x19663.html)


D. [SAGE: The SystemAdministrators Guild](https://tldp.org/LDP/nag2/x-087-2-sage.app.html)


[Index](https://tldp.org/LDP/nag2/doc-index.html)


**List of Tables**


2-1. [IP Address Ranges Reserved for Private Use](https://tldp.org/LDP/nag2/x-087-2-issues.ip-addresses.html#X-087-2-ISSUES.RESERVED.ADDRESSES)


4-1. [setserial Command-Line Parameters](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL-SETSERIAL-PARAMETERS)


4-2. [stty Flags Most Relevant to Configuring Serial Devices](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL.STTY.FLAGS)


7-1. [Linux Slip-Line Disciplines](https://tldp.org/LDP/nag2/x-087-2-slip.operation.html#X-087-2-SLIP.LINE.DISCIPLINES)


7-2. [/etc/diphosts Field Description](https://tldp.org/LDP/nag2/x-087-2-slip.server.html#X-087-2-SLIP.DIPHOSTS.FIELDS)


9-1. [Common Netmask Bit Values](https://tldp.org/LDP/nag2/x-087-2-firewall.original.html#X-087-2-CHFW-NETMASKS)


9-2. [ICMP Datagram Types](https://tldp.org/LDP/nag2/x-087-2-firewall.original.html#X-087-2-CHFW-ICMPTYPES)


9-3. [Suggested Uses for TOS Bitmasks](https://tldp.org/LDP/nag2/x-087-2-firewall.tos.manipulation.html#X-087-2-FIREWALL.IPCHAINS.TOS.RECIPES)


13-1. [Some Standard NIS Maps and Corresponding Files](https://tldp.org/LDP/nag2/x10579.html#X-087-2-NIS.TABLE.MAPS)


15-1. [XNS, Novell, and TCP/IP Protocol Relationships](https://tldp.org/LDP/nag2/x11684.html#X-087-2-IX.PROTOCOL.FAMILY)


15-2. [ncpmount Command Arguments](https://tldp.org/LDP/nag2/x-087-2-ipx.ncpfs.client.html#X-087-2-IPX.NCPMOUNT.ARGS)


15-3. [Linux Bindery Manipulation Tools](https://tldp.org/LDP/nag2/x-087-2-ipx.othertools.html#X-087-2-CHIX-BINDERYTOOLS)


15-4. [nprint Command-Line Options](https://tldp.org/LDP/nag2/x-087-2-ipx.ncpfs.printing.html#X-087-2-IPX.NPRINT.OPTIONS)


**List of Figures**


1-1. [The three steps of sending a datagram from erdos to quark](https://tldp.org/LDP/nag2/x-087-2-intro.tcpip.html#X-087-2-INTRO.FIG.IP-FLOW)


2-1. [Subnetting a class B network](https://tldp.org/LDP/nag2/x-087-2-issues.routing.html#X-087-2-ISSUES.FIG.SUBNET)


2-2. [A part of the net topology at Groucho Marx University](https://tldp.org/LDP/nag2/x-087-2-issues.routing.html#X-087-2-ISSUES.FIG.IP)


3-1. [The relationship between drivers, interfaces, and hardware](https://tldp.org/LDP/nag2/x-087-2-hardware.html#X-087-2-HARDWARE.FIG.DRIVERS)


6-1. [A part of the domain namespace](https://tldp.org/LDP/nag2/x-087-2-resolv.howdnsworks.html#X-087-2-RESOLV.FIG.DNS)


9-1. [The two major classes of firewall design](https://tldp.org/LDP/nag2/x-087-2-firewall.introduction.html#X-087-2-FIREWALL.DESIGN.GRAPHIC)


9-2. [The stages of IP datagram processing](https://tldp.org/LDP/nag2/x-087-2-firewall.filteringmethods.html#X-087-2-FIREWALL.METHODS.GRAPHIC)


9-3. [FTP server modes](https://tldp.org/LDP/nag2/x-087-2-firewall.original.html#X-087-2-FIREWALL.FTP.GRAPHIC)


9-4. [A simple IP chain ruleset](https://tldp.org/LDP/nag2/x-087-2-firewall.fwchains.html#X-087-2-FIREWALL.IPCHAINS)


9-5. [The sequence of rules tested for a received UDP datagram](https://tldp.org/LDP/nag2/x-087-2-firewall.fwchains.html#X-087-2-FIREWALL.IPCHAINS.UDP)


9-6. [The rules flow for a received TCP datagram for ssh](https://tldp.org/LDP/nag2/x-087-2-firewall.fwchains.html#X-087-2-FIREWALL.IPCHAINS.TCP.SSH)


9-7. [The rules flow for a received TCP datagram for telnet](https://tldp.org/LDP/nag2/x-087-2-firewall.fwchains.html#X-087-2-FIREWALL.IPCHAINS.TCP.OTHER)


9-8. [Datagram processing chain in IP chains](https://tldp.org/LDP/nag2/x-087-2-firewall.future.html#X-087-2-FIREWALL.ROUTING.IPCHAINS)


9-9. [Datagram processing chain in netfilter](https://tldp.org/LDP/nag2/x-087-2-firewall.future.html#X-087-2-FIREWALL.ROUTING.NETFILTER)


11-1. [A typical IP masquerade configuration](https://tldp.org/LDP/nag2/x-087-2-ipmasq.html#X-087-2-MASQUERADE.NET)


15-1. [IPX internal network](https://tldp.org/LDP/nag2/x-087-2-ipx.router.html#X-087-2-IPX.INTERNAL.NETWORK)


16-1. [Interaction of Taylor UUCP configuration files](https://tldp.org/LDP/nag2/x-087-2-uucp.config.files.html#X-087-2-UUCP.FIG.FILES)


20-1. [Usenet newsflow through Groucho Marx University](https://tldp.org/LDP/nag2/x-087-2-news.usenet.html#X-087-2-NEWS.FIG.ARTICLE-FLOW)


21-1. [News flow through relaynews](https://tldp.org/LDP/nag2/x-087-2-cnews.rnews.html#X-087-2-CNEWS.FIG.FLOW)


23-1. [INN architecture (simplified for clarity)](https://tldp.org/LDP/nag2/x18201.html#X-087-2-INN.INN.ARCHITECTURE)


A-1. [The Virtual Brewery and Virtual Winery subnets](https://tldp.org/LDP/nag2/x-087-2-appendix.brewery.html#X-087-2-APPENDIX.BREWERY.DIAGRAM)


A-2. [The Virtual Brewery Network](https://tldp.org/LDP/nag2/x-087-2-appendix.brewery.html#X-087-2-APPENDIX.BREWERY.SUBSIDIARY)


B-1. [Parallel PLIP cable](https://tldp.org/LDP/nag2/x-087-2-cable.serial.html#X-087-2-CABLE.PLIP.DIAGRAM)


B-2. [Serial NULL-Modem cable](https://tldp.org/LDP/nag2/x-087-2-cable.serial.html#X-087-2-CABLE.NULLMODEM.DIAGRAM)


**List of Examples**


4-1. [Example rc.serial setserial Commands](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL-RC.SERIAL.SETSERIAL)


4-2. [Output of setserial -bg /dev/ttyS Command](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL.SETSERIAL.OUTPUT)


4-3. [Example rc.serial stty Commands](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL-RC.SERIAL.STTY)


4-4. [Example rc.serial stty Commands Using Modern Syntax](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL-RC.SERIAL.STTY.NEW)


4-5. [Output of stty -a Command](https://tldp.org/LDP/nag2/x-087-2-serial-configuration.html#X-087-2-SERIAL.STTY.OUTPUT)


4-6. [Sample /etc/mgetty/mgetty.config File](https://tldp.org/LDP/nag2/x-087-2-serial.getty.html#X-087-2-SERIAL.MGETTY.CONF)


6-1. [Sample host.conf File](https://tldp.org/LDP/nag2/x-087-2-resolv.library.html#X-087-2-DNS-HOST.CONF.FILE)


6-2. [Sample nsswitch.conf File](https://tldp.org/LDP/nag2/x-087-2-resolv.library.html#X-087-2-DNS-NSSWITCH.CONF.FILE)


6-3. [Sample nsswitch.conf File Using an Action Statement](https://tldp.org/LDP/nag2/x-087-2-resolv.library.html#X-087-2-DNS-NSSWITCH.CONF.FILE.EXTENDED)


6-4. [An Excerpt from the named.hosts File for the Physics Department](https://tldp.org/LDP/nag2/x-087-2-resolv.howdnsworks.html#X-087-2-RESOLV.FIG.HOSTS)


6-5. [An Excerpt from the named.hosts File for GMU](https://tldp.org/LDP/nag2/x-087-2-resolv.howdnsworks.html#X-087-2-RESOLV.FIG.NSPTR)


6-6. [An Excerpt from the named.rev File for Subnet 12](https://tldp.org/LDP/nag2/x-087-2-resolv.howdnsworks.html#X-087-2-RESOLV.FIG.SUBNET12)


6-7. [An Excerpt from the named.rev File for Network 149.76](https://tldp.org/LDP/nag2/x-087-2-resolv.howdnsworks.html#X-087-2-RESOLV.FIG.GROUCHO-REV)


6-8. [The named.boot File for vlager](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html#X-087-2-RESOLV.FIG.NAMED.BOOT)


6-9. [The BIND 8 equivalent named.conf File for vlager](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html#X-087-2-RESOLV.FIG.NAMED.CONF)


6-10. [The named.ca File](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html#X-087-2-RESOLV.FIG.NAMED.CACHE)


6-11. [The named.hosts File](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html#X-087-2-RESOLV.FIG.NAMED.HOSTS)


6-12. [The named.local File](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html#X-087-2-RESOLV.FIG.NAMED.LOCAL)


6-13. [The named.rev File](https://tldp.org/LDP/nag2/x-087-2-resolv.named.html#X-087-2-RESOLV.FIG.NAMED.REV)


7-1. [A Sample dip Script](https://tldp.org/LDP/nag2/x-087-2-slip.dip.html#X-087-2-SLIP.FIG.SCRIPT)


12-1. [A Sample /etc/inetd.conf File](https://tldp.org/LDP/nag2/x-087-2-appl.inetd.html#X-087-2-APPL.FIG.INETD.CONF)


12-2. [A Sample /etc/services File](https://tldp.org/LDP/nag2/x-087-2-appl.services.html#X-087-2-ETC.SERVICES)


12-3. [A Sample /etc/protocols File](https://tldp.org/LDP/nag2/x-087-2-appl.services.html#X-087-2-ETC.PROTOCOLS)


12-4. [A Sample /etc/rpc File](https://tldp.org/LDP/nag2/x-087-2-appl.rpc.html#X-087-2-RPC.FIG)


12-5. [Example ssh Client Configuration File](https://tldp.org/LDP/nag2/x-087-2-appl.remote.html#X-087-2-FEATURES.SSH.CONF)


13-1. [Sample ypserv.securenets File](https://tldp.org/LDP/nag2/x-087-2-nis.securenets.html#X-087-2-NIS.SECURENETS.FILE)


13-2. [Sample nsswitch.conf File](https://tldp.org/LDP/nag2/x-087-2-nis.nsswitch.html#X-087-2-NIS.FIG.SWITCH)


18-1. [Sample Configuration File vstout.smtp.m4](https://tldp.org/LDP/nag2/x14661.html#X-087-2-SENDMAIL.MC.SMTP)


18-2. [Sample Configuration File vstout.uucpsmtp.m4](https://tldp.org/LDP/nag2/x14661.html#X-087-2-SENDMAIL.MC.UUCPSMTP)


18-3. [Rewrite Rule from vstout.uucpsmtp.m4](https://tldp.org/LDP/nag2/x14923.html#X-087-2-SENDMAIL.REWRITE.EXAMPLE)


18-4. [Sample aliases File](https://tldp.org/LDP/nag2/x15291.html#X-087-2-SAMP.ALIAS.FIG)


18-5. [Sample Output of the mailstats Command](https://tldp.org/LDP/nag2/x15691.html#X-087-2-SENDMAIL.MAILSTATS)


18-6. [Sample Output of the oststat Command](https://tldp.org/LDP/nag2/x15691.html#X-087-2-SENDMAIL.HOSTSTAT)

* * *
|  | [Next](https://tldp.org/LDP/nag2/f3.html)
---|---|---
|  | Preface
