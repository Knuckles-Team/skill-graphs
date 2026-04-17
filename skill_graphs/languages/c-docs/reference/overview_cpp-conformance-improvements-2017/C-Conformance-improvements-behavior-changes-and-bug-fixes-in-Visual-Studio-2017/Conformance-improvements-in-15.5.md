##  Conformance improvements in 15.5
Features marked with [14] are available unconditionally even in **`/std:c++14`**mode.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#new-compiler-switch-for-extern-constexpr)
### New compiler switch for `extern constexpr`
In earlier versions of Visual Studio, the compiler always gave a **`constexpr`**variable internal linkage, even when the variable was marked**`extern`**. In Visual Studio 2017 version 15.5, a new compiler switch,[`/Zc:externConstexpr`](https://learn.microsoft.com/en-us/cpp/build/reference/zc-externconstexpr?view=msvc-170), enables correct and standards-conforming behavior. For more information, see [`extern constexpr` linkage](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#extern_linkage).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#removing-dynamic-exception-specifications)
### Removing dynamic exception specifications
`throw()` specification is kept strictly as an alias for `noexcept(true)`. For more information, see [Dynamic exception specification removal and `noexcept`](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#noexcept_removal).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#not_fn)
### `not_fn()`
`not_fn` is a replacement of `not1` and `not2`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#rewording-enable_shared_from_this)
### Rewording `enable_shared_from_this`
`enable_shared_from_this` was added in C++11. The C++17 standard updates the specification to better handle certain corner cases. [14]
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#splicing-maps-and-sets)
### Splicing maps and sets
`map`, `set`, `unordered_map`, `unordered_set`) which can then be modified and inserted back into the same container or a different container that uses the same node type. (A common use case is to extract a node from a `std::map`, change the key, and reinsert.)
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#deprecating-vestigial-library-parts)
### Deprecating vestigial library parts
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#removing-allocator-support-in-stdfunction)
### Removing allocator support in `std::function`
`std::function` had several constructors that took an allocator argument. However, the use of allocators in this context was problematic, and the semantics were unclear. The problematic constructors have been removed.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#fixes-for-not_fn)
### Fixes for `not_fn()`
`std::not_fn` provides support of propagation of value category when used in wrapper invocation.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#shared_ptrt-shared_ptrtn)
###  `shared_ptr<T[]>`, `shared_ptr<T[N]>`
`shared_ptr` changes from Library Fundamentals to C++17. [14]
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#fixing-shared_ptr-for-arrays)
### Fixing `shared_ptr` for arrays
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#clarifying-insert_return_type)
### Clarifying `insert_return_type`
`insert` that returns a nested type `insert_return_type`. That return type is now defined as a specialization of a type that is parameterized on the Iterator and NodeType of the container.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#inline-variables-for-the-standard-library)
### Inline variables for the standard library
For
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#annex-d-features-deprecated)
### Annex D features deprecated
Annex D of the C++ standard contains all the features that have been deprecated, including `shared_ptr::unique()`, `<codecvt>`, and `namespace std::tr1`. When the **`/std:c++17`**or later compiler option is set, almost all the standard library features in Annex D are marked as deprecated. For more information, see[Standard library features in Annex D are marked as deprecated](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#annex_d).
The `std::tr2::sys` namespace in `<experimental/filesystem>` now emits a deprecation warning under **`/std:c++14`**by default, and is now removed under**`/std:c++17`**and later by default.
Improved conformance in `<iostream>` by avoiding a non-standard extension (in-class explicit specializations).
The standard library now uses variable templates internally.
The standard library was updated in response to C++17 compiler changes. Updates include the addition of **`noexcept`**in the type system, and the removal of dynamic-exception-specifications.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#partial-ordering-change)
### Partial ordering change
The compiler now correctly rejects the following code and gives the correct error message:
C++
Copy
```
template<typename... T>
int f(T* ...)
{
    return 1;
}

template<typename T>
int f(const T&)
{
    return 2;
}

int main()
{
    int i = 0;
    f(&i);    // C2668
}

```

Output
Copy
```
t161.cpp
t161.cpp(16): error C2668: 'f': ambiguous call to overloaded function
t161.cpp(8): note: could be 'int f<int*>(const T &)'
        with
        [
            T=int*
        ]
t161.cpp(2): note: or       'int f<int>(int*)'
t161.cpp(16): note: while trying to match the argument list '(int*)'

```

The problem in the example above is that there are two differences in the types (const vs. non-const and pack vs. non-pack). To eliminate the compiler error, remove one of the differences. Then the compiler can unambiguously order the functions.
C++
Copy
```
template<typename... T>
int f(T* ...)
{
    return 1;
}

template<typename T>
int f(T&)
{
    return 2;
}

int main()
{
    int i = 0;
    f(&i);
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#exception-handlers)
### Exception handlers
Handlers of reference to array or function type are never a match for any exception object. The compiler now correctly honors this rule and raises a level 4 warning, [C4843](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4843?view=msvc-170). It also no longer matches a handler of `char*` or `wchar_t*` to a string literal when **`/Zc:strictStrings`**is used.
C++
Copy
```
int main()
{
    try {
        throw "";
    }
    catch (int (&)[1]) {} // C4843 (This should always be dead code.)
    catch (void (&)()) {} // C4843 (This should always be dead code.)
    catch (char*) {} // This should not be a match under /Zc:strictStrings
}

```

Output
Copy
```
warning C4843: 'int (&)[1]': An exception handler of reference to array or function type is unreachable, use 'int*' instead
warning C4843: 'void (__cdecl &)(void)': An exception handler of reference to array or function type is unreachable, use 'void (__cdecl*)(void)' instead

```

The following code avoids the error:
C++
Copy
```
catch (int (*)[1]) {}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#tr1)
###  `std::tr1` namespace is deprecated
The non-standard `std::tr1` namespace is now marked as deprecated in both C++14 and C++17 modes. In Visual Studio 2017 version 15.5, the following code raises C4996:
C++
Copy
```
#include <functional>
#include <iostream>
using namespace std;

int main() {
    std::tr1::function<int (int, int)> f = std::plus<int>(); //C4996
    cout << f(3, 5) << std::endl;
    f = std::multiplies<int>();
    cout << f(3, 5) << std::endl;
}

```

Output
Copy
```
warning C4996: 'std::tr1': warning STL4002: The non-standard std::tr1 namespace and TR1-only machinery are deprecated and will be REMOVED. You can define _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING to acknowledge that you have received this warning.

```

To fix the error, remove the reference to the `tr1` namespace:
C++
Copy
```
#include <functional>
#include <iostream>
using namespace std;

int main() {
    std::function<int (int, int)> f = std::plus<int>();
    cout << f(3, 5) << std::endl;
    f = std::multiplies<int>();
    cout << f(3, 5) << std::endl;
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#annex_d)
###  Standard library features in Annex D are marked as deprecated
When the **`/std:c++17`**mode or later compiler switch is set, almost all standard library features in Annex D are marked as deprecated.
In Visual Studio 2017 version 15.5, the following code raises C4996:
C++
Copy
```
#include <iterator>

class MyIter : public std::iterator<std::random_access_iterator_tag, int> {
public:
    // ... other members ...
};

#include <type_traits>

static_assert(std::is_same<MyIter::pointer, int*>::value, "BOOM");

```

Output
Copy
```
warning C4996: 'std::iterator<std::random_access_iterator_tag,int,ptrdiff_t,_Ty*,_Ty &>::pointer': warning STL4015: The std::iterator class template (used as a base class to provide typedefs) is deprecated in C++17. (The <iterator> header is NOT deprecated.) The C++ standard has never required user-defined iterators to derive from std::iterator. To fix this warning, stop deriving from std::iterator and start providing publicly accessible typedefs named iterator_category, value_type, difference_type, pointer, and reference. Note that value_type is required to be non-const, even for constant iterators. You can define _SILENCE_CXX17_ITERATOR_BASE_CLASS_DEPRECATION_WARNING or _SILENCE_ALL_CXX17_DEPRECATION_WARNINGS to acknowledge that you have received this warning.

```

To fix the error, follow the instructions in the warning text, as demonstrated in the following code:
C++
Copy
```
#include <iterator>

class MyIter {
public:
    typedef std::random_access_iterator_tag iterator_category;
    typedef int value_type;
    typedef ptrdiff_t difference_type;
    typedef int* pointer;
    typedef int& reference;

    // ... other members ...
};

#include <type_traits>

static_assert(std::is_same<MyIter::pointer, int*>::value, "BOOM");

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#unreferenced-local-variables)
### Unreferenced local variables
In Visual Studio 15.5, warning [C4189](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-4-c4189?view=msvc-170) is emitted in more cases, as shown in the following code:
C++
Copy
```
void f() {
    char s[2] = {0}; // C4189. Either use the variable or remove it.
}

```

Output
Copy
```
warning C4189: 's': local variable is initialized but not referenced

```

To fix the error, remove the unused variable.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#single-line-comments)
### Single-line comments
In Visual Studio 2017 version 15.5, warnings C4001 and C4179 are no longer emitted by the C compiler. Previously, they were only emitted under the **`/Za`**compiler switch. The warnings are no longer needed because single-line comments have been part of the C standard since C99.
C++
Copy
```
/* C only */
#pragma warning(disable:4001) // C4619
#pragma warning(disable:4179)
// single line comment
//* single line comment */

```

Output
Copy
```
warning C4619: #pragma warning: there is no warning number '4001'

```

When the code doesn't need to be backwards compatible, avoid the warning by removing the C4001 and C4179 suppression. If the code does need to be backward compatible, then suppress C4619 only.
C
Copy
```
/* C only */

#pragma warning(disable:4619)
#pragma warning(disable:4001)
#pragma warning(disable:4179)

// single line comment
/* single line comment */

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#__declspec-attributes-with-extern-c-linkage)
###  `__declspec` attributes with `extern "C"` linkage
In earlier versions of Visual Studio, the compiler ignored `__declspec(...)` attributes when `__declspec(...)` was applied before the `extern "C"` linkage specification. This behavior caused code to be generated that the user didn't intend, with possible runtime implications. The [C4768](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4768?view=msvc-170) warning was added in Visual Studio version 15.3, but was off by default. In Visual Studio 2017 version 15.5, the warning is enabled by default.
C++
Copy
```
__declspec(noinline) extern "C" HRESULT __stdcall // C4768

```

Output
Copy
```
warning C4768: __declspec attributes before linkage specification are ignored

```

To fix the error, place the linkage specification before the __declspec attribute:
C++
Copy
```
extern "C" __declspec(noinline) HRESULT __stdcall

```

This new warning C4768 is given on some Windows SDK headers that were shipped with Visual Studio 2017 15.3 or older (for example: version 10.0.15063.0, also known as RS2 SDK). However, later versions of Windows SDK headers (specifically, ShlObj.h and ShlObj_core.h) have been fixed so that they don't produce the warning. When you see this warning coming from Windows SDK headers, you can take these actions:
  1. Switch to the latest Windows SDK that came with Visual Studio 2017 version 15.5 release.
  2. Turn off the warning around the #include of the Windows SDK header statement:


C++
Copy
```
   #pragma warning (push)
   #pragma warning(disable:4768)
   #include <shlobj.h>
   #pragma warning (pop)

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#extern_linkage)
###  `extern constexpr` linkage
In earlier versions of Visual Studio, the compiler always gave a **`constexpr`**variable internal linkage even when the variable was marked**`extern`**. In Visual Studio 2017 version 15.5, a new compiler switch (**`/Zc:externConstexpr`**) enables correct, standards-conforming behavior. Eventually this behavior will become the default.
C++
Copy
```
extern constexpr int x = 10;

```

Output
Copy
```
error LNK2005: "int const x" already defined

```

If a header file contains a variable declared **`extern constexpr`**, it needs to be marked`__declspec(selectany)` to have its duplicate declarations combined correctly:
C++
Copy
```
extern constexpr __declspec(selectany) int x = 10;

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#typeid-cant-be-used-on-incomplete-class-type)
###  `typeid` can't be used on incomplete class type
In earlier versions of Visual Studio, the compiler incorrectly allowed the following code, resulting in potentially incorrect type information. In Visual Studio 2017 version 15.5, the compiler correctly raises an error:
C++
Copy
```
#include <typeinfo>

struct S;

void f() { typeid(S); } //C2027 in 15.5

```

Output
Copy
```
error C2027: use of undefined type 'S'

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#stdis_convertible-target-type)
###  `std::is_convertible` target type
`std::is_convertible` requires the target type to be a valid return type. In earlier versions of Visual Studio, the compiler incorrectly allowed abstract types, which might lead to incorrect overload resolution and unintended runtime behavior. The following code now correctly raises C2338:
C++
Copy
```
#include <type_traits>

struct B { virtual ~B() = 0; };
struct D : public B { virtual ~D(); };

static_assert(std::is_convertible<D, B>::value, "fail"); // C2338 in 15.5

```

To avoid the error, when using `is_convertible` you should compare pointer types because a non-pointer-type comparison might fail if one type is abstract:
C++
Copy
```
#include <type_traits>

struct B { virtual ~B() = 0; };
struct D : public B { virtual ~D(); };

static_assert(std::is_convertible<D *, B *>::value, "fail");

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#noexcept_removal)
###  Dynamic exception specification removal and `noexcept`
In C++17, `throw()` is an alias for **`noexcept`**,`throw(<type list>)` and `throw(...)` are removed, and certain types may include **`noexcept`**. This change can cause source compatibility issues with code that conforms to C++14 or earlier. The**`/Zc:noexceptTypes-`**switch can be used to revert to the C++14 version of**`noexcept`**while using C++17 mode in general. It enables you to update your source code to conform to C++17 without having to rewrite all your`throw()` code at the same time.
The compiler also now diagnoses more mismatched exception specifications in declarations in C++17 mode or with [`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170) with the new warning C5043.
The following code generates C5043 and C5040 in Visual Studio 2017 version 15.5 when the **`/std:c++17`**switch is applied:
C++
Copy
```
void f() throw(); // equivalent to void f() noexcept;
void f() {} // warning C5043
void g() throw(); // warning C5040

struct A {
    virtual void f() throw();
};

struct B : A {
    virtual void f() { } // error C2694
};

```

To remove the errors while still using **`/std:c++17`**, either add the**`/Zc:noexceptTypes-`**switch to the command line, or else update your code to use**`noexcept`**, as shown in the following example:
C++
Copy
```
void f() noexcept;
void f() noexcept { }
void g() noexcept(false);

struct A {
    virtual void f() noexcept;
};

struct B : A {
    virtual void f() noexcept { }
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#inline-variables)
### Inline variables
Static **`constexpr`**data members are now implicitly**`inline`**, which means that their declaration within a class is now their definition. Using an out-of-line definition for a**`static constexpr`**data member is redundant, and now deprecated. In Visual Studio 2017 version 15.5, when the**`/std:c++17`**switch is applied the following code now produces warning C5041:
C++
Copy
```
struct X {
    static constexpr int size = 3;
};
const int X::size; // C5041: 'size': out-of-line definition for constexpr static data member is not needed and is deprecated in C++17

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#extern-c-__declspec-warning-c4768-now-on-by-default)
###  `extern "C" __declspec(...)` warning C4768 now on by default
The warning was added in Visual Studio 2017 version 15.3, but was off by default. In Visual Studio 2017 version 15.5, the warning is on by default. For more information, see [New warning on `__declspec` attributes](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#declspec).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#defaulted-functions-and-__declspecnothrow)
### Defaulted functions and `__declspec(nothrow)`
The compiler previously allowed defaulted functions to be declared with `__declspec(nothrow)` when the corresponding base/member functions permitted exceptions. This behavior is contrary to the C++ standard and can cause undefined behavior at runtime. The standard requires such functions to be defined as deleted if there's an exception specification mismatch. Under **`/std:c++17`**, the following code raises C2280:
C++
Copy
```
struct A {
    A& operator=(const A& other) { // No exception specification; this function may throw.
        ...
    }
};

struct B : public A {
    __declspec(nothrow) B& operator=(const B& other) = default;
};

int main()
{
    B b1, b2;
    b2 = b1; // error C2280: attempting to reference a deleted function.
             // Function was implicitly deleted because the explicit exception
             // specification is incompatible with that of the implicit declaration.
}

```

To correct this code, either remove __declspec(nothrow) from the defaulted function, or remove `= default` and provide a definition for the function along with any required exception handling:
C++
Copy
```
struct A {
    A& operator=(const A& other) {
        // ...
    }
};

struct B : public A {
    B& operator=(const B& other) = default;
};

int main()
{
    B b1, b2;
    b2 = b1;
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#noexcept-and-partial-specializations)
###  `noexcept` and partial specializations
With **`noexcept`**in the type system, partial specializations for matching particular "callable" types may not compile, or fail to choose the primary template, because of a missing partial specialization for pointers-to-noexcept-functions.
In such cases, you may need to add more partial specializations to handle the **`noexcept`**function pointers and**`noexcept`**pointers to member functions. These overloads are only legal in**`/std:c++17`**mode or later. If backwards-compatibility with C++14 must be maintained, and you're writing code that others consume, then you should guard these new overloads inside`#ifdef` directives. If you're working in a self-contained module, then instead of using `#ifdef` guards you can just compile with the **`/Zc:noexceptTypes-`**switch.
The following code compiles under **`/std:c++14`**but fails under**`/std:c++17`**with error C2027:
C++
Copy
```
template <typename T> struct A;

template <>
struct A<void(*)()>
{
    static const bool value = true;
};

template <typename T>
bool g(T t)
{
    return A<T>::value;
}

void f() noexcept {}

int main()
{
    return g(&f) ? 0 : 1; // C2027: use of undefined type 'A<T>'
}

```

The following code succeeds under **`/std:c++17`**because the compiler chooses the new partial specialization`A<void (*)() noexcept>` :
C++
Copy
```
template <typename T> struct A;

template <>
struct A<void(*)()>
{
    static const bool value = true;
};

template <>
struct A<void(*)() noexcept>
{
    static const bool value = true;
};

template <typename T>
bool g(T t)
{
    return A<T>::value;
}

void f() noexcept {}

int main()
{
    return g(&f) ? 0 : 1; // OK
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#improvements_156)
