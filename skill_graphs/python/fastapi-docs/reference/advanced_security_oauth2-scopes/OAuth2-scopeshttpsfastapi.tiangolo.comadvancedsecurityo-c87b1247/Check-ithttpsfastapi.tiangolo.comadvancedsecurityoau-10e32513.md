## Check it[¶](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#check-it)
If you open the API docs, you can authenticate and specify which scopes you want to authorize.
![](https://fastapi.tiangolo.com/img/tutorial/security/image11.png)
If you don't select any scope, you will be "authenticated", but when you try to access `/users/me/` or `/users/me/items/` you will get an error saying that you don't have enough permissions. You will still be able to access `/status/`.
And if you select the scope `me` but not the scope `items`, you will be able to access `/users/me/` but not `/users/me/items/`.
That's what would happen to a third party application that tried to access one of these _path operations_ with a token provided by a user, depending on how many permissions the user gave the application.
