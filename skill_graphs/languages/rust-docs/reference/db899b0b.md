# [Multiple bounds](https://doc.rust-lang.org/rust-by-example/print.html#multiple-bounds)
Multiple bounds for a single type can be applied with a `+`. Like normal, different types are separated with `,`.
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














use std::fmt::{Debug, Display};






fn compare_prints<T: Debug + Display>(t: &T) {



    println!("Debug: `{:?}`", t);



    println!("Display: `{}`", t);



}





fn compare_types<T: Debug, U: Debug>(t: &T, u: &U) {



    println!("t: `{:?}`", t);



    println!("u: `{:?}`", u);



}





fn main() {



    let string = "words";



    let array = [1, 2, 3];



    let vec = vec![1, 2, 3];





    compare_prints(&string);



    //compare_prints(&array);



    // TODO ^ Try uncommenting this.





    compare_types(&array, &vec);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-41)
[`std::fmt`](https://doc.rust-lang.org/rust-by-example/print.html#formatted-print) and [`trait`s](https://doc.rust-lang.org/rust-by-example/print.html#traits-2)
