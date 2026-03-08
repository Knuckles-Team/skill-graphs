# [Unpacking options and defaults](https://doc.rust-lang.org/rust-by-example/print.html#unpacking-options-and-defaults)
There is more than one way to unpack an `Option` and fall back on a default if it is `None`. To choose the one that meets our needs, we need to consider the following:
  * do we need eager or lazy evaluation?
  * do we need to keep the original empty value intact, or modify it in place?


## [`or()` is chainable, evaluates eagerly, keeps empty value intact](https://doc.rust-lang.org/rust-by-example/print.html#or-is-chainable-evaluates-eagerly-keeps-empty-value-intact)
`or()`is chainable and eagerly evaluates its argument, as is shown in the following example. Note that because `or`’s arguments are evaluated eagerly, the variable passed to `or` is moved.
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













#[derive(Debug)]




enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }






fn main() {



    let apple = Some(Fruit::Apple);



    let orange = Some(Fruit::Orange);



    let no_fruit: Option<Fruit> = None;





    let first_available_fruit = no_fruit.or(orange).or(apple);



    println!("first_available_fruit: {:?}", first_available_fruit);



    // first_available_fruit: Some(Orange)





    // `or` moves its argument.



    // In the example above, `or(orange)` returned a `Some`, so `or(apple)` was not invoked.



    // But the variable named `apple` has been moved regardless, and cannot be used anymore.



    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);



    // TODO: uncomment the line above to see the compiler error



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [`or_else()` is chainable, evaluates lazily, keeps empty value intact](https://doc.rust-lang.org/rust-by-example/print.html#or_else-is-chainable-evaluates-lazily-keeps-empty-value-intact)
Another alternative is to use `or_else`, which is also chainable, and evaluates lazily, as is shown in the following example:
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













#[derive(Debug)]




enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }






fn main() {



    let no_fruit: Option<Fruit> = None;



    let get_kiwi_as_fallback = || {




        println!("Providing kiwi as fallback");




        Some(Fruit::Kiwi)



    };



    let get_lemon_as_fallback = || {




        println!("Providing lemon as fallback");




        Some(Fruit::Lemon)



    };





    let first_available_fruit = no_fruit



        .or_else(get_kiwi_as_fallback)




        .or_else(get_lemon_as_fallback);



    println!("first_available_fruit: {:?}", first_available_fruit);



    // Providing kiwi as fallback



    // first_available_fruit: Some(Kiwi)



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [`get_or_insert()` evaluates eagerly, modifies empty value in place](https://doc.rust-lang.org/rust-by-example/print.html#get_or_insert-evaluates-eagerly-modifies-empty-value-in-place)
To make sure that an `Option` contains a value, we can use `get_or_insert` to modify it in place with a fallback value, as is shown in the following example. Note that `get_or_insert` eagerly evaluates its parameter, so variable `apple` is moved:
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













#[derive(Debug)]




enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }






fn main() {



    let mut my_fruit: Option<Fruit> = None;



    let apple = Fruit::Apple;



    let first_available_fruit = my_fruit.get_or_insert(apple);



    println!("first_available_fruit is: {:?}", first_available_fruit);



    println!("my_fruit is: {:?}", my_fruit);



    // first_available_fruit is: Apple



    // my_fruit is: Some(Apple)



    //println!("Variable named `apple` is moved: {:?}", apple);



    // TODO: uncomment the line above to see the compiler error



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [`get_or_insert_with()` evaluates lazily, modifies empty value in place](https://doc.rust-lang.org/rust-by-example/print.html#get_or_insert_with-evaluates-lazily-modifies-empty-value-in-place)
Instead of explicitly providing a value to fall back on, we can pass a closure to `get_or_insert_with`, as follows:
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













#[derive(Debug)]




enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }






fn main() {



    let mut my_fruit: Option<Fruit> = None;



    let get_lemon_as_fallback = || {




        println!("Providing lemon as fallback");




        Fruit::Lemon


    };



    let first_available_fruit = my_fruit



        .get_or_insert_with(get_lemon_as_fallback);



    println!("first_available_fruit is: {:?}", first_available_fruit);



    println!("my_fruit is: {:?}", my_fruit);



    // Providing lemon as fallback



    // first_available_fruit is: Lemon



    // my_fruit is: Some(Lemon)





    // If the Option has a value, it is left unchanged, and the closure is not invoked



    let mut my_apple = Some(Fruit::Apple);



    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);



    println!("should_be_apple is: {:?}", should_be_apple);



    println!("my_apple is unchanged: {:?}", my_apple);



    // The output is a follows. Note that the closure `get_lemon_as_fallback` is not invoked



    // should_be_apple is: Apple



    // my_apple is unchanged: Some(Apple)



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-65)
[`closures`](https://doc.rust-lang.org/book/ch13-01-closures.html), [`get_or_insert`](https://doc.rust-lang.org/core/option/enum.Option.html#method.get_or_insert), [`get_or_insert_with`](https://doc.rust-lang.org/core/option/enum.Option.html#method.get_or_insert_with), [`moved variables`](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html), [`or`](https://doc.rust-lang.org/core/option/enum.Option.html#method.or), [`or_else`](https://doc.rust-lang.org/core/option/enum.Option.html#method.or_else)
