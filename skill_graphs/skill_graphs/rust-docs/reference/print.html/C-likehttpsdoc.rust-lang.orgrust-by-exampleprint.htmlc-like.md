# [C-like](https://doc.rust-lang.org/rust-by-example/print.html#c-like)
`enum` can also be used as C-like enums.
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













// An attribute to hide warnings for unused code.


#![allow(dead_code)]





// enum with implicit discriminator (starts at 0)



enum Number {



    Zero,



    One,



    Two,



}




// enum with explicit discriminator



enum Color {



    Red = 0xff0000,



    Green = 0x00ff00,



    Blue = 0x0000ff,



}





fn main() {



    // `enums` can be cast as integers.



    println!("zero is {}", Number::Zero as i32);



    println!("one is {}", Number::One as i32);





    println!("roses are #{:06x}", Color::Red as u32);



    println!("violets are #{:06x}", Color::Blue as u32);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-10)
[casting](https://doc.rust-lang.org/rust-by-example/print.html#casting)
