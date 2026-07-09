# Get Member Information
GET`https://api.vercel.com/v1/installations/{integrationConfigurationId}/member/{memberId}`
Returns the member role and other information for a given member ID ("user_id" claim in the SSO OIDC token).
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/member/{memberId}
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/member/memberId', {






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

  "role": "ADMIN",






4

  "globalUserId": "example_id",






5

  "userEmail": "user@example.com"






6

}




```
