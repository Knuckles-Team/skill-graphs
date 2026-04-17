# [Structures](https://doc.rust-lang.org/rust-by-example/print.html#structures)
There are three types of structures (“structs”) that can be created using the `struct` keyword:
  * Tuple structs, which are, basically, named tuples.
  * The classic
  * Unit structs, which are field-less, are useful for generics.

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













// An attribute to hide warnings for unused code.


#![allow(dead_code)]





#[derive(Debug)]




struct Person {



    name: String,



    age: u8,



}




// A unit struct



struct Unit;





// A tuple struct



struct Pair(i32, f32);





// A struct with two fields



struct Point {



    x: f32,



    y: f32,



}




// Structs can be reused as fields of another struct



struct Rectangle {



    // A rectangle can be specified by where the top left and bottom right



    // corners are in space.



    top_left: Point,



    bottom_right: Point,



}





fn main() {



    // Create struct with field init shorthand



    let name = String::from("Peter");



    let age = 27;



    let peter = Person { name, age };





    // Print debug struct



    println!("{:?}", peter);





    // Instantiate a `Point`



    let point: Point = Point { x: 5.2, y: 0.4 };



    let another_point: Point = Point { x: 10.3, y: 0.2 };





    // Access the fields of the point



    println!("point coordinates: ({}, {})", point.x, point.y);





    // Make a new point by using struct update syntax to use the fields of our



    // other one



    let bottom_right = Point { x: 10.3, ..another_point };





    // `bottom_right.y` will be the same as `another_point.y` because we used that field



    // from `another_point`



    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);





    // Destructure the point using a `let` binding



    let Point { x: left_edge, y: top_edge } = point;





    let _rectangle = Rectangle {




        // struct instantiation is an expression too




        top_left: Point { x: left_edge, y: top_edge },




        bottom_right: bottom_right,



    };





    // Instantiate a unit struct



    let _unit = Unit;





    // Instantiate a tuple struct



    let pair = Pair(1, 0.1);





    // Access the fields of a tuple struct



    println!("pair contains {:?} and {:?}", pair.0, pair.1);





    // Destructure a tuple struct



    let Pair(integer, decimal) = pair;





    println!("pair contains {:?} and {:?}", integer, decimal);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [Activity](https://doc.rust-lang.org/rust-by-example/print.html#activity-5)
  1. Add a function `rect_area` which calculates the area of a `Rectangle` (try using nested destructuring).
  2. Add a function `square` which takes a `Point` and a `f32` as arguments, and returns a `Rectangle` with its top left corner on the point, and a width and height corresponding to the `f32`.


### [See also](https://doc.rust-lang.org/rust-by-example/print.html#see-also-7)
[`attributes`](https://doc.rust-lang.org/rust-by-example/print.html#attributes), [raw identifiers](https://doc.rust-lang.org/rust-by-example/print.html#raw-identifiers) and [destructuring](https://doc.rust-lang.org/rust-by-example/print.html#destructuring)
