[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Dynamic_allocation)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Dynamic_allocation)
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
  * Dynamic allocation


# Dynamic allocation
* * *
Dynamic allocation of memory is a very important subject in C. It allows building complex data structures such as linked lists. Allocating memory dynamically helps us to store data without initially knowing the size of the data in the time we wrote the program.
To allocate a chunk of memory dynamically, we need to have a pointer ready to store the location of the newly allocated memory. We can access memory that was allocated to us using that same pointer, and we can use that pointer to free the memory again, once we have finished using it.
Let's assume we want to dynamically allocate a person structure. The person is defined like this:
```
typedef struct {
    char * name;
    int age;
} person;

```

To allocate a new person in the `myperson` argument, we use the following syntax:
```
person * myperson = (person *) malloc(sizeof(person));

```

This tells the compiler that we want to dynamically allocate just enough to hold a person struct in memory and then return a pointer of type `person` to the newly allocated data. The memory allocation function `malloc()` reserves the specified memory space. In this case, this is the size of `person` in bytes.
The reason we write `(person *)` before the call to `malloc()` is that `malloc()` returns a "void pointer," which is a pointer that doesn't have a type. Writing `(person *)` in front of it is called _typecasting_ , and changes the type of the pointer returned from `malloc()` to be `person`. However, it isn't strictly necessary to write it like this as C will implicitly convert the type of the returned pointer to that of the pointer it is assigned to (in this case, `myperson`) if you don't typecast it.
Note that `sizeof` is not an actual function, because the compiler interprets it and translates it to the actual memory size of the person struct.
To access the person's members, we can use the `->` notation:
```
myperson->name = "John";
myperson->age = 27;

```

After we are done using the dynamically allocated struct, we can release it using `free`:
```
free(myperson);

```

Note that the free does not delete the `myperson` variable itself, it simply releases the data that it points to. The `myperson` variable will still point to somewhere in the memory - but after calling `free(myperson)` we are not allowed to access that area anymore. We must not use that pointer again until we allocate new data using it.
## Exercise
Use `malloc` to dynamically allocate a point structure.
* * *
[ ](https://www.learn-c.org/en/Function_arguments_by_reference) [ Next Tutorial ](https://www.learn-c.org/en/Arrays_and_Pointers)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Dynamic_allocation)
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
#include <stdio.h> #include <stdlib.h> typedef struct { int x; int y; } point; int main() { point * mypoint = NULL; /* Dynamically allocate a new point struct which mypoint points to here */ mypoint->x = 10; mypoint->y =5 ; printf("mypoint coordinates: %d, %d\n", mypoint->x, mypoint->y); free(mypoint); return 0; }
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=1839527466913356&rc=)
