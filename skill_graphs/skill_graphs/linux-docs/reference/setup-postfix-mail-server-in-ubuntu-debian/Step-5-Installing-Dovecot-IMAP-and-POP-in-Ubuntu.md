## Step 5: Installing Dovecot IMAP and POP in Ubuntu
**9.** **Dovecot** is a mail delivery agent (**MDA**), it delivers the emails from/to the mail server, to install it, run the following command.
```
sudo apt install dovecot-imapd dovecot-pop3d

```
![Install Dovecot in Ubuntu](https://www.tecmint.com/wp-content/uploads/2020/09/Install-Dovecot-Server.png)Install Dovecot in Ubuntu
**10.** Next, restart the Dovecot service and verify the status using the following commands.
```
sudo systemctl restart dovecot
sudo systemctl status dovecot

```
![Check Dovecot Status](https://www.tecmint.com/wp-content/uploads/2020/09/Check-Dovecot-Server.png)Check Dovecot Status
