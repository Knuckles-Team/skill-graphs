# [`Result`](https://doc.rust-lang.org/rust-by-example/print.html#result-1)
We’ve seen that the `Option` enum can be used as a return value from functions that may fail, where `None` can be returned to indicate failure. However, sometimes it is important to express _why_ an operation failed. To do this we have the `Result` enum.
The `Result<T, E>` enum has two variants:
  * `Ok(value)` which indicates that the operation succeeded, and wraps the `value` returned by the operation. (`value` has type `T`)
  * `Err(why)`, which indicates that the operation failed, and wraps `why`, which (hopefully) explains the cause of the failure. (`why` has type `E`)

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



58














mod checked {



    // Mathematical "errors" we want to catch



    #[derive(Debug)]



    pub enum MathError {




        DivisionByZero,




        NonPositiveLogarithm,




        NegativeSquareRoot,



    }





    pub type MathResult = Result<f64, MathError>;





    pub fn div(x: f64, y: f64) -> MathResult {




        if y == 0.0 {




            // This operation would `fail`, instead let's return the reason of




            // the failure wrapped in `Err`




            Err(MathError::DivisionByZero)




        } else {




            // This operation is valid, return the result wrapped in `Ok`




            Ok(x / y)




        }



    }





    pub fn sqrt(x: f64) -> MathResult {




        if x < 0.0 {




            Err(MathError::NegativeSquareRoot)




        } else {




            Ok(x.sqrt())




        }



    }





    pub fn ln(x: f64) -> MathResult {




        if x <= 0.0 {




            Err(MathError::NonPositiveLogarithm)




        } else {




            Ok(x.ln())




        }



    }



}




// `op(x, y)` === `sqrt(ln(x / y))`



fn op(x: f64, y: f64) -> f64 {



    // This is a three level match pyramid!



    match checked::div(x, y) {




        Err(why) => panic!("{:?}", why),




        Ok(ratio) => match checked::ln(ratio) {




            Err(why) => panic!("{:?}", why),




            Ok(ln) => match checked::sqrt(ln) {




                Err(why) => panic!("{:?}", why),




                Ok(sqrt) => sqrt,




            },




        },



    }



}





fn main() {



    // Will this fail?



    println!("{}", op(1.0, 10.0));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
