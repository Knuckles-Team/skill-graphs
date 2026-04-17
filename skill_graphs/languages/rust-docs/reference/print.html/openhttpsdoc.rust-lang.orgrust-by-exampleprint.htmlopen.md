# [`open`](https://doc.rust-lang.org/rust-by-example/print.html#open)
The `open` function can be used to open a file in read-only mode.
A `File` owns a resource, the file descriptor and takes care of closing the file when it is `drop`ed.
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














use std::fs::File;




use std::io::prelude::*;




use std::path::Path;






fn main() {



    // Create a path to the desired file



    let path = Path::new("hello.txt");



    let display = path.display();





    // Open the path in read-only mode, returns `io::Result<File>`



    let mut file = match File::open(&path) {




        Err(why) => panic!("couldn't open {}: {}", display, why),




        Ok(file) => file,



    };





    // Read the file contents into a string, returns `io::Result<usize>`



    let mut s = String::new();



    match file.read_to_string(&mut s) {




        Err(why) => panic!("couldn't read {}: {}", display, why),




        Ok(_) => print!("{} contains:\n{}", display, s),



    }





    // `file` goes out of scope, and the "hello.txt" file gets closed



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```

Here’s the expected successful output:
```

__
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt contains:
Hello World!

```

(You are encouraged to test the previous example under different failure conditions: `hello.txt` doesn’t exist, or `hello.txt` is not readable, etc.)
