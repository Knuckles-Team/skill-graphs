# [Primitives](https://doc.rust-lang.org/rust-by-example/print.html#primitives)
Rust provides access to a wide variety of `primitives`. A sample includes:
### [Scalar Types](https://doc.rust-lang.org/rust-by-example/print.html#scalar-types)
  * Signed integers: `i8`, `i16`, `i32`, `i64`, `i128` and `isize` (pointer size)
  * Unsigned integers: `u8`, `u16`, `u32`, `u64`, `u128` and `usize` (pointer size)
  * Floating point: `f32`, `f64`
  * `char` Unicode scalar values like `'a'`, `'α'` and `'∞'` (4 bytes each)
  * `bool` either `true` or `false`
  * The unit type `()`, whose only possible value is an empty tuple: `()`


Despite the value of a unit type being a tuple, it is not considered a compound type because it does not contain multiple values.
### [Compound Types](https://doc.rust-lang.org/rust-by-example/print.html#compound-types)
  * Arrays like `[1, 2, 3]`
  * Tuples like `(1, true)`


Variables can always be _type annotated_. Numbers may additionally be annotated via a _suffix_ or _by default_. Integers default to `i32` and floats to `f64`. Note that Rust can also infer types from context.
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














fn main() {



    // Variables can be type annotated.



    let logical: bool = true;





    let a_float: f64 = 1.0;  // Regular annotation



    let an_integer   = 5i32; // Suffix annotation





    // Or a default will be used.



    let default_float   = 3.0; // `f64`



    let default_integer = 7;   // `i32`





    // A type can also be inferred from context.



    let mut inferred_type = 12; // Type i64 is inferred from another line.



    inferred_type = 4294967296i64;





    // A mutable variable's value can be changed.



    let mut mutable = 12; // Mutable `i32`



    mutable = 21;





    // Error! The type of a variable can't be changed.



    mutable = true;





    // Variables can be overwritten with shadowing.



    let mutable = true;





    /* Compound types - Array and Tuple */





    // Array signature consists of Type T and length as [T; length].



    let my_array: [i32; 5] = [1, 2, 3, 4, 5];





    // Tuple is a collection of values of different types



    // and is constructed using parentheses ().



    let my_tuple = (5u32, 1u8, true, -5.04f32);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-6)
[the `std` library](https://doc.rust-lang.org/std/), [`mut`](https://doc.rust-lang.org/rust-by-example/print.html#mutability), [`inference`](https://doc.rust-lang.org/rust-by-example/print.html#inference), and [`shadowing`](https://doc.rust-lang.org/rust-by-example/print.html#scope-and-shadowing)
