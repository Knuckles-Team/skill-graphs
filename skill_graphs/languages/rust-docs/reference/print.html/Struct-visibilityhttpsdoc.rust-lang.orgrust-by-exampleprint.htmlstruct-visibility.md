# [Struct visibility](https://doc.rust-lang.org/rust-by-example/print.html#struct-visibility)
Structs have an extra level of visibility with their fields. The visibility defaults to private, and can be overridden with the `pub` modifier. This visibility only matters when a struct is accessed from outside the module where it is defined, and has the goal of hiding information (encapsulation).
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














mod my {



    // A public struct with a public field of generic type `T`



    pub struct OpenBox<T> {




        pub contents: T,



    }





    // A public struct with a private field of generic type `T`



    pub struct ClosedBox<T> {




        contents: T,



    }





    impl<T> ClosedBox<T> {




        // A public constructor method




        pub fn new(contents: T) -> ClosedBox<T> {




            ClosedBox {




                contents: contents,




            }




        }



    }



}





fn main() {



    // Public structs with public fields can be constructed as usual



    let open_box = my::OpenBox { contents: "public information" };





    // and their fields can be normally accessed.



    println!("The open box contains: {}", open_box.contents);





    // Public structs with private fields cannot be constructed using field names.



    // Error! `ClosedBox` has private fields



    //let closed_box = my::ClosedBox { contents: "classified information" };



    // TODO ^ Try uncommenting this line





    // However, structs with private fields can be created using



    // public constructors



    let _closed_box = my::ClosedBox::new("classified information");





    // and the private fields of a public struct cannot be accessed.



    // Error! The `contents` field is private



    //println!("The closed box contains: {}", _closed_box.contents);



    // TODO ^ Try uncommenting this line



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-33)
[generics](https://doc.rust-lang.org/rust-by-example/print.html#generics) and [methods](https://doc.rust-lang.org/rust-by-example/print.html#associated-functions--methods)
