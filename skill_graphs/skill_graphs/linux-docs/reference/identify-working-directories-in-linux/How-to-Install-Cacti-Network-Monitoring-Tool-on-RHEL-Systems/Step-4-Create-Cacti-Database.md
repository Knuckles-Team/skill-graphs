## Step 4: Create Cacti Database
Log in to the MySQL server using the newly created password, and then create the Cacti database with the user “**Cacti** ” setting a password for it.
```
sudo mysql -u root -p
CREATE DATABASE cacti;
CREATE USER 'cacti'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON cacti.* TO 'cacti'@'localhost';
FLUSH PRIVILEGES;
EXIT;

```
![Create Cacti Database](https://www.tecmint.com/wp-content/uploads/2015/03/Create-Cacti-Database.png)Create Cacti Database
Next, you need to import the default **Cacti** database schema into the newly created database, but before that, you need to find out the database file path using the [rpm command](https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/ "RPM Commands in Linux") and import it as shown.
```
sudo rpm -ql cacti | grep cacti.sql
sudo mysql -u cactiuser -p cacti < /usr/share/doc/cacti/cacti.sql

```
![Import Cacti Database](https://www.tecmint.com/wp-content/uploads/2015/03/Import-Cacti-Database.png)Import Cacti Database
