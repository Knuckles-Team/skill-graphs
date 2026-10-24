# [`Result`](https://doc.rust-lang.org/rust-by-example/print.html#result)
[`Result`](https://doc.rust-lang.org/std/result/enum.Result.html) is a richer version of the [`Option`](https://doc.rust-lang.org/std/option/enum.Option.html) type that describes possible _error_ instead of possible _absence_.
That is, `Result<T, E>` could have one of two outcomes:
  * `Ok(T)`: An element `T` was found
  * `Err(E)`: An error was found with element `E`


By convention, the expected outcome is `Ok` while the unexpected outcome is `Err`.
Like `Option`, `Result` has many methods associated with it. `unwrap()`, for example, either yields the element `T` or `panic`s. For case handling, there are many combinators between `Result` and `Option` that overlap.
In working with Rust, you will likely encounter methods that return the `Result` type, such as the [`parse()`](https://doc.rust-lang.org/std/primitive.str.html#method.parse) method. It might not always be possible to parse a string into the other type, so `parse()` returns a `Result` indicating possible failure.
Let’s see what happens when we successfully and unsuccessfully `parse()` a string:
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














fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {



    // Let's try using `unwrap()` to get the number out. Will it bite us?



    let first_number = first_number_str.parse::<i32>().unwrap();



    let second_number = second_number_str.parse::<i32>().unwrap();



    first_number * second_number


}





fn main() {



    let twenty = multiply("10", "2");



    println!("double is {}", twenty);





    let tt = multiply("t", "2");



    println!("double is {}", tt);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

In the unsuccessful case, `parse()` leaves us with an error for `unwrap()` to `panic` on. Additionally, the `panic` exits our program and provides an unpleasant error message.
To improve the quality of our error message, we should be more specific about the return type and consider explicitly handling the error.
## [Using `Result` in `main`](https://doc.rust-lang.org/rust-by-example/print.html#using-result-in-main)
The `Result` type can also be the return type of the `main` function if specified explicitly. Typically the `main` function will be of the form:
```


__

fn main() {
    println!("Hello World!");
}
```

However `main` is also able to have a return type of `Result`. If an error occurs within the `main` function it will return an error code and print a debug representation of the error (using the [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html) trait). The following example shows such a scenario and touches on aspects covered in [the following section](https://doc.rust-lang.org/rust-by-example/print.html#early-returns).
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














use std::num::ParseIntError;






fn main() -> Result<(), ParseIntError> {



    let number_str = "10";



    let number = match number_str.parse::<i32>() {




        Ok(number)  => number,




        Err(e) => return Err(e),



    };



    println!("{}", number);



    Ok(())



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
