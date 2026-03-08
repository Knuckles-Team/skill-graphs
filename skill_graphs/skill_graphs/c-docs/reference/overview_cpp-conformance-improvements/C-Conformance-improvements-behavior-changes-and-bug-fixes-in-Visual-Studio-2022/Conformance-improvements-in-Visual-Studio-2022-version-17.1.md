##  Conformance improvements in Visual Studio 2022 version 17.1
Visual Studio 2022 version 17.1 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#detect-ill-formed-capture-default-in-nonlocal-lambda-expressions)
### Detect ill-formed capture default in nonlocal lambda-expressions
The C++ Standard only allows a lambda expression in block scope to have a capture-default. In Visual Studio 2022 version 17.1 and later, the compiler detects when a capture default isn't allowed in a nonlocal lambda expression. It emits a new level 4 warning, C5253.
This change is a source breaking change. It applies in any mode that uses the new lambda processor: **`/Zc:lambda`**,**`/std:c++20`**, or**`/std:c++latest`**.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-6)
#### Example
In Visual Studio 2022 version 17.1 this code now emits an error:
C++
Copy
```
#pragma warning(error:5253)

auto incr = [=](int value) { return value + 1; };

// capture_default.cpp(3,14): error C5253: a nonlocal lambda cannot have a capture default
// auto incr = [=](int value) { return value + 1; };
//              ^

```

To fix this issue, remove the capture default:
C++
Copy
```
#pragma warning(error:5253)

auto incr = [](int value) { return value + 1; };

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#c4028-is-now-c4133-for-function-to-pointer-operations)
### C4028 is now C4133 for function-to-pointer operations
Before Visual Studio 2022 version 17.1, the compiler reported an incorrect error message on certain pointer-to-function comparisons in C code. The incorrect message was reported when you compared two function pointers that had the same argument counts but incompatible types. Now, we issue a different warning that complains about pointer-to-function incompatibility rather than function parameter mismatch.
This change is a source breaking change. It applies when code is compiled as C.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-7)
#### Example
C
Copy
```
int f1(int);
int f2(char*);
int main(void)
{
    return (f1 == f2);
}
// Old warning:
// C4028: formal parameter 1 different from declaration
// New warning:
// C4113: 'int (__cdecl *)(char *)' differs in parameter lists from 'int (__cdecl *)(int)'

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#error-on-a-nondependent-static_assert)
### Error on a nondependent `static_assert`
In Visual Studio 2022 version 17.1 and later, if the expression associated with a `static_assert` isn't a dependent expression, the compiler evaluates the expression when it's parsed. If the expression evaluates to `false`, the compiler emits an error. Previously, if the `static_assert` was within the body of a function template (or within the body of a member function of a class template), the compiler wouldn't perform this analysis.
This change is a source breaking change. It applies in any mode that implies **`/permissive-`**or**`/Zc:static_assert`**. This change in behavior can be disabled by using the**`/Zc:static_assert-`**compiler option.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#example-8)
#### Example
In Visual Studio 2022 version 17.1 and later, this code now causes an error:
C++
Copy
```
template<typename T>
void f()
{
   static_assert(false, "BOOM!");
}

```

To fix this issue, make the expression dependent. For example:
C++
Copy
```
template<typename>
constexpr bool dependent_false = false;

template<typename T>
void f()
{
   static_assert(dependent_false<T>, "BOOM!");
}

```

With this change, the compiler only emits an error if the function template `f` is instantiated.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_170)
