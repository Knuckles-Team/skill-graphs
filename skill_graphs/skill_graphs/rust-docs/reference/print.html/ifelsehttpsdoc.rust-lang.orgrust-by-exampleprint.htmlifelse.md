# [if/else](https://doc.rust-lang.org/rust-by-example/print.html#ifelse)
Branching with `if`-`else` is similar to other languages. Unlike many of them, the boolean condition doesn’t need to be surrounded by parentheses, and each condition is followed by a block. `if`-`else` conditionals are expressions, and, all branches must return the same type.
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














fn main() {



    let n = 5;





    if n < 0 {




        print!("{} is negative", n);



    } else if n > 0 {




        print!("{} is positive", n);



    } else {




        print!("{} is zero", n);



    }





    let big_n =




        if n < 10 && n > -10 {




            println!(", and is a small number, increase ten-fold");






            // This expression returns an `i32`.




            10 * n



        } else {




            println!(", and is a big number, halve the number");






            // This expression must return an `i32` as well.




            n / 2




            // TODO ^ Try suppressing this expression with a semicolon.




        };



    //   ^ Don't forget to put a semicolon here! All `let` bindings need it.





    println!("{} -> {}", n, big_n);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
