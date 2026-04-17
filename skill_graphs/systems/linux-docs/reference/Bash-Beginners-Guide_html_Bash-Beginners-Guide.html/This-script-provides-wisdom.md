# This script provides wisdom

FORTUNE=/usr/games/fortune

while true; do
echo "On which topic do you want advice?"
cat << topics
politics
startrek
kernelnewbies
sports
bofh-excuses
magic
love
literature
drugs
education
topics

echo
echo -n "Make your choice: "
read topic
echo
echo "Free advice on the topic of $topic: "
echo
$FORTUNE $topic
echo

done

```

---
A _here_ document is used to present the user with possible choices. And again, the **true** test repeats the commands from the **CONSEQUENT-COMMANDS** list over and over again.
* * *
###  9.2.2.4. Calculating an average
This script calculates the average of user input, which is tested before it is processed: if input is not within range, a message is printed. If **q** is pressed, the loop exits:
```

#!/bin/bash

# This script provides wisdom
