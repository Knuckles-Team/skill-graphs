# [Formatting](https://doc.rust-lang.org/rust-by-example/print.html#formatting)
We’ve seen that formatting is specified via a _format string_ :
  * `format!("{}", foo)` -> `"3735928559"`
  * `format!("0x{:X}", foo)` ->
  * `format!("0o{:o}", foo)` -> `"0o33653337357"`


The same variable (`foo`) can be formatted differently depending on which _argument type_ is used: `X` vs `o` vs _unspecified_.
This formatting functionality is implemented via traits, and there is one trait for each argument type. The most common formatting trait is `Display`, which handles cases where the argument type is left unspecified: `{}` for instance.
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














use std::fmt::{self, Formatter, Display};






struct City {



    name: &'static str,



    // Latitude



    lat: f32,



    // Longitude



    lon: f32,



}





impl Display for City {



    // `f` is a buffer, and this method must write the formatted string into it.



    fn fmt(&self, f: &mut Formatter) -> fmt::Result {




        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };




        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };






        // `write!` is like `format!`, but it will write the formatted string




        // into a buffer (the first argument).




        write!(f, "{}: {:.3}°{} {:.3}°{}",




               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)



    }



}




#[derive(Debug)]




struct Color {



    red: u8,



    green: u8,



    blue: u8,



}





fn main() {



    for city in [




        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },




        City { name: "Oslo", lat: 59.95, lon: 10.75 },




        City { name: "Vancouver", lat: 49.25, lon: -123.1 },



    ] {




        println!("{}", city);



    }



    for color in [




        Color { red: 128, green: 255, blue: 90 },




        Color { red: 0, green: 3, blue: 254 },




        Color { red: 0, green: 0, blue: 0 },



    ] {




        // Switch this to use {} once you've added an implementation




        // for fmt::Display.




        println!("{:?}", color);



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

You can view a [full list of formatting traits](https://doc.rust-lang.org/std/fmt/#formatting-traits) and their argument types in the [`std::fmt`](https://doc.rust-lang.org/std/fmt/) documentation.
### [Activity](https://doc.rust-lang.org/rust-by-example/print.html#activity-3)
Add an implementation of the `fmt::Display` trait for the `Color` struct above so that the output displays as:
```

__
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000

```

Two hints if you get stuck:
  * You [may need to list each color more than once](https://doc.rust-lang.org/std/fmt/#named-parameters).
  * You can [pad with zeros to a width of 2](https://doc.rust-lang.org/std/fmt/#width) with `:0>2`. For hexadecimals, you can use `:02X`.


Bonus:
  * If you would like to experiment with [type casting](https://doc.rust-lang.org/rust-by-example/print.html#casting) in advance, the formula for `RGB = (R * 65_536) + (G * 256) + B`, where `R is RED, G is GREEN, and B is BLUE`. An unsigned 8-bit integer (`u8`) can only hold numbers up to 255. To cast `u8` to `u32`, you can write `variable_name as u32`.


### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-5)
[`std::fmt`](https://doc.rust-lang.org/std/fmt/)
