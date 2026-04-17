##  Conformance improvements in Visual Studio 2022 version 17.14
Visual Studio 2022 version 17.14 includes the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#conformance-improvements)
### Conformance improvements
  * Standard library hardening ([__fastfail](https://learn.microsoft.com/en-us/cpp/intrinsics/fastfail?view=msvc-170). Off by default. Define `_MSVC_STL_HARDENING=1` project-wide to enable.


[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#enhanced-behavior)
### Enhanced behavior
  * Implemented "destructor tombstones" to mitigate use-after-free mistakes. Off by default. Define `_MSVC_STL_DESTRUCTOR_TOMBSTONES=1` project-wide to enable.


[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#bug-fixes)
### Bug fixes
  * Fixed errant compiler errors when using `<format>` in a CUDA project.
  * Fixed a compiler issue where the address of a local variable could "leak" during `constexpr` evaluation. For example:
C++
Copy
```
const unsigned & func()
{
  const int x = 0;
  constexpr const unsigned & r1 = x; // Previously accepted, now an error
  return r1;
}

auto r = func();  // Previously, the local address leaked

```

**Example #2**
C++
Copy
```
#include <initializer_list>

void test()
{
    constexpr std::initializer_list<int> xs { 1, 2, 3 };        // Previously accepted, now an error

    static constexpr std::initializer_list<int> ys { 1, 2, 3 }; // Correct usage - note use of static
}

```

  * Code compiled with `/permissive-` no longer accepts a combination of `friend` and `static` on a declaration. The fix is usually to remove `static` from the declaration. For example:
C++
Copy
```
struct S
{
    friend static void f(); // Previously accepted, now emits error C2440: 'static' cannot be used with 'friend'
};

```

  * Reference binding to volatile-qualified types fixed when referring to a base or derived class. For example:
C++
Copy
```
struct A {};
struct B : public A {};

void f(A&);                 // 1
void f(const volatile A&);  // 2

f(B{}); // Previously called 2. This is ill-formed under /permissive- or /Zc:referenceBinding. Chooses 1 if relaxed reference binding rules are enabled.

```



For an in-depth summary of changes made to the Standard Template Library, including conformance changes, bug fixes, and performance improvements, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1713)
