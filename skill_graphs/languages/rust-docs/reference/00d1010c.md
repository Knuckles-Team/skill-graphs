# [`super` and `self`](https://doc.rust-lang.org/rust-by-example/print.html#super-and-self)
The `super` and `self` keywords can be used in the path to remove ambiguity when accessing items and to prevent unnecessary hardcoding of paths.
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














fn function() {



    println!("called `function()`");



}





mod cool {



    pub fn function() {




        println!("called `cool::function()`");



    }



}





mod my {



    fn function() {




        println!("called `my::function()`");



    }





    mod cool {




        pub fn function() {




            println!("called `my::cool::function()`");




        }



    }





    pub fn indirect_call() {




        // Let's access all the functions named `function` from this scope!




        print!("called `my::indirect_call()`, that\n> ");






        // The `self` keyword refers to the current module scope - in this case `my`.




        // Calling `self::function()` and calling `function()` directly both give




        // the same result, because they refer to the same function.




        self::function();




        function();






        // We can also use `self` to access another module inside `my`:




        self::cool::function();






        // The `super` keyword refers to the parent scope (outside the `my` module).




        super::function();






        // This will bind to the `cool::function` in the *crate* scope.




        // In this case the crate scope is the outermost scope.




        {




            use crate::cool::function as root_function;




            root_function();




        }



    }



}





fn main() {



    my::indirect_call();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
