# [Unpacking options with `?`](https://doc.rust-lang.org/rust-by-example/print.html#unpacking-options-with-)
You can unpack `Option`s by using `match` statements, but it’s often easier to use the `?` operator. If `x` is an `Option`, then evaluating `x?` will return the underlying value if `x` is `Some`, otherwise it will terminate whatever function is being executed and return `None`.
```

__
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // If `current_age` is `None`, this returns `None`.
    // If `current_age` is `Some`, the inner `u8` value + 1
    // gets assigned to `next_age`
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

You can chain many `?`s together to make your code much more readable.
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














struct Person {



    job: Option<Job>,



}




#[derive(Clone, Copy)]




struct Job {



    phone_number: Option<PhoneNumber>,



}




#[derive(Clone, Copy)]




struct PhoneNumber {



    area_code: Option<u8>,



    number: u32,



}





impl Person {





    // Gets the area code of the phone number of the person's job, if it exists.



    fn work_phone_area_code(&self) -> Option<u8> {




        // This would need many nested `match` statements without the `?` operator.




        // It would take a lot more code - try writing it yourself and see which




        // is easier.




        self.job?.phone_number?.area_code


    }



}





fn main() {



    let p = Person {




        job: Some(Job {




            phone_number: Some(PhoneNumber {




                area_code: Some(61),




                number: 439222222,




            }),




        }),



    };





    assert_eq!(p.work_phone_area_code(), Some(61));



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
