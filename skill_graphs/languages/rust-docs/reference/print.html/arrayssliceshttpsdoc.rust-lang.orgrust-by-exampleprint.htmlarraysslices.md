# [arrays/slices](https://doc.rust-lang.org/rust-by-example/print.html#arraysslices)
Like tuples, arrays and slices can be destructured this way:
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














fn main() {



    // Try changing the values in the array, or make it a slice!



    let array = [1, -2, 6];





    match array {




        // Binds the second and the third elements to the respective variables




        [0, second, third] =>




            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),






        // Single values can be ignored with _




        [1, _, third] => println!(




            "array[0] = 1, array[2] = {} and array[1] was ignored",




            third



        ),






        // You can also bind some and ignore the rest




        [-1, second, ..] => println!(




            "array[0] = -1, array[1] = {} and all the other ones were ignored",




            second



        ),




        // The code below would not compile




        // [-1, second] => ...






        // Or store them in another array/slice (the type depends on




        // that of the value that is being matched against)




        [3, second, tail @ ..] => println!(




            "array[0] = 3, array[1] = {} and the other elements were {:?}",




            second, tail



        ),






        // Combining these patterns, we can, for example, bind the first and




        // last values, and store the rest of them in a single array




        [first, middle @ .., last] => println!(




            "array[0] = {}, middle = {:?}, array[2] = {}",




            first, middle, last



        ),



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-17)
[Arrays and Slices](https://doc.rust-lang.org/rust-by-example/print.html#arrays-and-slices) and [Binding](https://doc.rust-lang.org/rust-by-example/print.html#binding) for `@` sigil
