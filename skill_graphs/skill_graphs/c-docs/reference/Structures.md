[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Structures)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Structures)
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
  * Structures


# Structures
* * *
C structures are special, large variables which contain several named variables inside. Structures are the basic foundation for objects and classes in C. Structures are used for:
  * Serialization of data
  * Passing multiple arguments in and out of functions through a single argument
  * Data structures such as linked lists, binary trees, and more


The most basic example of structures are **points** , which are a single entity that contains two variables - `x` and `y`. Let's define a point:
```
struct point {
    int x;
    int y;
};

```

Now, let's define a new point, and use it. Assume the function `draw` receives a point and draws it on a screen. Without structs, using it would require two arguments - each for every coordinate:
```
/* draws a point at 10, 5 */
int x = 10;
int y = 5;
draw(x, y);

```

Using structs, we can pass a point argument:
```
/* draws a point at 10, 5 */
struct point p;
p.x = 10;
p.y = 5;
draw(p);

```

To access the point's variables, we use the dot `.` operator.
### Typedefs
Typedefs allow us to define types with a different name - which can come in handy when dealing with structs and pointers. In this case, we'd want to get rid of the long definition of a point structure. We can use the following syntax to remove the `struct` keyword from each time we want to define a new point:
```
typedef struct {
    int x;
    int y;
} point;

```

This will allow us to define a new point like this:
```
point p;

```

Structures can also hold pointers - which allows them to hold strings, or pointers to other structures as well - which is their real power. For example, we can define a vehicle structure in the following manner:
```
typedef struct {
    char * brand;
    int model;
} vehicle;

```

Since brand is a char pointer, the vehicle type can contain a string (which, in this case, indicates the brand of the vehicle).
```
vehicle mycar;
mycar.brand = "Ford";
mycar.model = 2007;

```

## Exercise
Define a new data structure, named "person", which contains a string (pointer to char) called `name`, and an integer called `age`.
* * *
[ ](https://www.learn-c.org/en/Pointers) [ Next Tutorial ](https://www.learn-c.org/en/Function_arguments_by_reference)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Structures)
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
#include <stdio.h> /* define the person struct here using the typedef syntax */ int main() { person john; /* testing code */ john.name = "John"; john.age = 27; printf("%s is %d years old.", john.name, john.age); }
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=554521324062232&rc=)
