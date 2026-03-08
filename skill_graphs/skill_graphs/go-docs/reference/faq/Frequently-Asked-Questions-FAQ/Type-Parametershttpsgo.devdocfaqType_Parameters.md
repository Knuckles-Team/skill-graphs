## Type Parameters[¶](https://go.dev/doc/faq#Type_Parameters)
### Why does Go have type parameters?[¶](https://go.dev/doc/faq#why_generics)
Type parameters permit what is known as generic programming, in which functions and data structures are defined in terms of types that are specified later, when those functions and data structures are used. For example, they make it possible to write a function that returns the minimum of two values of any ordered type, without having to write a separate version for each possible type. For a more in-depth explanation with examples see the blog post [Why Generics?](https://go.dev/blog/why-generics).
### How are generics implemented in Go?[¶](https://go.dev/doc/faq#generics_implementation)
The compiler can choose whether to compile each instantiation separately or whether to compile similar instantiations as a single implementation. The single implementation approach is similar to a function with an interface parameter. Different compilers will make different choices for different cases. The standard Go compiler ordinarily emits a single instantiation for every type argument with the same shape, where the shape is determined by properties of the type such as the size and the location of pointers that it contains. Future releases may experiment with the tradeoff between compile time, run-time efficiency, and code size.
### How do generics in Go compare to generics in other languages?[¶](https://go.dev/doc/faq#generics_comparison)
The basic functionality in all languages is similar: it is possible to write types and functions using types that are specified later. That said, there are some differences.
  * Java
In Java, the compiler checks generic types at compile time but removes the types at run time. This is known as `List<Integer>` at compile time will become the non-generic type `List` at run time. This means, for example, that when using the Java form of type reflection it is impossible to distinguish a value of type `List<Integer>` from a value of type `List<Float>`. In Go the reflection information for a generic type includes the full compile-time type information.
Java uses type wildcards such as `List<? extends Number>` or `List<? super Number>` to implement generic covariance and contravariance. Go does not have these concepts, which makes generic types in Go much simpler.
  * C++
Traditionally C++ templates do not enforce any constraints on type arguments, although C++20 supports optional constraints via
C++ supports template metaprogramming; Go does not. In practice, all C++ compilers compile each template at the point where it is instantiated; as noted above, Go can and does use different approaches for different instantiations.
  * Rust
The Rust version of constraints is known as trait bounds. In Rust the association between a trait bound and a type must be defined explicitly, either in the crate that defines the trait bound or the crate that defines the type. In Go type arguments implicitly satisfy constraints, just as Go types implicitly implement interface types. The Rust standard library defines standard traits for operations such as comparison or addition; the Go standard library does not, as these can be expressed in user code via interface types. The one exception is Go’s `comparable` predefined interface, which captures a property not expressible in the type system.
  * Python
Python is not a statically typed language, so one can reasonably say that all Python functions are always generic by default: they can always be called with values of any type, and any type errors are detected at run time.


### Why does Go use square brackets for type parameter lists?[¶](https://go.dev/doc/faq#generic_brackets)
Java and C++ use angle brackets for type parameter lists, as in Java `List<Integer>` and C++ `std::vector<int>`. However, that option was not available for Go, because it leads to a syntactic problem: when parsing code within a function, such as `v := F<T>`, at the point of seeing the `<` it’s ambiguous whether we are seeing an instantiation or an expression using the `<` operator. This is very difficult to resolve without type information.
For example, consider a statement like
```
    a, b = w < x, y > (z)

```

Without type information, it is impossible to decide whether the right hand side of the assignment is a pair of expressions (`w < x` and `y > z`), or whether it is a generic function instantiation and call that returns two result values (`(w<x, y>)(z)`).
It is a key design decision of Go that parsing be possible without type information, which seems impossible when using angle brackets for generics.
Go is not unique or original in using square brackets; there are other languages such as Scala that also use square brackets for generic code.
### Why does Go not support methods with type parameters?[¶](https://go.dev/doc/faq#generic_methods)
Go permits a generic type to have methods, but, other than the receiver, the arguments to those methods cannot use parameterized types. We do not anticipate that Go will ever add generic methods.
The problem is how to implement them. Specifically, consider checking whether a value in an interface implements another interface with additional methods. For example, consider this type, an empty struct with a generic `Nop` method that returns its argument, for any possible type:
```
type Empty struct{}

func (Empty) Nop[T any](x T) T {
    return x
}

```

Now suppose an `Empty` value is stored in an `any` and passed to other code that checks what it can do:
```
func TryNops(x any) {
    if x, ok := x.(interface{ Nop(string) string }); ok {
        fmt.Printf("string %s\n", x.Nop("hello"))
    }
    if x, ok := x.(interface{ Nop(int) int }); ok {
        fmt.Printf("int %d\n", x.Nop(42))
    }
    if x, ok := x.(interface{ Nop(io.Reader) io.Reader }); ok {
        data, err := io.ReadAll(x.Nop(strings.NewReader("hello world")))
        fmt.Printf("reader %q %v\n", data, err)
    }
}

```

How does that code work if `x` is an `Empty`? It seems that `x` must satisfy all three tests, along with any other form with any other type.
What code runs when those methods are called? For non-generic methods, the compiler generates the code for all method implementations and links them into the final program. But for generic methods, there can be an infinite number of method implementations, so a different strategy is needed.
There are four choices:
  1. At link time, make a list of all the possible dynamic interface checks, and then look for types that would satisfy them but are missing compiled methods, and then reinvoke the compiler to add those methods.
This would make builds significantly slower, by needing to stop after linking and repeat some compilations. It would especially slow down incremental builds. Worse, it is possible that the newly compiled method code would itself have new dynamic interface checks, and the process would have to be repeated. Examples can be constructed where the process never even finishes.
  2. Implement some kind of JIT, compiling the needed method code at runtime.
Go benefits greatly from the simplicity and predictable performance of being purely ahead-of-time compiled. We are reluctant to take on the complexity of a JIT just to implement one language feature.
  3. Arrange to emit a slow fallback for each generic method that uses a table of functions for every possible language operation on the type parameter, and then use that fallback implementation for the dynamic tests.
This approach would make a generic method parameterized by an unexpected type much slower than the same method parameterized by a type observed at compile time. This would make performance much less predictable.
  4. Define that generic methods cannot be used to satisfy interfaces at all.
Interfaces are an essential part of programming in Go. Disallowing generic methods from satisfying interfaces is unacceptable from a design point of view.


None of these choices are good ones, so we chose “none of the above.”
Instead of methods with type parameters, use top-level functions with type parameters, or add the type parameters to the receiver type.
For more details, including more examples, see the [proposal](https://go.dev/design/43651-type-parameters#no-parameterized-methods).
### Why can’t I use a more specific type for the receiver of a parameterized type?[¶](https://go.dev/doc/faq#types_in_method_declaration)
The method declarations of a generic type are written with a receiver that includes the type parameter names. Perhaps because of the similarity of the syntax for specifying types at a call site, some have thought this provides a mechanism for producing a method customized for certain type arguments by naming a specific type in the receiver, such as `string`:
```
type S[T any] struct { f T }

func (s S[string]) Add(t string) string {
    return s.f + t
}

```

This fails because the word `string` is taken by the compiler to be the name of the type argument in the method. The compiler error message will be something like “`operator + not defined on s.f (variable of type string)`”. This can be confusing because the `+` operator works fine on the predeclared type `string`, but the declaration has overwritten, for this method, the definition of `string`, and the operator does not work on that unrelated version of `string`. It’s valid to overwrite a predeclared name like this, but is an odd thing to do and often a mistake.
### Why can’t the compiler infer the type argument in my program?[¶](https://go.dev/doc/faq#type_inference)
There are many cases where a programmer can easily see what the type argument for a generic type or function must be, but the language does not permit the compiler to infer it. Type inference is intentionally limited to ensure that there is never any confusion as to which type is inferred. Experience with other languages suggests that unexpected type inference can lead to considerable confusion when reading and debugging a program. It is always possible to specify the explicit type argument to be used in the call. In the future new forms of inference may be supported, as long as the rules remain simple and clear.
