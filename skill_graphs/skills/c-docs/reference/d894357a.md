##  Conformance improvements in 15.8
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#typename-on-unqualified-identifiers)
###  `typename` on unqualified identifiers
In [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode, spurious **`typename`**keywords on unqualified identifiers in alias template definitions are no longer accepted by the compiler. The following code now produces C7511:
C++
Copy
```
template <typename T>
using  X = typename T; // C7511: 'T': 'typename' keyword must be
                       // followed by a qualified name

```

To fix the error, change the second line to `using  X = T;`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#__declspec-on-right-side-of-alias-template-definitions)
###  `__declspec()` on right side of alias template definitions
[`__declspec`](https://learn.microsoft.com/en-us/cpp/cpp/declspec?view=msvc-170) is no longer permitted on the right-hand-side of an alias template definition. Previously, the compiler accepted but ignored this code. It would never result in a deprecation warning when the alias was used.
The standard C++ attribute [`[[deprecated]]`](https://learn.microsoft.com/en-us/cpp/cpp/attributes?view=msvc-170) may be used instead, and is respected in Visual Studio 2017 version 15.6. The following code now produces C2760:
C++
Copy
```
template <typename T>
using X = __declspec(deprecated("msg")) T; // C2760: syntax error:
                                           // unexpected token '__declspec',
                                           // expected 'type specifier'

```

To fix the error, change the code to the following (with the attribute placed before the '=' of the alias definition):
C++
Copy
```
template <typename T>
using  X [[deprecated("msg")]] = T;

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#two-phase-name-lookup-diagnostics)
### Two-phase name lookup diagnostics
Two-phase name lookup requires that non-dependent names used in template bodies must be visible to the template at definition time. Previously, the Microsoft C++ compiler would leave an unfound name as not looked up until instantiation time. Now, it requires that non-dependent names are bound in the template body.
One way this can manifest is with lookup into dependent base classes. Previously, the compiler allowed the use of names that are defined in dependent base classes. It's because they'd be looked up during instantiation time when all the types are resolved. Now that code is treated as an error. In these cases, you can force the variable to be looked up at instantiation time by qualifying it with the base class type or otherwise making it dependent, for example, by adding a `this->` pointer.
In [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode, the following code now raises C3861:
C++
Copy
```
template <class T>
struct Base {
    int base_value = 42;
};

template <class T>
struct S : Base<T> {
    int f() {
        return base_value; // C3861: 'base_value': identifier not found
    }
};

```

To fix the error, change the **`return`**statement to`return this->base_value;`.
In Boost.Python library versions before 1.70, there's been an MSVC-specific workaround for a template forward declaration in [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode starting in Visual Studio 2017 version 15.8 (`_MSC_VER==1915`), the MSVC compiler does argument-dependent name lookup (ADL) correctly. It's now consistent with other compilers, making this workaround guard unnecessary. To avoid error C3861: `'unwind_type': identifier not found`, update your Boost.Python library.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#forward-declarations-and-definitions-in-namespace-std)
### forward declarations and definitions in namespace `std`
The C++ standard doesn't allow a user to add forward declarations or definitions into namespace `std`. Adding declarations or definitions to namespace `std` or to a namespace within namespace `std` now results in undefined behavior.
At some time in the future, Microsoft will move the location where some standard library types are defined. This change will break existing code that adds forward declarations to namespace `std`. A new warning, C4643, helps identify such source issues. The warning is enabled in **`/default`**mode and is off by default. It will affect programs that are compiled with**`/Wall`**or**`/WX`**.
The following code now raises C4643:
C++
Copy
```
namespace std {
    template<typename T> class vector;  // C4643: Forward declaring 'vector'
                                        // in namespace std is not permitted
                                        // by the C++ Standard
}

```

To fix the error, use a **`#include`**directive rather than a forward declaration:
C++
Copy
```
#include <vector>

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#constructors-that-delegate-to-themselves)
### Constructors that delegate to themselves
The C++ standard suggests that a compiler should emit a diagnostic when a delegating constructor delegates to itself. The Microsoft C++ compiler in [`/std:c++17`](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170) and [`/std:c++latest`](https://learn.microsoft.com/en-us/cpp/build/reference/std-specify-language-standard-version?view=msvc-170) modes now raises C7535.
Without this error, the following program will compile but will generate an infinite loop:
C++
Copy
```
class X {
public:
    X(int, int);
    X(int v) : X(v){} // C7535: 'X::X': delegating constructor calls itself
};

```

To avoid the infinite loop, delegate to a different constructor:
C++
Copy
```
class X {
public:

    X(int, int);
    X(int v) : X(v, 0) {}
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#offsetof-with-constant-expressions)
###  `offsetof` with constant expressions
[`offsetof`](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/offsetof-macro?view=msvc-170) has traditionally been implemented using a macro that requires a [`reinterpret_cast`](https://learn.microsoft.com/en-us/cpp/cpp/reinterpret-cast-operator?view=msvc-170). This usage is illegal in contexts that require a constant expression, but the Microsoft C++ compiler has traditionally allowed it. The `offsetof` macro that is shipped as part of the standard library correctly uses a compiler intrinsic (**`__builtin_offsetof`**), but many people have used the macro trick to define their own`offsetof`.
In Visual Studio 2017 version 15.8, the compiler constrains the areas that these **`reinterpret_cast`**operators can appear in the default mode, to help code conform to standard C++ behavior. Under[`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170), the constraints are even stricter. Using the result of an `offsetof` in places that require constant expressions may result in code that issues warning C4644 or C2975.
The following code raises C4644 in default and **`/std:c++17`**modes, and C2975 in[`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode:
C++
Copy
```
struct Data {
    int x;
};

// Common pattern of user-defined offsetof
#define MY_OFFSET(T, m) (unsigned long long)(&(((T*)nullptr)->m))

int main()

{
    switch (0) {
    case MY_OFFSET(Data, x): return 0; // C4644: usage of the
        // macro-based offsetof pattern in constant expressions
        // is non-standard; use offsetof defined in the C++
        // standard library instead
        // OR
        // C2975: invalid template argument, expected
        // compile-time constant expression

    default: return 1;
    }
}

```

To fix the error, use `offsetof` as defined via _`<cstddef>`_:
C++
Copy
```
#include <cstddef>

struct Data {
    int x;
};

int main()
{
    switch (0) {
    case offsetof(Data, x): return 0;
    default: return 1;
    }
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#cv-qualifiers-on-base-classes-subject-to-pack-expansion)
### cv-qualifiers on base classes subject to pack expansion
Previous versions of the Microsoft C++ compiler didn't detect that a base-class had cv-qualifiers if it was also subject to pack expansion.
In Visual Studio 2017 version 15.8, in [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode, the following code raises C3770:
C++
Copy
```
template<typename... T>
class X : public T... { };

class S { };

int main()
{
    X<const S> x; // C3770: 'const S': is not a valid base class
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#template-keyword-and-nested-name-specifiers)
###  `template` keyword and nested-name-specifiers
In [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode, the compiler now requires the **`template`**keyword to precede a template-name when it comes after a dependent nested-name-specifier.
The following code in [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode now raises [C7510](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c7510?view=msvc-170):
C++
Copy
```
template<typename T> struct Base
{
    template<class U> void example() {}
};

template<typename T>
struct X : Base<T>
{
    void example()
    {
        Base<T>::example<int>(); // C7510: 'example': use of dependent
            // template name must be prefixed with 'template'
            // note: see reference to class template instantiation
            // 'X<T>' being compiled
    }
};

```

To fix the error, add the **`template`**keyword to the`Base<T>::example<int>();` statement, as shown in the following example:
C++
Copy
```
template<typename T> struct Base
{
    template<class U> void example() {}
};

template<typename T>
struct X : Base<T>
{
    void example()
    {
        // Add template keyword here:
        Base<T>::template example<int>();
    }
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#improvements_159)
