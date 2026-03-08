# [for loops](https://doc.rust-lang.org/rust-by-example/print.html#for-loops)
## [for and range](https://doc.rust-lang.org/rust-by-example/print.html#for-and-range)
The `for in` construct can be used to iterate through an `Iterator`. One of the easiest ways to create an iterator is to use the range notation `a..b`. This yields values from `a` (inclusive) to `b` (exclusive) in steps of one.
Let’s write FizzBuzz using `for` instead of `while`.
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














fn main() {



    // `n` will take the values: 1, 2, ..., 100 in each iteration



    for n in 1..101 {




        if n % 15 == 0 {




            println!("fizzbuzz");




        } else if n % 3 == 0 {




            println!("fizz");




        } else if n % 5 == 0 {




            println!("buzz");




        } else {




            println!("{}", n);




        }



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Alternatively, `a..=b` can be used for a range that is inclusive on both ends. The above can be written as:
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














fn main() {



    // `n` will take the values: 1, 2, ..., 100 in each iteration



    for n in 1..=100 {




        if n % 15 == 0 {




            println!("fizzbuzz");




        } else if n % 3 == 0 {




            println!("fizz");




        } else if n % 5 == 0 {




            println!("buzz");




        } else {




            println!("{}", n);




        }



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

## [for and iterators](https://doc.rust-lang.org/rust-by-example/print.html#for-and-iterators)
The `for in` construct is able to interact with an `Iterator` in several ways. As discussed in the section on the [Iterator](https://doc.rust-lang.org/rust-by-example/print.html#iterators) trait, by default the `for` loop will apply the `into_iter` function to the collection. However, this is not the only means of converting collections into iterators.
`into_iter`, `iter` and `iter_mut` all handle the conversion of a collection into an iterator in different ways, by providing different views on the data within.
  * `iter` - This borrows each element of the collection through each iteration. Thus leaving the collection untouched and available for reuse after the loop.

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














fn main() {



    let names = vec!["Bob", "Frank", "Ferris"];





    for name in names.iter() {




        match name {




            &"Ferris" => println!("There is a rustacean among us!"),




            // TODO ^ Try deleting the & and matching just "Ferris"




            _ => println!("Hello {}", name),




        }



    }





    println!("names: {:?}", names);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

  * `into_iter` - This consumes the collection so that on each iteration the exact data is provided. Once the collection has been consumed it is no longer available for reuse as it has been ‘moved’ within the loop.

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














fn main() {



    let names = vec!["Bob", "Frank", "Ferris"];





    for name in names.into_iter() {




        match name {




            "Ferris" => println!("There is a rustacean among us!"),




            _ => println!("Hello {}", name),




        }



    }





    println!("names: {:?}", names);



    // FIXME ^ Comment out this line



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

  * `iter_mut` - This mutably borrows each element of the collection, allowing for the collection to be modified in place.

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














fn main() {



    let mut names = vec!["Bob", "Frank", "Ferris"];





    for name in names.iter_mut() {




        *name = match name {




            &mut "Ferris" => "There is a rustacean among us!",




            _ => "Hello",




        }



    }





    println!("names: {:?}", names);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

In the above snippets note the type of `match` branch, that is the key difference in the types of iteration. The difference in type then of course implies differing actions that are able to be performed.
### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-14)
[Iterator](https://doc.rust-lang.org/rust-by-example/print.html#iterators)
