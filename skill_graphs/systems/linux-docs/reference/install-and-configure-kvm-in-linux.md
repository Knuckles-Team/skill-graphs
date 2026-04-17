[Skip to content](https://www.tecmint.com/install-and-configure-kvm-in-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/install-and-configure-kvm-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-and-configure-kvm-in-linux/)
![Install and Configure KVM in CentOS](https://www.tecmint.com/wp-content/uploads/2015/01/Install-and-Configure-KVM-in-CentOS-620x297.jpg)Create Virtual Machines in Linux Using KVM – Part 1
This tutorial discusses KVM introduction, deployment and how to use it to create virtual machines under RedHat based-distributions such as **RHEL** /**CentOS7** and **Fedora 21**.
#### What is KVM?
KVM or (Kernel-based Virtual Machine) is a full virtualization solution for Linux on Intel 64 and AMD 64 hardware that is included in the mainline Linux kernel since 2.6.20 and is stable and fast for most workloads.
#### KVM Features
There are many useful features and advantages which you will gain when you use KVM to deploy your virtual platform. KVM hypervisor supports following features:
  1. **Over-committing** : Which means allocating more virtualized CPUs or memory than the available resources on the system.
  2. **Thin provisioning** : Which allows the allocation of flexible storage and optimizes the available space for every guest virtual machine.
  3. **Disk I/O throttling** : Provides the ability to set a limit on disk I/O requests sent from virtual machines to the host machine.
  4. **Automatic NUMA balancing** : Improves the performance of applications running on NUMA hardware systems.
  5. **Virtual CPU hot add capability** : Provides the ability to increase processing power as needed on running virtual machines, without downtime.


This is our first on-going KVM (Kernel-based Virtual Machine) series, here we will going to cover following articles in part wise fashion.
**Part 1** : **How to Create Virtual Machines in Linux Using KVM (Kernel-based Virtual Machine)**
**Part 2** : [Deploy Virtual Machines using Network Install (HTTP, FTP and NFS) under KVM](https://www.tecmint.com/multiple-virtual-machine-installation-using-network-install-kvm/)
**Part 3** : [How to Manage KVM Storage Volumes and Pools for Virtual Machines](https://www.tecmint.com/manage-kvm-storage-volumes-and-pools/)
**Part 4** : [Managing KVM Virtual Environment using CLI Tools](https://www.tecmint.com/kvm-management-tools-to-manage-virtual-machines/)
#### Prerequisites
Make sure that your system has the hardware virtualization extensions: For Intel-based hosts, verify the CPU virtualization extension [**vmx**] are available using following command.
```
[root@server ~]# grep -e 'vmx' /proc/cpuinfo

```
![Check Virtualization Support](https://www.tecmint.com/wp-content/uploads/2015/01/Check-Virtualization-Support-620x35.png)Check Virtualization Support
For AMD-based hosts, verify the CPU virtualization extension [**svm**] are available.
```
[root@server ~]# grep -e 'svm' /proc/cpuinfo

```
![Check CPU Virtualization Support](https://www.tecmint.com/wp-content/uploads/2015/01/Check-CPU-Virtualization-Support-620x34.png)Check CPU Virtualization Support
If there is no output make sure that virtualization extensions is enabled in BIOS. Verify that KVM modules are loaded in the kernel “it should be loaded by default”.
```
[root@server ~]# lsmod | grep kvm

```

The output should contains **kvm_intel** for intel-based hosts or **kvm_amd** for amd-based hosts.
![Check KVM Kernel Module Support](https://www.tecmint.com/wp-content/uploads/2015/01/Check-KVM-Kernel-Module.png)Check KVM Kernel Module
Before starting , you will need the root account or non-root user with sudo privileges configured on your system and also make sure that your system is up-to-date.
```
[root@server ~]# yum update

```

Make sure that Selinux be in Permissive mode.
```
[root@server ~]# setenforce 0

```

### Step 1: KVM Installation and Deployment
**1.** We will install **qemu-kvm** and **qemu-img** packages at first. These packages provide the user-level KVM and disk image manager.
```
[root@server ~]# yum install qemu-kvm qemu-img

```

**2.** Now, you have the minimum requirement to deploy virtual platform on your host, but we also still have useful tools to administrate our platform such as:
  1. **virt-manager** provides a GUI tool to administrate your virtual machines.
  2. **libvirt-client** provides a CL tool to administrate your virtual environment this tool called virsh.
  3. **virt-install** provides the command “virt-install” to create your virtual machines from CLI.
  4. **libvirt** provides the server and host side libraries for interacting with hypervisors and host systems.


Let’s install these above tools using the following command.
```
[root@server ~]# yum install virt-manager libvirt libvirt-python libvirt-client

```

**3.** For RHEL/CentOS7 users, also still having additional package groups such as: Virtualization Client, Virtualization Platform and Virtualization Tools to install.
```
[root@server ~]#yum groupinstall virtualization-client virtualization-platform virtualization-tools

```

**4.** The virtualization daemon which manage all of the platform is “**libvirtd** ”. lets restart it.
```
[root@server ~]#systemctl restart libvirtd

```

**5.** After restarting the daemon, then check its status by running following command.
```
[root@server ~]#systemctl status libvirtd

```

##### Sample Output
```
libvirtd.service - Virtualization daemon
   Loaded: loaded (/usr/lib/systemd/system/libvirtd.service; enabled)
   Active: active (running) since Mon 2014-12-29 15:48:46 EET; 14s ago
 Main PID: 25701 (libvirtd)

```
![Check Libvirtd Status](https://www.tecmint.com/wp-content/uploads/2015/01/Check-Libvirtd-Status-620x122.png)Check Libvirtd Status
Now, lets switch to the next section to create our virtual machines.
### Step 2: Create VMs using KVM
As we mentioned early, we have some useful tools to manage our virtual platform and creating virtual machines. One of this tools called [**virt-manager**] which we use in the next section.
**6.** Although **virt-manager** is a GUI based tool, we also could launch/start it from terminal as well as from GUI.
```
[root@server ~]#virt-manager

```

##### Using GNOME
![Start Virtual Manager in GNOME](https://www.tecmint.com/wp-content/uploads/2015/01/Start-Virtual-Manager-in-GNOME-600x450.jpeg)Start Virtual Manager in GNOME
##### Using GNOME Classic
![Start Virtual Manager in GNOME Classic](https://www.tecmint.com/wp-content/uploads/2015/01/Start-Virtual-Manager-in-GNOME-Classic-600x450.jpeg)Start Virtual Manager in GNOME Classic
**7.** After starting the tool, this window will appear.
![Start Virtual Manager Window](https://www.tecmint.com/wp-content/uploads/2015/01/Start-Virtual-Manager-Window-425x450.png)Start Virtual Manager Window
**8.** By default you will find manager is connected directly to **localhost** , fortunately you could use the same tool to manage another host remotely. From “**File** ” tab, just select “**Add Connection** ” and this window will appear.
![Add Connection](https://www.tecmint.com/wp-content/uploads/2015/01/Add-Connection.png)Add Connection
Check “**Connect to remote host** ” option then provide **Hostname** /**IP** of the remote server. If you need establishing connection to the remote host at every time the manager starting, just check “**Auto Connect** ” option.
**9.** Let’s return to our localhost, before creating new virtual machine you should decide where will the files be stored?! in other words, you should create the **Volume Disk** (Virtual disk / Disk image ) for your virtual machine.
By Right clicking on localhost and selecting “**Details** ” and then select “**Storage** ” tab.
![VM Storage Details](https://www.tecmint.com/wp-content/uploads/2015/01/VM-Storage-Details-428x450.png)VM Storage Details ![VM Storage Volume](https://www.tecmint.com/wp-content/uploads/2015/01/VM-Storage-Volume-597x450.png)VM Storage Volume
**10.** Next, press “**New Volume** ” button, then enter the name of your new virtual disk (**Volume Disk**) and enter the size which you want/need in the “**Max Capacity** ” section.
![Create KVM VM Storage Disk](https://www.tecmint.com/wp-content/uploads/2015/01/Create-VM-Storage-Disk.png)Create VM Storage Disk
The allocation size is the actual size for your disk which will be allocated immediately from your physical disk after finishing the steps.
**Note** : This is an important technology in storage administration field which called “**thin provision** ”. It used to allocate the used storage size only, NOT all of available size.
For example, you created virtual disk with size **60G** , but you have used actually only **20G** , using this technology the allocated size from your physical hard disk will be **20G** not **60G**.
In another words the allocated physical size will by dynamically allocated depending on the actual used size. You could find more information in details at
**11.** You will note that a label of the new Volume Disk has been appeared in the list.
![VM Storage Label](https://www.tecmint.com/wp-content/uploads/2015/01/VM-Storage-Label-620x352.png)VM Storage Label
You should also notice the path of the new disk image (Volume Disk), by default it will be under **/var/lib/libvirt/images** , you can verify it using the following command.
```
[root@server Downloads]# ls -l /var/lib/libvirt/images
-rw-------. 1 root root 10737418240 Jan  3 16:47 vm1Storage.img

```

**12.** Now, we’re ready to create our virtual machine. Let’s hit the button “**VM** ” in the main window, this wizard window will be appear.
![Create New Virtual Machine in KVM](https://www.tecmint.com/wp-content/uploads/2015/01/Create-New-Virtual-Machine.png)Create New Virtual Machine
Select the installation method which you will use to create the virtual machine. For now we will use Local install media, later we will discuss the remaining methods.
**13.** Now its time to specify which Local install media to be used, we have two options:
  1. From physical [CDROM/DVD].
  2. From ISO image.


For our tutorial, lets use ISO image method, so you should provide the path of your ISO image.
![Select Installation Media](https://www.tecmint.com/wp-content/uploads/2015/01/Select-Installation-Media-431x450.png)Select Installation Media
**Important** : Unfortunately there’s a really silly bug for whom use RHEL/CentOS7. This bug prevents you from installation using physical [CDROM/DVD], you will find the option is grayed like this.
![Disabled CD DVD Rom in KVM](https://www.tecmint.com/wp-content/uploads/2015/01/Disabled-CD-DVD-Rom.png)Disabled CD DVD Rom in KVM
And if you hold your cursor on it, this error message will appear.
![CD DVD Not Supported in KVM](https://www.tecmint.com/wp-content/uploads/2015/01/CD-DVD-Not-Supported-457x450.png)CD DVD Not Supported in KVM
Until now there is no official/direct solution for this bug, you could find more information on the same at
**14.** The storage has return back, we will use the virtual disk which we have created early to install virtual machine on it. It will be as shown.
![Enable KVM Storage for Virtual Machine](https://www.tecmint.com/wp-content/uploads/2015/01/Enable-Storage-for-Virtual-Machine.png)Enable Storage for Virtual Machine
**15.** The final step which ask you about the name of your virtual machine and another advanced options lets talk about it later.
![Enter Name of Virtual Machine](https://www.tecmint.com/wp-content/uploads/2015/01/Enter-Name-of-Virtual-Machine-393x450.png)Enter Name of Virtual Machine
If you like to change some configuration or doing some customization just check “**Customize configuration before install** ” option. Then click **finish** and wait seconds, control console will appear for your Guest OS to manage it
![KVM Virtual Machine Installation](https://www.tecmint.com/wp-content/uploads/2015/01/Virtual-Machine-Installation-551x450.png)Virtual Machine Installation
### Conclusion
Now you have learned what is is KVM, How to manage your virtual platform using GUI tools, How to deploy virtual machine using it and another awesome things.
Although this isn’t end of the article, in our up-coming articles, we will discuss another important topics which related to KVM. Make your hands dirty using the previous knowledge and be ready for the next part…..
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Monitor System Usage, Outages and Troubleshoot Linux Servers – Part 9](https://www.tecmint.com/linux-system-monitoring-troubleshooting-tools/)
Next article:
[How to Turn a Linux Server into a Router to Handle Traffic Statically and Dynamically – Part 10](https://www.tecmint.com/setup-linux-as-router/)
![Photo of author](https://secure.gravatar.com/avatar/827dd63ae735741f16af81c2b0cf22e8a1b66a706e6d0572f8e3d8d3f29e1e95?s=100&d=blank&r=g)
Mohammad Dosoukey
Mohammad is Linux system administrator at his university in Egypt . He is a person who fond of Virtualization, Cloud and System administration. He is also RHCE and VCP5-DCV .
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-and-configure-kvm-in-linux/#respond)** or
## Related Posts
[![Resize KVM Virtual Machine Disk Size](https://www.tecmint.com/wp-content/uploads/2023/10/Resize-KVM-Virtual-Machine-Disk-Size.png)](https://www.tecmint.com/resize-kvm-virtual-machine-disk-size/ "How to Extend or Increase KVM Virtual Machine \(VM\) Disk Size")
[![Install Qemu/KVM in Ubuntu](https://www.tecmint.com/wp-content/uploads/2018/06/Install-Qemu-KVM-in-Ubuntu.jpg)](https://www.tecmint.com/install-qemu-kvm-ubuntu-create-virtual-machines/ "How to Install QEMU/KVM on Ubuntu to Create Virtual Machines")
[![KVM Virtualization Book](https://www.tecmint.com/wp-content/uploads/2021/02/kvm-virtualization-ebook.png)](https://www.tecmint.com/kvm-virtualization-book/ "eBook: Introducing KVM Virtualization Setup Guide for Linux")
[![Create a KVM Virtual Machine Template](https://www.tecmint.com/wp-content/uploads/2021/01/Create-KVM-Virtual-Machine-Template.png)](https://www.tecmint.com/create-kvm-virtual-machine-template/ "How to Create a KVM Virtual Machine Template")
[![Manage Virtual Machines Using Virt-Manager](https://www.tecmint.com/wp-content/uploads/2021/01/Manage-Virtual-Machines-Using-Virt-Manager.png)](https://www.tecmint.com/manage-virtual-machines-in-kvm-using-virt-manager/ "How to Manage Virtual Machines in KVM Using Virt-Manager")
[![Create Virtual Machines Using Virt-Manager](https://www.tecmint.com/wp-content/uploads/2021/01/Create-Virtual-Machines-Using-Virt-Manager.png)](https://www.tecmint.com/create-virtual-machines-in-kvm-using-virt-manager/ "How to Create Virtual Machines in KVM Using Virt-Manager")
### 12 Comments
[Leave a Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#reply-title)
  1. Here’s my Vagrant configuration using the “generic/debian12” box:
```
Vagrant.configure("2") do |config|
  config.vm.define "Lager01" do |lg_config|
    lg_config.vm.box = "generic/debian12"
    lg_config.vm.provider "libvirt" do |lv|
      lv.memory = 2048
    end
    lg_config.vm.network "private_network", type: "static", ip: "192.168.56.*"
    lg_config.vm.hostname = "Lager01"
  end
end

```
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-2154518)
  2. As I am using CentOS 6.4 in vmware and unable to execute command, while writing command and hitting enter butter the arrow goes to next line with no output. Please resolve issue if any one knows.
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-895577)
  3. Can you please suggest me the best hardware configuration to install KVM for android emulators.
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-881510)
  4. yum install qemu-kvm fails saying package does not exist
Using centOS7
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-846129)
  5. i want to know how to create **rht-vmctl** reset server, desktop command to reset vm to snapshot image like which we do in rhce lab environment,and i want to create shortcut of virtual machines on desktop
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-810139)
  6. Its not required to remember list of all the rpm names for installing. Just install “yum groupinstall virtualization-client virtualization-platform virtualization-tools” will take care of meeting all dependencies.
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-775998)
  7. Does every new virtual machine need a new storage volume?
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-772448)
  8. heads up, yum install virtualization\ hypervisor has qemu-kvm package not virtualization\ platform, other than that very nice tutorial. To list these groups use yum groups list hidden -v or yum groups list hidden id, followed by yum groups info virtualization-hypervisor.
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-709600)
  9. Mount your rhel 7 or centOS 7 dvd and disk dump it to a folder as an iso. Use the disk dumped iso in your number 13 above as a workaround for you so-called silly bug:
mount /dev/cdrom /mnt
dd if=/dev/sr0 of=/rhel7.iso
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-680559)
  10. mount /dev/cdrom /mnt
dd if=/dev/sr0 of=/rhel7.iso
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-680556)
  11. I tried it but I noted that it is slow tool when i compare it with virtual box or vmware
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-671619)
  12. Nice topic thanks very much
[Reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#comment-671616)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-and-configure-kvm-in-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/install-and-configure-kvm-in-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
