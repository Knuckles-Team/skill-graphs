# [Documentation](https://doc.rust-lang.org/rust-by-example/print.html#documentation)
Use `cargo doc` to build documentation in `target/doc`, `cargo doc --open` will automatically open it in your web browser.
Use `cargo test` to run all tests (including documentation tests), and `cargo test --doc` to only run documentation tests.
These commands will appropriately invoke `rustdoc` (and `rustc`) as required.
## [Doc comments](https://doc.rust-lang.org/rust-by-example/print.html#doc-comments)
Doc comments are very useful for big projects that require documentation. When running `rustdoc`, these are the comments that get compiled into documentation. They are denoted by a `///`, and support
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













#![crate_name = "doc"]





/// A human being is represented here



pub struct Person {



    /// A person must have a name, no matter how much Juliet may hate it



    name: String,



}





impl Person {



    /// Creates a person with the given name.



    ///



    /// # Examples



    ///



    /// ```



    /// // You can have rust code between fences inside the comments



    /// // If you pass --test to `rustdoc`, it will even test it for you!



    /// use doc::Person;



    /// let person = Person::new("name");



    /// ```



    pub fn new(name: &str) -> Person {




        Person {




            name: name.to_string(),




        }



    }





    /// Gives a friendly hello!



    ///



    /// Says "Hello, [name](Person::name)" to the `Person` it is called on.



    pub fn hello(&self) {




        println!("Hello, {}!", self.name);



    }



}





fn main() {



    let john = Person::new("John");





    john.hello();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

To run the tests, first build the code as a library, then tell `rustdoc` where to find the library so it can link it into each doctest program:
```

__
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs

```

## [Doc attributes](https://doc.rust-lang.org/rust-by-example/print.html#doc-attributes)
Below are a few examples of the most common `#[doc]` attributes used with `rustdoc`.
### [`inline`](https://doc.rust-lang.org/rust-by-example/print.html#inline)
Used to inline docs, instead of linking out to separate page.
```

__
#[doc(inline)]
pub use bar::Bar;

/// bar docs
pub mod bar {
    /// the docs for Bar
    pub struct Bar;
}
```

### [`no_inline`](https://doc.rust-lang.org/rust-by-example/print.html#no_inline)
Used to prevent linking out to separate page or anywhere.
```

__
// Example from libcore/prelude
#[doc(no_inline)]
pub use crate::mem::drop;
```

### [`hidden`](https://doc.rust-lang.org/rust-by-example/print.html#hidden)
Using this tells `rustdoc` not to include this in documentation:
```

__


1



2



3













// Example from the futures-rs library


#[doc(hidden)]




pub use self::async_await::*;

















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

For documentation, `rustdoc` is widely used by the community. It’s what is used to generate the [std library docs](https://doc.rust-lang.org/std/).
### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-79)
  * [The Rust Book: Making Useful Documentation Comments](https://doc.rust-lang.org/book/ch14-02-publishing-to-crates-io.html#making-useful-documentation-comments)
  * [The rustdoc Book](https://doc.rust-lang.org/rustdoc/index.html)
  * [The Reference: Doc comments](https://doc.rust-lang.org/stable/reference/comments.html#doc-comments)
