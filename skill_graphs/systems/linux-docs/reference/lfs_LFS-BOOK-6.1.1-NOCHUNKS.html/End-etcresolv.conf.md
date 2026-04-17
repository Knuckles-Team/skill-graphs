# End /etc/resolv.conf`
EOF`
```

Replace _`[IP address of the nameserver]`_ with the IP address of the DNS most appropriate for the setup. There will often be more than one entry (requirements demand secondary servers for fallback capability). If you only need or want one DNS server, remove the second _nameserver_ line from the file. The IP address may also be a router on the local network.
##  Chapter 8. Making the LFS System Bootable
##  8.1. Introduction
It is time to make the LFS system bootable. This chapter discusses creating an `fstab` file, building a kernel for the new LFS system, and installing the GRUB boot loader so that the LFS system can be selected for booting at startup.
##  8.2. Creating the /etc/fstab File
The `/etc/fstab` file is used by some programs to determine where file systems are to be mounted by default, in which order, and which must be checked (for integrity errors) prior to mounting. Create a new file systems table like this:
```
`cat > /etc/fstab << "EOF"
`# Begin /etc/fstab
