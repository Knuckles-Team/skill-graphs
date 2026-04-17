# [Aliasing](https://doc.rust-lang.org/rust-by-example/print.html#aliasing)
The `type` statement can be used to give a new name to an existing type. Types must have `UpperCamelCase` names, or the compiler will raise a warning. The exception to this rule are the primitive types: `usize`, `f32`, etc.
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













// `NanoSecond`, `Inch`, and `U64` are new names for `u64`.



type NanoSecond = u64;




type Inch = u64;




type U64 = u64;






fn main() {



    // `NanoSecond` = `Inch` = `U64` = `u64`.



    let nanoseconds: NanoSecond = 5 as u64;



    let inches: Inch = 2 as U64;





    // Note that type aliases *don't* provide any extra type safety, because



    // aliases are *not* new types



    println!("{} nanoseconds + {} inches = {} unit?",




             nanoseconds,




             inches,




             nanoseconds + inches);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

The main use of aliases is to reduce boilerplate; for example the `io::Result<T>` type is an alias for the `Result<T, io::Error>` type.
### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-13)
[Attributes](https://doc.rust-lang.org/rust-by-example/print.html#attributes)
