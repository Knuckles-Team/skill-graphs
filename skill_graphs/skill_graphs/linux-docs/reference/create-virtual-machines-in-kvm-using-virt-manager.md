[Skip to content](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/)
Menu
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
  * [Pro Courses](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/ "Linux Online Courses")
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


[](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/)
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
  * [Pro Courses](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/ "Linux Online Courses")
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


[](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/)
# How to Configure Custom Access and Error Log Formats in Nginx
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: November 22, 2017 Read Time: 6 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Nginx](https://www.tecmint.com/category/web-servers/nginx/) [Leave a comment](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/#respond)
**Nginx HTTP** server has a phenomenal logging facility which is highly customizable. In this article, we will explain how to configure you own formats for access and error logs for Nginx in Linux.
The aim of this guide is to help you understand how logs are generated, so as to configure custom log formats for purposes of debugging, troubleshooting or analysis of what unfolds within your web server as well as web applications (such as tracing requests).
**Read Also** : [4 Good Open Source Log Monitoring and Management Tools for Linux](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/)
This article is made of three sections which will enlighten you about configuring **access/error logs** and how to enable conditional logging in Nginx.
### Configuring Access Logs in Nginx
Under **Nginx** , all client requests to the server are recored in the **access log** in a specified format using the **ngx_http_log_module** module.
The default log file is **log/access.log** (usually **/var/log/nginx/access_log** on Linux systems) and the default format for logging is normally the combined or main format (this can vary from one distro to another).
The **access_log** directive (applicable in the http, server, location, if in location and limit except context) is used to set the log file and the **log_format** directive (applicable under the http context only) is used to set the log format. The log format is described by common variables, and variables that generated only at the time when a log is written.
The syntax for configuring a log format is:
```
log_format format_name 'set_of_variables_to_define_format';

```

and the syntax for configuring access log is:
```
access_log /path/to/log_file format_name;		#simplest form
OR
access_log /path/to/log_file [format [buffer=size] [gzip[=level]] [flush=time] [if=condition]];

```

The following is a excerpt from the default Nginx configuration file **/etc/nginx/nginx.conf** on **CentOS 7**.
/etc/nginx/nginx.conf
```
http {
	#main log format
	log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                               '$status $body_bytes_sent "$http_referer" '
                               '"$http_user_agent" "$http_x_forwarded_for"';

	access_log /var/log/nginx/access.log;
}

```

This log format yields the following log entry.
```
127.0.0.1 - dbmanager [20/Nov/2017:18:52:17 +0000] "GET / HTTP/1.1" 401 188 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"

```

The following is another useful logging format which we use for tracing requests to our web applications using the some of the default variables, it most importantly has the request ID and logs client location details (country, country code, region and city).
/etc/nginx/nginx.conf
```
log_format  custom '$remote_addr - $remote_user [$time_local] '
                         	     '"$request" $status $body_bytes_sent '
                      		     '"$http_referer" "$http_user_agent" '
                     		     '"$http_x_forwarded_for" $request_id '
                   		     '$geoip_country_name $geoip_country_code '
                  		     '$geoip_region_name $geoip_city ';

```

You can use it like this:
```
access_log  /var/log/nginx/access.log custom;

```

This will produce a log entry which appears like this.
```
153.78.107.192 - - [21/Nov/2017:08:45:45 +0000] "POST /ngx_pagespeed_beacon?url=https%3A%2F%2Fwww.example.com%2Fads%2Ffresh-oranges-1509260795 HTTP/2.0" 204 0 "https://www.suasell.com/ads/fresh-oranges-1509260795" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0" "-" a02b2dea9cf06344a25611c1d7ad72db Uganda UG Kampala Kampala

```

You can specify several logs using the **access_log** directives on the same level, here we are using more than one log file in the http context.
/etc/nginx/nginx.conf
```
http{
	##default log format
	log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                                	      '$status $body_bytes_sent "$http_referer" '
                                         '"$http_user_agent" "$http_x_forwarded_for"';

	##request tracing using custom format
	log_format custom '$remote_addr - $remote_user [$time_local] '
                                           '"$request" $status $body_bytes_sent '
                                           '"$http_referer" "$http_user_agent" '
                                           '"$http_x_forwarded_for" $request_id '
                                           '$geoip_country_name $geoip_country_code '
                                          '$geoip_region_name $geoip_city ';

	##this uses the default log format
	access_log /var/log/nginx/access.log;

	##this uses the our custom log format
	access_log /var/log/nginx/custom_log custom;
}

```

The following are more advanced logging configurations examples, which are useful for log formats that contain compression-related variables and for creating compressed log files:
```
access_log /var/log/nginx/custom_log custom buffer 32k;
access_log /path/to/log.gz compression  gzip  flush=5m;

```

### Configuring Error Logs in Nginx
In case **Nginx** experiences any glitches, it records information concerning them in the error log. These issues fall under different severity levels: **debug** , **info** , **notice** , **warn** , **error** (this is the default level and works globally), **crit** , **alert** , or **emerg**.
The default log file is **log/error.log** , but it is normally located in **/var/log/nginx/** on Linux distributions. The **error_log** directive is used to specify the log file, and it can be used in the main, http, mail, stream, server, location context (in that order).
You should also note that:
  * Configurations in the main context are always inherited by lower levels in the order above.
  * and configurations in the lower levels override the configurations inherited from the higher levels.


You can configure error logging using the following syntax:
```
error_log /path/to/log_file log_level;

```

For example:
```
error_log /var/log/nginx/error_log warn;

```

This will instruct Nginx to log all messages of type **warn** and more severe log level **crit** , **alert** , and **emerg** messages.
In the next example, messages of **crit** , **alert** , and **emerg** levels will be logged.
```
error_log /var/www/example1.com/log/error_log crit;

```

Consider the configuration below, here, we have defined error logging on different levels (in the http and server context). In case of an error, the message is written to only one error log, the one closest to the level where the error has appeared.
/etc/nginx/nginx.conf
```
http {
	log_format compression '$remote_addr - $remote_user [$time_local] '
                           '"$request" $status $body_bytes_sent '
                           '"$http_referer" "$http_user_agent" "$gzip_ratio"';

	error_log  /var/log/nginx/error_log  crit;

    	server {
		listen 80;
		server_name example1.com;

		#this logs errors messages for example1.com only
      		error_log  /var/log/nginx/example1.error_log  warn;
            	…...
	}

     	server {
		listen 80;
		server_name  example2.com;

		#this logs errors messages for example2.com only
        		error_log  /var/log/nginx/example1.error_log;
        		…….
    	}
}

```

If you use more than one **error_log** directives as in the configuration below (same level), the messages are written to all specified logs.
/etc/nginx/nginx.conf
```
server {
		listen 80;
		server_name example1.com;

      		error_log  /var/www/example1.com/log/error_log  warn;
		error_log  /var/log/nginx/example1.error_log  crit;
            	…...
	}

```

### Configuring Conditional Logging in Nginx
In some cases, we may want Nginx to perform conditional logging of messages. Not every message has to be logged by Nginx, therefore we can ignore insignificant or less important log entries from our access logs for particular instances.
We can use the **ngx_http_map_module** module which creates variables whose values depend on values of other variables. The parameters inside a map block (which should exist in the http content only) specify a mapping between source and resulting values.
For this kind of setting, a request will not be logged if the condition evaluates to `“0”` or an empty string. This example excludes requests with HTTP status codes **2xx** and **3xx**.
/etc/nginx/nginx.conf
```
http{
	map $status $condition {
		~^[23] 0;
    		default 1;
	}
	server{
		access_log  /path/to/access.log  custom if=$condition;
	}
}

```

Here is another useful example for debugging a web application in a development phase. This will ignore all messages and only log debug information.
/etc/nginx/nginx.conf
```

http{
	map $info  $debuggable {
    		default     0;
    		debug       1;
	}
	server{
		……..
		access_log /var/log/nginx/testapp_debug_access_log  debug if=$debuggable;
		#logs other requests
		access_log  /var/log/nginx/testapp_access.log  main;
		…….
	}
}

```

You can find out more information, including logging to syslog
That’s all for now! In this guide, we explained how to configure custom logging format for access and error logs in Nginx. Use the feedback form below to ask questions or share you thoughts about this article.
Tags [Nginx Tips](https://www.tecmint.com/tag/nginx-tips/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install WordPress with FAMP Stack in FreeBSD](https://www.tecmint.com/install-wordpress-in-freebsd-with-apache/)
Next article:
[How to Install Piwik (Alternative to Google Analytics) in Linux](https://www.tecmint.com/install-piwik-alternative-to-google-analytics-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[![Disk Usage Monitoring Script in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/linux-disk-usage-monitoring-shell-script.webp)](https://www.tecmint.com/monitor-disk-usage-bash-script/ "A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%")
[A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%](https://www.tecmint.com/monitor-disk-usage-bash-script/)
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[How to Install ‘atop’ to Monitor Real-Time System Performance](https://www.tecmint.com/atop-linux-performance-monitoring/)
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
## Upgrade Your Linux Learning with Pro.Tecmint
**If you find TecMint helpful** , consider supporting us by subscribing to [**Pro.Tecmint.com**](https://pro.tecmint.com) – our premium platform with exclusive guides, ad-free experience, early access to tutorials, and much more.

Your support helps us keep creating quality Linux content for everyone.
[ Get Lifetime Access ](https://pro.tecmint.com)
## Linux Commands and Tools
[5 Different Types of Shell Commands and Their Usage in Linux](https://www.tecmint.com/understanding-different-linux-shell-commands-usage/)
[How to Keep ‘sudo’ Password Timeout Session Longer in Linux](https://www.tecmint.com/set-sudo-password-timeout-session-longer-linux/)
[How to Use sed and awk to Modify Config Files in Linux](https://www.tecmint.com/edit-configuration-files-using-sed-and-awk/)
[How to Reduce RAM & CPU Usage on Linux](https://www.tecmint.com/reduce-ram-cpu-usage-on-linux/)
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
[How to Check Timezone in Linux](https://www.tecmint.com/check-linux-timezone/)
## Linux Server Monitoring Tools
[How to Install Zabbix on RHEL/CentOS and Debian/Ubuntu – Part 1](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/)
[Nmon – Monitor Linux System and Network Performance](https://www.tecmint.com/nmon-linux-performance-monitor/)
[Trickle – Control Network Traffic Bandwidth Of Applications in a Linux](https://www.tecmint.com/limit-linux-network-bandwidth-usage-with-trickle/)
[Swatchdog – Simple Log File Watcher in Real-Time in Linux](https://www.tecmint.com/swatch-linux-log-file-watcher/)
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[How to Install Nagios 4 in Ubuntu and Debian](https://www.tecmint.com/install-nagios-core-in-ubuntu-and-debian/)
## Learn Linux Tricks & Tips
[How to Auto Execute Commands/Scripts During Reboot or Startup](https://www.tecmint.com/auto-execute-linux-scripts-during-reboot-or-startup/)
[How to Compress and Decompress a .bz2 File in Linux](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/)
[How to Repair and Defragment Linux System Partitions and Directories](https://www.tecmint.com/defragment-linux-system-partitions-and-directories/)
[How to Find Difference Between Two Directories Using Diff and Meld Tools](https://www.tecmint.com/compare-find-difference-between-two-directories-in-linux/)
[How to Test Website Loading Speed in Linux Terminal](https://www.tecmint.com/test-website-loading-speed-in-linux-terminal/)
[How to Delete Root Mails (Mailbox) File in Linux](https://www.tecmint.com/delete-root-mails-mailbox-file-in-linux/)
## Best Linux Tools
[8 Best RDP (Remote Desktop) Clients for Linux in 2024](https://www.tecmint.com/best-linux-rdp-remote-desktop-clients/)
[7 Best CCleaner Alternatives for Ubuntu](https://www.tecmint.com/ccleaner-alternatives-for-ubuntu/)
[4 Best Tools for Creating Fillable PDF Forms on Linux](https://www.tecmint.com/create-pdf-forms-linux/)
[10 Best PDF Document Viewers for Linux Systems](https://www.tecmint.com/linux-pdf-viewers-and-readers-tools/)
[5 GUI Tools to Free Up Space on Debian, Ubuntu and Linux Mint](https://www.tecmint.com/free-disk-space-ubuntu-linux-mint/)
[17 Best KDE Multimedia Applications for Linux](https://www.tecmint.com/kde-multimedia-applications/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/configure-custom-access-and-error-log-formats-in-nginx/ "Scroll back to top")
Search for:
