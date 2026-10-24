# [Ownership and moves](https://doc.rust-lang.org/rust-by-example/print.html#ownership-and-moves)
Because variables are in charge of freeing their own resources, **resources can only have one owner**. This prevents resources from being freed more than once. Note that not all variables own resources (e.g. [references](https://doc.rust-lang.org/rust-by-example/print.html#pointersref)).
When doing assignments (`let x = y`) or passing function arguments by value (`foo(x)`), the _ownership_ of the resources is transferred. In Rust-speak, this is known as a _move_.
After moving resources, the previous owner can no longer be used. This avoids creating dangling pointers.
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













// This function takes ownership of the heap allocated memory



fn destroy_box(c: Box<i32>) {



    println!("Destroying a box that contains {}", c);





    // `c` is destroyed and the memory freed



}





fn main() {



    // _Stack_ allocated integer



    let x = 5u32;





    // *Copy* `x` into `y` - no resources are moved



    let y = x;





    // Both values can be independently used



    println!("x is {}, and y is {}", x, y);





    // `a` is a pointer to a _heap_ allocated integer



    let a = Box::new(5i32);





    println!("a contains: {}", a);





    // *Move* `a` into `b`



    let b = a;



    // The pointer address of `a` is copied (not the data) into `b`.



    // Both are now pointers to the same heap allocated data, but



    // `b` now owns it.





    // Error! `a` can no longer access the data, because it no longer owns the



    // heap memory



    //println!("a contains: {}", a);



    // TODO ^ Try uncommenting this line





    // This function takes ownership of the heap allocated memory from `b`



    destroy_box(b);





    // Since the heap memory has been freed at this point, this action would



    // result in dereferencing freed memory, but it's forbidden by the compiler



    // Error! Same reason as the previous Error



    //println!("b contains: {}", b);



    // TODO ^ Try uncommenting this line



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
