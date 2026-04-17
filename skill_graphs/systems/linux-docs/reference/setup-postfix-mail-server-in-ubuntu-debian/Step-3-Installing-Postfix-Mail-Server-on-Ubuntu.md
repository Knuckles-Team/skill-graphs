## Step 3: Installing Postfix Mail Server on Ubuntu
**4.** Postfix is a mail transfer agent (**MTA**) which is the responsible software for delivering & receiving emails, it’s essential in order to create a complete mail server.
To install it on Ubuntu/Debian or even Mint, run:
```
sudo apt install postfix

```
![Install Postfix Mail Server](https://www.tecmint.com/wp-content/uploads/2020/09/Install-Postfix-Mail-Server.png)Install Postfix Mail Server
During installation, you will be asked to choose the type of mail configuration, and choose “**Internet Site** ”.
![Install Postfix in Ubuntu](https://www.tecmint.com/wp-content/uploads/2014/12/Install-Postfix-in-Ubuntu.png)Install Postfix in Ubuntu
**5.** Now enter the fully qualified domain name that you want to use for sending and receiving emails.
![Set Postfix Mail Domain](https://www.tecmint.com/wp-content/uploads/2014/12/Set-Postfix-Mail-Domain.png)Set Postfix Mail Domain
**6.** Once Postfix is installed, it will automatically start and create a new **/etc/postfix/main.cf** file. You can verify the Postfix status of the service using the following commands.
```
sudo systemctl status postfix

```
![Check Postfix Status](https://www.tecmint.com/wp-content/uploads/2020/09/Check-Postfix-Mail-Server.png)Check Postfix Status
