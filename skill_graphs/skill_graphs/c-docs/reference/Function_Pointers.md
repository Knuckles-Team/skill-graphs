[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Function_Pointers)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Function_Pointers)
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
  * Function Pointers


# Function Pointers
* * *
Remember pointers? We used them to point to an array of chars then make a string out of them. Then things got more interesting when we learned how to control these pointers. Now it is time to do something even more interesting with pointers, using them to point to and call functions.
### Why point to a function?
The first question that may come to your mind is why would we use pointers to call a function when we can simply call a function by its name: `function();` - that's a great question! Now imagine the `sort` function where you need to sort an array. Sometimes you want to order array elements in an ascending order or descending order. How would you choose? Function pointers!
### Function Pointer Syntax
```
void (*pf)(int);

```

I agree with you. This definitely is very complicated, or so you may think. Let's re-read that code and try to understand it point by point. Read it inside-out. `*pf` is the pointer to a function. `void` is the return type of that function, and finally `int` is the argument type of that function. Got it? Good.
Let's insert pointers into the function pointer and try to read it again:
```
char* (*pf)(int*)

```

Again: 1. `*pf` is the function pointer. 2. `char*` is the return type of that function. 3. `int*` is the type of the argument.
Ok enough with theory. Let's get our hands dirty with some real code. See this example:
```
#include <stdio.h>
void someFunction(int arg)
{
    printf("This is someFunction being called and arg is: %d\n", arg);
    printf("Whoops leaving the function now!\n");
}

main()
{
    void (*pf)(int);
    pf = &someFunction;
    printf("We're about to call someFunction() using a pointer!\n");
    (pf)(5);
    printf("Wow that was cool. Back to main now!\n\n");
}

```

Remember `sort()` we talked about earlier? We can do the same with it. Instead of ordering a set in an ascending way we can do the opposite using our own comparison function as follows:
```
#include <stdio.h>
#include <stdlib.h> //for qsort()

int compare(const void* left, const void* right)
{
    return (*(int*)right - *(int*)left);
    // go back to ref if this seems complicated: http://www.cplusplus.com/reference/cstdlib/qsort/
}
main()
{
    int (*cmp) (const void* , const void*);
    cmp = &compare;

    int iarray[] = {1,2,3,4,5,6,7,8,9};
    qsort(iarray, sizeof(iarray)/sizeof(*iarray), sizeof(*iarray), cmp);

    int c = 0;
    while (c < sizeof(iarray)/sizeof(*iarray))
    {
        printf("%d \t", iarray[c]);
        c++;
    }
}

```

Let's remember again. Why do we use function pointers? 1. To allow programmers to use libraries for different usages -> "Flexibility"
## Exercise
Complete the array of pointers to functions and call each function using its pointer from the array. Array of pointers to functions? Yes you can do that!
* * *
[ ](https://www.learn-c.org/en/Pointer_Arithmetics) [ Next Tutorial ](https://www.learn-c.org/en/Bitmasks)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Function_Pointers)
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
#include <stdio.h> void f1(int var) { printf("this is f1 and var is: %d\n", var); } void f2(int var) { printf("this is f2 and var is: %d\n", var); } void f3(int var) { printf("this is f3 and var is: %d\n", var); } int main() { /* define an array full of function pointers to the above functions, that take an `int` as their only argument */ int c = 0; while(c < 3) { /* call the functions using the function pointers of the array at index `c` with `c` as an argument */ ++c; } return 0; }
```
    #include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=2077303268282339&rc=)
