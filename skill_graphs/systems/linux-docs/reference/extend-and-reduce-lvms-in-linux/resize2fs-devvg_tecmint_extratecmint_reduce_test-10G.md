# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10G
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-897478)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 27, 2017 at 3:44 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-897481)
@Rob,
Thanks for pointing out, we’ve corrected in the article..
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-897481)
  35. ![](https://secure.gravatar.com/avatar/05eaca825c2c0e2385afd7211310446a310a1e6b934bbf5a527ab096c7a3f83b?s=50&d=blank&r=g)
KM
[ June 24, 2017 at 3:41 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-897039)
Excellent detailed article!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-897039)
  36. ![](https://secure.gravatar.com/avatar/e2752beb201a0122ccca5f23bdcbcf6417a24d7054d202314e6e0b0147fcf611?s=50&d=blank&r=g)
S. Hildebrant - Solution Architect II
[ May 22, 2017 at 8:48 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-891293)
Great article – so helpful! I was able to use this to extend my media server library filesystem in CentOS 6.8 with no issue whatsoever (after I spent 6 hours rebuilding my RAID array that is)
Thanks for the help!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-891293)
  37. ![](https://secure.gravatar.com/avatar/6b50220c00e3e1eadbfd6a0eae6cc95c18b893a30efff539fc61a4e398448a37?s=50&d=blank&r=g)
Sjonnie
[ May 2, 2017 at 10:42 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-887574)
Excellent! This is exactly what I needed to resize my LV’s on my OpenMediaVault server. Made a how-to with reference to this page on the OMV forum. I hope it gets approved ;)
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-887574)
  38. ![](https://secure.gravatar.com/avatar/3ca7dc775607c0741280475958c81bbda3fde35a54f03348f90084fb04cdab31?s=50&d=blank&r=g)
michael
[ April 18, 2017 at 5:44 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-884476)
Is it possible to extend the space on a disk without adding another disk and no downtime?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-884476)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ April 19, 2017 at 11:44 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-884613)
@Michael,
Yes, it’s possible to extend the size without adding new disks, but we should have enough space in VG.
To extend the space for any logical volumes we don’t require any downtime, only we need downtime in the case of reducing disk space by unmounting.
Thanks & Regards,
Babin Lonston
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-884613)
       * ![](https://secure.gravatar.com/avatar/3ca7dc775607c0741280475958c81bbda3fde35a54f03348f90084fb04cdab31?s=50&d=blank&r=g)
michael
[ April 19, 2017 at 1:24 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-884633)
I know that you need space on VG. But what if I don’t have and I add space to the disk from vSphere or whatever virtualization product? Then it involves downtime to increase the disk space, right?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-884633)
         * ![](https://secure.gravatar.com/avatar/08af49a9bf77c19c97ddbd6aac848e0fe824ebb1f157e6ab2340c3203d8f9af0?s=50&d=blank&r=g)
lybad
[ May 8, 2017 at 4:23 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-888512)
Nope – it’s perfectly possible to increase available disk space on any file system without downtime.
We did a CentOS and an RHEL box last week – one was `/`, and the other was a `/srv` – both without downtime.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-888512)
  39. ![](https://secure.gravatar.com/avatar/cc7dbd5e0a8c68b24d2bd81358e75540dfb8346fee86d2f45c8182b29bf1fe28?s=50&d=blank&r=g)
Mark B
[ March 28, 2017 at 7:47 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-879229)
Great article. Can’t do this with built in GUI tools so this article was dead on for what to do.
Thanks.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-879229)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ April 8, 2017 at 12:49 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-881979)
@Mark,
In real world production environment, only DB servers are installed with GUI more over LVM GUI will not be configured.
It’s good to practice in CLI to keep hands on any platform.
Thanks & Regards,
Babin Lonston
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-881979)
  40. ![](https://secure.gravatar.com/avatar/08b98a59796fcbe9e10e6199c705543d277233301c680348e78e4846b9c1f126?s=50&d=blank&r=g)
MARTIN GARCIA
[ November 5, 2016 at 7:25 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-835430)
Great article,
Thanks for the explanation I modified my partitions without any problem
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-835430)
  41. ![](https://secure.gravatar.com/avatar/f8c5a0552be62d1130719c97817613fb8701da1a1410c844ce97f29899e15c69?s=50&d=blank&r=g)
John F. Godfrey, Pastor
[ October 7, 2016 at 10:14 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-827094)
This article was great! I found it very helpful so I could accomplish what I needed to do. Thanks for this!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-827094)
  42. ![](https://secure.gravatar.com/avatar/4bd74ac788893c0f8f30230d407f45f3031c551c35d20cbca2adc4b6d0db6627?s=50&d=blank&r=g)
Dheny Muhammad Ismail
[ September 13, 2016 at 1:27 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-816629)
I have two hard drives, SATA 1 (/ dev / sdb1) 80 GB and SATA 2 (dev / sdc1) 40 GB. Problem: the 40 GB hard drive is damaged and I will replace it with a new 40GB hard drive as well. How can I reduce the disk (/ dev / sdc1) without losing my data?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-816629)
  43. ![](https://secure.gravatar.com/avatar/4f1fa6099332c9d6e346bad001de404a60c7c49579c115e4d0394a02e98f3a71?s=50&d=blank&r=g)
Dans
[ August 11, 2016 at 5:13 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-806270)
Thanks it worked well.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-806270)
  44. ![](https://secure.gravatar.com/avatar/cc8b005fd4832106456e25297e51e570679fcadfe29bc9b93d9e70d905306be2?s=50&d=blank&r=g)
rafa
[ July 7, 2016 at 2:32 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-797978)
Hi,
it is possible to reduce filesystem mounted on “/” which can’t be umounted? I got “device is busy” error.
Thanks in advance!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-797978)
  45. ![](https://secure.gravatar.com/avatar/f6b1fa38ad106e61176576274997e5ae97e189d081977cff875da8721902a0ab?s=50&d=blank&r=g)
Nandkishor
[ May 20, 2016 at 10:14 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-782579)
awesome……………i got good information.thanks
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-782579)
  46. ![](https://secure.gravatar.com/avatar/f6b1fa38ad106e61176576274997e5ae97e189d081977cff875da8721902a0ab?s=50&d=blank&r=g)
Nandkishor
[ May 20, 2016 at 10:02 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-782574)
very nice information……your post is very helpful to understand how lvm reduce
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-782574)
  47. ![](https://secure.gravatar.com/avatar/e2ce60a6484a14585172935ac8c1acf9f2a14d22153302780652b99fef6a56be?s=50&d=blank&r=g)
bonar agung saputra
[ April 18, 2016 at 9:32 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-773025)
help me
i dont know. i got /dev/mapper/centos-home can’t read superblock
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-773025)
  48. ![](https://secure.gravatar.com/avatar/089c98acdd44f1e46ad26b8c6992b3568624ed623113b408bb7b445f0c3adbaa?s=50&d=blank&r=g)
sameer
[ April 8, 2016 at 12:51 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-770797)
quick question
in your article you have mentioned ” resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 8GB”
should it be : resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB” instead?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-770797)
  49. ![](https://secure.gravatar.com/avatar/fc06efb526fe49252cc6b8672c15aaffa1daa43092e99df1d08adc6b5d5b79f7?s=50&d=blank&r=g)
Minthang Sitlhou
[ March 26, 2016 at 6:03 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-765419)
I guess you have not understood what I am trying to say. I understand that there are 2 ways of reducing lvm size. One is with size name and other is using extent. The problem I see here is that you have reduced lvm size by 8 GB using when reducing with name size. Now, when you reduce lvm size with physical extent you have reduced it by 2048 PE which is equal to 10GB. Our target was to reduce the lvm size to 10GB and not to 8GB which is the case that was carried out while reducing lvm size using name size. Don’t you think both the conversions contradict with each other? I hope you have got the point here.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-765419)
  50. ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ March 25, 2016 at 1:52 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-764855)
@Minthang Sitlhou,
It’s a conversion for knowing the exact PE size for specific amount of GB.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-764855)
  51. ![](https://secure.gravatar.com/avatar/fc06efb526fe49252cc6b8672c15aaffa1daa43092e99df1d08adc6b5d5b79f7?s=50&d=blank&r=g)
Minthang Sitlhou
[ March 25, 2016 at 12:17 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-764469)
hi, can you please clarify the below statement and rectify if incorrect:
“For demonstration, I have created separate volume group and logical volume. Here, I’m going to reduce the logical volume tecmint_reduce_test. Now its 18GB in size. We need to reduce it to 10GB without data-loss. That means we need to reduce 8GB out of 18GB. Already there is 4GB data in the volume.”
While reducing the LVM using size you have used 8G in the example but when you reduce the LVM using physical extend you have used 10240MB / 4PE = 2048PE.
Is this a typo or it is a convention? Would be great if you could at least clarify it.
Thanks,
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-764469)
  52. ![](https://secure.gravatar.com/avatar/283e549fa9e1f8e0c583ed6a1aca261d16b577aafdd708e78048cb83f271511d?s=50&d=blank&r=g)
Muthu
[ January 27, 2016 at 12:06 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-744436)
Thanks, Nice to read the article
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-744436)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ February 6, 2016 at 8:33 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-748622)
@Muthu
Happy to hear from you, Thanks for your feedback.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-748622)
  53. ![](https://secure.gravatar.com/avatar/2c88333fba0931d5dd1e4cbf086321b142b683fb5f17ab81b4a0964cb8b43b75?s=50&d=blank&r=g)
Arnaud Mounier
[ January 13, 2016 at 2:37 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-738408)
Hi,
if you are in rescue mode and you want to extend a partition, you have to remount / in read-write mode before lvextend and resize2fs :
> mount -o remount, rw /
AM
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-738408)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ January 13, 2016 at 5:35 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-738494)
@Arnaud Mounier,
Thanks for the information however this scenario is very rare in production environment. Even a partition get fills we can get some free space by find and removing super blocks, Then we can extend the volume without having any downtime.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-738494)
  54. ![](https://secure.gravatar.com/avatar/8b13eaa7f312d1d6829cdb490b4cf413d870ab0b51e46d5ed2059405b6835684?s=50&d=blank&r=g)
Jose Parreira
[ November 24, 2015 at 4:55 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-712732)
Very helpful, thanks
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-712732)
  55. ![](https://secure.gravatar.com/avatar/04a901147de19dd059b87d204cf1a94e7b407b1b32469d5eb6abfb573a7d7199?s=50&d=blank&r=g)
mr man
[ October 13, 2015 at 8:02 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-685461)
This is a very good resource. This helped me resized lvm based partitions on my test systems painlessly. Thank you.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-685461)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ October 30, 2015 at 3:48 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-698121)
Thanks for your valuable feedback hope you have find some useful information from us.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-698121)
  56. ![](https://secure.gravatar.com/avatar/8326dd90f7750d13d5619df2439e0b43e400d3eccd80ffad218c111db7880339?s=50&d=blank&r=g)
William Lagerberg
[ September 23, 2015 at 8:03 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-672248)
nice article, thanks.
Need some help on this one,
[root@directadmin04 ~]# pvs
PV VG Fmt Attr PSize PFree
/dev/sda2 vg_directadmin04 lvm2 a– 99.51g 0
[root@directadmin04 ~]# vgs
VG #PV #LV #SN Attr VSize VFree
vg_directadmin04 1 3 0 wz–n- 99.51g 0
[root@directadmin04 ~]# lvs
LV VG Attr LSize Pool Origin Data% Meta% Move Log Cpy%Sync Convert
lv_home vg_directadmin04 -wi-ao—- 41.68g
lv_root vg_directadmin04 -wi-ao—- 50.00g
lv_swap vg_directadmin04 -wi-ao—- 7.83g
[root@directadmin04 ~]#
is there a way to down size the lv_root so that lv_home will become bigger, without losing information
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-672248)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ October 30, 2015 at 3:52 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-698122)
yes you can, But can’t perform from live want downtime for host and enter into maintenance mode to follow the resize steps.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-698122)
  57. ![](https://secure.gravatar.com/avatar/b10985c117d8698d1b04379593adb7905bbc970c6c716df150fdd72624af2c3b?s=50&d=blank&r=g)
Ofid
[ September 18, 2015 at 8:39 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-668370)
Thanks, very helpful
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-668370)
  58. ![](https://secure.gravatar.com/avatar/892006107b178d71b7c07ee4675afd744d4e8504d4e190995830e724093dca3f?s=50&d=blank&r=g)
Omid Mohajerani
[ August 12, 2015 at 3:06 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-642072)
Thank you for the post . you have one error .
resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 8GB
it should be :
resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10GB
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-642072)
  59. ![](https://secure.gravatar.com/avatar/617102dbecfa1172e6740b28d502f7ffeb124991f5a42efe9e9d43ca77efe09e?s=50&d=blank&r=g)
Manuel
[ July 14, 2015 at 1:11 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-623780)
I was helpful. Thanks!!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-623780)
  60. ![](https://secure.gravatar.com/avatar/545df305b09ed2f2aa09da6e9af2a61e28aa954549fe8d0a17cc83c1f51feb7a?s=50&d=blank&r=g)
Ben Kennish
[ June 25, 2015 at 7:43 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-607956)
I believe the line that says:
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 10G
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-607956)
     * ![](https://secure.gravatar.com/avatar/545df305b09ed2f2aa09da6e9af2a61e28aa954549fe8d0a17cc83c1f51feb7a?s=50&d=blank&r=g)
Ben Kennish
[ June 25, 2015 at 7:44 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-607957)
Just after “Next, reduce the file-system”
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-607957)
  61. ![](https://secure.gravatar.com/avatar/23d3e539728e397d57d1a925b488a2a10b8bafa4fb96ab212b99ccfb51e4b9e9?s=50&d=blank&r=g)
fermin rodriguez
[ April 1, 2015 at 9:40 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-528827)
i would like to note that for newer distributions (where XFS might be used by default) you need to use xfs_growfs instead (install xfsprogs.)
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-528827)
     * ![](https://secure.gravatar.com/avatar/380d5d12d46beb91ad3b79e2df94be9e99b165ed8e174cf97023c22a537f71d9?s=50&d=blank&r=g)
Ricardo Silva
[ February 5, 2016 at 4:12 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-748041)
Thanks, helped me a lot!!!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-748041)
  62. ![](https://secure.gravatar.com/avatar/d7311013298b48db7f9723378cd308ce20a6b95542a9f13c66273e188ce84df7?s=50&d=blank&r=g)
Sonic
[ February 5, 2015 at 8:11 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-474363)
This article is really helpful. I looked forward to finding some information to extend my logical volume with a new hard disk. Thanks!!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-474363)
  63. ![](https://secure.gravatar.com/avatar/233e36436affba019f63175d2f543992f1724a243485284161d2153332831503?s=50&d=blank&r=g)
Torbjrön Rasmusson
[ January 13, 2015 at 3:05 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-451340)
Thank you for the awesome guide! It saved me a lot of trouble!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-451340)
  64. ![](https://secure.gravatar.com/avatar/1dccc868983142f32aa841bb0d3031221af289cf1f5ba9eb52c9cb0c66cf6560?s=50&d=blank&r=g)
manzoor
[ January 6, 2015 at 8:33 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-444581)
Very nice document and well explained. I found some discrepancies between the screen-shots and command. for example you can see that you fired the command to reduce the FS size 8GB…
