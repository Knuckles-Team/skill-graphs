# [`dead_code`](https://doc.rust-lang.org/rust-by-example/print.html#dead_code)
The compiler provides a `dead_code` _attribute_ can be used to disable the lint.
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














fn used_function() {}





// `#[allow(dead_code)]` is an attribute that disables the `dead_code` lint


#[allow(dead_code)]




fn unused_function() {}






fn noisy_unused_function() {}



// FIXME ^ Add an attribute to suppress the warning





fn main() {



    used_function();



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Note that in real programs, you should eliminate dead code. In these examples we’ll allow dead code in some places because of the interactive nature of the examples.
