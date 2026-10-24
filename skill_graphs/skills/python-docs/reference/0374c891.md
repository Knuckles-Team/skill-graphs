## Methods of RawTurtle/Turtle and corresponding functions[¶](https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions "Link to this heading")
Most of the examples in this section refer to a Turtle instance called `turtle`.
### Turtle motion[¶](https://docs.python.org/3/library/turtle.html#turtle-motion "Link to this heading")

turtle.forward(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.forward "Link to this definition")


turtle.fd(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.fd "Link to this definition")


Parameters:

**distance** – a number (integer or float)
Move the turtle forward by the specified _distance_ , in the direction the turtle is headed.
Copy```
>>> turtle.position()
(0.00,0.00)
>>> turtle.forward(25)
>>> turtle.position()
(25.00,0.00)
>>> turtle.forward(-75)
>>> turtle.position()
(-50.00,0.00)

```


turtle.back(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.back "Link to this definition")


turtle.bk(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.bk "Link to this definition")


turtle.backward(_distance_)[¶](https://docs.python.org/3/library/turtle.html#turtle.backward "Link to this definition")


Parameters:

**distance** – a number
Move the turtle backward by _distance_ , opposite to the direction the turtle is headed. Do not change the turtle’s heading.
Copy```
>>> turtle.position()
(0.00,0.00)
>>> turtle.backward(30)
>>> turtle.position()
(-30.00,0.00)

```


turtle.right(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.right "Link to this definition")


turtle.rt(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.rt "Link to this definition")


Parameters:

**angle** – a number (integer or float)
Turn turtle right by _angle_ units. (Units are by default degrees, but can be set via the [`degrees()`](https://docs.python.org/3/library/turtle.html#turtle.degrees "turtle.degrees") and [`radians()`](https://docs.python.org/3/library/turtle.html#turtle.radians "turtle.radians") functions.) Angle orientation depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode").
Copy```
>>> turtle.heading()
22.0
>>> turtle.right(45)
>>> turtle.heading()
337.0

```


turtle.left(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.left "Link to this definition")


turtle.lt(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.lt "Link to this definition")


Parameters:

**angle** – a number (integer or float)
Turn turtle left by _angle_ units. (Units are by default degrees, but can be set via the [`degrees()`](https://docs.python.org/3/library/turtle.html#turtle.degrees "turtle.degrees") and [`radians()`](https://docs.python.org/3/library/turtle.html#turtle.radians "turtle.radians") functions.) Angle orientation depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode").
Copy```
>>> turtle.heading()
22.0
>>> turtle.left(45)
>>> turtle.heading()
67.0

```


turtle.goto(_x_ , _y =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.goto "Link to this definition")


turtle.setpos(_x_ , _y =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setpos "Link to this definition")


turtle.setposition(_x_ , _y =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setposition "Link to this definition")


Parameters:

  * **x** – a number or a pair/vector of numbers
  * **y** – a number or `None`


If _y_ is `None`, _x_ must be a pair of coordinates or a [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D") (e.g. as returned by [`pos()`](https://docs.python.org/3/library/turtle.html#turtle.pos "turtle.pos")).
Move turtle to an absolute position. If the pen is down, draw line. Do not change the turtle’s orientation.
Copy```
>>> tp = turtle.pos()
>>> tp
(0.00,0.00)
>>> turtle.setpos(60,30)
>>> turtle.pos()
(60.00,30.00)
>>> turtle.setpos((20,80))
>>> turtle.pos()
(20.00,80.00)
>>> turtle.setpos(tp)
>>> turtle.pos()
(0.00,0.00)

```


turtle.teleport(_x_ , _y =None_, _*_ , _fill_gap =False_)[¶](https://docs.python.org/3/library/turtle.html#turtle.teleport "Link to this definition")


Parameters:

  * **x** – a number or `None`
  * **y** – a number or `None`
  * **fill_gap** – a boolean


Move turtle to an absolute position. Unlike goto(x, y), a line will not be drawn. The turtle’s orientation does not change. If currently filling, the polygon(s) teleported from will be filled after leaving, and filling will begin again after teleporting. This can be disabled with fill_gap=True, which makes the imaginary line traveled during teleporting act as a fill barrier like in goto(x, y).
Copy```
>>> tp = turtle.pos()
>>> tp
(0.00,0.00)
>>> turtle.teleport(60)
>>> turtle.pos()
(60.00,0.00)
>>> turtle.teleport(y=10)
>>> turtle.pos()
(60.00,10.00)
>>> turtle.teleport(20, 30)
>>> turtle.pos()
(20.00,30.00)

```

Added in version 3.12.

turtle.setx(_x_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setx "Link to this definition")


Parameters:

**x** – a number (integer or float)
Set the turtle’s first coordinate to _x_ , leave second coordinate unchanged.
Copy```
>>> turtle.position()
(0.00,240.00)
>>> turtle.setx(10)
>>> turtle.position()
(10.00,240.00)

```


turtle.sety(_y_)[¶](https://docs.python.org/3/library/turtle.html#turtle.sety "Link to this definition")


Parameters:

**y** – a number (integer or float)
Set the turtle’s second coordinate to _y_ , leave first coordinate unchanged.
Copy```
>>> turtle.position()
(0.00,40.00)
>>> turtle.sety(-10)
>>> turtle.position()
(0.00,-10.00)

```


turtle.setheading(_to_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setheading "Link to this definition")


turtle.seth(_to_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.seth "Link to this definition")


Parameters:

**to_angle** – a number (integer or float)
Set the orientation of the turtle to _to_angle_. Here are some common directions in degrees:
standard mode | logo mode
---|---
0 - east | 0 - north
90 - north | 90 - east
180 - west | 180 - south
270 - south | 270 - west
Copy```
>>> turtle.setheading(90)
>>> turtle.heading()
90.0

```


turtle.home()[¶](https://docs.python.org/3/library/turtle.html#turtle.home "Link to this definition")

Move turtle to the origin – coordinates (0,0) – and set its heading to its start-orientation (which depends on the mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")).
Copy```
>>> turtle.heading()
90.0
>>> turtle.position()
(0.00,-10.00)
>>> turtle.home()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0

```


turtle.circle(_radius_ , _extent =None_, _steps =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.circle "Link to this definition")


Parameters:

  * **radius** – a number
  * **extent** – a number (or `None`)
  * **steps** – an integer (or `None`)


Draw a circle with given _radius_. The center is _radius_ units left of the turtle; _extent_ – an angle – determines which part of the circle is drawn. If _extent_ is not given, draw the entire circle. If _extent_ is not a full circle, one endpoint of the arc is the current pen position. Draw the arc in counterclockwise direction if _radius_ is positive, otherwise in clockwise direction. Finally the direction of the turtle is changed by the amount of _extent_.
As the circle is approximated by an inscribed regular polygon, _steps_ determines the number of steps to use. If not given, it will be calculated automatically. May be used to draw regular polygons.
Copy```
>>> turtle.home()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0
>>> turtle.circle(50)
>>> turtle.position()
(-0.00,0.00)
>>> turtle.heading()
0.0
>>> turtle.circle(120, 180)  # draw a semicircle
>>> turtle.position()
(0.00,240.00)
>>> turtle.heading()
180.0

```


turtle.dot()[¶](https://docs.python.org/3/library/turtle.html#turtle.dot "Link to this definition")


turtle.dot(_size_)


turtle.dot(_color_ , _/_)


turtle.dot(_size_ , _color_ , _/_)


turtle.dot(_size_ , _r_ , _g_ , _b_ , _/_)


Parameters:

  * **size** – an integer >= 1 (if given)
  * **color** – a colorstring or a numeric color tuple


Draw a circular dot with diameter _size_ , using _color_. If _size_ is not given, the maximum of `pensize+4` and `2*pensize` is used.
Copy```
>>> turtle.home()
>>> turtle.dot()
>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
>>> turtle.position()
(100.00,-0.00)
>>> turtle.heading()
0.0

```


turtle.stamp()[¶](https://docs.python.org/3/library/turtle.html#turtle.stamp "Link to this definition")

Stamp a copy of the turtle shape onto the canvas at the current turtle position. Return a stamp_id for that stamp, which can be used to delete it by calling `clearstamp(stamp_id)`.
Copy```
>>> turtle.color("blue")
>>> stamp_id = turtle.stamp()
>>> turtle.fd(50)

```


turtle.clearstamp(_stampid_)[¶](https://docs.python.org/3/library/turtle.html#turtle.clearstamp "Link to this definition")


Parameters:

**stampid** – an integer, must be return value of previous [`stamp()`](https://docs.python.org/3/library/turtle.html#turtle.stamp "turtle.stamp") call
Delete stamp with given _stampid_.
Copy```
>>> turtle.position()
(150.00,-0.00)
>>> turtle.color("blue")
>>> astamp = turtle.stamp()
>>> turtle.fd(50)
>>> turtle.position()
(200.00,-0.00)
>>> turtle.clearstamp(astamp)
>>> turtle.position()
(200.00,-0.00)

```


turtle.clearstamps(_n =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.clearstamps "Link to this definition")


Parameters:

**n** – an integer (or `None`)
Delete all or first/last _n_ of turtle’s stamps. If _n_ is `None`, delete all stamps, if _n_ > 0 delete first _n_ stamps, else if _n_ < 0 delete last _n_ stamps.
Copy```
>>> for i in range(8):
...     unused_stamp_id = turtle.stamp()
...     turtle.fd(30)
>>> turtle.clearstamps(2)
>>> turtle.clearstamps(-2)
>>> turtle.clearstamps()

```


turtle.undo()[¶](https://docs.python.org/3/library/turtle.html#turtle.undo "Link to this definition")

Undo (repeatedly) the last turtle action(s). Number of available undo actions is determined by the size of the undobuffer.
Copy```
>>> for i in range(4):
...     turtle.fd(50); turtle.lt(80)
...
>>> for i in range(8):
...     turtle.undo()

```


turtle.speed(_speed =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.speed "Link to this definition")


Parameters:

**speed** – an integer in the range 0..10 or a speedstring (see below)
Set the turtle’s speed to an integer value in the range 0..10. If no argument is given, return current speed.
If input is a number greater than 10 or smaller than 0.5, speed is set to 0. Speedstrings are mapped to speedvalues as follows:
  * “fastest”: 0
  * “fast”: 10
  * “normal”: 6
  * “slow”: 3
  * “slowest”: 1


Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning.
Attention: _speed_ = 0 means that _no_ animation takes place. forward/back makes turtle jump and likewise left/right make the turtle turn instantly.
Copy```
>>> turtle.speed()
3
>>> turtle.speed('normal')
>>> turtle.speed()
6
>>> turtle.speed(9)
>>> turtle.speed()
9

```

### Tell Turtle’s state[¶](https://docs.python.org/3/library/turtle.html#tell-turtle-s-state "Link to this heading")

turtle.position()[¶](https://docs.python.org/3/library/turtle.html#turtle.position "Link to this definition")


turtle.pos()[¶](https://docs.python.org/3/library/turtle.html#turtle.pos "Link to this definition")

Return the turtle’s current location (x,y) (as a [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D") vector).
Copy```
>>> turtle.pos()
(440.00,-0.00)

```


turtle.towards(_x_ , _y =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.towards "Link to this definition")


Parameters:

  * **x** – a number or a pair/vector of numbers or a turtle instance
  * **y** – a number if _x_ is a number, else `None`


Return the angle between the line from turtle position to position specified by (x,y), the vector or the other turtle. This depends on the turtle’s start orientation which depends on the mode - “standard”/”world” or “logo”.
Copy```
>>> turtle.goto(10, 10)
>>> turtle.towards(0,0)
225.0

```


turtle.xcor()[¶](https://docs.python.org/3/library/turtle.html#turtle.xcor "Link to this definition")

Return the turtle’s x coordinate.
Copy```
>>> turtle.home()
>>> turtle.left(50)
>>> turtle.forward(100)
>>> turtle.pos()
(64.28,76.60)
>>> print(round(turtle.xcor(), 5))
64.27876

```


turtle.ycor()[¶](https://docs.python.org/3/library/turtle.html#turtle.ycor "Link to this definition")

Return the turtle’s y coordinate.
Copy```
>>> turtle.home()
>>> turtle.left(60)
>>> turtle.forward(100)
>>> print(turtle.pos())
(50.00,86.60)
>>> print(round(turtle.ycor(), 5))
86.60254

```


turtle.heading()[¶](https://docs.python.org/3/library/turtle.html#turtle.heading "Link to this definition")

Return the turtle’s current heading (value depends on the turtle mode, see [`mode()`](https://docs.python.org/3/library/turtle.html#turtle.mode "turtle.mode")).
Copy```
>>> turtle.home()
>>> turtle.left(67)
>>> turtle.heading()
67.0

```


turtle.distance(_x_ , _y =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.distance "Link to this definition")


Parameters:

  * **x** – a number or a pair/vector of numbers or a turtle instance
  * **y** – a number if _x_ is a number, else `None`


Return the distance from the turtle to (x,y), the given vector, or the given other turtle, in turtle step units.
Copy```
>>> turtle.home()
>>> turtle.distance(30,40)
50.0
>>> turtle.distance((30,40))
50.0
>>> joe = Turtle()
>>> joe.forward(77)
>>> turtle.distance(joe)
77.0

```

### Settings for measurement[¶](https://docs.python.org/3/library/turtle.html#settings-for-measurement "Link to this heading")

turtle.degrees(_fullcircle =360.0_)[¶](https://docs.python.org/3/library/turtle.html#turtle.degrees "Link to this definition")


Parameters:

**fullcircle** – a number
Set angle measurement units, i.e. set number of “degrees” for a full circle. Default value is 360 degrees.
Copy```
>>> turtle.home()
>>> turtle.left(90)
>>> turtle.heading()
90.0

>>> # Change angle measurement unit to grad (also known as gon,
>>> # grade, or gradian and equals 1/100-th of the right angle.)
>>> turtle.degrees(400.0)
>>> turtle.heading()
100.0
>>> turtle.degrees(360)
>>> turtle.heading()
90.0

```


turtle.radians()[¶](https://docs.python.org/3/library/turtle.html#turtle.radians "Link to this definition")

Set the angle measurement units to radians. Equivalent to `degrees(2*math.pi)`.
Copy```
>>> turtle.home()
>>> turtle.left(90)
>>> turtle.heading()
90.0
>>> turtle.radians()
>>> turtle.heading()
1.5707963267948966

```

### Pen control[¶](https://docs.python.org/3/library/turtle.html#id1 "Link to this heading")
#### Drawing state[¶](https://docs.python.org/3/library/turtle.html#drawing-state "Link to this heading")

turtle.pendown()[¶](https://docs.python.org/3/library/turtle.html#turtle.pendown "Link to this definition")


turtle.pd()[¶](https://docs.python.org/3/library/turtle.html#turtle.pd "Link to this definition")


turtle.down()[¶](https://docs.python.org/3/library/turtle.html#turtle.down "Link to this definition")

Pull the pen down – drawing when moving.

turtle.penup()[¶](https://docs.python.org/3/library/turtle.html#turtle.penup "Link to this definition")


turtle.pu()[¶](https://docs.python.org/3/library/turtle.html#turtle.pu "Link to this definition")


turtle.up()[¶](https://docs.python.org/3/library/turtle.html#turtle.up "Link to this definition")

Pull the pen up – no drawing when moving.

turtle.pensize(_width =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.pensize "Link to this definition")


turtle.width(_width =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.width "Link to this definition")


Parameters:

**width** – a positive number
Set the line thickness to _width_ or return it. If resizemode is set to “auto” and turtleshape is a polygon, that polygon is drawn with the same line thickness. If no argument is given, the current pensize is returned.
Copy```
>>> turtle.pensize()
1
>>> turtle.pensize(10)   # from here on lines of width 10 are drawn

```


turtle.pen(_pen =None_, _** pendict_)[¶](https://docs.python.org/3/library/turtle.html#turtle.pen "Link to this definition")


Parameters:

  * **pen** – a dictionary with some or all of the below listed keys
  * **pendict** – one or more keyword-arguments with the below listed keys as keywords


Return or set the pen’s attributes in a “pen-dictionary” with the following key/value pairs:
  * “shown”: True/False
  * “pendown”: True/False
  * “pencolor”: color-string or color-tuple
  * “fillcolor”: color-string or color-tuple
  * “pensize”: positive number
  * “speed”: number in range 0..10
  * “resizemode”: “auto” or “user” or “noresize”
  * “stretchfactor”: (positive number, positive number)
  * “outline”: positive number
  * “tilt”: number


This dictionary can be used as argument for a subsequent call to `pen()` to restore the former pen-state. Moreover one or more of these attributes can be provided as keyword-arguments. This can be used to set several pen attributes in one statement.
Copy```
>>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
>>> sorted(turtle.pen().items())
[('fillcolor', 'black'), ('outline', 1), ('pencolor', 'red'),
 ('pendown', True), ('pensize', 10), ('resizemode', 'noresize'),
 ('shearfactor', 0.0), ('shown', True), ('speed', 9),
 ('stretchfactor', (1.0, 1.0)), ('tilt', 0.0)]
>>> penstate=turtle.pen()
>>> turtle.color("yellow", "")
>>> turtle.penup()
>>> sorted(turtle.pen().items())[:3]
[('fillcolor', ''), ('outline', 1), ('pencolor', 'yellow')]
>>> turtle.pen(penstate, fillcolor="green")
>>> sorted(turtle.pen().items())[:3]
[('fillcolor', 'green'), ('outline', 1), ('pencolor', 'red')]

```


turtle.isdown()[¶](https://docs.python.org/3/library/turtle.html#turtle.isdown "Link to this definition")

Return `True` if pen is down, `False` if it’s up.
Copy```
>>> turtle.penup()
>>> turtle.isdown()
False
>>> turtle.pendown()
>>> turtle.isdown()
True

```

#### Color control[¶](https://docs.python.org/3/library/turtle.html#color-control "Link to this heading")

turtle.pencolor()[¶](https://docs.python.org/3/library/turtle.html#turtle.pencolor "Link to this definition")


turtle.pencolor(_color_ , _/_)


turtle.pencolor(_r_ , _g_ , _b_ , _/_)

Return or set the pencolor.
Four input formats are allowed:

`pencolor()`

Return the current pencolor as color specification string or as a tuple (see example). May be used as input to another color/pencolor/fillcolor/bgcolor call.

`pencolor(colorstring)`

Set pencolor to _colorstring_ , which is a Tk color specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

`pencolor((r, g, b))`

Set pencolor to the RGB color represented by the tuple of _r_ , _g_ , and _b_. Each of _r_ , _g_ , and _b_ must be in the range 0..colormode, where colormode is either 1.0 or 255 (see [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")).

`pencolor(r, g, b)`

Set pencolor to the RGB color represented by _r_ , _g_ , and _b_. Each of _r_ , _g_ , and _b_ must be in the range 0..colormode.
If turtleshape is a polygon, the outline of that polygon is drawn with the newly set pencolor.
Copy```
>>> colormode()
1.0
>>> turtle.pencolor()
'red'
>>> turtle.pencolor("brown")
>>> turtle.pencolor()
'brown'
>>> tup = (0.2, 0.8, 0.55)
>>> turtle.pencolor(tup)
>>> turtle.pencolor()
(0.2, 0.8, 0.5490196078431373)
>>> colormode(255)
>>> turtle.pencolor()
(51.0, 204.0, 140.0)
>>> turtle.pencolor('#32c18f')
>>> turtle.pencolor()
(50.0, 193.0, 143.0)

```


turtle.fillcolor()[¶](https://docs.python.org/3/library/turtle.html#turtle.fillcolor "Link to this definition")


turtle.fillcolor(_color_ , _/_)


turtle.fillcolor(_r_ , _g_ , _b_ , _/_)

Return or set the fillcolor.
Four input formats are allowed:

`fillcolor()`

Return the current fillcolor as color specification string, possibly in tuple format (see example). May be used as input to another color/pencolor/fillcolor/bgcolor call.

`fillcolor(colorstring)`

Set fillcolor to _colorstring_ , which is a Tk color specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

`fillcolor((r, g, b))`

Set fillcolor to the RGB color represented by the tuple of _r_ , _g_ , and _b_. Each of _r_ , _g_ , and _b_ must be in the range 0..colormode, where colormode is either 1.0 or 255 (see [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")).

`fillcolor(r, g, b)`

Set fillcolor to the RGB color represented by _r_ , _g_ , and _b_. Each of _r_ , _g_ , and _b_ must be in the range 0..colormode.
If turtleshape is a polygon, the interior of that polygon is drawn with the newly set fillcolor.
Copy```
>>> turtle.fillcolor("violet")
>>> turtle.fillcolor()
'violet'
>>> turtle.pencolor()
(50.0, 193.0, 143.0)
>>> turtle.fillcolor((50, 193, 143))  # Integers, not floats
>>> turtle.fillcolor()
(50.0, 193.0, 143.0)
>>> turtle.fillcolor('#ffffff')
>>> turtle.fillcolor()
(255.0, 255.0, 255.0)

```


turtle.color()[¶](https://docs.python.org/3/library/turtle.html#turtle.color "Link to this definition")


turtle.color(_color_ , _/_)


turtle.color(_r_ , _g_ , _b_ , _/_)


turtle.color(_pencolor_ , _fillcolor_ , _/_)

Return or set pencolor and fillcolor.
Several input formats are allowed. They use 0 to 3 arguments as follows:

`color()`

Return the current pencolor and the current fillcolor as a pair of color specification strings or tuples as returned by [`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor "turtle.pencolor") and [`fillcolor()`](https://docs.python.org/3/library/turtle.html#turtle.fillcolor "turtle.fillcolor").

`color(colorstring)`, `color((r,g,b))`, `color(r,g,b)`

Inputs as in [`pencolor()`](https://docs.python.org/3/library/turtle.html#turtle.pencolor "turtle.pencolor"), set both, fillcolor and pencolor, to the given value.

`color(colorstring1, colorstring2)`, `color((r1,g1,b1), (r2,g2,b2))`

Equivalent to `pencolor(colorstring1)` and `fillcolor(colorstring2)` and analogously if the other input format is used.
If turtleshape is a polygon, outline and interior of that polygon is drawn with the newly set colors.
Copy```
>>> turtle.color("red", "green")
>>> turtle.color()
('red', 'green')
>>> color("#285078", "#a0c8f0")
>>> color()
((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))

```

See also: Screen method [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode").
#### Filling[¶](https://docs.python.org/3/library/turtle.html#filling "Link to this heading")

turtle.filling()[¶](https://docs.python.org/3/library/turtle.html#turtle.filling "Link to this definition")

Return fillstate (`True` if filling, `False` else).
Copy```
>>> turtle.begin_fill()
>>> if turtle.filling():
...    turtle.pensize(5)
... else:
...    turtle.pensize(3)

```


turtle.fill()[¶](https://docs.python.org/3/library/turtle.html#turtle.fill "Link to this definition")

Fill the shape drawn in the `with turtle.fill():` block.
Copy```
>>> turtle.color("black", "red")
>>> with turtle.fill():
...     turtle.circle(80)

```

Using `fill()` is equivalent to adding the [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "turtle.begin_fill") before the fill-block and [`end_fill()`](https://docs.python.org/3/library/turtle.html#turtle.end_fill "turtle.end_fill") after the fill-block:
Copy```
>>> turtle.color("black", "red")
>>> turtle.begin_fill()
>>> turtle.circle(80)
>>> turtle.end_fill()

```

Added in version 3.14.

turtle.begin_fill()[¶](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "Link to this definition")

To be called just before drawing a shape to be filled.

turtle.end_fill()[¶](https://docs.python.org/3/library/turtle.html#turtle.end_fill "Link to this definition")

Fill the shape drawn after the last call to [`begin_fill()`](https://docs.python.org/3/library/turtle.html#turtle.begin_fill "turtle.begin_fill").
Whether or not overlap regions for self-intersecting polygons or multiple shapes are filled depends on the operating system graphics, type of overlap, and number of overlaps. For example, the Turtle star above may be either all yellow or have some white regions.
Copy```
>>> turtle.color("black", "red")
>>> turtle.begin_fill()
>>> turtle.circle(80)
>>> turtle.end_fill()

```

#### More drawing control[¶](https://docs.python.org/3/library/turtle.html#more-drawing-control "Link to this heading")

turtle.reset()[¶](https://docs.python.org/3/library/turtle.html#turtle.reset "Link to this definition")

Delete the turtle’s drawings from the screen, re-center the turtle and set variables to the default values.
Copy```
>>> turtle.goto(0,-22)
>>> turtle.left(100)
>>> turtle.position()
(0.00,-22.00)
>>> turtle.heading()
100.0
>>> turtle.reset()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0

```


turtle.clear()[¶](https://docs.python.org/3/library/turtle.html#turtle.clear "Link to this definition")

Delete the turtle’s drawings from the screen. Do not move turtle. State and position of the turtle as well as drawings of other turtles are not affected.

turtle.write(_arg_ , _move =False_, _align ='left'_, _font =('Arial', 8, 'normal')_)[¶](https://docs.python.org/3/library/turtle.html#turtle.write "Link to this definition")


Parameters:

  * **arg** – object to be written to the TurtleScreen
  * **move** – True/False
  * **align** – one of the strings “left”, “center” or right”
  * **font** – a triple (fontname, fontsize, fonttype)


Write text - the string representation of _arg_ - at the current turtle position according to _align_ (“left”, “center” or “right”) and with the given font. If _move_ is true, the pen is moved to the bottom-right corner of the text. By default, _move_ is `False`.
Copy```
>>> turtle.write("Home = ", True, align="center")
>>> turtle.write((0,0), True)

```

### Turtle state[¶](https://docs.python.org/3/library/turtle.html#turtle-state "Link to this heading")
#### Visibility[¶](https://docs.python.org/3/library/turtle.html#visibility "Link to this heading")

turtle.hideturtle()[¶](https://docs.python.org/3/library/turtle.html#turtle.hideturtle "Link to this definition")


turtle.ht()[¶](https://docs.python.org/3/library/turtle.html#turtle.ht "Link to this definition")

Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing some complex drawing, because hiding the turtle speeds up the drawing observably.
Copy```
>>> turtle.hideturtle()

```


turtle.showturtle()[¶](https://docs.python.org/3/library/turtle.html#turtle.showturtle "Link to this definition")


turtle.st()[¶](https://docs.python.org/3/library/turtle.html#turtle.st "Link to this definition")

Make the turtle visible.
Copy```
>>> turtle.showturtle()

```


turtle.isvisible()[¶](https://docs.python.org/3/library/turtle.html#turtle.isvisible "Link to this definition")

Return `True` if the Turtle is shown, `False` if it’s hidden.
Copy```
>>> turtle.hideturtle()
>>> turtle.isvisible()
False
>>> turtle.showturtle()
>>> turtle.isvisible()
True

```

#### Appearance[¶](https://docs.python.org/3/library/turtle.html#appearance "Link to this heading")

turtle.shape(_name =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shape "Link to this definition")


Parameters:

**name** – a string which is a valid shapename
Set turtle shape to shape with given _name_ or, if name is not given, return name of current shape. Shape with _name_ must exist in the TurtleScreen’s shape dictionary. Initially there are the following polygon shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”. To learn about how to deal with shapes see Screen method [`register_shape()`](https://docs.python.org/3/library/turtle.html#turtle.register_shape "turtle.register_shape").
Copy```
>>> turtle.shape()
'classic'
>>> turtle.shape("turtle")
>>> turtle.shape()
'turtle'

```


turtle.resizemode(_rmode =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.resizemode "Link to this definition")


Parameters:

**rmode** – one of the strings “auto”, “user”, “noresize”
Set resizemode to one of the values: “auto”, “user”, “noresize”. If _rmode_ is not given, return current resizemode. Different resizemodes have the following effects:
  * “auto”: adapts the appearance of the turtle corresponding to the value of pensize.
  * “user”: adapts the appearance of the turtle according to the values of stretchfactor and outlinewidth (outline), which are set by [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize").
  * “noresize”: no adaption of the turtle’s appearance takes place.


`resizemode("user")` is called by [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize") when used with arguments.
Copy```
>>> turtle.resizemode()
'noresize'
>>> turtle.resizemode("auto")
>>> turtle.resizemode()
'auto'

```


turtle.shapesize(_stretch_wid =None_, _stretch_len =None_, _outline =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shapesize "Link to this definition")


turtle.turtlesize(_stretch_wid =None_, _stretch_len =None_, _outline =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.turtlesize "Link to this definition")


Parameters:

  * **stretch_wid** – positive number
  * **stretch_len** – positive number
  * **outline** – positive number


Return or set the pen’s attributes x/y-stretchfactors and/or outline. Set resizemode to “user”. If and only if resizemode is set to “user”, the turtle will be displayed stretched according to its stretchfactors: _stretch_wid_ is stretchfactor perpendicular to its orientation, _stretch_len_ is stretchfactor in direction of its orientation, _outline_ determines the width of the shape’s outline.
Copy```
>>> turtle.shapesize()
(1.0, 1.0, 1)
>>> turtle.resizemode("user")
>>> turtle.shapesize(5, 5, 12)
>>> turtle.shapesize()
(5, 5, 12)
>>> turtle.shapesize(outline=8)
>>> turtle.shapesize()
(5, 5, 8)

```


turtle.shearfactor(_shear =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shearfactor "Link to this definition")


Parameters:

**shear** – number (optional)
Set or return the current shearfactor. Shear the turtleshape according to the given shearfactor shear, which is the tangent of the shear angle. Do _not_ change the turtle’s heading (direction of movement). If shear is not given: return the current shearfactor, i. e. the tangent of the shear angle, by which lines parallel to the heading of the turtle are sheared.
Copy```
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.shearfactor(0.5)
>>> turtle.shearfactor()
0.5

```


turtle.tilt(_angle_)[¶](https://docs.python.org/3/library/turtle.html#turtle.tilt "Link to this definition")


Parameters:

**angle** – a number
Rotate the turtleshape by _angle_ from its current tilt-angle, but do _not_ change the turtle’s heading (direction of movement).
Copy```
>>> turtle.reset()
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.tilt(30)
>>> turtle.fd(50)
>>> turtle.tilt(30)
>>> turtle.fd(50)

```


turtle.tiltangle(_angle =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.tiltangle "Link to this definition")


Parameters:

**angle** – a number (optional)
Set or return the current tilt-angle. If angle is given, rotate the turtleshape to point in the direction specified by angle, regardless of its current tilt-angle. Do _not_ change the turtle’s heading (direction of movement). If angle is not given: return the current tilt-angle, i. e. the angle between the orientation of the turtleshape and the heading of the turtle (its direction of movement).
Copy```
>>> turtle.reset()
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.tilt(45)
>>> turtle.tiltangle()
45.0

```


turtle.shapetransform(_t11 =None_, _t12 =None_, _t21 =None_, _t22 =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.shapetransform "Link to this definition")


Parameters:

  * **t11** – a number (optional)
  * **t12** – a number (optional)
  * **t21** – a number (optional)
  * **t12** – a number (optional)


Set or return the current transformation matrix of the turtle shape.
If none of the matrix elements are given, return the transformation matrix as a tuple of 4 elements. Otherwise set the given elements and transform the turtleshape according to the matrix consisting of first row t11, t12 and second row t21, t22. The determinant t11 * t22 - t12 * t21 must not be zero, otherwise an error is raised. Modify stretchfactor, shearfactor and tiltangle according to the given matrix.
Copy```
>>> turtle = Turtle()
>>> turtle.shape("square")
>>> turtle.shapesize(4,2)
>>> turtle.shearfactor(-0.5)
>>> turtle.shapetransform()
(4.0, -1.0, -0.0, 2.0)

```


turtle.get_shapepoly()[¶](https://docs.python.org/3/library/turtle.html#turtle.get_shapepoly "Link to this definition")

Return the current shape polygon as tuple of coordinate pairs. This can be used to define a new shape or components of a compound shape.
Copy```
>>> turtle.shape("square")
>>> turtle.shapetransform(4, -1, 0, 2)
>>> turtle.get_shapepoly()
((50, -20), (30, 20), (-50, 20), (-30, -20))

```

### Using events[¶](https://docs.python.org/3/library/turtle.html#using-events "Link to this heading")

turtle.onclick(_fun_ , _btn =1_, _add =None_)


Parameters:

  * **fun** – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
  * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
  * **add** – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding


Bind _fun_ to mouse-click events on this turtle. If _fun_ is `None`, existing bindings are removed. Example for the anonymous turtle, i.e. the procedural way:
Copy```
>>> def turn(x, y):
...     left(180)
...
>>> onclick(turn)  # Now clicking into the turtle will turn it.
>>> onclick(None)  # event-binding will be removed

```


turtle.onrelease(_fun_ , _btn =1_, _add =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onrelease "Link to this definition")


Parameters:

  * **fun** – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
  * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
  * **add** – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding


Bind _fun_ to mouse-button-release events on this turtle. If _fun_ is `None`, existing bindings are removed.
Copy```
>>> class MyTurtle(Turtle):
...     def glow(self,x,y):
...         self.fillcolor("red")
...     def unglow(self,x,y):
...         self.fillcolor("")
...
>>> turtle = MyTurtle()
>>> turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
>>> turtle.onrelease(turtle.unglow) # releasing turns it to transparent.

```


turtle.ondrag(_fun_ , _btn =1_, _add =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.ondrag "Link to this definition")


Parameters:

  * **fun** – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
  * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
  * **add** – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding


Bind _fun_ to mouse-move events on this turtle. If _fun_ is `None`, existing bindings are removed.
Remark: Every sequence of mouse-move-events on a turtle is preceded by a mouse-click event on that turtle.
Copy```
>>> turtle.ondrag(turtle.goto)

```

Subsequently, clicking and dragging the Turtle will move it across the screen thereby producing handdrawings (if pen is down).
### Special Turtle methods[¶](https://docs.python.org/3/library/turtle.html#special-turtle-methods "Link to this heading")

turtle.poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.poly "Link to this definition")

Record the vertices of a polygon drawn in the `with turtle.poly():` block. The first and last vertices will be connected.
Copy```
>>> with turtle.poly():
...     turtle.forward(100)
...     turtle.right(60)
...     turtle.forward(100)

```

Added in version 3.14.

turtle.begin_poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.begin_poly "Link to this definition")

Start recording the vertices of a polygon. Current turtle position is first vertex of polygon.

turtle.end_poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.end_poly "Link to this definition")

Stop recording the vertices of a polygon. Current turtle position is last vertex of polygon. This will be connected with the first vertex.

turtle.get_poly()[¶](https://docs.python.org/3/library/turtle.html#turtle.get_poly "Link to this definition")

Return the last recorded polygon.
Copy```
>>> turtle.home()
>>> turtle.begin_poly()
>>> turtle.fd(100)
>>> turtle.left(20)
>>> turtle.fd(30)
>>> turtle.left(60)
>>> turtle.fd(50)
>>> turtle.end_poly()
>>> p = turtle.get_poly()
>>> register_shape("myFavouriteShape", p)

```


turtle.clone()[¶](https://docs.python.org/3/library/turtle.html#turtle.clone "Link to this definition")

Create and return a clone of the turtle with same position, heading and turtle properties.
Copy```
>>> mick = Turtle()
>>> joe = mick.clone()

```


turtle.getturtle()[¶](https://docs.python.org/3/library/turtle.html#turtle.getturtle "Link to this definition")


turtle.getpen()[¶](https://docs.python.org/3/library/turtle.html#turtle.getpen "Link to this definition")

Return the Turtle object itself. Only reasonable use: as a function to return the “anonymous turtle”:
Copy```
>>> pet = getturtle()
>>> pet.fd(50)
>>> pet
<turtle.Turtle object at 0x...>

```


turtle.getscreen()[¶](https://docs.python.org/3/library/turtle.html#turtle.getscreen "Link to this definition")

Return the [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen") object the turtle is drawing on. TurtleScreen methods can then be called for that object.
Copy```
>>> ts = turtle.getscreen()
>>> ts
<turtle._Screen object at 0x...>
>>> ts.bgcolor("pink")

```


turtle.setundobuffer(_size_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setundobuffer "Link to this definition")


Parameters:

**size** – an integer or `None`
Set or disable undobuffer. If _size_ is an integer, an empty undobuffer of given size is installed. _size_ gives the maximum number of turtle actions that can be undone by the [`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo "turtle.undo") method/function. If _size_ is `None`, the undobuffer is disabled.
Copy```
>>> turtle.setundobuffer(42)

```


turtle.undobufferentries()[¶](https://docs.python.org/3/library/turtle.html#turtle.undobufferentries "Link to this definition")

Return number of entries in the undobuffer.
Copy```
>>> while undobufferentries():
...     undo()

```

### Compound shapes[¶](https://docs.python.org/3/library/turtle.html#compound-shapes "Link to this heading")
To use compound turtle shapes, which consist of several polygons of different color, you must use the helper class [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape") explicitly as described below:
  1. Create an empty Shape object of type “compound”.
  2. Add as many components to this object as desired, using the [`addcomponent()`](https://docs.python.org/3/library/turtle.html#turtle.Shape.addcomponent "turtle.Shape.addcomponent") method.
For example:
Copy```
>>> s = Shape("compound")
>>> poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
>>> s.addcomponent(poly1, "red", "blue")
>>> poly2 = ((0,0),(10,-5),(-10,-5))
>>> s.addcomponent(poly2, "blue", "red")

```

  3. Now add the Shape to the Screen’s shapelist and use it:
Copy```
>>> register_shape("myshape", s)
>>> shape("myshape")

```



Note
The [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape") class is used internally by the [`register_shape()`](https://docs.python.org/3/library/turtle.html#turtle.register_shape "turtle.register_shape") method in different ways. The application programmer has to deal with the Shape class _only_ when using compound shapes like shown above!
