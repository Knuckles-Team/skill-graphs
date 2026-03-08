# [Combinators: `map`](https://doc.rust-lang.org/rust-by-example/print.html#combinators-map)
`match` is a valid method for handling `Option`s. However, you may eventually find heavy usage tedious, especially with operations only valid with an input. In these cases, [combinators](https://doc.rust-lang.org/reference/glossary.html#combinator) can be used to manage control flow in a modular fashion.
`Option` has a built in method called `map()`, a combinator for the simple mapping of `Some -> Some` and `None -> None`. Multiple `map()` calls can be chained together for even more flexibility.
In the following example, `process()` replaces all functions previous to it while staying compact.
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



56



57



58



59



60



61













#![allow(dead_code)]





#[derive(Debug)] enum Food { Apple, Carrot, Potato }





#[derive(Debug)] struct Peeled(Food);



#[derive(Debug)] struct Chopped(Food);



#[derive(Debug)] struct Cooked(Food);





// Peeling food. If there isn't any, then return `None`.


// Otherwise, return the peeled food.



fn peel(food: Option<Food>) -> Option<Peeled> {



    match food {




        Some(food) => Some(Peeled(food)),




        None       => None,



    }



}




// Chopping food. If there isn't any, then return `None`.


// Otherwise, return the chopped food.



fn chop(peeled: Option<Peeled>) -> Option<Chopped> {



    match peeled {




        Some(Peeled(food)) => Some(Chopped(food)),




        None               => None,



    }



}




// Cooking food. Here, we showcase `map()` instead of `match` for case handling.



fn cook(chopped: Option<Chopped>) -> Option<Cooked> {



    chopped.map(|Chopped(food)| Cooked(food))



}




// A function to peel, chop, and cook food all in sequence.


// We chain multiple uses of `map()` to simplify the code.



fn process(food: Option<Food>) -> Option<Cooked> {



    food.map(|f| Peeled(f))




        .map(|Peeled(f)| Chopped(f))




        .map(|Chopped(f)| Cooked(f))



}




// Check whether there's food or not before trying to eat it!



fn eat(food: Option<Cooked>) {



    match food {




        Some(food) => println!("Mmm. I love {:?}", food),




        None       => println!("Oh no! It wasn't edible."),



    }



}





fn main() {



    let apple = Some(Food::Apple);



    let carrot = Some(Food::Carrot);



    let potato = None;





    let cooked_apple = cook(chop(peel(apple)));



    let cooked_carrot = cook(chop(peel(carrot)));



    // Let's try the simpler looking `process()` now.



    let cooked_potato = process(potato);





    eat(cooked_apple);



    eat(cooked_carrot);



    eat(cooked_potato);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-63)
[closures](https://doc.rust-lang.org/rust-by-example/print.html#closures), [`Option`](https://doc.rust-lang.org/std/option/enum.Option.html), [`Option::map()`](https://doc.rust-lang.org/std/option/enum.Option.html#method.map)
