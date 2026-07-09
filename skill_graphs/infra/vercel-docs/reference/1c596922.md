# Get cert by id
GET`https://api.vercel.com/v8/certs/{id}`
Get cert by id
TypeScriptNext.jscURL
https://api.vercel.com/v8/certs/{id}
```


1

const response = await fetch('https://api.vercel.com/v8/certs/id?teamId=string&slug=string', {






2

  method: 'GET',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "createdAt": "123",






4

  "expiresAt": "123",






5

  "autoRenew": "false",






6

  "cns": []






7

}




```
