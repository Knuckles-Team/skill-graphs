# 18 Tar Command Examples in Linux
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: November 16, 2023 Read Time: 7 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/) [100 Comments](https://www.tecmint.com/tar-command-examples-linux/#comments)
The Linux “**tar** ” stands for tape archive, which is used by a large number of **Linux/Unix** system administrators to deal with tape drive [backup in Linux](https://www.tecmint.com/linux-system-backup-tools/ "Backup Utilities for Linux Systems").
The **[tar command in Linux](https://www.tecmint.com/install-tar-in-centos-rhel-and-fedora/ "Install tar in Linux")** is used to rip a collection of files and directories into a highly compressed archive file commonly called **tarball** or **tar** , **gzip,** and **bzip** in **Linux**.
The **tar** is the most widely used command to create compressed archive files that can be moved easily from one disk to another disk or machine to machine.
![tar - A Linux Archiving Utility](https://www.tecmint.com/wp-content/uploads/2022/09/tar-archiving-utility.png)tar – A Linux Archiving Utility
In this article, we will be going to review and discuss various **tar command examples** including how to create archive files using (**tar** , **tar.gz,** and **tar.bz2**) compression, how to extract archive files, extract a single file, view the content of the file, verify a file, add files or directories to the existing archive file, estimate the size of tar archive file, etc.
**You might also like:**
  * [How to Install and Use 7zip in Linux](https://www.tecmint.com/7zip-command-examples-in-linux/ "Install and Use 7zip in Linux")
  * [How to Create RAR Files in Linux](https://www.tecmint.com/how-to-open-extract-and-create-rar-files-in-linux/ "Create RAR Files in Linux")
  * [PeaZip – Open Source WinRar and WinZip Alternative for Linux](https://www.tecmint.com/peazip-linux-file-manager-and-file-archive-tool/ "PeaZip - WinRar and WinZip Alternative Tool")


The main purpose of this guide is to provide various **tar command examples** that might be helpful for you to understand and become an expert in tar archive manipulation.

Table of Contents
Toggle
  * [1. Creating a Tar Archive File](https://www.tecmint.com/tar-command-examples-linux/#1_Creating_a_Tar_Archive_File)
  * [2. Creating a Tar Archive with Compression](https://www.tecmint.com/tar-command-examples-linux/#2_Creating_a_Tar_Archive_with_Compression)
  * [3. Creating a tar.bz2 File in Linux](https://www.tecmint.com/tar-command-examples-linux/#3_Creating_a_tarbz2_File_in_Linux)
  * [4. Extracting a Tar Archive](https://www.tecmint.com/tar-command-examples-linux/#4_Extracting_a_Tar_Archive)
  * [5. Extracting a Compressed tar.gz Archive](https://www.tecmint.com/tar-command-examples-linux/#5_Extracting_a_Compressed_targz_Archive)
  * [6. Extracting a tar.bz2 Archive](https://www.tecmint.com/tar-command-examples-linux/#6_Extracting_a_tarbz2_Archive)
  * [7. Listing Contents of tar Archive](https://www.tecmint.com/tar-command-examples-linux/#7_Listing_Contents_of_tar_Archive)
  * [8. Viewing Contents of tar.gz Archive](https://www.tecmint.com/tar-command-examples-linux/#8_Viewing_Contents_of_targz_Archive)
  * [9. Printing Contents of tar.bz2 Archive](https://www.tecmint.com/tar-command-examples-linux/#9_Printing_Contents_of_tarbz2_Archive)
  * [10. Extracting a Single File from an Archive](https://www.tecmint.com/tar-command-examples-linux/#10_Extracting_a_Single_File_from_an_Archive)
  * [11. Extracting Multiple Files from an Archive](https://www.tecmint.com/tar-command-examples-linux/#11_Extracting_Multiple_Files_from_an_Archive)
  * [12. Extract a Group of Files Using Wildcard in Linux](https://www.tecmint.com/tar-command-examples-linux/#12_Extract_a_Group_of_Files_Using_Wildcard_in_Linux)
  * [13. Appending Files to an Existing Archive](https://www.tecmint.com/tar-command-examples-linux/#13_Appending_Files_to_an_Existing_Archive)
  * [14. Verifying a Tar Archive File](https://www.tecmint.com/tar-command-examples-linux/#14_Verifying_a_Tar_Archive_File)
  * [15. Checking Tar Archive File Size](https://www.tecmint.com/tar-command-examples-linux/#15_Checking_Tar_Archive_File_Size)
  * [16. Excluding Files When Creating a Tar Archive](https://www.tecmint.com/tar-command-examples-linux/#16_Excluding_Files_When_Creating_a_Tar_Archive)
  * [17. Removing Files From a Tar Archive](https://www.tecmint.com/tar-command-examples-linux/#17_Removing_Files_From_a_Tar_Archive)
  * [18. Extracing File Extension From a Tar Archive](https://www.tecmint.com/tar-command-examples-linux/#18_Extracing_File_Extension_From_a_Tar_Archive)
  * [19. Tar Command Usage and Options](https://www.tecmint.com/tar-command-examples-linux/#19_Tar_Command_Usage_and_Options)


The below example of the **tar** command will create a **tar** archive file `tecmint-17-11-2023.tar` for a directory **/home/tecmint** in the current working directory.
See the example of the **tar** command in action.
```
tar -cvf tecmint-17-11-2023.tar /home/tecmint/

```
![Create Tar Archive File](https://www.tecmint.com/wp-content/uploads/2023/04/Create-Tar-Archive-File.png)Create a Tar Archive File
Let’s discuss each option used in the above **tar** command.
  * `c` – Creates a new **.tar** archive file.
  * `v` – Verbosely show the **.tar** file progress.
  * `f` – File name type of the archive file.


To create a compressed archive file, we use the option `'z'` (compress the archive using gzip). For example, the command below will generate a compressed file named `'MyImages-17-11-2023.tar.gz'` for the directory ‘**/home/MyImages** ‘. (Note: `'tar.gz'` and `'tgz'` are interchangeable terms).
```
tar cvzf MyImages-17-11-2023.tar.gz /home/tecmint/MyImages
OR
tar cvzf MyImages-17-11-2023.tgz /home/tecmint/MyImages

```
![Create a Compressed Tar Archive](https://www.tecmint.com/wp-content/uploads/2023/04/Creating-Tar-Archive-with-Compression.png)Create a Compressed Tar Archive
The **bz2** feature compresses and creates an archive file that is smaller in size compared to **gzip**. However, the **bz2** compression method requires more time for both compression and decompression, whereas **gzip** is faster in both processes.
To create a highly compressed new tar archive named **Phpfiles-org.tar.bz2** by bundling all files and subdirectories within the **/home/php** directory, use the `-j` option, which instructs **tar** to utilize the **bzip2** compression algorithm, resulting in a smaller file size for efficient storage and transfer.
**Note** : **tar.bz2** and **tbz** are similar terms, both referring to **tb2**.
```
tar cvfj Phpfiles-org.tar.bz2 /home/tecmint/php
OR
tar cvfj Phpfiles-org.tar.tbz /home/tecmint/php
OR
tar cvfj Phpfiles-org.tar.tb2 /home/tecmint/php

```
![Create a tar.bz2 file Linux](https://www.tecmint.com/wp-content/uploads/2023/04/Create-a-Compressed-Tar-Bz2-File.png)Create a tar.bz2 file Linux
To untar or extract a tar file, simply execute the following command using the `'x'` option (extract). For instance, the command below will untar the file named ‘**tecmint-17-11-2023.tar** ‘ in the present working directory.
```
tar -xvf tecmint-17-11-2023.tar

```

If you want to untar in a different directory then use option `-C` (**specified directory**).
```
tar -xvf tecmint-17-11-2023.tar -C /home/tecmint/

```

To extract the contents of a compressed tar archive file named “**MyImages-17-11-2023.tar.gz** “, use the following command.
```
tar -xvf MyImages-17-11-2023.tar.gz

```

If you would like to extract in a different directory, just use the option `-C`, which will extract the files into the specified directory as shown.
```
tar -xvf MyImages-17-11-2023.tar.gz -C /home/tecmint/

```

To uncompress the highly compressed **tar.bz2** file, simply use the following command, which will untar all the files from the archive file.
```
tar -xvf Phpfiles-org.tar.bz2

```

To list or view the contents of the tar archive file, simply run the following command with the `-t` option (list content), which will display a detailed list of files and directories contained within the ‘**tecmint-17-11-2023.tar** ‘ archive.
```
tar -tvf tecmint-17-11-2023.tar

```
![View Tar Contents Without Extracting](https://www.tecmint.com/wp-content/uploads/2023/04/List-Tar-Contents.png)View Tar Contents Without Extracting
The following command will display a detailed list of files and directories contained within the “**MyImages-17-11-2023.tar.gz** ” archive.
```
tar -tvf MyImages-17-11-2023.tar.gz

```
![View Tar.gz Contents Without Extracting](https://www.tecmint.com/wp-content/uploads/2023/04/List-Tar.gz-Contents.png)View Tar.gz Contents Without Extracting
The following command provides an overview of the contents within the “**Phpfiles-org.tar.bz2** ” archive without extracting the files.
```
tar -tvf Phpfiles-org.tar.bz2

```
![View Tar Contents Without Extracting](https://www.tecmint.com/wp-content/uploads/2023/04/View-Tar-Archive-Contents.png)View Tar Contents Without Extracting
To extract a single file named `wp-cron.php` from the archive **Phpfiles-org.tar.bz2** , use the following command. Make sure to provide the correct path to the file you wish to extract.
```
tar -xvf Phpfiles-org.tar.bz2 home/tecmint/php/wp-cron.php

```
![Extract File From Tar Archive](https://www.tecmint.com/wp-content/uploads/2023/04/Extract-File-From-Tar-Archive.png)Extract File From Tar Archive
To extract or untar multiple files from `tar`, `tar.gz`, and `tar.bz2` archive files, use the following command, which will extract files from the specified archive files.
```
tar -xvf tecmint-17-11-2023.tar "file1" "file2"
tar -zxvf MyImages-17-11-2023.tar.gz "file1" "file2"
tar -jxvf Phpfiles-org.tar.bz2 "file1" "file2"

```

To extract a group of files we use wildcard-based extracting. For example, to extract a group of all files whose pattern begins with `.php` from a `tar`, `tar.gz`, and `tar.bz2` archive files, use:
```
tar -xvf Phpfiles-org.tar --wildcards '*.php'
tar -zxvf Phpfiles-org.tar.gz --wildcards '*.php'
tar -jxvf Phpfiles-org.tar.bz2 --wildcards '*.php'

```

To add files or directories to the existing `tar`, `tar.gz`, and `tar.bz2` archive files, use the option `-r`, which will add the files to an existing archive file.
```
tar -rvf tecmint-14-09-12.tar xyz.txt
tar -rvf MyImages-14-09-12.tar.gz xyz.txt
tar -rvf Phpfiles-org.tar.bz2 xyz.txt

```

The following command will display a detailed list of files and directories contained within the specified archive file, allowing you to visually verify the archive’s contents. If the archive is corrupted or incomplete, this verification process may reveal errors during the listing.
```
tar -tvf Phpfiles-org.tar.bz2

```

To check the size of any `tar`, `tar.gz`, and `tar.bz2` archive file, use the following command, which will display the size of the archive file in Kilobytes (**KB**).
```
tar -czf - tecmint-14-09-12.tar xyz.txt | wc -c
tar -czf - MyImages-14-09-12.tar.gz xyz.txt | wc -c
tar -czf - Phpfiles-org.tar.bz2 xyz.txt | wc -c

```

To exclude certain files and directories while creating a tar archive file, you can use the following command with the `--exclude` an option that will exclude files and directories when creating the tar archive file as shown.
```
tar --exclude='file1.txt' -zcvf backup.tar.gz /home/tecmint
tar --exclude='/home/tecmint/uploads' -zcvf backup.tar.gz /home/tecmint

```

In the above command, we excluded file ‘**file1.txt** ‘ and ‘**uploads** ‘ directory from the **/home/tecmint** folder.
To exclude files with specific file extensions `(.txt)` when creating a tar archive file, use:
```
tar --exclude='*.txt' -zcvf backup.tar.gz /home/tecmint

```

The following tar command will delete a file or directory from an already created tar file using the `--delete` option, as shown.
```
tar --delete -f backup.tar.gz file1.txt
tar --delete -f backup.tar.gz '/home/tecmint/uploads'

```

The following tar command will only extract files with the specific extension `.png` from the tar archive file using the `--wildcards` option as shown.
```
tar -xvf backup.tar.gz --wildcards '*.png'

```

Understanding the following various options and usage patterns of the ‘**tar** ‘ command is essential for efficient file archiving, compression, and extraction.
  * `-c` – create an archive file.
  * `-x` – extract an archive file.
  * `-v` – show the progress of the archive file.
  * `-f` – filename of the archive file.
  * `-t` – viewing the content of the archive file.
  * `-u` – archives and adds to an existing archive file.
  * `-j` – filter the archive through bzip2.
  * `-z` – filter the archive through gzip.
  * `-r` – append or update files or directories to the existing archive files.
  * `-W` – Verify an archive file.
  * `-A` – concatenates the archive files.
  * `--wildcards` – Specify patterns in the UNIX tar command.
  * `--exclude` – excludes files and directories when creating the archive.
  * `--delete` – remove the file and directory from the archive.


That’s it for now, hope the above **tar command examples** are enough for you to learn, and for more information please use the **man tar** command.
```
# man tar

```

If you are looking to split any large tar archive file into multiple parts or blocks, just go through this article:
  * [How to Split Tar File Into Multiple Files of Certain Size](https://www.tecmint.com/split-large-tar-into-multiple-files-of-certain-size/ "Split Tar File Into Multiple Files")
  * [How to Download and Extract Tar Files with One Command](https://www.tecmint.com/download-and-extract-tar-files-with-one-command/ "Download and Extract Tar Files with One Command")


If we’ve missed any examples please do share with us via the comment box and please don’t forget to share this article with your friends. This is the best way to say thanks…..
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[What if Linus Torvalds Would Have Accepted Steve Jobs Offer?](https://www.tecmint.com/what-if-linus-torvalds-would-have-accepted-job-proposal-of-steve-jobs/)
Next article:
[How to Change and Secure Default PhpMyAdmin Login URL](https://www.tecmint.com/change-secure-phpmyadmin-login-url-page/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/tar-command-examples-linux/#respond)** or
