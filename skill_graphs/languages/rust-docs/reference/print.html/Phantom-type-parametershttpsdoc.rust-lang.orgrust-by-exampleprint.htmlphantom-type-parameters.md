# [Phantom type parameters](https://doc.rust-lang.org/rust-by-example/print.html#phantom-type-parameters)
A phantom type parameter is one that doesn’t show up at runtime, but is checked statically (and only) at compile time.
Data types can use extra generic type parameters to act as markers or to perform type checking at compile time. These extra parameters hold no storage values, and have no runtime behavior.
In the following example, we combine [std::marker::PhantomData](https://doc.rust-lang.org/std/marker/struct.PhantomData.html) with the phantom type parameter concept to create tuples containing different data types.
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














use std::marker::PhantomData;





// A phantom tuple struct which is generic over `A` with hidden parameter `B`.


#[derive(PartialEq)] // Allow equality test for this type.




struct PhantomTuple<A, B>(A, PhantomData<B>);





// A phantom type struct which is generic over `A` with hidden parameter `B`.


#[derive(PartialEq)] // Allow equality test for this type.




struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }





// Note: Storage is allocated for generic type `A`, but not for `B`.


//       Therefore, `B` cannot be used in computations.





fn main() {



    // Here, `f32` and `f64` are the hidden parameters.



    // PhantomTuple type specified as `<char, f32>`.



    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);



    // PhantomTuple type specified as `<char, f64>`.



    let _tuple2: PhantomTuple<char, f64> = PhantomTuple('Q', PhantomData);





    // Type specified as `<char, f32>`.



    let _struct1: PhantomStruct<char, f32> = PhantomStruct {




        first: 'Q',




        phantom: PhantomData,



    };



    // Type specified as `<char, f64>`.



    let _struct2: PhantomStruct<char, f64> = PhantomStruct {




        first: 'Q',




        phantom: PhantomData,



    };





    // Compile-time Error! Type mismatch so these cannot be compared:



    // println!("_tuple1 == _tuple2 yields: {}",



    //           _tuple1 == _tuple2);





    // Compile-time Error! Type mismatch so these cannot be compared:



    // println!("_struct1 == _struct2 yields: {}",



    //           _struct1 == _struct2);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-46)
[Derive](https://doc.rust-lang.org/rust-by-example/print.html#derive), [struct](https://doc.rust-lang.org/rust-by-example/print.html#structures), and [tuple](https://doc.rust-lang.org/rust-by-example/print.html#tuples).
