# Drift file.

driftfile /etc/ntp/drift`

```

---
The most basic ntp.conf file will simply list 2 servers, one that it wishes to synchronize with, and a pseudo IP address for itself (in this case 127.127.1.0). The pseudo IP is used in case of network problems or if the remote NTP server goes down. NTP will synchronize against itself until the it can start synchronizing with the remote server again. It is recommended that you list at least 2 remote servers that you can synchronize against. One will act as a primary server and the other as a backup.
You should also list a location for a drift file. Over time NTP will "learn" the system clock's error rate and automatically adjust for it.
The restrict option can be used to provide better control and security over what NTP can do, and who can effect it. For example:
```
`# Prohibit general access to this service.
restrict default ignore
