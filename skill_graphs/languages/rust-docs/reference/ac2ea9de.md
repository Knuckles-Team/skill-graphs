# [Crates](https://doc.rust-lang.org/rust-by-example/print.html#crates-1)
The `crate_type` attribute can be used to tell the compiler whether a crate is a binary or a library (and even which type of library), and the `crate_name` attribute can be used to set the name of the crate.
However, it is important to note that both the `crate_type` and `crate_name` attributes have **no** effect whatsoever when using Cargo, the Rust package manager. Since Cargo is used for the majority of Rust projects, this means real-world uses of `crate_type` and `crate_name` are relatively limited.
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













// This crate is a library


#![crate_type = "lib"]



// The library is named "rary"


#![crate_name = "rary"]






pub fn public_function() {



    println!("called rary's `public_function()`");



}





fn private_function() {



    println!("called rary's `private_function()`");



}





pub fn indirect_access() {



    print!("called rary's `indirect_access()`, that\n> ");





    private_function();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

When the `crate_type` attribute is used, we no longer need to pass the `--crate-type` flag to `rustc`.
```

__
$ rustc lib.rs
$ ls lib*
library.rlib

```
