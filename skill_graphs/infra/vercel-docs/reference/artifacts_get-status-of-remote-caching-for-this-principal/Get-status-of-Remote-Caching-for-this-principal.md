# Get status of Remote Caching for this principal
GET`https://api.vercel.com/v8/artifacts/status`
Check the status of Remote Caching for this principal. Returns a JSON-encoded status indicating if Remote Caching is enabled, disabled, or disabled due to usage limits.
TypeScriptNext.jscURL
https://api.vercel.com/v8/artifacts/status
```


1

const response = await fetch('https://api.vercel.com/v8/artifacts/status?teamId=string&slug=string', {






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

  "status": "disabled"






3

}




```
