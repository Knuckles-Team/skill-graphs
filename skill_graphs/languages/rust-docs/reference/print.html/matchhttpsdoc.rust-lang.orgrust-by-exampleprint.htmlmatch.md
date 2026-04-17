# [match](https://doc.rust-lang.org/rust-by-example/print.html#match)
Rust provides pattern matching via the `match` keyword, which can be used like a C `switch`. The first matching arm is evaluated and all possible values must be covered.
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














fn main() {



    let number = 13;



    // TODO ^ Try different values for `number`





    println!("Tell me about {}", number);



    match number {




        // Match a single value




        1 => println!("One!"),




        // Match several values




        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),




        // TODO ^ Try adding 13 to the list of prime values




        // Match an inclusive range




        13..=19 => println!("A teen"),




        // Handle the rest of cases




        _ => println!("Ain't special"),




        // TODO ^ Try commenting out this catch-all arm



    }





    let boolean = true;



    // Match is an expression too



    let binary = match boolean {




        // The arms of a match must cover all the possible values




        false => 0,




        true => 1,




        // TODO ^ Try commenting out one of these arms



    };





    println!("{} -> {}", boolean, binary);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
