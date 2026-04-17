# [aliases for `Result`](https://doc.rust-lang.org/rust-by-example/print.html#aliases-for-result)
How about when we want to reuse a specific `Result` type many times? Recall that Rust allows us to create [aliases](https://doc.rust-lang.org/rust-by-example/print.html#aliasing). Conveniently, we can define one for the specific `Result` in question.
At a module level, creating aliases can be particularly helpful. Errors found in a specific module often have the same `Err` type, so a single alias can succinctly define _all_ associated `Results`. This is so useful that the `std` library even supplies one: [`io::Result`](https://doc.rust-lang.org/std/io/type.Result.html)!
Here’s a quick example to show off the syntax:
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














use std::num::ParseIntError;





// Define a generic alias for a `Result` with the error type `ParseIntError`.



type AliasedResult<T> = Result<T, ParseIntError>;





// Use the above alias to refer to our specific `Result` type.



fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {



    first_number_str.parse::<i32>().and_then(|first_number| {




        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)



    })



}




// Here, the alias again allows us to save some space.



fn print(result: AliasedResult<i32>) {



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

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-66)
[`io::Result`](https://doc.rust-lang.org/std/io/type.Result.html)
