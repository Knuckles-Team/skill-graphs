## Step 1: Install Required Packages in Linux
First, begin by updating your system’s package repository to ensure you have the latest versions of software packages available.
```
sudo dnf update

```

Next, install the necessary packages for **Cacti** and its dependencies using the following command.
```
sudo dnf install net-snmp-utils net-snmp-libs rrdtool php-mysqlnd php-snmp php-xml php-gd mariadb-server httpd

```
![Install Cacti Required Packages](https://www.tecmint.com/wp-content/uploads/2015/03/Install-Cacti-Required-Packages.png)Install Cacti Required Packages
