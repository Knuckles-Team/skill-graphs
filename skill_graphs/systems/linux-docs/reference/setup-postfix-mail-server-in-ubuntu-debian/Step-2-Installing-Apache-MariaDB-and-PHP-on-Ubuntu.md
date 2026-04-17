## Step 2: Installing Apache, MariaDB, and PHP on Ubuntu
**3.** To create a running mail server using “**Roundcube** ”, we’ll have to install **Apache2** , **MariaDB** , and **PHP** packages first, to do so, run.
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install apache2 apache2-utils mariadb-server mariadb-client php libapache2-mod-php php-mysql php-net-ldap2 php-net-ldap3 php-imagick php-common php-gd php-imap php-json php-curl php-zip php-xml php-mbstring php-bz2 php-intl php-gmp php-net-smtp php-mail-mime mailutils

```
![Installing Apache, MariaDB, and PHP on Ubuntu](https://www.tecmint.com/wp-content/uploads/2020/09/Install-LAMP-Stack.png)Installing Apache, MariaDB, and PHP on Ubuntu
