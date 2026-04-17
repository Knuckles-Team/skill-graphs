[Skip to content](https://www.tecmint.com/configure-iptables-firewall/#content "Skip to content")
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
Menu
  * [Learn Linux](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/ "Start Learning Linux")
  * [Linux Distros](https://www.tecmint.com/best-linux-distributions/ "Linux Distributions")
    * [Linux Distros for Beginners](https://www.tecmint.com/best-linux-distributions-for-beginners/)
    * [Linux Distros for Experts](https://www.tecmint.com/linux-distro-for-power-users/ "Widely Used Distros")
    * [New Linux Distros](https://www.tecmint.com/new-linux-distributions/)
    * [Linux Server Distros](https://www.tecmint.com/10-best-linux-server-distributions/)
    * [Secure Linux Distros](https://www.tecmint.com/best-security-centric-linux-distributions/)
    * [CentOS Alternatives](https://www.tecmint.com/centos-alternative-distributions/ "CentOS Alternative Distros")
    * [RedHat Distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat Based Distros")
    * [Debian Distributions](https://www.tecmint.com/debian-based-linux-distributions/ "Debian Based Distros")
    * [Ubuntu Distributions](https://www.tecmint.com/ubuntu-based-linux-distributions/ "Ubuntu Based Distros")
    * [Arch Linux Distros](https://www.tecmint.com/arch-based-linux-distributions/ "Arch Linux Based Distros")
    * [Rolling Linux Distros](https://www.tecmint.com/best-rolling-release-linux-distributions/)
    * [KDE Linux Distros](https://www.tecmint.com/best-linux-distributions-for-kde-plasma/ "KDE Based Distros")
    * [Linux Distros for Old PC](https://www.tecmint.com/linux-distributions-for-old-computers/ "Linux Distros for Older Computers")
    * [Linux Distros for Kids](https://www.tecmint.com/best-linux-distributions-for-kids/)
    * [Linux Distributions for Students](https://www.tecmint.com/linux-distros-students/)
    * [Linux Distros for Windows](https://www.tecmint.com/best-alternative-linux-distributions-for-windows-users/)
  * [Commands](https://www.tecmint.com/category/linux-commands/ "Linux Commands")
    * [A – Z Linux Commands](https://www.tecmint.com/linux-commands-cheat-sheet/)
    * [100+ Linux Commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands")
  * [Tools](https://www.tecmint.com/category/top-tools/ "Best Linux Software")
  * [Pro Courses](https://www.tecmint.com/configure-iptables-firewall/ "Linux Online Courses")
    * [Bash Scripting](https://pro.tecmint.com/learn-bash-scripting/ "Bash Scripting for Beginners")
    * [Learn Linux](https://pro.tecmint.com/learn-linux/ "Master Linux in 7 Days")
    * [AI for Linux](https://pro.tecmint.com/ai-for-linux/ "AI for Linux Course")
    * [RHCSA Certification](https://pro.tecmint.com/rhcsa-certification-course/ "RHCSA Certification Course")
    * [RHCE Certification](https://pro.tecmint.com/rhce-certification-course/ "RHCE Certification Course")
    * [LFCS Certification](https://pro.tecmint.com/lfcs-certification-course/ "LFCS Certification Course")
  *     * [RHCSA Exam](https://www.tecmint.com/rhcsa-exam-reviewing-essential-commands-system-documentation/ "RHCSA Certification eBook")
    * [RHCE Exam](https://www.tecmint.com/how-to-setup-and-configure-static-network-routing-in-rhel/ "RHCE Certification eBook")
    * [LFCS Exam](https://www.tecmint.com/sed-command-to-create-edit-and-manipulate-files-in-linux/ "LFCS Certification eBook")
    * [LFCE Exam](https://www.tecmint.com/installing-network-services-and-configuring-services-at-system-boot/ "LFCE Certification eBook")
    * [LFCA Exam](https://www.tecmint.com/understanding-linux-operating-system/ "LFCA Certification eBook")
    * [Ansible Exam](https://www.tecmint.com/understand-core-components-of-ansible/ "Ansible Certification eBook")
  * [About](https://www.tecmint.com/who-we-are/)
    * [Contact](https://www.tecmint.com/contact-us/ "Contact Us")
    * [Hiring](https://www.tecmint.com/hiring/ "Write for Us")
    * [Newsletter](https://www.tecmint.com/subscribe-to-blog/ "Linux Weekly Newsletter")
    * [Testimonials](https://www.tecmint.com/testimonials/)
    * [Donate](https://www.tecmint.com/donate-to-tecmint/ "Support TecMint")
    * [Advertise](https://www.tecmint.com/advertise/ "TecMint Sponsorship Opportunities")
    * [Submit Article Request](https://www.tecmint.com/submit-article-request/)
    * [Suggest an Update](https://www.tecmint.com/suggest-an-update/)


[](https://www.tecmint.com/configure-iptables-firewall/)
_
**Note** : The **Linux Foundation Certified Engineer** (**LFCE**) exam was officially retired on May 1, 2022. If you are preparing for certification, we recommend pursuing the [Linux Foundation Certified System Administrator (LFCS)](https://pro.tecmint.com/lfcs-certification-course/ "Linux Foundation Certified System Administrator \(LFCS\)") exam instead.
_
You will recall from [Part 1 – About Iptables](https://www.tecmint.com/installing-network-services-and-configuring-services-at-system-boot/) of this **LFCE** (**Linux Foundation Certified Engineer​**) series that we gave a basic description of what a firewall is: a mechanism to manage packets coming into and leaving the network. By “manage” we actually mean:
  1. To allow or prevent certain packets to enter or leave our network.
  2. To forward other packets from one point of the network to another.


based on predetermined criteria.
In this article we will discuss how to implement basic packet filtering and how to configure the firewall with iptables, a frontend to netfilter, which is a native kernel module used for firewalling.
Please note that firewalling is a vast subject and this article is not intended to be a comprehensive guide to understanding all that there is to know about it, but rather as a starting point for a deeper study of this topic. However, we will revisit the subject in **Part 10** of this series when we explore a few specific use cases of a firewall in Linux.
You can think of a firewall as an international airport where passenger planes come and go almost 24/7. Based on a number of conditions, such as the validity of a person’s passport, or his / her country of origin (to name a few examples) he or she may, or may not, be allowed to enter or leave a certain country.
At the same time, airport officers can instruct people to move from one place of the airport to another if necessary, for example when they need to go through Customs Services.
We may find the airport analogy useful during the rest of this tutorial. Just keep in mind the following relations as we proceed:
  1. Persons = Packets
  2. Firewall = Airport
  3. Country #1 = Network #1
  4. Country #2 = Network #2
  5. Airport regulations enforced by officers = firewall rules


### Iptables – The Basics
At the low level, it is the kernel itself which “**decides** ” what to do with packets based on rules grouped in **chains** , or **sentences**. These chains define what actions should be taken when a package matches the criteria specified by them.
The first action taken by iptables will consist in deciding what to do with a packet:
  1. Accept it (let it go through into our network)?
  2. Reject it (prevent it from accessing our network)?
  3. Forward it (to another chain)?


Just in case you were wondering why this tool is called **iptables** , it’s because these chains are organized in tables, with the **filter table** being the most well know and the one that is used to implement packet filtering with its three default chains:
**1.** The **INPUT** chain handles packets coming into the network, which are destined for local programs.
**2.** The **OUTPUT** chain is used to analyze packets originated in the local network, which are to be sent to the outside.
**3.** The **FORWARD** chain processes the packets which should be forwarded to another destination (as in the case of a router).
For each of these chains there is a default policy, which dictates what should be done by default when packets do not match any of the rules in the chain. You can view the rules created for each chain and the default policy by running the following command:
```
# iptables -L

```

The available policies are as follows:
  1. **ACCEPT** → lets the packet through. Any packet that does not match any rules in the chain is allowed into the network.
  2. **DROP** → drops the packet quietly. Any packet that does not match any rules in the chain is prevented from entering the network.
  3. **REJECT** → rejects the packet and returns an informative message. This one in particular does not work as a default policy. Instead, it is meant to complement packet filtering rules.

![Linux Firewall Policies](https://www.tecmint.com/wp-content/uploads/2015/01/Iptables-Policies-620x340.png)Linux Iptables Policies
When it comes to deciding which policy you will implement, you need to consider the **pros** and **cons** of each approach as explained above – note that there is no one-size-fits-all solution.
#### Adding Rules
To add a rule to the firewall, invoke the iptables command as follows:
```
# iptables -A chain_name criteria -j target

```

where,
  1. **-A** stands for Append (append the current rule to the end of the chain).
  2. **chain_name** is either INPUT, OUTPUT, or FORWARD.
  3. **target** is the action, or policy, to apply in this case (ACCEPT, REJECT, or DROP).
  4. **criteria** is the set of conditions against which the packets are to be examined. It is composed of at least one (most likely more) of the following flags. Options inside brackets, separated by a vertical bar, are equivalent to each other. The rest represents optional switches:

```
**[--protocol | -p] protocol**: specifies the protocol involved in a rule.
**[--source-port | -sport] port:[port]**: defines the port (or range of ports) where the packet originated.
**[--destination-port | -dport] port:[port]**: defines the port (or range of ports) to which the packet is destined.
**[--source | -s] address[/mask]**: represents the source address or network/mask.
**[--destination | -d] address[/mask]**: represents the destination address or network/mask.
**[--state] state** (preceded by **-m** state): manage packets depending on whether they are part of a state connection, where state can be NEW, ESTABLISHED, RELATED, or INVALID.
**[--in-interface | -i] interface**: specifies the input interface of the packet.
**[--out-interface | -o] interface**: the output interface.
**[--jump | -j] target**: what to do when the packet matches the rule.

```

#### Our Testing Environment
Let’s glue all that in 3 classic examples using the following test environment for the first two:
```
Firewall: Debian Wheezy 7.5
Hostname: dev2.gabrielcanepa.com
IP Address: 192.168.0.15

```
```
Source: CentOS 7
Hostname: dev1.gabrielcanepa.com
IP Address: 192.168.0.17

```

And this for the last example
```
NFSv4 server and firewall: Debian Wheezy 7.5
Hostname: debian
IP Address: 192.168.0.10

```
```
Source: Debian Wheezy 7.5
Hostname: dev2.gabrielcanepa.com
IP Address: 192.168.0.15

```

###### EXAMPLE 1: Analyzing the difference between the DROP and REJECT policies
We will define a **DROP** policy first for input pings to our firewall. That is, icmp packets will be dropped quietly.
```
# ping -c 3 192.168.0.15

```
```
# iptables -A INPUT --protocol icmp --in-interface eth0 -j DROP

```
![Linux Iptables Block ICMP Ping](https://www.tecmint.com/wp-content/uploads/2015/01/Drop-Icmp-in-Firewall-620x172.png)Drop ICMP Ping Request
Before proceeding with the **REJECT** part, we will flush all rules from the INPUT chain to make sure our packets will be tested by this new rule:
```
# iptables -F INPUT
# iptables -A INPUT --protocol icmp --in-interface eth0 -j REJECT

```
```
# ping -c 3 192.168.0.15

```
![Reject ICMP Ping Request in Linux](https://www.tecmint.com/wp-content/uploads/2015/01/Reject-Icmp-in-Firewall-620x295.png)Reject ICMP Ping Request in Firewall
###### EXAMPLE 2: Disabling / re-enabling ssh logins from dev2 to dev1
We will be dealing with the **OUTPUT** chain as we’re handling outgoing traffic:
```
# iptables -A OUTPUT --protocol tcp --destination-port 22 --out-interface eth0 --jump REJECT

```
![Block SSH Login in Linux Firewall](https://www.tecmint.com/wp-content/uploads/2015/01/Disable-SSH-Login-in-Firewall-620x116.png)Block SSH Login in Firewall
###### EXAMPLE 3: Allowing / preventing NFS clients (from 192.168.0.0/24) to mount NFS4 shares
Run the following commands in the NFSv4 server / firewall to close ports 2049 and 111 for all kind of traffic:
```
# iptables -F
# iptables -A INPUT -i eth0 -s 0/0 -p tcp --dport 2049 -j REJECT
# iptables -A INPUT -i eth0 -s 0/0 -p tcp --dport 111 -j REJECT

```
![Block NFS Port in Linux Firewall](https://www.tecmint.com/wp-content/uploads/2015/01/Reject-NFS-Ports-in-Firewall-620x202.png)Block NFS Ports in Firewall
Now let’s open those ports and see what happens.
```
# iptables -A INPUT -i eth0 -s 0/0 -p tcp --dport 111 -j ACCEPT
# iptables -A INPUT -i eth0 -s 0/0 -p tcp --dport 2049 -j ACCEPT

```
![Open NFS Ports in Firewall](https://www.tecmint.com/wp-content/uploads/2015/01/Open-NFS-Ports-in-Firewall-620x106.png)Open NFS Ports in Firewall
As you can see, we were able to mount the NFSv4 share after opening the traffic.
#### Inserting, Appending and Deleting Rules
In the previous examples we showed how to append rules to the **INPUT** and **OUTPUT** chains. Should we want to insert them instead at a predefined position, we should use the **-I** (uppercase i) switch instead.
You need to remember that rules will be evaluated one after another, and that the evaluation stops (or jumps) when a **DROP** or **ACCEPT** policy is matched. For that reason, you may find yourself in the need to move rules up or down in the chain list as needed.
We will use a trivial example to demonstrate this:
![Check Linux Iptables Rules](https://www.tecmint.com/wp-content/uploads/2015/01/List-Iptables-Rules-620x137.png)Check Rules of Iptables Firewall
Let’s place the following rule,
```
# iptables -I INPUT 2 -p tcp --dport 80 -j ACCEPT

```

at position 2) in the INPUT chain (thus moving previous #2 as #3)
![Linux Iptables Accept Rule](https://www.tecmint.com/wp-content/uploads/2015/01/Iptables-Accept-Rule-620x149.png)Iptables Accept Rule
Using the setup above, traffic will be checked to see whether it’s directed to port **80** before checking for port **2049**.
Alternatively, you can delete a rule and change the target of the remaining rules to **REJECT** (using the **-R** switch):
```
# iptables -D INPUT 1
# iptables -nL -v --line-numbers
# iptables -R INPUT 2 -i eth0 -s 0/0 -p tcp --dport 2049 -j REJECT
# iptables -R INPUT 1 -p tcp --dport 80 -j REJECT

```
![Linux Iptables Drop Rule](https://www.tecmint.com/wp-content/uploads/2015/01/Iptables-Drop-Rule-620x427.png)Iptables Drop Rule
Last, but not least, you will need to remember that in order for the firewall rules to be persistent, you will need to save them to a file and then restore them automatically upon boot (using the preferred method of your choice or the one that is available for your distribution).
Saving firewall rules:
```
# iptables-save > /etc/iptables/rules.v4		[On Ubuntu]
# iptables-save > /etc/sysconfig/iptables		[On CentOS / OpenSUSE]

```

Restoring rules:
```
# iptables-restore < /etc/iptables/rules.v4		[On Ubuntu]
# iptables-restore < /etc/sysconfig/iptables		[On CentOS / OpenSUSE]

```

Here we can see a similar procedure (saving and restoring firewall rules by hand) using a dummy file called **iptables.dump** instead of the default one as shown above.
```
# iptables-save > iptables.dump

```
![Save Iptables Rules in Linux](https://www.tecmint.com/wp-content/uploads/2015/01/Dump-Iptables-Rules-620x297.png)Dump Linux Iptables
To make these changes persistent across boots:
**Ubuntu** : Install the **iptables-persistent** package, which will load the rules saved in the **/etc/iptables/rules.v4** file.
```
# apt-get install iptables-persistent

```

**CentOS** : Add the following 2 lines to **/etc/sysconfig/iptables-config** file.
```
IPTABLES_SAVE_ON_STOP="yes"
IPTABLES_SAVE_ON_RESTART="yes"

```

**OpenSUSE** : List allowed ports, protocols, addresses, and so forth (separated by commas) in **/etc/sysconfig/SuSEfirewall2**.
For more information refer to the file itself, which is heavily commented.
### Conclusion
The examples provided in this article, while not covering all the bells and whistles of iptables, serve the purpose of illustrating how to enable and disable traffic incoming or outgoing traffic.
For those of you who are firewall fans, keep in mind that we will revisit this topic with more specific applications in **Part 10** of this **LFCE** series.
Feel free to let me know if you have any questions or comments.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Package PyGObject Applications and Programs as “.deb” Package for the Linux Desktop – Part 4](https://www.tecmint.com/package-pygobject-applications-as-deb-package/)
Next article:
[How to Monitor System Usage, Outages and Troubleshoot Linux Servers – Part 9](https://www.tecmint.com/linux-system-monitoring-troubleshooting-tools/)
![Photo of author](https://secure.gravatar.com/avatar/27b3ea2a3fb1de4ed1c8694a1465c099a86586d8b833a0d852a26d76d750df9f?s=100&d=blank&r=g)
Gabriel Cánepa
Gabriel Cánepa is a GNU/Linux sysadmin and web developer from Villa Mercedes, San Luis, Argentina. He works for a worldwide leading consumer product company and takes great pleasure in using FOSS tools to increase productivity in all areas of his daily work.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/configure-iptables-firewall/#respond)** or
## Related Posts
[![Audit Linux Systems](https://www.tecmint.com/wp-content/uploads/2015/01/Audit-Linux-Systems.jpg)](https://www.tecmint.com/audit-network-performance-security-and-troubleshooting-in-linux/ "How to Audit Network Performance, Security, and Troubleshooting in Linux – Part 12")
[![Setup Yum Local Repository in CentOS 7](https://www.tecmint.com/wp-content/uploads/2015/01/Network-Repository-in-Linux.jpg)](https://www.tecmint.com/setup-yum-repository-in-centos-7/ "How to Setup a Network Repository to Install or Update Packages – Part 11")
[![Configure Linux as Router](https://www.tecmint.com/wp-content/uploads/2015/01/Configure-Linux-as-Router.jpg)](https://www.tecmint.com/setup-linux-as-router/ "How to Turn a Linux Server into a Router to Handle Traffic Statically and Dynamically – Part 10")
[![Monitor Linux Servers](https://www.tecmint.com/wp-content/uploads/2015/01/Monitor-Linux-Servers1.jpg)](https://www.tecmint.com/linux-system-monitoring-troubleshooting-tools/ "How to Monitor System Usage, Outages and Troubleshoot Linux Servers – Part 9")
[![Setting Up Postfix Mail Server](https://www.tecmint.com/wp-content/uploads/2014/12/part72.jpg)](https://www.tecmint.com/setting-up-email-services-smtp-and-restricting-access-to-smtp/ "Setting Up Email Services \(SMTP, Imap and Imaps\) and Restricting Access to SMTP – Part 7")
[![Configure SquidGuard for Squid](https://www.tecmint.com/wp-content/uploads/2014/12/part6.jpg)](https://www.tecmint.com/configure-squidguard-for-squid-proxy/ "Configuring SquidGuard, Enabling Content Rules and Analyzing Squid Logs – Part 6")
### 10 Comments
[Leave a Reply](https://www.tecmint.com/configure-iptables-firewall/#reply-title)
  1. Thank you! this guide helped me a lot – especially on the NAT part.
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-1387270)
  2. In image [https://www.tecmint.com/wp-content/uploads/2015/01/Iptables-Policies-620×340.png](https://www.tecmint.com/wp-content/uploads/2015/01/Iptables-Policies-620x340.png) it says “you can change the default policy for a specific chain only if that chain has been flushed of all its rules.” Is this true of all versions of iptables? The reason I ask is because I’ve found tutorials that add rules to the input chain (for SSH) and then later change the default INPUT policy to drop.
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-773597)
     * @Brody,
Have you been able to test this? Perhaps the most appropriate wording for the text in the image would have been “It is recommended that…”. To clear all doubts, please reply to this comment with the URLs you are referring to, and if possible, the distributions used.
Best,
Gabriel
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-773728)
       * I was following the tutorial for ubuntu 14.04 at
They change the default policy in the section titled “Implementing a Drop Rule.”
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-774095)
  3. so instead of iptables-persistent, wouldn’t it be easier/better to use ‘post-up iptables-restore < /path/to/iptables.txt' in the /etc/network/interfaces file on ubuntu?
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-514319)
     * @birdman,
If you know of a better alternative which works best for you, feel free to use it. Keep in mind that both the LFCS and the LFCE are performance-based, so you have the freedom to choose any tool / command you feel for comfortable with as long as it gets the job done.
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-564436)
  4. I failed the Exam cause at the End i made a stupid Failure and flush my iptables-Rules and had no Backup to restore them. That costs me round about 30% i think
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-496181)
     * @Riot,
I am sorry to hear that. However, thanks for letting us know so other readers will be aware of that fact and take the necessary precautions when they take the exam. Good luck next time!
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-500535)
  5. Kindly do correct “packages” to “packet” in your article. Since you mean to say packets throught the article.
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-456894)
     * @Arun,
Thanks a ton and we are very sorry for such typos….corrected in the write up….
[Reply](https://www.tecmint.com/configure-iptables-firewall/#comment-457628)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/configure-iptables-firewall/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/configure-iptables-firewall/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=2291458542159063&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
