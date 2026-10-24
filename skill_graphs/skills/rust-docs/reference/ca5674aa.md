# [loop](https://doc.rust-lang.org/rust-by-example/print.html#loop)
Rust provides a `loop` keyword to indicate an infinite loop.
The `break` statement can be used to exit a loop at anytime, whereas the `continue` statement can be used to skip the rest of the iteration and start a new one.
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














fn main() {



    let mut count = 0u32;





    println!("Let's count until infinity!");





    // Infinite loop



    loop {




        count += 1;






        if count == 3 {




            println!("three");






            // Skip the rest of this iteration




            continue;




        }






        println!("{}", count);






        if count == 5 {




            println!("OK, that's enough");






            // Exit this loop




            break;




        }



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
