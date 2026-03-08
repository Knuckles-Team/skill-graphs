# Check DNS
 nameservers=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')
 echo -e '\E[32m'"Name Servers :" $tecreset $nameservers
