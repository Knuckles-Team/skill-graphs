# [Wait](https://doc.rust-lang.org/rust-by-example/print.html#wait)
If you’d like to wait for a `process::Child` to finish, you must call `Child::wait`, which will return a `process::ExitStatus`.
```

__
use std::process::Command;

fn main() {
    let mut child = Command::new("sleep").arg("5").spawn().unwrap();
    let _result = child.wait().unwrap();

    println!("reached end of main");
}
```
```

__
$ rustc wait.rs && ./wait
# `wait` keeps running for 5 seconds until the `sleep 5` command finishes
reached end of main

```
