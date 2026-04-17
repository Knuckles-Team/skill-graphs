[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html "previous chapter")
#### Next topic
[`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Cryptographic+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcrypto.html&pagesource=library%2Fcrypto.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/hashlib.html "hashlib — Secure hashes and message digests") |
  * [previous](https://docs.python.org/3/library/plistlib.html "plistlib — Generate and parse Apple .plist files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Cryptographic Services](https://docs.python.org/3/library/crypto.html)
  * |
  * Theme  Auto Light Dark |


# Cryptographic Services[¶](https://docs.python.org/3/library/crypto.html#cryptographic-services "Link to this heading")
The modules described in this chapter implement various algorithms of a cryptographic nature. They are available at the discretion of the installation. Here’s an overview:
  * [`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
    * [Hash algorithms](https://docs.python.org/3/library/hashlib.html#hash-algorithms)
    * [Usage](https://docs.python.org/3/library/hashlib.html#usage)
    * [Constructors](https://docs.python.org/3/library/hashlib.html#constructors)
    * [Attributes](https://docs.python.org/3/library/hashlib.html#attributes)
    * [Hash Objects](https://docs.python.org/3/library/hashlib.html#hash-objects)
    * [SHAKE variable length digests](https://docs.python.org/3/library/hashlib.html#shake-variable-length-digests)
    * [File hashing](https://docs.python.org/3/library/hashlib.html#file-hashing)
    * [Key derivation](https://docs.python.org/3/library/hashlib.html#key-derivation)
    * [BLAKE2](https://docs.python.org/3/library/hashlib.html#blake2)
      * [Creating hash objects](https://docs.python.org/3/library/hashlib.html#creating-hash-objects)
      * [Constants](https://docs.python.org/3/library/hashlib.html#constants)
      * [Examples](https://docs.python.org/3/library/hashlib.html#examples)
        * [Simple hashing](https://docs.python.org/3/library/hashlib.html#simple-hashing)
        * [Using different digest sizes](https://docs.python.org/3/library/hashlib.html#using-different-digest-sizes)
        * [Keyed hashing](https://docs.python.org/3/library/hashlib.html#keyed-hashing)
        * [Randomized hashing](https://docs.python.org/3/library/hashlib.html#randomized-hashing)
        * [Personalization](https://docs.python.org/3/library/hashlib.html#personalization)
        * [Tree mode](https://docs.python.org/3/library/hashlib.html#tree-mode)
      * [Credits](https://docs.python.org/3/library/hashlib.html#credits)
  * [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html)
  * [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)
    * [Random numbers](https://docs.python.org/3/library/secrets.html#random-numbers)
    * [Generating tokens](https://docs.python.org/3/library/secrets.html#generating-tokens)
      * [How many bytes should tokens use?](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use)
    * [Other functions](https://docs.python.org/3/library/secrets.html#other-functions)
    * [Recipes and best practices](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices)


#### Previous topic
[`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html "previous chapter")
#### Next topic
[`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Cryptographic+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcrypto.html&pagesource=library%2Fcrypto.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/hashlib.html "hashlib — Secure hashes and message digests") |
  * [previous](https://docs.python.org/3/library/plistlib.html "plistlib — Generate and parse Apple .plist files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Cryptographic Services](https://docs.python.org/3/library/crypto.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
