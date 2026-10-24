##  Conformance improvements in Visual Studio 2017 RTW (version 15.0)
With support for generalized **`constexpr`**and non-static data member initialization (NSDMI) for aggregates, the MSVC compiler in Visual Studio 2017 is now complete for features added in the C++14 standard. However, the compiler still lacks a few features from the C++11 and C++98 standards. See[Microsoft C/C++ language conformance](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170) for the current state of the compiler.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c11-expression-sfinae-support-in-more-libraries)
### C++11: Expression SFINAE support in more libraries
The compiler continues to improve its support for expression SFINAE. It's required for template argument deduction and substitution where **`decltype`**and**`constexpr`**expressions may appear as template parameters. For more information, see[Expression SFINAE improvements in Visual Studio 2017 RC](https://devblogs.microsoft.com/cppblog/expression-sfinae-improvements-in-vs-2015-update-3/).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c14-nsdmi-for-aggregates)
### C++14: NSDMI for aggregates
An _aggregate_ is an array or a class that has: no user-provided constructor, no non-static data members that are private or protected, no base classes, and no virtual functions. Beginning in C++14, aggregates may contain member initializers. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c14-extended-constexpr)
### C++14: Extended `constexpr`
Expressions declared as **`constexpr`**are now allowed to contain certain kinds of declarations, if and switch statements, loop statements, and mutation of objects whose lifetime began within the**`constexpr`**expression evaluation. There's no longer a requirement that a**`constexpr`**non-static member function must be implicitly**`const`**. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-terse-static_assert)
### C++17: Terse `static_assert`
the message parameter for **`static_assert`**is optional. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c17-fallthrough-attribute)
### C++17: `[[fallthrough]]` attribute
In **`/std:c++17`**mode and later, the`[[fallthrough]]` attribute can be used in the context of switch statements as a hint to the compiler that the fall-through behavior is intended. This attribute prevents the compiler from issuing warnings in such cases. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#generalized-range-based-for-loops)
### Generalized range-based `for` loops
Range-based `for` loops no longer require that `begin()` and `end()` return objects of the same type. This change enables `end()` to return a sentinel as used by ranges in
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#copy-list-initialization)
### Copy-list-initialization
Visual Studio 2017 correctly raises compiler errors related to object creation using initializer lists. These errors weren't caught in Visual Studio 2015, and could lead to crashes or undefined runtime behavior. As per _`copy-list-initialization`_, the compiler is required to consider an explicit constructor for overload resolution. However, it must raise an error if that particular overload gets chosen.
The following two examples compile in Visual Studio 2015 but not in Visual Studio 2017.
C++
Copy
```
struct A
{
    explicit A(int) {}
    A(double) {}
};

int main()
{
    A a1 = { 1 }; // error C3445: copy-list-initialization of 'A' cannot use an explicit constructor
    const A& a2 = { 1 }; // error C2440: 'initializing': cannot convert from 'int' to 'const A &'

}

```

To correct the error, use direct initialization:
C++
Copy
```
A a1{ 1 };
const A& a2{ 1 };

```

In Visual Studio 2015, the compiler erroneously treated copy-list-initialization in the same way as regular copy-initialization: it considered only converting constructors for overload resolution. In the following example, Visual Studio 2015 chooses `MyInt(23)`. Visual Studio 2017 correctly raises the error.
C++
Copy
```
// From https://www.open-std.org/jtc1/sc22/wg21/docs/cwg_closed.html#1228
struct MyStore {
    explicit MyStore(int initialCapacity);
};

struct MyInt {
    MyInt(int i);
};

struct Printer {
    void operator()(MyStore const& s);
    void operator()(MyInt const& i);
};

void f() {
    Printer p;
    p({ 23 }); // C3066: there are multiple ways that an object
        // of this type can be called with these arguments
}

```

This example is similar to the previous one but raises a different error. It succeeds in Visual Studio 2015 and fails in Visual Studio 2017 with [C2668](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c2668?view=msvc-170).
C++
Copy
```
struct A {
    explicit A(int) {}
};

struct B {
    B(int) {}
};

void f(const A&) {}
void f(const B&) {}

int main()
{
    f({ 1 }); // error C2668: 'f': ambiguous call to overloaded function
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#deprecated-typedefs)
### Deprecated typedefs
Visual Studio 2017 now issues the correct warning for deprecated typedefs declared in a class or struct. The following example compiles without warnings in Visual Studio 2015. It produces [C4996](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-3-c4996?view=msvc-170) in Visual Studio 2017.
C++
Copy
```
struct A
{
    // also for __declspec(deprecated)
    [[deprecated]] typedef int inttype;
};

int main()
{
    A::inttype a = 0; // C4996 'A::inttype': was declared deprecated
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#constexpr)
### `constexpr`
Visual Studio 2017 correctly raises an error when the left-hand operand of a conditionally evaluating operation isn't valid in a `constexpr` context. The following code compiles in Visual Studio 2015, but not in Visual Studio 2017, where it raises [C3615](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c3615?view=msvc-170):
C++
Copy
```
template<int N>
struct array
{
    int size() const { return N; }
};

constexpr bool f(const array<1> &arr)
{
    return arr.size() == 10 || arr.size() == 11; // C3615 constexpr function 'f' cannot result in a constant expression
}

```

To correct the error, either declare the `array::size()` function as **`constexpr`**or remove the**`constexpr`**qualifier from`f`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#class-types-passed-to-variadic-functions)
### Class types passed to variadic functions
In Visual Studio 2017, classes or structs that are passed to a variadic function such as `printf` must be trivially copyable. When such objects are passed, the compiler simply makes a bitwise copy and doesn't call the constructor or destructor.
C++
Copy
```
#include <atomic>
#include <memory>
#include <stdio.h>

int main()
{
    std::atomic<int> i(0);
    printf("%i\n", i); // error C4839: non-standard use of class 'std::atomic<int>'
                        // as an argument to a variadic function.
                        // note: the constructor and destructor will not be called;
                        // a bitwise copy of the class will be passed as the argument
                        // error C2280: 'std::atomic<int>::atomic(const std::atomic<int> &)':
                        // attempting to reference a deleted function

    struct S {
        S(int i) : i(i) {}
        S(const S& other) : i(other.i) {}
        operator int() { return i; }
    private:
        int i;
    } s(0);
    printf("%i\n", s); // warning C4840 : non-portable use of class 'main::S'
                      // as an argument to a variadic function
}

```

To correct the error, you can call a member function that returns a trivially copyable type,
C++
Copy
```
    std::atomic<int> i(0);
    printf("%i\n", i.load());

```

or else use a static cast to convert the object before passing it:
C++
Copy
```
    struct S {/* as before */} s(0);
    printf("%i\n", static_cast<int>(s))

```

For strings built and managed using `CString`, the provided `operator LPCTSTR()` should be used to cast a `CString` object to the C pointer expected by the format string.
C++
Copy
```
CString str1;
CString str2 = _T("hello!");
str1.Format(_T("%s"), static_cast<LPCTSTR>(str2));

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#cv-qualifiers-in-class-construction)
### Cv-qualifiers in class construction
In Visual Studio 2015, the compiler sometimes incorrectly ignores the cv-qualifier when generating a class object via a constructor call. This issue can potentially cause a crash or unexpected runtime behavior. The following example compiles in Visual Studio 2015 but raises a compiler error in Visual Studio 2017:
C++
Copy
```
struct S
{
    S(int);
    operator int();
};

int i = (const S)0; // error C2440

```

To correct the error, declare `operator int()` as **`const`**.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#access-checking-on-qualified-names-in-templates)
### Access checking on qualified names in templates
Previous versions of the compiler didn't check access to qualified names in some template contexts. This issue can interfere with expected SFINAE behavior, where the substitution is expected to fail because of the inaccessibility of a name. It could have potentially caused a crash or unexpected behavior at runtime, because the compiler incorrectly called the wrong overload of the operator. In Visual Studio 2017, a compiler error is raised. The specific error might vary, but a typical error is [C2672](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c2672?view=msvc-170), "no matching overloaded function found." The following code compiles in Visual Studio 2015 but raises an error in Visual Studio 2017:
C++
Copy
```
#include <type_traits>

template <class T> class S {
    typedef typename T type;
};

template <class T, std::enable_if<std::is_integral<typename S<T>::type>::value, T> * = 0>
bool f(T x);

int main()
{
    f(10); // C2672: No matching overloaded function found.
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#missing-template-argument-lists)
### Missing template argument lists
In Visual Studio 2015 and earlier, the compiler didn't diagnose all missing template argument lists. It wouldn't note when the missing template appeared in a template parameter list: for example, when part of a default template argument or a non-type template parameter was missing. This issue can result in unpredictable behavior, including compiler crashes or unexpected runtime behavior. The following code compiles in Visual Studio 2015, but produces an error in Visual Studio 2017.
C++
Copy
```
template <class T> class ListNode;
template <class T> using ListNodeMember = ListNode<T> T::*;
template <class T, ListNodeMember M> class ListHead; // C2955: 'ListNodeMember': use of alias
                                                     // template requires template argument list

// correct:  template <class T, ListNodeMember<T> M> class ListHead;

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#expression-sfinae)
### Expression-SFINAE
To support expression-SFINAE, the compiler now parses **`decltype`**arguments when the templates are declared rather than instantiated. So, if a non-dependent specialization is found in the**`decltype`**argument, it's not deferred until instantiation-time. It's processed immediately, and any resulting errors are diagnosed at that time.
The following example shows such a compiler error that is raised at the point of declaration:
C++
Copy
```
#include <utility>
template <class T, class ReturnT, class... ArgsT>
class IsCallable
{
public:
    struct BadType {};

    template <class U>
    static decltype(std::declval<T>()(std::declval<ArgsT>()...)) Test(int); //C2064. Should be declval<U>

    template <class U>
    static BadType Test(...);

    static constexpr bool value = std::is_convertible<decltype(Test<T>(0)), ReturnT>::value;
};

constexpr bool test1 = IsCallable<int(), int>::value;
static_assert(test1, "PASS1");
constexpr bool test2 = !IsCallable<int*, int>::value;
static_assert(test2, "PASS2");

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#classes-declared-in-anonymous-namespaces)
### Classes declared in anonymous namespaces
According to the C++ standard, a class declared inside an anonymous namespace has internal linkage, and that means it can't be exported. In Visual Studio 2015 and earlier, this rule wasn't enforced. In Visual Studio 2017, the rule is partially enforced. In Visual Studio 2017 the following example raises error [C2201](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2201?view=msvc-170):
C++
Copy
```
struct __declspec(dllexport) S1 { virtual void f() {} };
  // C2201 const anonymous namespace::S1::vftable: must have external linkage
  // in order to be exported/imported.

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#default-initializers-for-value-class-members-ccli)
### Default initializers for value class members (C++/CLI)
In Visual Studio 2015 and earlier, the compiler permitted (but ignored) a default member initializer for a member of a value class. Default initialization of a value class always zero-initializes the members. A default constructor isn't permitted. In Visual Studio 2017, default member initializers raise a compiler error, as shown in this example:
C++
Copy
```
value struct V
{
    int i = 0; // error C3446: 'V::i': a default member initializer
               // isn't allowed for a member of a value class
};

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#default-indexers-ccli)
### Default indexers (C++/CLI)
In Visual Studio 2015 and earlier, the compiler in some cases misidentified a default property as a default indexer. It was possible to work around the issue by using the identifier **`default`**to access the property. The workaround itself became problematic after**`default`**was introduced as a keyword in C++11. In Visual Studio 2017, the bugs that required the workaround were fixed. The compiler now raises an error when**`default`**is used to access the default property for a class.
C++
Copy
```
//class1.cs

using System.Reflection;
using System.Runtime.InteropServices;

namespace ClassLibrary1
{
    [DefaultMember("Value")]
    public class Class1
    {
        public int Value
        {
            // using attribute on the return type triggers the compiler bug
            [return: MarshalAs(UnmanagedType.I4)]
            get;
        }
    }
    [DefaultMember("Value")]
    public class Class2
    {
        public int Value
        {
            get;
        }
    }
}

// code.cpp
#using "class1.dll"

void f(ClassLibrary1::Class1 ^r1, ClassLibrary1::Class2 ^r2)
{
       r1->Value; // error
       r1->default;
       r2->Value;
       r2->default; // error
}

```

In Visual Studio 2017, you can access both Value properties by their name:
C++
Copy
```
#using "class1.dll"

void f(ClassLibrary1::Class1 ^r1, ClassLibrary1::Class2 ^r2)
{
       r1->Value;
       r2->Value;
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#improvements_153)
