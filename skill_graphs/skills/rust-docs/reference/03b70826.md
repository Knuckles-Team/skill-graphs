# [Enums](https://doc.rust-lang.org/rust-by-example/print.html#enums)
The `enum` keyword allows the creation of a type which may be one of a few different variants. Any variant which is valid as a `struct` is also valid in an `enum`.
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













// Create an `enum` to classify a web event. Note how both


// names and type information together specify the variant:


// `PageLoad != PageUnload` and `KeyPress(char) != Paste(String)`.


// Each is different and independent.



enum WebEvent {



    // An `enum` variant may either be `unit-like`,



    PageLoad,



    PageUnload,



    // like tuple structs,



    KeyPress(char),



    Paste(String),



    // or c-like structures.



    Click { x: i64, y: i64 },



}




// A function which takes a `WebEvent` enum as an argument and


// returns nothing.



fn inspect(event: WebEvent) {



    match event {




        WebEvent::PageLoad => println!("page loaded"),




        WebEvent::PageUnload => println!("page unloaded"),




        // Destructure `c` from inside the `enum` variant.




        WebEvent::KeyPress(c) => println!("pressed '{}'.", c),




        WebEvent::Paste(s) => println!("pasted \"{}\".", s),




        // Destructure `Click` into `x` and `y`.




        WebEvent::Click { x, y } => {




            println!("clicked at x={}, y={}.", x, y);




        },



    }



}





fn main() {



    let pressed = WebEvent::KeyPress('x');



    // `to_owned()` creates an owned `String` from a string slice.



    let pasted  = WebEvent::Paste("my text".to_owned());



    let click   = WebEvent::Click { x: 20, y: 80 };



    let load    = WebEvent::PageLoad;



    let unload  = WebEvent::PageUnload;





    inspect(pressed);



    inspect(pasted);



    inspect(click);



    inspect(load);



    inspect(unload);



}


















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [Type aliases](https://doc.rust-lang.org/rust-by-example/print.html#type-aliases)
If you use a type alias, you can refer to each enum variant via its alias. This might be useful if the enum’s name is too long or too generic, and you want to rename it.
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














enum VeryVerboseEnumOfThingsToDoWithNumbers {



    Add,



    Subtract,



}




// Creates a type alias



type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;






fn main() {



    // We can refer to each variant via its alias, not its long and inconvenient



    // name.



    let x = Operations::Add;



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

The most common place you’ll see this is in `impl` blocks using the `Self` alias.
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














enum VeryVerboseEnumOfThingsToDoWithNumbers {



    Add,



    Subtract,



}





impl VeryVerboseEnumOfThingsToDoWithNumbers {



    fn run(&self, x: i32, y: i32) -> i32 {




        match self {




            Self::Add => x + y,




            Self::Subtract => x - y,




        }



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

To learn more about enums and type aliases, you can read the
### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-8)
[`match`](https://doc.rust-lang.org/rust-by-example/print.html#match), [`fn`](https://doc.rust-lang.org/rust-by-example/print.html#functions), and [`String`](https://doc.rust-lang.org/rust-by-example/print.html#strings),
