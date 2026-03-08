# [tuples](https://doc.rust-lang.org/rust-by-example/print.html#tuples-1)
Tuples can be destructured in a `match` as follows:
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














fn main() {



    let triple = (0, -2, 3);



    // TODO ^ Try different values for `triple`





    println!("Tell me about {:?}", triple);



    // Match can be used to destructure a tuple



    match triple {




        // Destructure the second and third elements




        (0, y, z) => println!("First is `0`, `y` is {:?}, and `z` is {:?}", y, z),




        (1, ..)  => println!("First is `1` and the rest doesn't matter"),




        (.., 2)  => println!("last is `2` and the rest doesn't matter"),




        (3, .., 4)  => println!("First is `3`, last is `4`, and the rest doesn't matter"),




        // `..` can be used to ignore the rest of the tuple




        _      => println!("It doesn't matter what they are"),




        // `_` means don't bind the value to a variable



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-16)
[Tuples](https://doc.rust-lang.org/rust-by-example/print.html#tuples)
