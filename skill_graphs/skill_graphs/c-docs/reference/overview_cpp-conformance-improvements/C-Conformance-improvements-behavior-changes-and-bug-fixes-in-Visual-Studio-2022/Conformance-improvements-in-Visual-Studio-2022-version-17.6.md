##  Conformance improvements in Visual Studio 2022 version 17.6
Visual Studio 2022 version 17.6 contains the following conformance improvements, bug fixes, and behavior changes in the Microsoft C/C++ compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#compound-volatile-assignments-no-longer-deprecated)
### Compound `volatile` assignments no longer deprecated
C++20 deprecated applying certain operators to types qualified with `volatile`. For example, when the following code is compiled with `cl /std:c++20 /Wall test.cpp`:
C++
Copy
```
void f(volatile int& expr)
{
   ++expr;
}

```

The compiler produces `test.cpp(3): warning C5214: applying '++' to an operand with a volatile qualified type is deprecated in C++20`.
In C++20, compound assignment operators (operators of the form `@=`) were deprecated. In C++23, compound operators excluded in C++20 are no longer deprecated. For example, in C++23 the following code doesn't produce a warning, whereas it does in C++20:
C++
Copy
```
void f(volatile int& e1, int e2)
{
   e1 += e2;
}

```

For more information about this change, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#rewriting-equality-in-expressions-is-less-of-a-breaking-change-p2468r2)
### Rewriting equality in expressions is less of a breaking change (P2468R2)
In C++20,
C++
Copy
```
struct S
{
    bool operator==(const S&);
    bool operator!=(const S&);
};
bool b = S{} != S{};

```

The compiler accepts this code, which means that the compiler is more strict with code such as:
C++
Copy
```
struct S
{
  operator bool() const;
  bool operator==(const S&);
};

bool b = S{} == S{};

```

Version 17.5 of the compiler accepts this program. Version 17.6 of the compiler rejects it. To fix it, add `const` to `operator==` to remove the ambiguity. Or, add a corresponding `operator!=` to the definition as shown in the following example:
C++
Copy
```
struct S
{
  operator bool() const;
  bool operator==(const S&);
  bool operator!=(const S&);
};

bool b = S{} == S{};

```

Microsoft C/C++ compiler versions 17.5 and 17.6 accept the previous program, and calls `S::operator==` in both versions.
The general programming model outlined in P2468R2 is that if there's a corresponding `operator!=` for a type, it typically suppresses the rewrite behavior. Adding a corresponding `operator!=` is the suggested fix for code that previously compiled in C++17. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements?view=msvc-170#improvements_174)
