##  Conformance improvements in Visual Studio 2022 version 17.10
Visual Studio 2022 version 17.10 includes the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
For an in-depth summary of changes made to the Standard Template Library, including conformance changes, bug fixes, and performance improvements, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#conversion-operator-specialization-with-explicitly-specified-return-type)
### Conversion operator specialization with explicitly specified return type
The compiler used to specialize conversion operators incorrectly in some cases, which could lead to a mismatched return type. These invalid specializations no longer happen. This is a source code breaking change.
C++
Copy
```
// Example 1
struct S
{
    template<typename T> operator const T*();
};

void test()
{
    S{}.operator int*(); // this is invalid now
    S{}.operator const int*(); // this is valid
}

```

C++
Copy
```
// Example 2
// In some cases, the overload resolution result may change
struct S
{
    template <typename T> operator T*(); // overload 1
    template <typename T> operator const T*(); // overload 2
};

void test()
{
    S{}.operator int*(); // this used to call overload 2, now it calls overload 1
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#added-support-for-elifdef-and-elifndef)
### Added Support for `#elifdef` and `#elifndef`
Support added for WG21 `#elifdef` and `#elifndef` preprocessor directives. Requires `/std:clatest` or `/std:c++latest`.
Before:
C++
Copy
```
#ifdef __cplusplus
  #include <atomic>
#elif !defined(__STDC_NO_ATOMICS__)
  #include <stdatomic.h>
#else
  #include <custom_atomics_library.h>
#endif

```

After:
C++
Copy
```
#ifdef __cplusplus
  #include <atomic>
#elifndef __STDC_NO_ATOMICS__
  #include <stdatomic.h>
#else
  #include <custom_atomics_library.h>
#endif

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#application-of-_alignas-on-a-structured-type-in-c)
### Application of `_Alignas` on a structured type in C
Applies to the C language (C17 and later). Also added to Microsoft Visual Studio 17.9
In versions of Visual C++ before Visual Studio 2022 version 17.9, if the `_Alignas` specifier appeared next to a structured type in a declaration, it wasn't applied correctly according to the ISO-C Standard.
C++
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

According to the ISO-C Standard, this code should compile without `static_assert` emitting a diagnostic.
The `_Alignas` directive applies only to the member variable `member1`. It must not change the alignment of `struct Inner`. However, before Visual Studio 17.9.1, the diagnostic "incorrect alignment" was emitted. The compiler aligned `member2` to an offset of 32 bytes within the `struct Outer` type.
This is a binary breaking change, so a warning is now emitted when this change takes effect. Warning C5274 is now emitted at warning level 1 for the previous example: ` warning C5274: behavior change: _Alignas no longer applies to the type 'Inner' (only applies to declared data objects)`.
Also, in previous versions of Visual Studio, when the `_Alignas` specifier appeared next to an anonymous type declaration, it was ignored.
C++
Copy
```
// compile with /std:c17
#include <stddef.h>
struct S
{
    _Alignas(32) struct { int anon_member; };
    int k;
};

static_assert(offsetof(struct S, k)==4, "incorrect offsetof");
static_assert(sizeof(struct S)==32, "incorrect size");

```

Previously, both `static_assert` statements failed when compiling this code. Now the code compiles, but emits the following level 1 warnings:
C
Copy
```
warning C5274: behavior change: _Alignas no longer applies to the type '<unnamed-tag>' (only applies to declared data objects)
warning C5273: behavior change: _Alignas on anonymous type no longer ignored (promoted members will align)

```

To get the previous behavior, replace `_Alignas(N)` with `__declspec(align(N))`. Unlike `_Alignas`, `declspec(align)` applies to the type.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improved-warning-c4706)
### Improved warning C4706
This is a source code breaking change. Previously, the compiler didn't detect the convention of wrapping an assignment in parentheses, if assignment was intended, to suppress [warning C4706](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-4-c4706?view=msvc-170) about assignment within a conditional expression. The compiler now detects the parentheses and suppresses the warning.
C++
Copy
```
#pragma warning(error: 4706)

struct S
{
   auto mf()
   {
      if (value = 9)
         return value + 4;
      else
         return value;
   }

   int value = 9;
};

```

The compiler now also emits the warning in cases where the function isn't referenced. Previously, because `mf` is an inline function that isn't referenced, warning C4706 wasn't emitted for this code. Now the warning is emitted:
C++
Copy
```
error C4706: assignment used as a condition
note: if an assignment is intended you can enclose it in parentheses, '(e1 = e2)', to silence this warning

```

To fix this warning, either use an equality operator, `value == 9`, if this is what was intended. Or, wrap the assignment in parentheses, `(value = 9)`, if assignment is intended. Otherwise, since the function is unreferenced, remove it.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_179)
