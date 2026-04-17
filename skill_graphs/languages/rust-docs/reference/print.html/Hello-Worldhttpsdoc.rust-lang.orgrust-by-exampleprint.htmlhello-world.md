# [Hello World](https://doc.rust-lang.org/rust-by-example/print.html#hello-world)
This is the source code of the traditional Hello World program.
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













// This is a comment, and is ignored by the compiler.


// You can test this code by clicking the "Run" button over there ->


// or if you prefer to use your keyboard, you can use the "Ctrl + Enter"


// shortcut.




// This code is editable, feel free to hack it!


// You can always return to the original code by clicking the "Reset" button ->




// This is the main function.



fn main() {



    // Statements here are executed when the compiled binary is called.





    // Print text to the console.



    println!("Hello World!");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

`println!` is a [_macro_](https://doc.rust-lang.org/rust-by-example/print.html#macro_rules) that prints text to the console.
A binary can be generated using the Rust compiler: `rustc`.
```

__
$ rustc hello.rs

```

`rustc` will produce a `hello` binary that can be executed.
```

__
$ ./hello
Hello World!

```

### [Activity](https://doc.rust-lang.org/rust-by-example/print.html#activity)
Click ‘Run’ above to see the expected output. Next, add a new line with a second `println!` macro so that the output shows:
```

__
Hello World!
I'm a Rustacean!

```
