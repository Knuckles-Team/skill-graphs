# [To and from Strings](https://doc.rust-lang.org/rust-by-example/print.html#to-and-from-strings)
## [Converting to String](https://doc.rust-lang.org/rust-by-example/print.html#converting-to-string)
To convert any type to a `String` is as simple as implementing the [`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html) trait for the type. Rather than doing so directly, you should implement the [`fmt::Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html) trait which automatically provides [`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html) and also allows printing the type as discussed in the section on [`print!`](https://doc.rust-lang.org/rust-by-example/print.html#formatted-print).
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














use std::fmt;






struct Circle {



    radius: i32



}





impl fmt::Display for Circle {



    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {




        write!(f, "Circle of radius {}", self.radius)



    }



}





fn main() {



    let circle = Circle { radius: 6 };



    println!("{}", circle.to_string());



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [Parsing a String](https://doc.rust-lang.org/rust-by-example/print.html#parsing-a-string)
It’s useful to convert strings into many types, but one of the more common string operations is to convert them from string to number. The idiomatic approach to this is to use the [`parse`](https://doc.rust-lang.org/std/primitive.str.html#method.parse) function and either to arrange for type inference or to specify the type to parse using the ‘turbofish’ syntax. Both alternatives are shown in the following example.
This will convert the string into the type specified as long as the [`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) trait is implemented for that type. This is implemented for numerous types within the standard library.
```


__



1



2



3



4



5



6



7














fn main() {



    let parsed: i32 = "5".parse().unwrap();



    let turbo_parsed = "10".parse::<i32>().unwrap();





    let sum = parsed + turbo_parsed;



    println!("Sum: {:?}", sum);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

To obtain this functionality on a user defined type simply implement the [`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) trait for that type.
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














use std::num::ParseIntError;




use std::str::FromStr;





#[derive(Debug)]




struct Circle {



    radius: i32,



}





impl FromStr for Circle {



    type Err = ParseIntError;



    fn from_str(s: &str) -> Result<Self, Self::Err> {




        match s.trim().parse() {




            Ok(num) => Ok(Circle{ radius: num }),




            Err(e) => Err(e),




        }



    }



}





fn main() {



    let radius = "    3 ";



    let circle: Circle = radius.parse().unwrap();



    println!("{:?}", circle);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
