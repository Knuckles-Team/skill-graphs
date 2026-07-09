# [DRY (Don’t Repeat Yourself)](https://doc.rust-lang.org/rust-by-example/print.html#dry-dont-repeat-yourself)
Macros allow writing DRY code by factoring out the common parts of functions and/or test suites. Here is an example that implements and tests the `+=`, `*=` and `-=` operators on `Vec<T>`:
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



43



44



45



46



47



48



49



50



51



52



53



54



55



56



57














use std::ops::{Add, Mul, Sub};





macro_rules! assert_equal_len {



    // The `tt` (token tree) designator is used for



    // operators and tokens.



    ($a:expr, $b:expr, $func:ident, $op:tt) => {




        assert!($a.len() == $b.len(),




                "{:?}: dimension mismatch: {:?} {:?} {:?}",




                stringify!($func),




                ($a.len(),),




                stringify!($op),




                ($b.len(),));



    };



}




macro_rules! op {



    ($func:ident, $bound:ident, $op:tt, $method:ident) => {




        fn $func<T: $bound<T, Output=T> + Copy>(xs: &mut Vec<T>, ys: &Vec<T>) {




            assert_equal_len!(xs, ys, $func, $op);






            for (x, y) in xs.iter_mut().zip(ys.iter()) {




                *x = $bound::$method(*x, *y);




                // *x = x.$method(*y);




            }




        }



    };



}




// Implement `add_assign`, `mul_assign`, and `sub_assign` functions.


op!(add_assign, Add, +=, add);



op!(mul_assign, Mul, *=, mul);



op!(sub_assign, Sub, -=, sub);






mod test {



    use std::iter;



    macro_rules! test {




        ($func:ident, $x:expr, $y:expr, $z:expr) => {




            #[test]




            fn $func() {




                for size in 0usize..10 {




                    let mut x: Vec<_> = iter::repeat($x).take(size).collect();




                    let y: Vec<_> = iter::repeat($y).take(size).collect();




                    let z: Vec<_> = iter::repeat($z).take(size).collect();






                    super::$func(&mut x, &y);






                    assert_eq!(x, z);




                }




            }




        };



    }





    // Test `add_assign`, `mul_assign`, and `sub_assign`.



    test!(add_assign, 1u32, 2u32, 3u32);



    test!(mul_assign, 2u32, 3u32, 6u32);



    test!(sub_assign, 3u32, 2u32, 1u32);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
```

__
$ rustc --test dry.rs && ./dry
running 3 tests
test test::mul_assign ... ok
test test::add_assign ... ok
test test::sub_assign ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured

```
