# [As output parameters](https://doc.rust-lang.org/rust-by-example/print.html#as-output-parameters)
Closures as input parameters are possible, so returning closures as output parameters should also be possible. However, anonymous closure types are, by definition, unknown, so we have to use `impl Trait` to return them.
The valid traits for returning a closure are:
  * `Fn`
  * `FnMut`
  * `FnOnce`


Beyond this, the `move` keyword must be used, which signals that all captures occur by value. This is required because any captures by reference would be dropped as soon as the function exited, leaving invalid references in the closure.
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














fn create_fn() -> impl Fn() {



    let text = "Fn".to_owned();





    move || println!("This is a: {}", text)



}





fn create_fnmut() -> impl FnMut() {



    let text = "FnMut".to_owned();





    move || println!("This is a: {}", text)



}





fn create_fnonce() -> impl FnOnce() {



    let text = "FnOnce".to_owned();





    move || println!("This is a: {}", text)



}





fn main() {



    let fn_plain = create_fn();



    let mut fn_mut = create_fnmut();



    let fn_once = create_fnonce();





    fn_plain();



    fn_mut();



    fn_once();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-30)
[`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html), [Generics](https://doc.rust-lang.org/rust-by-example/print.html#generics) and [impl Trait](https://doc.rust-lang.org/rust-by-example/print.html#impl-trait).
