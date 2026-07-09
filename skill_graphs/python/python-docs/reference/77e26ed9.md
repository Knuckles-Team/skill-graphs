##  `turtledemo` — Demo scripts[¶](https://docs.python.org/3/library/turtle.html#module-turtledemo "Link to this heading")
The `turtledemo` package includes a set of demo scripts. These scripts can be run and viewed using the supplied demo viewer as follows:
Copy```
python -m turtledemo

```

Alternatively, you can run the demo scripts individually. For example,
Copy```
python -m turtledemo.bytedesign

```

The `turtledemo` package directory contains:
  * A demo viewer `__main__.py` which can be used to view the sourcecode of the scripts and run them at the same time.
  * Multiple scripts demonstrating different features of the `turtle` module. Examples can be accessed via the Examples menu. They can also be run standalone.
  * A `turtle.cfg` file which serves as an example of how to write and use such files.


The demo scripts are:
Name | Description | Features
---|---|---
`bytedesign` | complex classical turtle graphics pattern | [`tracer()`](https://docs.python.org/3/library/turtle.html#turtle.tracer "turtle.tracer"), [`delay()`](https://docs.python.org/3/library/turtle.html#turtle.delay "turtle.delay"), [`update()`](https://docs.python.org/3/library/turtle.html#turtle.update "turtle.update")
`chaos` | graphs Verhulst dynamics, shows that computer’s computations can generate results sometimes against the common sense expectations | world coordinates
`clock` | analog clock showing time of your computer | turtles as clock’s hands, [`ontimer()`](https://docs.python.org/3/library/turtle.html#turtle.ontimer "turtle.ontimer")
`colormixer` | experiment with r, g, b | [`ondrag()`](https://docs.python.org/3/library/turtle.html#turtle.ondrag "turtle.ondrag")
`forest` | 3 breadth-first trees | randomization
`fractalcurves` | Hilbert & Koch curves | recursion
`lindenmayer` | ethnomathematics (indian kolams) | L-System
`minimal_hanoi` | Towers of Hanoi | Rectangular Turtles as Hanoi discs ([`shape()`](https://docs.python.org/3/library/turtle.html#turtle.shape "turtle.shape"), [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize"))
`nim` | play the classical nim game with three heaps of sticks against the computer. | turtles as nimsticks, event driven (mouse, keyboard)
`paint` | super minimalistic drawing program | [`onclick()`](https://docs.python.org/3/library/turtle.html#turtle.onclick "turtle.onclick")
`peace` | elementary | turtle: appearance and animation
`penrose` | aperiodic tiling with kites and darts | [`stamp()`](https://docs.python.org/3/library/turtle.html#turtle.stamp "turtle.stamp")
`planet_and_moon` | simulation of gravitational system | compound shapes, [`Vec2D`](https://docs.python.org/3/library/turtle.html#turtle.Vec2D "turtle.Vec2D")
`rosette` | a pattern from the wikipedia article on turtle graphics | [`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone "turtle.clone"), [`undo()`](https://docs.python.org/3/library/turtle.html#turtle.undo "turtle.undo")
`round_dance` | dancing turtles rotating pairwise in opposite direction | compound shapes, [`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone "turtle.clone") [`shapesize()`](https://docs.python.org/3/library/turtle.html#turtle.shapesize "turtle.shapesize"), [`tilt()`](https://docs.python.org/3/library/turtle.html#turtle.tilt "turtle.tilt"), [`get_shapepoly()`](https://docs.python.org/3/library/turtle.html#turtle.get_shapepoly "turtle.get_shapepoly"), [`update()`](https://docs.python.org/3/library/turtle.html#turtle.update "turtle.update")
`sorting_animate` | visual demonstration of different sorting methods | simple alignment, randomization
`tree` | a (graphical) breadth first tree (using generators) | [`clone()`](https://docs.python.org/3/library/turtle.html#turtle.clone "turtle.clone")
`two_canvases` | simple design | turtles on two canvases
`yinyang` | another elementary example | [`circle()`](https://docs.python.org/3/library/turtle.html#turtle.circle "turtle.circle")
Have fun!
