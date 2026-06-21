## Tutorial[¶](https://docs.python.org/3/library/turtle.html#tutorial "Link to this heading")
New users should start here. In this tutorial we’ll explore some of the basics of turtle drawing.
### Starting a turtle environment[¶](https://docs.python.org/3/library/turtle.html#starting-a-turtle-environment "Link to this heading")
In a Python shell, import all the objects of the `turtle` module:
Copy```
from turtle import *

```

If you run into a `No module named '_tkinter'` error, you’ll have to install the [`Tk interface package`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") on your system.
### Basic drawing[¶](https://docs.python.org/3/library/turtle.html#basic-drawing "Link to this heading")
Send the turtle forward 100 steps:
Copy```
forward(100)

```

You should see (most likely, in a new window on your display) a line drawn by the turtle, heading East. Change the direction of the turtle, so that it turns 120 degrees left (anti-clockwise):
Copy```
left(120)

```

Let’s continue by drawing a triangle:
Copy```
forward(100)
left(120)
forward(100)

```

Notice how the turtle, represented by an arrow, points in different directions as you steer it.
Experiment with those commands, and also with `backward()` and `right()`.
#### Pen control[¶](https://docs.python.org/3/library/turtle.html#pen-control "Link to this heading")
Try changing the color - for example, `color('blue')` - and width of the line - for example, `width(3)` - and then drawing again.
You can also move the turtle around without drawing, by lifting up the pen: `up()` before moving. To start drawing again, use `down()`.
#### The turtle’s position[¶](https://docs.python.org/3/library/turtle.html#the-turtle-s-position "Link to this heading")
Send your turtle back to its starting-point (useful if it has disappeared off-screen):
Copy```
home()

```

The home position is at the center of the turtle’s screen. If you ever need to know them, get the turtle’s x-y coordinates with:
Copy```
pos()

```

Home is at `(0, 0)`.
And after a while, it will probably help to clear the window so we can start anew:
Copy```
clearscreen()

```

### Making algorithmic patterns[¶](https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns "Link to this heading")
Using loops, it’s possible to build up geometric patterns:
Copy```
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

```

- which of course, are limited only by the imagination!
Let’s draw the star shape at the top of this page. We want red lines, filled in with yellow:
Copy```
color('red')
fillcolor('yellow')

```

Just as `up()` and `down()` determine whether lines will be drawn, filling can be turned on and off:
Copy```
begin_fill()

```

Next we’ll create a loop:
Copy```
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

```

`abs(pos()) < 1` is a good way to know when the turtle is back at its home position.
Finally, complete the filling:
Copy```
end_fill()

```

(Note that filling only actually takes place when you give the `end_fill()` command.)
