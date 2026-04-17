# [Operator Overloading](https://doc.rust-lang.org/rust-by-example/print.html#operator-overloading)
In Rust, many of the operators can be overloaded via traits. That is, some operators can be used to accomplish different tasks based on their input arguments. This is possible because operators are syntactic sugar for method calls. For example, the `+` operator in `a + b` calls the `add` method (as in `a.add(b)`). This `add` method is part of the `Add` trait. Hence, the `+` operator can be used by any implementer of the `Add` trait.
A list of the traits, such as `Add`, that overload operators can be found in [`core::ops`](https://doc.rust-lang.org/core/ops/).
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














use std::ops;






struct Foo;




struct Bar;





#[derive(Debug)]




struct FooBar;





#[derive(Debug)]




struct BarFoo;





// The `std::ops::Add` trait is used to specify the functionality of `+`.


// Here, we make `Add<Bar>` - the trait for addition with a RHS of type `Bar`.


// The following block implements the operation: Foo + Bar = FooBar



impl ops::Add<Bar> for Foo {



    type Output = FooBar;





    fn add(self, _rhs: Bar) -> FooBar {




        println!("> Foo.add(Bar) was called");






        FooBar


    }



}




// By reversing the types, we end up implementing non-commutative addition.


// Here, we make `Add<Foo>` - the trait for addition with a RHS of type `Foo`.


// This block implements the operation: Bar + Foo = BarFoo



impl ops::Add<Foo> for Bar {



    type Output = BarFoo;





    fn add(self, _rhs: Foo) -> BarFoo {




        println!("> Bar.add(Foo) was called");






        BarFoo


    }



}





fn main() {



    println!("Foo + Bar = {:?}", Foo + Bar);



    println!("Bar + Foo = {:?}", Bar + Foo);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See Also](https://doc.rust-lang.org/rust-by-example/print.html#see-also-60)
[Add](https://doc.rust-lang.org/core/ops/trait.Add.html), [Syntax Index](https://doc.rust-lang.org/book/appendix-02-operators.html)
