# [Traits](https://doc.rust-lang.org/rust-by-example/print.html#traits)
Of course `trait`s can also be generic. Here we define one which reimplements the `Drop` `trait` as a generic method to `drop` itself and an input.
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













// Non-copyable types.



struct Empty;




struct Null;





// A trait generic over `T`.



trait DoubleDrop<T> {



    // Define a method on the caller type which takes an



    // additional single parameter `T` and does nothing with it.



    fn double_drop(self, _: T);



}




// Implement `DoubleDrop<T>` for any generic parameter `T` and


// caller `U`.



impl<T, U> DoubleDrop<T> for U {



    // This method takes ownership of both passed arguments,



    // deallocating both.



    fn double_drop(self, _: T) {}



}





fn main() {



    let empty = Empty;



    let null  = Null;





    // Deallocate `empty` and `null`.



    empty.double_drop(null);





    //empty;



    //null;



    // ^ TODO: Try uncommenting these lines.



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-38)
[`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html), [`struct`](https://doc.rust-lang.org/rust-by-example/print.html#structures), and [`trait`](https://doc.rust-lang.org/rust-by-example/print.html#traits-2)
