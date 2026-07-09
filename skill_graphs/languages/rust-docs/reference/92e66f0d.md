# [Static](https://doc.rust-lang.org/rust-by-example/print.html#static)
Rust has a few reserved lifetime names. One of those is `'static`. You might encounter it in two situations:
```

__
// A reference with 'static lifetime:
let s: &'static str = "hello world";

// 'static as part of a trait bound:
fn generic<T>(x: T) where T: 'static {}
```

Both are related but subtly different and this is a common source for confusion when learning Rust. Here are some examples for each situation:
## [Reference lifetime](https://doc.rust-lang.org/rust-by-example/print.html#reference-lifetime)
As a reference lifetime `'static` indicates that the data pointed to by the reference lives for the remaining lifetime of the running program. It can still be coerced to a shorter lifetime.
There are two common ways to make a variable with `'static` lifetime, and both are stored in the read-only memory of the binary:
  * Make a constant with the `static` declaration.
  * Make a `string` literal which has type: `&'static str`.


See the following example for a display of each method:
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













// Make a constant with `'static` lifetime.



static NUM: i32 = 18;





// Returns a reference to `NUM` where its `'static`


// lifetime is coerced to that of the input argument.



fn coerce_static<'a>(_: &'a i32) -> &'a i32 {



    &NUM


}





fn main() {



    {




        // Make a `string` literal and print it:




        let static_string = "I'm in read-only memory";




        println!("static_string: {}", static_string);






        // When `static_string` goes out of scope, the reference




        // can no longer be used, but the data remains in the binary.



    }





    {




        // Make an integer to use for `coerce_static`:




        let lifetime_num = 9;






        // Coerce `NUM` to lifetime of `lifetime_num`:




        let coerced_static = coerce_static(&lifetime_num);






        println!("coerced_static: {}", coerced_static);



    }





    println!("NUM: {} stays accessible!", NUM);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Since `'static` references only need to be valid for the _remainder_ of a program’s life, they can be created while the program is executed. Just to demonstrate, the below example uses [`Box::leak`](https://doc.rust-lang.org/std/boxed/struct.Box.html#method.leak) to dynamically create `'static` references. In that case it definitely doesn’t live for the entire duration, but only from the leaking point onward.
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














extern crate rand;




use rand::Fill;






fn random_vec() -> &'static [usize; 100] {



    let mut rng = rand::thread_rng();



    let mut boxed = Box::new([0; 100]);



    boxed.try_fill(&mut rng).unwrap();



    Box::leak(boxed)



}





fn main() {



    let first: &'static [usize; 100] = random_vec();



    let second: &'static [usize; 100] = random_vec();



    assert_ne!(first, second)



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [Trait bound](https://doc.rust-lang.org/rust-by-example/print.html#trait-bound)
As a trait bound, it means the type does not contain any non-static references. Eg. the receiver can hold on to the type for as long as they want and it will never become invalid until they drop it.
It’s important to understand this means that any owned data always passes a `'static` lifetime bound, but a reference to that owned data generally does not:
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














use std::fmt::Debug;






fn print_it(input: impl Debug + 'static) {



    println!("'static value passed in is: {:?}", input);



}





fn main() {



    // i is owned and contains no references, thus it's 'static:



    let i = 5;



    print_it(i);





    // oops, &i only has the lifetime defined by the scope of



    // main(), so it's not 'static:



    print_it(&i);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

The compiler will tell you:
```

__
error[E0597]: `i` does not live long enough
  --> src/lib.rs:15:15
   |
15 |     print_it(&i);
   |     ---------^^--
   |     |         |
   |     |         borrowed value does not live long enough
   |     argument requires that `i` is borrowed for `'static`
16 | }
   | - `i` dropped here while still borrowed

```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-57)
[`'static` constants](https://doc.rust-lang.org/rust-by-example/print.html#constants)
