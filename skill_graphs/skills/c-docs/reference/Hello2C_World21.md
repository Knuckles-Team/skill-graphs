[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Hello%2C_World%21)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Hello%2C_World%21)
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
  * Hello, World!


# Hello, World!
* * *
### Introduction
The C programming language is a general purpose programming language, which relates closely to the way machines work. Understanding how computer memory works is an important aspect of the C programming language. Although C can be considered as "hard to learn", C is in fact a very simple language, with very powerful capabilities.
C is a very common language, and it is the language of many applications such as Windows, the Python interpreter, Git, and many many more.
C is a compiled language - which means that in order to run it, the compiler (for example, GCC or Visual Studio) must take the code that we wrote, process it, and then create an executable file. This file can then be executed, and will do what we intended for the program to do.
### Our first program
Every C program uses libraries, which give the ability to execute necessary functions. For example, the most basic function called `printf`, which prints to the screen, is defined in the `stdio.h` header file.
To add the ability to run the `printf` command to our program, we must add the following include directive to our first line of the code:
```
#include <stdio.h>

```

The second part of the code is the actual code which we are going to write. The first code which will run will always reside in the `main` function.
```
int main() {
  ... our code goes here
}

```

The `int` keyword indicates that the function `main` will return an integer - a simple number. The number which will be returned by the function indicates whether the program that we wrote worked correctly. If we want to say that our code was run successfully, we will return the number 0. A number greater than 0 will mean that the program that we wrote failed.
For this tutorial, we will return 0 to indicate that our program was successful:
```
return 0;

```

Notice that every statement in C must end with a semicolon, so that the compiler knows that a new statement has started.
Last but not least, we will need to call the function `printf` to print our sentence.
## Exercise
Change the program at the bottom so that it prints to the output "Hello, World!".
* * *
[ Next Tutorial ](https://www.learn-c.org/en/Variables_and_Types)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Hello%2C_World%21)
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
#include <stdio.h> int main() { printf("Goodbye, World!"); return 0; }
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=5566549295042095&rc=)
