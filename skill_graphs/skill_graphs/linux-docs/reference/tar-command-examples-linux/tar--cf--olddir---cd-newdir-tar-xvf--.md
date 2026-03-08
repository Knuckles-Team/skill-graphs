# tar -cf – olddir | ( cd newdir; tar xvf – )
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23158)
     * ![](https://secure.gravatar.com/avatar/b2401a8750c97f502a4b55b7856feaace7e5811f4982631c281c33c52b060684?s=50&d=blank&r=g)
John Lauro
[ February 12, 2013 at 7:50 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23164)
That is handy, and often times faster than cp -r. Taking it one step further…
tar -cf – dir | ssh user@remotehost “cd /newparent ; tar xvf -”
rsync is faster keeping directories in sync, but tar is much faster the first time, especially with lots of small files.
or to go the other way, and clone a directory from remote to local:
ssh user@remotehost “cd /parent ; tar cf – dir” | tar xf –
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23164)
  59. ![](https://secure.gravatar.com/avatar/049363595fac590b664205648474bea7beeb01cb5fecd64bd6a536a63846a742?s=50&d=blank&r=g)
flatcap
[ February 12, 2013 at 4:55 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23157)
The examples in section 13 won’t work as you suggest.
You haven’t escaped the spaces in the filenames, so tar will try to add three files:
“file”, “1”, “file” (again) and “2”.
I suggest changing the example to use “file1” and “file2”.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23157)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 12, 2013 at 6:38 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23163)
Thanks for pointing out, corrected as you suggested.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23163)
       * ![](https://secure.gravatar.com/avatar/56b43b384d95d7b935972b392f762a5fb088287d4972000ff2049bf0d7afb15f?s=50&d=blank&r=g)
dragonmouth
[ June 7, 2021 at 1:13 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-1516790)
As of June 6, 2021 it still has not been corrected.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-1516790)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 7, 2021 at 12:26 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-1517071)
@Dragonmouth,
The command has been corrected now.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-1517071)
  60. ![](https://secure.gravatar.com/avatar/6bcf126fd6f259bfa9de4ac47868c0d7b32aa3c16da848ad683d87bd6a15a4ca?s=50&d=blank&r=g)
Zakaria
[ February 12, 2013 at 10:26 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-23151)
Brilliant
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-23151)
  61. ![](https://secure.gravatar.com/avatar/f7eff0688f5d3057b8f0a90b25ec3ede151461b55e71e9e79d82636f428ab45c?s=50&d=blank&r=g)
Miguel Mateos
[ December 18, 2012 at 7:41 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-7383)
I found this article very helpful, especially item #16. Thank you!
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-7383)
  62. ![](https://secure.gravatar.com/avatar/4eba3f53b67c4695135fd9f17b42b060278b8276d29b4c1fe4e79cead7bac825?s=50&d=blank&r=g)
Rajkumar.m
[ September 18, 2012 at 10:30 am  ](https://www.tecmint.com/tar-command-examples-linux/#comment-854)
Very Helpful
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-854)
     * ![](https://secure.gravatar.com/avatar/129ef42e6a362fa8ca8be2afd3d9c437712a5ff37f1957a6d74c2a79699bef8b?s=50&d=blank&r=g)
ayush pratap singh
[ October 10, 2014 at 12:15 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-328060)
Dear Ravi,
Please tell me the -A option example use to append tar files to an archive.
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-328060)
       * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 10, 2014 at 3:27 pm  ](https://www.tecmint.com/tar-command-examples-linux/#comment-328274)
Dear Ayush,
You can include additional files to an already created tar archive, just use the following command example to add or append files to any existing tar file.
```
# $ tar rvf tecmint.tar newfile

```
[Reply](https://www.tecmint.com/tar-command-examples-linux/#comment-328274)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/tar-command-examples-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
