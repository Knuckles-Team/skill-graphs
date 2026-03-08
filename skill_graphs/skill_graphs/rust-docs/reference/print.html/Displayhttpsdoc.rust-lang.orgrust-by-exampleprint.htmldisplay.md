# [Display](https://doc.rust-lang.org/rust-by-example/print.html#display)
`fmt::Debug` hardly looks compact and clean, so it is often advantageous to customize the output appearance. This is done by manually implementing [`fmt::Display`](https://doc.rust-lang.org/std/fmt/), which uses the `{}` print marker. Implementing it looks like this:
```


__

#![allow(unused)]
fn main() {
// Import (via `use`) the `fmt` module to make it available.
use std::fmt;

// Define a structure for which `fmt::Display` will be implemented. This is
// a tuple struct named `Structure` that contains an `i32`.
struct Structure(i32);

// To use the `{}` marker, the trait `fmt::Display` must be implemented
// manually for the type.
impl fmt::Display for Structure {
    // This trait requires `fmt` with this exact signature.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Write strictly the first element into the supplied output
        // stream: `f`. Returns `fmt::Result` which indicates whether the
        // operation succeeded or failed. Note that `write!` uses syntax which
        // is very similar to `println!`.
        write!(f, "{}", self.0)
    }
}
}
```

`fmt::Display` may be cleaner than `fmt::Debug` but this presents a problem for the `std` library. How should ambiguous types be displayed? For example, if the `std` library implemented a single style for all `Vec<T>`, what style should it be? Would it be either of these two?
  * `Vec<path>`: `/:/etc:/home/username:/bin` (split on `:`)
  * `Vec<number>`: `1,2,3` (split on `,`)


No, because there is no ideal style for all types and the `std` library doesn’t presume to dictate one. `fmt::Display` is not implemented for `Vec<T>` or for any other generic containers. `fmt::Debug` must then be used for these generic cases.
This is not a problem though because for any new _container_ type which is _not_ generic, `fmt::Display` can be implemented.
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



51



52



53



54














use std::fmt; // Import `fmt`





// A structure holding two numbers. `Debug` will be derived so the results can


// be contrasted with `Display`.


#[derive(Debug)]




struct MinMax(i64, i64);





// Implement `Display` for `MinMax`.



impl fmt::Display for MinMax {



    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {




        // Use `self.number` to refer to each positional data point.




        write!(f, "({}, {})", self.0, self.1)



    }



}




// Define a structure where the fields are nameable for comparison.


#[derive(Debug)]




struct Point2D {



    x: f64,



    y: f64,



}




// Similarly, implement `Display` for `Point2D`.



impl fmt::Display for Point2D {



    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {




        // Customize so only `x` and `y` are denoted.




        write!(f, "x: {}, y: {}", self.x, self.y)



    }



}





fn main() {



    let minmax = MinMax(0, 14);





    println!("Compare structures:");



    println!("Display: {}", minmax);



    println!("Debug: {:?}", minmax);





    let big_range =   MinMax(-300, 300);



    let small_range = MinMax(-3, 3);





    println!("The big range is {big} and the small is {small}",




             small = small_range,




             big = big_range);





    let point = Point2D { x: 3.3, y: 7.2 };





    println!("Compare points:");



    println!("Display: {}", point);



    println!("Debug: {:?}", point);





    // Error. Both `Debug` and `Display` were implemented, but `{:b}`



    // requires `fmt::Binary` to be implemented. This will not work.



    // println!("What does Point2D look like in binary: {:b}?", point);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

So, `fmt::Display` has been implemented but `fmt::Binary` has not, and therefore cannot be used. `std::fmt` has many such [`traits`](https://doc.rust-lang.org/std/fmt/#formatting-traits) and each requires its own implementation. This is detailed further in [`std::fmt`](https://doc.rust-lang.org/std/fmt/).
### [Activity](https://doc.rust-lang.org/rust-by-example/print.html#activity-1)
After checking the output of the above example, use the `Point2D` struct as a guide to add a `Complex` struct to the example. When printed in the same way, the output should be:
```

__
Display: 3.3 +7.2i
Debug: Complex { real: 3.3, imag: 7.2 }

Display: 4.7 -2.3i
Debug: Complex { real: 4.7, imag: -2.3 }

```

Bonus: Add a space before the `+`/`-` signs.
Hints in case you get stuck:
  * Check the documentation for [`Sign/#/0`](https://doc.rust-lang.org/std/fmt/#sign0) in `std::fmt`.
  * Bonus: Check [`if`-`else`](https://doc.rust-lang.org/rust-by-example/print.html#ifelse) branching and the [`abs`](https://doc.rust-lang.org/std/primitive.f64.html#method.abs) function.


### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-3)
[`derive`](https://doc.rust-lang.org/rust-by-example/print.html#derive), [`std::fmt`](https://doc.rust-lang.org/std/fmt/), [`macros`](https://doc.rust-lang.org/rust-by-example/print.html#macro_rules), [`struct`](https://doc.rust-lang.org/rust-by-example/print.html#structures), [`trait`](https://doc.rust-lang.org/std/fmt/#formatting-traits), and [`use`](https://doc.rust-lang.org/rust-by-example/print.html#the-use-declaration)
