[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Functions)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Functions)
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
  * Functions


# Functions
* * *
C functions are simple, but because of how C works, the power of functions is a bit limited.
  * Functions receive either a fixed or variable amount of arguments.
  * Functions can only return one value, or return no value.


In C, arguments are copied by value to functions, which means that we cannot change the arguments to affect their value outside of the function. To do that, we must use pointers, which are taught later on.
Functions are defined using the following syntax:
```
int foo(int bar) {
    /* do something */
    return bar * 2;
}

int main() {
    foo(1);
}

```

The function `foo` we defined receives one argument, which is `bar`. The function receives an integer, multiplies it by two, and returns the result.
To execute the function `foo` with 1 as the argument `bar`, we use the following syntax:
```
foo(1);

```

In C, functions must be first defined before they are used in the code. They can be either declared first and then implemented later on using a header file or in the beginning of the C file, or they can be implemented in the order they are used (less preferable).
The correct way to use functions is as follows:
```
/* function declaration */
int foo(int bar);

int main() {
    /* calling foo from main */
    printf("The value of foo is %d", foo(1));
}

int foo(int bar) {
    return bar + 1;
}

```

We can also create functions that do not return a value by using the keyword `void`:
```
void moo() {
    /* do something and don't return a value */
}

int main() {
    moo();
}

```

## Exercise
Write a function called `print_big` which receives one argument (an integer) and prints the line `x is big` (where x is the argument) if the argument given to the function is a number bigger than 10.
  * **Important** : Don't forget to add a newline character `\n` at the end of the printf string.


* * *
[ ](https://www.learn-c.org/en/While_loops) [ Next Tutorial ](https://www.learn-c.org/en/Static)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Functions)
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
#include <stdio.h> /* function declaration */ void print_big(int number); int main() { int array[] = { 1, 11, 2, 22, 3, 33 }; int i; for (i = 0; i < 6; i++) { print_big(array[i]); } return 0; } /* write your function here */
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=4768596507666527&rc=)
