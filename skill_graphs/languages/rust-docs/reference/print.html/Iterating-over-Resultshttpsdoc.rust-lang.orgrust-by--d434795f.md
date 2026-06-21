# [Iterating over `Result`s](https://doc.rust-lang.org/rust-by-example/print.html#iterating-over-results)
An `Iter::map` operation might fail, for example:
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














fn main() {



    let strings = vec!["tofu", "93", "18"];



    let numbers: Vec<_> = strings



        .into_iter()




        .map(|s| s.parse::<i32>())




        .collect();



    println!("Results: {:?}", numbers);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Let’s step through strategies for handling this.
## [Ignore the failed items with `filter_map()`](https://doc.rust-lang.org/rust-by-example/print.html#ignore-the-failed-items-with-filter_map)
`filter_map` calls a function and filters out the results that are `None`.
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














fn main() {



    let strings = vec!["tofu", "93", "18"];



    let numbers: Vec<_> = strings



        .into_iter()




        .filter_map(|s| s.parse::<i32>().ok())




        .collect();



    println!("Results: {:?}", numbers);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [Collect the failed items with `map_err()` and `filter_map()`](https://doc.rust-lang.org/rust-by-example/print.html#collect-the-failed-items-with-map_err-and-filter_map)
`map_err` calls a function with the error, so by adding that to the previous `filter_map` solution we can save them off to the side while iterating.
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














fn main() {



    let strings = vec!["42", "tofu", "93", "999", "18"];



    let mut errors = vec![];



    let numbers: Vec<_> = strings



        .into_iter()




        .map(|s| s.parse::<u8>())




        .filter_map(|r| r.map_err(|e| errors.push(e)).ok())




        .collect();



    println!("Numbers: {:?}", numbers);



    println!("Errors: {:?}", errors);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [Fail the entire operation with `collect()`](https://doc.rust-lang.org/rust-by-example/print.html#fail-the-entire-operation-with-collect)
`Result` implements `FromIterator` so that a vector of results (`Vec<Result<T, E>>`) can be turned into a result with a vector (`Result<Vec<T>, E>`). Once an `Result::Err` is found, the iteration will terminate.
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














fn main() {



    let strings = vec!["tofu", "93", "18"];



    let numbers: Result<Vec<_>, _> = strings



        .into_iter()




        .map(|s| s.parse::<i32>())




        .collect();



    println!("Results: {:?}", numbers);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

This same technique can be used with `Option`.
## [Collect all valid values and failures with `partition()`](https://doc.rust-lang.org/rust-by-example/print.html#collect-all-valid-values-and-failures-with-partition)
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














fn main() {



    let strings = vec!["tofu", "93", "18"];



    let (numbers, errors): (Vec<_>, Vec<_>) = strings



        .into_iter()




        .map(|s| s.parse::<i32>())




        .partition(Result::is_ok);



    println!("Numbers: {:?}", numbers);



    println!("Errors: {:?}", errors);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

When you look at the results, you’ll note that everything is still wrapped in `Result`. A little more boilerplate is needed for this.
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














fn main() {



    let strings = vec!["tofu", "93", "18"];



    let (numbers, errors): (Vec<_>, Vec<_>) = strings



        .into_iter()




        .map(|s| s.parse::<i32>())




        .partition(Result::is_ok);



    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();



    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();



    println!("Numbers: {:?}", numbers);



    println!("Errors: {:?}", errors);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
