## Basic model usage[¶](https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage)
Note
Pydantic relies heavily on the existing Python typing constructs to define models. If you are not familiar with those, the following resources can be useful:
  * The
  * The


```
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

    model_config = ConfigDict(str_max_length=10)  [](https://docs.pydantic.dev/latest/concepts/models/#__code_0_annotation_1)

```

In this example, `User` is a model with two fields:
  * `id`, which is an integer (defined using the
  * `name`, which is a string (defined using the


The documentation on [types](https://docs.pydantic.dev/latest/concepts/types/) expands on the supported types.
Fields can be customized in a number of ways using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. See the [documentation on fields](https://docs.pydantic.dev/latest/concepts/fields/) for more information.
The model can then be instantiated:
```
user = User(id='123')

```

`user` is an instance of `User`. Initialization of the object will perform all parsing and validation. If no [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) exception is raised, you know the resulting model instance is valid.
Fields of a model can be accessed as normal attributes of the `user` object:
```
assert user.name == 'Jane Doe'  [](https://docs.pydantic.dev/latest/concepts/models/#__code_2_annotation_1)
assert user.id == 123  [](https://docs.pydantic.dev/latest/concepts/models/#__code_2_annotation_2)
assert isinstance(user.id, int)

```

The model instance can be serialized using the [`model_dump()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump) method:
```
assert user.model_dump() == {'id': 123, 'name': 'Jane Doe'}

```

Calling [`model_dump()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump) also provides numerous arguments to customize the serialization result.
By default, models are mutable and field values can be changed through attribute assignment:
```
user.id = 321
assert user.id == 321

```

Warning
When defining your models, watch out for naming collisions between your field name and its type annotation.
For example, the following will not behave as expected and would yield a validation error:
```
from typing import Optional

from pydantic import BaseModel


class Boo(BaseModel):
    int: Optional[int] = None


m = Boo(int=123)  # Will fail to validate.

```

Because of how Python evaluates `int: None = None`, thus leading to a validation error.
### Model methods and properties[¶](https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties)
The example above only shows the tip of the iceberg of what models can do. Model classes possess the following methods and attributes:
  * [`model_validate()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate): Validates the given object against the Pydantic model. See [Validating data](https://docs.pydantic.dev/latest/concepts/models/#validating-data).
  * [`model_validate_json()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_json): Validates the given JSON data against the Pydantic model. See [Validating data](https://docs.pydantic.dev/latest/concepts/models/#validating-data).
  * [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct): Creates models without running validation. See [Creating models without validation](https://docs.pydantic.dev/latest/concepts/models/#creating-models-without-validation).
  * [`model_dump()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump): Returns a dictionary of the model's fields and values. See [Serialization](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode).
  * [`model_dump_json()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump_json): Returns a JSON string representation of [`model_dump()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump). See [Serialization](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode).
  * [`model_copy()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy): Returns a copy (by default, shallow copy) of the model. See [Model copy](https://docs.pydantic.dev/latest/concepts/models/#model-copy).
  * [`model_json_schema()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema): Returns a jsonable dictionary representing the model's JSON Schema. See [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/).
  * [`model_fields`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields): A mapping between field names and their definitions ([`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) instances).
  * [`model_computed_fields`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_computed_fields): A mapping between computed field names and their definitions ([`ComputedFieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo) instances).
  * [`model_parametrized_name()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_parametrized_name): Computes the class name for parametrizations of generic classes.
  * [`model_post_init()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_post_init): Performs additional actions after the model is instantiated and all field validators are applied.
  * [`model_rebuild()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild): Rebuilds the model schema, which also supports building recursive generic models. See [Rebuilding model schema](https://docs.pydantic.dev/latest/concepts/models/#rebuilding-model-schema).


Model instances possess the following attributes:
  * [`model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra): The extra fields set during validation.
  * [`model_fields_set`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields_set): The set of fields which were explicitly provided when the model was initialized.


Note
See the API documentation of [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) for the class definition including a full list of methods and attributes.
Tip
See [Changes to `pydantic.BaseModel`](https://docs.pydantic.dev/latest/migration/#changes-to-pydanticbasemodel) in the [Migration Guide](https://docs.pydantic.dev/latest/migration/) for details on changes from Pydantic V1.
