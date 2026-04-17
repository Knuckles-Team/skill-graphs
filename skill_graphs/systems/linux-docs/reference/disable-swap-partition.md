[Skip to content](https://www.tecmint.com/disable-swap-partition/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/disable-swap-partition/ "Linux Online Courses")
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


[](https://www.tecmint.com/disable-swap-partition/)
Swapping or swap space represents a physical memory page that lives on top of a [disk partition or a special disk file](https://www.tecmint.com/everything-is-file-and-types-of-files-linux/ "Everything is a File in Linux") used for extending the RAM memory of a system when the physical memory fills up.
Using this method of extending RAM resources, inactive memory pages are frequently dumped into the swap area when no RAM is available. However, due to the spinning speed of classical hard disks, swap space is way lower in transfer speeds and access time compared to RAM.
On newer machines with fast SSD hard disks, reserving a small partition for swapping can greatly improve access time and speed transfer compared to classical HDD, but the speed is still magnitudes lower than RAM memory.
Some suggest that the swap space should be set as twice the amount of machine RAM. However, on systems with more than 4 GB of RAM, swap space should be set between **2** or **4** GB.
In case your server has sufficient RAM memory or does not require the use of swap space or the swapping greatly decreases your system performance, you should consider disabling the swap area.
## How to Check Swap Space in Linux
Before actually disabling swap space, first, you need to [visualize your memory load degree](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find Running Processes by Memory Usage") and then identify the partition that holds the swap area, by issuing the below [free command](https://www.tecmint.com/check-memory-usage-in-linux/ "Linux free Command").
```
# free -h

```

Look for the Swap space used size. If the used size is **0B** or close to **0** bytes, it can be assumed that swap space is not used intensively and can be safely disabled.
![Check Swap Space](https://www.tecmint.com/wp-content/uploads/2017/12/Check-Swap-Space.png)Check Swap Space
## How to Check Swap Partition in Linux
Next, issue following the **blkid command** , look for `TYPE="swap"` line in order to identify the swap partition, as shown in the below screenshot.
```
# blkid

```
![Check Swap Partition Type](https://www.tecmint.com/wp-content/uploads/2017/12/Check-Swap-Partition-Type.png)Check Swap Partition Type
Again, issue the following [lsblk command](https://www.tecmint.com/commands-to-collect-system-and-hardware-information-in-linux/ "Find Hardware Info in Linux") to search and identify the `[SWAP]` partition as shown in the below screenshot.
```
# lsblk

```
![Search Confirm Swap Partition](https://www.tecmint.com/wp-content/uploads/2017/12/Search-Confirm-Swap-Partition.png)Search Confirm Swap Partition
## How to Disable Swap in Linux
After you’ve identified the swap partition or file, execute the below command to deactivate the swap area.
```
# swapoff /dev/mapper/centos-swap

```

Or disable all swaps from **/proc/swaps** , which provides a snapshot of the swap file name.
```
# swapoff -a

```

Run [free command](https://www.tecmint.com/check-memory-usage-in-linux/) in order to check if the swap area has been disabled.
```
# free -h

```
![Disable Swap Partition](https://www.tecmint.com/wp-content/uploads/2017/12/Disable-Swap-Partition.png)Disable Swap Partition
## How to Disable Swap Permanently in Linux
In order to permanently disable swap space in Linux, open **/etc/fstab** file, search for the swap line and comment on the entire line by adding a `#` (hashtag) sign in front of the line, as shown in the below screenshot.
```
# vi /etc/fstab

```
![Disable Swap Partition Permanently](https://www.tecmint.com/wp-content/uploads/2017/12/Disable-Swap-Partition-Permanently.png)Disable Swap Partition Permanently
Afterward, **reboot** the system in order to apply the new swap setting or issue `mount -a` command in some cases might do the trick.
```
# mount -a

```

After the system reboot, issuing the commands presented at the beginning of this tutorial should reflect that the swap area has been completely and permanently disabled in your system.
```
# free -h
# blkid
# lsblk

```

**You might also like:**
  * [How to Add Swap Space on Ubuntu Linux](https://www.tecmint.com/add-swap-space-on-ubuntu/ "Add Swap Space on Ubuntu Linux")
  * [How To Create a Linux Swap File](https://www.tecmint.com/create-a-linux-swap-file/ "Create a Linux Swap File")
  * [How to Clear RAM Memory Cache, Buffer, and Swap Space on Linux](https://www.tecmint.com/clear-ram-memory-cache-buffer-and-swap-space-on-linux/ "Clear RAM and Swap on Linux")
  * [How to Monitor Swap Space Usage in Linux](https://www.tecmint.com/commands-to-monitor-swap-space-usage-in-linux/ "Monitor Swap Space Usage in Linux")


💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[iPerf3 – Test Network Speed/Throughput in Linux](https://www.tecmint.com/test-network-throughput-in-linux/)
Next article:
[RedHat vs Debian: Administrative Point of View in 2023](https://www.tecmint.com/redhat-vs-debian/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/disable-swap-partition/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 10 Comments
[Leave a Reply](https://www.tecmint.com/disable-swap-partition/#reply-title)
  1. With modern PCs, sporting 8, 16, or more GB of RAM, swap partition/file has become unnecessary. So, instead of just disabling it, delete it.
Granted that the gain in available space will be minimal but deleting swap will leave one less partition to be possibly corrupted.
One caveat with deleting swap is that some distros may refuse to install unless some kind of swap is present.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-2064001)
     * @dragonmouth,
Thank you for sharing your perspective on the topic of swap partitions/files in the context of modern PCs with ample RAM. You’re right that with the increasing amounts of RAM in today’s computers, the traditional role of swap as an “overflow” for RAM is less critical than it once was.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-2068552)
  2. I’ve been told that “**swap space** ” is used during **SUSPEND** operations.
I welcome someone to offer a robust explanation. It is important for road warriors and any who rely on laptop portability.
During “**sleep** ” [suspend to ram] current runtime details get written to swap before putting things on hold.
During “**hibernate** ” [suspend to disk] the majority of the system state gets written to swap before power off.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-2013232)
  3. The “**free -h** ” commands must be executed when the system is under heavy load. Otherwise, it does not provide the information necessary to determine whether a swap partition or space is needed. When executed on an idling system, the command will only tell you the size of the swap partition and that it is not being used. It’s like running the “**top** ” command on an idling system to see the CPU Load. It will show the CPU Load to be negligible.
I agree with S. Daniels on the use of GParted. It not only provides a visual representation of your disks but also can delete your swap partition and recover that space by moving and/or resizing other partitions. Using the command line to accomplish your tasks may be ‘leet’ and cool but it is also dangerous to the health of your system. Using GParted prevents misspelling or use of incorrect CLI commands, as well as the use of incorrect options which can result in making the drive unusable.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-1611203)
  4. These instructions are rather outdated for any linux with a desktop:MATE, xfce, Gnome or KDE/Plasma. Firstly, the program Gparted very nicely displays swap size, location and UUID. “blkid”, especially on a dual-boot or system with multiple OSes is just going to display a lot of confusing and unhelpful entries.
The KDE partitioner is inferior, but adequate. The centos-swap is fairly specific to CentOS Linux, this should be explained in the article. A swap file can also be used in place of a dedicated partition, this should also be mentioned.
“Vi” is very much overkill for editing fstab. “Vim” is easier than “vi” for newbies in every case, and “pico /etc/fstab” or “nano /etc/fstab” are more appropriate here.
Finally, for José , 30GB is seriously wrong. I suspect he somehow changed a data or system partition into a swap partition. He can “manage flags in Gparted” to inspect it for contents.
I’m just a hobbyist, but have nearly 20 years experience, since a Debian bootable CD, the first Linux installation disk that did not need a floppy to boot, came out in 2000.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-1011820)
     * I followed these instructions and worked.
what’s your better solution?
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-1397026)
       * If you notice, S.Daniels wrote “**outdated** “, he did not write “**does not work** “.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-2011570)
  5. You can shrink the swap partition to a smaller size. 30G of swap is kind of large file or partition for swapping.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-954754)
  6. If there is sufficient RAM (8GB), computer may never access swap space. What is the benefit of disabling swap in this case? Conversely, how will swap cause problems if the computer never accesses it.
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-953387)
  7. In my case, I have 30 GB. free 0 GB. I should not disable?
total used free shared buff/cache available
Memoria: 7.7G 1.6G 4.6G 196M 1.5G 5.6G
Swap—–: 30G 0B 30G
[Reply](https://www.tecmint.com/disable-swap-partition/#comment-952733)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/disable-swap-partition/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/disable-swap-partition/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=5595948299953536&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
