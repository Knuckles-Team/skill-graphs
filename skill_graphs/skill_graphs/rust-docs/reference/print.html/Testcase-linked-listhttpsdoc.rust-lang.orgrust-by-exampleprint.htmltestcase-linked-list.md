# [Testcase: linked-list](https://doc.rust-lang.org/rust-by-example/print.html#testcase-linked-list)
A common way to implement a linked-list is via `enums`:
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



62



63



64



65



66



67



68



69



70














use crate::List::*;






enum List {



    // Cons: Tuple struct that wraps an element and a pointer to the next node



    Cons(u32, Box<List>),



    // Nil: A node that signifies the end of the linked list



    Nil,



}




// Methods can be attached to an enum



impl List {



    // Create an empty list



    fn new() -> List {




        // `Nil` has type `List`




        Nil


    }





    // Consume a list, and return the same list with a new element at its front



    fn prepend(self, elem: u32) -> List {




        // `Cons` also has type List




        Cons(elem, Box::new(self))



    }





    // Return the length of the list



    fn len(&self) -> u32 {




        // `self` has to be matched, because the behavior of this method




        // depends on the variant of `self`




        // `self` has type `&List`, and `*self` has type `List`, matching on a




        // concrete type `T` is preferred over a match on a reference `&T`




        // after Rust 2018 you can use self here and tail (with no ref) below as well,




        // rust will infer &s and ref tail.




        // See https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html




        match *self {




            // Can't take ownership of the tail, because `self` is borrowed;




            // instead take a reference to the tail




            // And it's a non-tail recursive call which may cause stack overflow for long lists.




            Cons(_, ref tail) => 1 + tail.len(),




            // Base Case: An empty list has zero length




            Nil => 0




        }



    }





    // Return representation of the list as a (heap allocated) string



    fn stringify(&self) -> String {




        match *self {




            Cons(head, ref tail) => {




                // `format!` is similar to `print!`, but returns a heap




                // allocated string instead of printing to the console




                format!("{}, {}", head, tail.stringify())




            },




            Nil => {




                format!("Nil")




            },




        }



    }



}





fn main() {



    // Create an empty linked list



    let mut list = List::new();





    // Prepend some elements



    list = list.prepend(1);



    list = list.prepend(2);



    list = list.prepend(3);





    // Show the final state of the list



    println!("linked list has length: {}", list.len());



    println!("{}", list.stringify());



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-11)
[`Box`](https://doc.rust-lang.org/rust-by-example/print.html#box-stack-and-heap) and [methods](https://doc.rust-lang.org/rust-by-example/print.html#associated-functions--methods)
