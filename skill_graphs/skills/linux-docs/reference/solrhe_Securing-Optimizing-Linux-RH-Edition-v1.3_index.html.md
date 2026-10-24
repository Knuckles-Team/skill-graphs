# Securing and Optimizing Linux
## RedHat Edition -A Hands on Guide
![Wolf](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/Annimals/Chapter3.gif)
![openNA logo](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/images/OpenNA-NewLogo-Penguin.gif)
### Gerhard Mourani
Open Network Architecture [www.openna.com](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/appendixa.html#rsrcofwbi1)


gmourani@openna.com
gmourani@netscape.net

### Madhu "Maddy"
[Copyright](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/ln36.html) © 2000 by Gerhard Mourani and OpenDocs, LLC.
[Copyright](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/ln36.html) © 2000 by Madhusudan (Madhu "Maddy") XML Source
* * *

**Table of Contents**


[Preface](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/preface.html)


1. [Why did i write this book?](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/preface1.html)


2. [Why fiddle?](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/preface2.html)


3. [DocBook !](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/preface3.html)


4. [DocBook/XML](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/preface4.html)


1. [Getting Started](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/get-start.html)


1. [Introduction](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/intro.html)


2. [Installation](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/install.html)


2. [Overview of OS Linux](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/overview.html)


3. [Installation of your Linux Server](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/installlin.html)


4. [Post-Install](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/linpostinstall.html)


3. [Security, Optimization and Upgrade](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/Secure-optimize.html)


5. [General System Security](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/gen-syssecured.html)


6. [Linux General Optimization](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/gen-optim.html)


7. [Configuring and Building a Secure, Optimized Kernel](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/secopt-kernel.html)


4. [Networking -Management, Firewall, Masquerading and Forwarding](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/net-manage.html)


8. [TCP/IP -Network Management](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/tcp-ip.html)


9. [Files -Networking Functionality](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/file-netfunc.html)


10. [Networking -Firewall](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-netfirew.html)


11. [The firewall scripts files](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/fwall-scripts.html)


12. [Networking Firewall -Masquerading and Forwarding](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/Masq-forward.html)


5. [Software -Security](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-secure.html)


13. [Linux -The Compiler functionality](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/lin-compiler.html)


14. [Software -Security/Monitoring](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-secmonitor.html)


6. [Software -Networking](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-net.html)


15. [Software -Securities](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-netsecured.html)


16. [Software -Securties(commercial)](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/softsec-com.html)


17. [Software -Securities/System Integrity](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/sysintegrity.html)


18. [Linux Tripwire ASR 1.3.1](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/tripwireASR.html)


19. [Software -Securities/Management & Limitation](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-limits.html)


20. [Set Limits using Qouta](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/quota.html)


21. [Software -Networking](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-netwrkng.html)


22. [Software -Server/Mail Network](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soser-mailn.html)


23. [Linux IMAP & POP Server](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/imapop.html)


24. [Software -Networking/Encryption](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/netencrypt.html)


25. [Linux FreeS/WAN VPN](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/fSWAn.html)


26. [Linux OpenLDAP Server](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/net-oLDAP.html)


27. [Linux PostgreSQL Database Server](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/datab-pSQL.html)


28. [Software -Server/Proxy Network](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/netproxy-squid.html)


29. [Software -Network Server, web/Apache](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/netweb-Apache.html)


30. [Optional component to install with Apache](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/opt-Apache.html)


31. [Software -Server/File Sharing-Network](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/soft-fileshrng.html)


32. [Linux `FTP` Server](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/ftpd.html)


7. [Backup and Restore](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/backup-rest.html)


33. [Why's and When's of Backup and Restore](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/whywhen.html)


I. [Appendixes](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/Appendix.html)


A. [Resources](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/appendixa.html)


B. [Tweaks, Tips and Administration tasks](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/appendixb.html)


C. [Obtaining Requests for Comments (RFCs)](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/appendixc.html)


**List of Tables**


3-1. [Sample representation of partitions](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap3sec15.html#AEN907)


33-1. [Dump scheme](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/back-dump.html#AEN23759)


**List of Examples**


3-1. [Starting and Stopping various Daemon's](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap3sec21.html#AEN1574)


5-1. [Export file systems using NFS](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap5sec33.html#AEN3270)


5-2. [Disable console-equivalent access](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap5sec34.html#AEN3307)


5-3. [Print log reports](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap5sec50.html#AEN3854)


5-4. [Use man pages](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap5sec52.html#AEN4016)


5-5. [Use find to find](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap5sec62.html#AEN4250)


6-1. [For 128 MB of RAM](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap6sec69.html#AEN4625)


7-1. [SMP support](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap7sec80.html#AEN5283)


8-1. [Two ISA ethernet cards](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap8sec88.html#AEN5920)


12-1. [`rc.firewall.blocked`](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap12sec107.html#AEN6898)


13-1. [Using tar](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap13sec111.html#AEN7175)


15-1. [Remote login using ssh](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap15sec125.html#AEN8487)


15-2. [scp Secure Copy utility](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap15sec125.html#AEN8501)


15-3. [local to remote](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap15sec125.html#AEN8511)


16-1. [login to a remote using ssh2](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap16sec134.html#AEN9187)


16-2. [sftp2, Secure File Transfer](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap16sec134.html#AEN9200)


18-1. [Usage of Tripwire](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap18sec149.html#AEN9929)


19-1. [Importing using gpg](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap19sec154.html#AEN10076)


19-2. [Signing key](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap19sec154.html#AEN10089)


19-3. [Encrypting](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap19sec155.html#AEN10109)


19-4. [Decrypting](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap19sec155.html#AEN10132)


20-1. [`usrquota`](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap20sec156.html#AEN10233)


20-2. [`grpquota`](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap20sec156.html#AEN10253)


21-1. [dnsquery](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap21sec171.html#AEN11472)


21-2. [Look up host names](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap21sec171.html#AEN11485)


21-3. [Using host](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap21sec171.html#AEN11500)


21-4. [List a complete domain](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap21sec171.html#AEN11511)


22-1. [Overriding RBL](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap22sec176.html#AEN12140)


22-2. [Alternative names](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap22sec180.html#AEN12401)


22-3. [`sendmail.cf`](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap22sec182.html#AEN12549)


26-1. [`my-data-file`](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap26sec216.html#AEN16477)


26-2. [LDMB backend](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap26sec217.html#AEN16513)


26-3. [`modifyentry`](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap26sec217.html#AEN16549)


26-4. [Address Book](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap26sec218.html#AEN16613)


30-1. [Using Netscape browser](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap29sec271.html#AEN21301)


33-1. [Backup directory of a week](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap29sec306.html#AEN23634)


33-2. [scp SSH command](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap29sec311.html#AEN24103)


33-3. [scp SSH command](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap29sec311.html#AEN24141)

* * *
|  | [Next](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/preface.html)
---|---|---
|  | Preface
