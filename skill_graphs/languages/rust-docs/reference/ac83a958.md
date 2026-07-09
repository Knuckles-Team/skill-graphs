# [Methods](https://doc.rust-lang.org/rust-by-example/print.html#methods)
Methods are annotated similarly to functions:
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














struct Owner(i32);






impl Owner {



    // Annotate lifetimes as in a standalone function.



    fn add_one<'a>(&'a mut self) { self.0 += 1; }



    fn print<'a>(&'a self) {




        println!("`print`: {}", self.0);



    }



}





fn main() {



    let mut owner = Owner(18);





    owner.add_one();



    owner.print();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-53)
[methods](https://doc.rust-lang.org/rust-by-example/print.html#associated-functions--methods)
