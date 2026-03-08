## String constants[¶](https://docs.python.org/3/library/string.html#string-constants "Link to this heading")
The constants defined in this module are:

string.ascii_letters[¶](https://docs.python.org/3/library/string.html#string.ascii_letters "Link to this definition")

The concatenation of the [`ascii_lowercase`](https://docs.python.org/3/library/string.html#string.ascii_lowercase "string.ascii_lowercase") and [`ascii_uppercase`](https://docs.python.org/3/library/string.html#string.ascii_uppercase "string.ascii_uppercase") constants described below. This value is not locale-dependent.

string.ascii_lowercase[¶](https://docs.python.org/3/library/string.html#string.ascii_lowercase "Link to this definition")

The lowercase letters `'abcdefghijklmnopqrstuvwxyz'`. This value is not locale-dependent and will not change.

string.ascii_uppercase[¶](https://docs.python.org/3/library/string.html#string.ascii_uppercase "Link to this definition")

The uppercase letters `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. This value is not locale-dependent and will not change.

string.digits[¶](https://docs.python.org/3/library/string.html#string.digits "Link to this definition")

The string `'0123456789'`.

string.hexdigits[¶](https://docs.python.org/3/library/string.html#string.hexdigits "Link to this definition")

The string `'0123456789abcdefABCDEF'`.

string.octdigits[¶](https://docs.python.org/3/library/string.html#string.octdigits "Link to this definition")

The string `'01234567'`.

string.punctuation[¶](https://docs.python.org/3/library/string.html#string.punctuation "Link to this definition")

String of ASCII characters which are considered punctuation characters in the `C` locale: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`.

string.printable[¶](https://docs.python.org/3/library/string.html#string.printable "Link to this definition")

String of ASCII characters which are considered printable by Python. This is a combination of [`digits`](https://docs.python.org/3/library/string.html#string.digits "string.digits"), [`ascii_letters`](https://docs.python.org/3/library/string.html#string.ascii_letters "string.ascii_letters"), [`punctuation`](https://docs.python.org/3/library/string.html#string.punctuation "string.punctuation"), and [`whitespace`](https://docs.python.org/3/library/string.html#string.whitespace "string.whitespace").
Note
By design, [`string.printable.isprintable()`](https://docs.python.org/3/library/stdtypes.html#str.isprintable "str.isprintable") returns [`False`](https://docs.python.org/3/library/constants.html#False "False"). In particular, `string.printable` is not printable in the POSIX sense (see

string.whitespace[¶](https://docs.python.org/3/library/string.html#string.whitespace "Link to this definition")

A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
