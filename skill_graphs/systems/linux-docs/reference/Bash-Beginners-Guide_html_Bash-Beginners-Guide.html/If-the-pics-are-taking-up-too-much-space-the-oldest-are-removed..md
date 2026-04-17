# If the pics are taking up too much space, the oldest are removed.

while true; do
	DISKFUL=$(df -h $WEBDIR | grep -v File | awk '{print $5 }' | cut -d "%" -f1 -)

	until [ $DISKFUL -ge "90" ]; do

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

	DISKFULL=$(df -h $WEBDIR | grep -v File | awk '{ print $5 }' | cut -d "%" -f1 -)
	done

	TOREMOVE=$(find $WEBDIR -type d -a -mtime +30)
	for i in $TOREMOVE; do
		rm -rf "$i";
	done

done

```

---
Note the initialization of the `HOUR` and `DISKFULL` variables and the use of options with **ls** and **date** in order to obtain a correct listing for `TOREMOVE`.
* * *
#  9.4. I/O redirection and loops
##  9.4.1. Input redirection
Instead of controlling a loop by testing the result of a command or by user input, you can specify a file from which to read input that controls the loop. In such cases, **read** is often the controlling command. As long as input lines are fed into the loop, execution of the loop commands continues. As soon as all the input lines are read the loop exits.
Since the loop construct is considered to be one command structure (such as **while TEST-COMMAND; do CONSEQUENT-COMMANDS; done**), the redirection should occur after the **done** statement, so that it complies with the form
**command < `file`**
This kind of redirection also works with other kinds of loops.
* * *
##  9.4.2. Output redirection
In the example below, output of the **find** command is used as input for the **read** command controlling a **while** loop:
```

`[carol@octarine ~/testdir]` **cat `archiveoldstuff.sh`**
#!/bin/bash
