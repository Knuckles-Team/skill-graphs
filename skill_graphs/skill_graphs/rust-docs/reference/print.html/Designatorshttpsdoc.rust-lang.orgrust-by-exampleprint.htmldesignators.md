# [Designators](https://doc.rust-lang.org/rust-by-example/print.html#designators)
The arguments of a macro are prefixed by a dollar sign `$` and type annotated with a _designator_ :
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













macro_rules! create_function {



    // This macro takes an argument of designator `ident` and



    // creates a function named `$func_name`.



    // The `ident` designator is used for variable/function names.



    ($func_name:ident) => {




        fn $func_name() {




            // The `stringify!` macro converts an `ident` into a string.




            println!("You called {:?}()",




                     stringify!($func_name));




        }



    };



}




// Create functions named `foo` and `bar` with the above macro.


create_function!(foo);



create_function!(bar);





macro_rules! print_result {



    // This macro takes an expression of type `expr` and prints



    // it as a string along with its result.



    // The `expr` designator is used for expressions.



    ($expression:expr) => {




        // `stringify!` will convert the expression *as it is* into a string.




        println!("{:?} = {:?}",




                 stringify!($expression),




                 $expression);



    };



}





fn main() {



    foo();



    bar();





    print_result!(1u32 + 1);





    // Recall that blocks are expressions too!



    print_result!({




        let x = 1u32;






        x * x + 2 * x - 1



    });



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

These are some of the available designators:
  * `block`
  * `expr` is used for expressions
  * `ident` is used for variable/function names
  * `item`
  * `literal` is used for literal constants
  * `pat` (_pattern_)
  * `path`
  * `stmt` (_statement_)
  * `tt` (_token tree_)
  * `ty` (_type_)
  * `vis` (_visibility qualifier_)


For a complete list, see the [Rust Reference](https://doc.rust-lang.org/reference/macros-by-example.html).
