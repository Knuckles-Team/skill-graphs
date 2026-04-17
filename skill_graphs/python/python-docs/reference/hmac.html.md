[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html "previous chapter")
#### Next topic
[`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=hmac+%E2%80%94+Keyed-Hashing+for+Message+Authentication&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhmac.html&pagesource=library%2Fhmac.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/secrets.html "secrets — Generate secure random numbers for managing secrets") |
  * [previous](https://docs.python.org/3/library/hashlib.html "hashlib — Secure hashes and message digests") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Cryptographic Services](https://docs.python.org/3/library/crypto.html) »
  * [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html)
  * |
  * Theme  Auto Light Dark |


#  `hmac` — Keyed-Hashing for Message Authentication[¶](https://docs.python.org/3/library/hmac.html#module-hmac "Link to this heading")
**Source code:**
* * *
This module implements the HMAC algorithm as described by _fixed_ digest size. In particular, extendable output functions such as SHAKE-128 or SHAKE-256 cannot be used with HMAC.

hmac.new(_key_ , _msg=None_ , _digestmod_)[¶](https://docs.python.org/3/library/hmac.html#hmac.new "Link to this definition")

Return a new hmac object. _key_ is a bytes or bytearray object giving the secret key. If _msg_ is present, the method call `update(msg)` is made. _digestmod_ is the digest name, digest constructor or module for the HMAC object to use. It may be any name suitable to [`hashlib.new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new"). Despite its argument position, it is required.
Changed in version 3.4: Parameter _key_ can be a bytes or bytearray object. Parameter _msg_ can be of any type supported by [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms."). Parameter _digestmod_ can be the name of a hash algorithm.
Changed in version 3.8: The _digestmod_ argument is now required. Pass it as a keyword argument to avoid awkwardness when you do not have an initial _msg_.

hmac.digest(_key_ , _msg_ , _digest_)[¶](https://docs.python.org/3/library/hmac.html#hmac.digest "Link to this definition")

Return digest of _msg_ for given secret _key_ and _digest_. The function is equivalent to `HMAC(key, msg, digest).digest()`, but uses an optimized C or inline implementation, which is faster for messages that fit into memory. The parameters _key_ , _msg_ , and _digest_ have the same meaning as in [`new()`](https://docs.python.org/3/library/hmac.html#hmac.new "hmac.new").
CPython implementation detail, the optimized C implementation is only used when _digest_ is a string and name of a digest algorithm, which is supported by OpenSSL.
Added in version 3.7.

_class_ hmac.HMAC[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC "Link to this definition")

An HMAC object has the following methods:

HMAC.update(_msg_)[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.update "Link to this definition")

Update the hmac object with _msg_. Repeated calls are equivalent to a single call with the concatenation of all the arguments: `m.update(a); m.update(b)` is equivalent to `m.update(a + b)`.
Changed in version 3.4: Parameter _msg_ can be of any type supported by [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.").

HMAC.digest()[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.digest "Link to this definition")

Return the digest of the bytes passed to the [`update()`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.update "hmac.HMAC.update") method so far. This bytes object will be the same length as the _digest_size_ of the digest given to the constructor. It may contain non-ASCII bytes, including NUL bytes.
Warning
When comparing the output of `digest()` to an externally supplied digest during a verification routine, it is recommended to use the [`compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "hmac.compare_digest") function instead of the `==` operator to reduce the vulnerability to timing attacks.

HMAC.hexdigest()[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.hexdigest "Link to this definition")

Like [`digest()`](https://docs.python.org/3/library/hmac.html#hmac.digest "hmac.digest") except the digest is returned as a string twice the length containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.
Warning
When comparing the output of `hexdigest()` to an externally supplied digest during a verification routine, it is recommended to use the [`compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "hmac.compare_digest") function instead of the `==` operator to reduce the vulnerability to timing attacks.

HMAC.copy()[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.copy "Link to this definition")

Return a copy (“clone”) of the hmac object. This can be used to efficiently compute the digests of strings that share a common initial substring.
A hash object has the following attributes:

HMAC.digest_size[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.digest_size "Link to this definition")

The size of the resulting HMAC digest in bytes.

HMAC.block_size[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.block_size "Link to this definition")

The internal block size of the hash algorithm in bytes.
Added in version 3.4.

HMAC.name[¶](https://docs.python.org/3/library/hmac.html#hmac.HMAC.name "Link to this definition")

The canonical name of this HMAC, always lowercase, e.g. `hmac-md5`.
Added in version 3.4.
Changed in version 3.10: Removed the undocumented attributes `HMAC.digest_cons`, `HMAC.inner`, and `HMAC.outer`.
This module also provides the following helper function:

hmac.compare_digest(_a_ , _b_)[¶](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "Link to this definition")

Return `a == b`. This function uses an approach designed to prevent timing analysis by avoiding content-based short circuiting behaviour, making it appropriate for cryptography. _a_ and _b_ must both be of the same type: either [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") (ASCII only, as e.g. returned by [`HMAC.hexdigest()`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.hexdigest "hmac.HMAC.hexdigest")), or a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).
Note
If _a_ and _b_ are of different lengths, or if an error occurs, a timing attack could theoretically reveal information about the types and lengths of _a_ and _b_ —but not their values.
Added in version 3.3.
Changed in version 3.10: The function uses OpenSSL’s `CRYPTO_memcmp()` internally when available.
See also

Module [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")

The Python module providing secure hash functions.
#### Previous topic
[`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html "previous chapter")
#### Next topic
[`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=hmac+%E2%80%94+Keyed-Hashing+for+Message+Authentication&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhmac.html&pagesource=library%2Fhmac.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/secrets.html "secrets — Generate secure random numbers for managing secrets") |
  * [previous](https://docs.python.org/3/library/hashlib.html "hashlib — Secure hashes and message digests") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Cryptographic Services](https://docs.python.org/3/library/crypto.html) »
  * [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
