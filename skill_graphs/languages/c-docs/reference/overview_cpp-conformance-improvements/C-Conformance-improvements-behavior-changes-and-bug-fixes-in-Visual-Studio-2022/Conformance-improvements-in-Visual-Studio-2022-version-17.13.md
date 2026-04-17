##  Conformance improvements in Visual Studio 2022 version 17.13
Visual Studio 2022 version 17.13 includes the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
For an in-depth summary of changes made to the Standard Template Library, including conformance changes, bug fixes, and performance improvements, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#argument-dependent-lookup-adl)
### Argument-dependent lookup (ADL)
Language constructs such as range-for and structured bindings have special argument-dependent lookup rules for certain identifiers such as `begin`, `end`, or `get`. Previously, this lookup included candidates from the `std` namespace, even when namespace `std` isn't part of the ordinary set of associated namespaces for argument-dependent lookup.
Programs that introduced declarations to `std` for these constructs no longer compile. Instead, the declarations should be in a normal associated namespace for the types involved (possibly including the global namespace).
C++
Copy
```
template <typename T>
struct Foo {};

namespace std
{
    // To correct the program, move these declarations from std to the global namespace
    template <typename T>
    T* begin(Foo<T>& f);
    template <typename T>
    T* end(Foo<T>& f);
}

void f(Foo<int> foo)
{
   for (auto x : foo) // Previously compiled. Now emits error C3312: no callable 'begin' function found for type 'Foo<int>'
   {
      ...
   }
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#cant-modify-implementation-reserved-macros)
### Can't modify implementation-reserved macros
Previously, the compiler permitted changing or undefining certain implementation-provided macros such as `_MSC_EXTENSIONS`. Altering the definition of certain macros can result in undefined behavior.
Attempting to alter or undefine certain reserved macro names now results in the level-1 warning `C5308`. In `/permissive-` mode, this warning is treated as an error.
C++
Copy
```
#undef _MSC_EXTENSIONS // Warning C5308: Modifying reserved macro name `_MSC_EXTENSIONS` may cause undefined behavior

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_1712)
