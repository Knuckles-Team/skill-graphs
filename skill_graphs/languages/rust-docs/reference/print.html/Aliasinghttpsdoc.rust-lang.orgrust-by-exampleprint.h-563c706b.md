# [Aliasing](https://doc.rust-lang.org/rust-by-example/print.html#aliasing-1)
Data can be immutably borrowed any number of times, but while immutably borrowed, the original data can’t be mutably borrowed. On the other hand, only _one_ mutable borrow is allowed at a time. The original data can be borrowed again only _after_ the mutable reference has been used for the last time.
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














struct Point { x: i32, y: i32, z: i32 }






fn main() {



    let mut point = Point { x: 0, y: 0, z: 0 };





    let borrowed_point = &point;



    let another_borrow = &point;





    // Data can be accessed via the references and the original owner



    println!("Point has coordinates: ({}, {}, {})",




                borrowed_point.x, another_borrow.y, point.z);





    // Error! Can't borrow `point` as mutable because it's currently



    // borrowed as immutable.



    // let mutable_borrow = &mut point;



    // TODO ^ Try uncommenting this line





    // The borrowed values are used again here



    println!("Point has coordinates: ({}, {}, {})",




                borrowed_point.x, another_borrow.y, point.z);





    // The immutable references are no longer used for the rest of the code so



    // it is possible to reborrow with a mutable reference.



    let mutable_borrow = &mut point;





    // Change data via mutable reference



    mutable_borrow.x = 5;



    mutable_borrow.y = 2;



    mutable_borrow.z = 1;





    // Error! Can't borrow `point` as immutable because it's currently



    // borrowed as mutable.



    // let y = &point.y;



    // TODO ^ Try uncommenting this line





    // Error! Can't print because `println!` takes an immutable reference.



    // println!("Point Z coordinate is {}", point.z);



    // TODO ^ Try uncommenting this line





    // Ok! Mutable references can be passed as immutable to `println!`



    println!("Point has coordinates: ({}, {}, {})",




                mutable_borrow.x, mutable_borrow.y, mutable_borrow.z);





    // The mutable reference is no longer used for the rest of the code so it



    // is possible to reborrow



    let new_borrowed_point = &point;



    println!("Point now has coordinates: ({}, {}, {})",




             new_borrowed_point.x, new_borrowed_point.y, new_borrowed_point.z);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
