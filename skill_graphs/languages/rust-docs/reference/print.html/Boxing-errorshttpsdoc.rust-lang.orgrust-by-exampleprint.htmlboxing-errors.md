# [`Box`ing errors](https://doc.rust-lang.org/rust-by-example/print.html#boxing-errors)
A way to write simple code while preserving the original errors is to [`Box`](https://doc.rust-lang.org/std/boxed/struct.Box.html) them. The drawback is that the underlying error type is only known at runtime and not [statically determined](https://doc.rust-lang.org/book/ch17-02-trait-objects.html#trait-objects-perform-dynamic-dispatch).
The stdlib helps in boxing our errors by having `Box` implement conversion from any type that implements the `Error` trait into the trait object `Box<Error>`, via [`From`](https://doc.rust-lang.org/std/convert/trait.From.html).
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














use std::error;




use std::fmt;





// Change the alias to use `Box<dyn error::Error>`.



type Result<T> = std::result::Result<T, Box<dyn error::Error>>;





#[derive(Debug, Clone)]




struct EmptyVec;






impl fmt::Display for EmptyVec {



    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {




        write!(f, "invalid first item to double")



    }



}





impl error::Error for EmptyVec {}






fn double_first(vec: Vec<&str>) -> Result<i32> {



    vec.first()




        .ok_or_else(|| EmptyVec.into()) // Converts to Box using Into trait.




        .and_then(|s| {




            s.parse::<i32>()




                .map_err(From::from) // Converts to Box using From::from fn pointer.




                .map(|i| 2 * i)




        })



}





fn print(result: Result<i32>) {



    match result {




        Ok(n) => println!("The first doubled is {}", n),




        Err(e) => println!("Error: {}", e),



    }



}





fn main() {



    let numbers = vec!["42", "93", "18"];



    let empty = vec![];



    let strings = vec!["tofu", "93", "18"];





    print(double_first(numbers));



    print(double_first(empty));



    print(double_first(strings));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-67)
[Dynamic dispatch](https://doc.rust-lang.org/book/ch17-02-trait-objects.html#trait-objects-perform-dynamic-dispatch) and [`Error` trait](https://doc.rust-lang.org/std/error/trait.Error.html)
