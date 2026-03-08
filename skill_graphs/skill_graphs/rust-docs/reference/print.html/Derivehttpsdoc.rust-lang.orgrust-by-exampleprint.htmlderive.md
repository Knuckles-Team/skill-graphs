# [Derive](https://doc.rust-lang.org/rust-by-example/print.html#derive)
The compiler is capable of providing basic implementations for some traits via the `#[derive]` [attribute](https://doc.rust-lang.org/rust-by-example/print.html#attributes). These traits can still be manually implemented if a more complex behavior is required.
The following is a list of derivable traits:
  * Comparison traits: [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html), [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html), [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html), [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html).
  * [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html), to create `T` from `&T` via a copy.
  * [`Copy`](https://doc.rust-lang.org/core/marker/trait.Copy.html), to give a type ‘copy semantics’ instead of ‘move semantics’.
  * [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html), to compute a hash from `&T`.
  * [`Default`](https://doc.rust-lang.org/std/default/trait.Default.html), to create an empty instance of a data type.
  * [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html), to format a value using the `{:?}` formatter.

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













// `Centimeters`, a tuple struct that can be compared


#[derive(PartialEq, PartialOrd)]




struct Centimeters(f64);





// `Inches`, a tuple struct that can be printed


#[derive(Debug)]




struct Inches(i32);






impl Inches {



    fn to_centimeters(&self) -> Centimeters {




        let &Inches(inches) = self;






        Centimeters(inches as f64 * 2.54)



    }



}




// `Seconds`, a tuple struct with no additional attributes



struct Seconds(i32);






fn main() {



    let _one_second = Seconds(1);





    // Error: `Seconds` can't be printed; it doesn't implement the `Debug` trait



    //println!("One second looks like: {:?}", _one_second);



    // TODO ^ Try uncommenting this line





    // Error: `Seconds` can't be compared; it doesn't implement the `PartialEq` trait



    //let _this_is_true = (_one_second == _one_second);



    // TODO ^ Try uncommenting this line





    let foot = Inches(12);





    println!("One foot equals {:?}", foot);





    let meter = Centimeters(100.0);





    let cmp =




        if foot.to_centimeters() < meter {




            "smaller"




        } else {




            "bigger"




        };





    println!("One foot is {} than one meter.", cmp);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-59)
[`derive`](https://doc.rust-lang.org/reference/attributes.html#derive)
