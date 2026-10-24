# clear the screen
 clear

unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

while getopts iv name
 do
 case $name in
 i)iopt=1;;
 v)vopt=1;;
 *)echo "Invalid arg";;
 esac
 done

if [[ ! -z $iopt ]]
 then
 {
 wd=$(pwd)
 basename "$(test -L "$0" && readlink "$0" || echo "$0")" > /tmp/scriptname
 scriptname=$(echo -e -n $wd/ && cat /tmp/scriptname)
 su -c "cp $scriptname /usr/bin/monitor" root && echo "Congratulations! Script Installed, now run monitor Command" || echo "Installation failed"
 }
 fi

if [[ ! -z $vopt ]]
 then
 {
 echo -e "tecmint_monitor version 0.1\nDesigned by Tecmint.com\nReleased Under Apache 2.0 License"
 }
 fi

if [[ $# -eq 0 ]]
 then
 {
