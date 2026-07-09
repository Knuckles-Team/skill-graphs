# Returns the subcommand model instance (in this case, 'clone')
assert get_subcommand(cmd).model_dump() == {
    'directory': 'dest',
    'repository': 'repo',
}

```

The `CliSubCommand` and `CliPositionalArg` annotations also support union operations and aliases. For unions of Pydantic models, it is important to remember the [nuances](https://docs.pydantic.dev/latest/concepts/unions/) that can arise during validation. Specifically, for unions of subcommands that are identical in content, it is recommended to break them out into separate `CliSubCommand` fields to avoid any complications. Lastly, the derived subcommand names from unions will be the names of the Pydantic model classes themselves.
When assigning aliases to `CliSubCommand` or `CliPositionalArg` fields, only a single alias can be assigned. For non-union subcommands, aliasing will change the displayed help text and subcommand name. Conversely, for union subcommands, aliasing will have no tangible effect from the perspective of the CLI settings source. Lastly, for positional arguments, aliasing will change the CLI help text displayed for the field.
```
import sys
from typing import Union

from pydantic import BaseModel, Field

from pydantic_settings import (
    BaseSettings,
    CliPositionalArg,
    CliSubCommand,
    get_subcommand,
)


class Alpha(BaseModel):
    """Apha Help"""

    cmd_alpha: CliPositionalArg[str] = Field(alias='alpha-cmd')


class Beta(BaseModel):
    """Beta Help"""

    opt_beta: str = Field(alias='opt-beta')


class Gamma(BaseModel):
    """Gamma Help"""

    opt_gamma: str = Field(alias='opt-gamma')


class Root(BaseSettings, cli_parse_args=True, cli_exit_on_error=False):
    alpha_or_beta: CliSubCommand[Union[Alpha, Beta]] = Field(alias='alpha-or-beta-cmd')
    gamma: CliSubCommand[Gamma] = Field(alias='gamma-cmd')


sys.argv = ['example.py', 'Alpha', 'hello']
assert get_subcommand(Root()).model_dump() == {'cmd_alpha': 'hello'}

sys.argv = ['example.py', 'Beta', '--opt-beta=hey']
assert get_subcommand(Root()).model_dump() == {'opt_beta': 'hey'}

sys.argv = ['example.py', 'gamma-cmd', '--opt-gamma=hi']
assert get_subcommand(Root()).model_dump() == {'opt_gamma': 'hi'}

```

### Creating CLI Applications[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#creating-cli-applications)
The `CliApp` class provides two utility methods, `CliApp.run` and `CliApp.run_subcommand`, that can be used to run a Pydantic `BaseSettings`, `BaseModel`, or `pydantic.dataclasses.dataclass` as a CLI application. Primarily, the methods provide structure for running `cli_cmd` methods associated with models.
`CliApp.run` can be used in directly providing the `cli_args` to be parsed, and will run the model `cli_cmd` method (if defined) after instantiation:
```
from pydantic_settings import BaseSettings, CliApp


class Settings(BaseSettings):
    this_foo: str

    def cli_cmd(self) -> None:
        # Print the parsed data
        print(self.model_dump())
        #> {'this_foo': 'is such a foo'}

        # Update the parsed data showing cli_cmd ran
        self.this_foo = 'ran the foo cli cmd'


s = CliApp.run(Settings, cli_args=['--this_foo', 'is such a foo'])
print(s.model_dump())
#> {'this_foo': 'ran the foo cli cmd'}

```

Similarly, the `CliApp.run_subcommand` can be used in recursive fashion to run the `cli_cmd` method of a subcommand:
```
from pydantic import BaseModel

from pydantic_settings import CliApp, CliPositionalArg, CliSubCommand


class Init(BaseModel):
    directory: CliPositionalArg[str]

    def cli_cmd(self) -> None:
        print(f'git init "{self.directory}"')
        #> git init "dir"
        self.directory = 'ran the git init cli cmd'


class Clone(BaseModel):
    repository: CliPositionalArg[str]
    directory: CliPositionalArg[str]

    def cli_cmd(self) -> None:
        print(f'git clone from "{self.repository}" into "{self.directory}"')
        self.directory = 'ran the clone cli cmd'


class Git(BaseModel):
    clone: CliSubCommand[Clone]
    init: CliSubCommand[Init]

    def cli_cmd(self) -> None:
        CliApp.run_subcommand(self)


cmd = CliApp.run(Git, cli_args=['init', 'dir'])
assert cmd.model_dump() == {
    'clone': None,
    'init': {'directory': 'ran the git init cli cmd'},
}

```

Note
Unlike `CliApp.run`, `CliApp.run_subcommand` requires the subcommand model to have a defined `cli_cmd` method.
For `BaseModel` and `pydantic.dataclasses.dataclass` types, `CliApp.run` will internally use the following `BaseSettings` configuration defaults:
  * `nested_model_default_partial_update=True`
  * `case_sensitive=True`
  * `cli_hide_none_type=True`
  * `cli_avoid_json=True`
  * `cli_enforce_required=True`
  * `cli_implicit_flags=True`
  * `cli_kebab_case=True`


### Asynchronous CLI Commands[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#asynchronous-cli-commands)
Pydantic settings supports running asynchronous CLI commands via `CliApp.run` and `CliApp.run_subcommand`. With this feature, you can define async def methods within your Pydantic models (including subcommands) and have them executed just like their synchronous counterparts. Specifically:
  1. Asynchronous methods are supported: You can now mark your cli_cmd or similar CLI entrypoint methods as async def and have CliApp execute them.
  2. Subcommands may also be asynchronous: If you have nested CLI subcommands, the final (lowest-level) subcommand methods can likewise be asynchronous.
  3. Limit asynchronous methods to final subcommands: Defining parent commands as asynchronous is not recommended, because it can result in additional threads and event loops being created. For best performance and to avoid unnecessary resource usage, only implement your deepest (child) subcommands as async def.


Below is a simple example demonstrating an asynchronous top-level command:
```
from pydantic_settings import BaseSettings, CliApp


class AsyncSettings(BaseSettings):
    async def cli_cmd(self) -> None:
        print('Hello from an async CLI method!')
        #> Hello from an async CLI method!
