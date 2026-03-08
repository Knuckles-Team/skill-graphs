# [Introducing `?`](https://doc.rust-lang.org/rust-by-example/print.html#introducing-)
Sometimes we just want the simplicity of `unwrap` without the possibility of a `panic`. Until now, `unwrap` has forced us to nest deeper and deeper when what we really wanted was to get the variable _out_. This is exactly the purpose of `?`.
Upon finding an `Err`, there are two valid actions to take:
  1. `panic!` which we already decided to try to avoid if possible
  2. `return` because an `Err` means it cannot be handled


`?` is _almost_[1](https://doc.rust-lang.org/rust-by-example/print.html#footnote-%E2%80%A0) exactly equivalent to an `unwrap` which `return`s instead of `panic`king on `Err`s. Let’s see how we can simplify the earlier example that used combinators:
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














use std::num::ParseIntError;






fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {



    let first_number = first_number_str.parse::<i32>()?;



    let second_number = second_number_str.parse::<i32>()?;





    Ok(first_number * second_number)



}





fn print(result: Result<i32, ParseIntError>) {



    match result {




        Ok(n)  => println!("n is {}", n),




        Err(e) => println!("Error: {}", e),



    }



}





fn main() {



    print(multiply("10", "2"));



    print(multiply("t", "2"));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [The `try!` macro](https://doc.rust-lang.org/rust-by-example/print.html#the-try-macro)
Before there was `?`, the same functionality was achieved with the `try!` macro. The `?` operator is now recommended, but you may still find `try!` when looking at older code. The same `multiply` function from the previous example would look like this using `try!`:
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













// To compile and run this example without errors, while using Cargo, change the value


// of the `edition` field, in the `[package]` section of the `Cargo.toml` file, to "2015".





use std::num::ParseIntError;






fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {



    let first_number = try!(first_number_str.parse::<i32>());



    let second_number = try!(second_number_str.parse::<i32>());





    Ok(first_number * second_number)



}





fn print(result: Result<i32, ParseIntError>) {



    match result {




        Ok(n)  => println!("n is {}", n),




        Err(e) => println!("Error: {}", e),



    }



}





fn main() {



    print(multiply("10", "2"));



    print(multiply("t", "2"));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

* * *
  1. See [re-enter ?](https://doc.rust-lang.org/rust-by-example/print.html#other-uses-of-) for more details. [↩](https://doc.rust-lang.org/rust-by-example/print.html#fr-%E2%80%A0-1)
