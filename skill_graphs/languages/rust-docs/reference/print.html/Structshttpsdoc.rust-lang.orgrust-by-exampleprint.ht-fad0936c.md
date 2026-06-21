# [Structs](https://doc.rust-lang.org/rust-by-example/print.html#structs-1)
Annotation of lifetimes in structures are also similar to functions:
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













// A type `Borrowed` which houses a reference to an


// `i32`. The reference to `i32` must outlive `Borrowed`.


#[derive(Debug)]




struct Borrowed<'a>(&'a i32);





// Similarly, both references here must outlive this structure.


#[derive(Debug)]




struct NamedBorrowed<'a> {



    x: &'a i32,



    y: &'a i32,



}




// An enum which is either an `i32` or a reference to one.


#[derive(Debug)]




enum Either<'a> {



    Num(i32),



    Ref(&'a i32),



}





fn main() {



    let x = 18;



    let y = 15;





    let single = Borrowed(&x);



    let double = NamedBorrowed { x: &x, y: &y };



    let reference = Either::Ref(&x);



    let number    = Either::Num(y);





    println!("x is borrowed in {:?}", single);



    println!("x and y are borrowed in {:?}", double);



    println!("x is borrowed in {:?}", reference);



    println!("y is *not* borrowed in {:?}", number);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-54)
[`struct`s](https://doc.rust-lang.org/rust-by-example/print.html#structures)
