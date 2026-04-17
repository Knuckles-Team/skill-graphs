[Skip to content](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/ "Linux Online Courses")
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


[](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/)
Following the previous **Let’s Encrypt** tutorial regarding **Apache SSL** , in this article we’ll discuss how to generate and install a free SSL/TLS certificate issued by **Let’s Encrypt CA** for **Nginx** webserver on **Ubuntu** or **Debian**.
##### Also Read
  1. [Secure Apache with Free Let’s Encrypt on Ubuntu and Debian](https://www.tecmint.com/install-free-lets-encrypt-ssl-certificate-for-apache-on-debian-and-ubuntu/)
  2. [Install Let’s Encrypt SSL to Secure Apache on RHEL and CentOS](https://www.tecmint.com/install-lets-encrypt-ssl-certificate-to-secure-apache-on-rhel-centos/)


##### Testing Sample Environment
![Install Lets Encrypt to Secure Nginx on Ubuntu and Debian](https://www.tecmint.com/wp-content/uploads/2016/03/Install-Lets-Encrypt-on-Nginx-Ubuntu-Debian.png)Install Lets Encrypt to Secure Nginx on Ubuntu and Debian
#### Requirements
  1. A registered domain with valid DNS `A` records to point back to IP address of your server.
  2. A installed Nginx web server with enabled SSL and Vhost, in case you planning to [host multiple domains or subdomains](https://www.tecmint.com/install-nginx-with-virtual-hosts-and-ssl-certificate/).


### Step 1: Installing Nginx Web Server
**1.** On the first step install Nginx web server, if not installed already, by issuing the below command:
```
$ sudo apt-get install nginx

```
![Install Nginx Web Server on Ubuntu 14.04 and Debian 8](https://www.tecmint.com/wp-content/uploads/2016/03/Install-Nginx-Web-Server-on-Ubuntu-Debian.png)Install Nginx Web Server on Ubuntu 14.04 and Debian 8
### Step 2: Generate a Let’s Encrypt SSL Certificate for Nginx
**2.** Before generating a free SSL/TLS certificate, install **Let’s Encrypt** software in `/usr/local/` filesystem hierarchy with the help of **git** client by issuing the below commands:
```
$ sudo apt-get -y install git
$ cd /usr/local/
$ sudo git clone https://github.com/letsencrypt/letsencrypt

```

**3.** Although the procedure of getting a Certificate for **Nginx** is automated, you can still manually create and install a free SSL certificate for Nginx using Let’s Encrypt Standalone plugin.
This method requires that port **80** must not be in use on your system for a short period of time while Let’s Encrypt client validates the server’s identity before generating the certificate.
In case you are running Nginx already, stop the service by issuing the following command.
```
$ sudo service nginx stop
OR
$ sudo systemctl stop nginx

```

In case you’re running other service that binds on port **80** stop that service as well.
**4.** Confirm that port **80** is free by running the [netstat command](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/):
```
$ sudo netstat -tlpn | grep 80

```
![Check Current Listening Ports in Linux](https://www.tecmint.com/wp-content/uploads/2016/03/Check-Current-Listening-Ports-in-Linux.png)Check Current Listening Ports in Linux
**5.** Now it’s time to run `letsencrypt` in order to obtain a SSL Certificate. Go to **Let’s Encrypt** installation directory found in **/usr/local/letsencrypt** system path and run the **letsencrypt-auto** command by providing the certonly `--standalone` option and `-d` flag for each domain or subdomain you wish to generate a certificate.
```
$ cd /usr/local/letsencrypt
$ sudo ./letsencrypt-auto certonly --standalone -d your_domain.tld

```
![Obtain Let's Encrypt SSL Certificate](https://www.tecmint.com/wp-content/uploads/2016/03/Obtain-Lets-Encrypt-SSL-Certificate.png)Obtain Let’s Encrypt SSL Certificate
**6.** Enter the email address which will be used by Let’s Encrypt for lost key recovery or urgent notices.
![Enter Email Address](https://www.tecmint.com/wp-content/uploads/2016/03/Enter-Email-Address.png)Enter Email Address
**7.** Agree with the terms of the license by pressing Enter key.
![Accept Letsencrypt Agreement](https://www.tecmint.com/wp-content/uploads/2016/03/Accept-Letsencrypt-Agreement.png)Accept Letsencrypt Agreement
**8.** Finally, if everything went successful, a message similar to the screenshot below should appear on your terminal console.
![Letsencrypt Installation Finishes](https://www.tecmint.com/wp-content/uploads/2016/03/Letsencrypt-Installation-Finishes.png)Letsencrypt Installation Finishes
### Step 3: Install Let’s Encrypt SSL Certificate in Nginx
**9.** Now that your SSL Certificate has been generated is time to configure Nginx webserver to use it. The newly SSL certificates are placed in `/etc/letsencrypt/live/` under a directory named after your domain name. Run [ls command](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/) to list the Certificate files issued for your domain.
```
$ sudo ls /etc/letsencrypt/live/
$ sudo ls -al /etc/letsencrypt/live/caeszar.tk

```
![Letsencrypt SSL Certificates](https://www.tecmint.com/wp-content/uploads/2016/03/Letsencrypt-SSL-Certificates.png)Letsencrypt SSL Certificates
**10.** Next, open `/etc/nginx/sites-available/default` file with a text editor and add the following block after the first commented line that specifies the beginning of the SSL block. Use the below screenshot as guidance.
```
$ sudo nano /etc/nginx/sites-enabled/default

```

Nginx block excerpt:
```
# SSL configuration
        #
        listen 443 ssl default_server;
        ssl_certificate /etc/letsencrypt/live/caeszar.tk/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/caeszar.tk/privkey.pem;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
        ssl_dhparam /etc/nginx/ssl/dhparams.pem;

```
![Configure Nginx to Use Let's Encrypt SSL](https://www.tecmint.com/wp-content/uploads/2016/03/Configure-Nginx-to-Use-Lets-Encrypt-SSL.png)Configure Nginx to Use Let’s Encrypt SSL
Replace the domain name values for SSL certificates accordingly.
**11.** On the next step generate a strong **Diffie-Hellman** cipher in **/etc/nginx/ssl/** directory in order to protect your server against the **Logjam** attack by running the following commands.
```
$ sudo mkdir /etc/nginx/ssl
$ cd /etc/nginx/ssl
$ sudo openssl dhparam -out dhparams.pem 2048

```
![Generate Diffie Hellman Cipher for Nginx](https://www.tecmint.com/wp-content/uploads/2016/03/Generate-Diffie-Hellman-for-Nginx.png)Generate Diffie Hellman Cipher for Nginx
**12.** Finally, restart Nginx daemon to reflect changes.
```
$ sudo systemctl restart nginx

```

and test your SSL certificate by visiting the below URL.
```
https://www.ssllabs.com/ssltest/analyze.html

```
![Check Nginx Lets Encrypt SSL Certificate](https://www.tecmint.com/wp-content/uploads/2016/03/Check-Nginx-Lets-Encrypt-SSL-Certificate.png)Check Nginx Lets Encrypt SSL Certificate
### Step 4: Auto Renew Let’s Encrypt Nginx Certificates
**13.** Certificates issued by **Let’s Encrypt CA** are valid for 90 days. In order to auto renew the files before expiration date create `ssl-renew.sh` bash script in `/usr/local/bin/` directory with the following content.
```
$ sudo nano /usr/local/bin/ssl-renew.sh

```

Add the following content to `ssl-renew.sh` file.
```
#!/bin/bash

cd /usr/local/letsencrypt
sudo ./letsencrypt-auto certonly -a webroot --agree-tos --renew-by-default --webroot-path=/var/www/html/ -d your_domain.tld
sudo systemctl reload nginx
exit 0

```
![Auto Renew Nginx Lets Encrypt SSL Certificate](https://www.tecmint.com/wp-content/uploads/2016/03/Auto-Renew-Nginx-Lets-Encrypt-SSL-Certificate.png)Auto Renew Nginx Lets Encrypt SSL Certificate
Replace the `--webroot-path` variable to match your Nginx document root. Make sure the script is executable by issuing the following command.
```
$ sudo chmod +x /usr/local/bin/ssl-renew.sh

```

**14.** Finally add a cron job to run the script every two months at midnight in order to assure that your certificate will be updated in approximately 30 days before it expires.
```
$ sudo crontab -e

```

Add the following line at the bottom of the file.
```
0 1 1 */2 * /usr/local/bin/ssl-renew.sh >> /var/log/your_domain.tld-renew.log 2>&1

```
![Update Lets Encrypt SSL Certificates](https://www.tecmint.com/wp-content/uploads/2016/03/Update-Lets-Encrypt-SSL-Certificates.png)Update Lets Encrypt SSL Certificates
That’s it! Your Nginx server is now serving SSL content using a free **Let’s Encrypt SSL** certificate.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Deal: Learn Python Programming with Ultimate Python Coding Bundle $49](https://www.tecmint.com/learn-python-programming-online-with-ultimate-python-coding/)
Next article:
[Free: Master Android Coding With This No-Cost Bundle](https://www.tecmint.com/learn-android-programming-with-android-coding-bundle/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#respond)** or
## Related Posts
[![Fix “404 Not Found” Errors in Debian apt Update](https://www.tecmint.com/wp-content/uploads/2025/11/fix-apt-get-404-errors-debian.webp)](https://www.tecmint.com/fix-apt-get-404-errors-debian/ "How to Fix “404 Not Found” Errors in Debian During apt-get upgrade")
[![manage software in Debian using dpkg, apt, aptitude, Synaptic, and tasksel](https://www.tecmint.com/wp-content/uploads/2014/08/debian-dpkg-apt-aptitude-synaptic-tasksel.webp)](https://www.tecmint.com/debian-dpkg-apt-aptitude-synaptic-tasksel/ "How to Use dpkg, apt, aptitude, synaptic, and tasksel in Debian")
[![ufw setup ubuntu](https://www.tecmint.com/wp-content/uploads/2013/12/ufw-setup-ubuntu.webp)](https://www.tecmint.com/install-ufw-on-ubuntu-debian/ "UFW Firewall: How to Install, Configure, and Use It on Ubuntu/Debian")
[![Install ProtonVPN on Debian](https://www.tecmint.com/wp-content/uploads/2025/02/Install-ProtonVPN-on-Debian.webp)](https://www.tecmint.com/install-protonvpn-debian/ "How to Set Up ProtonVPN on Debian 12")
[![Installing Nvidia Drivers on Debian](https://www.tecmint.com/wp-content/uploads/2025/02/Installing-Nvidia-Drivers-on-Debian.webp)](https://www.tecmint.com/install-nvidia-drivers-debian/ "Installing Nvidia Graphics Drivers on Debian 12")
[![Auto Mount USB Drive in Linux](https://www.tecmint.com/wp-content/uploads/2025/01/auto-mount-usb-drive-linux.png)](https://www.tecmint.com/mount-usb-drive-on-linux-startup/ "How to Mount a USB Drive Every Time Linux Boots Up")
### 5 Comments
[Leave a Reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#reply-title)
  1. Hi Cezar, thanks for this tutorial. I followed all the steps, but when I tested it on **ssllabs** , I received this message: “Evaluation failed: unable to connect to the server”. The only reason I assume is that I don’t know what to do here: “Replace the domain name values for SSL certificates accordingly” …
My application is installed on the EC2 instance, NGINX is running, but does not respond over HTTPS. How can I check or proceed to resolve this?
Thank you for your help and time
[Reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#comment-1337369)
     * @Antionio,
Does your domain name was accessible from browser using HTTP and HTTPS? could you share your domain name to check at our end?
[Reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#comment-1337474)
  2. Your tutorials are inspired from real life experience? from production?
[Reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#comment-1229672)
  3. This tutorial is great, I can create https in my site. But I have questions. This tutorial can’t create https for multiple domain in the same server.
can you show another tutorial for create https for multiple domain, thanks
[Reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#comment-950013)
  4. Thanks for this great tutorial!
I’m a totally newbie in linux and server managing and took a little time to have my site secured.
[Reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#comment-796186)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/secure-nginx-with-lets-encrypt-ssl-certificate-on-ubuntu-and-debian/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
