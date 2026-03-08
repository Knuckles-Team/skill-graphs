##  Conformance improvements in Visual Studio 2022 version 17.4
Visual Studio 2022 version 17.4 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#underlying-types-of-unscoped-enum-with-no-fixed-type)
### Underlying types of unscoped `enum` with no fixed type
In versions of Visual Studio before Visual Studio 2022 version 17.4, the C++ compiler didn't correctly determine the underlying type of an unscoped enumeration with no fixed base type. Under [`/Zc:enumTypes`](https://learn.microsoft.com/en-us/cpp/build/reference/zc-enumtypes?view=msvc-170), we now correctly implement the standard behavior.
The C++ Standard requires the underlying type of an **`enum`**to be large enough to hold all enumerators in that**`enum`**. Sufficiently large enumerators can set the underlying type of the**`enum`**to**`unsigned int`**,**`long long`**, or**`unsigned long long`**. Previously, such**`enum`**types always had an underlying type of**`int`**in the Microsoft compiler, regardless of enumerator values.
When enabled, the **`/Zc:enumTypes`**option is a potential source and binary breaking change. It's off by default, and not enabled by**`/permissive-`**, because the fix might affect binary compatibility. Some enumeration types change size when the conformant fix is enabled. Certain Windows SDK headers include such enumeration definitions.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example)
#### Example
C++
Copy
```
enum Unsigned
{
    A = 0xFFFFFFFF // Value 'A' does not fit in 'int'.
};

// Previously, failed this static_assert. Now passes with /Zc:enumTypes.
static_assert(std::is_same_v<std::underlying_type_t<Unsigned>, unsigned int>);

template <typename T>
void f(T x)
{
}

int main()
{
    // Previously called f<int>, now calls f<unsigned int>.
    f(+A);
}

// Previously this enum would have an underlying type of `int`, but Standard C++ requires this to have
// a 64-bit underlying type. Using /Zc:enumTypes changes the size of this enum from 4 to 8, which could
// impact binary compatibility with code compiled with an earlier compiler version or without the switch.
enum Changed
{
    X = -1,
    Y = 0xFFFFFFFF
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#types-of-enumerators-within-an-enum-definition-with-no-fixed-underlying-type)
### Types of enumerators within an `enum` definition with no fixed underlying type
In versions of Visual Studio before Visual Studio 2022 version 17.4, the C++ compiler didn't correctly model the types of enumerators. It could assume an incorrect type in enumerations without a fixed underlying type before the closing brace of the enumeration. Under [`/Zc:enumTypes`](https://learn.microsoft.com/en-us/cpp/build/reference/zc-enumtypes?view=msvc-170), the compiler now correctly implements the standard behavior.
The C++ Standard specifies that within an enumeration definition of no fixed underlying type, initializers determine the types of enumerators. Or, for the enumerators with no initializer, by the type of the previous enumerator (accounting for overflow). Previously, such enumerators were always given the deduced type of the enumeration, with a placeholder for the underlying type (typically **`int`**).
When enabled, the **`/Zc:enumTypes`**option is a potential source and binary breaking change. It's off by default, and not enabled by**`/permissive-`**, because the fix might affect binary compatibility. Some enumeration types change size when the conformant fix is enabled. Certain Windows SDK headers include such enumeration definitions.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-1)
#### Example
C++
Copy
```
enum Enum {
    A = 'A',
    B = sizeof(A)
};

static_assert(B == 1); // previously failed, now succeeds under /Zc:enumTypes

```

In this example the enumerator `A` should have type **`char`**before the closing brace of the enumeration, so`B` should be initialized using `sizeof(char)`. Before the **`/Zc:enumTypes`**fix,`A` had enumeration type `Enum` with a deduced underlying type **`int`**, and`B` was initialized using `sizeof(Enum)`, or 4.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_173)
