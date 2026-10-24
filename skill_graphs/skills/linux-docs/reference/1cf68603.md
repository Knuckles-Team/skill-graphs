## Step 4: Testing Postfix Mail Server on Ubuntu
**7.** Now try to check your mail server is connecting on port 25 using the following command.
```
$ telnet gmail-smtp-in.l.google.com 25

Trying 74.125.200.27...
Connected to gmail-smtp-in.l.google.com.
Escape character is '^]'.
220 mx.google.com ESMTP k12si849250plk.430 - gsmtp

```

The above message indicates that the connection is successfully established. Type **quit** to close the connection.
**8.** You can also use a **mail** program to send and read emails using the following command.
```
$ mail username@gmail.com

**Cc**:
**Subject**: Testing My Postfix Mail Server
I'm sending this email using the postfix mail server from Ubuntu machine

```
