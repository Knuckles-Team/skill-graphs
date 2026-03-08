[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Variables_and_Types)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Variables_and_Types)
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
  * Variables and Types


# Variables and Types
* * *
### Data types
C has several types of variables, but there are a few basic types:
  * Integers - whole numbers which can be either positive or negative. Defined using `char`, `int`, `short`, `long` or `long long`.
  * Unsigned integers - whole numbers which can only be positive. Defined using `unsigned char`, `unsigned int`, `unsigned short`, `unsigned long` or `unsigned long long`.
  * Floating point numbers - real numbers (numbers with fractions). Defined using `float` and `double`.
  * Structures - will be explained later, in the Structures section.


The different types of variables define their bounds. A `char` can range only from -128 to 127, whereas a `long` can range from -2,147,483,648 to 2,147,483,647 (`long` and other numeric data types may have another range on different computers, for example - from –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 on 64-bit computer).
Note that C does _not_ have a boolean type. Usually, it is defined using the following notation:
```
#define BOOL char
#define FALSE 0
#define TRUE 1

```

C uses arrays of characters to define strings, and will be explained in the Strings section.
### Defining variables
For numbers, we will usually use the type `int`. On most computers today, it is a 32-bit number, which means the number can range from -2,147,483,648 to 2,147,483,647.
To define the variables `foo` and `bar`, we need to use the following syntax:
```
int foo;
int bar = 1;

```

The variable `foo` can be used, but since we did not initialize it, we don't know what's in it. The variable `bar` contains the number 1.
Now, we can do some math. Assuming `a`, `b`, `c`, `d`, and `e` are variables, we can simply use plus, minus and multiplication operators in the following notation, and assign a new value to `a`:
```
int a = 0, b = 1, c = 2, d = 3, e = 4;
a = b - c + d * e;
printf("%d", a); /* will print 1-2+3*4 = 11 */

```

## Exercise
In the next exercise, you will need to create a program which prints out the sum of the numbers `a`, `b`, and `c`.
* * *
[ ](https://www.learn-c.org/en/Hello,_World!) [ Next Tutorial ](https://www.learn-c.org/en/Arrays)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Variables_and_Types)
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
[Pointer Arithmetics](https://www.learn-c.org/en/Pointer_Arithmetics)
[Function Pointers](https://www.learn-c.org/en/Function_Pointers)
[Bitmasks](https://www.learn-c.org/en/Bitmasks)
[Contributing Tutorials](https://www.learn-c.org/en/Contributing_Tutorials)
Copyright © learn-c.org. Read our [Terms of Use](https://www.learn-c.org/tos) and [Privacy Policy](https://www.learn-c.org/privacy)
##### Code
Solution
#include <stdio.h> int main() { int a = 3; float b = 4.5; double c = 5.25; float sum; /* Your code goes here */ printf("The sum of a, b, and c is %f.", sum); return 0; }
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=7030442741473488&rc=)
