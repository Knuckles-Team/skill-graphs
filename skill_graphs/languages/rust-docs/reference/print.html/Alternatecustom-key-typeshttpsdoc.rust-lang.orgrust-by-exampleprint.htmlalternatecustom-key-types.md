# [Alternate/custom key types](https://doc.rust-lang.org/rust-by-example/print.html#alternatecustom-key-types)
Any type that implements the `Eq` and `Hash` traits can be a key in `HashMap`. This includes:
  * `bool` (though not very useful since there are only two possible keys)
  * `int`, `uint`, and all variations thereof
  * `String` and `&str` (protip: you can have a `HashMap` keyed by `String` and call `.get()` with an `&str`)


Note that `f32` and `f64` do _not_ implement `Hash`, likely because
All collection classes implement `Eq` and `Hash` if their contained type also respectively implements `Eq` and `Hash`. For example, `Vec<T>` will implement `Hash` if `T` implements `Hash`.
You can easily implement `Eq` and `Hash` for a custom type with just one line: `#[derive(PartialEq, Eq, Hash)]`
The compiler will do the rest. If you want more control over the details, you can implement `Eq` and/or `Hash` yourself. This guide will not cover the specifics of implementing `Hash`.
To play around with using a `struct` in `HashMap`, let’s try making a very simple user logon system:
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



48



49



50



51



52



53



54



55



56














use std::collections::HashMap;





// Eq requires that you derive PartialEq on the type.


#[derive(PartialEq, Eq, Hash)]




struct Account<'a>{



    username: &'a str,



    password: &'a str,



}





struct AccountInfo<'a>{



    name: &'a str,



    email: &'a str,



}





type Accounts<'a> = HashMap<Account<'a>, AccountInfo<'a>>;






fn try_logon<'a>(accounts: &Accounts<'a>,




        username: &'a str, password: &'a str){



    println!("Username: {}", username);



    println!("Password: {}", password);



    println!("Attempting logon...");





    let logon = Account {




        username,




        password,



    };





    match accounts.get(&logon) {




        Some(account_info) => {




            println!("Successful logon!");




            println!("Name: {}", account_info.name);




            println!("Email: {}", account_info.email);




        },




        _ => println!("Login failed!"),



    }



}





fn main(){



    let mut accounts: Accounts = HashMap::new();





    let account = Account {




        username: "j.everyman",




        password: "password123",



    };





    let account_info = AccountInfo {




        name: "John Everyman",




        email: "j.everyman@email.com",



    };





    accounts.insert(account, account_info);





    try_logon(&accounts, "j.everyman", "psasword123");





    try_logon(&accounts, "j.everyman", "password123");



}
















הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



```
