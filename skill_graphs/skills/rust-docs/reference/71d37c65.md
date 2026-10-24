# [Declare first](https://doc.rust-lang.org/rust-by-example/print.html#declare-first)
It is possible to declare variable bindings first and initialize them later, but all variable bindings must be initialized before they are used: the compiler forbids use of uninitialized variable bindings, as it would lead to undefined behavior.
It is not common to declare a variable binding and initialize it later in the function. It is more difficult for a reader to find the initialization when initialization is separated from declaration. It is common to declare and initialize a variable binding near where the variable will be used.
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














fn main() {



    // Declare a variable binding



    let a_binding;





    {




        let x = 2;






        // Initialize the binding




        a_binding = x * x;



    }





    println!("a binding: {}", a_binding);





    let another_binding;





    // Error! Use of uninitialized binding



    println!("another binding: {}", another_binding);



    // FIXME ^ Comment out this line





    another_binding = 1;





    println!("another binding: {}", another_binding);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
