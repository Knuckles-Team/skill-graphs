# fool-proof usage:
find "$PWD" -type f -a -mtime +5 | while read -d $'\000' file

do
gzip "$file"; mv "$file".gz "$DESTDIR"
echo "$file archived"
done

```

---
Files are compressed before they are moved into the archive directory.
* * *
#  9.5. Break and continue
##  9.5.1. The break built-in
The **break** statement is used to exit the current loop before its normal ending. This is done when you don't know in advance how many times the loop will have to execute, for instance because it is dependent on user input.
The example below demonstrates a **while** loop that can be interrupted. This is a slightly improved version of the `wisdom.sh` script from [Section 9.2.2.3](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_02_02_03).
```

#!/bin/bash
