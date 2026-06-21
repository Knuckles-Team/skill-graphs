# [Testcase: unit clarification](https://doc.rust-lang.org/rust-by-example/print.html#testcase-unit-clarification)
A useful method of unit conversions can be examined by implementing `Add` with a phantom type parameter. The `Add` `trait` is examined below:
```

__
// This construction would impose: `Self + RHS = Output`
// where RHS defaults to Self if not specified in the implementation.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` must be `T<U>` so that `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
    ...
}
```

The whole implementation:
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














use std::ops::Add;




use std::marker::PhantomData;





/// Create void enumerations to define unit types.


#[derive(Debug, Clone, Copy)]




enum Inch {}



#[derive(Debug, Clone, Copy)]




enum Mm {}





/// `Length` is a type with phantom type parameter `Unit`,


/// and is not generic over the length type (that is `f64`).


///


/// `f64` already implements the `Clone` and `Copy` traits.


#[derive(Debug, Clone, Copy)]




struct Length<Unit>(f64, PhantomData<Unit>);





/// The `Add` trait defines the behavior of the `+` operator.



impl<Unit> Add for Length<Unit> {



    type Output = Length<Unit>;





    // add() returns a new `Length` struct containing the sum.



    fn add(self, rhs: Length<Unit>) -> Length<Unit> {




        // `+` calls the `Add` implementation for `f64`.




        Length(self.0 + rhs.0, PhantomData)



    }



}





fn main() {



    // Specifies `one_foot` to have phantom type parameter `Inch`.



    let one_foot:  Length<Inch> = Length(12.0, PhantomData);



    // `one_meter` has phantom type parameter `Mm`.



    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);





    // `+` calls the `add()` method we implemented for `Length<Unit>`.



    //



    // Since `Length` implements `Copy`, `add()` does not consume



    // `one_foot` and `one_meter` but copies them into `self` and `rhs`.



    let two_feet = one_foot + one_foot;



    let two_meters = one_meter + one_meter;





    // Addition works.



    println!("one foot + one_foot = {:?} in", two_feet.0);



    println!("one meter + one_meter = {:?} mm", two_meters.0);





    // Nonsensical operations fail as they should:



    // Compile-time Error: type mismatch.



    //let one_feter = one_foot + one_meter;



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-47)
[Borrowing (`&`)](https://doc.rust-lang.org/rust-by-example/print.html#borrowing), [Bounds (`X: Y`)](https://doc.rust-lang.org/rust-by-example/print.html#bounds), [enum](https://doc.rust-lang.org/rust-by-example/print.html#enums), [impl & self](https://doc.rust-lang.org/rust-by-example/print.html#associated-functions--methods), [Overloading](https://doc.rust-lang.org/rust-by-example/print.html#operator-overloading), [ref](https://doc.rust-lang.org/rust-by-example/print.html#the-ref-pattern), [Traits (`X for Y`)](https://doc.rust-lang.org/rust-by-example/print.html#traits-2), and [TupleStructs](https://doc.rust-lang.org/rust-by-example/print.html#structures).
