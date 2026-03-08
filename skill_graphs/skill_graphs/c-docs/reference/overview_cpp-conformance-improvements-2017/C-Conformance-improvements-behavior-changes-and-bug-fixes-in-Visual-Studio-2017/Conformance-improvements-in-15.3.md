##  Conformance improvements in 15.3
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#constexpr-lambdas)
###  `constexpr` lambdas
Lambda expressions may now be used in constant expressions. For more information, see [`constexpr` lambda expressions in C++](https://learn.microsoft.com/en-us/cpp/cpp/lambda-expressions-constexpr?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#if-constexpr-in-function-templates)
###  `if constexpr` in function templates
A function template may contain **`if constexpr`**statements to enable compile-time branching. For more information, see[`if constexpr` statements](https://learn.microsoft.com/en-us/cpp/cpp/if-else-statement-cpp?view=msvc-170#if_constexpr).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#selection-statements-with-initializers)
### Selection statements with initializers
An **`if`**statement may include an initializer that introduces a variable at block scope within the statement itself. For more information, see[`if` statements with initializer](https://learn.microsoft.com/en-us/cpp/cpp/if-else-statement-cpp?view=msvc-170#if_with_init).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#maybe_unused-and-nodiscard-attributes)
###  `[[maybe_unused]]` and `[[nodiscard]]` attributes
New attribute `[[maybe_unused]]` silences warnings when an entity isn't used. The `[[nodiscard]]` attribute creates a warning if the return value of a function call is discarded. For more information, see [Attributes in C++](https://learn.microsoft.com/en-us/cpp/cpp/attributes?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#using-attribute-namespaces-without-repetition)
### Using attribute namespaces without repetition
New syntax to enable only a single namespace identifier in an attribute list. For more information, see [Attributes in C++](https://learn.microsoft.com/en-us/cpp/cpp/attributes?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#structured-bindings)
### Structured bindings
It's now possible in a single declaration to store a value with individual names for its components, when the value is an array, a `std::tuple` or `std::pair`, or has all public non-static data members. For more information, see [Returning multiple values from a function](https://learn.microsoft.com/en-us/cpp/cpp/functions-cpp?view=msvc-170#multi_val).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#construction-rules-for-enum-class-values)
### Construction rules for `enum class` values
There's now an implicit conversion for scoped enumerations that's non-narrowing. It converts from a scoped enumeration's underlying type to the enumeration itself. The conversion is available when its definition doesn't introduce an enumerator, and when the source uses a list-initialization syntax. For more information, see [Enumerations](https://learn.microsoft.com/en-us/cpp/cpp/enumerations-cpp?view=msvc-170#no_enumerators).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#capturing-this-by-value)
### Capturing `*this` by value
The **`*this`**object in a lambda expression may now be captured by value. This change enables scenarios in which the lambda is invoked in parallel and asynchronous operations, especially on newer machine architectures. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#removing-operator-for-bool)
### Removing `operator++` for `bool`
`operator++` is no longer supported on **`bool`**types. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#removing-deprecated-register-keyword)
### Removing deprecated `register` keyword
The **`register`**keyword, previously deprecated (and ignored by the compiler), is now removed from the language. For more information, see
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#calls-to-deleted-member-templates)
### Calls to deleted member templates
In previous versions of Visual Studio, the compiler in some cases would fail to emit an error for ill-formed calls to a deleted member template. These calls would potentially cause crashes at runtime. The following code now produces [C2280](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2280?view=msvc-170):
C++
Copy
```
template<typename T>
struct S {
   template<typename U> static int f() = delete;
};

void g()
{
   decltype(S<int>::f<int>()) i; // this should fail with
// C2280: 'int S<int>::f<int>(void)': attempting to reference a deleted function
}

```

To fix the error, declare `i` as **`int`**.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#pre-condition-checks-for-type-traits)
### Pre-condition checks for type traits
Visual Studio 2017 version 15.3 improves pre-condition checks for type-traits to more strictly follow the standard. One such check is for assignable. The following code produces [C2139](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2139?view=msvc-170) in Visual Studio 2017 version 15.3:
C++
Copy
```
struct S;
enum E;

static_assert(!__is_assignable(S, S), "fail"); // C2139 in 15.3
static_assert(__is_convertible_to(E, E), "fail"); // C2139 in 15.3

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#new-compiler-warning-and-runtime-checks-on-native-to-managed-marshaling)
### New compiler warning and runtime checks on native-to-managed marshaling
Calling from managed functions to native functions requires marshaling. The CLR does the marshaling, but it doesn't understand C++ semantics. If you pass a native object by value, CLR either calls the object's copy-constructor or uses `BitBlt`, which may cause undefined behavior at runtime.
Now the compiler emits a warning if it finds this error at compile time: a native object with deleted copy ctor gets passed between a native and managed boundary by value. For those cases in which the compiler doesn't know at compile time, it injects a runtime check so that the program calls `std::terminate` immediately when an ill-formed marshaling occurs. In Visual Studio 2017 version 15.3, the following code produces warning [C4606](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-1-c4606?view=msvc-170):
C++
Copy
```
class A
{
public:
   A() : p_(new int) {}
   ~A() { delete p_; }

   A(A const &) = delete;
   A(A &&rhs) {
   p_ = rhs.p_;
}

private:
   int *p_;
};

#pragma unmanaged

void f(A a)
{
}

#pragma managed

int main()
{
    // This call from managed to native requires marshaling. The CLR doesn't
    // understand C++ and uses BitBlt, which results in a double-free later.
    f(A()); // C4606 'A': passing argument by value across native and managed
    // boundary requires valid copy constructor. Otherwise, the runtime
    // behavior is undefined.
}

```

To fix the error, remove the `#pragma managed` directive to mark the caller as native and avoid marshaling.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#experimental-api-warning-for-winrt)
### Experimental API warning for WinRT
WinRT APIs that are released for experimentation and feedback are decorated with `Windows.Foundation.Metadata.ExperimentalAttribute`. In Visual Studio 2017 version 15.3, the compiler produces warning [C4698](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4698?view=msvc-170) for this attribute. A few APIs in previous versions of the Windows SDK have already been decorated with the attribute, and calls to these APIs now trigger this compiler warning. Newer Windows SDKs have the attribute removed from all shipped types. If you're using an older SDK, you'll need to suppress these warnings for all calls to shipped types.
The following code produces warning C4698:
C++
Copy
```
Windows::Storage::IApplicationDataStatics2::GetForUserAsync(); // C4698
// 'Windows::Storage::IApplicationDataStatics2::GetForUserAsync' is for
// evaluation purposes only and is subject to change or removal in future updates

```

To disable the warning, add a #pragma:
C++
Copy
```
#pragma warning(push)
#pragma warning(disable:4698)

Windows::Storage::IApplicationDataStatics2::GetForUserAsync();

#pragma warning(pop)

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#out-of-line-definition-of-a-template-member-function)
### Out-of-line definition of a template member function
Visual Studio 2017 version 15.3 produces an error for an out-of-line definition of a template member function that wasn't declared in the class. The following code now produces error [C2039](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2039?view=msvc-170):
C++
Copy
```
struct S {};

template <typename T>
void S::f(T t) {} // C2039: 'f': is not a member of 'S'

```

To fix the error, add a declaration to the class:
C++
Copy
```
struct S {
    template <typename T>
    void f(T t);
};
template <typename T>
void S::f(T t) {}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#attempting-to-take-the-address-of-this-pointer)
### Attempting to take the address of `this` pointer
In C++, **`this`**is a prvalue of type pointer to X. You can't take the address of**`this`**or bind it to an lvalue reference. In previous versions of Visual Studio, the compiler would allow you to circumvent this restriction by use of a cast. In Visual Studio 2017 version 15.3, the compiler produces error[C2664](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c2664?view=msvc-170).
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#conversion-to-an-inaccessible-base-class)
### Conversion to an inaccessible base class
Visual Studio 2017 version 15.3 produces an error when you attempt to convert a type to a base class that is inaccessible. The following code is ill-formed and can potentially cause a crash at runtime. The compiler now produces [C2243](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2243?view=msvc-170) when it sees code like this:
C++
Copy
```
#include <memory>

class B { };
class D : B { }; // C2243: 'type cast': conversion from 'D *' to 'B *' exists, but is inaccessible

void f()
{
   std::unique_ptr<B>(new D());
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#default-arguments-arent-allowed-on-out-of-line-definitions-of-member-functions)
### Default arguments aren't allowed on out of line definitions of member functions
Default arguments aren't allowed on out-of-line definitions of member functions in template classes. The compiler will issue a warning under **`/permissive`**, and a hard error under[`/permissive-`](https://learn.microsoft.com/en-us/cpp/build/reference/permissive-standards-conformance?view=msvc-170).
In previous versions of Visual Studio, the following ill-formed code could potentially cause a runtime crash. Visual Studio 2017 version 15.3 produces warning [C5037](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c5037?view=msvc-170):
C++
Copy
```
template <typename T>
struct A {
    T f(T t, bool b = false);
};

template <typename T>
T A<T>::f(T t, bool b = false) // C5037: 'A<T>::f': an out-of-line definition of a member of a class template cannot have default arguments
{
    // ...
}

```

To fix the error, remove the `= false` default argument.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#use-of-offsetof-with-compound-member-designator)
### Use of `offsetof` with compound member designator
In Visual Studio 2017 version 15.3, using `offsetof(T, m)` where _m_ is a "compound member designator" results in a warning when you compile with the **`/Wall`**option. The following code is ill-formed and could potentially cause a crash at runtime. Visual Studio 2017 version 15.3 produces warning[C4841](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4841?view=msvc-170):
C++
Copy
```
struct A {
   int arr[10];
};

// warning C4841: non-standard extension used: compound member designator used in offsetof
constexpr auto off = offsetof(A, arr[2]);

```

To fix the code, either disable the warning with a pragma or change the code to not use `offsetof`:
C++
Copy
```
#pragma warning(push)
#pragma warning(disable: 4841)
constexpr auto off = offsetof(A, arr[2]);
#pragma warning(pop)

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#using-offsetof-with-static-data-member-or-member-function)
### Using `offsetof` with static data member or member function
In Visual Studio 2017 version 15.3, using `offsetof(T, m)` where _m_ refers to a static data member or a member function results in an error. The following code produces error [C4597](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4597?view=msvc-170):
C++
Copy
```
#include <cstddef>

struct A {
   int ten() { return 10; }
   static constexpr int two = 2;
};

constexpr auto off = offsetof(A, ten);  // C4597: undefined behavior: offsetof applied to member function 'A::ten'
constexpr auto off2 = offsetof(A, two); // C4597: undefined behavior: offsetof applied to static data member 'A::two'

```

This code is ill-formed and could potentially cause a crash at runtime. To fix the error, change the code to no longer invoke undefined behavior. It's non-portable code that's disallowed by the C++ standard.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#declspec)
###  New warning on `__declspec` attributes
In Visual Studio 2017 version 15.3, the compiler no longer ignores attributes if `__declspec(...)` is applied before `extern "C"` linkage specification. Previously, the compiler would ignore the attribute, which could have runtime implications. When the **`/Wall`**and**`/WX`**options are set, the following code produces warning[C4768](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c4768?view=msvc-170):
C++
Copy
```
__declspec(noinline) extern "C" HRESULT __stdcall // C4768: __declspec attributes before linkage specification are ignored

```

To fix the warning, put `extern "C"` first:
C++
Copy
```
extern "C" __declspec(noinline) HRESULT __stdcall

```

This warning is off by default in Visual Studio 2017 version 15.3, and only impacts code compiled with **`/Wall`****`/WX`**. Starting in Visual Studio 2017 version 15.5, it's enabled by default as a level 3 warning.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#decltype-and-calls-to-deleted-destructors)
###  `decltype` and calls to deleted destructors
In previous versions of Visual Studio, the compiler didn't detect when a call to a deleted destructor occurred in the context of the expression associated with **`decltype`**. In Visual Studio 2017 version 15.3, the following code produces error[C2280](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-1/compiler-error-c2280?view=msvc-170):
C++
Copy
```
template<typename T>
struct A
{
   ~A() = delete;
};

template<typename T>
auto f() -> A<T>;

template<typename T>
auto g(T) -> decltype((f<T>()));

void h()
{
   g(42); // C2280: 'A<T>::~A(void)': attempting to reference a deleted function
}

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#uninitialized-const-variables)
### Uninitialized const variables
Visual Studio 2017 RTW release had a regression: the C++ compiler wouldn't issue a diagnostic for an uninitialized **`const`**variable. This regression has been fixed in Visual Studio 2017 version 15.3. The following code now produces warning[C4132](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-4-c4132?view=msvc-170):
C++
Copy
```
const int Value; // C4132: 'Value': const object should be initialized

```

To fix the error, assign a value to `Value`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#empty-declarations)
### Empty declarations
Visual Studio 2017 version 15.3 now warns on empty declarations for all types, not just built-in types. The following code now produces a level 2 [C4091](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-1-c4091?view=msvc-170) warning for all four declarations:
C++
Copy
```
struct A {};
template <typename> struct B {};
enum C { c1, c2, c3 };

int;    // warning C4091 : '' : ignored on left of 'int' when no variable is declared
A;      // warning C4091 : '' : ignored on left of 'main::A' when no variable is declared
B<int>; // warning C4091 : '' : ignored on left of 'B<int>' when no variable is declared
C;      // warning C4091 : '' : ignored on left of 'C' when no variable is declared

```

To remove the warnings, comment-out or remove the empty declarations. In cases where the unnamed object is intended to have a side effect (such as RAII), it should be given a name.
The warning is excluded under **`/Wv:18`**and is on by default under warning level W2.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#stdis_convertible-for-array-types)
###  `std::is_convertible` for array types
Previous versions of the compiler gave incorrect results for [`std::is_convertible`](https://learn.microsoft.com/en-us/cpp/standard-library/is-convertible-class?view=msvc-170) for array types. This required library writers to special-case the Microsoft C++ compiler when using the `std::is_convertible<...>` type trait. In the following example, the static asserts pass in earlier versions of Visual Studio but fail in Visual Studio 2017 version 15.3:
C++
Copy
```
#include <type_traits>

using Array = char[1];

static_assert(std::is_convertible<Array, Array>::value);
static_assert(std::is_convertible<const Array, const Array>::value, "");
static_assert(std::is_convertible<Array&, Array>::value, "");
static_assert(std::is_convertible<Array, Array&>::value, "");

```

`std::is_convertible<From, To>` is calculated by checking to see if an imaginary function definition is well formed:
C++
Copy
```
   To test() { return std::declval<From>(); }

```

[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#private-destructors-and-stdis_constructible)
### Private destructors and `std::is_constructible`
Previous versions of the compiler ignored whether a destructor was private when deciding the result of [`std::is_constructible`](https://learn.microsoft.com/en-us/cpp/standard-library/is-constructible-class?view=msvc-170). It now considers them. In the following example, the static asserts pass in earlier versions of Visual Studio but fail in Visual Studio 2017 version 15.3:
C++
Copy
```
#include <type_traits>

class PrivateDtor {
   PrivateDtor(int) { }
private:
   ~PrivateDtor() { }
};

// This assertion used to succeed. It now correctly fails.
static_assert(std::is_constructible<PrivateDtor, int>::value);

```

Private destructors cause a type to be non-constructible. `std::is_constructible<T, Args...>` is calculated as if the following declaration were written:
C++
Copy
```
   T obj(std::declval<Args>()...)

```

This call implies a destructor call.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c2668-ambiguous-overload-resolution)
### C2668: Ambiguous overload resolution
Previous versions of the compiler sometimes failed to detect ambiguity when it found multiple candidates via both using declarations and argument-dependent lookup. This failure can lead to the wrong overload being chosen, and to unexpected runtime behavior. In the following example, Visual Studio 2017 version 15.3 correctly raises [C2668](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c2668?view=msvc-170):
C++
Copy
```
namespace N {
   template<class T>
   void f(T&, T&);

   template<class T>
   void f();
}

template<class T>
void f(T&, T&);

struct S {};
void f()
{
   using N::f;

   S s1, s2;
   f(s1, s2); // C2668: 'f': ambiguous call to overloaded function
}

```

To fix the code, remove the using `N::f` statement if you intended to call `::f()`.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c2660-local-function-declarations-and-argument-dependent-lookup)
### C2660: local function declarations and argument-dependent lookup
Local function declarations hide the function declaration in the enclosing scope and disable argument-dependent lookup. Previous versions of the compiler always did argument-dependent lookup in this case. It could potentially lead to unexpected runtime behavior, if the compiler chose the wrong overload. Typically, the error is because of an incorrect signature of the local function declaration. In the following example, Visual Studio 2017 version 15.3 correctly raises [C2660](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-errors-2/compiler-error-c2660?view=msvc-170):
C++
Copy
```
struct S {};
void f(S, int);

void g()
{
   void f(S); // C2660 'f': function does not take 2 arguments:
   // or void f(S, int);
   S s;
   f(s, 0);
}

```

To fix the problem, either change the `f(S)` signature or remove it.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#c5038-order-of-initialization-in-initializer-lists)
### C5038: order of initialization in initializer lists
Class members get initialized in the order they're declared, not the order they appear in initializer lists. Previous versions of the compiler didn't warn when the order of the initializer list differed from the order of declaration. This issue could lead to undefined runtime behavior if one member's initialization depended on another member in the list already being initialized. In the following example, Visual Studio 2017 version 15.3 (with **`/Wall`**) raises warning[C5038](https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/c5038?view=msvc-170):
C++
Copy
```
struct A
{    // Initialized in reverse, y reused
    A(int a) : y(a), x(y) {} // C5038: data member 'A::y' will be initialized after data member 'A::x'
    int x;
    int y;
};

```

To fix the problem, arrange the initializer list to have the same order as the declarations. A similar warning is raised when one or both initializers refer to base class members.
This warning is off-by-default, and only affects code compiled with **`/Wall`**.
[](https://learn.microsoft.com/en-us/cpp/overview/cpp-conformance-improvements-2017?view=msvc-170#improvements_155)
