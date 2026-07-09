## Step 3: Secure MariaDB Database
To configure **MySQL** for **Cacti** , we must first secure the newly installed **MySQL** server and then create the **Cacti** database with the user “**Cacti** “. If your MySQL is already installed and secured, you don’t need to do this again.
```
sudo mysql_secure_installation

```

Follow the prompts to set up a root password, remove anonymous users, disallow remote root login, and remove the test database.
![Secure MySQL Installation](https://www.tecmint.com/wp-content/uploads/2015/03/Secure-MySQL-Installation.png)Secure MySQL Installation
