# [while let](https://doc.rust-lang.org/rust-by-example/print.html#while-let)
Similar to `if let`, `while let` can make awkward `match` sequences more tolerable. Consider the following sequence that increments `i`:
```


__

#![allow(unused)]
fn main() {
// Make `optional` of type `Option<i32>`
let mut optional = Some(0);

// Repeatedly try this test.
loop {
    match optional {
        // If `optional` destructures, evaluate the block.
        Some(i) => {
            if i > 9 {
                println!("Greater than 9, quit!");
                optional = None;
            } else {
                println!("`i` is `{:?}`. Try again.", i);
                optional = Some(i + 1);
            }
            // ^ Requires 3 indentations!
        },
        // Quit the loop when the destructure fails:
        _ => { break; }
        // ^ Why should this be required? There must be a better way!
    }
}
}
```

Using `while let` makes this sequence much nicer:
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














fn main() {



    // Make `optional` of type `Option<i32>`



    let mut optional = Some(0);





    // This reads: "while `let` destructures `optional` into



    // `Some(i)`, evaluate the block (`{}`). Else `break`.



    while let Some(i) = optional {




        if i > 9 {




            println!("Greater than 9, quit!");




            optional = None;




        } else {




            println!("`i` is `{:?}`. Try again.", i);




            optional = Some(i + 1);




        }




        // ^ Less rightward drift and doesn't require




        // explicitly handling the failing case.



    }



    // ^ `if let` had additional optional `else`/`else if`



    // clauses. `while let` does not have these.



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-25)
[`enum`](https://doc.rust-lang.org/rust-by-example/print.html#enums), [`Option`](https://doc.rust-lang.org/rust-by-example/print.html#option), and the
