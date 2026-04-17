# [Overload](https://doc.rust-lang.org/rust-by-example/print.html#overload)
Macros can be overloaded to accept different combinations of arguments. In that regard, `macro_rules!` can work similarly to a match block:
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













// `test!` will compare `$left` and `$right`


// in different ways depending on how you invoke it:


macro_rules! test {



    // Arguments don't need to be separated by a comma.



    // Any template can be used!



    ($left:expr; and $right:expr) => {




        println!("{:?} and {:?} is {:?}",




                 stringify!($left),




                 stringify!($right),




                 $left && $right)



    };



    // ^ each arm must end with a semicolon.



    ($left:expr; or $right:expr) => {




        println!("{:?} or {:?} is {:?}",




                 stringify!($left),




                 stringify!($right),




                 $left || $right)



    };



}





fn main() {



    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);



    test!(true; or false);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
