[Skip to content](https://www.tecmint.com/amplify-nginx-monitoring-tool/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/amplify-nginx-monitoring-tool/ "Linux Online Courses")
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


[](https://www.tecmint.com/amplify-nginx-monitoring-tool/)
**Nginx** amplify is a collection of useful tools for extensively monitoring a open source Nginx web server and NGINX Plus. With NGINX Amplify you can monitor performance, keep track of systems running Nginx and enables for practically examining and fixing problems associated with running and scaling web applications.
It can be used to visualize and determine a Nginx web server performance bottlenecks, overloaded servers, or potential DDoS attacks; enhance and [optimize Nginx performance](https://www.tecmint.com/nginx-web-server-security-hardening-and-performance-tips/) with intelligent advice and recommendations.
In addition, it can notify you when something is wrong with the any of your application setup, and it also serves as a web application capacity and performance planner.
The Nginx amplify architecture is built on 3 key components, which are described below:
  * **NGINX Amplify Backend** – the core system component, implemented as a SaaS (Software as a Service). It incorporates scalable metrics collection framework, a database, an analytics engine, and a core API.
  * **NGINX Amplify Agent** – a Python application which should be installed and run on monitored systems. All communications between the agent and the SaaS backend are done securely over SSL/TLS; all traffic is always initiated by the agent.
  * **NGINX Amplify Web UI** – a user interface compatible with all major browsers and it is only accessible only via TLS/SSL.


The web UI displays graphs for Nginx and operating system metrics, allows for the creation of a user-defined dashboard, offers a static analyzer to improve Nginx configuration and an alert system with automated notifications.
### Step 1: Install Amplify Agent on Linux System
**1.** Open your web browser, type the address below and create an account. A link will be sent to your email, use it to verify the email address andlogin to your new account.
```
https://amplify.nginx.com

```

**2.** After that, log into your remote server to be monitored, via SSH and download the nginx amplify agent auto-install script using **curl** or [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/).
```
$ wget https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh
OR
$ curl -L -O https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh

```

**3.** Now run the command below with superuser privileges using the [sudo command](https://www.tecmint.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/), to install the amplify agent package (the **API_KEY** will probably be different, unique for every system that you add).
```
$ sudo API_KEY='e126cf9a5c3b4f89498a4d7e1d7fdccf' sh ./install.sh

```
![Install Nginx Amplify Agent](https://www.tecmint.com/wp-content/uploads/2018/01/install-nginx-amplify-agent-.png)Install Nginx Amplify Agent
**Note** : You will possibly get an error indicating that **sub_status** has not been configured, this will be done in the next step.
**4.** Once the installation is complete, go back to the web UI and after about 1 minute, you will be able to see the new system in the list on the left.
### Step 2: Configure stub_status in NGINX
**5.** Now, you need to setup **stub_status** configuration to build key **Nginx** graphs (**Nginx Plus** users need to configure either the **stub_status** module or the **extended status** module).
Create a new configuration file for **stub_status** under **/etc/nginx/conf.d/**.
```
$ sudo vi /etc/nginx/conf.d/sub_status.conf

```

Then copy and paste the following **stub_status** configuration in the file.
```
server {
    listen 127.0.0.1:80;
    server_name 127.0.0.1;
    location /nginx_status {
        stub_status;
        allow 127.0.0.1;
        deny all;
    }
}

```

Save and close the file.
**6.** Next, restart Nginx services to activate the **stub_status** module configuration, as follows.
```
$ sudo systemctl restart nginx

```

### Step 3: Configure Additional NGINX Metrics for Monitoring
**7.** In this step, you need to setup additional Nginx metrics to keep a close eye on your applications performance. The agent will gather metrics from active and growing **access.log** and **error.log** files, whose locations it automatically detects. And importantly, it should be allowed to read these files.
All you have to do is define a specific **log_format** as the one below in your main Nginx configuration file, **/etc/nginx/nginx.conf**.
```
log_format main_ext '$remote_addr - $remote_user [$time_local] "$request" '
                                '$status $body_bytes_sent "$http_referer" '
                                '"$http_user_agent" "$http_x_forwarded_for" '
                                '"$host" sn="$server_name" ' 'rt=$request_time '
                                'ua="$upstream_addr" us="$upstream_status" '
                                'ut="$upstream_response_time" ul="$upstream_response_length" '
                                'cs=$upstream_cache_status' ;

```

Then use the above log format when defining your **access_log** and the **error_log** log level should be set to **warn** as shown.
```
access_log /var/log/nginx/suasell.com/suasell.com_access_log main_ext;
error_log /var/log/nginx/suasell.com/suasell.com_error_log  warn;

```

**8.** Now restart Nginx services once more, to effect the latest changes.
```
$ sudo systemctl restart nginx

```

### Step 4: Monitor Nginx Web Server Via Amplify Agent
**9.** Finally, you can begin monitoring your Nginx web server from the **Amplify Web UI**.
![Nginx Amplify Overview](https://www.tecmint.com/wp-content/uploads/2018/01/nginx-amplify-overview.png)Nginx Amplify Overview ![Nginx Amplify Graph](https://www.tecmint.com/wp-content/uploads/2018/01/nginx-amplify-graphs-interface.png)Nginx Amplify Graph
To add a another system to monitor, simply go to **Graphs** and click on “**New System** ” and follow the steps above.
**Nginx Amplify Homepage** :
**Amplify** is a powerful SaaS solution for monitoring your OS, Nginx web server as well as Nginx based applications. It offers a single, unified web UI for keeping an eye on multiple remote systems running Nginx. Use the comment form below to share your thoughts about this tool.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Convert Images to WebP Format in Linux](https://www.tecmint.com/convert-images-to-webp-format-in-linux/)
Next article:
[How to Show Asterisks While Typing Sudo Password in Linux](https://www.tecmint.com/show-asterisks-sudo-password-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/amplify-nginx-monitoring-tool/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[![Disk Usage Monitoring Script in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/linux-disk-usage-monitoring-shell-script.webp)](https://www.tecmint.com/monitor-disk-usage-bash-script/ "A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%")
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/amplify-nginx-monitoring-tool/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/amplify-nginx-monitoring-tool/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)![](https://eb2.3lift.com/highlight)
