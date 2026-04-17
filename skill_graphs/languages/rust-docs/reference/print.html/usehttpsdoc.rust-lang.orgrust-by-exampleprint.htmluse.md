# [use](https://doc.rust-lang.org/rust-by-example/print.html#use)
The `use` declaration can be used to avoid typing the full module path to access a name:
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













// An attribute to hide warnings for unused code.


#![allow(dead_code)]






enum Stage {



    Beginner,



    Advanced,



}





enum Role {



    Student,



    Teacher,



}





fn main() {



    // Explicitly `use` each name so they are available without



    // manual scoping.



    use Stage::{Beginner, Advanced};



    // Automatically `use` each name inside `Role`.



    use Role::*;





    // Equivalent to `Stage::Beginner`.



    let stage = Beginner;



    // Equivalent to `Role::Student`.



    let role = Student;





    match stage {




        // Note the lack of scoping because of the explicit `use` above.




        Beginner => println!("Beginners are starting their learning journey!"),




        Advanced => println!("Advanced learners are mastering their subjects..."),



    }





    match role {




        // Note again the lack of scoping.




        Student => println!("Students are acquiring knowledge!"),




        Teacher => println!("Teachers are spreading knowledge!"),



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-9)
[`match`](https://doc.rust-lang.org/rust-by-example/print.html#match) and [`use`](https://doc.rust-lang.org/rust-by-example/print.html#the-use-declaration)
