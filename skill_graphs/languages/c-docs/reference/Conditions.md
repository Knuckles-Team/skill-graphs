[ ![](https://www.learn-c.org/static/img/favicons/learn-c.org.ico) learn-c.org ](https://www.learn-c.org/)
  * [Home (current)](https://www.learn-c.org/)
  * [About](https://www.learn-c.org/about)
  * [ More Languages ](https://www.learn-c.org/en/Conditions)
[C](https://www.learn-c.org)


  * [ ![Languages](https://www.learn-c.org/static/img/icon20x24px-exported-transparent.png) ](https://www.learn-c.org/en/Conditions)
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
  * Conditions


# Conditions
* * *
### Decision Making
In life, we all have to make decisions. In order to make a decision we weigh out our options and so do our programs.
Here is the general form of the decision making structures found in C.
```
int target = 10;
if (target == 10) {
    printf("Target is equal to 10");
}

```

### The `if` statement
The `if` statement allows us to check if an expression is `true` or `false`, and execute different code according to the result.
To evaluate whether two variables are equal, the `==` operator is used, just like in the first example.
Inequality operators can also be used to evaluate expressions. For example:
```
int foo = 1;
int bar = 2;

if (foo < bar) {
    printf("foo is smaller than bar.");
}

if (foo > bar) {
    printf("foo is greater than bar.");
}

```

We can use the `else` keyword to execute code when our expression evaluates to `false`.
```
int foo = 1;
int bar = 2;

if (foo < bar) {
    printf("foo is smaller than bar.");
} else {
    printf("foo is greater than bar.");
}

```

Sometimes we will have more than two outcomes to choose from. In these cases, we can "chain" multiple `if` `else` statements together.
```
int foo = 1;
int bar = 2;

if (foo < bar) {
    printf("foo is smaller than bar.");
} else if (foo == bar) {
    printf("foo is equal to bar.");
} else {
    printf("foo is greater than bar.");
}

```

You can also nest `if` `else` statements if you like.
```
int peanuts_eaten = 22;
int peanuts_in_jar = 100;
int max_peanut_limit = 50;

if (peanuts_in_jar > 80) {
    if (peanuts_eaten < max_peanut_limit) {
        printf("Take as many peanuts as you want!\n");
    }
} else {
    if (peanuts_eaten > peanuts_in_jar) {
        printf("You can't have anymore peanuts!\n");
    }
    else {
        printf("Alright, just one more peanut.\n");
    }
}

```

Two or more expressions can be evaluated together using logical operators to check if two expressions evaluate to `true` together, or at least one of them. To check if two expressions both evaluate to `true`, use the AND operator `&&`. To check if at least one of the expressions evaluate to `true`, use the OR operator `||`.
```
int foo = 1;
int bar = 2;
int moo = 3;

if (foo < bar && moo > bar) {
    printf("foo is smaller than bar AND moo is larger than bar.");
}

if (foo < bar || moo > bar) {
    printf("foo is smaller than bar OR moo is larger than bar.");
}

```

The NOT operator `!` can also be used likewise:
```
int target = 9;
if (target != 10) {
    printf("Target is not equal to 10");
}

```

## Exercise
In this exercise, you must construct an `if` statement inside the `guessNumber` function statement that checks if the number `guess` is equal to 555. If that is the case, the function must print out using `printf` "Correct. You guessed it!". If `guess` is less than 555, the function must print out using `printf` "Your guess is too low." If `guess` is greater than 555, the function must print out using `printf` "Your guess is too high."
  * **Important** : Don't forget to add a newline character `\n` at the end of the printf string.


* * *
[ ](https://www.learn-c.org/en/Multidimensional_Arrays) [ Next Tutorial ](https://www.learn-c.org/en/Strings)
#### Sponsors
* * *
[ ![](https://www.learn-c.org/static/img/masterschool.png) ](https://www.learn-c.org/en/Conditions)
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
#include <stdio.h> void guessNumber(int guess) { // TODO: write your code here } int main() { guessNumber(500); guessNumber(600); guessNumber(555); }
```
#include <stdio.h>
```

##### Output
Expected Output
```
 
```

Powered by
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gda_r20260305&jk=4151142981157897&rc=)
