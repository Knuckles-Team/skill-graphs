# [Nesting and labels](https://doc.rust-lang.org/rust-by-example/print.html#nesting-and-labels)
It’s possible to `break` or `continue` outer loops when dealing with nested loops. In these cases, the loops must be annotated with some `'label`, and the label must be passed to the `break`/`continue` statement.
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













#![allow(unreachable_code, unused_labels)]






fn main() {



    'outer: loop {




        println!("Entered the outer loop");






        'inner: loop {




            println!("Entered the inner loop");






            // This would break only the inner loop




            //break;






            // This breaks the outer loop




            break 'outer;




        }






        println!("This point will never be reached");



    }





    println!("Exited the outer loop");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
