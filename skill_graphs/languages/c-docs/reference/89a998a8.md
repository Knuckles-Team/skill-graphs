##  Conformance improvements in 15.7
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-rewording-inheriting-constructors)
### C++17: Rewording inheriting constructors
**`using`**declaration that names a constructor now makes the corresponding base class constructors visible to initializations of the derived class, rather than declaring more derived class constructors. This rewording is a change from C++14. In Visual Studio 2017 version 15.7 and later, in**`/std:c++17`**mode and later, code that is valid in C++14 and uses inheriting constructors may not be valid, or may have different semantics.
The following example shows C++14 behavior:
C++
Copy
```
struct A {
    template<typename T>
    A(T, typename T::type = 0);
    A(int);
};

struct B : A {
    using A::A;
    B(int n) = delete; // Error C2280
};

B b(42L); // Calls B<long>(long), which calls A(int)
          //  due to substitution failure in A<long>(long).

```

The following example shows **`/std:c++17`**behavior in Visual Studio 15.7:
C++
Copy
```
struct A {
    template<typename T>
    A(T, typename T::type = 0);
    A(int);
};

struct B : A {
    using A::A;
    B(int n)
    {
        //do something
    }
};

B b(42L); // now calls B(int)

```

For more information, see [Constructors](https://learn.microsoft.com/en-us/cpp/cpp/constructors-cpp?view=msvc-170#inheriting_constructors).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-extended-aggregate-initialization)
### C++17: Extended aggregate initialization
If the constructor of a base class is non-public, but accessible to a derived class, then under **`/std:c++17`**mode and later in Visual Studio 2017 version 15.7, you can no longer use empty braces to initialize an object of the derived type. The following example shows C++14 conforming behavior:
C++
Copy
```
struct Derived;
struct Base {
    friend struct Derived;
private:
    Base() {}
};

struct Derived : Base {};
Derived d1; // OK. No aggregate init involved.
Derived d2 {}; // OK in C++14: Calls Derived::Derived()
               // which can call Base ctor.

```

In C++17, `Derived` is now considered an aggregate type. It means that the initialization of `Base` via the private default constructor happens directly, as part of the extended aggregate initialization rule. Previously, the `Base` private constructor was called via the `Derived` constructor, and it succeeded because of the friend declaration. The following example shows C++17 behavior in Visual Studio version 15.7 in **`/std:c++17`**mode:
C++
Copy
```
struct Derived;
struct Base {
    friend struct Derived;
private:
    Base() {}
};
struct Derived : Base {
    Derived() {} // add user-defined constructor
                 // to call with {} initialization
};
Derived d1; // OK. No aggregate init involved.
Derived d2 {}; // error C2248: 'Base::Base': cannot access
               // private member declared in class 'Base'

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-declaring-non-type-template-parameters-with-auto)
### C++17: Declaring non-type template parameters with auto
In **`/std:c++17`**mode, the compiler can now deduce the type of a non-type template argument that is declared with**`auto`**:
C++
Copy
```
template <auto x> constexpr auto constant = x;

auto v1 = constant<5>;      // v1 == 5, decltype(v1) is int
auto v2 = constant<true>;   // v2 == true, decltype(v2) is bool
auto v3 = constant<'a'>;    // v3 == 'a', decltype(v3) is char

```

One effect of this new feature is that valid C++14 code may not be valid or may have different semantics. For example, some overloads that were previously invalid are now valid. The following example shows C++14 code that compiles because the call to `example(p)` is bound to `example(void*);`. In Visual Studio 2017 version 15.7, in **`/std:c++17`**mode, the`example` function template is the best match.
C++
Copy
```
template <int N> struct A;
template <typename T, T N> int example(A<N>*) = delete;

void example(void *);

void sample(A<0> *p)
{
    example(p); // OK in C++14
}

```

The following example shows C++17 code in Visual Studio 15.7 in **`/std:c++17`**mode:
C++
Copy
```
template <int N> struct A;
template <typename T, T N> int example(A<N>*);

void example(void *);

void sample(A<0> *p)
{
    example(p); // C2280: 'int example<int,0>(A<0>*)': attempting to reference a deleted function
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-elementary-string-conversions-partial)
### C++17: Elementary string conversions (partial)
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c20-avoiding-unnecessary-decay-partial)
### C++20: Avoiding unnecessary decay (partial)
`remove_reference_t` replaces `decay_t` in some contexts. Support for `remove_cvref_t` is implemented in Visual Studio 2019.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-parallel-algorithms)
### C++17: Parallel algorithms
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-hypotx-y-z)
### C++17: `hypot(x, y, z)`
`std::hypot`, for types **`float`**,**`double`**, and**`long double`**, each of which has three input parameters.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-filesystem)
### C++17: _`<filesystem>`_
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-mathematical-special-functions)
### C++17: Mathematical special functions
_`<cmath>`_header.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-deduction-guides-for-the-standard-library)
### C++17: Deduction guides for the standard library
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-repairing-elementary-string-conversions)
### C++17: Repairing elementary string conversions
_`<charconv>`_and make other improvements, including changing error handling to use`std::errc` instead of `std::error_code`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-constexpr-for-char_traits-partial)
### C++17: `constexpr` for `char_traits` (partial)
`std::traits_type` member functions `length`, `compare`, and `find` to make `std::string_view` usable in constant expressions. (In Visual Studio 2017 version 15.6, supported for Clang/LLVM only. In version 15.7, support is nearly complete for ClXX as well.)
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-default-argument-in-the-primary-class-template)
### C++17: Default argument in the primary class template
This behavior change is a precondition for
Previously, the compiler ignored the default argument in the primary class template:
C++
Copy
```
template<typename T>
struct S {
    void f(int = 0);
};

template<typename T>
void S<T>::f(int = 0) {} // Re-definition necessary

```

In **`/std:c++17`**mode in Visual Studio 2017 version 15.7, the default argument isn't ignored:
C++
Copy
```
template<typename T>
struct S {
    void f(int = 0);
};

template<typename T>
void S<T>::f(int) {} // Default argument is used

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#dependent-name-resolution)
### Dependent name resolution
This behavior change is a precondition for
In the following example, the compiler in Visual Studio 15.6 and earlier resolves `D::type` to `B<T>::type` in the primary class template.
C++
Copy
```
template<typename T>
struct B {
    using type = T;
};

template<typename T>
struct D : B<T*> {
    using type = B<T*>::type;
};

```

Visual Studio 2017 version 15.7, in **`/std:c++17`**mode, requires the**`typename`**keyword in the**`using`**statement in D. Without**`typename`**, the compiler raises warning C4346:`'B<T*>::type': dependent name is not a type` and error C2061: `syntax error: identifier 'type'`:
C++
Copy
```
template<typename T>
struct B {
    using type = T;
};

template<typename T>
struct D : B<T*> {
    using type = typename B<T*>::type;
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-nodiscard-attribute---warning-level-increase)
### C++17: `[[nodiscard]]` attribute - warning level increase
In Visual Studio 2017 version 15.7 in **`/std:c++17`**mode, the warning level of[C4834](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4834?view=msvc-170) is increased from W3 to W1. You can disable the warning with a cast to **`void`**, or by passing**`/wd:4834`**to the compiler.
C++
Copy
```
[[nodiscard]] int f() { return 0; }

int main() {
    f(); // warning C4834: discarding return value
         // of function with 'nodiscard'
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#variadic-template-constructor-base-class-initialization-list)
### Variadic template constructor base class initialization list
In previous editions of Visual Studio, a variadic template constructor base class initialization list that was missing template arguments was erroneously allowed without error. In Visual Studio 2017 version 15.7, a compiler error is raised.
The following code example in Visual Studio 2017 version 15.7 raises error C2614:
C++
Copy
```
template<typename T>
struct B {};

template<typename T>
struct D : B<T>
{

    template<typename ...C>
    D() : B() {} // C2614: D<int>: illegal member initialization: 'B' is not a base or member
};

D<int> d;

```

To fix the error, change the `B()` expression to `B<T>()`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#constexpr-aggregate-initialization)
###  `constexpr` aggregate initialization
Previous versions of the C++ compiler incorrectly handled **`constexpr`**aggregate initialization. The compiler accepted invalid code in which the aggregate-init-list had too many elements, and produced bad object code for it. The following code is an example of such code:
C++
Copy
```
#include <array>
struct X {
    unsigned short a;
    unsigned char b;
};

int main() {
    constexpr std::array<X, 2> xs = { // C2078: too many initializers
        { 1, 2 },
        { 3, 4 }
    };
    return 0;
}

```

In Visual Studio 2017 version 15.7 update 3 and later, the previous example now raises C2078. The following example shows how to fix the code. When initializing a `std::array` with nested brace-init-lists, give the inner array a braced-list of its own:
C++
Copy
```
#include <array>
struct X {
    unsigned short a;
    unsigned char b;
};

int main() {
    constexpr std::array<X, 2> xs = {{ // note double braces
        { 1, 2 },
        { 3, 4 }
    }}; // note double braces
    return 0;
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#update_158)
