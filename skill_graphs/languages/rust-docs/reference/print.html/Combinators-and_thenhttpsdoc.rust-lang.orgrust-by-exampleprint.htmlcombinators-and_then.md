# [Combinators: `and_then`](https://doc.rust-lang.org/rust-by-example/print.html#combinators-and_then)
`map()` was described as a chainable way to simplify `match` statements. However, using `map()` on a function that returns an `Option<T>` results in the nested `Option<Option<T>>`. Chaining multiple calls together can then become confusing. That’s where another combinator called `and_then()`, known in some languages as flatmap, comes in.
`and_then()` calls its function input with the wrapped value and returns the result. If the `Option` is `None`, then it returns `None` instead.
In the following example, `cookable_v3()` results in an `Option<Food>`. Using `map()` instead of `and_then()` would have given an `Option<Option<Food>>`, which is an invalid type for `eat()`.
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



52



53



54



55













#![allow(dead_code)]





#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }



#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }





// We don't have the ingredients to make Sushi.



fn have_ingredients(food: Food) -> Option<Food> {



    match food {




        Food::Sushi => None,




        _           => Some(food),



    }



}




// We have the recipe for everything except Cordon Bleu.



fn have_recipe(food: Food) -> Option<Food> {



    match food {




        Food::CordonBleu => None,




        _                => Some(food),



    }



}




// To make a dish, we need both the recipe and the ingredients.


// We can represent the logic with a chain of `match`es:



fn cookable_v1(food: Food) -> Option<Food> {



    match have_recipe(food) {




        None       => None,




        Some(food) => have_ingredients(food),



    }



}




// This can conveniently be rewritten more compactly with `and_then()`:



fn cookable_v3(food: Food) -> Option<Food> {



    have_recipe(food).and_then(have_ingredients)



}




// Otherwise we'd need to `flatten()` an `Option<Option<Food>>`


// to get an `Option<Food>`:



fn cookable_v2(food: Food) -> Option<Food> {



    have_recipe(food).map(have_ingredients).flatten()



}





fn eat(food: Food, day: Day) {



    match cookable_v3(food) {




        Some(food) => println!("Yay! On {:?} we get to eat {:?}.", day, food),




        None       => println!("Oh no. We don't get to eat on {:?}?", day),



    }



}





fn main() {



    let (cordon_bleu, steak, sushi) = (Food::CordonBleu, Food::Steak, Food::Sushi);





    eat(cordon_bleu, Day::Monday);



    eat(steak, Day::Tuesday);



    eat(sushi, Day::Wednesday);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-64)
[closures](https://doc.rust-lang.org/rust-by-example/print.html#closures), [`Option`](https://doc.rust-lang.org/std/option/enum.Option.html), [`Option::and_then()`](https://doc.rust-lang.org/std/option/enum.Option.html#method.and_then), and [`Option::flatten()`](https://doc.rust-lang.org/std/option/enum.Option.html#method.flatten)
