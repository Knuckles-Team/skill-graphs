## How to…[¶](https://docs.python.org/3/library/turtle.html#how-to "Link to this heading")
This section covers some typical turtle use-cases and approaches.
### Get started as quickly as possible[¶](https://docs.python.org/3/library/turtle.html#get-started-as-quickly-as-possible "Link to this heading")
One of the joys of turtle graphics is the immediate, visual feedback that’s available from simple commands - it’s an excellent way to introduce children to programming ideas, with a minimum of overhead (not just children, of course).
The turtle module makes this possible by exposing all its basic functionality as functions, available with `from turtle import *`. The [turtle graphics tutorial](https://docs.python.org/3/library/turtle.html#turtle-tutorial) covers this approach.
It’s worth noting that many of the turtle commands also have even more terse equivalents, such as `fd()` for [`forward()`](https://docs.python.org/3/library/turtle.html#turtle.forward "turtle.forward"). These are especially useful when working with learners for whom typing is not a skill.
> You’ll need to have the [`Tk interface package`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") installed on your system for turtle graphics to work. Be warned that this is not always straightforward, so check this in advance if you’re planning to use turtle graphics with a learner.
### Automatically begin and end filling[¶](https://docs.python.org/3/library/turtle.html#automatically-begin-and-end-filling "Link to this heading")
Starting with Python 3.14, you can use the [`fill()`](https://docs.python.org/3/library/turtle.html#turtle.fill "turtle.fill") [context manager](https://docs.python.org/3/glossary.html#term-context-manager) instead of [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "turtle.begin_fill") and [`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill "turtle.end_fill") to automatically begin and end fill. Here is an example:
Copy```
with fill():
    for i in range(4):
        forward(100)
        right(90)

forward(200)

```

The code above is equivalent to:
Copy```
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()

forward(200)

```

### Use the `turtle` module namespace[¶](https://docs.python.org/3/library/turtle.html#use-the-turtle-module-namespace "Link to this heading")
Using `from turtle import *` is convenient - but be warned that it imports a rather large collection of objects, and if you’re doing anything but turtle graphics you run the risk of a name conflict (this becomes even more an issue if you’re using turtle graphics in a script where other modules might be imported).
The solution is to use `import turtle` - `fd()` becomes `turtle.fd()`, `width()` becomes `turtle.width()` and so on. (If typing “turtle” over and over again becomes tedious, use for example `import turtle as t` instead.)
### Use turtle graphics in a script[¶](https://docs.python.org/3/library/turtle.html#use-turtle-graphics-in-a-script "Link to this heading")
It’s recommended to use the `turtle` module namespace as described immediately above, for example:
Copy```
import turtle as t
from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

```

Another step is also required though - as soon as the script ends, Python will also close the turtle’s window. Add:
Copy```
t.mainloop()

```

to the end of the script. The script will now wait to be dismissed and will not exit until it is terminated, for example by closing the turtle graphics window.
### Use object-oriented turtle graphics[¶](https://docs.python.org/3/library/turtle.html#use-object-oriented-turtle-graphics "Link to this heading")
See also
[Explanation of the object-oriented interface](https://docs.python.org/3/library/turtle.html#turtle-explanation)
Other than for very basic introductory purposes, or for trying things out as quickly as possible, it’s more usual and much more powerful to use the object-oriented approach to turtle graphics. For example, this allows multiple turtles on screen at once.
In this approach, the various turtle commands are methods of objects (mostly of `Turtle` objects). You _can_ use the object-oriented approach in the shell, but it would be more typical in a Python script.
The example above then becomes:
Copy```
from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()

```

Note the last line. `t.screen` is an instance of the [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen") that a Turtle instance exists on; it’s created automatically along with the turtle.
The turtle’s screen can be customised, for example:
Copy```
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")

```
