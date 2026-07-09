# Get Account Information
GET`https://api.vercel.com/v1/installations/{integrationConfigurationId}/account`
Fetches the best account or user’s contact info
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/account
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/account', {






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

  "name": "Example Name",






3

  "url": "https://example.com",






4

  "contact": {






5

    "email": "user@example.com",






6

    "name": "Example Name"






7

  }






8

}




```
