# [Threads](https://doc.rust-lang.org/rust-by-example/print.html#threads)
Rust provides a mechanism for spawning native OS threads via the `spawn` function, the argument of this function is a moving closure.
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














use std::thread;






const NTHREADS: u32 = 10;





// This is the `main` thread



fn main() {



    // Make a vector to hold the children which are spawned.



    let mut children = vec![];





    for i in 0..NTHREADS {




        // Spin up another thread




        children.push(thread::spawn(move || {




            println!("this is thread number {}", i);




        }));



    }





    for child in children {




        // Wait for the thread to finish. Returns a result.




        let _ = child.join();



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

These threads will be scheduled by the OS.
