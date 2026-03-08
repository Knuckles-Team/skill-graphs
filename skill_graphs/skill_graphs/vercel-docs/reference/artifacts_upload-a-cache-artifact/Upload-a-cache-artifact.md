# Upload a cache artifact
PUT`https://api.vercel.com/v8/artifacts/{hash}`
Uploads a cache artifact identified by the `hash` specified on the path. The cache artifact can then be downloaded with the provided `hash`.
TypeScriptNext.jscURL
https://api.vercel.com/v8/artifacts/{hash}
```


1

const response = await fetch('https://api.vercel.com/v8/artifacts/hash?teamId=string&slug=string', {






2

  method: 'PUT',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

    'Content-Length': '123',






7

  },






8

});






9







10

const data = await response.json();






11

console.log(data);




```

Response
```


1

{






2

  "urls": []






3

}




```
