# [Supertraits](https://doc.rust-lang.org/rust-by-example/print.html#supertraits)
Rust doesn’t have “inheritance”, but you can define a trait as being a superset of another trait. For example:
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














trait Person {



    fn name(&self) -> String;



}




// Person is a supertrait of Student.


// Implementing Student requires you to also impl Person.



trait Student: Person {



    fn university(&self) -> String;



}





trait Programmer {



    fn fav_language(&self) -> String;



}




// CompSciStudent (computer science student) is a subtrait of both Programmer


// and Student. Implementing CompSciStudent requires you to impl both supertraits.



trait CompSciStudent: Programmer + Student {



    fn git_username(&self) -> String;



}





fn comp_sci_student_greeting(student: &dyn CompSciStudent) -> String {



    format!(




        "My name is {} and I attend {}. My favorite language is {}. My Git username is {}",




        student.name(),




        student.university(),




        student.fav_language(),




        student.git_username()



    )



}





fn main() {}

















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-61)
[The Rust Programming Language chapter on supertraits](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#using-supertraits-to-require-one-traits-functionality-within-another-trait)
