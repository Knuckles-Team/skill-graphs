# Update the protection bypass for a URL
PATCH`https://api.vercel.com/aliases/{id}/protection-bypass`
Update the protection bypass for the alias or deployment URL (used for user access & comment access for deployments). Used as shareable links and user scoped access for Vercel Authentication and also to allow external (logged in) people to comment on previews for Preview Comments (next-live-mode).
TypeScriptNext.jscURL
https://api.vercel.com/aliases/{id}/protection-bypass
```


1

const response = await fetch('https://api.vercel.com/aliases/id/protection-bypass?teamId=string&slug=string', {






2

  method: 'PATCH',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

  body: JSON.stringify({






8

    "ttl": "123",






9

    "revoke": {






10

      "secret": "string",






11

      "regenerate": "true"






12

    }






13

  }),






14

});






15







16

const data = await response.json();






17

console.log(data);




```

Response
```


1
"value"



```
