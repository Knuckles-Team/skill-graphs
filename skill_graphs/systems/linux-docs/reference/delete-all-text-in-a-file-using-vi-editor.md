[Skip to content](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/ "Linux Online Courses")
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


[](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/)
[Vim](https://www.tecmint.com/vim-8-0-install-in-ubuntu-linux-systems/) is a great tool for editing text or configuration files in Linux. One of the lesser-known [Vim tricks](https://www.tecmint.com/learn-vi-and-vim-editor-tips-and-tricks-in-linux/) is clearing or deleting all text or lines in a file. Although, this is not a frequently used operation, its a good practice to know or learn it.
In this article, we will describe steps on how to delete, remove or clear all text in a file using a Vim editor in different **vim modes**.
**Read Also** : [5 Ways to Empty or Delete a Large File Content in Linux](https://www.tecmint.com/empty-delete-file-content-linux/)
The first option is to remove, clear or delete the all lines in a file in the normal mode (note that Vim starts in “**normal** ” mode by default). Immediately after opening a file, type `“gg”` to move the cursor to the first line of the file, assuming it is not already there. Then type `dG` to delete all the lines or text in it.
![Delete Complete Text in Vi Editor](https://www.tecmint.com/wp-content/uploads/2019/04/Delete-Complete-Text-in-Vi-Editor.png)Delete Complete Text in Vi Editor
If **Vim** is in another mode, for example, **insert mode** , you can access normal mode by pressing `Esc` or `<**C-[**>`.
Alternatively, you can also clear all lines or text in Vi/Vim in **command mode** by running the following command.
```
:1,$d

```
![Delete Text in Vi Editor](https://www.tecmint.com/wp-content/uploads/2019/04/Delete-Text-in-Vi-Editor.png)Delete Text in Vi Editor
Last but not least, here is a list of Vim articles that you will find useful:
  1. [10 Reasons Why You Should Use Vi/Vim Text Editor in Linux](https://www.tecmint.com/reasons-to-learn-vi-vim-editor-in-linux/)
  2. [Learn Useful ‘Vi/Vim’ Editor Tips and Tricks to Enhance Your Skills](https://www.tecmint.com/learn-vi-and-vim-editor-tips-and-tricks-in-linux/)
  3. [How to Enable Syntax Highlighting in Vi/Vim Editor](https://www.tecmint.com/enable-syntax-highlighting-in-vi-editor/)
  4. [How to Password Protect a Vim File in Linux](https://www.tecmint.com/password-protect-vim-file-in-linux/)
  5. [6 Best Vi/Vim-Inspired Code Editors for Linux](https://www.tecmint.com/vi-vim-inspired-code-editors-for-linux/)
  6. [PacVim – A Game That Teaches You Vim Commands](https://www.tecmint.com/learn-vi-commands-with-pacvim-game/)


In this article, we have explained how to clear or delete all lines or text in a file using Vi/Vim editor. Remember to share your thoughts with us or ask questions using the comment form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Find openSUSE Linux Version](https://www.tecmint.com/find-opensuse-linux-version/)
Next article:
[3 Ways to Install Atom Text Editor in openSUSE](https://www.tecmint.com/install-atom-text-editor-in-opensuse/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 5 Comments
[Leave a Reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#reply-title)
  1. `1,$` is equal to `%`, hence `:%d` does do job with less keystrokes.
[Reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#comment-1187602)
  2. In insert mode, you can type `%d` to clear the text.
[Reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#comment-1151218)
     * @Jiaowen
Many thanks for sharing.
[Reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#comment-1152471)
  3. Wouldn’t it be simpler to just delete and then recreate the file using the file manager?
I know that CLI is generally faster and more efficient than GUI but in this case you are just unnecessarily complicating things by using CLI.
[Reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#comment-1133951)
     * @Dragonmouth
This article is intended to show users that Vim supports the explained option, especially after opening a file. Thanks for the feedback.
[Reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#comment-1135010)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
