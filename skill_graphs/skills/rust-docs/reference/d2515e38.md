# [The Problem](https://doc.rust-lang.org/rust-by-example/print.html#the-problem)
A `trait` that is generic over its container type has type specification requirements - users of the `trait` _must_ specify all of its generic types.
In the example below, the `Contains` `trait` allows the use of the generic types `A` and `B`. The trait is then implemented for the `Container` type, specifying `i32` for `A` and `B` so that it can be used with `fn difference()`.
Because `Contains` is generic, we are forced to explicitly state _all_ of the generic types for `fn difference()`. In practice, we want a way to express that `A` and `B` are determined by the _input_ `C`. As you will see in the next section, associated types provide exactly that capability.
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














struct Container(i32, i32);





// A trait which checks if 2 items are stored inside of container.


// Also retrieves first or last value.



trait Contains<A, B> {



    fn contains(&self, _: &A, _: &B) -> bool; // Explicitly requires `A` and `B`.



    fn first(&self) -> i32; // Doesn't explicitly require `A` or `B`.



    fn last(&self) -> i32;  // Doesn't explicitly require `A` or `B`.



}





impl Contains<i32, i32> for Container {



    // True if the numbers stored are equal.



    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {




        (&self.0 == number_1) && (&self.1 == number_2)



    }





    // Grab the first number.



    fn first(&self) -> i32 { self.0 }





    // Grab the last number.



    fn last(&self) -> i32 { self.1 }



}




// `C` contains `A` and `B`. In light of that, having to express `A` and


// `B` again is a nuisance.



fn difference<A, B, C>(container: &C) -> i32 where



    C: Contains<A, B> {



    container.last() - container.first()



}





fn main() {



    let number_1 = 3;



    let number_2 = 10;





    let container = Container(number_1, number_2);





    println!("Does container contain {} and {}: {}",




        &number_1, &number_2,




        container.contains(&number_1, &number_2));



    println!("First number: {}", container.first());



    println!("Last number: {}", container.last());





    println!("The difference is: {}", difference(&container));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-45)
[`struct`s](https://doc.rust-lang.org/rust-by-example/print.html#structures), and [`trait`s](https://doc.rust-lang.org/rust-by-example/print.html#traits-2)
