# Gets project-level redirects.
GET`https://api.vercel.com/v1/bulk-redirects`
Get the version history for a project's bulk redirects
TypeScriptNext.jscURL
https://api.vercel.com/v1/bulk-redirects
```


1

const response = await fetch('https://api.vercel.com/v1/bulk-redirects?projectId=string&versionId=string&q=string&diff=value&page=123&per_page=123&sort_by=string&sort_order=string&teamId=string&slug=string', {






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
"value"



```
