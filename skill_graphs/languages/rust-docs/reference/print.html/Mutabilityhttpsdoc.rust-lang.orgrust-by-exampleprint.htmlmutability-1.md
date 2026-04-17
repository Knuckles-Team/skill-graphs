# [Mutability](https://doc.rust-lang.org/rust-by-example/print.html#mutability-1)
Mutability of data can be changed when ownership is transferred.
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














fn main() {



    let immutable_box = Box::new(5u32);





    println!("immutable_box contains {}", immutable_box);





    // Mutability error



    //*immutable_box = 4;





    // *Move* the box, changing the ownership (and mutability)



    let mut mutable_box = immutable_box;





    println!("mutable_box contains {}", mutable_box);





    // Modify the contents of the box



    *mutable_box = 4;





    println!("mutable_box now contains {}", mutable_box);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
