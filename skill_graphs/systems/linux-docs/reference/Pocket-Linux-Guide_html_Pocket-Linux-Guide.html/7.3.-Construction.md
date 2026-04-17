#  7.3. Construction
##  7.3.1. Verify presence of getty and login
```
`bash#` ls ~/staging/sbin/getty
`bash#` ls ~/staging/bin/login
```

---
* * *
##  7.3.2. Modify inittab for multi-user mode
Modify `~/staging/etc/inittab` by changing the default runlevel and adding **getty** entries as shown below.
```
# /etc/inittab - init daemon configuration file
#
# Default runlevel
id:2:initdefault:
#
# System initialization
si:S:sysinit:/etc/init.d/rc S
#
# Runlevel scripts
r0:0:wait:/etc/init.d/rc 0
r1:1:respawn:/bin/sh
r2:2:wait:/etc/init.d/rc 2
r3:3:wait:/etc/init.d/rc 3
r4:4:wait:/etc/init.d/rc 4
r5:5:wait:/etc/init.d/rc 5
r6:6:wait:/etc/init.d/rc 6
#
# Spawn virtual terminals
1:235:respawn:/sbin/getty 38400 tty1 linux
2:235:respawn:/sbin/getty 38400 tty2 linux
3:235:respawn:/sbin/getty 38400 tty3 linux
4:235:respawn:/sbin/getty 38400 tty4 linux
5:235:respawn:/sbin/getty 38400 tty5 linux
6:2345:respawn:/sbin/getty 38400 tty6 linux
#
# end of /etc/inittab
```

---
* * *
##  7.3.3. Create tty devices
```
`bash#` cd ~/staging/dev
`bash#` mknod ~/staging/dev/tty0 c 4 0
`bash#` mknod ~/staging/dev/tty1 c 4 1
`bash#` mknod ~/staging/dev/tty2 c 4 2
`bash#` mknod ~/staging/dev/tty3 c 4 3
`bash#` mknod ~/staging/dev/tty4 c 4 4
`bash#` mknod ~/staging/dev/tty5 c 4 5
`bash#` mknod ~/staging/dev/tty6 c 4 6
`bash#` mknod ~/staging/dev/tty c 5 0
```

---
* * *
##  7.3.4. Create support files in /etc
###  7.3.4.1. /etc/issue
Create the file `~/staging/etc/issue` using the example below or design a customized message.
```
Connected to \l at \b bps.
```

---
Be sure that "\l" is a lowercase letter L and not the number one.
* * *
###  7.3.4.2. /etc/passwd
Use a text editor to create a minimal passwd file conforming to the Linux Standards Base (LSB) document. Save the file as `~/staging/etc/passwd`
```
root::0:0:Super User:/root:/bin/sh
bin:x:1:1:Legacy UID:/bin:/bin/false
daemon:x:2:2:Legacy UID:/sbin:/bin/false
```

---
* * *
###  7.3.4.3. /etc/group
Use a text editor to create an LSB conforming group file and save it as `~/staging/etc/group`
```
root::0:root
bin:x:1:root,bin,daemon
daemon:x:2:root,bin,daemon
```

---
* * *
###  7.3.4.4. /etc/nsswitch.conf
Create the following file and save it as `~/staging/etc/nsswitch.conf`
```
passwd: files
group:  files
```

---
* * *
##  7.3.5. Copy required libraries
```
`bash#` cp /lib/libnss_files.so.2 ~/staging/lib
bash# strip --strip-unneeded ~/staging/lib/*
```

---
* * *
##  7.3.6. Set directory and file permissions
Set minimal privileges on all files and directories under `~/staging`. Everything is owned by the root user and the root group. Permissions are read-write for the owner and read-only for the group. Exceptions to the blanket permissions are handled case by case.
```
`bash#` cd ~/staging
`bash#` chown -R 0:0 ~/staging/*
`bash#` chmod -R 640 ~/staging/*
```

---
Set execute permission on all directories. (Note the capital "X")
```
`bash#` chmod -R +X ~/staging/*
```

---
Files in `/bin` are read and execute for all, but `su` is an exception.
```
`bash#` chmod 755 ~/staging/bin/*
`bash#` chmod 4750 ~/staging/bin/su
```

---
Files in `/dev` have various permissions. Disk devices should be accessible to administrators only. Other files like `/dev/null` should have full privileges granted to everyone.
```
`bash#` chmod 660 ~/staging/dev/fd0 dev/ram0
`bash#` chmod 666 ~/staging/dev/null
`bash#` chmod 622 ~/staging/dev/console
`bash#` chmod 600 ~/staging/dev/initctl
`bash#` chmod 622 ~/staging/dev/tty
`bash#` chmod 622 ~/staging/dev/tty?
```

---
The `passwd` and `group` files must be world readable.
```
`bash#` chmod 644 ~/staging/etc/passwd
`bash#` chmod 644 ~/staging/etc/group
```

---
The scripts in `/etc/init.d` are read and execute for administrators.
```
`bash#` chmod 750 ~/staging/etc/init.d/*
```

---
Libraries need read and execute permissions for everyone.
```
`bash#` chmod 755 ~/staging/lib/*
```

---
Only root should have access to the `/root` directory.
```
`bash#` chmod 700 ~/staging/root
```

---
Make files in `/sbin` read and execute for administrators.
```
`bash#` chmod 750 ~/staging/sbin/*
```

---
Temp should be read-write for all with the sticky bit set.
```
`bash#` chmod 1777 ~/staging/tmp
```

---
* * *
##  7.3.7. Create the root disk image
```
`bash#` cd /
`bash#` dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
`bash#` mke2fs -m0 /dev/ram7 4096
`bash#` mount /dev/ram7 /mnt
`bash#` cp -dpR ~/staging/* /mnt
`bash#` umount /dev/ram7
`bash#` dd if=/dev/ram7 of=~/phase6-image bs=1k count=4096
`bash#` gzip -9 ~/phase6-image
```

---
* * *
##  7.3.8. Copy the image to diskette
Insert the diskette labeled "root disk" into drive fd0.
```
`bash#` dd if=~/phase6-image.gz of=/dev/fd0 bs=1k
```

---
* * *
