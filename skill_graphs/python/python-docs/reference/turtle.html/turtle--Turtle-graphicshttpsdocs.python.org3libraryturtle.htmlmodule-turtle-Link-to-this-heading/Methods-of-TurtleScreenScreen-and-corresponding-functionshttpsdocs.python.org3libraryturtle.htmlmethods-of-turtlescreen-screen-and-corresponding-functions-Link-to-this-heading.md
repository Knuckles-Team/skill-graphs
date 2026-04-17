## Methods of TurtleScreen/Screen and corresponding functions[¶](https://docs.python.org/3/library/turtle.html#methods-of-turtlescreen-screen-and-corresponding-functions "Link to this heading")
Most of the examples in this section refer to a TurtleScreen instance called `screen`.
### Window control[¶](https://docs.python.org/3/library/turtle.html#window-control "Link to this heading")

turtle.bgcolor()[¶](https://docs.python.org/3/library/turtle.html#turtle.bgcolor "Link to this definition")


turtle.bgcolor(_color_ , _/_)


turtle.bgcolor(_r_ , _g_ , _b_ , _/_)

Return or set the background color of the TurtleScreen.
Four input formats are allowed:

`bgcolor()`

Return the current background color as color specification string or as a tuple (see example). May be used as input to another color/pencolor/fillcolor/bgcolor call.

`bgcolor(colorstring)`

Set the background color to _colorstring_ , which is a Tk color specification string, such as `"red"`, `"yellow"`, or `"#33cc8c"`.

`bgcolor((r, g, b))`

Set the background color to the RGB color represented by the tuple of _r_ , _g_ , and _b_. Each of _r_ , _g_ , and _b_ must be in the range 0..colormode, where colormode is either 1.0 or 255 (see [`colormode()`](https://docs.python.org/3/library/turtle.html#turtle.colormode "turtle.colormode")).

`bgcolor(r, g, b)`

Set the background color to the RGB color represented by _r_ , _g_ , and _b_. Each of _r_ , _g_ , and _b_ must be in the range 0..colormode.
Copy```
>>> screen.bgcolor("orange")
>>> screen.bgcolor()
'orange'
>>> screen.bgcolor("#800080")
>>> screen.bgcolor()
(128.0, 0.0, 128.0)

```


turtle.bgpic(_picname =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.bgpic "Link to this definition")


Parameters:

**picname** – a string, name of an image file (PNG, GIF, PGM, and PPM) or `"nopic"`, or `None`
Set background image or return name of current backgroundimage. If _picname_ is a filename, set the corresponding image as background. If _picname_ is `"nopic"`, delete background image, if present. If _picname_ is `None`, return the filename of the current backgroundimage.
Copy```
>>> screen.bgpic()
'nopic'
>>> screen.bgpic("landscape.gif")
>>> screen.bgpic()
"landscape.gif"

```


turtle.clear()

Note
This TurtleScreen method is available as a global function only under the name `clearscreen`. The global function `clear` is a different one derived from the Turtle method `clear`.

turtle.clearscreen()[¶](https://docs.python.org/3/library/turtle.html#turtle.clearscreen "Link to this definition")

Delete all drawings and all turtles from the TurtleScreen. Reset the now empty TurtleScreen to its initial state: white background, no background image, no event bindings and tracing on.

turtle.reset()

Note
This TurtleScreen method is available as a global function only under the name `resetscreen`. The global function `reset` is another one derived from the Turtle method `reset`.

turtle.resetscreen()[¶](https://docs.python.org/3/library/turtle.html#turtle.resetscreen "Link to this definition")

Reset all Turtles on the Screen to their initial state.

turtle.screensize(_canvwidth =None_, _canvheight =None_, _bg =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.screensize "Link to this definition")


Parameters:

  * **canvwidth** – positive integer, new width of canvas in pixels
  * **canvheight** – positive integer, new height of canvas in pixels
  * **bg** – colorstring or color-tuple, new background color


If no arguments are given, return current (canvaswidth, canvasheight). Else resize the canvas the turtles are drawing on. Do not alter the drawing window. To observe hidden parts of the canvas, use the scrollbars. With this method, one can make visible those parts of a drawing which were outside the canvas before.
Copy```
>>> screen.screensize()
(400, 300)
>>> screen.screensize(2000,1500)
>>> screen.screensize()
(2000, 1500)

```

e.g. to search for an erroneously escaped turtle ;-)

turtle.setworldcoordinates(_llx_ , _lly_ , _urx_ , _ury_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates "Link to this definition")


Parameters:

  * **llx** – a number, x-coordinate of lower left corner of canvas
  * **lly** – a number, y-coordinate of lower left corner of canvas
  * **urx** – a number, x-coordinate of upper right corner of canvas
  * **ury** – a number, y-coordinate of upper right corner of canvas


Set up user-defined coordinate system and switch to mode “world” if necessary. This performs a `screen.reset()`. If mode “world” is already active, all drawings are redrawn according to the new coordinates.
**ATTENTION** : in user-defined coordinate systems angles may appear distorted.
Copy```
>>> screen.reset()
>>> screen.setworldcoordinates(-50,-7.5,50,7.5)
>>> for _ in range(72):
...     left(10)
...
>>> for _ in range(8):
...     left(45); fd(2)   # a regular octagon

```

### Animation control[¶](https://docs.python.org/3/library/turtle.html#animation-control "Link to this heading")

turtle.no_animation()[¶](https://docs.python.org/3/library/turtle.html#turtle.no_animation "Link to this definition")

Temporarily disable turtle animation. The code written inside the `no_animation` block will not be animated; once the code block is exited, the drawing will appear.
Copy```
>>> with screen.no_animation():
...     for dist in range(2, 400, 2):
...         fd(dist)
...         rt(90)

```

Added in version 3.14.

turtle.delay(_delay =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.delay "Link to this definition")


Parameters:

**delay** – positive integer
Set or return the drawing _delay_ in milliseconds. (This is approximately the time interval between two consecutive canvas updates.) The longer the drawing delay, the slower the animation.
Optional argument:
Copy```
>>> screen.delay()
10
>>> screen.delay(5)
>>> screen.delay()
5

```


turtle.tracer(_n =None_, _delay =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.tracer "Link to this definition")


Parameters:

  * **n** – nonnegative integer
  * **delay** – nonnegative integer


Turn turtle animation on/off and set delay for update drawings. If _n_ is given, only each n-th regular screen update is really performed. (Can be used to accelerate the drawing of complex graphics.) When called without arguments, returns the currently stored value of n. Second argument sets delay value (see [`delay()`](https://docs.python.org/3/library/turtle.html#turtle.delay "turtle.delay")).
Copy```
>>> screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

```


turtle.update()[¶](https://docs.python.org/3/library/turtle.html#turtle.update "Link to this definition")

Perform a TurtleScreen update. To be used when tracer is turned off.
See also the RawTurtle/Turtle method [`speed()`](https://docs.python.org/3/library/turtle.html#turtle.speed "turtle.speed").
### Using screen events[¶](https://docs.python.org/3/library/turtle.html#using-screen-events "Link to this heading")

turtle.listen(_xdummy =None_, _ydummy =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.listen "Link to this definition")

Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be able to pass `listen()` to the onclick method.

turtle.onkey(_fun_ , _key_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onkey "Link to this definition")


turtle.onkeyrelease(_fun_ , _key_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onkeyrelease "Link to this definition")


Parameters:

  * **fun** – a function with no arguments or `None`
  * **key** – a string: key (e.g. “a”) or key-symbol (e.g. “space”)


Bind _fun_ to key-release event of key. If _fun_ is `None`, event bindings are removed. Remark: in order to be able to register key-events, TurtleScreen must have the focus. (See method [`listen()`](https://docs.python.org/3/library/turtle.html#turtle.listen "turtle.listen").)
Copy```
>>> def f():
...     fd(50)
...     lt(60)
...
>>> screen.onkey(f, "Up")
>>> screen.listen()

```


turtle.onkeypress(_fun_ , _key =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onkeypress "Link to this definition")


Parameters:

  * **fun** – a function with no arguments or `None`
  * **key** – a string: key (e.g. “a”) or key-symbol (e.g. “space”)


Bind _fun_ to key-press event of key if key is given, or to any key-press-event if no key is given. Remark: in order to be able to register key-events, TurtleScreen must have focus. (See method [`listen()`](https://docs.python.org/3/library/turtle.html#turtle.listen "turtle.listen").)
Copy```
>>> def f():
...     fd(50)
...
>>> screen.onkey(f, "Up")
>>> screen.listen()

```


turtle.onclick(_fun_ , _btn =1_, _add =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onclick "Link to this definition")


turtle.onscreenclick(_fun_ , _btn =1_, _add =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.onscreenclick "Link to this definition")


Parameters:

  * **fun** – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
  * **btn** – number of the mouse-button, defaults to 1 (left mouse button)
  * **add** – `True` or `False` – if `True`, a new binding will be added, otherwise it will replace a former binding


Bind _fun_ to mouse-click events on this screen. If _fun_ is `None`, existing bindings are removed.
Example for a TurtleScreen instance named `screen` and a Turtle instance named `turtle`:
Copy```
>>> screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will
>>>                             # make the turtle move to the clicked point.
>>> screen.onclick(None)        # remove event binding again

```

Note
This TurtleScreen method is available as a global function only under the name `onscreenclick`. The global function `onclick` is another one derived from the Turtle method `onclick`.

turtle.ontimer(_fun_ , _t =0_)[¶](https://docs.python.org/3/library/turtle.html#turtle.ontimer "Link to this definition")


Parameters:

  * **fun** – a function with no arguments
  * **t** – a number >= 0


Install a timer that calls _fun_ after _t_ milliseconds.
Copy```
>>> running = True
>>> def f():
...     if running:
...         fd(50)
...         lt(60)
...         screen.ontimer(f, 250)
>>> f()   ### makes the turtle march around
>>> running = False

```


turtle.mainloop()[¶](https://docs.python.org/3/library/turtle.html#turtle.mainloop "Link to this definition")


turtle.done()[¶](https://docs.python.org/3/library/turtle.html#turtle.done "Link to this definition")

Starts event loop - calling Tkinter’s mainloop function. Must be the last statement in a turtle graphics program. Must _not_ be used if a script is run from within IDLE in -n mode (No subprocess) - for interactive use of turtle graphics.
Copy```
>>> screen.mainloop()

```

### Input methods[¶](https://docs.python.org/3/library/turtle.html#input-methods "Link to this heading")

turtle.textinput(_title_ , _prompt_)[¶](https://docs.python.org/3/library/turtle.html#turtle.textinput "Link to this definition")


Parameters:

  * **title** – string
  * **prompt** – string


Pop up a dialog window for input of a string. Parameter title is the title of the dialog window, prompt is a text mostly describing what information to input. Return the string input. If the dialog is canceled, return `None`.
Copy```
>>> screen.textinput("NIM", "Name of first player:")

```


turtle.numinput(_title_ , _prompt_ , _default =None_, _minval =None_, _maxval =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.numinput "Link to this definition")


Parameters:

  * **title** – string
  * **prompt** – string
  * **default** – number (optional)
  * **minval** – number (optional)
  * **maxval** – number (optional)


Pop up a dialog window for input of a number. title is the title of the dialog window, prompt is a text mostly describing what numerical information to input. default: default value, minval: minimum value for input, maxval: maximum value for input. The number input must be in the range minval .. maxval if these are given. If not, a hint is issued and the dialog remains open for correction. Return the number input. If the dialog is canceled, return `None`.
Copy```
>>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

```

### Settings and special methods[¶](https://docs.python.org/3/library/turtle.html#settings-and-special-methods "Link to this heading")

turtle.mode(_mode =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.mode "Link to this definition")


Parameters:

**mode** – one of the strings “standard”, “logo” or “world”
Set turtle mode (“standard”, “logo” or “world”) and perform reset. If mode is not given, current mode is returned.
Mode “standard” is compatible with old `turtle`. Mode “logo” is compatible with most Logo turtle graphics. Mode “world” uses user-defined “world coordinates”. **Attention** : in this mode angles appear distorted if `x/y` unit-ratio doesn’t equal 1.
Mode | Initial turtle heading | positive angles
---|---|---
“standard” | to the right (east) | counterclockwise
“logo” | upward (north) | clockwise
Copy```
>>> mode("logo")   # resets turtle heading to north
>>> mode()
'logo'

```


turtle.colormode(_cmode =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.colormode "Link to this definition")


Parameters:

**cmode** – one of the values 1.0 or 255
Return the colormode or set it to 1.0 or 255. Subsequently _r_ , _g_ , _b_ values of color triples have to be in the range 0..*cmode*.
Copy```
>>> screen.colormode(1)
>>> turtle.pencolor(240, 160, 80)
Traceback (most recent call last):
     ...
TurtleGraphicsError: bad color sequence: (240, 160, 80)
>>> screen.colormode()
1.0
>>> screen.colormode(255)
>>> screen.colormode()
255
>>> turtle.pencolor(240,160,80)

```


turtle.getcanvas()[¶](https://docs.python.org/3/library/turtle.html#turtle.getcanvas "Link to this definition")

Return the Canvas of this TurtleScreen. Useful for insiders who know what to do with a Tkinter Canvas.
Copy```
>>> cv = screen.getcanvas()
>>> cv
<turtle.ScrolledCanvas object ...>

```


turtle.getshapes()[¶](https://docs.python.org/3/library/turtle.html#turtle.getshapes "Link to this definition")

Return a list of names of all currently available turtle shapes.
Copy```
>>> screen.getshapes()
['arrow', 'blank', 'circle', ..., 'turtle']

```


turtle.register_shape(_name_ , _shape =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.register_shape "Link to this definition")


turtle.addshape(_name_ , _shape =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.addshape "Link to this definition")

There are four different ways to call this function:
  1. _name_ is the name of an image file (PNG, GIF, PGM, and PPM) and _shape_ is `None`: Install the corresponding image shape.
Copy```
>>> screen.register_shape("turtle.gif")

```

Note
Image shapes _do not_ rotate when turning the turtle, so they do not display the heading of the turtle!
  2. _name_ is an arbitrary string and _shape_ is the name of an image file (PNG, GIF, PGM, and PPM): Install the corresponding image shape.
Copy```
>>> screen.register_shape("turtle", "turtle.gif")

```

Note
Image shapes _do not_ rotate when turning the turtle, so they do not display the heading of the turtle!
  3. _name_ is an arbitrary string and _shape_ is a tuple of pairs of coordinates: Install the corresponding polygon shape.
Copy```
>>> screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

```

  4. _name_ is an arbitrary string and _shape_ is a (compound) [`Shape`](https://docs.python.org/3/library/turtle.html#turtle.Shape "turtle.Shape") object: Install the corresponding compound shape.


Add a turtle shape to TurtleScreen’s shapelist. Only thusly registered shapes can be used by issuing the command `shape(shapename)`.
Changed in version 3.14: Added support for PNG, PGM, and PPM image formats. Both a shape name and an image file name can be specified.

turtle.turtles()[¶](https://docs.python.org/3/library/turtle.html#turtle.turtles "Link to this definition")

Return the list of turtles on the screen.
Copy```
>>> for turtle in screen.turtles():
...     turtle.color("red")

```


turtle.window_height()[¶](https://docs.python.org/3/library/turtle.html#turtle.window_height "Link to this definition")

Return the height of the turtle window.
Copy```
>>> screen.window_height()
480

```


turtle.window_width()[¶](https://docs.python.org/3/library/turtle.html#turtle.window_width "Link to this definition")

Return the width of the turtle window.
Copy```
>>> screen.window_width()
640

```

### Methods specific to Screen, not inherited from TurtleScreen[¶](https://docs.python.org/3/library/turtle.html#methods-specific-to-screen-not-inherited-from-turtlescreen "Link to this heading")

turtle.bye()[¶](https://docs.python.org/3/library/turtle.html#turtle.bye "Link to this definition")

Shut the turtlegraphics window.

turtle.exitonclick()[¶](https://docs.python.org/3/library/turtle.html#turtle.exitonclick "Link to this definition")

Bind `bye()` method to mouse clicks on the Screen.
If the value “using_IDLE” in the configuration dictionary is `False` (default value), also enter mainloop. Remark: If IDLE with the `-n` switch (no subprocess) is used, this value should be set to `True` in `turtle.cfg`. In this case IDLE’s own mainloop is active also for the client script.

turtle.save(_filename_ , _overwrite =False_)[¶](https://docs.python.org/3/library/turtle.html#turtle.save "Link to this definition")

Save the current turtle drawing (and turtles) as a PostScript file.

Parameters:

  * **filename** – the path of the saved PostScript file
  * **overwrite** – if `False` and there already exists a file with the given filename, then the function will raise a `FileExistsError`. If it is `True`, the file will be overwritten.


Copy```
>>> screen.save("my_drawing.ps")
>>> screen.save("my_drawing.ps", overwrite=True)

```

Added in version 3.14.

turtle.setup(_width =_CFG['width']_, _height =_CFG['height']_, _startx =_CFG['leftright']_, _starty =_CFG['topbottom']_)[¶](https://docs.python.org/3/library/turtle.html#turtle.setup "Link to this definition")

Set the size and position of the main window. Default values of arguments are stored in the configuration dictionary and can be changed via a `turtle.cfg` file.

Parameters:

  * **width** – if an integer, a size in pixels, if a float, a fraction of the screen; default is 50% of screen
  * **height** – if an integer, the height in pixels, if a float, a fraction of the screen; default is 75% of screen
  * **startx** – if positive, starting position in pixels from the left edge of the screen, if negative from the right edge, if `None`, center window horizontally
  * **starty** – if positive, starting position in pixels from the top edge of the screen, if negative from the bottom edge, if `None`, center window vertically


Copy```
>>> screen.setup (width=200, height=200, startx=0, starty=0)
>>>              # sets window to 200x200 pixels, in upper left of screen
>>> screen.setup(width=.75, height=0.5, startx=None, starty=None)
>>>              # sets window to 75% of screen by 50% of screen and centers

```


turtle.title(_titlestring_)[¶](https://docs.python.org/3/library/turtle.html#turtle.title "Link to this definition")


Parameters:

**titlestring** – a string that is shown in the titlebar of the turtle graphics window
Set title of turtle window to _titlestring_.
Copy```
>>> screen.title("Welcome to the turtle zoo!")

```

## Public classes[¶](https://docs.python.org/3/library/turtle.html#public-classes "Link to this heading")

_class_ turtle.RawTurtle(_canvas_)[¶](https://docs.python.org/3/library/turtle.html#turtle.RawTurtle "Link to this definition")


_class_ turtle.RawPen(_canvas_)[¶](https://docs.python.org/3/library/turtle.html#turtle.RawPen "Link to this definition")


Parameters:

**canvas** – a `tkinter.Canvas`, a [`ScrolledCanvas`](https://docs.python.org/3/library/turtle.html#turtle.ScrolledCanvas "turtle.ScrolledCanvas") or a [`TurtleScreen`](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "turtle.TurtleScreen")
Create a turtle. The turtle has all methods described above as “methods of Turtle/RawTurtle”.

_class_ turtle.Turtle[¶](https://docs.python.org/3/library/turtle.html#turtle.Turtle "Link to this definition")

Subclass of RawTurtle, has the same interface but draws on a default [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen") object created automatically when needed for the first time.

_class_ turtle.TurtleScreen(_cv_)[¶](https://docs.python.org/3/library/turtle.html#turtle.TurtleScreen "Link to this definition")


Parameters:

**cv** – a `tkinter.Canvas`
Provides screen oriented methods like [`bgcolor()`](https://docs.python.org/3/library/turtle.html#turtle.bgcolor "turtle.bgcolor") etc. that are described above.

_class_ turtle.Screen[¶](https://docs.python.org/3/library/turtle.html#turtle.Screen "Link to this definition")

Subclass of TurtleScreen, with [four methods added](https://docs.python.org/3/library/turtle.html#screenspecific).

_class_ turtle.ScrolledCanvas(_master_)[¶](https://docs.python.org/3/library/turtle.html#turtle.ScrolledCanvas "Link to this definition")


Parameters:

**master** – some Tkinter widget to contain the ScrolledCanvas, i.e. a Tkinter-canvas with scrollbars added
Used by class Screen, which thus automatically provides a ScrolledCanvas as playground for the turtles.

_class_ turtle.Shape(_type__ , _data_)[¶](https://docs.python.org/3/library/turtle.html#turtle.Shape "Link to this definition")


Parameters:

**type_** – one of the strings “polygon”, “image”, “compound”
Data structure modeling shapes. The pair `(type_, data)` must follow this specification:
_type__ | _data_
---|---
“polygon” | a polygon-tuple, i.e. a tuple of pairs of coordinates
“image” | an image (in this form only used internally!)
“compound” | `None` (a compound shape has to be constructed using the [`addcomponent()`](https://docs.python.org/3/library/turtle.html#turtle.Shape.addcomponent "turtle.Shape.addcomponent") method)

addcomponent(_poly_ , _fill_ , _outline =None_)[¶](https://docs.python.org/3/library/turtle.html#turtle.Shape.addcomponent "Link to this definition")


Parameters:

  * **poly** – a polygon, i.e. a tuple of pairs of numbers
  * **fill** – a color the _poly_ will be filled with
  * **outline** – a color for the poly’s outline (if given)


Example:
Copy```
>>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
>>> s = Shape("compound")
>>> s.addcomponent(poly, "red", "blue")
>>> # ... add more components and then use register_shape()

```

See [Compound shapes](https://docs.python.org/3/library/turtle.html#compoundshapes).

_class_ turtle.Vec2D(_x_ , _y_)[¶](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "Link to this definition")

A two-dimensional vector class, used as a helper class for implementing turtle graphics. May be useful for turtle graphics programs too. Derived from tuple, so a vector is a tuple!
Provides (for _a_ , _b_ vectors, _k_ number):
  * `a + b` vector addition
  * `a - b` vector subtraction
  * `a * b` inner product
  * `k * a` and `a * k` multiplication with scalar
  * `abs(a)` absolute value of a
  * `a.rotate(angle)` rotation
