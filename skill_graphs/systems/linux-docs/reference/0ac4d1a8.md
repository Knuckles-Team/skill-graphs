# You can now exit in a decent way.

FORTUNE=/usr/games/fortune

while true; do
echo "On which topic do you want advice?"
echo "1.  politics"
echo "2.  startrek"
echo "3.  kernelnewbies"
echo "4.  sports"
echo "5.  bofh-excuses"
echo "6.  magic"
echo "7.  love"
echo "8.  literature"
echo "9.  drugs"
echo "10. education"
echo

echo -n "Enter your choice, or 0 for exit: "
read choice
echo

case $choice in
     1)
     $FORTUNE politics
     ;;
     2)
     $FORTUNE startrek
     ;;
     3)
     $FORTUNE kernelnewbies
     ;;
     4)
     echo "Sports are a waste of time, energy and money."
     echo "Go back to your keyboard."
     echo -e "\t\t\t\t -- \"Unhealthy is my middle name\" Soggie."
     ;;
     5)
     $FORTUNE bofh-excuses
     ;;
     6)
     $FORTUNE magic
     ;;
     7)
     $FORTUNE love
     ;;
     8)
     $FORTUNE literature
     ;;
     9)
     $FORTUNE drugs
     ;;
     10)
     $FORTUNE education
     ;;
     0)
     echo "OK, see you!"
     break
     ;;
     *)
     echo "That is not a valid choice, try a number from 0 to 10."
     ;;
esac
done

```

---
Mind that **break** exits the loop, not the script. This can be demonstrated by adding an **echo** command at the end of the script. This **echo** will also be executed upon input that causes **break** to be executed (when the user types "0").
In nested loops, **break** allows for specification of which loop to exit. See the Bash **info** pages for more.
* * *
##  9.5.2. The continue built-in
The **continue** statement resumes iteration of an enclosing **for** , **while** , **until** or **select** loop.
When used in a **for** loop, the controlling variable takes on the value of the next element in the list. When used in a **while** or **until** construct, on the other hand, execution resumes with **TEST-COMMAND** at the top of the loop.
* * *
##  9.5.3. Examples
In the following example, file names are converted to lower case. If no conversion needs to be done, a **continue** statement restarts execution of the loop. These commands don't eat much system resources, and most likely, similar problems can be solved using **sed** and **awk**. However, it is useful to know about this kind of construction when executing heavy jobs, that might not even be necessary when tests are inserted at the correct locations in a script, sparing system resources.
```

`[carol@octarine ~/test]` **cat `tolower.sh`**
#!/bin/bash
