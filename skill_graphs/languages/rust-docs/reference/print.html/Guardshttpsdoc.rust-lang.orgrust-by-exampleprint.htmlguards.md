# [Guards](https://doc.rust-lang.org/rust-by-example/print.html#guards)
A `match` _guard_ can be added to filter the arm.
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













#[allow(dead_code)]




enum Temperature {



    Celsius(i32),



    Fahrenheit(i32),



}





fn main() {



    let temperature = Temperature::Celsius(35);



    // ^ TODO try different values for `temperature`





    match temperature {




        Temperature::Celsius(t) if t > 30 => println!("{}C is above 30 Celsius", t),




        // The `if condition` part ^ is a guard




        Temperature::Celsius(t) => println!("{}C is equal to or below 30 Celsius", t),






        Temperature::Fahrenheit(t) if t > 86 => println!("{}F is above 86 Fahrenheit", t),




        Temperature::Fahrenheit(t) => println!("{}F is equal to or below 86 Fahrenheit", t),



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Note that the compiler won’t take guard conditions into account when checking if all patterns are covered by the match expression.
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














fn main() {



    let number: u8 = 4;





    match number {




        i if i == 0 => println!("Zero"),




        i if i > 0 => println!("Greater than zero"),




        // _ => unreachable!("Should never happen."),




        // TODO ^ uncomment to fix compilation



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-21)
[Tuples](https://doc.rust-lang.org/rust-by-example/print.html#tuples) [Enums](https://doc.rust-lang.org/rust-by-example/print.html#enums)
