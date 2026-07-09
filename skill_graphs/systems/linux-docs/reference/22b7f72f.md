## Step 5: Configure Cacti Database Connection
To configure the Cacti database connection, you need to open the configuration file as shown.
```
sudo vi /etc/cacti/db.php

```

Update the following lines with your database information.
```
$database_type     = 'mysql';
$database_default  = 'cacti';
$database_hostname = 'localhost';
$database_username = 'cacti';
$database_password = 'your_password';

```
![Configure Cacti Database Settings](https://www.tecmint.com/wp-content/uploads/2015/03/Configure-Cacti-Database.png)Configure Cacti Database Settings
