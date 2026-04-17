## Step 6: Installing Roundcube Webmail in Ubuntu
**11.** Roundcube is the webmail server that you’ll be using to manage emails on your server, it has a simple web interface to do the job, it can be customized by installing more modules & themes.
```
wget https://github.com/roundcube/roundcubemail/releases/download/1.6.6/roundcubemail-1.6.6-complete.tar.gz
tar -xvf roundcubemail-1.6.6-complete.tar.gz
sudo mv roundcubemail-1.6.6 /var/www/html/roundcubemail
sudo chown -R www-data:www-data /var/www/html/roundcubemail/
sudo chmod 755 -R /var/www/html/roundcubemail/

```

**12.** Next, you need to create a new database and user for **roundcube** and grant all permission to a new user to write to the database.
```
$ sudo mysql -u root
CREATE DATABASE roundcube DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER roundcubeuser@localhost IDENTIFIED BY '**password**';
GRANT ALL PRIVILEGES ON roundcube.* TO roundcubeuser@localhost;
flush privileges;
quit;

```

**13.** Next, import the initial tables to the Roundcube database.
```
sudo mysql roundcube < /var/www/html/roundcubemail/SQL/mysql.initial.sql

```
