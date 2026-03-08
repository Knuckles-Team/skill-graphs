# [`?`](https://doc.rust-lang.org/rust-by-example/print.html)
Chaining results using match can get pretty untidy; luckily, the `?` operator can be used to make things pretty again. `?` is used at the end of an expression returning a `Result`, and is equivalent to a match expression, where the `Err(err)` branch expands to an early `return Err(From::from(err))`, and the `Ok(ok)` branch expands to an `ok` expression.
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



59



60



61



62



63














mod checked {



    #[derive(Debug)]



    enum MathError {




        DivisionByZero,




        NonPositiveLogarithm,




        NegativeSquareRoot,



    }





    type MathResult = Result<f64, MathError>;





    fn div(x: f64, y: f64) -> MathResult {




        if y == 0.0 {




            Err(MathError::DivisionByZero)




        } else {




            Ok(x / y)




        }



    }





    fn sqrt(x: f64) -> MathResult {




        if x < 0.0 {




            Err(MathError::NegativeSquareRoot)




        } else {




            Ok(x.sqrt())




        }



    }





    fn ln(x: f64) -> MathResult {




        if x <= 0.0 {




            Err(MathError::NonPositiveLogarithm)




        } else {




            Ok(x.ln())




        }



    }





    // Intermediate function



    fn op_(x: f64, y: f64) -> MathResult {




        // if `div` "fails", then `DivisionByZero` will be `return`ed




        let ratio = div(x, y)?;






        // if `ln` "fails", then `NonPositiveLogarithm` will be `return`ed




        let ln = ln(ratio)?;






        sqrt(ln)



    }





    pub fn op(x: f64, y: f64) {




        match op_(x, y) {




            Err(why) => panic!("{}", match why {




                MathError::NonPositiveLogarithm



                    => "logarithm of non-positive number",




                MathError::DivisionByZero



                    => "division by zero",




                MathError::NegativeSquareRoot



                    => "square root of negative number",




            }),




            Ok(value) => println!("{}", value),




        }



    }



}





fn main() {



    checked::op(1.0, 10.0);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Be sure to check the [documentation](https://doc.rust-lang.org/std/result/index.html), as there are many methods to map/compose `Result`.
