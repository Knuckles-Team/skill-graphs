# [Mutability](https://doc.rust-lang.org/rust-by-example/print.html#mutability-2)
Mutable data can be mutably borrowed using `&mut T`. This is called a _mutable reference_ and gives read/write access to the borrower. In contrast, `&T` borrows the data via an immutable reference, and the borrower can read the data but not modify it:
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













#[allow(dead_code)]



#[derive(Clone, Copy)]




struct Book {



    // `&'static str` is a reference to a string allocated in read only memory



    author: &'static str,



    title: &'static str,



    year: u32,



}




// This function takes a reference to a book



fn borrow_book(book: &Book) {



    println!("I immutably borrowed {} - {} edition", book.title, book.year);



}




// This function takes a reference to a mutable book and changes `year` to 2014



fn new_edition(book: &mut Book) {



    book.year = 2014;



    println!("I mutably borrowed {} - {} edition", book.title, book.year);



}





fn main() {



    // Create an immutable Book named `immutabook`



    let immutabook = Book {




        // string literals have type `&'static str`




        author: "Douglas Hofstadter",




        title: "Gödel, Escher, Bach",




        year: 1979,



    };





    // Create a mutable copy of `immutabook` and call it `mutabook`



    let mut mutabook = immutabook;





    // Immutably borrow an immutable object



    borrow_book(&immutabook);





    // Immutably borrow a mutable object



    borrow_book(&mutabook);





    // Borrow a mutable object as mutable



    new_edition(&mut mutabook);





    // Error! Cannot borrow an immutable object as mutable



    new_edition(&mut immutabook);



    // FIXME ^ Comment out this line



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

### [See also:](https://doc.rust-lang.org/rust-by-example/print.html#see-also-50)
[`static`](https://doc.rust-lang.org/rust-by-example/print.html#static)
