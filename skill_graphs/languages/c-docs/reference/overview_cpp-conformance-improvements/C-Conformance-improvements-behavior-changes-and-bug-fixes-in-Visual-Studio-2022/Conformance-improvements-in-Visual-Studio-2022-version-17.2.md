##  Conformance improvements in Visual Studio 2022 version 17.2
Visual Studio 2022 version 17.2 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#unterminated-bidirectional-character-warnings)
### Unterminated bidirectional character warnings
Visual Studio 2022 version 17.2 adds level 3 warning C5255 for unterminated Unicode bidirectional characters in comments and strings. The warning addresses a security concern described in
Warning C5255 only addresses files that, after conversion, contain Unicode bidirectional characters. This warning applies to UTF-8, UTF-16, and UTF-32 files, so the proper source-encoding must be provided. This change is a source breaking change.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-beforeafter)
#### Example (before/after)
In versions of Visual Studio before Visual Studio 2022 version 17.2, an unterminated bidirectional character didn't produce a warning. Visual Studio 2022 version 17.2 produces warning C5255:
C++
Copy
```
// bidi.cpp
int main() {
    const char *access_level = "user";
    // The following source line contains bidirectional Unicode characters equivalent to:
    //    if ( strcmp(access_level, "user\u202e \u2066// Check if admin \u2069 \u2066") ) {
    // In most editors, it's rendered as:
    //    if ( strcmp(access_level, "user") ) { // Check if admin
    if ( strcmp(access_level, "user‮ ⁦// Check if admin ⁩ ⁦") ) {
        printf("You are an admin.\n");
    }
    return 0;
}

/* build output
bidi.cpp(8): warning C5255: unterminated bidirectional character encountered: 'U+202e'
bidi.cpp(8): warning C5255: unterminated bidirectional character encountered: 'U+2066'
*/

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#from_chars-float-tiebreaker)
###  `from_chars()` `float` tiebreaker
Visual Studio 2022 version 17.2 fixes a bug in `<charconv>` `from_chars()` `float` tiebreaker rules that produced incorrect results. This bug affected decimal strings that were at the exact midpoint of consecutive `float` values, within a narrow range. (The smallest and largest affected values were `32768.009765625` and `131071.98828125`, respectively.) The tiebreaker rule wanted to round to "even," and "even" happened to be "down," but the implementation incorrectly rounded "up" (`double` was unaffected.) For more information and implementation details, see
This change affects runtime behavior in the specified range of cases:
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-3)
#### Example
C++
Copy
```
// from_chars_float.cpp
#include <cassert>
#include <charconv>
#include <cstdio>
#include <string_view>
#include <system_error>
using namespace std;
int main() {
    const double dbl  = 32768.009765625;
    const auto sv     = "32768.009765625"sv;
    float flt         = 0.0f;
    const auto result = from_chars(sv.data(), sv.data() + sv.size(), flt);
    assert(result.ec == errc{});
    printf("from_chars() returned: %.1000g\n", flt);
    printf("This rounded %s.\n", flt < dbl ? "DOWN" : "UP");
}

```

In versions before Visual Studio 2022 version 17.2:
Output
Copy
```
C:\Temp>cl /EHsc /nologo /W4 /std:c++17 from_chars_float.cpp && from_chars_float
from_chars_float.cpp
from_chars() returned: 32768.01171875
This rounded UP.

```

In Visual Studio 2022 version 17.2 and after:
Output
Copy
```
C:\Temp>cl /EHsc /nologo /W4 /std:c++17 from_chars_float.cpp && from_chars_float
from_chars_float.cpp
from_chars() returned: 32768.0078125
This rounded DOWN.

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#zc__stdc__-makes-__stdc__-available-for-c)
###  `/Zc:__STDC__` makes `__STDC__` available for C
The C standard requires that a conforming C implementation defines `__STDC__` as `1`. Due to the behavior of the UCRT, which doesn't expose POSIX functions when `__STDC__` is `1`, it isn't possible to define this macro for C by default without introducing breaking changes to the stable language versions. Visual Studio 2022 version 17.2 and later add a conformance option [`/Zc:__STDC__`](https://learn.microsoft.com/en-us/cpp/build/reference/zc-stdc?view=msvc-170) that defines this macro. There's no negative version of the option. Currently, we plan to use this option by default for future versions of C.
This change is a source breaking change. It applies when C11 or C17 mode is enabled (**`/std:c11`**or**`/std:c17`**) and**`/Zc:__STDC__`**is specified.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-4)
#### Example
C
Copy
```
// test__STDC__.c
#include <io.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
#if __STDC__
    int f = _open("file.txt", _O_RDONLY);
    _close(f);
#else
    int f = open("file.txt", O_RDONLY);
    close(f);
#endif
}

/* Command line behavior

C:\Temp>cl /EHsc /W4 /Zc:__STDC__ test__STDC__.c && test__STDC__

*/

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#warning-for-missing-braces)
### Warning for missing braces
Warning C5246 reports missing braces during aggregate initialization of a subobject. Before Visual Studio 2022 version 17.2, the warning didn't handle the case of an anonymous `struct` or `union`.
This change is a source breaking change. It applies when the off-by-default warning C5246 is enabled.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-5)
#### Example
In Visual Studio 2022 version 17.2 and later, this code now causes an error:
C++
Copy
```
struct S {
   union {
      float f[4];
      double d[2];
   };
};

void f()
{
   S s = { 1.0f, 2.0f, 3.14f, 4.0f };
}

/* Command line behavior
cl /Wall /c t.cpp

t.cpp(10): warning C5246: 'anonymous struct or union': the initialization of a subobject should be wrapped in braces
*/

```

To resolve this issue, add braces to the initializer:
C++
Copy
```
void f()
{
   S s = { { 1.0f, 2.0f, 3.14f, 4.0f } };
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_171)
