## Step 6: Configure Apache for Cacti
Open a file called **/etc/httpd/conf.d/cacti.conf** with your choice of editor.
```
sudo vi /etc/httpd/conf.d/cacti.conf

```

Add the following lines to the file:
```
Alias /cacti /usr/share/cacti
<Directory /usr/share/cacti/>
    Options +FollowSymLinks
    AllowOverride None
    <IfModule mod_authz_core.c>
        # Apache 2.4
        Require all granted
    </IfModule>
    <IfModule !mod_authz_core.c>
        # Apache 2.2
        Order Deny,Allow
        Deny from all
        Allow from all
    </IfModule>
</Directory>

```

Save and close the file.
Finally, restart the **Apache** and **MariaDB** services to apply the changes.
```
sudo systemctl restart httpd
sudo systemctl restart mariadb

```
