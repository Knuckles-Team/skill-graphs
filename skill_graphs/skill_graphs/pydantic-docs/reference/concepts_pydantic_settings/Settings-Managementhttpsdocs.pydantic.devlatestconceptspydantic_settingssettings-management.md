# Settings Management[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#settings-management)
## Installation[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#installation)
Installation is as simple as:
```
pip install pydantic-settings

```

## Usage[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage)
If you create a model that inherits from `BaseSettings`, the model initialiser will attempt to determine the values of any fields not passed as keyword arguments by reading from the environment. (Default values will still be used if the matching environment variable is not set.)
This makes it easy to:
  * Create a clearly-defined, type-hinted application configuration class
  * Automatically read modifications to the configuration from environment variables
  * Manually override specific settings in the initialiser where desired (e.g. in unit tests)


For example:
```
from collections.abc import Callable
from typing import Any

from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class SubModel(BaseModel):
    foo: str = 'bar'
    apple: int = 1


class Settings(BaseSettings):
    auth_key: str = Field(validation_alias='my_auth_key')  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_1_annotation_1)

    api_key: str = Field(alias='my_api_key')  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_1_annotation_2)

    redis_dsn: RedisDsn = Field(
        'redis://user:pass@localhost:6379/1',
        validation_alias=AliasChoices('service_redis_dsn', 'redis_url'),  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_1_annotation_3)
    )
    pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    amqp_dsn: AmqpDsn = 'amqp://user:pass@localhost:5672/'

    special_function: ImportString[Callable[[Any], Any]] = 'math.cos'  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_1_annotation_4)

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    model_config = SettingsConfigDict(env_prefix='my_prefix_')  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_1_annotation_5)


print(Settings().model_dump())
"""
{
    'auth_key': 'xxx',
    'api_key': 'xxx',
    'redis_dsn': RedisDsn('redis://user:pass@localhost:6379/1'),
    'pg_dsn': PostgresDsn('postgres://user:pass@localhost:5432/foobar'),
    'amqp_dsn': AmqpDsn('amqp://user:pass@localhost:5672/'),
    'special_function': math.cos,
    'domains': set(),
    'more_settings': {'foo': 'bar', 'apple': 1},
}
"""

```

## Validation of default values[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#validation-of-default-values)
Unlike pydantic `BaseModel`, default values of `BaseSettings` fields are validated by default. You can disable this behaviour by setting `validate_default=False` either in `model_config` or on field level by `Field(validate_default=False)`:
```
from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(validate_default=False)

    # default won't be validated
    foo: int = 'test'


print(Settings())
#> foo='test'


class Settings1(BaseSettings):
    # default won't be validated
    foo: int = Field('test', validate_default=False)


print(Settings1())
#> foo='test'

```

Check the [validation of default values](https://docs.pydantic.dev/latest/concepts/fields/#validate-default-values) for more information.
## Environment variable names[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#environment-variable-names)
By default, the environment variable name is the same as the field name.
You can change the prefix for all environment variables by setting the `env_prefix` config setting, or via the `_env_prefix` keyword argument on instantiation:
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='my_prefix_')

    auth_key: str = 'xxx'  # will be read from `my_prefix_auth_key`

```

Note
The default `env_prefix` is `''` (empty string). `env_prefix` is not only for env settings but also for dotenv files, secrets, and other sources.
If you want to change the environment variable name for a single field, you can use an alias.
There are two ways to do this:
  * Using `Field(alias=...)` (see `api_key` above)
  * Using `Field(validation_alias=...)` (see `auth_key` above)


Check the [`Field` aliases documentation](https://docs.pydantic.dev/latest/concepts/fields/#field-aliases) for more information about aliases.
`env_prefix` does not apply to fields with alias. It means the environment variable name is the same as field alias:
```
from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='my_prefix_')

    foo: str = Field('xxx', alias='FooAlias')  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_4_annotation_1)

```

### Case-sensitivity[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#case-sensitivity)
By default, environment variable names are case-insensitive.
If you want to make environment variable names case-sensitive, you can set the `case_sensitive` config setting:
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    redis_host: str = 'localhost'

```

When `case_sensitive` is `True`, the environment variable names must match field names (optionally with a prefix), so in this example `redis_host` could only be modified via `export redis_host`. If you want to name environment variables all upper-case, you should name attribute all upper-case too. You can still name environment variables anything you like through `Field(validation_alias=...)`.
Case-sensitivity can also be set via the `_case_sensitive` keyword argument on instantiation.
In case of nested models, the `case_sensitive` setting will be applied to all nested models.
```
import os

from pydantic import BaseModel, ValidationError

from pydantic_settings import BaseSettings


class RedisSettings(BaseModel):
    host: str
    port: int


class Settings(BaseSettings, case_sensitive=True):
    redis: RedisSettings


os.environ['redis'] = '{"host": "localhost", "port": 6379}'
print(Settings().model_dump())
#> {'redis': {'host': 'localhost', 'port': 6379}}
os.environ['redis'] = '{"HOST": "localhost", "port": 6379}'  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_6_annotation_1)
try:
    Settings()
except ValidationError as e:
    print(e)
    """
    1 validation error for Settings
    redis.host
      Field required [type=missing, input_value={'HOST': 'localhost', 'port': 6379}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2/v/missing
    """

```

Note
On Windows, Python's `os` module always treats environment variables as case-insensitive, so the `case_sensitive` config setting will have no effect - settings will always be updated ignoring case.
## Parsing environment variable values[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values)
By default environment variables are parsed verbatim, including if the value is empty. You can choose to ignore empty environment variables by setting the `env_ignore_empty` config setting to `True`. This can be useful if you would prefer to use the default value for a field rather than an empty value from the environment.
For most simple field types (such as `int`, `float`, `str`, etc.), the environment variable value is parsed the same way it would be if passed directly to the initialiser (as a string).
Complex types like `list`, `set`, `dict`, and sub-models are populated from the environment by treating the environment variable's value as a JSON-encoded string.
Another way to populate nested complex variables is to configure your model with the `env_nested_delimiter` config setting, then use an environment variable with a name pointing to the nested module fields. What it does is simply explodes your variable into nested models or dicts. So if you define a variable `FOO__BAR__BAZ=123` it will convert it into `FOO={'BAR': {'BAZ': 123}}` If you have multiple variables with the same structure they will be merged.
Note
Sub model has to inherit from `pydantic.BaseModel`, Otherwise `pydantic-settings` will initialize sub model, collects values for sub model fields separately, and you may get unexpected results.
As an example, given the following environment variables:
```
# your environment
export V0=0
export SUB_MODEL='{"v1": "json-1", "v2": "json-2"}'
export SUB_MODEL__V2=nested-2
export SUB_MODEL__V3=3
export SUB_MODEL__DEEP__V4=v4

```

You could load them into the following settings model:
```
from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class DeepSubModel(BaseModel):  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_8_annotation_1)
    v4: str


class SubModel(BaseModel):  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_8_annotation_2)
    v1: str
    v2: bytes
    v3: int
    deep: DeepSubModel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='__')

    v0: str
    sub_model: SubModel


print(Settings().model_dump())
"""
{
    'v0': '0',
    'sub_model': {'v1': 'json-1', 'v2': b'nested-2', 'v3': 3, 'deep': {'v4': 'v4'}},
}
"""

```

`env_nested_delimiter` can be configured via the `model_config` as shown above, or via the `_env_nested_delimiter` keyword argument on instantiation.
By default environment variables are split by `env_nested_delimiter` into arbitrarily deep nested fields. You can limit the depth of the nested fields with the `env_nested_max_split` config setting. A common use case this is particularly useful is for two-level deep settings, where the `env_nested_delimiter` (usually a single `_`) may be a substring of model field names. For example:
```
# your environment
export GENERATION_LLM_PROVIDER='anthropic'
export GENERATION_LLM_API_KEY='your-api-key'
export GENERATION_LLM_API_VERSION='2024-03-15'

```

You could load them into the following settings model:
```
from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMConfig(BaseModel):
    provider: str = 'openai'
    api_key: str
    api_type: str = 'azure'
    api_version: str = '2023-03-15-preview'


class GenerationConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter='_', env_nested_max_split=1, env_prefix='GENERATION_'
    )

    llm: LLMConfig
    ...


print(GenerationConfig().model_dump())
"""
{
    'llm': {
        'provider': 'anthropic',
        'api_key': 'your-api-key',
        'api_type': 'azure',
        'api_version': '2024-03-15',
    }
}
"""

```

Without `env_nested_max_split=1` set, `GENERATION_LLM_API_KEY` would be parsed as `llm.api.key` instead of `llm.api_key` and it would raise a `ValidationError`.
Nested environment variables take precedence over the top-level environment variable JSON (e.g. in the example above, `SUB_MODEL__V2` trumps `SUB_MODEL`).
You may also populate a complex type by providing your own source class.
```
import json
import os
from typing import Any

from pydantic.fields import FieldInfo

from pydantic_settings import (
    BaseSettings,
    EnvSettingsSource,
    PydanticBaseSettingsSource,
)


class MyCustomSource(EnvSettingsSource):
    def prepare_field_value(
        self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
    ) -> Any:
        if field_name == 'numbers':
            return [int(x) for x in value.split(',')]
        return json.loads(value)


class Settings(BaseSettings):
    numbers: list[int]

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (MyCustomSource(settings_cls),)


os.environ['numbers'] = '1,2,3'
print(Settings().model_dump())
#> {'numbers': [1, 2, 3]}

```

### Disabling JSON parsing[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#disabling-json-parsing)
pydantic-settings by default parses complex types from environment variables as JSON strings. If you want to disable this behavior for a field and parse the value in your own validator, you can annotate the field with [`NoDecode`](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.NoDecode):
```
import os
from typing import Annotated

from pydantic import field_validator

from pydantic_settings import BaseSettings, NoDecode


class Settings(BaseSettings):
    numbers: Annotated[list[int], NoDecode]  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_12_annotation_1)

    @field_validator('numbers', mode='before')
    @classmethod
    def decode_numbers(cls, v: str) -> list[int]:
        return [int(x) for x in v.split(',')]


os.environ['numbers'] = '1,2,3'
print(Settings().model_dump())
#> {'numbers': [1, 2, 3]}

```

You can also disable JSON parsing for all fields by setting the `enable_decoding` config setting to `False`:
```
import os

from pydantic import field_validator

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(enable_decoding=False)

    numbers: list[int]

    @field_validator('numbers', mode='before')
    @classmethod
    def decode_numbers(cls, v: str) -> list[int]:
        return [int(x) for x in v.split(',')]


os.environ['numbers'] = '1,2,3'
print(Settings().model_dump())
#> {'numbers': [1, 2, 3]}

```

You can force JSON parsing for a field by annotating it with [`ForceDecode`](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.ForceDecode). This will bypass the `enable_decoding` config setting:
```
import os
from typing import Annotated

from pydantic import field_validator

from pydantic_settings import BaseSettings, ForceDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(enable_decoding=False)

    numbers: Annotated[list[int], ForceDecode]
    numbers1: list[int]  [](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#__code_14_annotation_1)

    @field_validator('numbers1', mode='before')
    @classmethod
    def decode_numbers1(cls, v: str) -> list[int]:
        return [int(x) for x in v.split(',')]


os.environ['numbers'] = '["1","2","3"]'
os.environ['numbers1'] = '1,2,3'
print(Settings().model_dump())
#> {'numbers': [1, 2, 3], 'numbers1': [1, 2, 3]}

```

## Nested model default partial updates[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#nested-model-default-partial-updates)
By default, Pydantic settings does not allow partial updates to nested model default objects. This behavior can be overriden by setting the `nested_model_default_partial_update` flag to `True`, which will allow partial updates on nested model default object fields.
```
import os

from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class SubModel(BaseModel):
    val: int = 0
    flag: bool = False


class SettingsPartialUpdate(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter='__', nested_model_default_partial_update=True
    )

    nested_model: SubModel = SubModel(val=1)


class SettingsNoPartialUpdate(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter='__', nested_model_default_partial_update=False
    )

    nested_model: SubModel = SubModel(val=1)


# Apply a partial update to the default object using environment variables
os.environ['NESTED_MODEL__FLAG'] = 'True'

# When partial update is enabled, the existing SubModel instance is updated
# with nested_model.flag=True change
assert SettingsPartialUpdate().model_dump() == {
    'nested_model': {'val': 1, 'flag': True}
}

# When partial update is disabled, a new SubModel instance is instantiated
# with nested_model.flag=True change
assert SettingsNoPartialUpdate().model_dump() == {
    'nested_model': {'val': 0, 'flag': True}
}

```

## Dotenv (.env) support[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support)
Dotenv files (generally named `.env`) are a common pattern that make it easy to use environment variables in a platform-independent manner.
A dotenv file follows the same general principles of all environment variables, and it looks like this:
.env```
