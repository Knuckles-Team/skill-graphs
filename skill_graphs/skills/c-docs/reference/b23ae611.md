##  Conformance improvements in Visual Studio 2022 version 17.9
Visual Studio 2022 version 17.9 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
For a broader summary of changes made to the Standard Template Library, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#application-of-_alignas-on-a-structured-type-in-c-1)
### Application of `_Alignas` on a structured type in C
In versions of Visual C++ before Visual Studio 2022 version 17.9, when `_Alignas` appeared next to a structure type in a declaration, it wasn't applied correctly according to the ISO-C Standard. For example:
C
Copy
```
// compile with /std:c17
#include <stddef.h>
struct Outer
{
    _Alignas(32) struct Inner { int i; } member1;
    struct Inner member2;
};
static_assert(offsetof(struct Outer, member2)==4, "incorrect alignment");

```

According to the ISO-C Standard, this code should compile without the `static_assert` emitting a diagnostic. The `_Alignas` directive applies only to the member variable `member1`. It must not change the alignment of `struct Inner`. However, before release 17.9.1 of Visual Studio, the diagnostic "incorrect alignment" was emitted. The compiler aligned `member2` to a 32 byte offset within `struct Outer`.
Fixing this is a binary breaking change, so when this change in behavior is applied a warning is emitted. For the preceding code, Warning C5274, "`_Alignas` no longer applies to the type 'Inner' (only applies to declared data objects)" is now emitted at warning level 1.
In previous versions of Visual Studio, `_Alignas` was ignored when it appeared next to an anonymous type declaration. For example:
C
Copy
```
// compile with /std:c17
#include <stddef.h>
struct S {
    _Alignas(32) struct { int anon_member; };
    int k;
};
static_assert(offsetof(struct S, k)==4, "incorrect offsetof");
static_assert(sizeof(struct S)==32, "incorrect size");

```

Previously, both `static_assert` statements failed when compiling this code. The code now compiles, but with the following level 1 warnings:
C
Copy
```
warning C5274: behavior change: _Alignas no longer applies to the type '<unnamed-tag>' (only applies to declared data objects)
warning C5273: behavior change: _Alignas on anonymous type no longer ignored (promoted members will align)

```

If you want the earlier behavior, replace `_Alignas(N)` with `__declspec(align(N))`. Unlike `_Alignas`, `declspec(align)` can be applied to a type.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#__va_opt__-is-enabled-as-an-extension-under-zcpreprocessor)
###  `__VA_OPT__` is enabled as an extension under `/Zc:preprocessor`
`__VA_OPT__` was added to C++20 and C23. Previous to its addition, there wasn't a standard way to elide a comma in a variadic macro. To provide better backward compatibility, `__VA_OPT__` is enabled under the token based preprocessor `/Zc:preprocessor` across all language versions.
For example, this now compiles without error:
C++
Copy
```
#define LOG_WRAPPER(message, ...) WRITE_LOG(__LINE__, message __VA_OPT__(, __VA_ARGS__))

// Failed to build under /std:c11, now succeeds.
LOG_WRAPPER("Log message");
LOG_WRAPPER("Log message with %s", "argument")

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#c23-language)
### C23 language
For C23, the following are available when using the `/std:clatest` compiler switch:
[`typeof`](https://learn.microsoft.com/en-us/cpp/c-language/typeof-c?view=msvc-170)
[`typeof_unqual`](https://learn.microsoft.com/en-us/cpp/c-language/typeof-unqual-c?view=msvc-170)
The following are available for all C language versions:
[`__typeof__`](https://learn.microsoft.com/en-us/cpp/c-language/typeof-c?view=msvc-170)
[`__typeof_unqual__`](https://learn.microsoft.com/en-us/cpp/c-language/typeof-unqual-c?view=msvc-170)
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#c-standard-library)
### C++ Standard Library
**C++23 features**
  * `formattable`, `range_format`, `format_kind`, and `set_debug_format()` as part of
  * `<mdspan>` per
  * `format()` pointers per


[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_178)
