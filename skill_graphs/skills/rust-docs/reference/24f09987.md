# [Partial moves](https://doc.rust-lang.org/rust-by-example/print.html#partial-moves)
Within the [destructuring](https://doc.rust-lang.org/rust-by-example/print.html#destructuring) of a single variable, both `by-move` and `by-reference` pattern bindings can be used at the same time. Doing this will result in a _partial move_ of the variable, which means that parts of the variable will be moved while other parts stay. In such a case, the parent variable cannot be used afterwards as a whole, however the parts that are only referenced (and not moved) can still be used. Note that types that implement the [`Drop` trait](https://doc.rust-lang.org/rust-by-example/print.html#drop) cannot be partially moved from, because its `drop` method would use it afterwards as a whole.
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














fn main() {



    #[derive(Debug)]



    struct Person {




        name: String,




        age: Box<u8>,



    }





    // Error! cannot move out of a type which implements the `Drop` trait



    //impl Drop for Person {



    //    fn drop(&mut self) {



    //        println!("Dropping the person struct {:?}", self)



    //    }



    //}



    // TODO ^ Try uncommenting these lines





    let person = Person {




        name: String::from("Alice"),




        age: Box::new(20),



    };





    // `name` is moved out of person, but `age` is referenced



    let Person { name, ref age } = person;





    println!("The person's age is {}", age);





    println!("The person's name is {}", name);





    // Error! borrow of partially moved value: `person` partial move occurs



    //println!("The person struct is {:?}", person);





    // `person` cannot be used but `person.age` can be used as it is not moved



    println!("The person's age from person struct is {}", person.age);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

(In this example, we store the `age` variable on the heap to illustrate the partial move: deleting `ref` in the above code would give an error as the ownership of `person.age` would be moved to the variable `age`. If `Person.age` were stored on the stack, `ref` would not be required as the definition of `age` would copy the data from `person.age` without moving it.)
### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-49)
[destructuring](https://doc.rust-lang.org/rust-by-example/print.html#destructuring)
