# Dbhost = localhost
Dbhost = 127.0.0.1
tcp 0 0 0.0.0.0:10050 0.0.0.0:* OUÇA 1162/zabbix_agentd
tcp 0 0 0.0.0.0:10050 0.0.0.0:* OUÇA 1162/zabbix_agentd
tcp 0 0 0.0.0.0:10051 0.0.0.0:* OUÇA 1317/zabbix_server
root@debian:~# telnet localhost 10051
Trying ::1…
Connected to localhost.
Escape character is ‘^]’.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-633901)
       * ![](https://secure.gravatar.com/avatar/a46c8d9ae38d9bc5e37b6ead5e938896fdf50772a5cf3f56a395666b313c695e?s=50&d=blank&r=g)
suresh
[ September 3, 2015 at 12:00 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-657154)
@Fábio
I did same changes but still same error Zabbix server is running No localhost:10051
telnet localhost 10051
Trying ::1…
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1…
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-657154)
         * ![](https://secure.gravatar.com/avatar/db6ae12effea4d8224a71ecb503df65accabbc510073c10e26cff60889a58c66?s=50&d=blank&r=g)
Tangles
[ October 22, 2015 at 7:50 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-691655)
