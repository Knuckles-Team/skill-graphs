##  Conformance improvements in Visual Studio 2022 version 17.7
Visual Studio 2022 version 17.7 contains the following highlighted conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#added-stdclatest-to-the-c-compiler)
### Added `/std:clatest` to the C compiler
This switch behaves like the `/std:c++latest` switch for the C++ compiler. The switch enables all currently implemented compiler and standard library features proposed for the next draft C standard, as well as some in-progress and experimental features.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#c-standard-library-2)
### C++ Standard Library
The `<print>` library is now supported. See
Implemented `views::cartesian_product`.
For a broader summary of changes made to the Standard Template Library, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#using-conformance)
###  `using` conformance
Previously, the `using` directive could cause names from used namespaces to remain visible when they shouldn't. This could cause unqualified name lookup to find a name in a namespace even when there's no `using` directive active.
Here are some examples of the new and old behavior.
References in the following comments to "(1)" mean the call to `f<K>(t)` in namespace `A`:
C++
Copy
```
namespace A
{
    template<typename K, typename T>
    auto f2(T t)
    {
        return f<K>(t); // (1) Unqualified lookup should not find anything
    }
}

namespace B
{
    template<typename K, typename T>
    auto f(T t) noexcept
    { // Previous behavior: This function was erroneously found during unqualified lookup at (1)
        return A::f2<K>(t);
    }
}

namespace C
{
    template<typename T>
    struct S {};

    template<typename, typename U>
    U&& f(U&&) noexcept; // New behavior: ADL at (1) correctly finds this function
}

namespace D
{
    using namespace B;

    void h()
    {
        D::f<void>(C::S<int>());
    }
}

```

The same underlying issue can cause code that previously compiled to now be rejected:
C++
Copy
```
#include <memory>
namespace Addin {}
namespace Gui
{
    using namespace Addin;
}

namespace Addin
{
    using namespace std;
}

// This previously compiled, but now emits error C2065 for undeclared name 'allocator'.
// This should be declared as 'std::allocator<T*>' because the using directive nominating
// 'std' is not active at this point.
template <class T, class U = allocator<T*>>
class resource_list
{
};

namespace Gui
{
    typedef resource_list<int> intlist;
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_176)
