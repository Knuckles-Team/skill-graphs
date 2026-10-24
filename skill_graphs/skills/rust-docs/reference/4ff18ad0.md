# [Playground](https://doc.rust-lang.org/rust-by-example/print.html#playground)
The [Rust Playground](https://play.rust-lang.org/) is a way to experiment with Rust code through a web interface.
## [Using it with `mdbook`](https://doc.rust-lang.org/rust-by-example/print.html#using-it-with-mdbook)
In
```


__



1



2



3














fn main() {



    println!("Hello World!");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

This allows the reader to both run your code sample, but also modify and tweak it. The key here is the adding of the word `editable` to your codefence block separated by a comma.
```

__
```rust,editable
//...place your code here
```

```

Additionally, you can add `ignore` if you want `mdbook` to skip your code when it builds and tests.
```

__
```rust,editable,ignore
//...place your code here
```

```

## [Using it with docs](https://doc.rust-lang.org/rust-by-example/print.html#using-it-with-docs)
You may have noticed in some of the [official Rust docs](https://doc.rust-lang.org/core/) a button that says “Run”, which opens the code sample up in a new tab in Rust Playground. This feature is enabled if you use the `#[doc]` attribute called [`html_playground_url`](https://doc.rust-lang.org/rustdoc/write-documentation/the-doc-attribute.html#html_playground_url).
```

__
#![doc(html_playground_url = "https://play.rust-lang.org/")]
//! ```
//! println!("Hello World");
//! ```

```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-80)
  * [The Rust Playground](https://play.rust-lang.org/)
  * [The rustdoc Book](https://doc.rust-lang.org/rustdoc/what-is-rustdoc.html)
