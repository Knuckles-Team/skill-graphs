[Skip to content](https://www.tecmint.com/timeout-http-requests/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/timeout-http-requests/ "Linux Online Courses")
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


[](https://www.tecmint.com/timeout-http-requests/)
As a Linux user with over 10 years of experience, I understand the importance of optimizing your system for performance and reliability. One common task that comes up in web servers and application management is controlling **HTTP** requests.
Specifically, setting a timeout for **HTTP** requests can help prevent your system from hanging or waiting indefinitely for a response from a server.
In this guide, I’ll walk you through the steps to timeout HTTP requests in Linux, covering different tools and configurations you can use to ensure your system is running smoothly.
## What is an HTTP Request Timeout?
An HTTP request timeout occurs when a client (like a browser or a script) sends a request to a server, but the server does not respond within a specified amount of time, which could be due to the server being too slow, overloaded, or unresponsive. In such cases, the client will stop waiting and return an error or timeout message.
Timeouts are crucial for ensuring that your system doesn’t waste resources waiting for responses from unresponsive servers. By setting appropriate timeouts, you can prevent delays, improve performance, and avoid [unnecessary load on your server](https://www.tecmint.com/understand-linux-load-averages-and-monitor-performance/ "Understand Linux Load Averages").
## Why Setting Timeout HTTP Requests?
There are several reasons why setting timeouts for HTTP requests is important:
  * **Avoid Server Overload** – Long-running HTTP requests can cause your server to become unresponsive or overloaded, especially when there are multiple requests.
  * **Improve System Performance** – By setting a timeout, you can ensure that your system isn’t waiting for too long for a response, which helps keep your resources free for other tasks.
  * **Better Error Handling** – Timeouts allow your system to fail gracefully when a server is unresponsive, rather than hanging indefinitely.
  * **Security** – Limiting the time spent waiting for a response can help mitigate the risk of certain types of attacks, such as **Denial of Service** (**DoS**) attacks.


## Methods for Setting Timeout HTTP Requests in Linux
There are several tools and methods available in Linux to manage HTTP request timeouts, let’s explore the most common ones.
### 1. Using curl for HTTP Request Timeout
[curl](https://www.tecmint.com/linux-curl-command-examples/ "Curl Command in Linux") is a command-line tool used for transferring data via URLs, which supports a wide range of protocols, including HTTP, and allows you to set timeouts for your requests.
To set a timeout in **curl** , use the `--max-time` option, which specifies the maximum time (in seconds) that **curl** will allow for the entire operation (including connection, data transfer, etc.). Once this time is exceeded, curl will abort the request.
```
curl --max-time 10 https://example.com

```

In this example, **curl** will wait for a maximum of **10** seconds for a response from `https://example.com`. If the server doesn’t respond within this time, **curl** will terminate the request and return an error.
### 2. Setting Timeouts in Apache HTTP Server
If you’re running a web server like **Apache** , you can configure timeouts directly in its configuration file (`httpd.conf` or `apache2.conf`).
Apache has two main timeout settings:
  * **Timeout** – This directive sets the maximum time the server will wait for a complete request from the client.
  * **ProxyTimeout** – This is used when **Apache** is acting as a reverse proxy and is waiting for a response from a backend server.


To set the **Timeout** directive in **Apache** , open the Apache configuration file and set the value for Timeout in seconds.
```
Timeout 60

```

This means Apache will wait for a maximum of 60 seconds for a request to be completed. If it takes longer, the server will return a timeout error.
Similarly, if you’re using Apache as a reverse proxy, you can set the **ProxyTimeout** directive:
```
ProxyTimeout 30

```

This sets the maximum time Apache will wait for a backend server response to 30 seconds.
### 3. Configuring Nginx for HTTP Timeout
**Nginx** is another popular web server, and it also provides several directives for controlling timeouts.
  * `client_header_timeout` – Defines the timeout for reading the client’s request header.
  * `client_body_timeout` – Defines the timeout for reading the client’s body.
  * `send_timeout` – Sets the timeout for sending data to the client.
  * `proxy_read_timeout` – Defines the timeout for reading a response from a proxied server.


To configure timeouts in **Nginx** , open the Nginx configuration file (`nginx.conf`) and set the desired timeout values.
```
http {
    client_header_timeout 10s;
    client_body_timeout 10s;
    send_timeout 10s;
    proxy_read_timeout 30s;
}

```

This configuration ensures that **Nginx** will wait no more than 10 seconds for client data and 30 seconds for a response from a proxied server.
### 4. Using wget for HTTP Request Timeout
Like [curl](https://www.tecmint.com/linux-curl-command-examples/ "Curl Command in Linux"), [wget](https://www.tecmint.com/10-wget-command-examples-in-linux/ "Wget Command in Linux") is another command-line tool used for downloading files from the web, which also supports setting timeouts.
To set a timeout in wget, use the `--timeout` option, which specifies the maximum time (in seconds) that **wget** will wait for a response from the server.
```
wget --timeout=15 https://example.com/file.zip

```

This command tells **wget** to wait a maximum of 15 seconds for a response before aborting the request.
### 5. Timeouts in PHP and Other Scripting Languages
If you’re using **PHP** or another server-side scripting language, you can also set timeouts for HTTP requests made within your scripts.
In PHP, you can use the `ini_set` function to configure the `max_execution_time` directive, which defines the maximum time a script is allowed to run.
```
ini_set('max_execution_time', 30); // 30 seconds

```

### 6. Timeouts in System-wide Network Settings
For system-wide timeout settings, you can configure the **TCP** connection timeout values using [sysctl command](https://www.tecmint.com/sysctl-command-examples/ "sysctl Command in Linux"). These settings control the time your system will wait for a TCP connection to be established or closed.
To set the **TCP** connection timeout, you can modify the following parameters in `/etc/sysctl.conf`:
  * `net.ipv4.tcp_fin_timeout` – Defines the time the system will wait for a connection to be closed.
  * `net.ipv4.tcp_keepalive_time` – Sets the time between keepalive probes.

```
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_time = 600

```

After editing the file, run the following command to apply the changes:
```
sysctl -p

```

##### Conclusion
Setting **HTTP** request **timeouts** in Linux is an essential task for managing server performance, security, and reliability.
Whether you’re using command-line tools like **curl** and **wget** , or configuring web servers like **Apache** or **Nginx** , you can easily control the maximum time your system will wait for a response from a server.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Move Files and Folders with Spaces on Linux](https://www.tecmint.com/linux-move-files-with-spaces/)
Next article:
[Beginner’s Guide to Android Studio and Kotlin Setup on Ubuntu 24.04](https://www.tecmint.com/android-studio-for-kotlin-development-in-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/timeout-http-requests/#respond)** or
## Related Posts
[![Create Apache Virtual Host in RHEL](https://www.tecmint.com/wp-content/uploads/2014/07/Create-Apache-Virtual-Host-in-RHEL.webp)](https://www.tecmint.com/apache-virtual-hosting-in-centos/ "How to Setup Apache Virtual Hosts in RHEL 9")
[![Monitor Apache Server Status](https://www.tecmint.com/wp-content/uploads/2014/01/Monitor-Apache-Server-Status.webp)](https://www.tecmint.com/monitor-apache-web-server-load-and-page-statistics/ "How to Monitor Apache Load with mod_status in Linux")
[![Apache htaccess Tips](https://www.tecmint.com/wp-content/uploads/2015/01/Apache-htaccess-Tips.webp)](https://www.tecmint.com/apache-htaccess-tricks/ "36 Useful Apache ‘.htaccess’ Tricks for Security and Performance")
[![Allow or Deny Access to Websites in Apache](https://www.tecmint.com/wp-content/uploads/2024/10/block-website-in-Apache.png)](https://www.tecmint.com/allow-deny-access-website-apache/ "How to Allow or Deny Access to Websites in Apache")
[![Enable mod_rewrite in .htaccess File](https://www.tecmint.com/wp-content/uploads/2024/10/Enable-mod_rewrite-in-htaccess-File.png)](https://www.tecmint.com/enable-mod_rewrite-in-htaccess/ "How to Enable mod_rewrite in .htaccess File")
[![Install Apache with Virtual Hosts on Debian 12](https://www.tecmint.com/wp-content/uploads/2019/08/Install-Apache-with-SSL-on-Debian.png)](https://www.tecmint.com/install-apache-with-ssl-on-debian/ "How to Host a Website with Apache & SSL on Debian 12")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/timeout-http-requests/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/timeout-http-requests/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=8851458667303342&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
