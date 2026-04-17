# A new directory is created every hour.

PICSDIR=/home/carol/pics
WEBDIR=/var/www/carol/webcam

while true; do
	DATE=`date +%Y%m%d`
	HOUR=`date +%H`
	mkdir $WEBDIR/"$DATE"

	while [ $HOUR -ne "00" ]; do
		DESTDIR=$WEBDIR/"$DATE"/"$HOUR"
		mkdir "$DESTDIR"
		mv $PICDIR/*.jpg "$DESTDIR"/
		sleep 3600
		HOUR=`date +%H`
	done
done

```

---
Note the use of the **true** statement. This means: continue execution until we are forcibly interrupted (with **kill** or **Ctrl** +**C**).
This small script can be used for simulation testing; it generates files:
```

#!/bin/bash

# A new directory is created every hour.
