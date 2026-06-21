# [Disambiguating overlapping traits](https://doc.rust-lang.org/rust-by-example/print.html#disambiguating-overlapping-traits)
A type can implement many different traits. What if two traits both require the same name for a function? For example, many traits might have a method named `get()`. They might even have different return types!
Good news: because each trait implementation gets its own `impl` block, it’s clear which trait’s `get` method you’re implementing.
What about when it comes time to _call_ those methods? To disambiguate between them, we have to use Fully Qualified Syntax.
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














trait UsernameWidget {



    // Get the selected username out of this widget



    fn get(&self) -> String;



}





trait AgeWidget {



    // Get the selected age out of this widget



    fn get(&self) -> u8;



}




// A form with both a UsernameWidget and an AgeWidget



struct Form {



    username: String,



    age: u8,



}





impl UsernameWidget for Form {



    fn get(&self) -> String {




        self.username.clone()



    }



}





impl AgeWidget for Form {



    fn get(&self) -> u8 {




        self.age


    }



}





fn main() {



    let form = Form {




        username: "rustacean".to_owned(),




        age: 28,



    };





    // If you uncomment this line, you'll get an error saying



    // "multiple `get` found". Because, after all, there are multiple methods



    // named `get`.



    // println!("{}", form.get());





    let username = <Form as UsernameWidget>::get(&form);



    assert_eq!("rustacean".to_owned(), username);



    let age = <Form as AgeWidget>::get(&form);



    assert_eq!(28, age);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-62)
[The Rust Programming Language chapter on Fully Qualified syntax](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#fully-qualified-syntax-for-disambiguation-calling-methods-with-the-same-name)
