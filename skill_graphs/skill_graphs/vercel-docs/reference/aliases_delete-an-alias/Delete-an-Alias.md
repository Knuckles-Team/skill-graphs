# Delete an Alias
DEL`https://api.vercel.com/v2/aliases/{aliasId}`
Delete an Alias with the specified ID.
TypeScriptNext.jscURL
https://api.vercel.com/v2/aliases/{aliasId}
```


1

const response = await fetch('https://api.vercel.com/v2/aliases/aliasId?teamId=string&slug=string', {






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

{






2

  "status": "SUCCESS"






3

}




```
