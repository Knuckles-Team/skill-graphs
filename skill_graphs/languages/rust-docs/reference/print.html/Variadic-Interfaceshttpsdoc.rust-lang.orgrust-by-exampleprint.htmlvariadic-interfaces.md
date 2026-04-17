# [Variadic Interfaces](https://doc.rust-lang.org/rust-by-example/print.html#variadic-interfaces)
A _variadic_ interface takes an arbitrary number of arguments. For example, `println!` can take an arbitrary number of arguments, as determined by the format string.
We can extend our `calculate!` macro from the previous section to be variadic:
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













macro_rules! calculate {



    // The pattern for a single `eval`



    (eval $e:expr) => {




        {




            let val: usize = $e; // Force types to be integers




            println!("{} = {}", stringify!{$e}, val);




        }



    };





    // Decompose multiple `eval`s recursively



    (eval $e:expr, $(eval $es:expr),+) => {{




        calculate! { eval $e }




        calculate! { $(eval $es),+ }



    }};



}





fn main() {



    calculate! { // Look ma! Variadic `calculate!`!




        eval 1 + 2,




        eval 3 + 4,




        eval (2 * 3) + 1



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Output:
```

__
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7

```
