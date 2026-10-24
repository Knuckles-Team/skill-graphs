# [Traits](https://doc.rust-lang.org/rust-by-example/print.html#traits-1)
Annotation of lifetimes in trait methods basically are similar to functions. Note that `impl` may have annotation of lifetimes too.
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













// A struct with annotation of lifetimes.


#[derive(Debug)]




struct Borrowed<'a> {



    x: &'a i32,



}




// Annotate lifetimes to impl.



impl<'a> Default for Borrowed<'a> {



    fn default() -> Self {




        Self {




            x: &10,




        }



    }



}





fn main() {



    let b: Borrowed = Default::default();



    println!("b is {:?}", b);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-55)
[`trait`s](https://doc.rust-lang.org/rust-by-example/print.html#traits-2)
