# [constants](https://doc.rust-lang.org/rust-by-example/print.html#constants)
Rust has two different types of constants which can be declared in any scope including global. Both require explicit type annotation:
  * `const`: An unchangeable value (the common case).
  * `static`: A possibly mutable variable with [`'static`](https://doc.rust-lang.org/rust-by-example/print.html#static) lifetime. The static lifetime is inferred and does not have to be specified. Accessing or modifying a mutable static variable is [`unsafe`](https://doc.rust-lang.org/rust-by-example/print.html#unsafe-operations).

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













// Globals are declared outside all other scopes.



static LANGUAGE: &str = "Rust";




const THRESHOLD: i32 = 10;






fn is_big(n: i32) -> bool {



    // Access constant in some function



    n > THRESHOLD


}





fn main() {



    let n = 16;





    // Access constant in the main thread



    println!("This is {}", LANGUAGE);



    println!("The threshold is {}", THRESHOLD);



    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });





    // Error! Cannot modify a `const`.



    THRESHOLD = 5;



    // FIXME ^ Comment out this line



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-12)
[`'static` lifetime](https://doc.rust-lang.org/rust-by-example/print.html#static)
