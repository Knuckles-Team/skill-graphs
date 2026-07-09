# Check Load Average
 loadaverage=$(top -n 1 -b | grep "load average:" | awk '{print $10 $11 $12}')
 echo -e '\E[32m'"Load Average :" $tecreset $loadaverage
