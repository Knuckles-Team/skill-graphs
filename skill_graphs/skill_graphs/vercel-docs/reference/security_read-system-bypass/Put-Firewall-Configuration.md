# Put Firewall Configuration
PUT`https://api.vercel.com/v1/security/firewall/config`
Set the firewall configuration to provided rules and settings. Creates or overwrite the existing firewall configuration.
TypeScriptNext.jscURL
https://api.vercel.com/v1/security/firewall/config
```


1

const response = await fetch('https://api.vercel.com/v1/security/firewall/config?projectId=string&teamId=string&slug=string', {






2

  method: 'PUT',






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

    "firewallEnabled": "true",






9

    "managedRules": "value",






10

    "crs": {






11

      "sd": {






12

        "active": "true",






13

        "action": "deny"






14

      },






15

      "ma": {






16

        "active": "true",






17

        "action": "deny"






18

      },






19

      "lfi": {






20

        "active": "true",






21

        "action": "deny"






22

      },






23

      "rfi": {






24

        "active": "true",






25

        "action": "deny"






26

      },






27

      "rce": {






28

        "active": "true",






29

        "action": "deny"






30

      },






31

      "php": {






32

        "active": "true",






33

        "action": "deny"






34

      },






35

      "gen": {






36

        "active": "true",






37

        "action": "deny"






38

      },






39

      "xss": {






40

        "active": "true",






41

        "action": "deny"






42

      },






43

      "sqli": {






44

        "active": "true",






45

        "action": "deny"






46

      },






47

      "sf": {






48

        "active": "true",






49

        "action": "deny"






50

      },






51

      "java": {






52

        "active": "true",






53

        "action": "deny"






54

      }






55

    },






56

    "rules": [






57

      {






58

        "id": "icfg_1234567890",






59

        "name": "Example Name",






60

        "description": "string",






61

        "active": "true",






62

        "conditionGroup": [






63

          {






64

            "conditions": [






65

              {






66

                "type": "host",






67

                "op": "re",






68

                "neg": "true",






69

                "key": "string",






70

                "value": "string"






71

              }






72

            ]






73

          }






74

        ],






75

        "action": {






76

          "mitigate": {






77

            "action": "log",






78

            "rateLimit": {






79

              "algo": "fixed_window",






80

              "window": "123",






81

              "limit": "123",






82

              "keys": [],






83

              "action": "log"






84

            },






85

            "redirect": {






86

              "location": "string",






87

              "permanent": "true"






88

            },






89

            "actionDuration": "string",






90

            "bypassSystem": "true"






91

          }






92

        },






93

        "valid": "true",






94

        "validationErrors": []






95

      }






96

    ],






97

    "ips": [






98

      {






99

        "id": "icfg_1234567890",






100

        "hostname": "Example Name",






101

        "ip": "string",






102

        "notes": "string",






103

        "action": "deny"






104

      }






105

    ],






106

    "botIdEnabled": "true"






107

  }),






108

});






109







110

const data = await response.json();






111

console.log(data);




```

Response
```


1

{






2

  "active": {






3

    "ownerId": "example_id",






4

    "projectKey": "string",






5

    "id": "icfg_1234567890",






6

    "version": "123",






7

    "updatedAt": "string",






8

    "firewallEnabled": "false",






9

    "crs": {






10

      "sd": {






11

        "active": "false",






12

        "action": "deny"






13

      },






14

      "ma": {






15

        "active": "false",






16

        "action": "deny"






17

      },






18

      "lfi": {






19

        "active": "false",






20

        "action": "deny"






21

      },






22

      "rfi": {






23

        "active": "false",






24

        "action": "deny"






25

      },






26

      "rce": {






27

        "active": "false",






28

        "action": "deny"






29

      },






30

      "php": {






31

        "active": "false",






32

        "action": "deny"






33

      },






34

      "gen": {






35

        "active": "false",






36

        "action": "deny"






37

      },






38

      "xss": {






39

        "active": "false",






40

        "action": "deny"






41

      },






42

      "sqli": {






43

        "active": "false",






44

        "action": "deny"






45

      },






46

      "sf": {






47

        "active": "false",






48

        "action": "deny"






49

      },






50

      "java": {






51

        "active": "false",






52

        "action": "deny"






53

      }






54

    },






55

    "rules": [






56

      {






57

        "id": "icfg_1234567890",






58

        "name": "Example Name",






59

        "description": "string",






60

        "active": "false",






61

        "conditionGroup": [






62

          {






63

            "conditions": [






64

              {






65

                "type": "host",






66

                "op": "sub",






67

                "neg": "false",






68

                "key": "string",






69

                "value": "string"






70

              }






71

            ]






72

          }






73

        ],






74

        "action": {






75

          "mitigate": {






76

            "action": "deny",






77

            "rateLimit": {






78

              "algo": "fixed_window",






79

              "window": "123",






80

              "limit": "123",






81

              "keys": [],






82

              "action": "deny"






83

            },






84

            "redirect": {






85

              "location": "string",






86

              "permanent": "false"






87

            },






88

            "actionDuration": "string",






89

            "bypassSystem": "false",






90

            "logHeaders": []






91

          }






92

        },






93

        "valid": "true",






94

        "validationErrors": "value"






95

      }






96

    ],






97

    "ips": [






98

      {






99

        "id": "icfg_1234567890",






100

        "hostname": "Example Name",






101

        "ip": "string",






102

        "notes": "string",






103

        "action": "deny"






104

      }






105

    ],






106

    "changes": [






107

      "value"






108

    ],






109

    "managedRules": {






110

      "bot_protection": {






111

        "active": "false",






112

        "action": "deny",






113

        "updatedAt": "string",






114

        "userId": "example_id",






115

        "username": "string"






116

      },






117

      "ai_bots": {






118

        "active": "false",






119

        "action": "deny",






120

        "updatedAt": "string",






121

        "userId": "example_id",






122

        "username": "string"






123

      },






124

      "owasp": {






125

        "active": "false",






126

        "action": "deny",






127

        "updatedAt": "string",






128

        "userId": "example_id",






129

        "username": "string"






130

      },






131

      "vercel_ruleset": {






132

        "active": "false",






133

        "action": "deny",






134

        "updatedAt": "string",






135

        "userId": "example_id",






136

        "username": "string"






137

      }






138

    },






139

    "botIdEnabled": "false"






140

  }






141

}




```

##  [Authentication](https://vercel.com/docs/rest-api/security/put-firewall-configuration#authentication)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/security/put-firewall-configuration#query-parameters)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#query-parameters)
projectIdstringRequired
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/security/put-firewall-configuration#body)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#body)
application/json
firewallEnabledbooleanRequired
managedRulesobjectOptional
crsobjectOptional
Custom Ruleset
+Show 11 properties
rulesarrayOptional
+Show 8 properties
ipsarrayOptional
+Show 5 properties
botIdEnabledbooleanOptional
##  [Response](https://vercel.com/docs/rest-api/security/put-firewall-configuration#response)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#response)
200Success
activeobjectRequired
+Show 12 properties
##  [Errors](https://vercel.com/docs/rest-api/security/put-firewall-configuration#errors)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402Error
403You do not have permission to access this resource.
404Error
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/security/firewall/config
```


1

const response = await fetch('https://api.vercel.com/v1/security/firewall/config?projectId=string&teamId=string&slug=string', {






2

  method: 'PUT',






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

    "firewallEnabled": "true",






9

    "managedRules": "value",






10

    "crs": {






11

      "sd": {






12

        "active": "true",






13

        "action": "deny"






14

      },






15

      "ma": {






16

        "active": "true",






17

        "action": "deny"






18

      },






19

      "lfi": {






20

        "active": "true",






21

        "action": "deny"






22

      },






23

      "rfi": {






24

        "active": "true",






25

        "action": "deny"






26

      },






27

      "rce": {






28

        "active": "true",






29

        "action": "deny"






30

      },






31

      "php": {






32

        "active": "true",






33

        "action": "deny"






34

      },






35

      "gen": {






36

        "active": "true",






37

        "action": "deny"






38

      },






39

      "xss": {






40

        "active": "true",






41

        "action": "deny"






42

      },






43

      "sqli": {






44

        "active": "true",






45

        "action": "deny"






46

      },






47

      "sf": {






48

        "active": "true",






49

        "action": "deny"






50

      },






51

      "java": {






52

        "active": "true",






53

        "action": "deny"






54

      }






55

    },






56

    "rules": [






57

      {






58

        "id": "icfg_1234567890",






59

        "name": "Example Name",






60

        "description": "string",






61

        "active": "true",






62

        "conditionGroup": [






63

          {






64

            "conditions": [






65

              {






66

                "type": "host",






67

                "op": "re",






68

                "neg": "true",






69

                "key": "string",






70

                "value": "string"






71

              }






72

            ]






73

          }






74

        ],






75

        "action": {






76

          "mitigate": {






77

            "action": "log",






78

            "rateLimit": {






79

              "algo": "fixed_window",






80

              "window": "123",






81

              "limit": "123",






82

              "keys": [],






83

              "action": "log"






84

            },






85

            "redirect": {






86

              "location": "string",






87

              "permanent": "true"






88

            },






89

            "actionDuration": "string",






90

            "bypassSystem": "true"






91

          }






92

        },






93

        "valid": "true",






94

        "validationErrors": []






95

      }






96

    ],






97

    "ips": [






98

      {






99

        "id": "icfg_1234567890",






100

        "hostname": "Example Name",






101

        "ip": "string",






102

        "notes": "string",






103

        "action": "deny"






104

      }






105

    ],






106

    "botIdEnabled": "true"






107

  }),






108

});






109







110

const data = await response.json();






111

console.log(data);




```

Response
```


1

{






2

  "active": {






3

    "ownerId": "example_id",






4

    "projectKey": "string",






5

    "id": "icfg_1234567890",






6

    "version": "123",






7

    "updatedAt": "string",






8

    "firewallEnabled": "false",






9

    "crs": {






10

      "sd": {






11

        "active": "false",






12

        "action": "deny"






13

      },






14

      "ma": {






15

        "active": "false",






16

        "action": "deny"






17

      },






18

      "lfi": {






19

        "active": "false",






20

        "action": "deny"






21

      },






22

      "rfi": {






23

        "active": "false",






24

        "action": "deny"






25

      },






26

      "rce": {






27

        "active": "false",






28

        "action": "deny"






29

      },






30

      "php": {






31

        "active": "false",






32

        "action": "deny"






33

      },






34

      "gen": {






35

        "active": "false",






36

        "action": "deny"






37

      },






38

      "xss": {






39

        "active": "false",






40

        "action": "deny"






41

      },






42

      "sqli": {






43

        "active": "false",






44

        "action": "deny"






45

      },






46

      "sf": {






47

        "active": "false",






48

        "action": "deny"






49

      },






50

      "java": {






51

        "active": "false",






52

        "action": "deny"






53

      }






54

    },






55

    "rules": [






56

      {






57

        "id": "icfg_1234567890",






58

        "name": "Example Name",






59

        "description": "string",






60

        "active": "false",






61

        "conditionGroup": [






62

          {






63

            "conditions": [






64

              {






65

                "type": "host",






66

                "op": "sub",






67

                "neg": "false",






68

                "key": "string",






69

                "value": "string"






70

              }






71

            ]






72

          }






73

        ],






74

        "action": {






75

          "mitigate": {






76

            "action": "deny",






77

            "rateLimit": {






78

              "algo": "fixed_window",






79

              "window": "123",






80

              "limit": "123",






81

              "keys": [],






82

              "action": "deny"






83

            },






84

            "redirect": {






85

              "location": "string",






86

              "permanent": "false"






87

            },






88

            "actionDuration": "string",






89

            "bypassSystem": "false",






90

            "logHeaders": []






91

          }






92

        },






93

        "valid": "true",






94

        "validationErrors": "value"






95

      }






96

    ],






97

    "ips": [






98

      {






99

        "id": "icfg_1234567890",






100

        "hostname": "Example Name",






101

        "ip": "string",






102

        "notes": "string",






103

        "action": "deny"






104

      }






105

    ],






106

    "changes": [






107

      "value"






108

    ],






109

    "managedRules": {






110

      "bot_protection": {






111

        "active": "false",






112

        "action": "deny",






113

        "updatedAt": "string",






114

        "userId": "example_id",






115

        "username": "string"






116

      },






117

      "ai_bots": {






118

        "active": "false",






119

        "action": "deny",






120

        "updatedAt": "string",






121

        "userId": "example_id",






122

        "username": "string"






123

      },






124

      "owasp": {






125

        "active": "false",






126

        "action": "deny",






127

        "updatedAt": "string",






128

        "userId": "example_id",






129

        "username": "string"






130

      },






131

      "vercel_ruleset": {






132

        "active": "false",






133

        "action": "deny",






134

        "updatedAt": "string",






135

        "userId": "example_id",






136

        "username": "string"






137

      }






138

    },






139

    "botIdEnabled": "false"






140

  }






141

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Read System Bypass
