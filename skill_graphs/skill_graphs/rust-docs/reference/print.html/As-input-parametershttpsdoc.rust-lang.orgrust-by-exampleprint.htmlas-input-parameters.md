# [As input parameters](https://doc.rust-lang.org/rust-by-example/print.html#as-input-parameters)
While Rust chooses how to capture variables on the fly mostly without type annotation, this ambiguity is not allowed when writing functions. When taking a closure as an input parameter, the closure’s complete type must be annotated using one of a few `traits`, and they’re determined by what the closure does with captured value. In order of decreasing restriction, they are:
  * `Fn`: the closure uses the captured value by reference (`&T`)
  * `FnMut`: the closure uses the captured value by mutable reference (`&mut T`)
  * `FnOnce`: the closure uses the captured value by value (`T`)


On a variable-by-variable basis, the compiler will capture variables in the least restrictive manner possible.
For instance, consider a parameter annotated as `FnOnce`. This specifies that the closure _may_ capture by `&T`, `&mut T`, or `T`, but the compiler will ultimately choose based on how the captured variables are used in the closure.
This is because if a move is possible, then any type of borrow should also be possible. Note that the reverse is not true. If the parameter is annotated as `Fn`, then capturing variables by `&mut T` or `T` are not allowed. However, `&T` is allowed.
In the following example, try swapping the usage of `Fn`, `FnMut`, and `FnOnce` to see what happens:
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



49



50



51













// A function which takes a closure as an argument and calls it.


// <F> denotes that F is a "Generic type parameter"



fn apply<F>(f: F) where



    // The closure takes no input and returns nothing.



    F: FnOnce() {



    // ^ TODO: Try changing this to `Fn` or `FnMut`.





    f();



}




// A function which takes a closure and returns an `i32`.



fn apply_to_3<F>(f: F) -> i32 where



    // The closure takes an `i32` and returns an `i32`.



    F: Fn(i32) -> i32 {





    f(3)



}





fn main() {



    use std::mem;





    let greeting = "hello";



    // A non-copy type.



    // `to_owned` creates owned data from borrowed one



    let mut farewell = "goodbye".to_owned();





    // Capture 2 variables: `greeting` by reference and



    // `farewell` by value.



    let diary = || {




        // `greeting` is by reference: requires `Fn`.




        println!("I said {}.", greeting);






        // Mutation forces `farewell` to be captured by




        // mutable reference. Now requires `FnMut`.




        farewell.push_str("!!!");




        println!("Then I screamed {}.", farewell);




        println!("Now I can sleep. zzzzz");






        // Manually calling drop forces `farewell` to




        // be captured by value. Now requires `FnOnce`.




        mem::drop(farewell);



    };





    // Call the function which applies the closure.



    apply(diary);





    // `double` satisfies `apply_to_3`'s trait bound



    let double = |x| 2 * x;





    println!("3 doubled: {}", apply_to_3(double));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-27)
[`std::mem::drop`](https://doc.rust-lang.org/std/mem/fn.drop.html), [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html), [Generics](https://doc.rust-lang.org/rust-by-example/print.html#generics), [where](https://doc.rust-lang.org/rust-by-example/print.html#where-clauses) and [`FnOnce`](https://doc.rust-lang.org/std/ops/trait.FnOnce.html)
