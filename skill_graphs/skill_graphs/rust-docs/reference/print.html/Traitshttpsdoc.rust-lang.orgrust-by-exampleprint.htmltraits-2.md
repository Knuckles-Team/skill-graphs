# [Traits](https://doc.rust-lang.org/rust-by-example/print.html#traits-2)
A `trait` is a collection of methods defined for an unknown type: `Self`. They can access other methods declared in the same trait.
Traits can be implemented for any data type. In the example below, we define `Animal`, a group of methods. The `Animal` `trait` is then implemented for the `Sheep` data type, allowing the use of methods from `Animal` with a `Sheep`.
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














struct Sheep { naked: bool, name: &'static str }






trait Animal {



    // Associated function signature; `Self` refers to the implementer type.



    fn new(name: &'static str) -> Self;





    // Method signatures; these will return a string.



    fn name(&self) -> &'static str;



    fn noise(&self) -> &'static str;





    // Traits can provide default method definitions.



    fn talk(&self) {




        println!("{} says {}", self.name(), self.noise());



    }



}





impl Sheep {



    fn is_naked(&self) -> bool {




        self.naked


    }





    fn shear(&mut self) {




        if self.is_naked() {




            // Implementer methods can use the implementor's trait methods.




            println!("{} is already naked...", self.name());




        } else {




            println!("{} gets a haircut!", self.name);






            self.naked = true;




        }



    }



}




// Implement the `Animal` trait for `Sheep`.



impl Animal for Sheep {



    // `Self` is the implementer type: `Sheep`.



    fn new(name: &'static str) -> Sheep {




        Sheep { name: name, naked: false }



    }





    fn name(&self) -> &'static str {




        self.name


    }





    fn noise(&self) -> &'static str {




        if self.is_naked() {




            "baaaaah?"




        } else {




            "baaaaah!"




        }



    }





    // Default trait methods can be overridden.



    fn talk(&self) {




        // For example, we can add some quiet contemplation.




        println!("{} pauses briefly... {}", self.name, self.noise());



    }



}





fn main() {



    // Type annotation is necessary in this case.



    let mut dolly: Sheep = Animal::new("Dolly");



    // TODO ^ Try removing the type annotations.





    dolly.talk();



    dolly.shear();



    dolly.talk();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
