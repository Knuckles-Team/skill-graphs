# [Iterator::any](https://doc.rust-lang.org/rust-by-example/print.html#iteratorany)
`Iterator::any` is a function which when passed an iterator, will return `true` if any element satisfies the predicate. Otherwise `false`. Its signature:
```

__
pub trait Iterator {
    // The type being iterated over.
    type Item;

    // `any` takes `&mut self` meaning the caller may be borrowed
    // and modified, but not consumed.
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` meaning any captured variable may at most be
        // modified, not consumed. `Self::Item` is the closure parameter type,
        // which is determined by the iterator (e.g., `&T` for `.iter()`,
        // `T` for `.into_iter()`).
        F: FnMut(Self::Item) -> bool;
}
```
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














fn main() {



    let vec1 = vec![1, 2, 3];



    let vec2 = vec![4, 5, 6];





    // `iter()` for vecs yields `&i32`. Destructure to `i32`.



    println!("2 in vec1: {}", vec1.iter()     .any(|&x| x == 2));



    // `into_iter()` for vecs yields `i32`. No destructuring required.



    println!("2 in vec2: {}", vec2.into_iter().any(|x| x == 2));





    // `iter()` only borrows `vec1` and its elements, so they can be used again



    println!("vec1 len: {}", vec1.len());



    println!("First element of vec1 is: {}", vec1[0]);



    // `into_iter()` does move `vec2` and its elements, so they cannot be used again



    // println!("First element of vec2 is: {}", vec2[0]);



    // println!("vec2 len: {}", vec2.len());



    // TODO: uncomment two lines above and see compiler errors.





    let array1 = [1, 2, 3];



    let array2 = [4, 5, 6];





    // `iter()` for arrays yields `&i32`.



    println!("2 in array1: {}", array1.iter()     .any(|&x| x == 2));



    // `into_iter()` for arrays yields `i32`.



    println!("2 in array2: {}", array2.into_iter().any(|x| x == 2));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-31)
[`std::iter::Iterator::any`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.any)
