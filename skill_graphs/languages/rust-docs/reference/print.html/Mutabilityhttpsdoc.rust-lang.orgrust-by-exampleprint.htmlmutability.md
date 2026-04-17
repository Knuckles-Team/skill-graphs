# [Mutability](https://doc.rust-lang.org/rust-by-example/print.html#mutability)
Variable bindings are immutable by default, but this can be overridden using the `mut` modifier.
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














fn main() {



    let _immutable_binding = 1;



    let mut mutable_binding = 1;





    println!("Before mutation: {}", mutable_binding);





    // Ok



    mutable_binding += 1;





    println!("After mutation: {}", mutable_binding);





    // Error! Cannot assign a new value to an immutable variable



    _immutable_binding += 1;



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

The compiler will throw a detailed diagnostic about mutability errors.
