# otherwise, asyncio.run() is used to execute this async method.
assert CliApp.run(AsyncSettings, cli_args=[]).model_dump() == {}

```

#### Asynchronous Subcommands[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#asynchronous-subcommands)
As mentioned above, you can also define subcommands as async. However, only do so for the leaf (lowest-level) subcommand to avoid spawning new threads and event loops unnecessarily in parent commands:
```
from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    CliApp,
    CliPositionalArg,
    CliSubCommand,
)


class Clone(BaseModel):
    repository: CliPositionalArg[str]
    directory: CliPositionalArg[str]

    async def cli_cmd(self) -> None:
        # Perform async tasks here, e.g. network or I/O operations
        print(f'Cloning async from "{self.repository}" into "{self.directory}"')
        #> Cloning async from "repo" into "dir"


class Git(BaseSettings):
    clone: CliSubCommand[Clone]

    def cli_cmd(self) -> None:
        # Run the final subcommand (clone/init). It is recommended to define async methods only at the deepest level.
        CliApp.run_subcommand(self)


CliApp.run(Git, cli_args=['clone', 'repo', 'dir']).model_dump() == {
    'repository': 'repo',
    'directory': 'dir',
}

```

When executing a subcommand with an asynchronous cli_cmd, Pydantic settings automatically detects whether the current thread already has an active event loop. If so, the async command is run in a fresh thread to avoid conflicts. Otherwise, it uses asyncio.run() in the current thread. This handling ensures your asynchronous subcommands "just work" without additional manual setup.
### Serializing CLI Arguments[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#serializing-cli-arguments)
An instantiated Pydantic model can be serialized into its CLI arguments using the `CliApp.serialize` method.
```
from pydantic import BaseModel

from pydantic_settings import CliApp


class Nested(BaseModel):
    that: int


class Settings(BaseModel):
    this: str
    nested: Nested


print(CliApp.serialize(Settings(this='hello', nested=Nested(that=123))))
#> ['--this', 'hello', '--nested.that', '123']

```

### Mutually Exclusive Groups[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#mutually-exclusive-groups)
CLI mutually exclusive groups can be created by inheriting from the `CliMutuallyExclusiveGroup` class.
Note
A `CliMutuallyExclusiveGroup` cannot be used in a union or contain nested models.
```
from typing import Optional

from pydantic import BaseModel

from pydantic_settings import CliApp, CliMutuallyExclusiveGroup, SettingsError


class Circle(CliMutuallyExclusiveGroup):
    radius: Optional[float] = None
    diameter: Optional[float] = None
    perimeter: Optional[float] = None


class Settings(BaseModel):
    circle: Circle


try:
    CliApp.run(
        Settings,
        cli_args=['--circle.radius=1', '--circle.diameter=2'],
        cli_exit_on_error=False,
    )
except SettingsError as e:
    print(e)
    """
    error parsing CLI: argument --circle.diameter: not allowed with argument --circle.radius
    """

```

### Customizing the CLI Experience[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customizing-the-cli-experience)
The below flags can be used to customise the CLI experience to your needs.
#### Change the Displayed Program Name[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#change-the-displayed-program-name)
Change the default program name displayed in the help text usage by setting `cli_prog_name`. By default, it will derive the name of the currently executing program from `sys.argv[0]`, just like argparse.
```
import sys

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True, cli_prog_name='appdantic'):
    pass


try:
    sys.argv = ['example.py', '--help']
    Settings()
except SystemExit as e:
    print(e)
    #> 0
"""
usage: appdantic [-h]

options:
  -h, --help  show this help message and exit
"""

```

#### CLI Boolean Flags[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#cli-boolean-flags)
Change whether boolean fields should be explicit or implicit by default using the `cli_implicit_flags` setting. By default, boolean fields are "explicit", meaning a boolean value must be explicitly provided on the CLI, e.g. `--flag=True`. Conversely, boolean fields that are "implicit" derive the value from the flag itself, e.g. `--flag,--no-flag`, which removes the need for an explicit value to be passed.
Additionally, the provided `CliImplicitFlag` and `CliExplicitFlag` annotations can be used for more granular control when necessary.
```
from pydantic_settings import BaseSettings, CliExplicitFlag, CliImplicitFlag


class ExplicitSettings(BaseSettings, cli_parse_args=True):
    """Boolean fields are explicit by default."""

    explicit_req: bool
    """
    --explicit_req bool   (required)
    """

    explicit_opt: bool = False
    """
    --explicit_opt bool   (default: False)
    """

    # Booleans are explicit by default, so must override implicit flags with annotation
    implicit_req: CliImplicitFlag[bool]
    """
    --implicit_req, --no-implicit_req (required)
    """

    implicit_opt: CliImplicitFlag[bool] = False
    """
    --implicit_opt, --no-implicit_opt (default: False)
    """


class ImplicitSettings(BaseSettings, cli_parse_args=True, cli_implicit_flags=True):
    """With cli_implicit_flags=True, boolean fields are implicit by default."""

    # Booleans are implicit by default, so must override explicit flags with annotation
    explicit_req: CliExplicitFlag[bool]
    """
    --explicit_req bool   (required)
    """

    explicit_opt: CliExplicitFlag[bool] = False
    """
    --explicit_opt bool   (default: False)
    """

    implicit_req: bool
    """
    --implicit_req, --no-implicit_req (required)
    """

    implicit_opt: bool = False
    """
    --implicit_opt, --no-implicit_opt (default: False)
    """

```

#### Ignore and Retrieve Unknown Arguments[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#ignore-and-retrieve-unknown-arguments)
Change whether to ignore unknown CLI arguments and only parse known ones using `cli_ignore_unknown_args`. By default, the CLI does not ignore any args. Ignored arguments can then be retrieved using the `CliUnknownArgs` annotation.
```
import sys

from pydantic_settings import BaseSettings, CliUnknownArgs


class Settings(BaseSettings, cli_parse_args=True, cli_ignore_unknown_args=True):
    good_arg: str
    ignored_args: CliUnknownArgs


sys.argv = ['example.py', '--bad-arg=bad', 'ANOTHER_BAD_ARG', '--good_arg=hello world']
print(Settings().model_dump())
#> {'good_arg': 'hello world', 'ignored_args': ['--bad-arg=bad', 'ANOTHER_BAD_ARG']}

```

#### CLI Kebab Case for Arguments[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#cli-kebab-case-for-arguments)
Change whether CLI arguments should use kebab case by enabling `cli_kebab_case`. By default, `cli_kebab_case=True` will ignore enum fields, and is equivalent to `cli_kebab_case='no_enums'`. To apply kebab case to everything, including enums, use `cli_kebab_case='all'`.
```
import sys

from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True, cli_kebab_case=True):
    my_option: str = Field(description='will show as kebab case on CLI')


try:
    sys.argv = ['example.py', '--help']
    Settings()
except SystemExit as e:
    print(e)
    #> 0
"""
usage: example.py [-h] [--my-option str]

options:
  -h, --help       show this help message and exit
  --my-option str  will show as kebab case on CLI (required)
"""

```

#### Change Whether CLI Should Exit on Error[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#change-whether-cli-should-exit-on-error)
Change whether the CLI internal parser will exit on error or raise a `SettingsError` exception by using `cli_exit_on_error`. By default, the CLI internal parser will exit on error.
```
import sys

from pydantic_settings import BaseSettings, SettingsError


class Settings(BaseSettings, cli_parse_args=True, cli_exit_on_error=False): ...


try:
    sys.argv = ['example.py', '--bad-arg']
    Settings()
except SettingsError as e:
    print(e)
    #> error parsing CLI: unrecognized arguments: --bad-arg

```

#### Enforce Required Arguments at CLI[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#enforce-required-arguments-at-cli)
Pydantic settings is designed to pull values in from various sources when instantiating a model. This means a field that is required is not strictly required from any single source (e.g. the CLI). Instead, all that matters is that one of the sources provides the required value.
However, if your use case [aligns more with #2](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#command-line-support), using Pydantic models to define CLIs, you will likely want required fields to be _strictly required at the CLI_. We can enable this behavior by using `cli_enforce_required`.
Note
A required `CliPositionalArg` field is always strictly required (enforced) at the CLI.
```
import os
import sys

from pydantic import Field

from pydantic_settings import BaseSettings, SettingsError


class Settings(
    BaseSettings,
    cli_parse_args=True,
    cli_enforce_required=True,
    cli_exit_on_error=False,
):
    my_required_field: str = Field(description='a top level required field')


os.environ['MY_REQUIRED_FIELD'] = 'hello from environment'

try:
    sys.argv = ['example.py']
    Settings()
except SettingsError as e:
    print(e)
    #> error parsing CLI: the following arguments are required: --my_required_field

```

#### Change the None Type Parse String[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#change-the-none-type-parse-string)
Change the CLI string value that will be parsed (e.g. "null", "void", "None", etc.) into `None` by setting `cli_parse_none_str`. By default it will use the `env_parse_none_str` value if set. Otherwise, it will default to "null" if `cli_avoid_json` is `False`, and "None" if `cli_avoid_json` is `True`.
```
import sys
from typing import Optional

from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True, cli_parse_none_str='void'):
    v1: Optional[int] = Field(description='the top level v0 option')


sys.argv = ['example.py', '--v1', 'void']
print(Settings().model_dump())
#> {'v1': None}

```

#### Hide None Type Values[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#hide-none-type-values)
Hide `None` values from the CLI help text by enabling `cli_hide_none_type`.
```
import sys
from typing import Optional

from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True, cli_hide_none_type=True):
    v0: Optional[str] = Field(description='the top level v0 option')


try:
    sys.argv = ['example.py', '--help']
    Settings()
except SystemExit as e:
    print(e)
    #> 0
"""
usage: example.py [-h] [--v0 str]

options:
  -h, --help  show this help message and exit
  --v0 str    the top level v0 option (required)
"""

```

#### Avoid Adding JSON CLI Options[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#avoid-adding-json-cli-options)
Avoid adding complex fields that result in JSON strings at the CLI by enabling `cli_avoid_json`.
```
import sys

from pydantic import BaseModel, Field

from pydantic_settings import BaseSettings


class SubModel(BaseModel):
    v1: int = Field(description='the sub model v1 option')


class Settings(BaseSettings, cli_parse_args=True, cli_avoid_json=True):
    sub_model: SubModel = Field(
        description='The help summary for SubModel related options'
    )


try:
    sys.argv = ['example.py', '--help']
    Settings()
except SystemExit as e:
    print(e)
    #> 0
"""
usage: example.py [-h] [--sub_model.v1 int]

options:
  -h, --help          show this help message and exit

sub_model options:
  The help summary for SubModel related options

  --sub_model.v1 int  the sub model v1 option (required)
"""

```

#### Use Class Docstring for Group Help Text[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#use-class-docstring-for-group-help-text)
By default, when populating the group help text for nested models it will pull from the field descriptions. Alternatively, we can also configure CLI settings to pull from the class docstring instead.
Note
If the field is a union of nested models the group help text will always be pulled from the field description; even if `cli_use_class_docs_for_groups` is set to `True`.
```
import sys

from pydantic import BaseModel, Field

from pydantic_settings import BaseSettings


class SubModel(BaseModel):
    """The help text from the class docstring."""

    v1: int = Field(description='the sub model v1 option')


class Settings(BaseSettings, cli_parse_args=True, cli_use_class_docs_for_groups=True):
    """My application help text."""

    sub_model: SubModel = Field(description='The help text from the field description')


try:
    sys.argv = ['example.py', '--help']
    Settings()
except SystemExit as e:
    print(e)
    #> 0
"""
usage: example.py [-h] [--sub_model JSON] [--sub_model.v1 int]

My application help text.

options:
  -h, --help          show this help message and exit

sub_model options:
  The help text from the class docstring.

  --sub_model JSON    set sub_model from JSON string
  --sub_model.v1 int  the sub model v1 option (required)
"""

```

#### Change the CLI Flag Prefix Character[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#change-the-cli-flag-prefix-character)
Change The CLI flag prefix character used in CLI optional arguments by settings `cli_flag_prefix_char`.
```
import sys

from pydantic import AliasChoices, Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings, cli_parse_args=True, cli_flag_prefix_char='+'):
    my_arg: str = Field(validation_alias=AliasChoices('m', 'my-arg'))


sys.argv = ['example.py', '++my-arg', 'hi']
print(Settings().model_dump())
#> {'my_arg': 'hi'}

sys.argv = ['example.py', '+m', 'hi']
print(Settings().model_dump())
#> {'my_arg': 'hi'}

```

#### Suppressing Fields from CLI Help Text[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#suppressing-fields-from-cli-help-text)
To suppress a field from the CLI help text, the `CliSuppress` annotation can be used for field types, or the `CLI_SUPPRESS` string constant can be used for field descriptions.
```
import sys

from pydantic import Field

from pydantic_settings import CLI_SUPPRESS, BaseSettings, CliSuppress


class Settings(BaseSettings, cli_parse_args=True):
    """Suppress fields from CLI help text."""

    field_a: CliSuppress[int] = 0
    field_b: str = Field(default=1, description=CLI_SUPPRESS)


try:
    sys.argv = ['example.py', '--help']
    Settings()
except SystemExit as e:
    print(e)
    #> 0
"""
usage: example.py [-h]

Suppress fields from CLI help text.

options:
  -h, --help          show this help message and exit
"""

```

#### CLI Shortcuts for Arguments[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#cli-shortcuts-for-arguments)
Add alternative CLI argument names (shortcuts) for fields using the `cli_shortcuts` option in `SettingsConfigDict`. This allows you to define additional names for CLI arguments, which can be especially useful for providing more user-friendly or shorter aliases for deeply nested or verbose field names.
The `cli_shortcuts` option takes a dictionary mapping the target field name (using dot notation for nested fields) to one or more shortcut names. If multiple fields share the same shortcut, the first matching field will take precedence.
**Flat Example:**
```
from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    option: str = Field(default='foo')
    list_option: str = Field(default='fizz')

    model_config = SettingsConfigDict(
        cli_shortcuts={'option': 'option2', 'list_option': ['list_option2']}
    )
