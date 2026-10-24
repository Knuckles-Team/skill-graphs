# Else, do nothing.

if [ $WEEKOFFSET -eq "0" ]; then
  echo "Sunday evening, put out the garbage cans." | mail -s "Garbage cans out" your@your_domain.org
fi

```

---
* * *
###  7.1.2.3. String comparisons
An example of comparing strings for testing the user ID:
```

if [ "$(whoami)" != 'root' ]; then
        echo "You have no permission to run $0 as non-root user."
        exit 1;
fi

```

---
With Bash, you can shorten this type of construct. The compact equivalent of the above test is as follows:
```

[ "$(whoami)" != 'root' ] && ( echo you are using a non-privileged account; exit 1 )

```

---
Similar to the "&&" expression which indicates what to do if the test proves true, "||" specifies what to do if the test is false.
Regular expressions may also be used in comparisons:
```

`anny >` **`gender`=`_"female"_`**

`anny >` **if `_[[ "$gender" == f* ]]_`**
`More input>` **then echo `_"Pleasure to meet you, Madame."_`; fi**
Pleasure to meet you, Madame.

`anny >`

```

---
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **Real Programmers**
---|---
|  Most programmers will prefer to use the **test** built-in command, which is equivalent to using square brackets for comparison, like this: | ```

test "$(whoami)" != 'root' && (echo you are using a non-privileged account; exit 1)

```

---
![Note](https://tldp.org/LDP/Bash-Beginners-Guide/images/note.gif) | **No exit?**
---|---
| If you invoke the **exit** in a subshell, it will not pass variables to the parent. Use { and } instead of ( and ) if you do not want Bash to fork a subshell.
See the info pages for Bash for more information on pattern matching with the "(( EXPRESSION ))" and "[[ EXPRESSION ]]" constructs.
* * *
