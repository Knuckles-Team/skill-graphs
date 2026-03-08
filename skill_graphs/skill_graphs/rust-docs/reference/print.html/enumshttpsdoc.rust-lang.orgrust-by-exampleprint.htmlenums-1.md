# [enums](https://doc.rust-lang.org/rust-by-example/print.html#enums-1)
An `enum` is destructured similarly:
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













// `allow` required to silence warnings because only


// one variant is used.


#[allow(dead_code)]




enum Color {



    // These 3 are specified solely by their name.



    Red,



    Blue,



    Green,



    // These likewise tie `u32` tuples to different names: color models.



    RGB(u32, u32, u32),



    HSV(u32, u32, u32),



    HSL(u32, u32, u32),



    CMY(u32, u32, u32),



    CMYK(u32, u32, u32, u32),



}





fn main() {



    let color = Color::RGB(122, 17, 40);



    // TODO ^ Try different variants for `color`





    println!("What color is it?");



    // An `enum` can be destructured using a `match`.



    match color {




        Color::Red   => println!("The color is Red!"),




        Color::Blue  => println!("The color is Blue!"),




        Color::Green => println!("The color is Green!"),




        Color::RGB(r, g, b) =>




            println!("Red: {}, green: {}, and blue: {}!", r, g, b),




        Color::HSV(h, s, v) =>




            println!("Hue: {}, saturation: {}, value: {}!", h, s, v),




        Color::HSL(h, s, l) =>




            println!("Hue: {}, saturation: {}, lightness: {}!", h, s, l),




        Color::CMY(c, m, y) =>




            println!("Cyan: {}, magenta: {}, yellow: {}!", c, m, y),




        Color::CMYK(c, m, y, k) =>




            println!("Cyan: {}, magenta: {}, yellow: {}, key (black): {}!",




                c, m, y, k),




        // Don't need another arm because all variants have been examined



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-18)
[`#[allow(...)]`](https://doc.rust-lang.org/rust-by-example/print.html#dead_code), [`enum`](https://doc.rust-lang.org/rust-by-example/print.html#enums)
