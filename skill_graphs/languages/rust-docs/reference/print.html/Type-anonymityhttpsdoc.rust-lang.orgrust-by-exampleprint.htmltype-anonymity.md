# [Type anonymity](https://doc.rust-lang.org/rust-by-example/print.html#type-anonymity)
Closures succinctly capture variables from enclosing scopes. Does this have any consequences? It surely does. Observe how using a closure as a function parameter requires [generics](https://doc.rust-lang.org/rust-by-example/print.html#generics), which is necessary because of how they are defined:
```


__

#![allow(unused)]
fn main() {
// `F` must be generic.
fn apply<F>(f: F) where
    F: FnOnce() {
    f();
}
}
```

When a closure is defined, the compiler implicitly creates a new anonymous structure to store the captured variables inside, meanwhile implementing the functionality via one of the `traits`: `Fn`, `FnMut`, or `FnOnce` for this unknown type. This type is assigned to the variable which is stored until calling.
Since this new type is of unknown type, any usage in a function will require generics. However, an unbounded type parameter `<T>` would still be ambiguous and not be allowed. Thus, bounding by one of the `traits`: `Fn`, `FnMut`, or `FnOnce` (which it implements) is sufficient to specify its type.
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













// `F` must implement `Fn` for a closure which takes no


// inputs and returns nothing - exactly what is required


// for `print`.



fn apply<F>(f: F) where



    F: Fn() {



    f();



}





fn main() {



    let x = 7;





    // Capture `x` into an anonymous type and implement



    // `Fn` for it. Store it in `print`.



    let print = || println!("{}", x);





    apply(print);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-28)
[`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html), and [`FnOnce`](https://doc.rust-lang.org/std/ops/trait.FnOnce.html)
