# [Formatted print](https://doc.rust-lang.org/rust-by-example/print.html#formatted-print)
Printing is handled by a series of [`macros`](https://doc.rust-lang.org/rust-by-example/print.html#macro_rules) defined in [`std::fmt`](https://doc.rust-lang.org/std/fmt/) some of which are:
  * `format!`: write formatted text to [`String`](https://doc.rust-lang.org/rust-by-example/print.html#strings)
  * `print!`: same as `format!` but the text is printed to the console (io::stdout).
  * `println!`: same as `print!` but a newline is appended.
  * `eprint!`: same as `print!` but the text is printed to the standard error (io::stderr).
  * `eprintln!`: same as `eprint!` but a newline is appended.


All parse text in the same fashion. As a plus, Rust checks formatting correctness at compile time.
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



38



39



40



41



42



43



44



45



46



47



48



49



50



51



52



53



54



55



56



57














fn main() {



    // In general, the `{}` will be automatically replaced with any



    // arguments. These will be stringified.



    println!("{} days", 31);





    // Positional arguments can be used. Specifying an integer inside `{}`



    // determines which additional argument will be replaced. Arguments start



    // at 0 immediately after the format string.



    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");





    // As can named arguments.



    println!("{subject} {verb} {object}",




             object="the lazy dog",




             subject="the quick brown fox",




             verb="jumps over");





    // Different formatting can be invoked by specifying the format character



    // after a `:`.



    println!("Base 10:               {}",   69420); // 69420



    println!("Base 2 (binary):       {:b}", 69420); // 10000111100101100



    println!("Base 8 (octal):        {:o}", 69420); // 207454



    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c





    // You can right-justify text with a specified width. This will



    // output "    1". (Four white spaces and a "1", for a total width of 5.)



    println!("{number:>5}", number=1);





    // You can pad numbers with extra zeroes,



    println!("{number:0>5}", number=1); // 00001



    // and left-adjust by flipping the sign. This will output "10000".



    println!("{number:0<5}", number=1); // 10000





    // You can use named arguments in the format specifier by appending a `$`.



    println!("{number:0>width$}", number=1, width=5);





    // Rust even checks to make sure the correct number of arguments are used.



    println!("My name is {0}, {1} {0}", "Bond");



    // FIXME ^ Add the missing argument: "James"





    // Only types that implement fmt::Display can be formatted with `{}`. User-



    // defined types do not implement fmt::Display by default.





    #[allow(dead_code)] // disable `dead_code` which warn against unused module



    struct Structure(i32);





    // This will not compile because `Structure` does not implement



    // fmt::Display.



    // println!("This struct `{}` won't print...", Structure(3));



    // TODO ^ Try uncommenting this line





    // For Rust 1.58 and above, you can directly capture the argument from a



    // surrounding variable. Just like the above, this will output



    // "    1", 4 white spaces and a "1".



    let number: f64 = 1.0;



    let width: usize = 5;



    println!("{number:>width$}");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

[`std::fmt`](https://doc.rust-lang.org/std/fmt/) contains many [`traits`](https://doc.rust-lang.org/std/fmt/#formatting-traits) which govern the display of text. The base form of two important ones are listed below:
  * `fmt::Debug`: Uses the `{:?}` marker. Format text for debugging purposes.
  * `fmt::Display`: Uses the `{}` marker. Format text in a more elegant, user friendly fashion.


Here, we used `fmt::Display` because the std library provides implementations for these types. To print text for custom types, more steps are required.
Implementing the `fmt::Display` trait automatically implements the [`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html) trait which allows us to [convert](https://doc.rust-lang.org/rust-by-example/print.html#to-and-from-strings) the type to [`String`](https://doc.rust-lang.org/rust-by-example/print.html#strings).
In _line 43_ , `#[allow(dead_code)]` is an [attribute](https://doc.rust-lang.org/rust-by-example/print.html#attributes) which only applies to the module after it.
### [Activities](https://doc.rust-lang.org/rust-by-example/print.html#activities)
  * Fix the issue in the above code (see FIXME) so that it runs without error.
  * Try uncommenting the line that attempts to format the `Structure` struct (see TODO)
  * Add a `println!` macro call that prints: `Pi is roughly 3.142` by controlling the number of decimal places shown. For the purposes of this exercise, use `let pi = 3.141592` as an estimate for pi. (Hint: you may need to check the [`std::fmt`](https://doc.rust-lang.org/std/fmt/) documentation for setting the number of decimals to display)


### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-1)
[`std::fmt`](https://doc.rust-lang.org/std/fmt/), [`macros`](https://doc.rust-lang.org/rust-by-example/print.html#macro_rules), [`struct`](https://doc.rust-lang.org/rust-by-example/print.html#structures), [`traits`](https://doc.rust-lang.org/std/fmt/#formatting-traits), and [`dead_code`](https://doc.rust-lang.org/rust-by-example/print.html#dead_code)
