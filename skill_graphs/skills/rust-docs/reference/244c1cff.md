# [Returning from loops](https://doc.rust-lang.org/rust-by-example/print.html#returning-from-loops)
One of the uses of a `loop` is to retry an operation until it succeeds. If the operation returns a value though, you might need to pass it to the rest of the code: put it after the `break`, and it will be returned by the `loop` expression.
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














fn main() {



    let mut counter = 0;





    let result = loop {




        counter += 1;






        if counter == 10 {




            break counter * 2;




        }



    };





    assert_eq!(result, 20);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
