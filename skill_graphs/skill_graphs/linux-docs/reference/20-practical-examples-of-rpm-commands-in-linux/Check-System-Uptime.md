# Check System Uptime
 tecuptime=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)
 echo -e '\E[32m'"System Uptime Days/(HH:MM) :" $tecreset $tecuptime
