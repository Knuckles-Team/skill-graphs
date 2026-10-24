# [Comments](https://doc.rust-lang.org/rust-by-example/print.html#comments)
Any program requires comments, and Rust supports a few different varieties:
## [Regular Comments](https://doc.rust-lang.org/rust-by-example/print.html#regular-comments)
These are ignored by the compiler:
  * **Line comments** : Start with `//` and continue to the end of the line
  * **Block comments** : Enclosed in `/* ... */` and can span multiple lines


##  [Documentation Comments (Doc Comments) which are parsed into HTML library ](https://doc.rust-lang.org/rust-by-example/print.html#documentation-comments-doc-comments-which-are-parsed-into-html-library-documentation)[documentation](https://doc.rust-lang.org/rust-by-example/print.html#documentation):
  * `///` - Generates docs for the item that follows it
  * `//!` - Generates docs for the enclosing item (typically used at the top of a file or module)

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
















fn main() {



    // Line comments start with two slashes.



    // Everything after the slashes is ignored by the compiler.





    // Example: This line won't execute



    // println!("Hello, world!");





    // Try removing the slashes above and running the code again.





    /*




     * Block comments are useful for temporarily disabling code.




     * They can also be nested: /* like this */ which makes it easy




     * to comment out large sections quickly.




     */





    /*



    Note: The asterisk column on the left is just for style -


    it's not required by the language.



    */





    // Block comments make it easy to toggle code on/off by adding



    // or removing just one slash:





    /* <- Add a '/' here to uncomment the entire block below





    println!("Now");


    println!("everything");


    println!("executes!");


    // Line comments inside remain unaffected





    // */





    // Block comments can also be used within expressions:



    let x = 5 + /* 90 + */ 5;



    println!("Is `x` 10 or 100? x = {}", x);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also)
[Library documentation](https://doc.rust-lang.org/rust-by-example/print.html#documentation)
