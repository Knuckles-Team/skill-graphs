# [Pulling `Result`s out of `Option`s](https://doc.rust-lang.org/rust-by-example/print.html#pulling-results-out-of-options)
The most basic way of handling mixed error types is to just embed them in each other.
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














use std::num::ParseIntError;






fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {



    vec.first().map(|first| {




        first.parse::<i32>().map(|n| 2 * n)



    })



}





fn main() {



    let numbers = vec!["42", "93", "18"];



    let empty = vec![];



    let strings = vec!["tofu", "93", "18"];





    println!("The first doubled is {:?}", double_first(numbers));





    println!("The first doubled is {:?}", double_first(empty));



    // Error 1: the input vector is empty





    println!("The first doubled is {:?}", double_first(strings));



    // Error 2: the element doesn't parse to a number



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

There are times when we’ll want to stop processing on errors (like with [`?`](https://doc.rust-lang.org/rust-by-example/print.html#introducing-)) but keep going when the `Option` is `None`. The `transpose` function comes in handy to swap the `Result` and `Option`.
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














use std::num::ParseIntError;






fn double_first(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {



    let opt = vec.first().map(|first| {




        first.parse::<i32>().map(|n| 2 * n)



    });





    opt.transpose()



}





fn main() {



    let numbers = vec!["42", "93", "18"];



    let empty = vec![];



    let strings = vec!["tofu", "93", "18"];





    println!("The first doubled is {:?}", double_first(numbers));



    println!("The first doubled is {:?}", double_first(empty));



    println!("The first doubled is {:?}", double_first(strings));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
