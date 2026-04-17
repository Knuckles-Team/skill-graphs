[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)
    * [GNU **gettext** API](https://docs.python.org/3/library/gettext.html#gnu-gettext-api)
    * [Class-based API](https://docs.python.org/3/library/gettext.html#class-based-api)
      * [The `NullTranslations` class](https://docs.python.org/3/library/gettext.html#the-nulltranslations-class)
      * [The `GNUTranslations` class](https://docs.python.org/3/library/gettext.html#the-gnutranslations-class)
      * [Solaris message catalog support](https://docs.python.org/3/library/gettext.html#solaris-message-catalog-support)
      * [The Catalog constructor](https://docs.python.org/3/library/gettext.html#the-catalog-constructor)
    * [Internationalizing your programs and modules](https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules)
      * [Localizing your module](https://docs.python.org/3/library/gettext.html#localizing-your-module)
      * [Localizing your application](https://docs.python.org/3/library/gettext.html#localizing-your-application)
      * [Changing languages on the fly](https://docs.python.org/3/library/gettext.html#changing-languages-on-the-fly)
      * [Deferred translations](https://docs.python.org/3/library/gettext.html#deferred-translations)
    * [Acknowledgements](https://docs.python.org/3/library/gettext.html#acknowledgements)


#### Previous topic
[Internationalization](https://docs.python.org/3/library/i18n.html "previous chapter")
#### Next topic
[`locale` — Internationalization services](https://docs.python.org/3/library/locale.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=gettext+%E2%80%94+Multilingual+internationalization+services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgettext.html&pagesource=library%2Fgettext.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/locale.html "locale — Internationalization services") |
  * [previous](https://docs.python.org/3/library/i18n.html "Internationalization") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internationalization](https://docs.python.org/3/library/i18n.html) »
  * [`gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)
  * |
  * Theme  Auto Light Dark |


#  `gettext` — Multilingual internationalization services[¶](https://docs.python.org/3/library/gettext.html#module-gettext "Link to this heading")
**Source code:**
* * *
The `gettext` module provides internationalization (I18N) and localization (L10N) services for your Python modules and applications. It supports both the GNU **gettext** message catalog API and a higher level, class-based API that may be more appropriate for Python files. The interface described below allows you to write your module and application messages in one natural language, and provide a catalog of translated messages for running under different natural languages.
Some hints on localizing your Python modules and applications are also given.
## GNU **gettext** API[¶](https://docs.python.org/3/library/gettext.html#gnu-gettext-api "Link to this heading")
The `gettext` module defines the following API, which is very similar to the GNU **gettext** API. If you use this API you will affect the translation of your entire application globally. Often this is what you want if your application is monolingual, with the choice of language dependent on the locale of your user. If you are localizing a Python module, or if your application needs to switch languages on the fly, you probably want to use the class-based API instead.

gettext.bindtextdomain(_domain_ , _localedir =None_)[¶](https://docs.python.org/3/library/gettext.html#gettext.bindtextdomain "Link to this definition")

Bind the _domain_ to the locale directory _localedir_. More concretely, `gettext` will look for binary `.mo` files for the given domain using the path (on Unix): `_localedir_/_language_/LC_MESSAGES/_domain_.mo`, where _language_ is searched for in the environment variables `LANGUAGE`, `LC_ALL`, `LC_MESSAGES`, and `LANG` respectively.
If _localedir_ is omitted or `None`, then the current binding for _domain_ is returned. [[1]](https://docs.python.org/3/library/gettext.html#id3)

gettext.textdomain(_domain =None_)[¶](https://docs.python.org/3/library/gettext.html#gettext.textdomain "Link to this definition")

Change or query the current global domain. If _domain_ is `None`, then the current global domain is returned, otherwise the global domain is set to _domain_ , which is returned.

gettext.gettext(_message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.gettext "Link to this definition")

Return the localized translation of _message_ , based on the current global domain, language, and locale directory. This function is usually aliased as `_()` in the local namespace (see examples below).

gettext.dgettext(_domain_ , _message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.dgettext "Link to this definition")

Like [`gettext()`](https://docs.python.org/3/library/gettext.html#gettext.gettext "gettext.gettext"), but look the message up in the specified _domain_.

gettext.ngettext(_singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.ngettext "Link to this definition")

Like [`gettext()`](https://docs.python.org/3/library/gettext.html#gettext.gettext "gettext.gettext"), but consider plural forms. If a translation is found, apply the plural formula to _n_ , and return the resulting message (some languages have more than two plural forms). If no translation is found, return _singular_ if _n_ is 1; return _plural_ otherwise.
The Plural formula is taken from the catalog header. It is a C or Python expression that has a free variable _n_ ; the expression evaluates to the index of the plural in the catalog. See `.po` files and the formulas for a variety of languages.

gettext.dngettext(_domain_ , _singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.dngettext "Link to this definition")

Like [`ngettext()`](https://docs.python.org/3/library/gettext.html#gettext.ngettext "gettext.ngettext"), but look the message up in the specified _domain_.

gettext.pgettext(_context_ , _message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.pgettext "Link to this definition")


gettext.dpgettext(_domain_ , _context_ , _message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.dpgettext "Link to this definition")


gettext.npgettext(_context_ , _singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.npgettext "Link to this definition")


gettext.dnpgettext(_domain_ , _context_ , _singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.dnpgettext "Link to this definition")

Similar to the corresponding functions without the `p` in the prefix (that is, [`gettext()`](https://docs.python.org/3/library/gettext.html#module-gettext "gettext: Multilingual internationalization services."), [`dgettext()`](https://docs.python.org/3/library/gettext.html#gettext.dgettext "gettext.dgettext"), [`ngettext()`](https://docs.python.org/3/library/gettext.html#gettext.ngettext "gettext.ngettext"), [`dngettext()`](https://docs.python.org/3/library/gettext.html#gettext.dngettext "gettext.dngettext")), but the translation is restricted to the given message _context_.
Added in version 3.8.
Note that GNU **gettext** also defines a `dcgettext()` method, but this was deemed not useful and so it is currently unimplemented.
Here’s an example of typical usage for this API:
Copy```
import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
# ...
print(_('This is a translatable string.'))

```

## Class-based API[¶](https://docs.python.org/3/library/gettext.html#class-based-api "Link to this heading")
The class-based API of the `gettext` module gives you more flexibility and greater convenience than the GNU **gettext** API. It is the recommended way of localizing your Python applications and modules. `gettext` defines a [`GNUTranslations`](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "gettext.GNUTranslations") class which implements the parsing of GNU `.mo` format files, and has methods for returning strings. Instances of this class can also install themselves in the built-in namespace as the function `_()`.

gettext.find(_domain_ , _localedir =None_, _languages =None_, _all =False_)[¶](https://docs.python.org/3/library/gettext.html#gettext.find "Link to this definition")

This function implements the standard `.mo` file search algorithm. It takes a _domain_ , identical to what [`textdomain()`](https://docs.python.org/3/library/gettext.html#gettext.textdomain "gettext.textdomain") takes. Optional _localedir_ is as in [`bindtextdomain()`](https://docs.python.org/3/library/gettext.html#gettext.bindtextdomain "gettext.bindtextdomain"). Optional _languages_ is a list of strings, where each string is a language code.
If _localedir_ is not given, then the default system locale directory is used. [[2]](https://docs.python.org/3/library/gettext.html#id4) If _languages_ is not given, then the following environment variables are searched: `LANGUAGE`, `LC_ALL`, `LC_MESSAGES`, and `LANG`. The first one returning a non-empty value is used for the _languages_ variable. The environment variables should contain a colon separated list of languages, which will be split on the colon to produce the expected list of language code strings.
`find()` then expands and normalizes the languages, and then iterates through them, searching for an existing file built of these components:
`_localedir_/_language_/LC_MESSAGES/_domain_.mo`
The first such file name that exists is returned by `find()`. If no such file is found, then `None` is returned. If _all_ is given, it returns a list of all file names, in the order in which they appear in the languages list or the environment variables.

gettext.translation(_domain_ , _localedir =None_, _languages =None_, _class_ =None_, _fallback =False_)[¶](https://docs.python.org/3/library/gettext.html#gettext.translation "Link to this definition")

Return a `*Translations` instance based on the _domain_ , _localedir_ , and _languages_ , which are first passed to [`find()`](https://docs.python.org/3/library/gettext.html#gettext.find "gettext.find") to get a list of the associated `.mo` file paths. Instances with identical `.mo` file names are cached. The actual class instantiated is _class__ if provided, otherwise [`GNUTranslations`](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "gettext.GNUTranslations"). The class’s constructor must take a single [file object](https://docs.python.org/3/glossary.html#term-file-object) argument.
If multiple files are found, later files are used as fallbacks for earlier ones. To allow setting the fallback, [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy") is used to clone each translation object from the cache; the actual instance data is still shared with the cache.
If no `.mo` file is found, this function raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if _fallback_ is false (which is the default), and returns a [`NullTranslations`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations "gettext.NullTranslations") instance if _fallback_ is true.
Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised, it is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Changed in version 3.11: _codeset_ parameter is removed.

gettext.install(_domain_ , _localedir =None_, _*_ , _names =None_)[¶](https://docs.python.org/3/library/gettext.html#gettext.install "Link to this definition")

This installs the function `_()` in Python’s builtins namespace, based on _domain_ and _localedir_ which are passed to the function [`translation()`](https://docs.python.org/3/library/gettext.html#gettext.translation "gettext.translation").
For the _names_ parameter, please see the description of the translation object’s [`install()`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.install "gettext.NullTranslations.install") method.
As seen below, you usually mark the strings in your application that are candidates for translation, by wrapping them in a call to the `_()` function, like this:
Copy```
print(_('This string will be translated.'))

```

For convenience, you want the `_()` function to be installed in Python’s builtins namespace, so it is easily accessible in all modules of your application.
Changed in version 3.11: _names_ is now a keyword-only parameter.
### The [`NullTranslations`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations "gettext.NullTranslations") class[¶](https://docs.python.org/3/library/gettext.html#the-nulltranslations-class "Link to this heading")
Translation classes are what actually implement the translation of original source file message strings to translated message strings. The base class used by all translation classes is [`NullTranslations`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations "gettext.NullTranslations"); this provides the basic interface you can use to write your own specialized translation classes. Here are the methods of `NullTranslations`:

_class_ gettext.NullTranslations(_fp =None_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations "Link to this definition")

Takes an optional [file object](https://docs.python.org/3/glossary.html#term-file-object) _fp_ , which is ignored by the base class. Initializes “protected” instance variables __info_ and __charset_ which are set by derived classes, as well as __fallback_ , which is set through [`add_fallback()`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.add_fallback "gettext.NullTranslations.add_fallback"). It then calls `self._parse(fp)` if _fp_ is not `None`.

_parse(_fp_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations._parse "Link to this definition")

No-op in the base class, this method takes file object _fp_ , and reads the data from the file, initializing its message catalog. If you have an unsupported message catalog file format, you should override this method to parse your format.

add_fallback(_fallback_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.add_fallback "Link to this definition")

Add _fallback_ as the fallback object for the current translation object. A translation object should consult the fallback if it cannot provide a translation for a given message.

gettext(_message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.gettext "Link to this definition")

If a fallback has been set, forward `gettext()` to the fallback. Otherwise, return _message_. Overridden in derived classes.

ngettext(_singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.ngettext "Link to this definition")

If a fallback has been set, forward `ngettext()` to the fallback. Otherwise, return _singular_ if _n_ is 1; return _plural_ otherwise. Overridden in derived classes.

pgettext(_context_ , _message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.pgettext "Link to this definition")

If a fallback has been set, forward `pgettext()` to the fallback. Otherwise, return the translated message. Overridden in derived classes.
Added in version 3.8.

npgettext(_context_ , _singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.npgettext "Link to this definition")

If a fallback has been set, forward `npgettext()` to the fallback. Otherwise, return the translated message. Overridden in derived classes.
Added in version 3.8.

info()[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.info "Link to this definition")

Return a dictionary containing the metadata found in the message catalog file.

charset()[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.charset "Link to this definition")

Return the encoding of the message catalog file.

install(_names =None_)[¶](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.install "Link to this definition")

This method installs [`gettext()`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.gettext "gettext.NullTranslations.gettext") into the built-in namespace, binding it to `_`.
If the _names_ parameter is given, it must be a sequence containing the names of functions you want to install in the builtins namespace in addition to `_()`. Supported names are `'gettext'`, `'ngettext'`, `'pgettext'`, and `'npgettext'`.
Note that this is only one way, albeit the most convenient way, to make the `_()` function available to your application. Because it affects the entire application globally, and specifically the built-in namespace, localized modules should never install `_()`. Instead, they should use this code to make `_()` available to their module:
Copy```
import gettext
t = gettext.translation('mymodule', ...)
_ = t.gettext

```

This puts `_()` only in the module’s global namespace and so only affects calls within this module.
Changed in version 3.8: Added `'pgettext'` and `'npgettext'`.
### The [`GNUTranslations`](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "gettext.GNUTranslations") class[¶](https://docs.python.org/3/library/gettext.html#the-gnutranslations-class "Link to this heading")
The `gettext` module provides one additional class derived from [`NullTranslations`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations "gettext.NullTranslations"): [`GNUTranslations`](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "gettext.GNUTranslations"). This class overrides `_parse()` to enable reading GNU **gettext** format `.mo` files in both big-endian and little-endian format.
[`GNUTranslations`](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "gettext.GNUTranslations") parses optional metadata out of the translation catalog. It is convention with GNU **gettext** to include metadata as the translation for the empty string. This metadata is in `key: value` pairs, and should contain the `Project-Id-Version` key. If the key `Content-Type` is found, then the `charset` property is used to initialize the “protected” `_charset` instance variable, defaulting to `None` if not found. If the charset encoding is specified, then all message ids and message strings read from the catalog are converted to Unicode using this encoding, else ASCII is assumed.
Since message ids are read as Unicode strings too, all `*gettext()` methods will assume message ids as Unicode strings, not byte strings.
The entire set of key/value pairs are placed into a dictionary and set as the “protected” `_info` instance variable.
If the `.mo` file’s magic number is invalid, the major version number is unexpected, or if other problems occur while reading the file, instantiating a [`GNUTranslations`](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "gettext.GNUTranslations") class can raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

_class_ gettext.GNUTranslations[¶](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations "Link to this definition")

The following methods are overridden from the base class implementation:

gettext(_message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations.gettext "Link to this definition")

Look up the _message_ id in the catalog and return the corresponding message string, as a Unicode string. If there is no entry in the catalog for the _message_ id, and a fallback has been set, the look up is forwarded to the fallback’s [`gettext()`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.gettext "gettext.NullTranslations.gettext") method. Otherwise, the _message_ id is returned.

ngettext(_singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations.ngettext "Link to this definition")

Do a plural-forms lookup of a message id. _singular_ is used as the message id for purposes of lookup in the catalog, while _n_ is used to determine which plural form to use. The returned message string is a Unicode string.
If the message id is not found in the catalog, and a fallback is specified, the request is forwarded to the fallback’s [`ngettext()`](https://docs.python.org/3/library/gettext.html#gettext.NullTranslations.ngettext "gettext.NullTranslations.ngettext") method. Otherwise, when _n_ is 1 _singular_ is returned, and _plural_ is returned in all other cases.
Here is an example:
Copy```
n = len(os.listdir('.'))
cat = GNUTranslations(somefile)
message = cat.ngettext(
    'There is %(num)d file in this directory',
    'There are %(num)d files in this directory',
    n) % {'num': n}

```


pgettext(_context_ , _message_)[¶](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations.pgettext "Link to this definition")

Look up the _context_ and _message_ id in the catalog and return the corresponding message string, as a Unicode string. If there is no entry in the catalog for the _message_ id and _context_ , and a fallback has been set, the look up is forwarded to the fallback’s `pgettext()` method. Otherwise, the _message_ id is returned.
Added in version 3.8.

npgettext(_context_ , _singular_ , _plural_ , _n_)[¶](https://docs.python.org/3/library/gettext.html#gettext.GNUTranslations.npgettext "Link to this definition")

Do a plural-forms lookup of a message id. _singular_ is used as the message id for purposes of lookup in the catalog, while _n_ is used to determine which plural form to use.
If the message id for _context_ is not found in the catalog, and a fallback is specified, the request is forwarded to the fallback’s `npgettext()` method. Otherwise, when _n_ is 1 _singular_ is returned, and _plural_ is returned in all other cases.
Added in version 3.8.
### Solaris message catalog support[¶](https://docs.python.org/3/library/gettext.html#solaris-message-catalog-support "Link to this heading")
The Solaris operating system defines its own binary `.mo` file format, but since no documentation can be found on this format, it is not supported at this time.
### The Catalog constructor[¶](https://docs.python.org/3/library/gettext.html#the-catalog-constructor "Link to this heading")
GNOME uses a version of the `gettext` module by James Henstridge, but this version has a slightly different API. Its documented usage was:
Copy```
import gettext
cat = gettext.Catalog(domain, localedir)
_ = cat.gettext
print(_('hello world'))

```

For compatibility with this older module, the function `Catalog()` is an alias for the [`translation()`](https://docs.python.org/3/library/gettext.html#gettext.translation "gettext.translation") function described above.
One difference between this module and Henstridge’s: his catalog objects supported access through a mapping API, but this appears to be unused and so is not currently supported.
## Internationalizing your programs and modules[¶](https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules "Link to this heading")
Internationalization (I18N) refers to the operation by which a program is made aware of multiple languages. Localization (L10N) refers to the adaptation of your program, once internationalized, to the local language and cultural habits. In order to provide multilingual messages for your Python programs, you need to take the following steps:
  1. prepare your program or module by specially marking translatable strings
  2. run a suite of tools over your marked files to generate raw messages catalogs
  3. create language-specific translations of the message catalogs
  4. use the `gettext` module so that message strings are properly translated


In order to prepare your code for I18N, you need to look at all the strings in your files. Any string that needs to be translated should be marked by wrapping it in `_('...')` — that is, a call to the function [`_`](https://docs.python.org/3/library/gettext.html#module-gettext "gettext: Multilingual internationalization services."). For example:
Copy```
filename = 'mylog.txt'
message = _('writing a log message')
with open(filename, 'w') as fp:
    fp.write(message)

```

In this example, the string `'writing a log message'` is marked as a candidate for translation, while the strings `'mylog.txt'` and `'w'` are not.
There are a few tools to extract the strings meant for translation. The original GNU **gettext** only supported C or C++ source code but its extended version **xgettext** scans code written in a number of languages, including Python, to find strings marked as translatable. `pybabel` script to extract and compile message catalogs. François Pinard’s program called **xpot** does a similar job and is available as part of his
(Python also includes pure-Python versions of these programs, called **pygettext.py** and **msgfmt.py** ; some Python distributions will install them for you. **pygettext.py** is similar to **xgettext** , but only understands Python source code and cannot handle other programming languages such as C or C++. **pygettext.py** supports a command-line interface similar to **xgettext** ; for details on its use, run `pygettext.py --help`. **msgfmt.py** is binary compatible with GNU **msgfmt**. With these two programs, you may not need the GNU **gettext** package to internationalize your Python applications.)
**xgettext** , **pygettext** , and similar tools generate `.po` files that are message catalogs. They are structured human-readable files that contain every marked string in the source code, along with a placeholder for the translated versions of these strings.
Copies of these `.po` files are then handed over to the individual human translators who write translations for every supported natural language. They send back the completed language-specific versions as a `<language-name>.po` file that’s compiled into a machine-readable `.mo` binary catalog file using the **msgfmt** program. The `.mo` files are used by the `gettext` module for the actual translation processing at run-time.
How you use the `gettext` module in your code depends on whether you are internationalizing a single module or your entire application. The next two sections will discuss each case.
### Localizing your module[¶](https://docs.python.org/3/library/gettext.html#localizing-your-module "Link to this heading")
If you are localizing your module, you must take care not to make global changes, e.g. to the built-in namespace. You should not use the GNU **gettext** API but instead the class-based API.
Let’s say your module is called “spam” and the module’s various natural language translation `.mo` files reside in `/usr/share/locale` in GNU **gettext** format. Here’s what you would put at the top of your module:
Copy```
import gettext
t = gettext.translation('spam', '/usr/share/locale')
_ = t.gettext

```

### Localizing your application[¶](https://docs.python.org/3/library/gettext.html#localizing-your-application "Link to this heading")
If you are localizing your application, you can install the `_()` function globally into the built-in namespace, usually in the main driver file of your application. This will let all your application-specific files just use `_('...')` without having to explicitly install it in each file.
In the simple case then, you need only add the following bit of code to the main driver file of your application:
Copy```
import gettext
gettext.install('myapplication')

```

If you need to set the locale directory, you can pass it into the [`install()`](https://docs.python.org/3/library/gettext.html#gettext.install "gettext.install") function:
Copy```
import gettext
gettext.install('myapplication', '/usr/share/locale')

```

### Changing languages on the fly[¶](https://docs.python.org/3/library/gettext.html#changing-languages-on-the-fly "Link to this heading")
If your program needs to support many languages at the same time, you may want to create multiple translation instances and then switch between them explicitly, like so:
Copy```
import gettext

lang1 = gettext.translation('myapplication', languages=['en'])
lang2 = gettext.translation('myapplication', languages=['fr'])
lang3 = gettext.translation('myapplication', languages=['de'])

# start by using language1
lang1.install()

# ... time goes by, user selects language 2
lang2.install()

# ... more time goes by, user selects language 3
lang3.install()

```

### Deferred translations[¶](https://docs.python.org/3/library/gettext.html#deferred-translations "Link to this heading")
In most coding situations, strings are translated where they are coded. Occasionally however, you need to mark strings for translation, but defer actual translation until later. A classic example is:
Copy```
animals = ['mollusk',
           'albatross',
           'rat',
           'penguin',
           'python', ]
# ...
for a in animals:
    print(a)

```

Here, you want to mark the strings in the `animals` list as being translatable, but you don’t actually want to translate them until they are printed.
Here is one way you can handle this situation:
Copy```
def _(message): return message

animals = [_('mollusk'),
           _('albatross'),
           _('rat'),
           _('penguin'),
           _('python'), ]

del _

# ...
for a in animals:
    print(_(a))

```

This works because the dummy definition of `_()` simply returns the string unchanged. And this dummy definition will temporarily override any definition of `_()` in the built-in namespace (until the [`del`](https://docs.python.org/3/reference/simple_stmts.html#del) command). Take care, though if you have a previous definition of `_()` in the local namespace.
Note that the second use of `_()` will not identify “a” as being translatable to the **gettext** program, because the parameter is not a string literal.
Another way to handle this is with the following example:
Copy```
def N_(message): return message

animals = [N_('mollusk'),
           N_('albatross'),
           N_('rat'),
           N_('penguin'),
           N_('python'), ]

# ...
for a in animals:
    print(_(a))

```

In this case, you are marking translatable strings with the function `N_()`, which won’t conflict with any definition of `_()`. However, you will need to teach your message extraction program to look for translatable strings marked with `N_()`. **xgettext** , **pygettext** , `pybabel extract`, and **xpot** all support this through the use of the `-k` command-line switch. The choice of `N_()` here is totally arbitrary; it could have just as easily been `MarkThisStringForTranslation()`.
## Acknowledgements[¶](https://docs.python.org/3/library/gettext.html#acknowledgements "Link to this heading")
The following people contributed code, feedback, design suggestions, previous implementations, and valuable experience to the creation of this module:
  * Peter Funk
  * James Henstridge
  * Juan David Ibáñez Palomar
  * Marc-André Lemburg
  * Martin von Löwis
  * François Pinard
  * Barry Warsaw
  * Gustavo Niemeyer


Footnotes
[[1](https://docs.python.org/3/library/gettext.html#id1)]
The default locale directory is system dependent; for example, on Red Hat Linux it is `/usr/share/locale`, but on Solaris it is `/usr/lib/locale`. The `gettext` module does not try to support these system dependent defaults; instead its default is `_sys.base_prefix_/share/locale`(see[`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")). For this reason, it is always best to call [`bindtextdomain()`](https://docs.python.org/3/library/gettext.html#gettext.bindtextdomain "gettext.bindtextdomain") with an explicit absolute path at the start of your application.
[[2](https://docs.python.org/3/library/gettext.html#id2)]
See the footnote for [`bindtextdomain()`](https://docs.python.org/3/library/gettext.html#gettext.bindtextdomain "gettext.bindtextdomain") above.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)
    * [GNU **gettext** API](https://docs.python.org/3/library/gettext.html#gnu-gettext-api)
    * [Class-based API](https://docs.python.org/3/library/gettext.html#class-based-api)
      * [The `NullTranslations` class](https://docs.python.org/3/library/gettext.html#the-nulltranslations-class)
      * [The `GNUTranslations` class](https://docs.python.org/3/library/gettext.html#the-gnutranslations-class)
      * [Solaris message catalog support](https://docs.python.org/3/library/gettext.html#solaris-message-catalog-support)
      * [The Catalog constructor](https://docs.python.org/3/library/gettext.html#the-catalog-constructor)
    * [Internationalizing your programs and modules](https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules)
      * [Localizing your module](https://docs.python.org/3/library/gettext.html#localizing-your-module)
      * [Localizing your application](https://docs.python.org/3/library/gettext.html#localizing-your-application)
      * [Changing languages on the fly](https://docs.python.org/3/library/gettext.html#changing-languages-on-the-fly)
      * [Deferred translations](https://docs.python.org/3/library/gettext.html#deferred-translations)
    * [Acknowledgements](https://docs.python.org/3/library/gettext.html#acknowledgements)


#### Previous topic
[Internationalization](https://docs.python.org/3/library/i18n.html "previous chapter")
#### Next topic
[`locale` — Internationalization services](https://docs.python.org/3/library/locale.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=gettext+%E2%80%94+Multilingual+internationalization+services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgettext.html&pagesource=library%2Fgettext.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/locale.html "locale — Internationalization services") |
  * [previous](https://docs.python.org/3/library/i18n.html "Internationalization") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internationalization](https://docs.python.org/3/library/i18n.html) »
  * [`gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)
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
