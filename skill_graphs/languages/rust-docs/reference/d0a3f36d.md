# [Associated functions & Methods](https://doc.rust-lang.org/rust-by-example/print.html#associated-functions--methods)
Some functions are connected to a particular type. These come in two forms: associated functions, and methods. Associated functions are functions that are defined on a type generally, while methods are associated functions that are called on a particular instance of a type.
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



71



72



73



74



75



76



77



78



79



80



81



82



83



84



85



86



87



88



89



90



91



92



93



94



95



96



97



98



99



100



101



102



103



104



105



106



107



108



109














struct Point {



    x: f64,



    y: f64,



}




// Implementation block, all `Point` associated functions & methods go in here



impl Point {



    // This is an "associated function" because this function is associated with



    // a particular type, that is, Point.



    //



    // Associated functions don't need to be called with an instance.



    // These functions are generally used like constructors.



    fn origin() -> Point {




        Point { x: 0.0, y: 0.0 }



    }





    // Another associated function, taking two arguments:



    fn new(x: f64, y: f64) -> Point {




        Point { x: x, y: y }



    }



}





struct Rectangle {



    p1: Point,



    p2: Point,



}





impl Rectangle {



    // This is a method



    // `&self` is sugar for `self: &Self`, where `Self` is the type of the



    // caller object. In this case `Self` = `Rectangle`



    fn area(&self) -> f64 {




        // `self` gives access to the struct fields via the dot operator




        let Point { x: x1, y: y1 } = self.p1;




        let Point { x: x2, y: y2 } = self.p2;






        // `abs` is a `f64` method that returns the absolute value of the




        // caller




        ((x1 - x2) * (y1 - y2)).abs()



    }





    fn perimeter(&self) -> f64 {




        let Point { x: x1, y: y1 } = self.p1;




        let Point { x: x2, y: y2 } = self.p2;






        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())



    }





    // This method requires the caller object to be mutable



    // `&mut self` desugars to `self: &mut Self`



    fn translate(&mut self, x: f64, y: f64) {




        self.p1.x += x;




        self.p2.x += x;






        self.p1.y += y;




        self.p2.y += y;



    }



}




// `Pair` owns resources: two heap allocated integers



struct Pair(Box<i32>, Box<i32>);






impl Pair {



    // This method "consumes" the resources of the caller object



    // `self` desugars to `self: Self`



    fn destroy(self) {




        // Destructure `self`




        let Pair(first, second) = self;






        println!("Destroying Pair({}, {})", first, second);






        // `first` and `second` go out of scope and get freed



    }



}





fn main() {



    let rectangle = Rectangle {




        // Associated functions are called using double colons




        p1: Point::origin(),




        p2: Point::new(3.0, 4.0),



    };





    // Methods are called using the dot operator



    // Note that the first argument `&self` is implicitly passed, i.e.



    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`



    println!("Rectangle perimeter: {}", rectangle.perimeter());



    println!("Rectangle area: {}", rectangle.area());





    let mut square = Rectangle {




        p1: Point::origin(),




        p2: Point::new(1.0, 1.0),



    };





    // Error! `rectangle` is immutable, but this method requires a mutable



    // object



    //rectangle.translate(1.0, 0.0);



    // TODO ^ Try uncommenting this line





    // Okay! Mutable objects can call mutable methods



    square.translate(1.0, 1.0);





    let pair = Pair(Box::new(1), Box::new(2));





    pair.destroy();





    // Error! Previous `destroy` call "consumed" `pair`



    //pair.destroy();



    // TODO ^ Try uncommenting this line



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
