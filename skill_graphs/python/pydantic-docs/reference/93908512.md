# ignore comment
ENVIRONMENT="production"
REDIS_ADDRESS=localhost:6379
MEANING_OF_LIFE=42
MY_VAR='Hello world'

```

Once you have your `.env` file filled with variables, _pydantic_ supports loading it in two ways:
  1. Setting the `env_file` (and `env_file_encoding` if you don't want the default encoding of your OS) on `model_config` in the `BaseSettings` class:
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

```

  2. Instantiating the `BaseSettings` derived class with the `_env_file` keyword argument (and the `_env_file_encoding` if needed):
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings(_env_file='prod.env', _env_file_encoding='utf-8')

```

In either case, the value of the passed argument can be any valid path or filename, either absolute or relative to the current working directory. From there, _pydantic_ will handle everything for you by loading in your variables and validating them.


Note
If a filename is specified for `env_file`, Pydantic will only check the current working directory and won't check any parent directories for the `.env` file.
Even when using a dotenv file, _pydantic_ will still read environment variables as well as the dotenv file, **environment variables will always take priority over values loaded from a dotenv file**.
Passing a file path via the `_env_file` keyword argument on instantiation (method 2) will override the value (if any) set on the `model_config` class. If the above snippets were used in conjunction, `prod.env` would be loaded while `.env` would be ignored.
If you need to load multiple dotenv files, you can pass multiple file paths as a tuple or list. The files will be loaded in order, with each file overriding the previous one.
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=('.env', '.env.prod')
    )

```

You can also use the keyword argument override to tell Pydantic not to load any file at all (even if one is set in the `model_config` class) by passing `None` as the instantiation keyword argument, e.g. `settings = Settings(_env_file=None)`.
Because python-dotenv is used to parse the file, bash-like semantics such as `export` can be used which (depending on your OS and environment) may allow your dotenv file to also be used with `source`, see
Pydantic settings consider `extra` config in case of dotenv file. It means if you set the `extra=forbid` (_default_) on `model_config` and your dotenv file contains an entry for a field that is not defined in settings model, it will raise `ValidationError` in settings construction.
For compatibility with pydantic 1.x BaseSettings you should use `extra=ignore`:
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

```

Note
Pydantic settings loads all the values from dotenv file and passes it to the model, regardless of the model's `env_prefix`. So if you provide extra values in a dotenv file, whether they start with `env_prefix` or not, a `ValidationError` will be raised.
## Command Line Support[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#command-line-support)
Pydantic settings provides integrated CLI support, making it easy to quickly define CLI applications using Pydantic models. There are two primary use cases for Pydantic settings CLI:
  1. When using a CLI to override fields in Pydantic models.
  2. When using Pydantic models to define CLIs.


By default, the experience is tailored towards use case #1 and builds on the foundations established in [parsing environment variables](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values). If your use case primarily falls into #2, you will likely want to enable most of the defaults outlined at the end of [creating CLI applications](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#creating-cli-applications).
### The Basics[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#the-basics)
To get started, let's revisit the example presented in [parsing environment variables](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values) but using a Pydantic settings CLI:
```
import sys

from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class DeepSubModel(BaseModel):
    v4: str


class SubModel(BaseModel):
    v1: str
    v2: bytes
    v3: int
    deep: DeepSubModel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(cli_parse_args=True)

    v0: str
    sub_model: SubModel


sys.argv = [
    'example.py',
    '--v0=0',
    '--sub_model={"v1": "json-1", "v2": "json-2"}',
    '--sub_model.v2=nested-2',
    '--sub_model.v3=3',
    '--sub_model.deep.v4=v4',
]

print(Settings().model_dump())
"""
{
    'v0': '0',
    'sub_model': {'v1': 'json-1', 'v2': b'nested-2', 'v3': 3, 'deep': {'v4': 'v4'}},
}
"""

```

To enable CLI parsing, we simply set the `cli_parse_args` flag to a valid value, which retains similar connotations as defined in `argparse`.
Note that a CLI settings source is [**the topmost source**](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#field-value-priority) by default unless its [priority value is customised](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customise-settings-sources):
```
import os
import sys

from pydantic_settings import (
    BaseSettings,
    CliSettingsSource,
    PydanticBaseSettingsSource,
)


class Settings(BaseSettings):
    my_foo: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, CliSettingsSource(settings_cls, cli_parse_args=True)


os.environ['MY_FOO'] = 'from environment'

sys.argv = ['example.py', '--my_foo=from cli']

print(Settings().model_dump())
#> {'my_foo': 'from environment'}

```

#### Lists[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#lists)
CLI argument parsing of lists supports intermixing of any of the below three styles:
  * JSON style `--field='[1,2]'`
  * Argparse style `--field 1 --field 2`
  * Lazy style `--field=1,2`


```
import sys

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True):
    my_list: list[int]


sys.argv = ['example.py', '--my_list', '[1,2]']
print(Settings().model_dump())
#> {'my_list': [1, 2]}

sys.argv = ['example.py', '--my_list', '1', '--my_list', '2']
print(Settings().model_dump())
#> {'my_list': [1, 2]}

sys.argv = ['example.py', '--my_list', '1,2']
print(Settings().model_dump())
#> {'my_list': [1, 2]}

```

#### Dictionaries[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dictionaries)
CLI argument parsing of dictionaries supports intermixing of any of the below two styles:
  * JSON style `--field='{"k1": 1, "k2": 2}'`
  * Environment variable style `--field k1=1 --field k2=2`


These can be used in conjunction with list forms as well, e.g:
  * `--field k1=1,k2=2 --field k3=3 --field '{"k4": 4}'` etc.


```
import sys

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True):
    my_dict: dict[str, int]


sys.argv = ['example.py', '--my_dict', '{"k1":1,"k2":2}']
print(Settings().model_dump())
#> {'my_dict': {'k1': 1, 'k2': 2}}

sys.argv = ['example.py', '--my_dict', 'k1=1', '--my_dict', 'k2=2']
print(Settings().model_dump())
#> {'my_dict': {'k1': 1, 'k2': 2}}

```

#### Literals and Enums[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#literals-and-enums)
CLI argument parsing of literals and enums are converted into CLI choices.
```
import sys
from enum import IntEnum
from typing import Literal

from pydantic_settings import BaseSettings


class Fruit(IntEnum):
    pear = 0
    kiwi = 1
    lime = 2


class Settings(BaseSettings, cli_parse_args=True):
    fruit: Fruit
    pet: Literal['dog', 'cat', 'bird']


sys.argv = ['example.py', '--fruit', 'lime', '--pet', 'cat']
print(Settings().model_dump())
#> {'fruit': <Fruit.lime: 2>, 'pet': 'cat'}

```

#### Aliases[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#aliases)
Pydantic field aliases are added as CLI argument aliases. Aliases of length one are converted into short options.
```
import sys

from pydantic import AliasChoices, AliasPath, Field

from pydantic_settings import BaseSettings


class User(BaseSettings, cli_parse_args=True):
    first_name: str = Field(
        validation_alias=AliasChoices('f', 'fname', AliasPath('name', 0))
    )
    last_name: str = Field(
        validation_alias=AliasChoices('l', 'lname', AliasPath('name', 1))
    )


sys.argv = ['example.py', '--fname', 'John', '--lname', 'Doe']
print(User().model_dump())
#> {'first_name': 'John', 'last_name': 'Doe'}

sys.argv = ['example.py', '-f', 'John', '-l', 'Doe']
print(User().model_dump())
#> {'first_name': 'John', 'last_name': 'Doe'}

sys.argv = ['example.py', '--name', 'John,Doe']
print(User().model_dump())
#> {'first_name': 'John', 'last_name': 'Doe'}

sys.argv = ['example.py', '--name', 'John', '--lname', 'Doe']
print(User().model_dump())
#> {'first_name': 'John', 'last_name': 'Doe'}

```

### Subcommands and Positional Arguments[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#subcommands-and-positional-arguments)
Subcommands and positional arguments are expressed using the `CliSubCommand` and `CliPositionalArg` annotations. The subcommand annotation can only be applied to required fields (i.e. fields that do not have a default value). Furthermore, subcommands must be a valid type derived from either a pydantic `BaseModel` or pydantic.dataclasses `dataclass`.
Parsed subcommands can be retrieved from model instances using the `get_subcommand` utility function. If a subcommand is not required, set the `is_required` flag to `False` to disable raising an error if no subcommand is found.
Note
CLI settings subcommands are limited to a single subparser per model. In other words, all subcommands for a model are grouped under a single subparser; it does not allow for multiple subparsers with each subparser having its own set of subcommands. For more information on subparsers, see
Note
`CliSubCommand` and `CliPositionalArg` are always case sensitive.
```
import sys

from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    CliPositionalArg,
    CliSubCommand,
    SettingsError,
    get_subcommand,
)


class Init(BaseModel):
    directory: CliPositionalArg[str]


class Clone(BaseModel):
    repository: CliPositionalArg[str]
    directory: CliPositionalArg[str]


class Git(BaseSettings, cli_parse_args=True, cli_exit_on_error=False):
    clone: CliSubCommand[Clone]
    init: CliSubCommand[Init]
