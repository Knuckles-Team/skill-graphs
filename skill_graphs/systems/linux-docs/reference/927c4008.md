# End /etc/nsswitch.conf`
EOF`
```

To determine the local time zone, run the following script:
```
`tzselect`
```

After answering a few questions about the location, the script will output the name of the time zone (e.g., _EST5EDT_ or _Canada/Eastern_). Then create the `/etc/localtime` file by running:
```
`cp -v --remove-destination /usr/share/zoneinfo/_`[xxx]`_ \
    /etc/localtime`
```

Replace _`[xxx]`_ with the name of the time zone that **tzselect** provided (e.g., Canada/Eastern).
The meaning of the cp option:

_`--remove-destination`_

This is needed to force removal of the already existing symbolic link. The reason for copying the file instead of using a symlink is to cover the situation where `/usr` is on a separate partition. This could be important when booted into single user mode.
###  6.11.3. Configuring Dynamic Loader
By default, the dynamic loader (`/lib/ld-linux.so.2`) searches through `/lib` and `/usr/lib` for dynamic libraries that are needed by programs as they are run. However, if there are libraries in directories other than `/lib` and `/usr/lib`, these need to be added to the `/etc/ld.so.conf` file in order for the dynamic loader to find them. Two directories that are commonly known to contain additional libraries are `/usr/local/lib` and `/opt/lib`, so add those directories to the dynamic loader's search path.
Create a new file `/etc/ld.so.conf` by running the following:
```
`cat > /etc/ld.so.conf << "EOF"
`# Begin /etc/ld.so.conf

/usr/local/lib
/opt/lib
