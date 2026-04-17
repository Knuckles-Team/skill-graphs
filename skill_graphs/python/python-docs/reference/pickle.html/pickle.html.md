[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
    * [Relationship to other Python modules](https://docs.python.org/3/library/pickle.html#relationship-to-other-python-modules)
      * [Comparison with `marshal`](https://docs.python.org/3/library/pickle.html#comparison-with-marshal)
      * [Comparison with `json`](https://docs.python.org/3/library/pickle.html#comparison-with-json)
    * [Data stream format](https://docs.python.org/3/library/pickle.html#data-stream-format)
    * [Module Interface](https://docs.python.org/3/library/pickle.html#module-interface)
    * [What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)
    * [Pickling Class Instances](https://docs.python.org/3/library/pickle.html#pickling-class-instances)
      * [Persistence of External Objects](https://docs.python.org/3/library/pickle.html#persistence-of-external-objects)
      * [Dispatch Tables](https://docs.python.org/3/library/pickle.html#dispatch-tables)
      * [Handling Stateful Objects](https://docs.python.org/3/library/pickle.html#handling-stateful-objects)
    * [Custom Reduction for Types, Functions, and Other Objects](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects)
    * [Out-of-band Buffers](https://docs.python.org/3/library/pickle.html#out-of-band-buffers)
      * [Provider API](https://docs.python.org/3/library/pickle.html#provider-api)
      * [Consumer API](https://docs.python.org/3/library/pickle.html#consumer-api)
      * [Example](https://docs.python.org/3/library/pickle.html#example)
    * [Restricting Globals](https://docs.python.org/3/library/pickle.html#restricting-globals)
    * [Performance](https://docs.python.org/3/library/pickle.html#performance)
    * [Examples](https://docs.python.org/3/library/pickle.html#examples)
    * [Command-line interface](https://docs.python.org/3/library/pickle.html#command-line-interface)


#### Previous topic
[Data Persistence](https://docs.python.org/3/library/persistence.html "previous chapter")
#### Next topic
[`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pickle+%E2%80%94+Python+object+serialization&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpickle.html&pagesource=library%2Fpickle.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/copyreg.html "copyreg — Register pickle support functions") |
  * [previous](https://docs.python.org/3/library/persistence.html "Data Persistence") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
  * |
  * Theme  Auto Light Dark |
