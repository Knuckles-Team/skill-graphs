# [New Type Idiom](https://doc.rust-lang.org/rust-by-example/print.html#new-type-idiom)
The `newtype` idiom gives compile time guarantees that the right type of value is supplied to a program.
For example, an age verification function that checks age in years, _must_ be given a value of type `Years`.
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














struct Years(i64);






struct Days(i64);






impl Years {



    pub fn to_days(&self) -> Days {




        Days(self.0 * 365)



    }



}





impl Days {



    /// truncates partial years



    pub fn to_years(&self) -> Years {




        Years(self.0 / 365)



    }



}





fn is_adult(age: &Years) -> bool {



    age.0 >= 18



}





fn main() {



    let age = Years(25);



    let age_days = age.to_days();



    println!("Is an adult? {}", is_adult(&age));



    println!("Is an adult? {}", is_adult(&age_days.to_years()));



    // println!("Is an adult? {}", is_adult(&age_days));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Uncomment the last print statement to observe that the type supplied must be `Years`.
To obtain the `newtype`’s value as the base type, you may use the tuple or destructuring syntax like so:
```


__



1



2



3



4



5



6



7














struct Years(i64);






fn main() {



    let years = Years(42);



    let years_as_primitive_1: i64 = years.0; // Tuple



    let Years(years_as_primitive_2) = years; // Destructuring



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-43)
[`structs`](https://doc.rust-lang.org/rust-by-example/print.html#structures)
