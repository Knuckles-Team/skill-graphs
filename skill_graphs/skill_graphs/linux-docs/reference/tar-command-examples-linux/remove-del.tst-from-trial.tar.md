# remove del.tst from ‘trial.tar’
$ tar -vf trial.tar –delete del.tst
#List tar ball contents.
$ tar -tf trial.tar
dellable.tst
MpPhNum.tst
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 22, 2013 at 5:57 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-74088)
Dear Ajay,
Thanks for your efforts, I will include in the list.
  49. ![](https://secure.gravatar.com/avatar/12d044d5b4e2a85c881ce9acf226d76b52eef4af7fecf719318a011683eaffac?s=50&d=blank&r=g)
Durgaprasad.r
[ October 13, 2013 at 1:31 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-56825)
Very nice article. It’s very clear and easily understandable. Thanks for sharing this.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-56825)
  50. ![](https://secure.gravatar.com/avatar/d1692c3b794b67bea470dd4336876986dc62bbed12114241b8c127d5a1fca7ba?s=50&d=blank&r=g)
Syed Zabi
[ September 3, 2013 at 2:18 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-40076)
Thank you its relly very helpful
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-40076)
  51. ![](https://secure.gravatar.com/avatar/7e5ca779cd6e2c500758e6237c0f7465ec01167a9bf5c3311bff96904558f9f2?s=50&d=blank&r=g)
Rishi Raj
[ August 30, 2013 at 11:06 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-38474)
Very helpful article. Thanks for writing and sharing.
I’ll check whether ‘z’ and ‘j’ switches for tar.gz and tar.bz2 are needed in the following commands, respectively:
tar -xvf thumbnails-14-09-12.tar.gz
tar -xvf videos-14-09-12.tar.bz2
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-38474)
  52. ![](https://secure.gravatar.com/avatar/d1e0b55d580657c32a26e3253f9c23ad03d6da9e428322839cd6b2cb50125f27?s=50&d=blank&r=g)
L Reddy
[ August 21, 2013 at 9:51 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-35256)
My english not good pls excuse me, my ? is
I want take daily backup and incremental backup but i don’t want more than 10 days backup file pls write cmd
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-35256)
  53. ![](https://secure.gravatar.com/avatar/e1efb00e1a1244d603823ff1c687d7533dd79fb7586d4297117fae276ce56f15?s=50&d=blank&r=g)
Volka Racho
[ July 3, 2013 at 12:51 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-30074)
Is there a way to resume a tar extract for a large file which was interupted due to script time out from the apache webserver?
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-30074)
  54. ![](https://secure.gravatar.com/avatar/86c42a1c2cbf7967ae4f474df3958ca6ad5127b9851fdb603cfc9afe8c1680be?s=50&d=blank&r=g)
Ivan
[ April 12, 2013 at 11:56 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-25609)
Any way to exclude a folder or subfoler or file with tar itself. (other than changing it’s chmod to 666)
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-25609)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 13, 2013 at 1:59 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-25672)
The tar command has options to exclude certain files. For example to exclude file ‘abc’ and ‘xyz’ you can use use the command as follows.
```
$ tar -zcvf /home/tecmint.tar.gz --exclude='abc' --exclude='xyz' /home/tecmint

```
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-25672)
       * ![](https://secure.gravatar.com/avatar/6826bec42a53d7665ca4c4738af7183fb13e4b2e825b947277d4fabe924b8d66?s=50&d=blank&r=g)
Arvind
[ November 7, 2013 at 6:46 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-66731)
Any way to exclude a folder or subfoler or file with tar itself.
You have mentioned a option to exclude a file, not folder.
Please correct it..
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-66731)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 7, 2013 at 6:57 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-66737)
Same command is used to exclude files and folders.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-66737)
  55. ![](https://secure.gravatar.com/avatar/92e1a7709875c2f2ad5ed8804aa2624bb5e07bb072085464b3760dd66e9ad92c?s=50&d=blank&r=g)
Abdul
[ February 20, 2013 at 11:35 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23305)
how about excluding some files and directories and ignoring files or directories when backing-up.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23305)
  56. ![](https://secure.gravatar.com/avatar/6ef01a026ef330a4f4cbfa5516be5ec3521e11deba03698a7ea1ac27777972f4?s=50&d=blank&r=g)
pablo7
[ February 12, 2013 at 9:39 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23167)
Don’t you need to add the “j” option to extract the bzipped tar file in example 6? I get errors when I don’t.
Thanks for the all the examples. I wish more were included in manpages.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23167)
     * ![](https://secure.gravatar.com/avatar/192248873790f6e3ec551c9a1b5a3c94c368fafcc92ce6639fe9fe5d00bac492?s=50&d=blank&r=g)
Christopher
[ February 13, 2013 at 1:41 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23170)
Some versions of tar will detect the compression type and will automatically decompress it with the correct program (gzip or bzip2). Others will always assume it’s a regular, uncompressed tar file unless you pass it a “z” or “j” option. Some older versions of GNU tar even used the “I” (capital i) instead of “j” for bzip2 compression, and this is mentioned in the man page. The most portable method (I believe) is to decompress the file and pipe it directly to tar for extraction/listing:
zcat archive.tgz | tar -xf –
bzcat archive.tbz | tar -xf –
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23170)
  57. ![](https://secure.gravatar.com/avatar/192248873790f6e3ec551c9a1b5a3c94c368fafcc92ce6639fe9fe5d00bac492?s=50&d=blank&r=g)
Christopher
[ February 12, 2013 at 9:26 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23165)
Number 18 does not do what you say it does. You say that it displays the size of an archive file in kilobytes, but what it actually does is creates a new gzip-compressed archive file (to an unnamed pipe) containing a single file (the archive file that you are supposedly “checking”) and displays the size of that new archive file in bytes (not in kilobytes).
Here’s an easier and faster way to display the size of an archive file (or any other type of file) in kilobytes:
ls -lk archive.tar
ls -lk archive.tar.gz
ls -lk archive.tar.bz2
(The -k option is not standard but is supported by at least the Linux and BSD versions of ls.)
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23165)
  58. ![](https://secure.gravatar.com/avatar/69d194e4caaa8397aef722424f9176e17a73a5672dc75e384b7105a4251ca7a3?s=50&d=blank&r=g)
pen
[ February 12, 2013 at 5:12 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23158)
Excellent tips, one more for the road: How to copy a directory structure
