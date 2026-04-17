# Calculate the average of a series of numbers.

SCORE="0"
AVERAGE="0"
SUM="0"
NUM="0"

while true; do

  echo -n "Enter your score [0-100%] ('q' for quit): "; read SCORE;

  if (("$SCORE" < "0"))  || (("$SCORE" > "100")); then
    echo "Be serious.  Common, try again: "
  elif [ "$SCORE" == "q" ]; then
    echo "Average rating: $AVERAGE%."
    break
  else
    SUM=$[$SUM + $SCORE]
    NUM=$[$NUM + 1]
    AVERAGE=$[$SUM / $NUM]
  fi

done

echo "Exiting."

```

---
Note how the variables in the last lines are left unquoted in order to do arithmetic.
* * *
#  9.3. The until loop
##  9.3.1. What is it?
The **until** loop is very similar to the **while** loop, except that the loop executes until the **TEST-COMMAND** executes successfully. As long as this command fails, the loop continues. The syntax is the same as for the **while** loop:
**until TEST-COMMAND; do CONSEQUENT-COMMANDS; done**
The return status is the exit status of the last command executed in the **CONSEQUENT-COMMANDS** list, or zero if none was executed. **TEST-COMMAND** can, again, be any command that can exit with a success or failure status, and **CONSEQUENT-COMMANDS** can be any UNIX command, script or shell construct.
As we already explained previously, the ";" may be replaced with one or more newlines wherever it appears.
* * *
##  9.3.2. Example
An improved `picturesort.sh` script (see [Section 9.2.2.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_09_02_02_02)), which tests for available disk space. If not enough disk space is available, remove pictures from the previous months:
```

#!/bin/bash
