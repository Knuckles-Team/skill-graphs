# Check OS Release Version and Name
 cat /etc/issue |head -n 1 > /tmp/osrelease
 osname=$(cat /tmp/osrelease |awk '{print $1}')
 osrelease=$(cat /tmp/osrelease |awk '{print $3}')
 #cat /etc/os-release | grep 'NAME\|VERSION' | grep -v 'VERSION_ID' | grep -v 'PRETTY_NAME' > /tmp/osrelease
 echo -n -e '\E[32m'"OS Name :" $tecreset  ; echo $osname \"
 echo -n -e '\E[32m'"OS Version :" $tecreset ; echo $osrelease \"
