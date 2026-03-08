## Comment navigation
[← Older Comments](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/comment-page-1/#comments)
  1. Everything works fine, except when sending emails roundcube gives an error and does not send emails. It can receive emails.
```

Error message :  SMTP Error (): Connection to server failed

```

Outlook works fine)
Please advise
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2246725)
     * @Nadun,
It seems like the issue is with Roundcube’s SMTP configuration.
Make sure that the SMTP hostname, port, and encryption (SSL/TLS) settings in Roundcube are correct.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2246909)
  2. I followed every step I downloaded everything but the webmail said error 404.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2108881)
     * @Mario,
Make sure to verify the file and directory permissions, ensuring that the web server has the necessary access to the files. Incorrect permissions could result in a 404 error.
Also, check your configuration settings to ensure they are correctly set up like database connections, and any other relevant configuration details.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2109066)
  3. Thanks for the helpful tutorial.
I have done everything, of course, I am using nginx. I got an error when I am using the command:
```
# telnet gmail-smtp-in.l.google.com 25

```

The error is:
```
Trying 108.177.15.26...
Trying 2a00:1450:400c:c0c::1a...
telnet: Unable to connect to remote host: Network is unreachable

```

I test 587 and 465 ports and they go the same. However, this one goes well: “telnet smtp.gmail.com 587”.
Now in my roundcube panel, I try to send an email and I get this error in the roundcube log:
```
PHP Error: Connection refused
PHP Error: Failed to connect socket: Connection refused
SMTP Error: Connection failed:  (Code: -1) in /var/www/html/roundcube/program/lib/Roundcube/rcube.php on line 1794

```

And another problem is that I receive no emails. No emails are shown in my roundcube panel.
Does anyone know the solutions?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2043875)
     * @Farhad,
The error message you’re encountering, “**Network is unreachable** “, typically indicates that your system is unable to establish a network connection to the target IP addresses.
This can be due to several reasons such as internet connection issues, network configuration issues, or firewalls or security software blocking a request…
The “**Connection refused** ” and “**Failed to connect socket** ” errors indicate that the **Roundcube** application is unable to establish a connection to the SMTP server.
I suggest you check your SMTP server configuration, firewall, or selinux restricting connection, or check that the PHP socket extension is enabled in the PHP configuration. Also, make sure to check SMTP server logs for more information.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2044241)
  4. I’m getting an smtp error on the test…
SMTP send: NOT OK(Connection failed: (Code: -1))”
Please help me…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2014943)
  5. I did the tutorial step by step and actually everything is working but it created a new ip and now I can’t do it locally (my local IP just to work in my virtual machines) and I can’t open the roundcube page because of it!, just the Apache default one that runs on my ip.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2014005)
  6. Hi, I’m new to this and in step 17 I got lost, I didn’t know how to create what “**config.inc.php** ” asks for, I deleted the installer as requested, but now the domain no longer works for me, I get:
DATABASE ERROR: CONNECTION FAILED!
Unable to connect to the database!
Please contact your server-administrator.
I don’t know what to do, help.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2012829)
     * @Alexis,
The **config.inc.php** file is saved to the **/var/www/html/roundcubemail/config** directory.
Please check if the file is there, if not, create **config.inc.php** file by using the **defaults.inc.php** file.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2012840)
  7. Hello Bro,
I have already installed the LAMP server on UBUNTU 22.04 Can I install postfix roundcube now or do I need a fresh machine? I am using DigitalOcean hosting.
Please reply as soon as possible.
My application is in trouble with e-mail
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2004110)
     * @Pardeep,
You can install the Roundcube email client on the same machine, no need to have a fresh system…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2004210)
       * Okay, brother Thanks for the quick response…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-2004223)
  8. How about ssl configuration for the mail server?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1799085)
  9. Is there any advantage to joining the Ubuntu machine to our Active Directory domain before installing the email server?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1729222)
  10. So I did everything like the tutorial but apache says that this url doesnt exist.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1607690)
     * Have you registered your domain ??
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1715035)
  11. Hello,
Is it possible to do this without a fixed IP address? With a dynamic DNS for example? Is it possible to change the DNS records automatically when the external IP changes?
Thanks,
Isaiah
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1607583)
     * Yeah, you can change the Records automatically with your script or a **dyndns** client. But with dynamic IP will not have the Reverse DNS that will be a problem for your mail server.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1686763)
  12. Can anyone please suggest a very good cloud server site apart from digitalocean and vultr?
Anyone with open port 25.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1564624)
     * Linode Hosting –
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1607827)
  13. Hi all,
How to create users for dovecot?
I tried as mentioned in this tutorial but it’s impossible to connect in Roundcube.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1563791)
     * @Jacques,
What error are you getting while logging into Roundcube as a user?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1564318)
       * I can’t connect. I type in the login and password created as indicated but I can’t connect. I have no error message on the interface.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1564370)
         * Someone, to help me?
How to create users who can connect to Roundcube?
My server is Ubuntu 20
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1565253)
  14. I am sorry for my bad English, this my problem, with postfix in Linux.
I work in a single vps, with two wordpress,” contact form send mail just for mail “contact@domain1.com”,
```
contact@domain2.com  contact@domain2.com:passwd-2
contact@domain1.com  contact@domain1.com:passwd-1
[smtp.zoho.com]:587  contact@domain1.com:passwd-1

```

If I change file **sasl_passwd** like this contact form send mail just for **"contact@domain2.com",:**
```
contact@domain2.com  contact@domain2.com:passwd-2
contact@domain1.com  contact@domain1.com:passwd-1
[smtp.zoho.com]:587  contact@domain2.com:passwd-2          <<<<<<

```

If I use shell to send mail like this, both cases work perfectly :
```
echo "this is the mail2" | sendmail -F "Bogus User" -f  contact@domain1.com contact@domain1.com
echo "this is the mail2" | sendmail -F "Bogus User" -f  contact@domain2.com contact@domain2.com

```

So I need to find a problem with config wordpress or config postfix?
If there solution how to send a message from both wordpress, please help,
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1530483)
  15. Could you update the guide for SASL authentication (openssl) and thunderbird add email account please?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1508906)
     * @John,
I Will update the article with SASL authentication and thunderbird as an email client soon…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1509520)
  16. I have a problem regarding step no 2 I am using the ubuntu 20.04 server but this command is not working terminal says unable to locate the package **php-net-ldap3** kindly help me.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1482792)
  17. On point 16. access webmail. I get an URL not found.
Apache/2.4.41 (Ubuntu) Server at example Port 80
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1416926)
  18. Hi, thank you for this tutorial! I do have one tiny problem though. When I want to access the login page it gives me ‘ Unable to connect to the database, please contact your administrator “. I followed everything to the point. please help!
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1416919)
  19. Hi, may I use the PostgreSQL database for this setup?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1410612)
  20. I installed **Roundcube** as described in the HowTo. When I enter the server/install URL, I get a 404. If I enter the URL for the root of the server, I get the following:
CONFIGURATION ERROR
config.inc.php was not found.
Please read the INSTALL instructions!
I also noticed that there were no instructions for configuring the **http.conf** file, somehow there is something that is not being configured. Can you give me a couple of pointers on where to look?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1408238)
     * @Frank,
Check Step 7, point 14 for Apache configuration for Roundcube…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1408470)
  21. Most of the buttons on the Roundcube interface are un-clickable and grayed out. Why is this?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1395575)
  22. In step 2, many packages could not be found (I use a Debian 10 server).
Terminal info:
root@Server007:/etc/apache2/sites-enabled# sudo apt install apache2 apache2-utils mariadb-server mariadb-client php7.4 libapache2-mod-php7.4 php7.4-mysql php-net-ldap2 php-net-ldap3 php-imagick php7.4-common php7.4-gd php7.4-imap php7.4-json php7.4-curl php7.4-zip php7.4-xml php7.4-mbstring php7.4-bz2 php7.4-intl php7.4-gmp php-net-smtp php-mail-mime php-net-idna2 mailutils
Reading package lists… Done
Building dependency tree
Reading state information… Done
Package php-net-ldap2 is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
Package php-net-ldap3 is not available but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
E: Unable to locate package php7.4
E: Couldn’t find any package by glob ‘php7.4’
E: Couldn’t find any package by regex ‘php7.4’
E: Unable to locate package libapache2-mod-php7.4
E: Couldn’t find any package by glob ‘libapache2-mod-php7.4’
E: Couldn’t find any package by regex ‘libapache2-mod-php7.4’
E: Unable to locate package php7.4-mysql
E: Couldn’t find any package by glob ‘php7.4-mysql’
E: Couldn’t find any package by regex ‘php7.4-mysql’
E: Package ‘php-net-ldap2’ has no installation candidate
E: Package ‘php-net-ldap3’ has no installation candidate
E: Unable to locate package php7.4-common
E: Couldn’t find any package by glob ‘php7.4-common’
E: Couldn’t find any package by regex ‘php7.4-common’
E: Unable to locate package php7.4-gd
E: Couldn’t find any package by glob ‘php7.4-gd’
E: Couldn’t find any package by regex ‘php7.4-gd’
E: Unable to locate package php7.4-imap
E: Couldn’t find any package by glob ‘php7.4-imap’
E: Couldn’t find any package by regex ‘php7.4-imap’
E: Unable to locate package php7.4-json
E: Couldn’t find any package by glob ‘php7.4-json’
E: Couldn’t find any package by regex ‘php7.4-json’
E: Unable to locate package php7.4-curl
E: Couldn’t find any package by glob ‘php7.4-curl’
E: Couldn’t find any package by regex ‘php7.4-curl’
E: Unable to locate package php7.4-zip
E: Couldn’t find any package by glob ‘php7.4-zip’
E: Couldn’t find any package by regex ‘php7.4-zip’
E: Unable to locate package php7.4-xml
E: Couldn’t find any package by glob ‘php7.4-xml’
E: Couldn’t find any package by regex ‘php7.4-xml’
E: Unable to locate package php7.4-mbstring
E: Couldn’t find any package by glob ‘php7.4-mbstring’
E: Couldn’t find any package by regex ‘php7.4-mbstring’
E: Unable to locate package php7.4-bz2
E: Couldn’t find any package by glob ‘php7.4-bz2’
E: Couldn’t find any package by regex ‘php7.4-bz2’
E: Unable to locate package php7.4-intl
E: Couldn’t find any package by glob ‘php7.4-intl’
E: Couldn’t find any package by regex ‘php7.4-intl’
E: Unable to locate package php7.4-gmp
E: Couldn’t find any package by glob ‘php7.4-gmp’
E: Couldn’t find any package by regex ‘php7.4-gmp’
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1394028)
     * @Michael,
I think PHP 7.4 not included in the official Debian repository. If you still want to install PHP 7.4 on Debian 10, you need to enable SURY PHP PPA repository and then install PHP 7.4 on Debian 10 or Debian 9 as shown.
### Install PHP 7.4 on Debian 10
```
$ sudo apt -y install lsb-release apt-transport-https ca-certificates
$ sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
$ echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list
$ sudo apt update
$ sudo apt install apache2 apache2-utils mariadb-server mariadb-client php7.4 libapache2-mod-php7.4 php7.4-mysql php-net-ldap2 php-net-ldap3 php-imagick php7.4-common php7.4-gd php7.4-imap php7.4-json php7.4-curl php7.4-zip php7.4-xml php7.4-mbstring php7.4-bz2 php7.4-intl php7.4-gmp php-net-smtp php-mail-mime php-net-idna2 mailutils

```
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1394080)
  23. Thanks for this tutorial. It was really helpful.
However, I can get emails from Roundcube but I cannot send emails from that interface. I get the following error: SMTP Error (-1): Connection to server failed.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1387067)
  24. Pretty much every package failed to load / could not be found when running step 2
Reading package lists… Done
Building dependency tree
Reading state information… Done
E: Unable to locate package php7.4
E: Couldn’t find any package by glob ‘php7.4’
E: Couldn’t find any package by regex ‘php7.4’
E: Unable to locate package libapache2-mod-php7.4
E: Couldn’t find any package by glob ‘libapache2-mod-php7.4’
E: Couldn’t find any package by regex ‘libapache2-mod-php7.4’
E: Unable to locate package php7.4-mysql
E: Couldn’t find any package by glob ‘php7.4-mysql’
E: Couldn’t find any package by regex ‘php7.4-mysql’
E: Unable to locate package php7.4-common
E: Couldn’t find any package by glob ‘php7.4-common’
E: Couldn’t find any package by regex ‘php7.4-common’
E: Unable to locate package php7.4-gd
E: Couldn’t find any package by glob ‘php7.4-gd’
E: Couldn’t find any package by regex ‘php7.4-gd’
E: Unable to locate package php7.4-imap
E: Couldn’t find any package by glob ‘php7.4-imap’
E: Couldn’t find any package by regex ‘php7.4-imap’
E: Unable to locate package php7.4-json
E: Couldn’t find any package by glob ‘php7.4-json’
E: Couldn’t find any package by regex ‘php7.4-json’
E: Unable to locate package php7.4-curl
E: Couldn’t find any package by glob ‘php7.4-curl’
E: Couldn’t find any package by regex ‘php7.4-curl’
E: Unable to locate package php7.4-zip
E: Couldn’t find any package by glob ‘php7.4-zip’
E: Couldn’t find any package by regex ‘php7.4-zip’
E: Unable to locate package php7.4-xml
E: Couldn’t find any package by glob ‘php7.4-xml’
E: Couldn’t find any package by regex ‘php7.4-xml’
E: Unable to locate package php7.4-mbstring
E: Couldn’t find any package by glob ‘php7.4-mbstring’
E: Couldn’t find any package by regex ‘php7.4-mbstring’
E: Unable to locate package php7.4-bz2
E: Couldn’t find any package by glob ‘php7.4-bz2’
E: Couldn’t find any package by regex ‘php7.4-bz2’
E: Unable to locate package php7.4-intl
E: Couldn’t find any package by glob ‘php7.4-intl’
E: Couldn’t find any package by regex ‘php7.4-intl’
E: Unable to locate package php7.4-gmp
E: Couldn’t find any package by glob ‘php7.4-gmp’
E: Couldn’t find any package by regex ‘php7.4-gmp’
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1386673)
     * @Ian,
Which Ubuntu release version you are using?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1387167)
  25. And before running **install-jsdeps.sh** you need to make overwrite the content of file jsdeps.json with this:
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1370890)
  26. UI does not work because of missing **jquery.js** files.
we need to execute bin/install-jsdeps.sh script to get those JS files.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1370886)
  27. Just in case people come across problem-related to packages php not loading, I had to install
```
php-pear
php-mbstring
php-xml
php-curl

```

over php7.4 to make it working.
sample error logs:
PHP Fatal error: Uncaught Error: Class ‘PEAR’ not found in /var/www/html/roundcubemail/program/lib/Roundcube/bootstrap.php:103\nStack trace:\n#0 /var/www/html/roundcubemail/program/include/iniset.php(62): require_once()\n#1 /var/www/html/roundcubemail/installer/index.php(43): require(‘/var/www/html/r…’)\n#2 {main}\n thrown in /var/www/html/roundcubemail/program/lib/Roundcube/bootstrap.php on line 103
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1370189)
  28. wow.. thanks. Now I can send and receive email from my own domain… thanks for this clear tutorial…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1365025)
     * @Winar
Many thanks for the useful feedback.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1365084)
  29. Why I cannot telnet to SMTP Gmail with port 25?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1362376)
     * @Fandi,
Check Port 25 is opened on your UFW firewall and also make sure that port 25 listening on the TCP socket using the netstat command.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1362584)
  30. Wow, this article just popped up in my RSS reader today.
IMHO:
Why on earth SquirrelMail? I have used it 14 yrs ago on my 50MB webspace, but it seems like since then it has not evolved – besides security fixes – at all.
It might still work just good enough for its purpose, but I think there are a couple of modern alternatives…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1362074)
     * @Sebastian,
We didn’t know that SquirrelMail development stopped. We will replace it with Roundcube.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1362231)
       * I don’t know for sure that development has “stopped”.
I thought it still is maintained for security patches.
But take a look at its homepage, it has barely seen updates in the last 5-6 yrs.
TIA for updating. I also use Roundcube, it’s a good alternative!
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1362258)
     * I have updated the article and included Roundcube webmail as suggested by you…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1362295)
  31. I have this problem:
ERROR: Config file ‘. ‘”config/config.php” not found. You need to ‘ . ‘configure SquirrelMail before you can use it.
‘; exit; } // If we are, go ahead to the login page. header(‘Location: src/login.php’); ?>
Run ./configure and can’t access rahimpenfriends.ddns.net/squirrelmail
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1355412)
  32. Hey, great tutorial. I had some problems at the end though.
If anyone is having the same problem on an **Apache2** server, of `www-data` not being able to write to **/var/local/squirrelmail/data** you have to create the directories, use chown to give it to `www-data` and give it write permissions with chmod.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1349504)
  33. I am getting this error on my apache2 php7.3:- Warning: session_set_cookie_params(): Cannot change session cookie parameters when session is active in /var/www/html/squirrelmail/functions/global.php on line 472.
Any solution??
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1340239)
  34. I can’t access the **domain.com** , I have already made sure that everything was correct and as it is. Please help me and contact me on my email if you are willing to help. this is for my final project.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1340215)
  35. I’m not sure why, but I am able to send Emails yet I can’t receive them. I’ve tried sending an email to myself, and I followed this tutorial perfectly, with the addition of changing `$data_dir` to **/var/www/html/squirrelmail/data/** so that my user can log in. I also opened ports 25,80,143,443.
Please help me…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1340160)
  36. Hi Guys,
Everything went well until Step 4.12 When I put `karanpatel.co/squirrelmail` in a Google browser (from a different computer) it gives me “internal error – server connection terminated” or sometimes “503 Service Unavailable – No server is available to handle this request”.
Just to add here, I’ve just recently bought this domain name for the sake of trying out to set up an email service on my Ubuntu VM (Ubuntu 19.10), I’ve got no website running with that domain – could that be a problem here?
Best Regards,
Karan Patel
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1337407)
  37. How to point the domain to it?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1335691)
  38. You should install this package to allow PHP to interface with apache2:
```
libapache2-mod-php

```

Do not forget to edit the **dir.conf** file to make `.php` have higher precedence than `.html` so that the mail server works. Afterward restart the server and it should work
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1335354)
  39. Loggin in with the user account is not a good idea tho. Most server configuration files can be read by all user and some of WordPress files can be written by all users (not by default). Your server will be vulnerable if one of your user accounts is exposed. It is better to use database based mail user account
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1334819)
  40. I can receive emails but no one receives mine…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1334584)
     * Got this message:
This is the mail system at host [DOMAIN].
I’m sorry to have to inform you that your message could not
be delivered to one or more recipients. It’s attached below.
For further assistance, please send mail to postmaster.
If you do so, please include this problem report. You can
delete your own text from the attached returned message.
The mail system
: host
gmail-smtp-in.l.google.com[2a00:1450:400c:c01::1b] said: 550-5.7.1
[2a02:c205:3002:4898::1] Our system has detected that this message
550-5.7.1 does not meet IPv6 sending guidelines regarding PTR records and
550-5.7.1 authentication. Please review 550-5.7.1

5.7.1 . d14si1503938wrn.307 – gsmtp (in reply to end of DATA command)
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1334585)
       * The problem seems to be Gmail related because outlook addresses get my emails…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1334587)
         * Yeah I fixed it :)
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1345320)
  41. Hi, first and foremost, this is a great page; I’m stuck in step 4.12 (installing SquirrelMail-access the webserver (login page)) because I’m getting the PHP code (plain text) instead of the login page in my browser.
I’m running an ubuntu 16.04 server and I will appreciate any help to fix this issue.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1333929)
  42. Hello there, I’m trying to set up my email, but when I try to log in, I get an error as below.
Error opening ../data/default_pref
Could not create an initial preference file!
/var/local/squirrelmail/data/ should be writable by user www-data
Please contact your system administrator and report this error.
What should I do?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1330045)
     * @Katumba,
Make the following directory writable by user **www-data**.
```
$ sudo chown -R www-data:www-data /var/local/squirrelmail/data/
$ sudo chmod -R 776 /var/local/squirrelmail/data/

```
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1330370)
  43. I had an issue like “**Error opening ../config/default_pref** ”
Could not create initial preference file!
/var/lib/squirrelmail/data/ should be writable by user www-data
Please contact your system administrator and report this error.”
I could fix it by changing the Data Directory in the General Options to **/var/www/html/squirrelmail/data**.
Hope this helps somebody
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1329556)
     * @MM,
Make the following directory writable by user www-data.
```
$ sudo chown -R www-data:www-data /var/local/squirrelmail/data/
$ sudo chmod -R 776 /var/local/squirrelmail/data/

```
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1330373)
  44. I work on my client’s Linux servers, and I found your article useful for me. I had permission issues though with the mail server but finally fixed it.
Thanks
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1329278)
     * @Adnan
Nice! Many thanks for the useful feedback.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1329343)
     * I can’t
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1336650)
  45. Hello,
I followed this article and the Sending mail work with **@localhost** and doesn’t work **@mydomain**.
I miss something?
FYI:
/var/log/mail.log & /var/log/mail.err doesn’t show error.
.
After sending it to **user2@localhost** , the sender has **user1@mydomain** and the mail is received by user2. by sending to **user2@mydomain** , nothing happens (status=bounced and nothing to tell that:25 is blocked = this mean it’s ok)
Regards,
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1328372)
     * @ElMokhtar
Have you tried using a valid domain like mydomain.com?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1328674)
       * Hello Aaron,
I mean by **@mydomain =** (My FQDN, in my case hostname.mycountrycode)
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1328758)
         * @ElMokhtar
Are there any relevant entries in the **/var/log/mail.err** file?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1328841)
     * Hi @ElMokhtar,
Maybe this can help :) `https://drive.google.com/file/d/17nii7skTJi9WfiGSs4BtNl24khY3nxBS/view?fbclid=IwAR1pa5DkFn_nIYUgNkq8mMInYKUFURs_4TJnxHeJBT8N_3kZ3RNRL6R7sOU`
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1328845)
  46. This is very grateful and easy to install and configure Postfix (MTA server), Dovecot (MDA server) and Squirrel (MUA server). this is how we can configure a complete mail server. Its easy and very fewer configurations involved.
I got the same error of permissions as:
Error opening ../data/default_pref
Could not create an initial preference file!
but it was resolved as I gave full rights to all required folders like:
```
# sudo chmod 777 ...

```
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1318479)
  47. Error opening ../data/default_pref
Could not create an initial preference file!
/var/local/squirrelmail/data/ should be writable by user www-data
Please contact your system administrator and report this error.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1314143)
  48. Hi there,
I read this article and follow all the instructions to set up the Squirrelmail and worked too.
When I login with **myusername** and password, it gives this error
`ERROR
 Error opening ../data/default_pref
 Could not create an initial preference file!
 /var/local/squirrelmail/data/ should be writable by user www-data
 Please contact your system administrator and report this error.`
This is the permission of folders `http://prntscr.com/qktqcb`.
And second thing via command line using this command `usermod -m -d /var/www/etraininghq/etraining etraining`.
`usermod: no changes`
Please help me if you have any solution.
Thanks in advance
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1310868)
     * Create the folder/folders, assign the perms to it, all good after that. It worked for me.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1314501)
  49. SquirrelMail version 1.4.22
By the SquirrelMail Project Team
ERROR
An unknown user or password is incorrect.
Go to the login page
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1310253)
  50. I feel like a total noob which I am, but even after assigning perms to `myusername:myusername` the login just wouldn’t succeed. It still gives me the Query: CAPABILITY error, and then in the logs, it says **mkdir() failed due to insufficient permissions**.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1309074)
  51. Hi, is it possible to login in thunderbird with this mail server?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307912)
     * @Anton,
Yes, you can use POP and Imap setting in Thunderbird to Login…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307956)
       * Oh okay thank you but where do I find my IMAP and SMTP link, because it’s asking me for this. And do I have to change some settings for this?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1308047)
  52. Simple question. can I build this on the same server I use to host my website? or does it have to be an independent server?
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307549)
     * @Abraham,
Not an issue, you can host the Mail server on the same server with Apache.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307650)
  53. Hi, This is a great guide, and I am a complete novice to all this. I have come across an issue and cannot figure out how to solve it.
When setting up, I got a screen asking about SSL as I have SSL setup on my server and a forced redirect to HTTPS. It asked me for a name, so I put in my hostname `mattemedia.co.uk`, and followed the rest of the guide.
Now when I go to open SquirrelMail login, I get a 404 – not available on port 443…
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307530)
     * @Matthew,
Please check the SSL and Mail logs, might you will find a solution to fix this problem..
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307653)
       * I’ve checked the logs and it just says ‘mailbox could not be auto created’
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1307658)
  54. Try the command `sudo a2enmod php7.0`.
[Reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#comment-1304306)


## Comment navigation
[← Older Comments](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/comment-page-1/#comments)
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
