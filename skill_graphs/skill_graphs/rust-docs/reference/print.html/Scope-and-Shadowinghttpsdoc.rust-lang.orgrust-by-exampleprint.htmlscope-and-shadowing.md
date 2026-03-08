# [Scope and Shadowing](https://doc.rust-lang.org/rust-by-example/print.html#scope-and-shadowing)
Variable bindings have a scope, and are constrained to live in a _block_. A block is a collection of statements enclosed by braces `{}`.
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














fn main() {



    // This binding lives in the main function



    let long_lived_binding = 1;





    // This is a block, and has a smaller scope than the main function



    {




        // This binding only exists in this block




        let short_lived_binding = 2;






        println!("inner short: {}", short_lived_binding);



    }



    // End of the block





    // Error! `short_lived_binding` doesn't exist in this scope



    println!("outer short: {}", short_lived_binding);



    // FIXME ^ Comment out this line





    println!("outer long: {}", long_lived_binding);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Also,
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



    let shadowed_binding = 1;





    {




        println!("before being shadowed: {}", shadowed_binding);






        // This binding *shadows* the outer one




        let shadowed_binding = "abc";






        println!("shadowed in inner block: {}", shadowed_binding);



    }



    println!("outside inner block: {}", shadowed_binding);





    // This binding *shadows* the previous binding



    let shadowed_binding = 2;



    println!("shadowed in outer block: {}", shadowed_binding);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
