## Step 1: Set a Hostname and DNS Records for Domain
**1.** First, set a valid **FQDN** (**Fully Qualified Domain Name**) hostname for your Ubuntu server using the [hostnamectl command](https://www.tecmint.com/hostname-command-examples-for-linux/ "Set Hostname in Ubuntu") as shown.
```
sudo hostnamectl set-hostname **mail.tecmint.com**

```

**2.** Next, you need to add a `MX` and `A` records for your domain in your DNS control panel that guides other MTAs that your mail server `mail.yourdomain.com` domain is responsible for email delivery.
```
MX record    @           mail.tecmint.com
mail.tecmint.com        <IP-address>

```
