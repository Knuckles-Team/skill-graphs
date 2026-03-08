# [RAII](https://doc.rust-lang.org/rust-by-example/print.html#raii)
Variables in Rust do more than just hold data in the stack: they also _own_ resources, e.g. `Box<T>` owns memory in the heap. Rust enforces
This behavior shields against _resource leak_ bugs, so you’ll never have to manually free memory or worry about memory leaks again! Here’s a quick showcase:
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













// raii.rs



fn create_box() {



    // Allocate an integer on the heap



    let _box1 = Box::new(3i32);





    // `_box1` is destroyed here, and memory gets freed



}





fn main() {



    // Allocate an integer on the heap



    let _box2 = Box::new(5i32);





    // A nested scope:



    {




        // Allocate an integer on the heap




        let _box3 = Box::new(4i32);






        // `_box3` is destroyed here, and memory gets freed



    }





    // Creating lots of boxes just for fun



    // There's no need to manually free memory!



    for _ in 0u32..1_000 {




        create_box();



    }





    // `_box2` is destroyed here, and memory gets freed



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Of course, we can double check for memory errors using
```

__
$ rustc raii.rs && valgrind ./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command: ./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)

```

No leaks here!
## [Destructor](https://doc.rust-lang.org/rust-by-example/print.html#destructor)
The notion of a destructor in Rust is provided through the [`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html) trait. The destructor is called when the resource goes out of scope. This trait is not required to be implemented for every type, only implement it for your type if you require its own destructor logic.
Run the below example to see how the [`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html) trait works. When the variable in the `main` function goes out of scope the custom destructor will be invoked.
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














struct ToDrop;






impl Drop for ToDrop {



    fn drop(&mut self) {




        println!("ToDrop is being dropped");



    }



}





fn main() {



    let x = ToDrop;



    println!("Made a ToDrop!");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-48)
[Box](https://doc.rust-lang.org/rust-by-example/print.html#box-stack-and-heap)
