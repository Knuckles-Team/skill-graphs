# [pointers/ref](https://doc.rust-lang.org/rust-by-example/print.html#pointersref)
For pointers, a distinction needs to be made between destructuring and dereferencing as they are different concepts which are used differently from languages like C/C++.
  * Dereferencing uses `*`
  * Destructuring uses `&`, `ref`, and `ref mut`

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



34



35



36



37



38



39



40



41



42



43



44



45



46



47



48



49



50














fn main() {



    // Assign a reference of type `i32`. The `&` signifies there



    // is a reference being assigned.



    let reference = &4;





    match reference {




        // If `reference` is pattern matched against `&val`, it results




        // in a comparison like:




        // `&i32`




        // `&val`




        // ^ We see that if the matching `&`s are dropped, then the `i32`




        // should be assigned to `val`.




        &val => println!("Got a value via destructuring: {:?}", val),



    }





    // To avoid the `&`, you dereference before matching.



    match *reference {




        val => println!("Got a value via dereferencing: {:?}", val),



    }





    // What if you don't start with a reference? `reference` was a `&`



    // because the right side was already a reference. This is not



    // a reference because the right side is not one.



    let _not_a_reference = 3;





    // Rust provides `ref` for exactly this purpose. It modifies the



    // assignment so that a reference is created for the element; this



    // reference is assigned.



    let ref _is_a_reference = 3;





    // Accordingly, by defining 2 values without references, references



    // can be retrieved via `ref` and `ref mut`.



    let value = 5;



    let mut mut_value = 6;





    // Use `ref` keyword to create a reference.



    match value {




        ref r => println!("Got a reference to a value: {:?}", r),



    }





    // Use `ref mut` similarly.



    match mut_value {




        ref mut m => {




            // Got a reference. Gotta dereference it before we can




            // add anything to it.




            *m += 10;




            println!("We added 10. `mut_value`: {:?}", m);




        },



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-19)
[The ref pattern](https://doc.rust-lang.org/rust-by-example/print.html#the-ref-pattern)
