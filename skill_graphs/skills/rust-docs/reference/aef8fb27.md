# [`abort` and `unwind`](https://doc.rust-lang.org/rust-by-example/print.html#abort-and-unwind)
The previous section illustrates the error handling mechanism `panic`. Different code paths can be conditionally compiled based on the panic setting. The current values available are `unwind` and `abort`.
Building on the prior lemonade example, we explicitly use the panic strategy to exercise different lines of code.
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














fn drink(beverage: &str) {



    // You shouldn't drink too much sugary beverages.



    if beverage == "lemonade" {




        if cfg!(panic = "abort") {




            println!("This is not your party. Run!!!!");




        } else {




            println!("Spit it out!!!!");




        }



    } else {




        println!("Some refreshing {} is all I need.", beverage);



    }



}





fn main() {



    drink("water");



    drink("lemonade");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Here is another example focusing on rewriting `drink()` and explicitly use the `unwind` keyword.
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













#[cfg(panic = "unwind")]




fn ah() {



    println!("Spit it out!!!!");



}




#[cfg(not(panic = "unwind"))]




fn ah() {



    println!("This is not your party. Run!!!!");



}





fn drink(beverage: &str) {



    if beverage == "lemonade" {




        ah();



    } else {




        println!("Some refreshing {} is all I need.", beverage);



    }



}





fn main() {



    drink("water");



    drink("lemonade");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

The panic strategy can be set from the command line by using `abort` or `unwind`.
```

__
rustc  lemonade.rs -C panic=abort

```
