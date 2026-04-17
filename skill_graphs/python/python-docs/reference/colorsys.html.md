[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html "previous chapter")
#### Next topic
[Internationalization](https://docs.python.org/3/library/i18n.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=colorsys+%E2%80%94+Conversions+between+color+systems&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcolorsys.html&pagesource=library%2Fcolorsys.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/i18n.html "Internationalization") |
  * [previous](https://docs.python.org/3/library/wave.html "wave — Read and write WAV files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Multimedia Services](https://docs.python.org/3/library/mm.html) »
  * [`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html)
  * |
  * Theme  Auto Light Dark |


#  `colorsys` — Conversions between color systems[¶](https://docs.python.org/3/library/colorsys.html#module-colorsys "Link to this heading")
**Source code:**
* * *
The `colorsys` module defines bidirectional conversions of color values between colors expressed in the RGB (Red Green Blue) color space used in computer monitors and three other coordinate systems: YIQ, HLS (Hue Lightness Saturation) and HSV (Hue Saturation Value). Coordinates in all of these color spaces are floating-point values. In the YIQ space, the Y coordinate is between 0 and 1, but the I and Q coordinates can be positive or negative. In all other spaces, the coordinates are all between 0 and 1.
See also
More information about color spaces can be found at
The `colorsys` module defines the following functions:

colorsys.rgb_to_yiq(_r_ , _g_ , _b_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.rgb_to_yiq "Link to this definition")

Convert the color from RGB coordinates to YIQ coordinates.

colorsys.yiq_to_rgb(_y_ , _i_ , _q_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.yiq_to_rgb "Link to this definition")

Convert the color from YIQ coordinates to RGB coordinates.

colorsys.rgb_to_hls(_r_ , _g_ , _b_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.rgb_to_hls "Link to this definition")

Convert the color from RGB coordinates to HLS coordinates.

colorsys.hls_to_rgb(_h_ , _l_ , _s_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.hls_to_rgb "Link to this definition")

Convert the color from HLS coordinates to RGB coordinates.

colorsys.rgb_to_hsv(_r_ , _g_ , _b_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.rgb_to_hsv "Link to this definition")

Convert the color from RGB coordinates to HSV coordinates.

colorsys.hsv_to_rgb(_h_ , _s_ , _v_)[¶](https://docs.python.org/3/library/colorsys.html#colorsys.hsv_to_rgb "Link to this definition")

Convert the color from HSV coordinates to RGB coordinates.
Example:
Copy```
>>> import colorsys
>>> colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
(0.5, 0.5, 0.4)
>>> colorsys.hsv_to_rgb(0.5, 0.5, 0.4)
(0.2, 0.4, 0.4)

```

#### Previous topic
[`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html "previous chapter")
#### Next topic
[Internationalization](https://docs.python.org/3/library/i18n.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=colorsys+%E2%80%94+Conversions+between+color+systems&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcolorsys.html&pagesource=library%2Fcolorsys.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/i18n.html "Internationalization") |
  * [previous](https://docs.python.org/3/library/wave.html "wave — Read and write WAV files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Multimedia Services](https://docs.python.org/3/library/mm.html) »
  * [`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
