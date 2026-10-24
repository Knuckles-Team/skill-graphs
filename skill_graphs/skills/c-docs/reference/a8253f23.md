##  Conformance improvements in Visual Studio 2022 version 17.12
Visual Studio 2022 version 17.12 includes the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
For an in-depth summary of changes made to the Standard Template Library, including conformance changes, bug fixes, and performance improvements, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#_com_ptr_toperator-bool-is-now-explicit)
###  `_com_ptr_t::operator bool()` is now explicit
This is a source/binary breaking change.
The implicit conversion to `bool` from `_com_ptr_t` instances can be surprising or lead to compiler errors. `_com_ptr_t` contained implicit conversions to both `bool` and `Interface*`. These two implicit conversions can lead to ambiguities.
To address this, the conversion to `bool` is now explicit. The conversion to `Interface*` is unchanged.
A macro is provided to opt-out of this new behavior and restore the previous implicit conversion. Compile with `/D_COM_DISABLE_EXPLICIT_OPERATOR_BOOL` to opt-out of this change. We recommend that you modify the code to not rely on implicit conversions.
For example:
C++
Copy
```
#include <comip.h>

template<class Iface>
using _com_ptr = _com_ptr_t<_com_IIID<Iface, &__uuidof(Iface)>>;

int main()
{
   _com_ptr<IUnknown> unk;
   if (unk) // Still valid
   {
      // ...
   }
   bool b = unk; // Still valid.
   int v = unk; // Previously permitted, now emits C2240: cannot convert from '_com_ptr_t<_com_IIID<IUnknown,& _GUID_00000000_0000_0000_c000_000000000046>>' to 'int'
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#constant-expressions-are-no-longer-always-noexcept-in-permissive-mode)
### Constant expressions are no longer always `noexcept` in permissive mode
This is a source/binary breaking change.
A constant expression was always `noexcept`, even if it involved a function call to a function declared with a potentially throwing exception specification. This wording was removed in C++17, although the Microsoft Visual C++ compiler still supported it in `/permissive` mode in all C++ language versions.
This `/permissive` mode behavior is removed. Constant expressions are no longer given special implicit behavior.
The `noexcept` specifier on `constexpr` functions is now respected in all modes. This change is required for correct implementation of later core issue resolutions that rely on the standard `noexcept` behavior.
For example:
C++
Copy
```
constexpr int f(bool b) noexcept(false)
{
    if (b)
    {
        throw 1;
    }
    else
    {
        return 1;
    }
}

void g(bool b)
{
   noexcept(f(b)); // false. No change to behavior
   noexcept(f(true)); // false. No change to behavior
   noexcept(f(false)); // false. Was true in /permissive mode only in previous versions.
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1711)
