##  fastapi.openapi.models [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models "Permanent link")
###  SchemaType `module-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SchemaType "Permanent link")
```
SchemaType = Literal[
    "array",
    "boolean",
    "integer",
    "null",
    "number",
    "object",
    "string",
]

```

###  SchemaOrBool `module-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SchemaOrBool "Permanent link")
```
SchemaOrBool = Schema[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Schema</span> \(<code>fastapi.openapi.models.Schema</code>\)") | bool

```

###  SecurityScheme `module-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityScheme "Permanent link")
```
SecurityScheme = (
    APIKey[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">APIKey</span> \(<code>fastapi.openapi.models.APIKey</code>\)") | HTTPBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">HTTPBase</span> \(<code>fastapi.openapi.models.HTTPBase</code>\)") | OAuth2[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuth2</span> \(<code>fastapi.openapi.models.OAuth2</code>\)") | OpenIdConnect[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OpenIdConnect</span> \(<code>fastapi.openapi.models.OpenIdConnect</code>\)") | HTTPBearer[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">HTTPBearer</span> \(<code>fastapi.openapi.models.HTTPBearer</code>\)")
)

```

###  BaseModelWithConfig [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "Permanent link")
Bases: `BaseModel`
####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Contact [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Contact "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  name `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Contact.name "Permanent link")
```
name = None

```

####  url `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Contact.url "Permanent link")
```
url = None

```

####  email `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Contact.email "Permanent link")
```
email = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Contact.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  License [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.License "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.License.name "Permanent link")
```
name

```

####  identifier `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.License.identifier "Permanent link")
```
identifier = None

```

####  url `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.License.url "Permanent link")
```
url = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.License.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Info [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  title `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.title "Permanent link")
```
title

```

####  summary `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.summary "Permanent link")
```
summary = None

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.description "Permanent link")
```
description = None

```

####  termsOfService `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.termsOfService "Permanent link")
```
termsOfService = None

```

####  contact `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.contact "Permanent link")
```
contact = None

```

####  license `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.license "Permanent link")
```
license = None

```

####  version `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.version "Permanent link")
```
version

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Info.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  ServerVariable [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ServerVariable "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  enum `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ServerVariable.enum "Permanent link")
```
enum = None

```

####  default `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ServerVariable.default "Permanent link")
```
default

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ServerVariable.description "Permanent link")
```
description = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ServerVariable.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Server [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Server "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  url `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Server.url "Permanent link")
```
url

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Server.description "Permanent link")
```
description = None

```

####  variables `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Server.variables "Permanent link")
```
variables = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Server.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Reference [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Reference "Permanent link")
Bases: `BaseModel`
####  ref `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Reference.ref "Permanent link")
```
ref = Field(alias='$ref')

```

###  Discriminator [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Discriminator "Permanent link")
Bases: `BaseModel`
####  propertyName `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Discriminator.propertyName "Permanent link")
```
propertyName

```

####  mapping `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Discriminator.mapping "Permanent link")
```
mapping = None

```

###  XML [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  name `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML.name "Permanent link")
```
name = None

```

####  namespace `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML.namespace "Permanent link")
```
namespace = None

```

####  prefix `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML.prefix "Permanent link")
```
prefix = None

```

####  attribute `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML.attribute "Permanent link")
```
attribute = None

```

####  wrapped `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML.wrapped "Permanent link")
```
wrapped = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.XML.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  ExternalDocumentation [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ExternalDocumentation "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ExternalDocumentation.description "Permanent link")
```
description = None

```

####  url `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ExternalDocumentation.url "Permanent link")
```
url

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ExternalDocumentation.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Schema [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  schema_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.schema_ "Permanent link")
```
schema_ = Field(default=None, alias='$schema')

```

####  vocabulary `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.vocabulary "Permanent link")
```
vocabulary = Field(default=None, alias='$vocabulary')

```

####  id `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.id "Permanent link")
```
id = Field(default=None, alias='$id')

```

####  anchor `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.anchor "Permanent link")
```
anchor = Field(default=None, alias='$anchor')

```

####  dynamicAnchor `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.dynamicAnchor "Permanent link")
```
dynamicAnchor = Field(default=None, alias='$dynamicAnchor')

```

####  ref `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.ref "Permanent link")
```
ref = Field(default=None, alias='$ref')

```

####  dynamicRef `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.dynamicRef "Permanent link")
```
dynamicRef = Field(default=None, alias='$dynamicRef')

```

####  defs `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.defs "Permanent link")
```
defs = Field(default=None, alias='$defs')

```

####  comment `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.comment "Permanent link")
```
comment = Field(default=None, alias='$comment')

```

####  allOf `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.allOf "Permanent link")
```
allOf = None

```

####  anyOf `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.anyOf "Permanent link")
```
anyOf = None

```

####  oneOf `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.oneOf "Permanent link")
```
oneOf = None

```

####  not_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.not_ "Permanent link")
```
not_ = Field(default=None, alias='not')

```

####  if_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.if_ "Permanent link")
```
if_ = Field(default=None, alias='if')

```

####  then `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.then "Permanent link")
```
then = None

```

####  else_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.else_ "Permanent link")
```
else_ = Field(default=None, alias='else')

```

####  dependentSchemas `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.dependentSchemas "Permanent link")
```
dependentSchemas = None

```

####  prefixItems `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.prefixItems "Permanent link")
```
prefixItems = None

```

####  items `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.items "Permanent link")
```
items = None

```

####  contains `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.contains "Permanent link")
```
contains = None

```

####  properties `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.properties "Permanent link")
```
properties = None

```

####  patternProperties `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.patternProperties "Permanent link")
```
patternProperties = None

```

####  additionalProperties `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.additionalProperties "Permanent link")
```
additionalProperties = None

```

####  propertyNames `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.propertyNames "Permanent link")
```
propertyNames = None

```

####  unevaluatedItems `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.unevaluatedItems "Permanent link")
```
unevaluatedItems = None

```

####  unevaluatedProperties `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.unevaluatedProperties "Permanent link")
```
unevaluatedProperties = None

```

####  type `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.type "Permanent link")
```
type = None

```

####  enum `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.enum "Permanent link")
```
enum = None

```

####  const `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.const "Permanent link")
```
const = None

```

####  multipleOf `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.multipleOf "Permanent link")
```
multipleOf = Field(default=None, gt=0)

```

####  maximum `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.maximum "Permanent link")
```
maximum = None

```

####  exclusiveMaximum `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.exclusiveMaximum "Permanent link")
```
exclusiveMaximum = None

```

####  minimum `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.minimum "Permanent link")
```
minimum = None

```

####  exclusiveMinimum `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.exclusiveMinimum "Permanent link")
```
exclusiveMinimum = None

```

####  maxLength `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.maxLength "Permanent link")
```
maxLength = Field(default=None, ge=0)

```

####  minLength `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.minLength "Permanent link")
```
minLength = Field(default=None, ge=0)

```

####  pattern `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.pattern "Permanent link")
```
pattern = None

```

####  maxItems `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.maxItems "Permanent link")
```
maxItems = Field(default=None, ge=0)

```

####  minItems `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.minItems "Permanent link")
```
minItems = Field(default=None, ge=0)

```

####  uniqueItems `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.uniqueItems "Permanent link")
```
uniqueItems = None

```

####  maxContains `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.maxContains "Permanent link")
```
maxContains = Field(default=None, ge=0)

```

####  minContains `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.minContains "Permanent link")
```
minContains = Field(default=None, ge=0)

```

####  maxProperties `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.maxProperties "Permanent link")
```
maxProperties = Field(default=None, ge=0)

```

####  minProperties `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.minProperties "Permanent link")
```
minProperties = Field(default=None, ge=0)

```

####  required `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.required "Permanent link")
```
required = None

```

####  dependentRequired `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.dependentRequired "Permanent link")
```
dependentRequired = None

```

####  format `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.format "Permanent link")
```
format = None

```

####  contentEncoding `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.contentEncoding "Permanent link")
```
contentEncoding = None

```

####  contentMediaType `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.contentMediaType "Permanent link")
```
contentMediaType = None

```

####  contentSchema `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.contentSchema "Permanent link")
```
contentSchema = None

```

####  title `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.title "Permanent link")
```
title = None

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.description "Permanent link")
```
description = None

```

####  default `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.default "Permanent link")
```
default = None

```

####  deprecated `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.deprecated "Permanent link")
```
deprecated = None

```

####  readOnly `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.readOnly "Permanent link")
