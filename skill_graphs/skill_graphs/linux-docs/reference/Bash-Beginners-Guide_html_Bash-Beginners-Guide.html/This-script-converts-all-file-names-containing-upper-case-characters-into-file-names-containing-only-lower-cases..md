# This script converts all file names containing upper case characters into file# names containing only lower cases.

LIST="$(ls)"

for name in "$LIST"; do

if [[ "$name" != *[[:upper:]]* ]]; then
continue
fi

ORIG="$name"
NEW=`echo $name | tr 'A-Z' 'a-z'`

mv "$ORIG" "$NEW"
echo "new name for $ORIG is $NEW"
done

```

---
This script has at least one disadvantage: it overwrites existing files. The `noclobber` option to Bash is only useful when redirection occurs. The `-b` option to the **mv** command provides more security, but is only safe in case of one accidental overwrite, as is demonstrated in this test:
```

`[carol@octarine ~/test]` **rm `*`**

`[carol@octarine ~/test]` **touch `test Test TEST`**

`[carol@octarine ~/test]` **bash `-x` `tolower.sh`**
++ ls
+ LIST=test
Test
TEST
+ [[ test != *[[:upper:]]* ]]
+ continue
+ [[ Test != *[[:upper:]]* ]]
+ ORIG=Test
++ echo Test
++ tr A-Z a-z
+ NEW=test
+ mv -b Test test
+ echo 'new name for Test is test'
new name for Test is test
+ [[ TEST != *[[:upper:]]* ]]
+ ORIG=TEST
++ echo TEST
++ tr A-Z a-z
+ NEW=test
+ mv -b TEST test
+ echo 'new name for TEST is test'
new name for TEST is test

`[carol@octarine ~/test]` **ls `-a`**
./  ../  test  test~

```

---
The **tr** is part of the _textutils_ package; it can perform all kinds of character transformations.
* * *
#  9.6. Making menus with the select built-in
##  9.6.1. General
###  9.6.1.1. Use of select
The **select** construct allows easy menu generation. The syntax is quite similar to that of the **for** loop:
**select` WORD` [in `LIST`]; do RESPECTIVE-COMMANDS; done**
`LIST` is expanded, generating a list of items. The expansion is printed to standard error; each item is preceded by a number. If **in` LIST`** is not present, the positional parameters are printed, as if **in` $@`** would have been specified. `LIST` is only printed once.
Upon printing all the items, the `PS3` prompt is printed and one line from standard input is read. If this line consists of a number corresponding to one of the items, the value of `WORD` is set to the name of that item. If the line is empty, the items and the `PS3` prompt are displayed again. If an _EOF_ (End Of File) character is read, the loop exits. Since most users don't have a clue which key combination is used for the EOF sequence, it is more user-friendly to have a **break** command as one of the items. Any other value of the read line will set `WORD` to be a null string.
The read line is saved in the `REPLY` variable.
The **RESPECTIVE-COMMANDS** are executed after each selection until the number representing the **break** is read. This exits the loop.
* * *
###  9.6.1.2. Examples
This is a very simple example, but as you can see, it is not very user-friendly:
```

`[carol@octarine testdir]` **cat `private.sh`**
#!/bin/bash

echo "This script can make any of the files in this directory private."
echo "Enter the number of the file you want to protect:"

select FILENAME in *;
do
     echo "You picked $FILENAME ($REPLY), it is now only accessible to you."
     chmod go-rwx "$FILENAME"
done

`[carol@octarine testdir]` **./private.sh**
This script can make any of the files in this directory private.
Enter the number of the file you want to protect:
1) archive-20030129
2) bash
3) private.sh
#? 1
You picked archive-20030129 (1)
#?

```

---
Setting the `PS3` prompt and adding a possibility to quit makes it better:
```

#!/bin/bash

echo "This script can make any of the files in this directory private."
echo "Enter the number of the file you want to protect:"

PS3="Your choice: "
QUIT="QUIT THIS PROGRAM - I feel safe now."
touch "$QUIT"

select FILENAME in *;
do
  case $FILENAME in
        "$QUIT")
          echo "Exiting."
          break
          ;;
        *)
          echo "You picked $FILENAME ($REPLY)"
          chmod go-rwx "$FILENAME"
          ;;
  esac
done
rm "$QUIT"

```

---
* * *
##  9.6.2. Submenus
Any statement within a **select** construct can be another **select** loop, enabling (a) submenu(s) within a menu.
By default, the `PS3` variable is not changed when entering a nested **select** loop. If you want a different prompt in the submenu, be sure to set it at the appropriate time(s).
* * *
#  9.7. The shift built-in
##  9.7.1. What does it do?
The **shift** command is one of the Bourne shell built-ins that comes with Bash. This command takes one argument, a number. The positional parameters are shifted to the left by this number, _N_. The positional parameters from `N+1` to `$#` are renamed to variable names from `$1` to `$# - N+1`.
Say you have a command that takes 10 arguments, and N is 4, then `$4` becomes `$1`, `$5` becomes `$2` and so on. `$10` becomes `$7` and the original `$1`, `$2` and `$3` are thrown away.
If N is zero or greater than `$#`, the positional parameters are not changed (the total number of arguments, see [Section 7.2.1.2](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#sect_07_02_01_02)) and the command has no effect. If N is not present, it is assumed to be 1. The return status is zero unless N is greater than `$#` or less than zero; otherwise it is non-zero.
* * *
##  9.7.2. Examples
A shift statement is typically used when the number of arguments to a command is not known in advance, for instance when users can give as many arguments as they like. In such cases, the arguments are usually processed in a **while** loop with a test condition of **(( $# ))**. This condition is true as long as the number of arguments is greater than zero. The `$1` variable and the **shift** statement process each argument. The number of arguments is reduced each time **shift** is executed and eventually becomes zero, upon which the **while** loop exits.
The example below, `cleanup.sh`, uses **shift** statements to process each file in the list generated by **find** :
```

#!/bin/bash
