# This script opens 4 terminal windows.

i="0"

while [ $i -lt 4 ]
do
xterm &
i=$[$i+1]
done

```

---
* * *
###  9.2.2.2. Nested while loops
The example below was written to copy pictures that are made with a webcam to a web directory. Every five minutes a picture is taken. Every hour, a new directory is created, holding the images for that hour. Every day, a new directory is created containing 24 subdirectories. The script runs in the background.
```

#!/bin/bash
