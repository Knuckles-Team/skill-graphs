# [Testcase: empty bounds](https://doc.rust-lang.org/rust-by-example/print.html#testcase-empty-bounds)
A consequence of how bounds work is that even if a `trait` doesn’t include any functionality, you can still use it as a bound. `Eq` and `Copy` are examples of such `trait`s from the `std` library.
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














struct Cardinal;




struct BlueJay;




struct Turkey;






trait Red {}




trait Blue {}






impl Red for Cardinal {}




impl Blue for BlueJay {}





// These functions are only valid for types which implement these


// traits. The fact that the traits are empty is irrelevant.



fn red<T: Red>(_: &T)   -> &'static str { "red" }




fn blue<T: Blue>(_: &T) -> &'static str { "blue" }






fn main() {



    let cardinal = Cardinal;



    let blue_jay = BlueJay;



    let _turkey   = Turkey;





    // `red()` won't work on a blue jay nor vice versa



    // because of the bounds.



    println!("A cardinal is {}", red(&cardinal));



    println!("A blue jay is {}", blue(&blue_jay));



    //println!("A turkey is {}", red(&_turkey));



    // ^ TODO: Try uncommenting this line.



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-40)
[`std::cmp::Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html), [`std::marker::Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html), and [`trait`s](https://doc.rust-lang.org/rust-by-example/print.html#traits-2)
