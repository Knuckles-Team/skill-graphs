## Step 7: Create an Apache Virtual Host for Roundcube Webmail
**14.** Create an Apache virtual host for **Roundcube** webmail.
```
sudo nano /etc/apache2/sites-available/roundcube.conf

```

Add the following configuration to it.
```
<VirtualHost *:80>
  ServerName tecmint.com
  DocumentRoot /var/www/html/roundcubemail/

  ErrorLog ${APACHE_LOG_DIR}/roundcube_error.log
  CustomLog ${APACHE_LOG_DIR}/roundcube_access.log combined

  <Directory />
    Options FollowSymLinks
    AllowOverride All
  </Directory>

  <Directory /var/www/html/roundcubemail/>
    Options FollowSymLinks MultiViews
    AllowOverride All
    Order allow,deny
    allow from all
  </Directory>

</VirtualHost>

```

**15.** Next, enable this virtual host and reload the Apache for the changes.
```
sudo a2ensite roundcube.conf
sudo systemctl reload apache2

```

**16.** You can now access the roundcube webmail by going to the following url.
```
http://yourdomain.com/roundcubemail/installer/

```
![Roundcube Webmail Installer](https://www.tecmint.com/wp-content/uploads/2020/09/Roundcube-Webmail-Installer.png)Roundcube Webmail Installer
**16.** Next, go to the Database settings and add the database details.
![Roundcube Webmail Database Settings](https://www.tecmint.com/wp-content/uploads/2020/09/Roundcube-Webmail-Database-Settings.png)Roundcube Webmail Database Settings
**17.** After making all the changes, create a `config.inc.php` file.
![Create Roundcube Configuration File](https://www.tecmint.com/wp-content/uploads/2020/09/Create-Roundcube-Configuration-File.png)Create Roundcube Configuration File
**18.** After finishing the installation and the final tests please delete the `installer` folder and make sure that `enable_installer` option in `config.inc.php` is disabled.
```
$ sudo rm /var/www/html/roundcubemail/installer/ -r

```

**19.** Now go to the login page and enter the username and password of the user.
```
http://yourdomain.com/roundcubemail/

```
![Roundcube Webmail Login](https://www.tecmint.com/wp-content/uploads/2020/09/Roundcube-Webmail-Login.png)Roundcube Webmail Login
