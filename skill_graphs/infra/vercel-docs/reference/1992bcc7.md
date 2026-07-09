# Create Event
POST`https://api.vercel.com/v1/installations/{integrationConfigurationId}/events`
Partner notifies Vercel of any changes made to an Installation or a Resource. Vercel is expected to use `list-resources` and other read APIs to get the new state.

`resource.updated` event should be dispatched when any state of a resource linked to Vercel is modified by the partner.
`installation.updated` event should be dispatched when an installation's billing plan is changed via the provider instead of Vercel.

Resource update use cases:

- The user renames a database in the partner’s application. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource in Vercel’s datastores.
- A resource has been suspended due to a lack of use. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource's status in Vercel's datastores.

TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/events
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/events', {






2

  method: 'POST',






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

    "event": {






9

      "type": "installation.updated",






10

      "billingPlanId": "example_id"






11

    }






12

  }),






13

});






14







15

const data = await response.json();






16

console.log(data);




```

Response
```


1

{}




```
