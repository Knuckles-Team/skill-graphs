[Skip to content](https://www.tecmint.com/command-line-language-translators-for-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/command-line-language-translators-for-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/command-line-language-translators-for-linux/)
The importance of Language translation applications cannot be overemphasized especially for those who travel a lot or communicate with people who don’t share the same language on a regular basis.
Today, I introduce to you the best command-line based translation tools for Linux.
### 1. DeepL Translator CLI
**DeepL** , a German tech company and released under the MIT license.
The languages it supports include English (EN), German (DE), French (FR), Italian (IT), Dutch (NL), Spanish (ES), Russian, Portuguese, and Polish (PL) and while the terminal tool is free, **DeepL** offers subscription plans for interested users.
#### Install DeepL Translator CLI in Linux
To install **DeepL Translator** command-line tool, first you need to install the [latest version of Node.js](https://www.tecmint.com/install-nodejs-npm-in-centos-ubuntu/) in your Linux distribution.
Next, install **Yarn** package dependency manager using Debian package repository on **Debian** and **Ubuntu** distribution using following commands.
```
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
$ sudo apt-get update
$ sudo apt-get install yarn

```

On **CentOS** , **Fedora** and **RHEL** distribution, you can install **Yarn** via RPM package repository.
```
# curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
# yum install yarn  [On **CentOS/RHEL**]
# dnf install yarn  [On **Fedora**]

```

Now install **DeepL Translator** command-line tool using the following command.
```
$ yarn global add deepl-translator-cli

```

Verify the installation status by checking **DeepL** version.
```
$ deepl --version

```

**DeepL** works by making API calls to the main website at **deepl.com** so, at the moment, you need to be online to use it. It reportedly runs on a supercomputer capable of 5.1 petaFLOPS – enough speed to detect and translate languages in a blink.
#### DeepL Usage Examples
```
**# Translate text into German**
$ deepl translate -t 'DE' 'How do you do?'

**# Pipe text from standard input**
$ echo 'How do you do?' | deepl translate -t 'DE'

**# Detect language**
$ deepl detect 'Wie geht es Ihnen?'

**# For help**
$ deepl -h
$ deepl translate -h
$ deepl detect -h

```

### 2. Translate Shell
_**Google Translate CLI**_) is a free and open source command-line language translator tool powered by **Google Translate** , Yandex Translate, Apertium, and Bing Translator. It is available for most POSIX-compliant systems including Windows (via Cygwin, WSL, or MSYS2), GNU/Linux, macOS, and BSD.
**Translate Shell** allows users to use it for simple translations or as an interactive shell. For simple translations, **Translate Shell** gives details of the translated text by default unless when made to do exclude the details using the keyword, brief.
```
$ trans 'Saluton, Mondo!'
Saluton, Mondo!

Hello, World!

Translations of Saluton, Mondo!
[ Esperanto -> English ]
Saluton ,
    Hello,
Mondo !
    World!

```
```
$ trans -brief 'Saluton, Mondo!'
Hello, World!
```

When used as an interactive shell, it will translate the texts as you enter them line by line. For example,
```
$ trans -shell -brief
> Rien ne réussit comme le succès.
Nothing succeeds like success.
> Was mich nicht umbringt, macht mich stärker.
What does not kill me makes me stronger.
> Юмор есть остроумие глубокого чувства.
Humor has a deep sense of with.
> 幸福になるためには、人から愛されるのが一番の近道。
In order to be happy, the best way is to be loved by people.
```

#### Install Translate Shell in Linux
My recommended download method is for you to grab the self-contained executable file from
```
$ wget git.io/trans
$ chmod +x ./trans

```

For more details on installation and usage check its official GitHub page
Do you know other awesome command line text translator apps for Linux? Add your suggestions in the comments section below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Find Linux Server Geographic Location in Terminal](https://www.tecmint.com/find-linux-server-geographic-location/)
Next article:
[How to Setup Secure Private Chat Server with Ytalk over SSH](https://www.tecmint.com/setup-secure-private-chat-server-with-ytalk-over-ssh/)
![Photo of author](https://secure.gravatar.com/avatar/39b3c5bde91d4db16987908aad18f4fbaa639710336d8037877ecfd57683431a?s=100&d=blank&r=g)
Martins D. Okoi
Martins Divine Okoi is a graduate of Computer Science with a passion for Linux and the Open Source community. He works as a Graphic Designer, Web Developer, and programmer.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/command-line-language-translators-for-linux/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 4 Comments
[Leave a Reply](https://www.tecmint.com/command-line-language-translators-for-linux/#reply-title)
  1. Just to know, Deepl shell translator is not anymore working (API$ policy, :-))
[Reply](https://www.tecmint.com/command-line-language-translators-for-linux/#comment-2187754)
  2. Help: deepl-translate(1) does not exist, try `--help`.
[Reply](https://www.tecmint.com/command-line-language-translators-for-linux/#comment-1154567)
     * Have you installed DeepL?
Run “`deepl --version`” and if the version displays, run “`deepl --help`“.
[Reply](https://www.tecmint.com/command-line-language-translators-for-linux/#comment-1155157)
     * Based on this issue (
[Reply](https://www.tecmint.com/command-line-language-translators-for-linux/#comment-1203679)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/command-line-language-translators-for-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/command-line-language-translators-for-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
