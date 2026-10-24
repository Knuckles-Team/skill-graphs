# Remove cert
DEL`https://api.vercel.com/v8/certs/{id}`
Remove cert
TypeScriptNext.jscURL
https://api.vercel.com/v8/certs/{id}
```


1

const response = await fetch('https://api.vercel.com/v8/certs/id?teamId=string&slug=string', {






2

  method: 'DELETE',






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
"value"



```
