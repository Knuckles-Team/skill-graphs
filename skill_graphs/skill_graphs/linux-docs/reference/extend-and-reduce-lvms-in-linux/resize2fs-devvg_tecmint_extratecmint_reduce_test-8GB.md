# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 8GB
…but on the actual screen you showing:
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 8GB
should read:
# resize2fs /dev/vg_tecmint_extra/tecmint_reduce_test 8GB
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-444581)
  65. ![](https://secure.gravatar.com/avatar/cc62c005613aae5773d3f4288c5e713bdbc44cefdd97a13ca54787fa305c670f?s=50&d=blank&r=g)
ram
[ November 7, 2014 at 6:17 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-362160)
@Babin Lonston can you give me steps how to create new partion to install Ubuntu from existing LVM. I follwed your steps but it added that space to “Free PE /Size”can you tell me how to take that space out for installing ubuntu in that place.
Current my machine is running fedora.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-362160)
  66. ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ October 6, 2014 at 8:01 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-323483)
@ Egi Adithia Pradana, Yes its Possible to reduce the logical volume size and extend other logical volume in the same volume group. Even you can create a new logical volume if you have enough space in Volume group.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-323483)
     * ![](https://secure.gravatar.com/avatar/cc62c005613aae5773d3f4288c5e713bdbc44cefdd97a13ca54787fa305c670f?s=50&d=blank&r=g)
ram
[ November 7, 2014 at 6:17 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-362161)
@Babin Lonston can you give me steps how to create new partion to install Ubuntu from existing LVM. I follwed your steps but it added that space to “Free PE /Size”can you tell me how to take that space out for installing ubuntu in that place.
Current my machine is running fedora.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-362161)
  67. ![](https://secure.gravatar.com/avatar/7830d8ba7760ef7bb434c496fd46c2e332e81c51c4f1ee58b37198a3bd689556?s=50&d=blank&r=g)
Egi Adithia Pradana
[ October 6, 2014 at 1:31 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-323188)
hi
it possible if i want to reduce some LVM partition and use the empty space after reducing to extending another LVM partition such root?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-323188)
  68. ![](https://secure.gravatar.com/avatar/246558b332c0de4989e96f18615146240ec1e342af52c32e4a1c1837dfe2873b?s=50&d=blank&r=g)
kamesh
[ October 3, 2014 at 12:09 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-319386)
Nice document!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-319386)
  69. ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ August 13, 2014 at 8:20 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238808)
we can recover from metadata, Yes we can use LVM in raid. Going to write those articles soon. :) After thin-volumes.
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238808)
  70. ![](https://secure.gravatar.com/avatar/5221c795b1ead31139a51b27237e011e303543836b12d0c4e73dadfd889024aa?s=50&d=blank&r=g)
twisted87
[ August 13, 2014 at 4:00 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238229)
nice work!
What if a disk start to fail? How can I substitute it? Can I use LVM with a raid?
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238229)
  71. ![](https://secure.gravatar.com/avatar/924b0ee4166ecc502693dfa1453bc93182e6b74573a225d5fa9165080e5bdf05?s=50&d=blank&r=g)
Ashok P Gowda
[ August 13, 2014 at 2:48 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238190)
Great Explanation!!!!
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238190)
     * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ August 13, 2014 at 8:11 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238803)
@ Ashok P Gowda, Thanks dear
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-238803)
       * ![](https://secure.gravatar.com/avatar/506d121ddd507ea6406444eb12280087a7eff82a35367b4767059c6eaff23f59?s=50&d=blank&r=g)
OLUYOMI
[ October 25, 2014 at 2:50 am  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-346108)
Hello, Pls i am trying to Reduce a LVM to 150MB and i follow the below step but at the end of my step, iam not able to mount the Filesystem back as the systems tells me that i user do fuser .
2500
my steps:
umount /home
e2fsck /dev/mapper/vg_nw
resize2fs /dev/mapper/vg_new 150M
lvcreduce -L 150M /dev/mapper/vg_new
mount -a ………..This where the problems comes in, as i am not able to remount /home
df -h . pls advice , is it only possible to reduce to GB not MB? pls help me on this ASAP. my email is
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-346108)
         * ![](https://secure.gravatar.com/avatar/aee0f4132b51db24f8e9b0685778f38002014aae575549ca7881f21e71b58d9b?s=50&d=blank&r=g)
Babin Lonston
[ October 25, 2014 at 11:43 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-347222)
@OLUYOMI
We can reduce lvm to any size. May i know the size of your LVM ?
I’am assuming that you have a 500MB LVM with the name of lv_oluyomi and now you need to reduce it to 150MB ok.
I’am assuming that your volume group is vg_oluyomi and your logical volume mounted under /mnt/oluyomi.
1. First step you have to unmount the file system to reduce.
