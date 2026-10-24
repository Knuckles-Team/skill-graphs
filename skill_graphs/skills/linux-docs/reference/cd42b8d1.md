## Step 8: Access Cacti Web Interface
To access the **Cacti** web interface, you need to open port 80 on the firewall to allow inbound traffic on that port.
```
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --reload

```

You can now access **Cacti** via a web browser using the server’s IP address or domain name as shown.
```
http://your_server_ip/cacti
OR
http://domain.com/cacti

```

Now, follow the on-screen instructions to complete the installation process
```
User: admin
Password: admin

```
![Cacti User Login](https://www.tecmint.com/wp-content/uploads/2015/03/Cacti-User-Login.png)Cacti User Login
Next, change the default Cacti password.
![Change Cacti Admin Password](https://www.tecmint.com/wp-content/uploads/2015/03/Change-Cacti-Admin-Password.png)Change Cacti Admin Password
Accept Cacti License Agreement.
![Accept Cacti License Agreement](https://www.tecmint.com/wp-content/uploads/2015/03/Accept-Cacti-License-Agreement.png)Accept Cacti License Agreement
Next, the screen shows Pre-installation Checks for Cacti installation, please correct the suggested settings in your `/etc/php.ini` file as shown and restart Apache after making changes.
```
memory_limit = 800M
max_execution_time = 60
date.timezone = Asia/Kolkata

```
![Cacti Pre-installation Checks](https://www.tecmint.com/wp-content/uploads/2015/03/Cacti-Pre-installation-Checks.png)Cacti Pre-installation Checks
Similarly, you also need to grant access to the MySQL TimeZone database for user Cacti, so that the database is populated with global TimeZone information.
```
mysql> use mysql;
mysql> GRANT SELECT ON mysql.time_zone_name TO cacti@localhost;
mysql> flush privileges;

```
![Cacti MySQL Pre-Installation Checks](https://www.tecmint.com/wp-content/uploads/2015/03/Cacti-MySQL-Pre-Installation-Checks.png)Cacti MySQL Pre-Installation Checks
Please choose the installation Type as “**New Install** “.
![Select Cacti Installation Type](https://www.tecmint.com/wp-content/uploads/2015/03/Select-Cacti-Installation-Type.png)Select Cacti Installation Type
Make sure all the following directory permissions are correct before continuing.
![Cacti Directory Permission Checks](https://www.tecmint.com/wp-content/uploads/2015/03/Cacti-Directory-Permission-Checks.png)Cacti Directory Permission Checks
Make sure all of these **Critical Binary Locations and Versions** values are correct before continuing.
![Critical Binary Locations and Versions](https://www.tecmint.com/wp-content/uploads/2015/03/Critical-Binary-Locations-and-Versions.png)Critical Binary Locations and Versions
Please choose the default **Data Source Profile** to be used for polling sources.
![Select Data Source Profile](https://www.tecmint.com/wp-content/uploads/2015/03/Select-Data-Source-Profile.png)Select Data Source Profile
Please, choose the **Device Templates** that you wish to use after the Cacti Install.
![Select Cacti Device Templates](https://www.tecmint.com/wp-content/uploads/2015/03/Select-Cacti-Device-Templates.png)Select Cacti Device Templates
Set the **Server Collation** in your MySQL configuration file **/etc/my.cnf** under the **[mysqld]** section as shown.
```
[mysqld]
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci

```
![Set Server Collation](https://www.tecmint.com/wp-content/uploads/2015/03/Set-Server-Collation.png)Set Server Collation
Your Cacti Server is almost ready. Please confirm that you are happy to proceed.
![Cacti Installation Process](https://www.tecmint.com/wp-content/uploads/2015/03/Cacti-Installation-Process.png)Cacti Installation Process ![Installing Cacti Server](https://www.tecmint.com/wp-content/uploads/2015/03/Installing-Cacti-Server.png)Installing Cacti Server ![Cacti Dashboard](https://www.tecmint.com/wp-content/uploads/2015/03/Cacti-Dashboard.png)Cacti Dashboard
Congratulations! You have successfully installed **Cacti** on RHEL-based systems. You can now start monitoring your network infrastructure by adding devices, creating graphs, and setting up alerts within the Cacti web interface.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install ImageMagick 7 on Debian and Ubuntu](https://www.tecmint.com/install-imagemagick-on-debian-ubuntu/)
Next article:
[apt-fast: Speeds Up Your APT Package Downloads in Ubuntu](https://www.tecmint.com/fast-apt-download-packages/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#respond)** or
