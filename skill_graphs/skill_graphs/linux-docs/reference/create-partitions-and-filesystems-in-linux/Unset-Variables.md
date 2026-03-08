# Unset Variables
 unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage
 `
`# Remove Temporary Files
 rm /tmp/osrelease /tmp/who /tmp/ramcache /tmp/diskusage
 }
 fi
 shift $(($OPTIND -1))
 `
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-873968)
  27. ![](https://secure.gravatar.com/avatar/f1a1b68f4dcf1782b15ff4ec9a309989cdad77816dd35c75428c2dcd7e2ee78a?s=50&d=blank&r=g)
interminable
[ February 20, 2017 at 12:48 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-869497)
elif [ -f /etc/gentoo-release ] ; then
DIST=’Gentoo’
PSUEDONAME=`cat /etc/gentoo-release | sed s/.*\\(// | sed s/\\)//`
REV=`cat /etc/gentoo-release | sed s/.*release\ // | sed s/\ .*//`
