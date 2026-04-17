##  Conformance improvements in 15.9
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#left-to-right-evaluation-order-for-operators-----and-)
### Left-to-right evaluation order for operators `->*`, `[]`, `>>`, and `<<`
Starting in C++17, the operands of the operators `->*`, `[]`, `>>`, and `<<` must be evaluated in left-to-right order. There are two cases in which the compiler is unable to guarantee this order:
  * when one of the operand expressions is an object passed by value or contains an object passed by value, or
  * when compiled by using **`/clr`**, and one of the operands is a field of an object or an array element.


The compiler emits warning [C4866](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4866?view=msvc-170) when it can't guarantee left-to-right evaluation. The compiler generates this warning only if **`/std:c++17`**or later is specified, as the left-to-right order requirement of these operators was introduced in C++17.
To resolve this warning, first consider whether left-to-right evaluation of the operands is necessary. For example, it could be necessary when evaluation of the operands might produce order-dependent side-effects. The order in which operands are evaluated has no observable effect in many cases. If the order of evaluation must be left-to-right, consider whether you can pass the operands by const reference instead. This change eliminates the warning in the following code sample:
C++
Copy
```
// C4866.cpp
// compile with: /w14866 /std:c++17

class HasCopyConstructor
{
public:
    int x;

    HasCopyConstructor(int x) : x(x) {}
    HasCopyConstructor(const HasCopyConstructor& h) : x(h.x) { }
};

int operator>>(HasCopyConstructor a, HasCopyConstructor b) { return a.x >> b.x; }

// This version of operator>> does not trigger the warning:
// int operator>>(const HasCopyConstructor& a, const HasCopyConstructor& b) { return a.x >> b.x; }

int main()
{
    HasCopyConstructor a{ 1 };
    HasCopyConstructor b{ 2 };

    a>>b;        // C4866 for call to operator>>
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#identifiers-in-member-alias-templates)
### Identifiers in member alias templates
An identifier used in a member alias template definition must be declared before use.
In previous versions of the compiler, the following code was allowed. In Visual Studio 2017 version 15.9, in [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode, the compiler raises [C3861](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c3861?view=msvc-170):
C++
Copy
```
template <typename... Ts>
struct A
{
  public:
    template <typename U>
    using from_template_t = decltype(from_template(A<U>{})); // C3861:
        // 'from_template': identifier not found

  private:
    template <template <typename...> typename Type, typename... Args>
    static constexpr A<Args...> from_template(A<Type<Args...>>);
};

A<>::from_template_t<A<int>> a;

```

To fix the error, declare `from_template` before `from_template_t`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#modules-changes)
### Modules changes
In Visual Studio 2017, version 15.9, the compiler raises [C5050](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c5050?view=msvc-170) whenever the command-line options for modules aren't consistent between the module creation and module consumption sides. In the following example, there are two issues:
  * On the consumption side (main.cpp), the option **`/EHsc`**isn't specified.
  * The C++ version is **`/std:c++17`**on the creation side, and**`/std:c++14`**on the consumption side.


Windows Command Prompt
Copy
```
cl /EHsc /std:c++17 m.ixx /experimental:module
cl /experimental:module /module:reference m.ifc main.cpp /std:c++14

```

The compiler raises C5050 for both of these cases:
Output
Copy
```
warning C5050: Possible incompatible environment while
importing module 'm': mismatched C++ versions.
Current "201402" module version "201703".

```

The compiler also raises [C7536](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c7536?view=msvc-170) whenever the _`.ifc`_file has been tampered with. The header of the module interface contains an SHA2 hash of the contents below it. On import, the _`.ifc`_file is hashed, then checked against the hash provided in the header. If these don't match, error C7536 is raised:
Output
Copy
```
error C7536: ifc failed integrity checks.
Expected SHA2: '66d5c8154df0c71d4cab7665bab4a125c7ce5cb9a401a4d8b461b706ddd771c6'

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#partial-ordering-involving-aliases-and-non-deduced-contexts)
### Partial ordering involving aliases and non-deduced contexts
Implementations diverge in the partial ordering rules involving aliases in non-deduced contexts. In the following example, GCC and the Microsoft C++ compiler (in [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) mode) raise an error, while Clang accepts the code.
C++
Copy
```
#include <utility>
using size_t = std::size_t;

template <typename T>
struct A {};
template <size_t, size_t>
struct AlignedBuffer {};
template <size_t len>
using AlignedStorage = AlignedBuffer<len, 4>;

template <class T, class Alloc>
int f(Alloc &alloc, const AlignedStorage<T::size> &buffer)
{
    return 1;
}

template <class T, class Alloc>
int f(A<Alloc> &alloc, const AlignedStorage<T::size> &buffer)
{
    return 2;
}

struct Alloc
{
    static constexpr size_t size = 10;
};

int main()
{
    A<void> a;
    AlignedStorage<Alloc::size> buf;
    if (f<Alloc>(a, buf) != 2)
    {
        return 1;
    }

    return 0;
}

```

The previous example raises [C2668](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c2668?view=msvc-170):
Output
Copy
```
partial_alias.cpp(32): error C2668: 'f': ambiguous call to overloaded function
partial_alias.cpp(18): note: could be 'int f<Alloc,void>(A<void> &,const AlignedBuffer<10,4> &)'
partial_alias.cpp(12): note: or       'int f<Alloc,A<void>>(Alloc &,const AlignedBuffer<10,4> &)'
        with
        [
            Alloc=A<void>
        ]
partial_alias.cpp(32): note: while trying to match the argument list '(A<void>, AlignedBuffer<10,4>)'

```

The implementation divergence is because of a regression in the C++ standard wording. The resolution to core issue 2235 removed some text that would allow these overloads to be ordered. The current C++ standard doesn't provide a mechanism to partially order these functions, so they're considered ambiguous.
As a workaround, we recommended that you not rely on partial ordering to resolve this problem. Instead, use SFINAE to remove particular overloads. In the following example, we use a helper class `IsA` to remove the first overload when `Alloc` is a specialization of `A`:
C++
Copy
```
#include <utility>
using size_t = std::size_t;

template <typename T>
struct A {};
template <size_t, size_t>
struct AlignedBuffer {};
template <size_t len>
using AlignedStorage = AlignedBuffer<len, 4>;

template <typename T> struct IsA : std::false_type {};
template <typename T> struct IsA<A<T>> : std::true_type {};

template <class T, class Alloc, typename = std::enable_if_t<!IsA<Alloc>::value>>
int f(Alloc &alloc, const AlignedStorage<T::size> &buffer)
{
    return 1;
}

template <class T, class Alloc>
int f(A<Alloc> &alloc, const AlignedStorage<T::size> &buffer)
{
    return 2;
}

struct Alloc
{
    static constexpr size_t size = 10;
};

int main()
{
    A<void> a;
    AlignedStorage<Alloc::size> buf;
    if (f<Alloc>(a, buf) != 2)
    {
        return 1;
    }

    return 0;
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#illegal-expressions-and-non-literal-types-in-templated-function-definitions)
### Illegal expressions and non-literal types in templated function definitions
Illegal expressions and non-literal types are now correctly diagnosed in the definitions of templated functions that are explicitly specialized. Previously, such errors weren't emitted for the function definition. However, the illegal expression or non-literal type would still have been diagnosed if evaluated as part of a constant expression.
In previous versions of Visual Studio, the following code compiles without warning:
C++
Copy
```
void g();

template<typename T>
struct S
{
    constexpr void f();
};

template<>
constexpr void S<int>::f()
{
    g(); // C3615 in 15.9
}

```

In Visual Studio 2017 version 15.9, the code raises error [C3615](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c3615?view=msvc-170):
Output
Copy
```
error C3615: constexpr function 'S<int>::f' cannot result in a constant expression.
note: failure was caused by call of undefined function or one not declared 'constexpr'
note: see usage of 'g'.

```

To avoid the error, remove the **`constexpr`**qualifier from the explicit instantiation of the function`f()`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#see-also)
