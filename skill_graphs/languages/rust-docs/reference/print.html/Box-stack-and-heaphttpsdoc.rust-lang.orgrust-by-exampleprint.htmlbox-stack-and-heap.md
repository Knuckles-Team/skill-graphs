# [Box, stack and heap](https://doc.rust-lang.org/rust-by-example/print.html#box-stack-and-heap)
All values in Rust are stack allocated by default. Values can be _boxed_ (allocated on the heap) by creating a `Box<T>`. A box is a smart pointer to a heap allocated value of type `T`. When a box goes out of scope, its destructor is called, the inner object is destroyed, and the memory on the heap is freed.
Boxed values can be dereferenced using the `*` operator; this removes one layer of indirection.
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














use std::mem;





#[allow(dead_code)]



#[derive(Debug, Clone, Copy)]




struct Point {



    x: f64,



    y: f64,



}




// A Rectangle can be specified by where its top left and bottom right


// corners are in space


#[allow(dead_code)]




struct Rectangle {



    top_left: Point,



    bottom_right: Point,



}





fn origin() -> Point {



    Point { x: 0.0, y: 0.0 }



}





fn boxed_origin() -> Box<Point> {



    // Allocate this point on the heap, and return a pointer to it



    Box::new(Point { x: 0.0, y: 0.0 })



}





fn main() {



    // (all the type annotations are superfluous)



    // Stack allocated variables



    let point: Point = origin();



    let rectangle: Rectangle = Rectangle {




        top_left: origin(),




        bottom_right: Point { x: 3.0, y: -4.0 }



    };





    // Heap allocated rectangle



    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {




        top_left: origin(),




        bottom_right: Point { x: 3.0, y: -4.0 },



    });





    // The output of functions can be boxed



    let boxed_point: Box<Point> = Box::new(origin());





    // Double indirection



    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());





    println!("Point occupies {} bytes on the stack",




             mem::size_of_val(&point));



    println!("Rectangle occupies {} bytes on the stack",




             mem::size_of_val(&rectangle));





    // box size == pointer size



    println!("Boxed point occupies {} bytes on the stack",




             mem::size_of_val(&boxed_point));



    println!("Boxed rectangle occupies {} bytes on the stack",




             mem::size_of_val(&boxed_rectangle));



    println!("Boxed box occupies {} bytes on the stack",




             mem::size_of_val(&box_in_a_box));





    // Copy the data contained in `boxed_point` into `unboxed_point`



    let unboxed_point: Point = *boxed_point;



    println!("Unboxed point occupies {} bytes on the stack",




             mem::size_of_val(&unboxed_point));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
