# How to Extend/Reduce LVM’s (Logical Volume Management) in Linux – Part II
[Babin Lonston](https://www.tecmint.com/author/babinlonston/ "View all posts by Babin Lonston")Last Updated: April 1, 2023 Read Time: 6 minsCategories [Storage](https://www.tecmint.com/category/storage/) [93 Comments](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comments)
Previously we have seen how to create a flexible disk storage using LVM. Here, we are going to see how to extend volume group, extend and reduce a logical volume. Here we can reduce or extend the partitions in Logical volume management (LVM) also called as flexible volume file-system.
![Extend/Reduce LVMs in Linux](https://www.tecmint.com/wp-content/uploads/2014/08/LVM_extend.jpg)Extend/Reduce LVMs in Linux
#### Requirements
  1. [Create Flexible Disk Storage with LVM – Part I](https://www.tecmint.com/create-lvm-storage-in-linux/)


##### When do we need to reduce volume?
May be we need to create a separate partition for any other use or we need to expand the size of any low space partition, if so we can reduce the large size partition and we can expand the low space partition very easily by the following simple easy steps.
##### My Server Setup – Requirements
  1. Operating System – CentOS 6.5 with LVM Installation
  2. Server IP – 192.168.0.200


### How to Extend Volume Group and Reduce Logical Volume
#### Logical Volume Extending
Currently, we have One PV, VG and 2 LV. Let’s list them one by one using following commands.
```
# pvs
# vgs
# lvs
```
![Logical Volume Extending](https://www.tecmint.com/wp-content/uploads/2014/08/Logical-Volume-Extending.jpg)Logical Volume Extending
There are no free space available in Physical Volume and Volume group. So, now we can’t extend the lvm size, for extending we need to add one physical volume (**PV**), and then we have to extend the volume group by extending the **vg**. We will get enough space to extend the Logical volume size. So first we are going to add one physical volume.
For adding a new **PV** we have to use fdisk to create the LVM partition.
```
# fdisk -cu /dev/sda
```

  1. To Create new partition Press **n**.
  2. Choose primary partition use **p**.
  3. Choose which number of partition to be selected to create the primary partition.
  4. Press **1** if any other disk available.
  5. Change the type using **t**.
  6. Type **8e** to change the partition type to Linux LVM.
  7. Use **p** to print the create partition ( here we have not used the option).
  8. Press **w** to write the changes.


Restart the system once completed.
![Create LVM Partition](https://www.tecmint.com/wp-content/uploads/2014/08/Create-LVM-Partition.jpg)Create LVM Partition
List and check the partition we have created using fdisk.
```
# fdisk -l /dev/sda
```
![Verify LVM Partition](https://www.tecmint.com/wp-content/uploads/2014/08/Verify-LVM-Partition.jpg)Verify LVM Partition
Next, create new **PV** (Physical Volume) using following command.
```
# pvcreate /dev/sda1
```

Verify the pv using below command.
```
# pvs
```
![Create Physical Volume](https://www.tecmint.com/wp-content/uploads/2014/08/Create-Physical-Volume.jpg)Create Physical Volume
#### Extending Volume Group
Add this pv to **vg_tecmint** vg to extend the size of a volume group to get more space for expanding **lv**.
```
# vgextend vg_tecmint /dev/sda1
```

Let us check the size of a Volume Group now using.
```
# vgs
```
![Extend Volume Group](https://www.tecmint.com/wp-content/uploads/2014/08/Extend-Volume-Group.jpg)Extend Volume Group
We can even see which **PV** are used to create particular Volume group using.
```
# pvscan
```
![Check Volume Group](https://www.tecmint.com/wp-content/uploads/2014/08/Check-Volume-Group.jpg)Check Volume Group
Here, we can see which Volume groups are under Which Physical Volumes. We have just added one pv and its totally free. Let us see the size of each logical volume we have currently before expanding it.
![Check All Logical Volume](https://www.tecmint.com/wp-content/uploads/2014/08/Check-Each-Logical-Volume-347x450.jpg)Check All Logical Volume
  1. LogVol00 defined for Swap.
  2. LogVol01 defined for /.
  3. Now we have 16.50 GB size for / (root).
  4. Currently there are 4226 Physical Extend (PE) available.


Now we are going to expand the **/** partition **LogVol01**. After expanding we can list out the size as above for confirmation. We can extend using GB or PE as I have explained it in LVM PART-I, here I’m using PE to extend.
For getting the available Physical Extend size run.
```
# vgdisplay
```
![Check Available Physical Size](https://www.tecmint.com/wp-content/uploads/2014/08/Check-Available-Physical-Extend-502x450.jpg)Check Available Physical Size
There are **4607** free PE available = **18GB** Free space available. So we can expand our logical volume up-to **18GB** more. Let us use the PE size to extend.
```
# lvextend -l +4607 /dev/vg_tecmint/LogVol01
```

Use **+** to add the more space. After Extending, we need to re-size the file-system using.
```
# resize2fs /dev/vg_tecmint/LogVol01
```
![Expand Logical Volume](https://www.tecmint.com/wp-content/uploads/2014/08/Expand-Logical-Volume-620x240.jpg)Expand Logical Volume
  1. Command used to extend the logical volume using Physical extends.
  2. Here we can see it is extended to 34GB from 16.51GB.
  3. Re-size the file system, If the file-system is mounted and currently under use.
  4. For extending Logical volumes we don’t need to unmount the file-system.


Now let’s see the size of re-sized logical volume using.
```
# lvdisplay
```
![Resize Logical Volume](https://www.tecmint.com/wp-content/uploads/2014/08/Resize-Logical-Volume-363x450.jpg)Resize Logical Volume
  1. LogVol01 defined for / extended volume.
  2. After extending there is 34.50GB from 16.50GB.
  3. Current extends, Before extending there was 4226, we have added 4607 extends to expand so totally there are 8833.


Now if we check the vg available Free PE it will be 0.
```
# vgdisplay
```

See the result of extending.
```
# pvs
# vgs
# lvs
```
![Verify Resize Partition](https://www.tecmint.com/wp-content/uploads/2014/08/Verify-Resize-Partition.jpg)Verify Resize Partition
  1. New Physical Volume added.
  2. Volume group vg_tecmint extended from 17.51GB to 35.50GB.
  3. Logical volume LogVol01 extended from 16.51GB to 34.50GB.


Here we have completed the process of extending volume group and logical volumes. Let us move towards some interesting part in Logical volume management.
#### Reducing Logical Volume (LVM)
Here we are going to see how to reduce the Logical Volumes. Everyone say its critical and may end up with disaster while we reduce the lvm. Reducing lvm is really interesting than any other part in Logical volume management.
  1. Before starting, it is always good to backup the data, so that it will not be a headache if something goes wrong.
  2. To Reduce a logical volume there are 5 steps needed to be done very carefully.
  3. While extending a volume we can extend it while the volume under mount status (online), but for reduce we must need to unmount the file system before reducing.


Let’s wee what are the 5 steps below.
  1. unmount the file system for reducing.
  2. Check the file system after unmount.
  3. Reduce the file system.
  4. Reduce the Logical Volume size than Current size.
  5. Recheck the file system for error.
  6. Remount the file-system back to stage.


For demonstration, I have created separate volume group and logical volume. Here, I’m going to reduce the logical volume **tecmint_reduce_test**. Now its 18GB in size. We need to reduce it to **10GB** without data-loss. That means we need to reduce **8GB** out of **18GB**. Already there is **4GB** data in the volume.
```
18GB ---> 10GB
```

While reducing size, we need to reduce only 8GB so it will roundup to 10GB after the reduce.
```
# lvs
```
![Reduce Logical Volume](https://www.tecmint.com/wp-content/uploads/2014/08/Reduce-Logical-Volume.jpg)Reduce Logical Volume
Here we can see the file-system information.
```
# df -h
```
![Check File System Size](https://www.tecmint.com/wp-content/uploads/2014/08/Check-File-System-Size-620x130.jpg)Check File System Size
  1. The size of the Volume is 18GB.
  2. Already it used upto 3.9GB.
  3. Available Space is 13GB.


First unmount the mount point.
```
# umount -v /mnt/tecmint_reduce_test/
```
![Unmount Parition](https://www.tecmint.com/wp-content/uploads/2014/08/Unmount-Parition.jpg)Unmount Parition
Then check for the file-system error using following command.
```
# e2fsck -ff /dev/vg_tecmint_extra/tecmint_reduce_test
```
![Scan Parition for Errors](https://www.tecmint.com/wp-content/uploads/2014/08/Scan-Parition-for-Errors-620x223.jpg)Scan Parition for Errors
**Note** : Must pass in every 5 steps of file-system check if not there might be some issue with your file-system.
Next, reduce the file-system.
```
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10G
```
![Reduce File System](https://www.tecmint.com/wp-content/uploads/2014/08/Reduce-File-System-620x91.jpg)Reduce File System
Reduce the Logical volume using GB size.
```
# lvreduce -L -8G /dev/vg_tecmint_extra/tecmint_reduce_test
```
![Reduce Logical Partition](https://www.tecmint.com/wp-content/uploads/2014/08/Reduce-Logical-Volume-Partition.jpg)Reduce Logical Partition
To Reduce Logical volume using PE Size we need to Know the size of default PE size and total PE size of a Volume Group to put a small calculation for accurate Reduce size.
```
# lvdisplay vg_tecmint_extra
```

Here we need to do a little calculation to get the PE size of 10GB using bc command.
```
1024MB x 10GB = 10240MB or 10GB

10240MB / 4PE = 2048PE
```

Press **CRTL+D** to exit from BC.
![Calculate PE Size](https://www.tecmint.com/wp-content/uploads/2014/08/bc-command.jpg)Calculate PE Size
Reduce the size using PE.
```
# lvreduce -l -2048 /dev/vg_tecmint_extra/tecmint_reduce_test
```
![Reduce Size Using PE](https://www.tecmint.com/wp-content/uploads/2014/08/Reduce-Size-Using-PE-620x129.jpg)Reduce Size Using PE
Re-size the file-system back, In this step if there is any error that means we have messed-up our file-system.
```
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test
```
![Resize File System](https://www.tecmint.com/wp-content/uploads/2014/08/Resize-File-System-620x139.jpg)Resize File System
Mount the file-system back to same point.
```
# mount /dev/vg_tecmint_extra/tecmint_reduce_test /mnt/tecmint_reduce_test/
```
![Mount File System](https://www.tecmint.com/wp-content/uploads/2014/08/Mount-File-System-620x323.jpg)Mount File System
Check the size of partition and files.
```
# lvdisplay vg_tecmint_extra
```

Here we can see the final result as the logical volume was reduced to 10GB size.
![Verify Logical Volume Size](https://www.tecmint.com/wp-content/uploads/2014/08/Verify-Logical-Volume-Size.jpg)Verify Logical Volume Size
In this article, we have seen how to extend the volume group, logical volume and reduce the logical volume. In the next part (Part III), we will see how to take a Snapshot of logical volume and restore it to earlier stage.
Tags [lvm](https://www.tecmint.com/tag/lvm/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Icinga: A Next Generation Open Source ‘Linux Server Monitoring’ Tool for RHEL/CentOS 7.0](https://www.tecmint.com/install-icinga-in-centos-7/)
Next article:
[Install Kernel 3.16 (Latest Released) in Ubuntu and Derivatives](https://www.tecmint.com/install-kernel-in-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/ed7ad2c5315a198976b948522cb12517a16d8feb5bf48b6be3ab367a9c3d02cf?s=100&d=blank&r=g)
Babin Lonston
I'm Working as a System Administrator for last 10 year's with 4 years experience with Linux Distributions, fall in love with text based operating systems.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#respond)** or
## Related Posts
[![Manage Layered Local Storage with Stratis](https://www.tecmint.com/wp-content/uploads/2024/10/Manage-Layered-Local-Storage-with-Stratis.webp)](https://www.tecmint.com/install-stratis-to-manage-layered-local-storage-on-rhel/ "How to Install Stratis to Manage Layered Local Storage on RHEL 9/8")
[How to Install Stratis to Manage Layered Local Storage on RHEL 9/8](https://www.tecmint.com/install-stratis-to-manage-layered-local-storage-on-rhel/)
[![Setup LVM Storage in Linux](https://www.tecmint.com/wp-content/uploads/2023/08/Setup-LVM-Storage-in-Linux.png)](https://www.tecmint.com/create-lvm-storage-in-linux/ "How to Create Disk Storage with Logical Volume Management \(LVM\) in Linux – PART 1")
[How to Create Disk Storage with Logical Volume Management (LVM) in Linux – PART 1](https://www.tecmint.com/create-lvm-storage-in-linux/)
[![Install ownCloud in Linux](https://www.tecmint.com/wp-content/uploads/2021/07/Install-ownCloud-in-Linux.png)](https://www.tecmint.com/install-owncloud-to-create-personal-storage-in-linux/ "How to Install OwnCloud to Create Own Cloud Storage in Linux")
[How to Install OwnCloud to Create Own Cloud Storage in Linux](https://www.tecmint.com/install-owncloud-to-create-personal-storage-in-linux/)
[![Install OwnCloud on Ubuntu](https://www.tecmint.com/wp-content/uploads/2020/03/Install-OwnCloud-in-Ubuntu.png)](https://www.tecmint.com/install-owncloud-on-ubuntu/ "How to Install OwnCloud on Ubuntu 18.04")
[How to Install OwnCloud on Ubuntu 18.04](https://www.tecmint.com/install-owncloud-on-ubuntu/)
[![Install NextCloud on CentOS 8](https://www.tecmint.com/wp-content/uploads/2020/03/Install-NextCloud-in-CentOS-8.png)](https://www.tecmint.com/install-nextcloud-on-centos-8/ "How to Install NextCloud on CentOS 8")
[How to Install NextCloud on CentOS 8](https://www.tecmint.com/install-nextcloud-on-centos-8/)
[![Install OwnCloud in Debian 10](https://www.tecmint.com/wp-content/uploads/2020/03/Install-OwnCloud-on-Debian.png)](https://www.tecmint.com/install-owncloud-in-debian/ "How to Install OwnCloud in Debian 10")
[How to Install OwnCloud in Debian 10](https://www.tecmint.com/install-owncloud-in-debian/)
### 93 Comments
[Leave a Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/8219ae3056ed079ff779e7757bfd4af44da90f81a639030e10ba1b1ded74f0f0?s=50&d=blank&r=g)
Dave Hotrum
[ August 15, 2023 at 6:25 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-2045442)
I have what I consider a big problem. I installed **Ubuntu 22.04** and **LVM** during installation. I have 3 HDs before installing I moved all data to the 3rd drive, **sdc**.
Now after installing it, I do not see the **sdc**. With gparted I can see the **sdc** and it is called **sdc**. It shows an area with data. MY DATA but I cannot see it in **Nautilus**.
How to see it and move my data back to the **/home/user/**? The data was created on Ubuntu 23.04. I went down because of too many problems on 23.04. What can I do?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-2045442)
  2. ![](https://secure.gravatar.com/avatar/77cd5114375fc87e6fa11ae526fb2f4c7bba2a017995cdedb045568cef40179b?s=50&d=blank&r=g)
xabispacebiker
[ March 31, 2023 at 5:32 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1990597)
There is a typo:
```
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB

```

should be:
```
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10G

```
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1990597)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 1, 2023 at 9:37 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1990882)
@Xabispacebiker,
Thanks for your input, corrected the command in the article…
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1990882)
  3. ![](https://secure.gravatar.com/avatar/7de73add300af5475407493fde3373b0c9fb1daebadca338230bbac7e979d848?s=50&d=blank&r=g)
helwie
[ June 9, 2022 at 10:24 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1822089)
Nice post.
I have a question related to that article above. can I reduce my multiple HDD were use by home partition? we have five HDD @2TB extend with lvm with xfs format in centos 7.
So we need to resize the partition home from 10TB to 5TB. I need to remove two HDDs and make sure all data cant corrupt.
can you advise me step by step. thanks
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1822089)
  4. ![](https://secure.gravatar.com/avatar/7bd6d76d7f52798f112e5647c95e46a38cad13be42c35d0a0411601510ef609e?s=50&d=blank&r=g)
Ramesh
[ May 4, 2022 at 4:06 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1782794)
How to extend the partition without using **lvextend** command?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1782794)
  5. ![](https://secure.gravatar.com/avatar/a9615984405cc16a1503e399dea8790b58047eec214eb29c71dce06bd8712eba?s=50&d=blank&r=g)
Narender Singh
[ December 24, 2020 at 7:07 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1404157)
The actual command you can see 10G is used in the terminal screenshot.
The author/editor needs to update in display information which may be due to a typing mistakes.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1404157)
  6. ![](https://secure.gravatar.com/avatar/aa4294749886ab28112b5b28f627abaf20e87758d2797f6ff0a526d494cf53fd?s=50&d=blank&r=g)
Divakaran E
[ August 14, 2020 at 6:03 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1353110)
Hi,
my **activemq** is running on `/data`. Can I extend **lvm** online without stopping process of activemq?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1353110)
  7. ![](https://secure.gravatar.com/avatar/08585afa0bccffbd84d3045dfcfee0ce965e4603206a2b199b3199ab4fb78916?s=50&d=blank&r=g)
Michael
[ August 8, 2020 at 2:04 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1351255)
I have already expanded the `/home` by following the instructions above.
```
[root@maxs ~]# lvs
  LV   VG     Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  home centos -wi-ao---- 20.93g
  root centos -wi-ao---- 37.25g
  swap centos -wi-ao---- <3.73g

```

However when I use the **df** command to verify the `/home` size, its size is still **953M**.
```
[root@maxs ~]# df -h /home
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-home  953M  953M   88K 100% /home

```

Hope you can help me.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1351255)
  8. ![](https://secure.gravatar.com/avatar/f6391ba05639816d8df8d431b5e3a51271d74f064bfc2a5dcb32033d57b4995e?s=50&d=blank&r=g)
Nathan
[ August 6, 2020 at 12:06 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1350301)
” **resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB** ”
Your command line is wrong. resize2fs takes size with a single character. It should be 10G and not 10GB.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1350301)
  9. ![](https://secure.gravatar.com/avatar/1f9d0a111f59a7950f850cdaf04ae5f23ab340c5423e09f31bb69679609c846f?s=50&d=blank&r=g)
Bobby Brown
[ May 15, 2020 at 7:46 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1333615)
Thank you! This took forever to figure out what I wanted to do. Super clear instructions, much better than ubuntu forums or StackOverflow LOL
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1333615)
  10. ![](https://secure.gravatar.com/avatar/fe5261392533077c7cfe19b54843bbd0412dbc9caa2b6415c977abc9303e1e3e?s=50&d=blank&r=g)
Johannes Linkels
[ March 16, 2020 at 1:33 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1321510)
You have to unmount **/home** first. This might not be possible if you are logged in. You can try to go to the console with `CTRL-ALT-F1`, log in as root. Stop the GUI. Depending on what Desktop you are running you have to google how to do that. After the GUI is stopped you should be able to unmount **/home**. Root does not use **/home**.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1321510)
  11. ![](https://secure.gravatar.com/avatar/add8e6b63c17c937ca71b0e9f7c011a2c7a6d647b42eb72931fc3f1f25023bc0?s=50&d=blank&r=g)
wffger
[ March 14, 2020 at 11:36 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1321295)
How to reduce lvm mapped to **/home**? When I use e2fsck, it returns the device is busy.
```
[root@ydx-mf ~]# pvs
  PV             VG   Fmt  Attr PSize   PFree
  /dev/nvme0n1p3 VG01 lvm2 a--  475.35g    0
[root@ydx-mf ~]# lvs
  LV   VG   Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  home VG01 -wi-ao---- 397.96g
  root VG01 -wi-ao----  70.00g
  swap VG01 -wi-ao----   7.39g

```
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1321295)
     * ![](https://secure.gravatar.com/avatar/f6391ba05639816d8df8d431b5e3a51271d74f064bfc2a5dcb32033d57b4995e?s=50&d=blank&r=g)
Nathan
[ August 6, 2020 at 12:07 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1350303)
You cannot resize a volume you have mounted, and that you are also currently in.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1350303)
  12. ![](https://secure.gravatar.com/avatar/8f5d243d3291457763e374536b1e1ed6f47555b0d3cb7946a50bb52487ee59c9?s=50&d=blank&r=g)
Arshad Bhutto
[ March 13, 2020 at 8:44 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1321173)
Thanks, this was a very helpful write up!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1321173)
  13. ![](https://secure.gravatar.com/avatar/ab9d174a1d69ab1d2522de2b4f77dfb3b27ae0464ecd1e3a750c959e42b1b36e?s=50&d=blank&r=g)
benyamin
[ February 28, 2020 at 11:52 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1319123)
I am getting following errors.
```
[root@server ~]# fdisk -l /dev/sda

Disk /dev/sda: 1000.2 GB, 1000204886016 bytes, 1953525168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk label type: dos
Disk identifier: 0x000e2dce

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     1026047      512000   83  Linux
/dev/sda2         1026048  1953523711   976248832   8e  Linux LVM

```
```
[root@server ~]# pvcreate /dev/sda2
  WARNING: Device for PV YNsfOB-W0GD-J6DV-y7JS-dv8J-3ScO-JtQw1d not found or rejected by a filter.
  Couldn't find device with uuid YNsfOB-W0GD-J6DV-y7JS-dv8J-3ScO-JtQw1d.
  Can't initialize physical volume "/dev/sda2" of volume group "centos" without -ff
  /dev/sda2: physical volume not initialized.

```
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1319123)
  14. ![](https://secure.gravatar.com/avatar/fd8fc70725d54740c3dba97c78d734ffc63994276f257f48aea5e5ddf550a44e?s=50&d=blank&r=g)
Godwin Chanda
[ December 19, 2019 at 3:06 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1307518)
Free-flowing explanation from start to finish. Many thanks.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1307518)
  15. ![](https://secure.gravatar.com/avatar/78f43cb561d30918cb22957947f5963294dcdf15528c92c968e7b9d9bed70df0?s=50&d=blank&r=g)
Harsh
[ November 13, 2019 at 8:45 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1287841)
This was very helpful!! Thanks Babin!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1287841)
  16. ![](https://secure.gravatar.com/avatar/d8a717a88b9266fd4cdcf289da27c282087fa617aae2ddfe22d11a47f4dbd314?s=50&d=blank&r=g)
Aditya Garg
[ August 17, 2019 at 11:53 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1226426)
In summary, to reduce ext filesystem:
     * unmount/mount at the end
     * fsck
     * resize the filesystem
     * lvreduce
     * resize again to avoid discrepancies between LV and FS
     * fsck
1 thru 5 are taken care by single command: `lvreduce -L (size) -r /dev/mapper/vg-lv`
As seen here:
The command performs each of the steps (even unmounts and mounts back)
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1226426)
  17. ![](https://secure.gravatar.com/avatar/8fbeef883667b9a83b7f0ed5bc15076fed16e5e9039667f622d271409f460753?s=50&d=blank&r=g)
Zak
[ July 10, 2019 at 12:24 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1198879)
Thanks, this was a very helpful write up!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1198879)
  18. ![](https://secure.gravatar.com/avatar/20566b7dc5a39625f6bc1301fe74a26b21102fed177774de51000b2f61e743eb?s=50&d=blank&r=g)
Bhargavi
[ June 12, 2019 at 5:20 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1166938)
Hi,
I have created one hard disk (sdc) and want to add in (sdb) hard disk how to add in command line in LVM please let me know.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1166938)
  19. ![](https://secure.gravatar.com/avatar/ed7ad2c5315a198976b948522cb12517a16d8feb5bf48b6be3ab367a9c3d02cf?s=50&d=blank&r=g)
Babin
[ March 25, 2019 at 10:23 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1117983)
@Mihir,
Still, XFS did not provide an option to reduce, but you can grow the size on the fly.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1117983)
  20. ![](https://secure.gravatar.com/avatar/6689040147a67deeae0f582432cf0f2ec10beeb14eedd1d11395175d1dce4008?s=50&d=blank&r=g)
Mihir Agrawal
[ March 21, 2019 at 8:50 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1115714)
How to reduce xfs file system?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1115714)
  21. ![](https://secure.gravatar.com/avatar/8cc6e83c0335dde183cb6dd39a8272ba7b8b96e49e4d51d15294a967e675b9ff?s=50&d=blank&r=g)
Peter Haas
[ February 28, 2019 at 2:55 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1106153)
It is worth mentioning if your partition is xfs then you will need to use ‘**xfs_growfs** ‘.
xfs seems popular for later releases of Centos.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1106153)
  22. ![](https://secure.gravatar.com/avatar/fe9f8160018427b02fc5592c7ddc5de2034d86f342fa2c99566f01c14b331e7b?s=50&d=blank&r=g)
Andrew Krenitz
[ January 23, 2019 at 12:48 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1096951)
All was going well until I ran Couldn’t find valid
```
[root@localhost ~]# lvextend -l +20000 /dev/fedora/root
  Size of logical volume fedora/root changed from 15.00 GiB (3840 extents) to 93.12 GiB (23840 extents).
  Logical volume fedora/root successfully resized.

```
```
[root@localhost ~]# resize2fs /dev/fedora/root
resize2fs 1.44.3 (10-July-2018)
resize2fs: Bad magic number in super-block while trying to open /dev/fedora/root

```

Couldn't find valid filesystem superblock.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1096951)
  23. ![](https://secure.gravatar.com/avatar/3ca7dc775607c0741280475958c81bbda3fde35a54f03348f90084fb04cdab31?s=50&d=blank&r=g)
Michael
[ October 17, 2018 at 4:57 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1049452)
Hi Guys,
I need to increase disk space on a centos 7 but when I do `fdisk -cu /dev/sda` I get the menu with options. If I do only `fdisk /dev/sda` I get a warning that fdisk GPT support is current new.
Already added a new disk from the hypervisor to the virtual machine.
Used the same method as described in the article but for Ubuntu.
Any thoughts?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1049452)
  24. ![](https://secure.gravatar.com/avatar/aec0045125859f047c52169e0344352e64ef1120b87abd713c7de069f0e1c3db?s=50&d=blank&r=g)
George Fisherman
[ October 12, 2018 at 3:38 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1047033)
Thank You, worked Perfectly on Red Hat Enterprise Linux Server release 6.3
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1047033)
  25. ![](https://secure.gravatar.com/avatar/79bc266dfe76b1e269e8bb4ebf3b467e1c4bf0d2493f30e4e1abe9cb9e97fb58?s=50&d=blank&r=g)
6ril
[ October 10, 2018 at 9:00 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1046406)
**resizefs** give error about bad superblock.
I had to use **xfs_growfs** instead of **resizefs**.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1046406)
     * ![](https://secure.gravatar.com/avatar/ed7ad2c5315a198976b948522cb12517a16d8feb5bf48b6be3ab367a9c3d02cf?s=50&d=blank&r=g)
Babin Lonston
[ October 11, 2018 at 3:53 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1046791)
@6ril,
Yes, resize2fs for ext file systems. We need to use **xfs_growfs** for **xfs** file systems.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-1046791)
  26. ![](https://secure.gravatar.com/avatar/7c9de62944b9bdb74268158e4df5c7cc8c59a6abb5b6d009a8a9c295732f2e45?s=50&d=blank&r=g)
krishna
[ May 17, 2018 at 11:04 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-993459)
Hi,
I have 2 questions any one please give me a answer:
1. what is the difference between **L** and **l** (small) ?
2. what is the difference between **LVresize** and **LV** extend ?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-993459)
     * ![](https://secure.gravatar.com/avatar/ed7ad2c5315a198976b948522cb12517a16d8feb5bf48b6be3ab367a9c3d02cf?s=50&d=blank&r=g)
Bobin Lonston
[ May 18, 2018 at 8:40 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-993851)
@Krishna,
1. what is the difference between L and l (small)?
L = Can be used while MB, GB or TB in size
l = Can be used while resizing or reducing with Physical extent in size (PE), (The default extent size of a single PE is 4 MB).
2. what is the difference between LVresize and LV extent?
lvresize = Take an example resizing from 10 GB to 20 GB using existing PEs from the Volume group.
lvextend = Only used while adding a new device (/dev/sdc or /dev/sdd or whatever ) to existing volume group.
Thanks & Regards,
Bobin Lonston
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-993851)
  27. ![](https://secure.gravatar.com/avatar/fe5261392533077c7cfe19b54843bbd0412dbc9caa2b6415c977abc9303e1e3e?s=50&d=blank&r=g)
Hans Linkels
[ April 26, 2018 at 12:18 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-986616)
I tried reducing the LV on a test system. Worked like breeze. To calculate the PE’s to remove I converted everything to real bytes. That is, PE size of 4MiB = 4 * 1024 * 1024. And the number of GB to remove was 1Gib = 1024 * 1024 * 2014 bytes.
After resizefs, the space needed by the file system is specified in 4kiB blocks, so 4096 bytes each. If you want to calculate accurately without losing a GB here and there AND you want to be sure not to reduce the LV beyond the size of the file system, I’d recommend this.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-986616)
  28. ![](https://secure.gravatar.com/avatar/b7edde6da9c1d11ab4c22ec83a749da74f7a0e83963dd6450acdda926a177501?s=50&d=blank&r=g)
Spas
[ March 22, 2018 at 2:16 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-977244)
I think the command `**resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB** ` should be `**resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10G** ` –> 10GB produces: invalid new size.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-977244)
     * ![](https://secure.gravatar.com/avatar/fe5261392533077c7cfe19b54843bbd0412dbc9caa2b6415c977abc9303e1e3e?s=50&d=blank&r=g)
Hans Linkels
[ April 26, 2018 at 12:14 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-986614)
That is correct. I had the same problem
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-986614)
  29. ![](https://secure.gravatar.com/avatar/f6229a93a5c15d543033ae76aa7fe89ff07e2d969e898ae4ae98ff59c929dade?s=50&d=blank&r=g)
Pratik
[ February 27, 2018 at 6:21 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-973056)
We can use **lvextend** and **resize2fs** same time with **lvextend -r** command.
From the man page:
**-r|–resizefs** – Resize underlying filesystem together with the LV using fsadm(8).
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-973056)
  30. ![](https://secure.gravatar.com/avatar/de80b5b1aa59f4825910c2d5b81bdf8fe644148b46d921dcdef789fbd3c6f6b0?s=50&d=blank&r=g)
sagar
[ January 20, 2018 at 4:09 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-961648)
Thanks for sharing the article…Really helpful.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-961648)
  31. ![](https://secure.gravatar.com/avatar/cb0c98557c0ed79b75be56e56e7ad246a6e08a0c99111b9c5d0a7583202960c4?s=50&d=blank&r=g)
Amiya
[ January 14, 2018 at 12:40 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-960435)
Awesome article! Straight to the point.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-960435)
  32. ![](https://secure.gravatar.com/avatar/13fa0b3f55ed04664bfeee469af92059af947f57eae4ff328332aed585cf30da?s=50&d=blank&r=g)
Ramesh Das
[ December 30, 2017 at 1:13 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-955592)
Hello Ravi,
```
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 8GB

```

but on the actual screen you showing:
```
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10G

```

Still the article is live and you have not corrected. Please make the correction as its been followed by many techs.
Regards
Ramesh Das
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-955592)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 2, 2018 at 11:10 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-956815)
@Ramesh,
We extremely sorry for trouble, we’ve corrected the command as suggested, if you still seeing same, clear your browser cache..
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-956815)
  33. ![](https://secure.gravatar.com/avatar/7eccbf29204865938f3db1e570cd0eaa0cb5f254d540d207a579b89cb65d963b?s=50&d=blank&r=g)
Dimitri
[ August 15, 2017 at 3:01 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-906622)
Thanks a lot ! This is the best tutorial I have ever seen !
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-906622)
  34. ![](https://secure.gravatar.com/avatar/41b6f02b4f3ea70ae9f24a2b1d92cdb17dc7f7f7abccebe5808dd0ee6e060d4e?s=50&d=blank&r=g)
Rob
[ June 27, 2017 at 3:13 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-897478)
Great article.
Just a little mistake you made. In reducing LVM you saying:
