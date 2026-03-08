[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html)
    * [Example HTML Parser Application](https://docs.python.org/3/library/html.parser.html#example-html-parser-application)
    * [`HTMLParser` Methods](https://docs.python.org/3/library/html.parser.html#htmlparser-methods)
    * [Examples](https://docs.python.org/3/library/html.parser.html#examples)


#### Previous topic
[`html` — HyperText Markup Language support](https://docs.python.org/3/library/html.html "previous chapter")
#### Next topic
[`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=html.parser+%E2%80%94+Simple+HTML+and+XHTML+parser&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhtml.parser.html&pagesource=library%2Fhtml.parser.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/html.entities.html "html.entities — Definitions of HTML general entities") |
  * [previous](https://docs.python.org/3/library/html.html "html — HyperText Markup Language support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html)
  * |
  * Theme  Auto Light Dark |


#  `html.parser` — Simple HTML and XHTML parser[¶](https://docs.python.org/3/library/html.parser.html#module-html.parser "Link to this heading")
**Source code:**
* * *
This module defines a class [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") which serves as the basis for parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML.

_class_ html.parser.HTMLParser(_*_ , _convert_charrefs =True_, _scripting =False_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "Link to this definition")

Create a parser instance able to parse invalid markup.
If _convert_charrefs_ is true (the default), all character references (except the ones in elements like `script` and `style`) are automatically converted to the corresponding Unicode characters.
If _scripting_ is false (the default), the content of the `noscript` element is parsed normally; if it’s true, it’s returned as is without being parsed.
An `HTMLParser` instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. The user should subclass `HTMLParser` and override its methods to implement the desired behavior.
This parser does not check that end tags match start tags or call the end-tag handler for elements which are closed implicitly by closing an outer element.
Changed in version 3.4: _convert_charrefs_ keyword argument added.
Changed in version 3.5: The default value for argument _convert_charrefs_ is now `True`.
Changed in version 3.14.1: Added the _scripting_ parameter.
## Example HTML Parser Application[¶](https://docs.python.org/3/library/html.parser.html#example-html-parser-application "Link to this heading")
As a basic example, below is a simple HTML parser that uses the [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") class to print out start tags, end tags, and data as they are encountered:
Copy```
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

```

The output will then be:
```
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html

```

##  [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") Methods[¶](https://docs.python.org/3/library/html.parser.html#htmlparser-methods "Link to this heading")
[`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") instances have the following methods:

HTMLParser.feed(_data_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.feed "Link to this definition")

Feed some text to the parser. It is processed insofar as it consists of complete elements; incomplete data is buffered until more data is fed or [`close()`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.close "html.parser.HTMLParser.close") is called. _data_ must be [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").

HTMLParser.close()[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.close "Link to this definition")

Force processing of all buffered data as if it were followed by an end-of-file mark. This method may be redefined by a derived class to define additional processing at the end of the input, but the redefined version should always call the [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") base class method `close()`.

HTMLParser.reset()[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.reset "Link to this definition")

Reset the instance. Loses all unprocessed data. This is called implicitly at instantiation time.

HTMLParser.getpos()[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.getpos "Link to this definition")

Return current line number and offset.

HTMLParser.get_starttag_text()[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.get_starttag_text "Link to this definition")

Return the text of the most recently opened start tag. This should not normally be needed for structured processing, but may be useful in dealing with HTML “as deployed” or for re-generating input with minimal changes (whitespace between attributes can be preserved, etc.).
The following methods are called when data or markup elements are encountered and they are meant to be overridden in a subclass. The base class implementations do nothing (except for [`handle_startendtag()`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_startendtag "html.parser.HTMLParser.handle_startendtag")):

HTMLParser.handle_starttag(_tag_ , _attrs_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_starttag "Link to this definition")

This method is called to handle the start tag of an element (e.g. `<div id="main">`).
The _tag_ argument is the name of the tag converted to lower case. The _attrs_ argument is a list of `(name, value)` pairs containing the attributes found inside the tag’s `<>` brackets. The _name_ will be translated to lower case, and quotes in the _value_ have been removed, and character and entity references have been replaced.
For instance, for the tag `<A HREF="https://www.cwi.nl/">`, this method would be called as `handle_starttag('a', [('href', 'https://www.cwi.nl/')])`.
All entity references from [`html.entities`](https://docs.python.org/3/library/html.entities.html#module-html.entities "html.entities: Definitions of HTML general entities.") are replaced in the attribute values.

HTMLParser.handle_endtag(_tag_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_endtag "Link to this definition")

This method is called to handle the end tag of an element (e.g. `</div>`).
The _tag_ argument is the name of the tag converted to lower case.

HTMLParser.handle_startendtag(_tag_ , _attrs_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_startendtag "Link to this definition")

Similar to [`handle_starttag()`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_starttag "html.parser.HTMLParser.handle_starttag"), but called when the parser encounters an XHTML-style empty tag (`<img ... />`). This method may be overridden by subclasses which require this particular lexical information; the default implementation simply calls `handle_starttag()` and [`handle_endtag()`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_endtag "html.parser.HTMLParser.handle_endtag").

HTMLParser.handle_data(_data_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_data "Link to this definition")

This method is called to process arbitrary data (e.g. text nodes and the content of elements like `script` and `style`).

HTMLParser.handle_entityref(_name_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_entityref "Link to this definition")

This method is called to process a named character reference of the form `&name;` (e.g. `&gt;`), where _name_ is a general entity reference (e.g. `'gt'`). This method is only called if _convert_charrefs_ is false.

HTMLParser.handle_charref(_name_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_charref "Link to this definition")

This method is called to process decimal and hexadecimal numeric character references of the form `&#_NNN_;`and`&#x _NNN_;`. For example, the decimal equivalent for`&gt;` is `&#62;`, whereas the hexadecimal is `&#x3E;`; in this case the method will receive `'62'` or `'x3E'`. This method is only called if _convert_charrefs_ is false.

HTMLParser.handle_comment(_data_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_comment "Link to this definition")

This method is called when a comment is encountered (e.g. `<!--comment-->`).
For example, the comment `<!-- comment -->` will cause this method to be called with the argument `' comment '`.
The content of Internet Explorer conditional comments (condcoms) will also be sent to this method, so, for `<!--[if IE 9]>IE9-specific content<![endif]-->`, this method will receive `'[if IE 9]>IE9-specific content<![endif]'`.

HTMLParser.handle_decl(_decl_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_decl "Link to this definition")

This method is called to handle an HTML doctype declaration (e.g. `<!DOCTYPE html>`).
The _decl_ parameter will be the entire contents of the declaration inside the `<!...>` markup (e.g. `'DOCTYPE html'`).

HTMLParser.handle_pi(_data_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_pi "Link to this definition")

Method called when a processing instruction is encountered. The _data_ parameter will contain the entire processing instruction. For example, for the processing instruction `<?proc color='red'>`, this method would be called as `handle_pi("proc color='red'")`. It is intended to be overridden by a derived class; the base class implementation does nothing.
Note
The [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") class uses the SGML syntactic rules for processing instructions. An XHTML processing instruction using the trailing `'?'` will cause the `'?'` to be included in _data_.

HTMLParser.unknown_decl(_data_)[¶](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.unknown_decl "Link to this definition")

This method is called when an unrecognized declaration is read by the parser.
The _data_ parameter will be the entire contents of the declaration inside the `<![...]>` markup. It is sometimes useful to be overridden by a derived class. The base class implementation does nothing.
## Examples[¶](https://docs.python.org/3/library/html.parser.html#examples "Link to this heading")
The following class implements a parser that will be used to illustrate more examples:
Copy```
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()

```

Parsing a doctype:
Copy```
>>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
...             '"http://www.w3.org/TR/html4/strict.dtd">')
Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"

```

Parsing an element with a few attributes and a title:
Copy```
>>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
Start tag: img
     attr: ('src', 'python-logo.png')
     attr: ('alt', 'The Python logo')
>>>
>>> parser.feed('<h1>Python</h1>')
Start tag: h1
Data     : Python
End tag  : h1

```

The content of elements like `script` and `style` is returned as is, without further parsing:
Copy```
>>> parser.feed('<style type="text/css">#python { color: green }</style>')
Start tag: style
     attr: ('type', 'text/css')
Data     : #python { color: green }
End tag  : style

>>> parser.feed('<script type="text/javascript">'
...             'alert("<strong>hello! &#9786;</strong>");</script>')
Start tag: script
     attr: ('type', 'text/javascript')
Data     : alert("<strong>hello! &#9786;</strong>");
End tag  : script

```

Parsing comments:
Copy```
>>> parser.feed('<!--a comment-->'
...             '<!--[if IE 9]>IE-specific content<![endif]-->')
Comment  : a comment
Comment  : [if IE 9]>IE-specific content<![endif]

```

Parsing named and numeric character references and converting them to the correct char (note: these 3 references are all equivalent to `'>'`):
Copy```
>>> parser = MyHTMLParser()
>>> parser.feed('&gt;&#62;&#x3E;')
Data     : >>>

>>> parser = MyHTMLParser(convert_charrefs=False)
>>> parser.feed('&gt;&#62;&#x3E;')
Named ent: >
Num ent  : >
Num ent  : >

```

Feeding incomplete chunks to [`feed()`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.feed "html.parser.HTMLParser.feed") works, but [`handle_data()`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_data "html.parser.HTMLParser.handle_data") might be called more than once if _convert_charrefs_ is false:
Copy```
>>> for chunk in ['<sp', 'an>buff', 'ered', ' text</s', 'pan>']:
...     parser.feed(chunk)
...
Start tag: span
Data     : buff
Data     : ered
Data     :  text
End tag  : span

```

Parsing invalid HTML (e.g. unquoted attributes) also works:
Copy```
>>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
Start tag: p
Start tag: a
     attr: ('class', 'link')
     attr: ('href', '#main')
Data     : tag soup
End tag  : p
End tag  : a

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html)
    * [Example HTML Parser Application](https://docs.python.org/3/library/html.parser.html#example-html-parser-application)
    * [`HTMLParser` Methods](https://docs.python.org/3/library/html.parser.html#htmlparser-methods)
    * [Examples](https://docs.python.org/3/library/html.parser.html#examples)


#### Previous topic
[`html` — HyperText Markup Language support](https://docs.python.org/3/library/html.html "previous chapter")
#### Next topic
[`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=html.parser+%E2%80%94+Simple+HTML+and+XHTML+parser&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhtml.parser.html&pagesource=library%2Fhtml.parser.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/html.entities.html "html.entities — Definitions of HTML general entities") |
  * [previous](https://docs.python.org/3/library/html.html "html — HyperText Markup Language support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html)
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
