##  Conformance improvements in Visual Studio 2022 version 17.0
Visual Studio 2022 version 17.0 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#warning-on-bitfield-width-for-enumeration-type)
### Warning on bitfield width for enumeration type
When you declare an instance of an enumeration type as a bitfield, the width of the bitfield must accommodate all possible values of the enumeration. Otherwise, the compiler issues a diagnostic message. Consider this example: Consider:
C++
Copy
```
enum class E : unsigned { Zero, One, Two };

struct S {
  E e : 1;
};

```

A programmer might expect the class member `S::e` can hold any of the explicitly named `enum` values. Given the number of enumeration elements, it isn't possible. The bitfield can't cover the range of explicitly provided values of `E` (conceptually, the _domain_ of `E`). To address the concern that the bitfield width isn't large enough for the domain of the enumeration, a new (off by default) warning is added to MSVC:
Output
Copy
```
t.cpp(4,5): warning C5249: 'S::e' of type 'E' has named enumerators with values that cannot be represented in the given bit field width of '1'.
  E e : 1;
    ^
t.cpp(1,38): note: see enumerator 'E::Two' with value '2'
enum class E : unsigned { Zero, One, Two };
                                     ^

```

This compiler behavior is a source and binary breaking change that affects all **`/std`**and**`/permissive`**modes.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#error-on-ordered-pointer-comparison-against-nullptr-or-0)
### Error on ordered pointer comparison against `nullptr` or 0
The C++ Standard inadvertently allowed an ordered pointer comparison against `nullptr` or 0. For example:
C++
Copy
```
bool f(int *p)
{
   return p >= 0;
}

```

WG21 paper **`/permissive-`**(and**`/diagnostics:caret`**), it emits the following error:
Output
Copy
```
t.cpp(3,14): error C7664: '>=': ordered comparison of pointer and integer zero ('int *' and 'int')
    return p >= 0;
             ^

```

This compiler behavior is a source and binary breaking change that affects code compiled using **`/permissive-`**in all**`/std`**modes.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#see-also)
