# [Arrays and Slices](https://doc.rust-lang.org/rust-by-example/print.html#arrays-and-slices)
An array is a collection of objects of the same type `T`, stored in contiguous memory. Arrays are created using brackets `[]`, and their length, which is known at compile time, is part of their type signature `[T; length]`.
Slices are similar to arrays, but their length is not known at compile time. Instead, a slice is a two-word object; the first word is a pointer to the data, the second word is the length of the slice. The word size is the same as usize, determined by the processor architecture, e.g. 64 bits on an x86-64. Slices can be used to borrow a section of an array and have the type signature `&[T]`.
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














use std::mem;





// This function borrows a slice.



fn analyze_slice(slice: &[i32]) {



    println!("First element of the slice: {}", slice[0]);



    println!("The slice has {} elements", slice.len());



}





fn main() {



    // Fixed-size array (type signature is superfluous).



    let xs: [i32; 5] = [1, 2, 3, 4, 5];





    // All elements can be initialized to the same value.



    let ys: [i32; 500] = [0; 500];





    // Indexing starts at 0.



    println!("First element of the array: {}", xs[0]);



    println!("Second element of the array: {}", xs[1]);





    // `len` returns the count of elements in the array.



    println!("Number of elements in array: {}", xs.len());





    // Arrays are stack allocated.



    println!("Array occupies {} bytes", mem::size_of_val(&xs));





    // Arrays can be automatically borrowed as slices.



    println!("Borrow the whole array as a slice.");



    analyze_slice(&xs);





    // Slices can point to a section of an array.



    // They are of the form [starting_index..ending_index].



    // `starting_index` is the first position in the slice.



    // `ending_index` is one more than the last position in the slice.



    println!("Borrow a section of the array as a slice.");



    analyze_slice(&ys[1 .. 4]);





    // Example of empty slice `&[]`:



    let empty_array: [u32; 0] = [];



    assert_eq!(&empty_array, &[]);



    assert_eq!(&empty_array, &[][..]); // Same but more verbose





    // Arrays can be safely accessed using `.get`, which returns an



    // `Option`. This can be matched as shown below, or used with



    // `.expect()` if you would like the program to exit with a nice



    // message instead of happily continue.



    for i in 0..xs.len() + 1 { // Oops, one element too far!




        match xs.get(i) {




            Some(xval) => println!("{}: {}", i, xval),




            None => println!("Slow down! {} is too far!", i),




        }



    }





    // Out of bound indexing on array with constant value causes compile time error.



    //println!("{}", xs[5]);



    // Out of bound indexing on slice causes runtime error.



    //println!("{}", xs[..][5]);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
