# [Testcase: List](https://doc.rust-lang.org/rust-by-example/print.html#testcase-list)
Implementing `fmt::Display` for a structure where the elements must each be handled sequentially is tricky. The problem is that each `write!` generates a `fmt::Result`. Proper handling of this requires dealing with _all_ the results. Rust provides the `?` operator for exactly this purpose.
Using `?` on `write!` looks like this:
```

__
// Try `write!` to see if it errors. If it errors, return
// the error. Otherwise continue.
write!(f, "{}", value)?;
```

With `?` available, implementing `fmt::Display` for a `Vec` is straightforward:
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














use std::fmt; // Import the `fmt` module.





// Define a structure named `List` containing a `Vec`.



struct List(Vec<i32>);






impl fmt::Display for List {



    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {




        // Extract the value using tuple indexing,




        // and create a reference to `vec`.




        let vec = &self.0;






        write!(f, "[")?;






        // Iterate over `v` in `vec` while enumerating the iteration




        // index in `index`.




        for (index, v) in vec.iter().enumerate() {




            // For every element except the first, add a comma.




            // Use the ? operator to return on errors.




            if index != 0 { write!(f, ", ")?; }




            write!(f, "{}", v)?;




        }






        // Close the opened bracket and return a fmt::Result value.




        write!(f, "]")



    }



}





fn main() {



    let v = List(vec![1, 2, 3]);



    println!("{}", v);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [Activity](https://doc.rust-lang.org/rust-by-example/print.html#activity-2)
Try changing the program so that the index of each element in the vector is also printed. The new output should look like this:
```

__
[0: 1, 1: 2, 2: 3]
```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-4)
[`for`](https://doc.rust-lang.org/rust-by-example/print.html#for-loops), [`ref`](https://doc.rust-lang.org/rust-by-example/print.html#the-ref-pattern), [`Result`](https://doc.rust-lang.org/rust-by-example/print.html#result-1), [`struct`](https://doc.rust-lang.org/rust-by-example/print.html#structures), [`?`](https://doc.rust-lang.org/rust-by-example/print.html), and [`vec!`](https://doc.rust-lang.org/rust-by-example/print.html#vectors)
