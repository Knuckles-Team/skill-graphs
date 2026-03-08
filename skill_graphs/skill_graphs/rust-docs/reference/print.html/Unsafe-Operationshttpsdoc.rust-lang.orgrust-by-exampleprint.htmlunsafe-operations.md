# [Unsafe Operations](https://doc.rust-lang.org/rust-by-example/print.html#unsafe-operations)
As an introduction to this section, to borrow from [the official docs](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html), “one should try to minimize the amount of unsafe code in a code base.” With that in mind, let’s get started! Unsafe annotations in Rust are used to bypass protections put in place by the compiler; specifically, there are four primary things that unsafe is used for:
  * dereferencing raw pointers
  * calling functions or methods which are `unsafe` (including calling a function over FFI, see [a previous chapter](https://doc.rust-lang.org/rust-by-example/print.html#foreign-function-interface) of the book)
  * accessing or modifying static mutable variables
  * implementing unsafe traits


### [Raw Pointers](https://doc.rust-lang.org/rust-by-example/print.html#raw-pointers)
Raw pointers `*` and references `&T` function similarly, but references are always safe because they are guaranteed to point to valid data due to the borrow checker. Dereferencing a raw pointer can only be done through an unsafe block.
```


__



1



2



3



4



5



6



7














fn main() {



    let raw_p: *const u32 = &10;





    unsafe {




        assert!(*raw_p == 10);



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [Calling Unsafe Functions](https://doc.rust-lang.org/rust-by-example/print.html#calling-unsafe-functions)
Some functions can be declared as `unsafe`, meaning it is the programmer’s responsibility to ensure correctness instead of the compiler’s. One example of this is [`std::slice::from_raw_parts`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html) which will create a slice given a pointer to the first element and a length.
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














use std::slice;






fn main() {



    let some_vector = vec![1, 2, 3, 4];





    let pointer = some_vector.as_ptr();



    let length = some_vector.len();





    unsafe {




        let my_slice: &[u32] = slice::from_raw_parts(pointer, length);






        assert_eq!(some_vector.as_slice(), my_slice);



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

For `slice::from_raw_parts`, one of the assumptions which _must_ be upheld is that the pointer passed in points to valid memory and that the memory pointed to is of the correct type. If these invariants aren’t upheld then the program’s behaviour is undefined and there is no knowing what will happen.
