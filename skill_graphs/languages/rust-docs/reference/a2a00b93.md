# [Child processes](https://doc.rust-lang.org/rust-by-example/print.html#child-processes)
The `process::Output` struct represents the output of a finished child process, and the `process::Command` struct is a process builder.
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














use std::process::Command;






fn main() {



    let output = Command::new("rustc")




        .arg("--version")




        .output().unwrap_or_else(|e| {




            panic!("failed to execute process: {}", e)



    });





    if output.status.success() {




        let s = String::from_utf8_lossy(&output.stdout);






        print!("rustc succeeded and stdout was:\n{}", s);



    } else {




        let s = String::from_utf8_lossy(&output.stderr);






        print!("rustc failed and stderr was:\n{}", s);



    }



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

(You are encouraged to try the previous example with an incorrect flag passed to `rustc`)
