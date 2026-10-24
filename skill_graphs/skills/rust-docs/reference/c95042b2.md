# [Functions](https://doc.rust-lang.org/rust-by-example/print.html#functions-1)
The same set of rules can be applied to functions: a type `T` becomes generic when preceded by `<T>`.
Using generic functions sometimes requires explicitly specifying type parameters. This may be the case if the function is called where the return type is generic, or if the compiler doesn’t have enough information to infer the necessary type parameters.
A function call with explicitly specified type parameters looks like: `fun::<A, B, ...>()`.
```


__



1



2



3



4



5



6



7



8



9



10



11



12



13



14



15



16



17



18



19



20



21



22



23



24



25



26



27



28



29



30



31



32



33



34



35



36



37














struct A;          // Concrete type `A`.




struct S(A);       // Concrete type `S`.




struct SGen<T>(T); // Generic type `SGen`.





// The following functions all take ownership of the variable passed into


// them and immediately go out of scope, freeing the variable.




// Define a function `reg_fn` that takes an argument `_s` of type `S`.


// This has no `<T>` so this is not a generic function.



fn reg_fn(_s: S) {}





// Define a function `gen_spec_t` that takes an argument `_s` of type `SGen<T>`.


// It has been explicitly given the type parameter `A`, but because `A` has not


// been specified as a generic type parameter for `gen_spec_t`, it is not generic.



fn gen_spec_t(_s: SGen<A>) {}





// Define a function `gen_spec_i32` that takes an argument `_s` of type `SGen<i32>`.


// It has been explicitly given the type parameter `i32`, which is a specific type.


// Because `i32` is not a generic type, this function is also not generic.



fn gen_spec_i32(_s: SGen<i32>) {}





// Define a function `generic` that takes an argument `_s` of type `SGen<T>`.


// Because `SGen<T>` is preceded by `<T>`, this function is generic over `T`.



fn generic<T>(_s: SGen<T>) {}






fn main() {



    // Using the non-generic functions



    reg_fn(S(A));          // Concrete type.



    gen_spec_t(SGen(A));   // Implicitly specified type parameter `A`.



    gen_spec_i32(SGen(6)); // Implicitly specified type parameter `i32`.





    // Explicitly specified type parameter `char` to `generic()`.



    generic::<char>(SGen('a'));





    // Implicitly specified type parameter `char` to `generic()`.



    generic(SGen('c'));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-36)
[functions](https://doc.rust-lang.org/rust-by-example/print.html#functions) and [`struct`s](https://doc.rust-lang.org/rust-by-example/print.html#structures)
