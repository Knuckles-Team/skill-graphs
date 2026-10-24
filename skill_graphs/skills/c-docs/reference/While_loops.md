[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/While_loops)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/While_loops)
[None](https://www.learn-c.org/cn/)
[Deutsch](https://www.learn-c.org/de/)
[English](https://www.learn-c.org/en/)
[Español](https://www.learn-c.org/es/)
[None](https://www.learn-c.org/fa/)
[Français](https://www.learn-c.org/fr/)
[Nederlands](https://www.learn-c.org/nl/)
[Polski](https://www.learn-c.org/pl/)



  * [C](https://www.learn-c.org)


  * [Welcome](https://www.learn-c.org/en/Welcome) /
  * While loops


# While loops
* * *
While loops are similar to for loops, but have less functionality. A while loop continues executing the while block as long as the condition in the while remains true. For example, the following code will execute exactly ten times:
```
int n = 0;
while (n < 10) {
    n++;
}

```

While loops can also execute infinitely if a condition is given which always evaluates as true (non-zero):
```
while (1) {
   /* do something */
}

```

### Loop directives
There are two important loop directives that are used in conjunction with all loop types in C - the `break` and `continue` directives.
The `break` directive halts a loop after ten loops, even though the while loop never finishes:
```
int n = 0;
while (1) {
    n++;
    if (n == 10) {
        break;
    }
}

```

In the following code, the `continue` directive causes the `printf` command to be skipped, so that only even numbers are printed out:
```
int n = 0;
while (n < 10) {
    n++;

    /* check that n is odd */
    if (n % 2 == 1) {
        /* go back to the start of the while block */
        continue;
    }

    /* we reach this code only if n is even */
    printf("The number %d is even.\n", n);
}

```

## Exercise
The `array` variable consists of a sequence of ten numbers. Inside the while loop, you must write two `if` conditions, which change the flow of the loop in the following manner (without changing the `printf` command):
  * If the current number which is about to printed is less than 5, don't print it.
  * If the current number which is about to printed is greater than 10, don't print it and stop the loop.


Notice that if you do not advance the iterator variable `i` and use the `continue` derivative, you will get stuck in an infinite loop.
* * *
[ ](https://www.learn-c.org/en/For_loops) [ Next Tutorial ](https://www.learn-c.org/en/Functions)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/While_loops)
#### Chapters
* * *
[Hello, World!](https://www.learn-c.org/en/Hello%2C_World%21)
[Variables and Types](https://www.learn-c.org/en/Variables_and_Types)
[Arrays](https://www.learn-c.org/en/Arrays)
[Multidimensional Arrays](https://www.learn-c.org/en/Multidimensional_Arrays)
[Conditions](https://www.learn-c.org/en/Conditions)
[Strings](https://www.learn-c.org/en/Strings)
[For loops](https://www.learn-c.org/en/For_loops)
[While loops](https://www.learn-c.org/en/While_loops)
[Functions](https://www.learn-c.org/en/Functions)
[Static](https://www.learn-c.org/en/Static)
[Pointers](https://www.learn-c.org/en/Pointers)
[Structures](https://www.learn-c.org/en/Structures)
[Function arguments by reference](https://www.learn-c.org/en/Function_arguments_by_reference)
[Dynamic allocation](https://www.learn-c.org/en/Dynamic_allocation)
[Arrays and Pointers](https://www.learn-c.org/en/Arrays_and_Pointers)
[Recursion](https://www.learn-c.org/en/Recursion)
[Linked lists](https://www.learn-c.org/en/Linked_lists)
[Binary trees](https://www.learn-c.org/en/Binary_trees)
[Unions](https://www.learn-c.org/en/Unions)
[Pointer Arithmetic](https://www.learn-c.org/en/Pointer_Arithmetics)
[Function Pointers](https://www.learn-c.org/en/Function_Pointers)
[Bitmasks](https://www.learn-c.org/en/Bitmasks)
[Contributing Tutorials](https://www.learn-c.org/en/Contributing_Tutorials)
Copyright © learn-c.org. Read our [Terms of Use](https://www.learn-c.org/tos) and [Privacy Policy](https://www.learn-c.org/privacy)
##### Code
Solution
#include <stdio.h> int main() { int array[] = {1, 7, 4, 5, 9, 3, 5, 11, 6, 3, 4}; int i = 0; while (i < 10) { /* your code goes here */ printf("%d\n", array[i]); i++; } return 0; }
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=2273313681056589&rc=)
