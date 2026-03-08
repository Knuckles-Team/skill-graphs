# [Coercion](https://doc.rust-lang.org/rust-by-example/print.html#coercion)
A longer lifetime can be coerced into a shorter one so that it works inside a scope it normally wouldn’t work in. This comes in the form of inferred coercion by the Rust compiler, and also in the form of declaring a lifetime difference:
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













// Here, Rust infers a lifetime that is as short as possible.


// The two references are then coerced to that lifetime.



fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {



    first * second


}




// `<'a: 'b, 'b>` reads as lifetime `'a` is at least as long as `'b`.


// Here, we take in an `&'a i32` and return a `&'b i32` as a result of coercion.



fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {



    first


}





fn main() {



    let first = 2; // Longer lifetime





    {




        let second = 3; // Shorter lifetime






        println!("The product is {}", multiply(&first, &second));




        println!("{} is the first", choose_first(&first, &second));



    };



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
