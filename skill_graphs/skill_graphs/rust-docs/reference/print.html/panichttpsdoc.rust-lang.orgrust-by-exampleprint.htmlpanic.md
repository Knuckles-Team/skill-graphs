# [`panic`](https://doc.rust-lang.org/rust-by-example/print.html#panic)
The simplest error handling mechanism we will see is `panic`. It prints an error message, starts unwinding the stack, and usually exits the program. Here, we explicitly call `panic` on our error condition:
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














fn drink(beverage: &str) {



    // You shouldn't drink too many sugary beverages.



    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }





    println!("Some refreshing {} is all I need.", beverage);



}





fn main() {



    drink("water");



    drink("lemonade");



    drink("still water");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

The first call to `drink` works. The second panics and thus the third is never called.
