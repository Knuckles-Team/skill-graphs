[Skip to content](https://www.tecmint.com/restore-schema-postgresql-database/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/restore-schema-postgresql-database/ "Linux Online Courses")
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


[](https://www.tecmint.com/restore-schema-postgresql-database/)
If you intend to restore only one or a few schemas from a **PostgreSQL** backup file, you can use the **pg_restore** command, which is used for restoring a particular PostgreSQL database from an archive created by **pg_dump** in non-plain-text formats.
In this guide, we will show how to restore a particular schema from a PostgreSQL database backup file using the **pg_restore** command-line tool.
### Restoring Database Schema from PostgreSQL Database
Here is an example **pg_restore** command that restores a selected schema from a PostgreSQL database backup file:
Let’s look at the meaning of each option in the above command:
  * `-d` – defines the target database name which must exist on the server, **pg_restore** connects to it and restores directly into the database.
  * `-n` or `--schema` – defines the name of the schema to be restored, it instructs **pg_restore** to restore only objects that are in the named schema.
  * `backup.dump` – the name of the database backup file. In this case, the backup is in a custom format, one of the formats supported by the **pg_dump** tool.


### Restoring Multiple Schemas from PostgreSQL Database
To restore multiple schemas, use multiple `-n` as shown.
```
$ pg_restore -d testdb -n schema_name1 -n schema_name2 -n schema_name3 backup.dump
OR
$ pg_restore -d testdb --schema=schema_name1 --schema=schema_name2 --schema=schema_name3 backup.dump

```

If you are restoring the backup file on a new server, ensure that the owner or user of the database as defined in the backup is created on the server before the restoration process is initiated.
### pg_restore Command Options
There are several other valuable **pg_restore** command-line options that you can use while performing a database restoration, we will cover a few below.
One useful option is the `-C` or `--create` option which you can use to instruct **pg_restore** to create the database (specified using the `-d` option) in case it doesn’t exist on the cluster before restoring it.
Here is an example command:
```
$ pg_restore -d testdb -C -n schema_name  backup.dump
OR
$ pg_restore -d testdb --create -n schema_name backup.dump

```

**Note** : When the `-C` option is employed, the database name **testdb** (in the above command) is only used to run the initial “**DROP DATABASE testdb** ” and “**CREATE DATABASE testdb** ” commands, but the data is restored into the database name that appears in the backup file.
Furthermore, if you use the `--clean` option, **pg_restore** will clean (drop) and recreate the target database before connecting to it.
```
$ pg_restore --clean -d testdb -n schema_name backup.dump

```

Additionally, you can also specify the number of jobs to run concurrently while performing the restoration, using the `-j` or `--number-of-jobs`. This flag tells **pg_restore** to run time-consuming steps such as loading data, creating indexes, or creating constraints concurrently using concurrent sessions of up to the specified number of jobs:
```
$ pg_restore -j 4 --clean -d testdb -n schema_name backup.dump
OR
$ pg_restore --number-of-jobs=4 --clean -d testdb -n schema_name backup.dump

```

The above option is affected by hardware factors such as the [number of CPU cores](https://www.tecmint.com/check-linux-cpu-information/ "Get CPU Information on Linux") and disk setup on the server, client, and network. Besides, it only supports the custom and directory archive formats.
For more information, check out the **pg_restore** man page as shown.
```
$ man pg_restore

```

**You might also like:**
  * [What is PostgreSQL? How Does PostgreSQL Work?](https://www.tecmint.com/what-is-postgresql-how-does-postgresql-work/ "What is PostgreSQ")
  * [How to Backup and Restore a PostgreSQL Database](https://www.tecmint.com/backup-and-restore-postgresql-database/ "Backup and Restore a PostgreSQL Database")
  * [10 Useful Websites for Learning PostgreSQL Database System](https://www.tecmint.com/learn-postgresql-database-system/ "Learning PostgreSQL Database System")
  * [How To Exclude a Schema While Restoring a PostgreSQL Database](https://www.tecmint.com/restore-schema-postgresql-database/ "Restore Schema from a PostgreSQL Database")


That’s all! **pg_restore** is one of the handy command-line tools for the PostgreSQL database management system. In this article, we have looked at how to restore a particular schema from a PostgreSQL database backup file.
For any queries or comments concerning this guide, use the feedback form below to reach us.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How To Install and Use Android Debug Bridge (adb) in Linux](https://www.tecmint.com/install-android-debug-bridge-linux/)
Next article:
[Have You Tried Virtualbox Unattended Guest OS Install?](https://www.tecmint.com/virtualbox-unattended-guest-install/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/restore-schema-postgresql-database/#respond)** or
## Related Posts
[![Install PostgreSQL on Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/10/Install-PostgreSQL-on-Ubuntu.webp)](https://www.tecmint.com/install-postgresql-on-ubuntu/ "How to Install and Use PostgreSQL 18 on Ubuntu 24.04 LTS")
[![Install PostgreSQL from Sources](https://www.tecmint.com/wp-content/uploads/2017/11/Install-PostgreSQL-from-Source-Code.png)](https://www.tecmint.com/install-postgresql-from-source-code-in-linux/ "How to Install PostgreSQL from Source in Linux")
[![Install PostgreSQL with pgAdmin on Debian](https://www.tecmint.com/wp-content/uploads/2017/08/Install-PostgreSQL-with-pgAdmin-on-Debian.png)](https://www.tecmint.com/install-postgresql-on-debian/ "How to Install PostgreSQL 16 and pgAdmin on Debian 12")
[![Install PostgreSQL on CentOS](https://www.tecmint.com/wp-content/uploads/2017/08/Install-PostgreSQL-on-CentOS-RedHat-Fedora.png)](https://www.tecmint.com/install-postgresql-on-centos-rhel-fedora/ "How to Install PostgreSQL 16 on RHEL-Based Distributions")
[![Backup and Restore PostgreSQL Database](https://www.tecmint.com/wp-content/uploads/2020/10/Backup-and-Restore-PostgreSQL-Database.png)](https://www.tecmint.com/backup-and-restore-postgresql-database/ "How to Backup and Restore a PostgreSQL Database in Linux")
[![Exclude Schema in PostgreSQL](https://www.tecmint.com/wp-content/uploads/2023/03/Exclude-Schema-in-PostgreSQL.png)](https://www.tecmint.com/exclude-schema-postgresql/ "How To Exclude a Schema While Restoring a PostgreSQL Database")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/restore-schema-postgresql-database/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/restore-schema-postgresql-database/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
