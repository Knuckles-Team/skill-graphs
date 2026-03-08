# Deletes an access group
DEL`https://api.vercel.com/v1/access-groups/{idOrName}`
Allows to delete an access group
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups/{idOrName}
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups/idOrName?teamId=string&slug=string', {






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

{}




```
