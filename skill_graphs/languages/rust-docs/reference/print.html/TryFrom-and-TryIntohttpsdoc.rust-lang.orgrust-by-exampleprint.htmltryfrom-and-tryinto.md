# [`TryFrom` and `TryInto`](https://doc.rust-lang.org/rust-by-example/print.html#tryfrom-and-tryinto)
Similar to [`From` and `Into`](https://doc.rust-lang.org/rust-by-example/print.html#from-and-into), [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html) and [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html) are generic traits for converting between types. Unlike `From`/`Into`, the `TryFrom`/`TryInto` traits are used for fallible conversions, and as such, return [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html)s.
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














use std::convert::TryFrom;




use std::convert::TryInto;





#[derive(Debug, PartialEq)]




struct EvenNumber(i32);






impl TryFrom<i32> for EvenNumber {



    type Error = ();





    fn try_from(value: i32) -> Result<Self, Self::Error> {




        if value % 2 == 0 {




            Ok(EvenNumber(value))




        } else {




            Err(())




        }



    }



}





fn main() {



    // TryFrom





    assert_eq!(EvenNumber::try_from(8), Ok(EvenNumber(8)));



    assert_eq!(EvenNumber::try_from(5), Err(()));





    // TryInto





    let result: Result<EvenNumber, ()> = 8i32.try_into();



    assert_eq!(result, Ok(EvenNumber(8)));



    let result: Result<EvenNumber, ()> = 5i32.try_into();



    assert_eq!(result, Err(()));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
