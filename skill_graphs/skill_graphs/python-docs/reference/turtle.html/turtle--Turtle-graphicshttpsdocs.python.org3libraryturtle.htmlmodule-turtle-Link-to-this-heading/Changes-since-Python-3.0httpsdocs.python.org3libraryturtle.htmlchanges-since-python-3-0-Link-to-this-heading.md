## Changes since Python 3.0[¶](https://docs.python.org/3/library/turtle.html#changes-since-python-3-0 "Link to this heading")
  * The [`Turtle`](https://docs.python.org/3/library/turtle.html#turtle.Turtle "turtle.Turtle") methods [`shearfactor()`](https://docs.python.org/3/library/turtle.html#turtle.shearfactor "turtle.shearfactor"), [`shapetransform()`](https://docs.python.org/3/library/turtle.html#turtle.shapetransform "turtle.shapetransform") and [`get_shapepoly()`](https://docs.python.org/3/library/turtle.html#turtle.get_shapepoly "turtle.get_shapepoly") have been added. Thus the full range of regular linear transforms is now available for transforming turtle shapes. [`tiltangle()`](https://docs.python.org/3/library/turtle.html#turtle.tiltangle "turtle.tiltangle") has been enhanced in functionality: it now can be used to get or set the tilt angle.
  * The [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen") method [`onkeypress()`](https://docs.python.org/3/library/turtle.html#turtle.onkeypress "turtle.onkeypress") has been added as a complement to [`onkey()`](https://docs.python.org/3/library/turtle.html#turtle.onkey "turtle.onkey"). As the latter binds actions to the key release event, an alias: [`onkeyrelease()`](https://docs.python.org/3/library/turtle.html#turtle.onkeyrelease "turtle.onkeyrelease") was also added for it.
  * The method [`Screen.mainloop`](https://docs.python.org/3/library/turtle.html#turtle.mainloop "turtle.mainloop") has been added, so there is no longer a need to use the standalone `mainloop()` function when working with [`Screen`](https://docs.python.org/3/library/turtle.html#turtle.Screen "turtle.Screen") and [`Turtle`](https://docs.python.org/3/library/turtle.html#turtle.Turtle "turtle.Turtle") objects.
  * Two input methods have been added: [`Screen.textinput`](https://docs.python.org/3/library/turtle.html#turtle.textinput "turtle.textinput") and [`Screen.numinput`](https://docs.python.org/3/library/turtle.html#turtle.numinput "turtle.numinput"). These pop up input dialogs and return strings and numbers respectively.


### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html)
    * [Introduction](https://docs.python.org/3/library/turtle.html#introduction)
    * [Get started](https://docs.python.org/3/library/turtle.html#get-started)
    * [Tutorial](https://docs.python.org/3/library/turtle.html#tutorial)
      * [Starting a turtle environment](https://docs.python.org/3/library/turtle.html#starting-a-turtle-environment)
      * [Basic drawing](https://docs.python.org/3/library/turtle.html#basic-drawing)
        * [Pen control](https://docs.python.org/3/library/turtle.html#pen-control)
        * [The turtle’s position](https://docs.python.org/3/library/turtle.html#the-turtle-s-position)
      * [Making algorithmic patterns](https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns)
    * [How to…](https://docs.python.org/3/library/turtle.html#how-to)
      * [Get started as quickly as possible](https://docs.python.org/3/library/turtle.html#get-started-as-quickly-as-possible)
      * [Automatically begin and end filling](https://docs.python.org/3/library/turtle.html#automatically-begin-and-end-filling)
      * [Use the `turtle` module namespace](https://docs.python.org/3/library/turtle.html#use-the-turtle-module-namespace)
      * [Use turtle graphics in a script](https://docs.python.org/3/library/turtle.html#use-turtle-graphics-in-a-script)
      * [Use object-oriented turtle graphics](https://docs.python.org/3/library/turtle.html#use-object-oriented-turtle-graphics)
    * [Turtle graphics reference](https://docs.python.org/3/library/turtle.html#turtle-graphics-reference)
      * [Turtle methods](https://docs.python.org/3/library/turtle.html#turtle-methods)
      * [Methods of TurtleScreen/Screen](https://docs.python.org/3/library/turtle.html#methods-of-turtlescreen-screen)
    * [Methods of RawTurtle/Turtle and corresponding functions](https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions)
      * [Turtle motion](https://docs.python.org/3/library/turtle.html#turtle-motion)
      * [Tell Turtle’s state](https://docs.python.org/3/library/turtle.html#tell-turtle-s-state)
      * [Settings for measurement](https://docs.python.org/3/library/turtle.html#settings-for-measurement)
      * [Pen control](https://docs.python.org/3/library/turtle.html#id1)
        * [Drawing state](https://docs.python.org/3/library/turtle.html#drawing-state)
        * [Color control](https://docs.python.org/3/library/turtle.html#color-control)
        * [Filling](https://docs.python.org/3/library/turtle.html#filling)
        * [More drawing control](https://docs.python.org/3/library/turtle.html#more-drawing-control)
      * [Turtle state](https://docs.python.org/3/library/turtle.html#turtle-state)
        * [Visibility](https://docs.python.org/3/library/turtle.html#visibility)
        * [Appearance](https://docs.python.org/3/library/turtle.html#appearance)
      * [Using events](https://docs.python.org/3/library/turtle.html#using-events)
      * [Special Turtle methods](https://docs.python.org/3/library/turtle.html#special-turtle-methods)
      * [Compound shapes](https://docs.python.org/3/library/turtle.html#compound-shapes)
    * [Methods of TurtleScreen/Screen and corresponding functions](https://docs.python.org/3/library/turtle.html#methods-of-turtlescreen-screen-and-corresponding-functions)
      * [Window control](https://docs.python.org/3/library/turtle.html#window-control)
      * [Animation control](https://docs.python.org/3/library/turtle.html#animation-control)
      * [Using screen events](https://docs.python.org/3/library/turtle.html#using-screen-events)
      * [Input methods](https://docs.python.org/3/library/turtle.html#input-methods)
      * [Settings and special methods](https://docs.python.org/3/library/turtle.html#settings-and-special-methods)
      * [Methods specific to Screen, not inherited from TurtleScreen](https://docs.python.org/3/library/turtle.html#methods-specific-to-screen-not-inherited-from-turtlescreen)
    * [Public classes](https://docs.python.org/3/library/turtle.html#public-classes)
    * [Explanation](https://docs.python.org/3/library/turtle.html#explanation)
    * [Help and configuration](https://docs.python.org/3/library/turtle.html#help-and-configuration)
      * [How to use help](https://docs.python.org/3/library/turtle.html#how-to-use-help)
      * [Translation of docstrings into different languages](https://docs.python.org/3/library/turtle.html#translation-of-docstrings-into-different-languages)
      * [How to configure Screen and Turtles](https://docs.python.org/3/library/turtle.html#how-to-configure-screen-and-turtles)
    * [`turtledemo` — Demo scripts](https://docs.python.org/3/library/turtle.html#module-turtledemo)
    * [Changes since Python 2.6](https://docs.python.org/3/library/turtle.html#changes-since-python-2-6)
    * [Changes since Python 3.0](https://docs.python.org/3/library/turtle.html#changes-since-python-3-0)


#### Previous topic
[IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html "previous chapter")
#### Next topic
[Development Tools](https://docs.python.org/3/library/development.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=turtle+%E2%80%94+Turtle+graphics&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fturtle.html&pagesource=library%2Fturtle.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/development.html "Development Tools") |
  * [previous](https://docs.python.org/3/library/idle.html "IDLE — Python editor and shell") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
