```
readOnly = None

```

####  writeOnly `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.writeOnly "Permanent link")
```
writeOnly = None

```

####  examples `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.examples "Permanent link")
```
examples = None

```

####  discriminator `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.discriminator "Permanent link")
```
discriminator = None

```

####  xml `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.xml "Permanent link")
```
xml = None

```

####  externalDocs `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.externalDocs "Permanent link")
```
externalDocs = None

```

####  example `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.example "Permanent link")
```
example = None

```

Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.
####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Schema.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Example [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "Permanent link")
Bases: `TypedDict`
####  summary `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example.summary "Permanent link")
```
summary

```

####  description `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example.description "Permanent link")
```
description

```

####  value `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example.value "Permanent link")
```
value

```

####  externalValue `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example.externalValue "Permanent link")
```
externalValue

```

###  ParameterInType [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterInType "Permanent link")
Bases: `Enum`
####  query `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterInType.query "Permanent link")
```
query = 'query'

```

####  header `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterInType.header "Permanent link")
```
header = 'header'

```

####  path `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterInType.path "Permanent link")
```
path = 'path'

```

####  cookie `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterInType.cookie "Permanent link")
```
cookie = 'cookie'

```

###  Encoding [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  contentType `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding.contentType "Permanent link")
```
contentType = None

```

####  headers `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding.headers "Permanent link")
```
headers = None

```

####  style `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding.style "Permanent link")
```
style = None

```

####  explode `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding.explode "Permanent link")
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding.allowReserved "Permanent link")
```
allowReserved = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Encoding.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  MediaType [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.MediaType "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  schema_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.MediaType.schema_ "Permanent link")
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.MediaType.example "Permanent link")
```
example = None

```

####  examples `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.MediaType.examples "Permanent link")
```
examples = None

```

####  encoding `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.MediaType.encoding "Permanent link")
```
encoding = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.MediaType.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  ParameterBase [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.description "Permanent link")
```
description = None

```

####  required `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.required "Permanent link")
```
required = None

```

####  deprecated `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.deprecated "Permanent link")
```
deprecated = None

```

####  style `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.style "Permanent link")
```
style = None

```

####  explode `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.explode "Permanent link")
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.allowReserved "Permanent link")
```
allowReserved = None

```

####  schema_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.schema_ "Permanent link")
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.example "Permanent link")
```
example = None

```

####  examples `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.examples "Permanent link")
```
examples = None

```

####  content `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.content "Permanent link")
```
content = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Parameter [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter "Permanent link")
Bases: `ParameterBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ParameterBase</span> \(<code>fastapi.openapi.models.ParameterBase</code>\)")`
####  name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.name "Permanent link")
```
name

```

####  in_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.in_ "Permanent link")
```
in_ = Field(alias='in')

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.description "Permanent link")
```
description = None

```

####  required `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.required "Permanent link")
```
required = None

```

####  deprecated `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.deprecated "Permanent link")
```
deprecated = None

```

####  style `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.style "Permanent link")
```
style = None

```

####  explode `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.explode "Permanent link")
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.allowReserved "Permanent link")
```
allowReserved = None

```

####  schema_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.schema_ "Permanent link")
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.example "Permanent link")
```
example = None

```

####  examples `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.examples "Permanent link")
```
examples = None

```

####  content `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Parameter.content "Permanent link")
```
content = None

```

###  Header [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header "Permanent link")
Bases: `ParameterBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.ParameterBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ParameterBase</span> \(<code>fastapi.openapi.models.ParameterBase</code>\)")`
####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.description "Permanent link")
```
description = None

```

####  required `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.required "Permanent link")
```
required = None

```

####  deprecated `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.deprecated "Permanent link")
```
deprecated = None

```

####  style `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.style "Permanent link")
```
style = None

```

####  explode `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.explode "Permanent link")
```
explode = None

```

####  allowReserved `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.allowReserved "Permanent link")
```
allowReserved = None

```

####  schema_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.schema_ "Permanent link")
```
schema_ = Field(default=None, alias='schema')

```

####  example `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.example "Permanent link")
```
example = None

```

####  examples `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.examples "Permanent link")
```
examples = None

```

####  content `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Header.content "Permanent link")
```
content = None

```

###  RequestBody [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.RequestBody "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.RequestBody.description "Permanent link")
```
description = None

```

####  content `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.RequestBody.content "Permanent link")
```
content

```

####  required `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.RequestBody.required "Permanent link")
```
required = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.RequestBody.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Link [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  operationRef `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.operationRef "Permanent link")
```
operationRef = None

```

####  operationId `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.operationId "Permanent link")
```
operationId = None

```

####  parameters `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.parameters "Permanent link")
```
parameters = None

```

####  requestBody `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.requestBody "Permanent link")
```
requestBody = None

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.description "Permanent link")
```
description = None

```

####  server `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.server "Permanent link")
```
server = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Link.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Response [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Response "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  description `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Response.description "Permanent link")
```
description

```

####  headers `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Response.headers "Permanent link")
```
headers = None

```

####  content `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Response.content "Permanent link")
```
content = None

```

####  links `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Response.links "Permanent link")
```
links = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Response.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Operation [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  tags `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.tags "Permanent link")
```
tags = None

```

####  summary `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.summary "Permanent link")
```
summary = None

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.description "Permanent link")
```
description = None

```

####  externalDocs `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.externalDocs "Permanent link")
```
externalDocs = None

```

####  operationId `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.operationId "Permanent link")
```
operationId = None

```

####  parameters `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.parameters "Permanent link")
```
parameters = None

```

####  requestBody `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.requestBody "Permanent link")
```
requestBody = None

```

####  responses `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.responses "Permanent link")
```
responses = None

```

####  callbacks `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.callbacks "Permanent link")
```
callbacks = None

```

####  deprecated `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.deprecated "Permanent link")
```
deprecated = None

```

####  security `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.security "Permanent link")
```
security = None

```

####  servers `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.servers "Permanent link")
```
servers = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Operation.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  PathItem [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  ref `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.ref "Permanent link")
```
ref = Field(default=None, alias='$ref')

```

####  summary `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.summary "Permanent link")
```
summary = None

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.description "Permanent link")
```
description = None

```

####  get `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.get "Permanent link")
```
get = None

```

####  put `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.put "Permanent link")
```
put = None

```

####  post `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.post "Permanent link")
```
post = None

```

####  delete `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.delete "Permanent link")
```
delete = None

```

####  options `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.options "Permanent link")
```
options = None

```

####  head `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.head "Permanent link")
```
head = None

```

####  patch `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.patch "Permanent link")
```
patch = None

```

####  trace `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.trace "Permanent link")
```
trace = None

```

####  servers `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.servers "Permanent link")
