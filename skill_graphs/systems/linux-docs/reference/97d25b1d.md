# End /etc/hosts (network card version)`
EOF`
```

The _`[192.168.1.1]`_ and _`[ <HOSTNAME>.example.org]`_ values need to be changed for specific users or requirements (if assigned an IP address by a network/system administrator and the machine will be connected to an existing network).
If a network card is not going to be configured, create the `/etc/hosts` file by running:
```
`cat > /etc/hosts << "EOF"
`# Begin /etc/hosts (no network card version)

127.0.0.1 _`[<HOSTNAME>.example.org]`_ _`[HOSTNAME]`_ localhost
