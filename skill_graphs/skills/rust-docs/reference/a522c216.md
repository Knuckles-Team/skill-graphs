# [Channels](https://doc.rust-lang.org/rust-by-example/print.html#channels)
Rust provides asynchronous `channels` for communication between threads. Channels allow a unidirectional flow of information between two end-points: the `Sender` and the `Receiver`.
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














use std::sync::mpsc::{Sender, Receiver};




use std::sync::mpsc;




use std::thread;






static NTHREADS: i32 = 3;






fn main() {



    // Channels have two endpoints: the `Sender<T>` and the `Receiver<T>`,



    // where `T` is the type of the message to be transferred



    // (type annotation is superfluous)



    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();



    let mut children = Vec::new();





    for id in 0..NTHREADS {




        // The sender endpoint can be copied




        let thread_tx = tx.clone();






        // Each thread will send its id via the channel




        let child = thread::spawn(move || {




            // The thread takes ownership over `thread_tx`




            // Each thread queues a message in the channel




            thread_tx.send(id).unwrap();






            // Sending is a non-blocking operation, the thread will continue




            // immediately after sending its message




            println!("thread {} finished", id);




        });






        children.push(child);



    }





    // Here, all the messages are collected



    let mut ids = Vec::with_capacity(NTHREADS as usize);



    for _ in 0..NTHREADS {




        // The `recv` method picks a message from the channel




        // `recv` will block the current thread if there are no messages available




        ids.push(rx.recv());



    }





    // Wait for the threads to complete any remaining work



    for child in children {




        child.join().expect("oops! the child thread panicked");



    }





    // Show the order in which the messages were sent



    println!("{:?}", ids);



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
