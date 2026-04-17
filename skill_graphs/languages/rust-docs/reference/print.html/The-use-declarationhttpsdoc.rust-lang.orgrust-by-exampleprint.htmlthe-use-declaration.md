# [The `use` declaration](https://doc.rust-lang.org/rust-by-example/print.html#the-use-declaration)
The `use` declaration can be used to bind a full path to a new name, for easier access. It is often used like this:
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














use crate::deeply::nested::{



    my_first_function,



    my_second_function,



    AndATraitType



};






fn main() {



    my_first_function();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

You can use the `as` keyword to bind imports to a different name:
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













// Bind the `deeply::nested::function` path to `other_function`.



use deeply::nested::function as other_function;






fn function() {



    println!("called `function()`");



}





mod deeply {



    pub mod nested {




        pub fn function() {




            println!("called `deeply::nested::function()`");




        }



    }



}





fn main() {



    // Easier access to `deeply::nested::function`



    other_function();





    println!("Entering block");



    {




        // This is equivalent to `use deeply::nested::function as function`.




        // This `function()` will shadow the outer one.




        use crate::deeply::nested::function;






        // `use` bindings have a local scope. In this case, the




        // shadowing of `function()` is only in this block.




        function();






        println!("Leaving block");



    }





    function();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
