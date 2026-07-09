# 12 Tcpdump Commands – A Network Sniffer Tool
[Narad Shrestha](https://www.tecmint.com/author/navin/ "View all posts by Narad Shrestha")Last Updated: July 26, 2023 Read Time: 8 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/), [Networking Commands](https://www.tecmint.com/category/networking-commands/) [33 Comments](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comments)
In our previous article, we have seen [20 Netstat Commands](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/) (netstat now replaced by [ss command](https://www.tecmint.com/ss-command-examples-in-linux/ "Monitor Network Connections in Linux")) to monitor or manage a Linux network.
This is another ongoing series of packet sniffer tools called **tcpdump**. Here, we are going to show you how to install **tcpdump** and then we discuss and cover some useful commands with their practical examples.
![Linux tcpdump command examples](https://www.tecmint.com/wp-content/uploads/2012/08/Tcpdump-Commands-300x194.png)Linux tcpdump command examples
**tcpdump** is a most powerful and widely used command-line packets sniffer or package analyzer tool which is used to capture or filter **TCP/IP** packets that are received or transferred over a network on a specific interface.
**You might also like:**
  * [19 Linux Network Bandwidth Monitoring Tools](https://www.tecmint.com/linux-network-bandwidth-monitoring-tools/ "Linux Network Bandwidth Monitoring Tools")
  * [22 Linux Networking Commands for Sysadmin](https://www.tecmint.com/linux-networking-commands/ "Linux Networking Commands for Sysadmin")
  * [15 ‘ifconfig’ Commands to Configure Network Interface in Linux](https://www.tecmint.com/ifconfig-command-examples/ "ifconfig Commands to Configure Network in Linux")
  * [11 Best IP Address Management Tools for Linux Network](https://www.tecmint.com/ip-address-management-tools-for-linux/ "Linux IP Address Management Tools")


**Tcpdump** is readily available across a wide range of Linux/Unix-based operating systems. Furthermore, it offers the invaluable option to save captured packets in a file for future analysis.
It saves the file in a **pcap** format, that can be viewed by tcpdump command or an open-source GUI-based tool called [Wireshark (Network Protocol Analyzer)](https://www.tecmint.com/wireshark-network-traffic-analyzer-for-linux/) that reads tcpdump **pcap** format files.
### How to Install tcpdump in Linux
[Many Linux distributions](https://www.tecmint.com/top-most-popular-linux-distributions/ "Popular Linux Distributions") already shipped with the **tcpdump** tool, if in case you don’t have it on a system, you can install it using either of the following commands.
```
$ sudo apt install tcpdump         [On **Debian, Ubuntu and Mint**]
$ sudo yum install tcpdump         [On **RHEL/CentOS/Fedora** and **Rocky/AlmaLinux**]
$ sudo emerge -a sys-apps/tcpdump  [On **Gentoo Linux**]
$ sudo apk add tcpdump             [On **Alpine Linux**]
$ sudo pacman -S tcpdump           [On **Arch Linux**]
$ sudo zypper install tcpdump      [On **OpenSUSE**]

```

### Getting Started with tcpdump Command Examples
Once the **tcpdump** tool is installed on your system, you can continue to browse the following commands with their examples.
#### 1. Capture Packets from Specific Interface
The command screen will scroll up until you interrupt and when we execute the **tcpdump** command it will capture from all the interfaces, however with `-i` switch only capture from the desired interface.
```
**# tcpdump -i eth0**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:33:31.976358 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 3500440357:3500440553, ack 3652628334, win 18760, length 196
11:33:31.976603 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 196, win 64487, length 0
11:33:31.977243 ARP, Request who-has tecmint.com tell 172.16.25.126, length 28
11:33:31.977359 ARP, Reply tecmint.com is-at 00:14:5e:67:26:1d (oui Unknown), length 46
11:33:31.977367 IP 172.16.25.126.54807 > tecmint.com: 4240+ PTR? 125.25.16.172.in-addr.arpa. (44)
11:33:31.977599 IP tecmint.com > 172.16.25.126.54807: 4240 NXDomain 0/1/0 (121)
11:33:31.977742 IP 172.16.25.126.44519 > tecmint.com: 40988+ PTR? 126.25.16.172.in-addr.arpa. (44)
11:33:32.028747 IP 172.16.20.33.netbios-ns > 172.16.31.255.netbios-ns: NBT UDP PACKET(137): QUERY; REQUEST; BROADCAST
11:33:32.112045 IP 172.16.21.153.netbios-ns > 172.16.31.255.netbios-ns: NBT UDP PACKET(137): QUERY; REQUEST; BROADCAST
11:33:32.115606 IP 172.16.21.144.netbios-ns > 172.16.31.255.netbios-ns: NBT UDP PACKET(137): QUERY; REQUEST; BROADCAST
11:33:32.156576 ARP, Request who-has 172.16.16.37 tell old-oraclehp1.midcorp.mid-day.com, length 46
11:33:32.348738 IP tecmint.com > 172.16.25.126.44519: 40988 NXDomain 0/1/0 (121)
```

#### 2. Capture Only N Number of Packets
When you run the **tcpdump** command it will capture all the packets for the specified interface, until you **hit** the cancel button. But using `-c` option, you can capture a specified number of packets. The below example will only capture **6** packets.
```
**# tcpdump -c 5 -i eth0**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:40:20.281355 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 3500447285:3500447481, ack 3652629474, win 18760, length 196
11:40:20.281586 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 196, win 65235, length 0
11:40:20.282244 ARP, Request who-has tecmint.com tell 172.16.25.126, length 28
11:40:20.282360 ARP, Reply tecmint.com is-at 00:14:5e:67:26:1d (oui Unknown), length 46
11:40:20.282369 IP 172.16.25.126.53216 > tecmint.com.domain: 49504+ PTR? 125.25.16.172.in-addr.arpa. (44)
11:40:20.332494 IP tecmint.com.netbios-ssn > 172.16.26.17.nimaux: Flags [P.], seq 3058424861:3058424914, ack 693912021, win 64190, length 53 NBT Session Packet: Session Message
**6 packets captured**
23 packets received by filter
0 packets dropped by kernel
```

#### 3. Print Captured Packets in ASCII
The below **tcpdump** command with the option `-A` displays the package in **ASCII** format. It is a character-encoding scheme format.
```
**# tcpdump -A -i eth0**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
09:31:31.347508 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 3329372346:3329372542, ack 4193416789, win 17688, length 196
M.r0...vUP.E.X.......~.%..>N..oFk.........KQ..)Eq.d.,....r^l......m\.oyE....-....g~m..Xy.6..1.....c.O.@...o_..J....i.*.....2f.mQH...Q.c...6....9.v.gb........;..4.).UiCY]..9..x.)..Z.XF....'|..E......M..u.5.......ul
09:31:31.347760 IP 192.168.0.1.nokia-ann-ch1 > 192.168.0.2.ssh: Flags [.], ack 196, win 64351, length 0
M....vU.r1~P.._..........
^C09:31:31.349560 IP 192.168.0.2.46393 > b.resolvers.Level3.net.domain: 11148+ PTR? 1.0.168.192.in-addr.arpa. (42)
E..F..@.@............9.5.2.f+............1.0.168.192.in-addr.arpa.....

3 packets captured
11 packets received by filter
0 packets dropped by kernel
```

#### 4. Display Available Interfaces
To list the number of available interfaces on the system, run the following command with `-D` option.
```
**# tcpdump -D**

 1.eth0
2.eth1
3.usbmon1 (USB bus number 1)
4.usbmon2 (USB bus number 2)
5.usbmon3 (USB bus number 3)
6.usbmon4 (USB bus number 4)
7.usbmon5 (USB bus number 5)
8.any (Pseudo-device that captures on all interfaces)
9.lo
```

#### 5. Display Captured Packets in HEX and ASCII
The following command with option `-XX` capture the data of each packet, including its link level header in **HEX** and **ASCII** format.
```
**# tcpdump -XX -i eth0**

11:51:18.974360 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 3509235537:3509235733, ack 3652638190, win 18760, length 196
        0x0000:  b8ac 6f2e 57b3 0001 6c99 1468 0800 4510  ..o.W...l..h..E.
        0x0010:  00ec 8783 4000 4006 275d ac10 197e ac10  ....@.@.']...~..
        0x0020:  197d 0016 1129 d12a af51 d9b6 d5ee 5018  .}...).*.Q....P.
        0x0030:  4948 8bfa 0000 0e12 ea4d 22d1 67c0 f123  IH.......M".g..#
        0x0040:  9013 8f68 aa70 29f3 2efc c512 5660 4fe8  ...h.p).....V`O.
        0x0050:  590a d631 f939 dd06 e36a 69ed cac2 95b6  Y..1.9...ji.....
        0x0060:  f8ba b42a 344b 8e56 a5c4 b3a2 ed82 c3a1  ...*4K.V........
        0x0070:  80c8 7980 11ac 9bd7 5b01 18d5 8180 4536  ..y.....[.....E6
        0x0080:  30fd 4f6d 4190 f66f 2e24 e877 ed23 8eb0  0.OmA..o.$.w.#..
        0x0090:  5a1d f3ec 4be4 e0fb 8553 7c85 17d9 866f  Z...K....S|....o
        0x00a0:  c279 0d9c 8f9d 445b 7b01 81eb 1b63 7f12  .y....D[{....c..
        0x00b0:  71b3 1357 52c7 cf00 95c6 c9f6 63b1 ca51  q..WR.......c..Q
        0x00c0:  0ac6 456e 0620 38e6 10cb 6139 fb2a a756  ..En..8...a9.*.V
        0x00d0:  37d6 c5f3 f5f3 d8e8 3316 d14f d7ab fd93  7.......3..O....
        0x00e0:  1137 61c1 6a5c b4d1 ddda 380a f782 d983  .7a.j\....8.....
        0x00f0:  62ff a5a9 bb39 4f80 668a                 b....9O.f.
11:51:18.974759 IP 172.16.25.126.60952 > mddc-01.midcorp.mid-day.com.domain: 14620+ PTR? 125.25.16.172.in-addr.arpa. (44)
        0x0000:  0014 5e67 261d 0001 6c99 1468 0800 4500  ..^g&...l..h..E.
        0x0010:  0048 5a83 4000 4011 5e25 ac10 197e ac10  .HZ.@.@.^%...~..
        0x0020:  105e ee18 0035 0034 8242 391c 0100 0001  .^...5.4.B9.....
        0x0030:  0000 0000 0000 0331 3235 0232 3502 3136  .......125.25.16
        0x0040:  0331 3732 0769 6e2d 6164 6472 0461 7270  .172.in-addr.arp
        0x0050:  6100 000c 0001                           a.....
```

#### 6. Capture and Save Packets in a File
As we said, that **tcpdump** has a feature to capture and save the file in a **.pcap** format, to do this just execute the command with `-w` option.
```
**# tcpdump -w 0001.pcap -i eth0**

tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
4 packets captured
4 packets received by filter
0 packets dropped by kernel
```

#### 7. Read Captured Packets File
To read and analyze captured packet **0001.pcap** file use the command with `-r` option, as shown below.
```
**# tcpdump -r 0001.pcap**

reading from file 0001.pcap, link-type EN10MB (Ethernet)
09:59:34.839117 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 3353041614:3353041746, ack 4193563273, win 18760, length 132
09:59:34.963022 IP 192.168.0.1.nokia-ann-ch1 > 192.168.0.2.ssh: Flags [.], ack 132, win 65351, length 0
09:59:36.935309 IP 192.168.0.1.netbios-dgm > 192.168.0.255.netbios-dgm: NBT UDP PACKET(138)
09:59:37.528731 IP 192.168.0.1.nokia-ann-ch1 > 192.168.0.2.ssh: Flags [P.], seq 1:53, ack 132, win 65351, length 5
```

#### 8. Capture IP Address Packets
To capture packets for a specific interface, run the following command with option `-n`.
```
**# tcpdump -n -i eth0**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
12:07:03.952358 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 3509512873:3509513069, ack 3652639034, win 18760, length 196
12:07:03.952602 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 196, win 64171, length 0
12:07:03.953311 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 196:504, ack 1, win 18760, length 308
12:07:03.954288 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 504:668, ack 1, win 18760, length 164
12:07:03.954502 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 668, win 65535, length 0
12:07:03.955298 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 668:944, ack 1, win 18760, length 276
12:07:03.955425 IP 172.16.23.16.netbios-ns > 172.16.31.255.netbios-ns: NBT UDP PACKET(137): REGISTRATION; REQUEST; BROADCAST
12:07:03.956299 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 944:1236, ack 1, win 18760, length 292
12:07:03.956535 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 1236, win 64967, length 0
```

#### 9. Capture only TCP Packets.
To capture packets based on **TCP** port, run the following command with option **tcp**.
```
**# tcpdump -i eth0 tcp**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
12:10:36.216358 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 3509646029:3509646225, ack 3652640142, win 18760, length 196
12:10:36.216592 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 196, win 64687, length 0
12:10:36.219069 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 196:504, ack 1, win 18760, length 308
12:10:36.220039 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 504:668, ack 1, win 18760, length 164
12:10:36.220260 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 668, win 64215, length 0
12:10:36.222045 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 668:944, ack 1, win 18760, length 276
12:10:36.223036 IP 172.16.25.126.ssh > 172.16.25.125.apwi-rxspooler: Flags [P.], seq 944:1108, ack 1, win 18760, length 164
12:10:36.223252 IP 172.16.25.125.apwi-rxspooler > 172.16.25.126.ssh: Flags [.], ack 1108, win 65535, length 0
^C12:10:36.223461 IP mid-pay.midcorp.mid-day.com.netbios-ssn > 172.16.22.183.recipe: Flags [.], seq 283256512:283256513, ack 550465221, win 65531, length 1[|SMB]
```

#### 10. Capture Packet from Specific Port
Let’s say you want to capture packets for specific port 22, execute the below command by specifying port number **22** as shown below.
```
**# tcpdump -i eth0 port 22**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
10:37:49.056927 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 3364204694:3364204890, ack 4193655445, win 20904, length 196
10:37:49.196436 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 4294967244:196, ack 1, win 20904, length 248
10:37:49.196615 IP 192.168.0.1.nokia-ann-ch1 > 192.168.0.2.ssh: Flags [.], ack 196, win 64491, length 0
10:37:49.379298 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 196:616, ack 1, win 20904, length 420
10:37:49.381080 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 616:780, ack 1, win 20904, length 164
10:37:49.381322 IP 192.168.0.1.nokia-ann-ch1 > 192.168.0.2.ssh: Flags [.], ack 780, win 65535, length 0
```

#### 11. Capture Packets from source IP
To capture packets from the source **IP** , say you want to capture packets for **192.168.0.2** , use the command as follows.
```
**# tcpdump -i eth0 src 192.168.0.2**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
10:49:15.746474 IP 192.168.0.2.ssh > 192.168.0.1.nokia-ann-ch1: Flags [P.], seq 3364578842:3364579038, ack 4193668445, win 20904, length 196
10:49:15.748554 IP 192.168.0.2.56200 > b.resolvers.Level3.net.domain: 11289+ PTR? 1.0.168.192.in-addr.arpa. (42)
10:49:15.912165 IP 192.168.0.2.56234 > b.resolvers.Level3.net.domain: 53106+ PTR? 2.0.168.192.in-addr.arpa. (42)
10:49:16.074720 IP 192.168.0.2.33961 > b.resolvers.Level3.net.domain: 38447+ PTR? 2.2.2.4.in-addr.arpa. (38)
```

#### 12. Capture Packets from destination IP
To capture packets from the destination **IP** , say you want to capture packets for **50.116.66.139** , use the command as follows.
```
**# tcpdump -i eth0 dst 50.116.66.139**

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
10:55:01.798591 IP 192.168.0.2.59896 > 50.116.66.139.http: Flags [.], ack 2480401451, win 318, options [nop,nop,TS val 7955710 ecr 804759402], length 0
10:55:05.527476 IP 192.168.0.2.59894 > 50.116.66.139.http: Flags [F.], seq 2521556029, ack 2164168606, win 245, options [nop,nop,TS val 7959439 ecr 804759284], length 0
10:55:05.626027 IP 192.168.0.2.59894 > 50.116.66.139.http: Flags [.], ack 2, win 245, options [nop,nop,TS val 7959537 ecr 804759787], length 0
```

This article may help you to explore the **tcpdump** command in-depth and also to capture and analyze packets in the future. There are a number of options available, you can use the options as per your requirement. Please share if you find this article useful through our comment box.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Resolve “Temporary failure in name resolution” Issue](https://www.tecmint.com/resolve-temporary-failure-in-name-resolution/)
Next article:
[How to Connect Odoo with ONLYOFFICE Docs on Ubuntu](https://www.tecmint.com/integrate-odoo-with-onlyoffice-on-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/a157a8a03eb75c94b928f5d1750df58aa79cead2a9689003c11da3642b08cd74?s=100&d=blank&r=g)
Narad Shrestha
He has over 10 years of rich IT experience which includes various Linux Distros, FOSS and Networking. Narad always believes sharing IT knowledge with others and adopts new technology with ease.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[How to Use Rsync Command: 16 Examples for Linux File Sync](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[15 Useful “ifconfig” Commands to Configure Network Interface in Linux](https://www.tecmint.com/ifconfig-command-examples/)
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[How to Find Most Used Disk Space Directories and Files in Linux](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/)
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[4 Ways to Find Out Which Process Listening on a Particular Port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[How to Find Command Location and Description in Linux](https://www.tecmint.com/find-linux-command-description-and-location/)
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
[How to Use the Linux column Command to Format Text into Tables](https://www.tecmint.com/linux-column-command/)
### 33 Comments
[Leave a Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/f2d3c1b80da7aef76b3727216b8ee48d01b71171574f12b4bfc64e5313c97730?s=50&d=blank&r=g)
eisteingr
[ May 17, 2025 at 10:51 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-2308004)
Tcpdump is an optimal tool, but when I need to extract TCP stream content, I prefer using Justniffer
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-2308004)
  2. ![](https://secure.gravatar.com/avatar/600268c67b95cad0beb51d9a7671643cd160fbf21d59919c257cfad8b0489dcd?s=50&d=blank&r=g)
Skye
[ April 16, 2019 at 4:05 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1132482)
The description of `"-n"` is not correct. That option simply skips name resolution.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1132482)
  3. ![](https://secure.gravatar.com/avatar/85c952866173a30e3994d488db3427d8d9dbe84b42123f833be8b1bd3ccb50cd?s=50&d=blank&r=g)
Tanmay Pradhan
[ March 28, 2019 at 5:54 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1120430)
very useful to execute day to day task.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1120430)
  4. ![](https://secure.gravatar.com/avatar/b77f796ad48eca215f0dbf6184be19a5cbed93b4ba249006b0e52b308bad7323?s=50&d=blank&r=g)
Lakshmisha
[ February 12, 2019 at 11:00 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1100573)
How to print this page/save as PDF there is no option provided here.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1100573)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 12, 2019 at 11:52 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1100577)
@Lakshisha,
Sorry we currently don’t have any feature to save the page as PDF, but we are planning to introduce “Save as PDF” feature soon..
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1100577)
       * ![](https://secure.gravatar.com/avatar/d95f251672d75e8e207786ec4e7aba9683a1059dc34695482a9d4db521f0892a?s=50&d=blank&r=g)
dan Edens
[ August 31, 2023 at 8:29 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-2050742)
Check out “**GoFullPage – Full Page Screen Capture** ” chrome extension to capture a screenshot of current page in entirety and reliably.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-2050742)
  5. ![](https://secure.gravatar.com/avatar/d98b8b6d8bae5d42979596e47ec34df96cce551ed450d7fb7498676683a037a4?s=50&d=blank&r=g)
DPow
[ September 28, 2018 at 7:27 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1040779)
Really excellent article on tcpdump commands, liked how the commands are explained.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1040779)
  6. ![](https://secure.gravatar.com/avatar/952823823264e5330decf49dd5242d22c2af87f1bf4b064b68fdef69f41b4abc?s=50&d=blank&r=g)
Zoran Veljković
[ September 13, 2018 at 2:33 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1035208)
Hello,
I rarely use Linux but now, for one reason, I have to, because I have a problem with my provider.
I use the Cisco IP Phone 7911 in the company. The address of the remote TFTP server is 1.2.3.4. My CISCO phone can not establish a connection because, I suppose, the provider blocked ports or services at my address.
For connection to a remote TFTP server we use the Mikrotik router. I would like to use the tcpdump command to get a response, where there is a problem in the path to my TFTP server.
Can you help me?
Regards,
Zoran
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1035208)
     * ![](https://secure.gravatar.com/avatar/d95f251672d75e8e207786ec4e7aba9683a1059dc34695482a9d4db521f0892a?s=50&d=blank&r=g)
dan Edens
[ August 31, 2023 at 8:31 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-2050743)
I could be wrong, I’d need to see it to better understand, but I think you need to forward the port through the mikrotik, and then use the address of the mikrotik instead of hitting the tftp server directly.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-2050743)
  7. ![](https://secure.gravatar.com/avatar/6240d64901b848ad05e16adeb6401bf2caedd730a10f51d9c64bf4f58d06cbfc?s=50&d=blank&r=g)
Mohit
[ August 23, 2018 at 12:52 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1026633)
Great compilation of most useful options of tcpdump. Thanks.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-1026633)
  8. ![](https://secure.gravatar.com/avatar/5208dd7e66c1b16dc574387acc122e28cdf3b20ab97735e7639d00c4f604d086?s=50&d=blank&r=g)
Bad Prad
[ March 15, 2018 at 12:33 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-975997)
This may be unrelated to tcpdump, but I am trying to find who which workstation on a LAN is using too much traffic.
All traffic is routed through a wireless LAN, which is turn is a cellular modem. The modem control panel cannot provide this information.
Workstation on the LAN run various operating systems – Linux, Windows, Android and IOS.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-975997)
  9. ![](https://secure.gravatar.com/avatar/3c1ca1d8bca7cee5ce089d57ca28595bc6822f8d81c729fddf8db4412ce70ffc?s=50&d=blank&r=g)
Josh
[ June 20, 2017 at 8:32 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-896088)
Excellent article. Do you have any article on network interface source code or configuration of network interface card?
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-896088)
  10. ![](https://secure.gravatar.com/avatar/f9c2e5ee6340cd6ff2894e5b0cf1650cd5b227c73bab2a57625355110bdd16be?s=50&d=blank&r=g)
Admin
[ September 18, 2016 at 9:37 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-818989)
Having a hard time here, hopefully you can help. This server in question (Centos 6.8) has bandwidth sky rocketing to about 100MBps. It’s running cPanel control panel and none of the accounts are using much bandwidth. I cannot figure out how to trace where the spike is coming from. I tried this tcpdump but confused. I need to trace the source of the bandwidth spike and really could use some help. IPTRAF is a bit confusing too to me.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-818989)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 19, 2016 at 11:18 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-819199)
@Admin,
I think you should use these two tools to find out the network bandwidth source..
<https://www.tecmint.com/install-iftop-bandwidth-monitoring-tool-in-rhel-centos-fedora/>
<https://www.tecmint.com/install-vnstat-and-vnstati-to-monitor-linux-network-traffic/>
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-819199)
  11. ![](https://secure.gravatar.com/avatar/67c63aa460b1c81a5a750eaba8ce746491d5f85ac6064e8d58a0e26ca7928d3a?s=50&d=blank&r=g)
Gene
[ October 9, 2015 at 1:45 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-682491)
This has been very informative and helpful. Had to use some of the commands for some deep debugging…. thanks
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-682491)
  12. ![](https://secure.gravatar.com/avatar/e59757bcb62d5bd5290e4cf683379a682daa2a7fc9ee93b6a7e73d5d149d1516?s=50&d=blank&r=g)
abhi
[ September 23, 2015 at 9:16 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-672287)
How can I take the tcpdump of a destination port.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-672287)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 24, 2015 at 11:54 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-672697)
@Abhi,
Here is the following command that will help you out.
```
# tcpdump -i eth0 port 22

```

Don’t forget to replace the port 22 with your desired port.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-672697)
  13. ![](https://secure.gravatar.com/avatar/95ae91d6102bb94fe094d82f1bbd3e1ae7b57bd07dc59e4e20fd8af3d9d9a0e4?s=50&d=blank&r=g)
Nilesh
[ September 20, 2015 at 3:20 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-669983)
Very Good article
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-669983)
  14. ![](https://secure.gravatar.com/avatar/4a89e1f1b35f489db1f1b8321ec71c42e18d0b10cdc8b050be29bc825c427a5e?s=50&d=blank&r=g)
sara kiran
[ April 14, 2015 at 10:05 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-542055)
Hope you must be fine by grace of God. I am facing a problem in my thesis which is about to change the link data rate depending upon the buffer occupancy i-e if the buffer space is filled above threshold then increase the link data rate and if the buffer is occupied below threshold then reduce the link data rate. Now the problem exists in determining the buffer space occupied. For this I am using” ifconfig” and “netstat”.
For ifconfig the output for switch AS-1 eth1 is as follows (by using netstat I was getting the same output):
AS-1-eth1 Link encap:Ethernet HWaddr 7a:81:df:f1:29:74
inet6 addr: fe80::7881:dfff:fef1:2974/64 Scope: Link
UP BROADCAST RUNNING MULTICAST MTU: 1500 Metric: 1
RX packets: 88 errors: 0 dropped: 0 overruns: 0 frame: 0
TX packets: 57 errors: 0 dropped: 0 overruns: 0 carrier: 0
Collisions: 0 txqueuelen: 1000
RX bytes: 12266 (12.2 KB) TX bytes: 9052 (9.0 KB)
Now I am thinking, packets in queue= RX packets-TX packets=88-57=31packets (31 packets are in the buffer). Am I thinking in the right direction?
For “ifconfig” kindly check the following link

[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-542055)
  15. ![](https://secure.gravatar.com/avatar/22d992e64115671cd12ca79e85ace4ed3890107add00a6037da50ec094698842?s=50&d=blank&r=g)
Pankhuri Jaiswal
[ November 20, 2014 at 3:29 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-378010)
hello!!
M in a deep trouble…i need to do this tcp steganography in linux environment…can you please tell me the required steps and commands…i need it urgent…please help
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-378010)
     * ![](https://secure.gravatar.com/avatar/82a043deb904edf994f4928a423ba5669951299ad7e6bb6121bb38d212f157ee?s=50&d=blank&r=g)
Mohinder
[ November 3, 2015 at 6:35 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-700241)
Pankhuri,
Please let us know how the steganography went. What commands did you find useful and what was the end result. Thank you and very good day to you.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-700241)
  16. ![](https://secure.gravatar.com/avatar/aee9bc6e05667ef3a8d67086f434b5970e2d223e13d7f6a63f26da6ab19f0303?s=50&d=blank&r=g)
techie
[ October 13, 2014 at 9:25 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-332020)
Thanx, very informative
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-332020)
  17. ![](https://secure.gravatar.com/avatar/5dade858e5c3d55c7b9efbac7433e0506376bfe8810ba43f89fe147af94c66b4?s=50&d=blank&r=g)
engineer5
[ July 23, 2014 at 2:35 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-221579)
Hello man, I have a question.
How to decode audio samples from pcap? or How to get audo samples which is transmitter over ethernet with AVB.
thank you.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-221579)
  18. ![](https://secure.gravatar.com/avatar/1d66cff063d1ba1a138077a25179259a5ccf97bd9655b008db1cc741ad4a8956?s=50&d=blank&r=g)
Deepak Kushwaha
[ June 15, 2014 at 1:50 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-192691)
Very informative
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-192691)
  19. ![](https://secure.gravatar.com/avatar/809df6e99f80a383c29d4f628d022916801b1bca974cc20b337432cf8dd85990?s=50&d=blank&r=g)
Sunil
[ February 25, 2014 at 12:07 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-126372)
Really this info was helpful. Nice work .
Keep Up !
Thanks
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-126372)
  20. ![](https://secure.gravatar.com/avatar/9bfd6038e305e5dc9bbefbb26650f95e89309111804997938f98b71684ebb989?s=50&d=blank&r=g)
Murat
[ February 22, 2014 at 12:44 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-124938)
Thanks man. This is one of the most useful references I found about tcpdump.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-124938)
  21. ![](https://secure.gravatar.com/avatar/fe34562ef76903b77ac346674a158651c2acc786ab9da01049e86da75e7b7ae8?s=50&d=blank&r=g)
skullquake
[ January 24, 2014 at 9:07 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-112394)
Thanks for teaching us the basics!
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-112394)
  22. ![](https://secure.gravatar.com/avatar/0f7ba25024f9adec9d714ee3aaad24f97dcce8dbdc2073672d1d43479d05a8d7?s=50&d=blank&r=g)
abhi
[ January 4, 2014 at 9:06 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-99869)
it is telling
E:could not open lock file/var/lib/dpkg/lock -open(13: permission denied)
how to open lock
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-99869)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 4, 2014 at 2:49 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-100059)
You must use sudo to give permission to perform tasks.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-100059)
  23. ![](https://secure.gravatar.com/avatar/191c824016c5df0de3ac87d4a7dfb868f63f73313c0ed04d08eee15c63bd573f?s=50&d=blank&r=g)
Alon
[ January 2, 2014 at 2:30 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-98514)
Simple and stupid examples,
What about logical operators use like OR AND etc.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-98514)
  24. ![](https://secure.gravatar.com/avatar/de85a8685b4090468d9dc07ef94e0a681aad35cea240f5f34e4c0add904cebe6?s=50&d=blank&r=g)
Manish
[ November 19, 2013 at 11:15 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-72926)
can i get only the mac address of wireless devices (such as smart phones) through some shell commands. and can i run that shell script on the Access point to send me information every minute or second.
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-72926)
  25. ![](https://secure.gravatar.com/avatar/1d83dcebab1a867b6a88a6f099059ced1182545dee0eebd212e1be20b463e5a6?s=50&d=blank&r=g)
sagar
[ October 9, 2013 at 2:03 pm  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-55567)
It is very helpful for student like me.
Thank you
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-55567)
  26. ![](https://secure.gravatar.com/avatar/a237ebab824b7e66a70386a97f6edb12afa4f7dd303228548e76b29557ec6ed2?s=50&d=blank&r=g)
Vikas
[ March 18, 2013 at 11:51 am  ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-24133)
Very nice article !!
[Reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#comment-24133)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
## Upgrade Your Linux Learning with Pro.Tecmint
**If you find TecMint helpful** , consider supporting us by subscribing to [**Pro.Tecmint.com**](https://pro.tecmint.com) – our premium platform with exclusive guides, ad-free experience, early access to tutorials, and much more.

Your support helps us keep creating quality Linux content for everyone.
[ Get Lifetime Access ](https://pro.tecmint.com)
## Linux Commands and Tools
[12 Practical Examples of Linux Xargs Command for Beginners](https://www.tecmint.com/xargs-command-examples/)
[sysget – A Front-end for Every Package Manager in Linux](https://www.tecmint.com/sysget-front-end-package-manager-in-linux/)
[10 Little-Known Linux Commands You Probably Missed – Part 5](https://www.tecmint.com/10-lesser-known-useful-linux-commands-part-v/)
[How to Optimize and Compress JPEG or PNG Images in Linux Commandline](https://www.tecmint.com/optimize-and-compress-jpeg-or-png-batch-images-linux-commandline/)
[How to Show Asterisks While Typing Sudo Password in Linux](https://www.tecmint.com/show-asterisks-sudo-password-in-linux/)
[How to Disable ‘su’ Access for Sudo Users](https://www.tecmint.com/disable-su-access-sudo-users/)
## Linux Server Monitoring Tools
[Iotop – Monitor Linux Disk I/O Activity and Usage Per-Process Basis](https://www.tecmint.com/iotop-monitor-linux-disk-io-activity-per-process/)
[10 Strace Commands for Troubleshooting and Debugging Linux Processes](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
[How to Install Zabbix on RHEL/CentOS and Debian/Ubuntu – Part 1](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/)
[How to Install LibreNMS Monitoring Tool on Debian 11/10](https://www.tecmint.com/install-librenms-debian/)
[Petiti – An Open Source Log Analysis Tool for Linux SysAdmins](https://www.tecmint.com/petiti-log-analysis-tool-for-linux-sysadmins/)
[ctop – Top-like Interface for Monitoring Docker Containers](https://www.tecmint.com/ctop-monitor-docker-containers/)
## Learn Linux Tricks & Tips
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
[7 Ways to Determine the File System Type in Linux (Ext2, Ext3 or Ext4)](https://www.tecmint.com/find-linux-filesystem-type/)
[How to Upload or Download Files/Directories Using sFTP in Linux](https://www.tecmint.com/sftp-upload-download-directory-in-linux/)
[4 Useful Tips on mkdir, tar and kill Commands in Linux](https://www.tecmint.com/mkdir-tar-and-kill-commands-in-linux/)
[Tips to Create ISO from CD, Watch User Activity and Check Memory Usages of Browser](https://www.tecmint.com/creating-cdrom-iso-image-watch-user-activity-in-linux/)
[How To Assign Output of a Linux Command to a Variable](https://www.tecmint.com/assign-linux-command-output-to-variable/)
## Best Linux Tools
[9 Best Free UPnP and DLNA Servers for Linux in 2024](https://www.tecmint.com/upnp-dlna-media-servers-linux/)
[15 Best Kali Linux Web Penetration Testing Tools](https://www.tecmint.com/kali-linux-web-penetration-testing-tools/)
[13 Most Used Microsoft Office Alternatives for Linux](https://www.tecmint.com/microsoft-office-alternatives-for-linux/)
[8 Best Open Source Web Servers in 2024](https://www.tecmint.com/best-open-source-web-servers/)
[8 Useful Linux Security Features and Tools for Beginners](https://www.tecmint.com/linux-security-features-and-tools/)
[6 Best Whiteboard Applications for Your Linux Systems](https://www.tecmint.com/linux-whiteboard-applications/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)![](https://secure.adnxs.com/getuid?https://ids.ad.gt/api/v1/match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&adnxs_id=$UID&gdpr=0)![](https://u.openx.net/w/1.0/cm?id=998eaf06-9905-4eae-9e26-9fac75960c53&r=https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Fopenx%3Fopenx_id%3D%7BOPENX_ID%7D%26id%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q%26auid%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://image2.pubmatic.com/AdServer/UCookieSetPug?rd=https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Fpbm_match%3Fpbm%3D%23PM_USER_ID%26id%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://token.rubiconproject.com/token?pid=50242&puid=AU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://match.adsrvr.org/track/cmf/generic?ttd_pid=8gkxb6n&ttd_tpi=1&ttd_puid=AU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://pixel.tapad.com/idsync/ex/receive?partner_id=3185&partner_device_id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&partner_url=https://ids.ad.gt%2Fapi%2Fv1%2Ftapad_match%3Fid%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q%26tapad_id%3D%24%7BTA_DEVICE_ID%7D&gdpr=0)![](https://cm.g.double-click.net/pixel?google_cm&google_nid=audigent_dmp&google_hm=QVUxRC0wMTAwLTAwMTc3Mjk0OTc1MC1YWE0yRkkxSC1TRzJR&id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://d.turn.com/r/dd/id/L2NzaWQvMS9jaWQvMTc0ODI0MTY1OC90LzA/url/https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Famo_match%3Fturn_id%3D%24!{TURN_UUID}%26id%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q)![](https://sync.go.sonobi.com/us?https://ids.ad.gt/api/v1/son_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&uid=\[UID\]&gdpr=0)![](https://ad.360yield.com/ux?&publisher_dmp_id=15&r=https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Fimpr_match%3Fid%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q%26impr_uid%3D%7BPUB_USER_ID%7D&gdpr=0)
