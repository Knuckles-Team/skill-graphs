# List access groups for a team, project or member
GET`https://api.vercel.com/v1/access-groups`
List access groups
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups?projectId=string&search=string&membersLimit=123&projectsLimit=123&limit=123&next=string&teamId=string&slug=string', {






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
