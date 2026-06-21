# [`map` for `Result`](https://doc.rust-lang.org/rust-by-example/print.html#map-for-result)
Panicking in the previous example’s `multiply` does not make for robust code. Generally, we want to return the error to the caller so it can decide what is the right way to respond to errors.
We first need to know what kind of error type we are dealing with. To determine the `Err` type, we look to [`parse()`](https://doc.rust-lang.org/std/primitive.str.html#method.parse), which is implemented with the [`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) trait for [`i32`](https://doc.rust-lang.org/std/primitive.i32.html). As a result, the `Err` type is specified as [`ParseIntError`](https://doc.rust-lang.org/std/num/struct.ParseIntError.html).
In the example below, the straightforward `match` statement leads to code that is overall more cumbersome.
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














use std::num::ParseIntError;





// With the return type rewritten, we use pattern matching without `unwrap()`.



fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {



    match first_number_str.parse::<i32>() {




        Ok(first_number)  => {




            match second_number_str.parse::<i32>() {




                Ok(second_number)  => {




                    Ok(first_number * second_number)




                },




                Err(e) => Err(e),




            }




        },




        Err(e) => Err(e),



    }



}





fn print(result: Result<i32, ParseIntError>) {



    match result {




        Ok(n)  => println!("n is {}", n),




        Err(e) => println!("Error: {}", e),



    }



}





fn main() {



    // This still presents a reasonable answer.



    let twenty = multiply("10", "2");



    print(twenty);





    // The following now provides a much more helpful error message.



    let tt = multiply("t", "2");



    print(tt);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Luckily, `Option`’s `map`, `and_then`, and many other combinators are also implemented for `Result`. [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html) contains a complete listing.
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














use std::num::ParseIntError;





// As with `Option`, we can use combinators such as `map()`.


// This function is otherwise identical to the one above and reads:


// Multiply if both values can be parsed from str, otherwise pass on the error.



fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {



    first_number_str.parse::<i32>().and_then(|first_number| {




        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)



    })



}





fn print(result: Result<i32, ParseIntError>) {



    match result {




        Ok(n)  => println!("n is {}", n),




        Err(e) => println!("Error: {}", e),



    }



}





fn main() {



    // This still presents a reasonable answer.



    let twenty = multiply("10", "2");



    print(twenty);





    // The following now provides a much more helpful error message.



    let tt = multiply("t", "2");



    print(tt);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
