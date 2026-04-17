# Models
API Documentation
[`pydantic.main.BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)

One of the primary ways of defining schema in Pydantic is via models. Models are simply classes which inherit from [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) and define fields as annotated attributes.
You can think of models as similar to structs in languages like C, or as the requirements of a single endpoint in an API.
Models share many similarities with Python's [Dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/) section of the docs.
Untrusted data can be passed to a model and, after parsing and validation, Pydantic guarantees that the fields of the resultant model instance will conform to the field types defined on the model.
Validation — a _deliberate_ misnomer
### TL;DR
We use the term "validation" to refer to the process of instantiating a model (or other type) that adheres to specified types and constraints. This task, which Pydantic is well known for, is most widely recognized as "validation" in colloquial terms, even though in other contexts the term "validation" may be more restrictive.
* * *
### The long version
The potential confusion around the term "validation" arises from the fact that, strictly speaking, Pydantic's primary focus doesn't align precisely with the dictionary definition of "validation":
> ### validation
> _noun_ the action of checking or proving the validity or accuracy of something.
In Pydantic, the term "validation" refers to the process of instantiating a model (or other type) that adheres to specified types and constraints. Pydantic guarantees the types and constraints of the output, not the input data. This distinction becomes apparent when considering that Pydantic's `ValidationError` is raised when data cannot be successfully parsed into a model instance.
While this distinction may initially seem subtle, it holds practical significance. In some cases, "validation" goes beyond just model creation, and can include the copying and coercion of data. This can involve copying arguments passed to the constructor in order to perform coercion to a new type without mutating the original input data. For a more in-depth understanding of the implications for your usage, refer to the [Data Conversion](https://docs.pydantic.dev/latest/concepts/models/#data-conversion) and [Attribute Copies](https://docs.pydantic.dev/latest/concepts/models/#attribute-copies) sections below.
In essence, Pydantic's primary goal is to assure that the resulting structure post-processing (termed "validation") precisely conforms to the applied type hints. Given the widespread adoption of "validation" as the colloquial term for this process, we will consistently use it in our documentation.
While the terms "parse" and "validation" were previously used interchangeably, moving forward, we aim to exclusively employ "validate", with "parse" reserved specifically for discussions related to [JSON parsing](https://docs.pydantic.dev/latest/concepts/json/).
