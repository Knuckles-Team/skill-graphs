# [Implementation](https://doc.rust-lang.org/rust-by-example/print.html#implementation)
Similar to functions, implementations require care to remain generic.
```


__

#![allow(unused)]
fn main() {
struct S; // Concrete type `S`
struct GenericVal<T>(T); // Generic type `GenericVal`

// impl of GenericVal where we explicitly specify type parameters:
impl GenericVal<f32> {} // Specify `f32`
impl GenericVal<S> {} // Specify `S` as defined above

// `<T>` Must precede the type to remain generic
impl<T> GenericVal<T> {}
}
```
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














struct Val {



    val: f64,



}





struct GenVal<T> {



    gen_val: T,



}




// impl of Val



impl Val {



    fn value(&self) -> &f64 {




        &self.val


    }



}




// impl of GenVal for a generic type `T`



impl<T> GenVal<T> {



    fn value(&self) -> &T {




        &self.gen_val


    }



}





fn main() {



    let x = Val { val: 3.0 };



    let y = GenVal { gen_val: 3i32 };





    println!("{}, {}", x.value(), y.value());



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-37)
[functions returning references](https://doc.rust-lang.org/rust-by-example/print.html#functions-2), [`impl`](https://doc.rust-lang.org/rust-by-example/print.html#associated-functions--methods), and [`struct`](https://doc.rust-lang.org/rust-by-example/print.html#structures)
