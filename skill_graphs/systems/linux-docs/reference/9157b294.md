# End /etc/profile`
EOF`
```

###  Note
The “C” (default) and “en_US” (the recommended one for United States English users) locales are different.
Setting the keyboard layout, screen font, and locale-related environment variables are the only internationalization steps needed to support locales that use ordinary single-byte encodings and left-to-right writing direction. More complex cases (including UTF-8 based locales) require additional steps and additional patches because many applications tend to not work properly under such conditions. These steps and patches are not included in the LFS book and such locales are not yet supported by LFS.
##  7.10. Configuring the localnet Script
Part of the job of the **localnet** script is setting the system's hostname. This needs to be configured in the `/etc/sysconfig/network` file.
Create the `/etc/sysconfig/network` file and enter a hostname by running:
```
`echo "HOSTNAME=_`[lfs]`_" > /etc/sysconfig/network`
```

_`[lfs]`_ needs to be replaced with the name given to the computer. Do not enter the Fully Qualified Domain Name (FQDN) here. That information will be put in the `/etc/hosts` file in the next section.
##  7.11. Creating the /etc/hosts File
If a network card is to be configured, decide on the IP address, FQDN, and possible aliases for use in the `/etc/hosts` file. The syntax is:
```
            <IP address> myhost.example.org aliases
```

Unless the computer is to be visible to the Internet (i.e., there is a registered domain and a valid block of assigned IP addresses—most users do not have this), make sure that the IP address is in the private network IP address range. Valid ranges are:
```
    Class Networks
        A     10.0.0.0
        B     172.16.0.0 through 172.31.0.255
        C     192.168.0.0 through 192.168.255.255
```

A valid IP address could be 192.168.1.1. A valid FQDN for this IP could be www.linuxfromscratch.org (not recommended because this is a valid registered domain address and could cause domain name server issues).
Even if not using a network card, an FQDN is still required. This is necessary for certain programs to operate correctly.
Create the `/etc/hosts` file by running:
```
`cat > /etc/hosts << "EOF"
`# Begin /etc/hosts (network card version)

127.0.0.1 localhost
_`[192.168.1.1]`_ _`[<HOSTNAME>.example.org]`_ _`[HOSTNAME]`_
