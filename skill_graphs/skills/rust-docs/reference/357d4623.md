# [Higher Order Functions](https://doc.rust-lang.org/rust-by-example/print.html#higher-order-functions)
Rust provides Higher Order Functions (HOF). These are functions that take one or more functions and/or produce a more useful function. HOFs and lazy iterators give Rust its functional flavor.
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














fn is_odd(n: u32) -> bool {



    n % 2 == 1



}





fn main() {



    println!("Find the sum of all the numbers with odd squares under 1000");



    let upper = 1000;





    // Imperative approach



    // Declare accumulator variable



    let mut acc = 0;



    // Iterate: 0, 1, 2, ... to infinity



    for n in 0.. {




        // Square the number




        let n_squared = n * n;






        if n_squared >= upper {




            // Break loop if exceeded the upper limit




            break;




        } else if is_odd(n_squared) {




            // Accumulate value, if it's odd




            acc += n;




        }



    }



    println!("imperative style: {}", acc);





    // Functional approach



    let sum: u32 =




        (0..).take_while(|&n| n * n < upper) // Below upper limit




             .filter(|&n| is_odd(n * n))     // That are odd




             .sum();                         // Sum them



    println!("functional style: {}", sum);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

[Option](https://doc.rust-lang.org/core/option/enum.Option.html) and [Iterator](https://doc.rust-lang.org/core/iter/trait.Iterator.html) implement their fair share of HOFs.
