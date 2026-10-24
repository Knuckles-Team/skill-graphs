# This generates a file every 5 minutes

while true; do
touch pic-`date +%s`.jpg
sleep 300
done

```

---
Note the use of the **date** command to generate all kinds of file and directory names. See the man page for more.
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **Use the system**
---|---
| The previous example is for the sake of demonstration. Regular checks can easily be achieved using the system's _cron_ facility. Do not forget to redirect output and errors when using scripts that are executed from your crontab!
* * *
###  9.2.2.3. Using keyboard input to control the while loop
This script can be interrupted by the user when a **Ctrl** +**C** sequence is entered:
```

#!/bin/bash
