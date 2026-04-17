# [Freezing](https://doc.rust-lang.org/rust-by-example/print.html#freezing)
When data is bound by the same name immutably, it also _freezes_. _Frozen_ data can’t be modified until the immutable binding goes out of scope:
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














fn main() {



    let mut _mutable_integer = 7i32;





    {




        // Shadowing by immutable `_mutable_integer`




        let _mutable_integer = _mutable_integer;






        // Error! `_mutable_integer` is frozen in this scope




        _mutable_integer = 50;




        // FIXME ^ Comment out this line






        // `_mutable_integer` goes out of scope



    }





    // Ok! `_mutable_integer` is not frozen in this scope



    _mutable_integer = 3;



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
