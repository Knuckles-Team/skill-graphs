# just need to load the pre-parsed args into the settings source.
parsed_args = parser.parse_args(['--food', 'kiwi', '--name', 'ralph'])
s = CliApp.run(Settings, cli_args=parsed_args, cli_settings_source=cli_settings)
print(s.model_dump())
#> {'name': 'ralph'}

```

A `CliSettingsSource` connects with a `root_parser` object by using parser methods to add `settings_cls` fields as command line arguments. The `CliSettingsSource` internal parser representation is based on the `argparse` library, and therefore, requires parser methods that support the same attributes as their `argparse` counterparts. The available parser methods that can be customised, along with their argparse counterparts (the defaults), are listed below:
  * `parse_args_method` - (`argparse.ArgumentParser.parse_args`)
  * `add_argument_method` - (`argparse.ArgumentParser.add_argument`)
  * `add_argument_group_method` - (`argparse.ArgumentParser.add_argument_group`)
  * `add_parser_method` - (`argparse._SubParsersAction.add_parser`)
  * `add_subparsers_method` - (`argparse.ArgumentParser.add_subparsers`)
  * `formatter_class` - (`argparse.RawDescriptionHelpFormatter`)


For a non-argparse parser the parser methods can be set to `None` if not supported. The CLI settings will only raise an error when connecting to the root parser if a parser method is necessary but set to `None`.
Note
The `formatter_class` is only applied to subcommands. The `CliSettingsSource` never touches or modifies any of the external parser settings to avoid breaking changes. Since subcommands reside on their own internal parser trees, we can safely apply the `formatter_class` settings without breaking the external parser logic.
## Secrets[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets)
Placing secret values in files is a common pattern to provide sensitive configuration to an application.
A secret file follows the same principal as a dotenv file except it only contains a single value and the file name is used as the key. A secret file will look like the following:
/var/run/database_password```
super_secret_database_password

```

Once you have your secret files, _pydantic_ supports loading it in two ways:
  1. Setting the `secrets_dir` on `model_config` in a `BaseSettings` class to the directory where your secret files are stored.
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(secrets_dir='/var/run')

    database_password: str

```

  2. Instantiating the `BaseSettings` derived class with the `_secrets_dir` keyword argument:
```
settings = Settings(_secrets_dir='/var/run')

```



In either case, the value of the passed argument can be any valid directory, either absolute or relative to the current working directory. **Note that a non existent directory will only generate a warning**. From there, _pydantic_ will handle everything for you by loading in your variables and validating them.
Even when using a secrets directory, _pydantic_ will still read environment variables from a dotenv file or the environment, **a dotenv file and environment variables will always take priority over values loaded from the secrets directory**.
Passing a file path via the `_secrets_dir` keyword argument on instantiation (method 2) will override the value (if any) set on the `model_config` class.
If you need to load settings from multiple secrets directories, you can pass multiple paths as a tuple or list. Just like for `env_file`, values from subsequent paths override previous ones.
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # files in '/run/secrets' take priority over '/var/run'
    model_config = SettingsConfigDict(secrets_dir=('/var/run', '/run/secrets'))

    database_password: str

```

If any of `secrets_dir` is missing, it is ignored, and warning is shown. If any of `secrets_dir` is a file, error is raised.
### Use Case: Docker Secrets[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#use-case-docker-secrets)
Docker Secrets can be used to provide sensitive configuration to an application running in a Docker container. To use these secrets in a _pydantic_ application the process is simple. More information regarding creating, managing and using secrets in Docker see the official
First, define your `Settings` class with a `SettingsConfigDict` that specifies the secrets directory.
```
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(secrets_dir='/run/secrets')

    my_secret_data: str

```

Note
By default `Config.secrets_dir` accordingly.
Then, create your secret via the Docker CLI
```
printf "This is a secret" | docker secret create my_secret_data -

```

Last, run your application inside a Docker container and supply your newly created secret
```
docker service create --name pydantic-with-secrets --secret my_secret_data pydantic-app:latest

```

## Nested Secrets[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#nested-secrets)
The default secrets implementation, `SecretsSettingsSource`, has behaviour that is not always desired or sufficient. For example, the default implementation does not support secret fields in nested submodels.
`NestedSecretsSettingsSource` can be used as a drop-in replacement to `SecretsSettingsSource` to adjust the default behaviour. All differences are summarized in the table below.
`SecretsSettingsSource` | `NestedSecretsSettingsSourcee`
---|---
Secret fields must belong to a top level model. | Secrets can be fields of nested models.
Secret files can be placed in `secrets_dir`s only. | Secret files can be placed in subdirectories for nested models.
Secret files discovery is based on the same configuration options that are used by `EnvSettingsSource`: `case_sensitive`, `env_nested_delimiter`, `env_prefix`. | Default options are respected, but can be overridden with `secrets_case_sensitive`, `secrets_nested_delimiter`, `secrets_prefix`.
When `secrets_dir` is missing on the file system, a warning is generated. | Use `secrets_dir_missing` options to choose whether to issue warning, raise error, or silently ignore.
### Use Case: Plain Directory Layout[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#use-case-plain-directory-layout)
```
📂 secrets
├── 📄 app_key
└── 📄 db_passwd

```

In the example below, secrets nested delimiter `'_'` is different from env nested delimiter `'__'`. Value for `Settings.db.user` can be passed in env variable `MY_DB__USER`.
```
from pydantic import BaseModel, SecretStr

from pydantic_settings import (
    BaseSettings,
    NestedSecretsSettingsSource,
    SettingsConfigDict,
)


class AppSettings(BaseModel):
    key: SecretStr


class DbSettings(BaseModel):
    user: str
    passwd: SecretStr


class Settings(BaseSettings):
    app: AppSettings
    db: DbSettings

    model_config = SettingsConfigDict(
        env_prefix='MY_',
        env_nested_delimiter='__',
        secrets_dir='secrets',
        secrets_nested_delimiter='_',
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            NestedSecretsSettingsSource(file_secret_settings),
        )

```

### Use Case: Nested Directory Layout[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#use-case-nested-directory-layout)
```
📂 secrets
├── 📂 app
│   └── 📄 key
└── 📂 db
    └── 📄 passwd

```

```
from pydantic import BaseModel, SecretStr

from pydantic_settings import (
    BaseSettings,
    NestedSecretsSettingsSource,
    SettingsConfigDict,
)


class AppSettings(BaseModel):
    key: SecretStr


class DbSettings(BaseModel):
    user: str
    passwd: SecretStr


class Settings(BaseSettings):
    app: AppSettings
    db: DbSettings

    model_config = SettingsConfigDict(
        env_prefix='MY_',
        env_nested_delimiter='__',
        secrets_dir='secrets',
        secrets_nested_subdir=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            NestedSecretsSettingsSource(file_secret_settings),
        )

```

### Use Case: Multiple Nested Directories[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#use-case-multiple-nested-directories)
```
📂 secrets
├── 📂 default
│   ├── 📂 app
│   │   └── 📄 key
│   └── 📂 db
│       └── 📄 passwd
└── 📂 override
    ├── 📂 app
    │   └── 📄 key
    └── 📂 db
        └── 📄 passwd

```

```
from pydantic import BaseModel, SecretStr

from pydantic_settings import (
    BaseSettings,
    NestedSecretsSettingsSource,
    SettingsConfigDict,
)


class AppSettings(BaseModel):
    key: SecretStr


class DbSettings(BaseModel):
    user: str
    passwd: SecretStr


class Settings(BaseSettings):
    app: AppSettings
    db: DbSettings

    model_config = SettingsConfigDict(
        env_prefix='MY_',
        env_nested_delimiter='__',
        secrets_dir=['secrets/default', 'secrets/override'],
        secrets_nested_subdir=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            NestedSecretsSettingsSource(file_secret_settings),
        )

```

### Configuration Options[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#configuration-options)
#### secrets_dir[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_dir)
Path to secrets directory, same as `SecretsSettingsSource.secrets_dir`. If `list`, the last match wins. If `secrets_dir` is passed in both source constructor and model config, values are not merged (constructor wins).
#### secrets_dir_missing[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_dir_missing)
If `secrets_dir` does not exist, original `SecretsSettingsSource` issues a warning. However, this may be undesirable, for example if we don't mount Docker Secrets in e.g. dev environment. Use `secrets_dir_missing` to choose:
  * `'ok'` — do nothing if `secrets_dir` does not exist
  * `'warn'` (default) — print warning, same as `SecretsSettingsSource`
  * `'error'` — raise `SettingsError`


If multiple `secrets_dir` passed, the same `secrets_dir_missing` action applies to each of them.
#### secrets_dir_max_size[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_dir_max_size)
Limit the size of `secrets_dir` for security reasons, defaults to `SECRETS_DIR_MAX_SIZE` equal to 16 MiB.
`NestedSecretsSettingsSource` is a thin wrapper around `EnvSettingsSource`, which loads all potential secrets on initialization. This could lead to `MemoryError` if we mount a large file under `secrets_dir`.
If multiple `secrets_dir` passed, the limit applies to each directory independently.
#### secrets_case_sensitive[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_case_sensitive)
Same as `case_sensitive`, but works for secrets only. If not specified, defaults to `case_sensitive`.
#### secrets_nested_delimiter[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_nested_delimiter)
Same as `env_nested_delimiter`, but works for secrets only. If not specified, defaults to `env_nested_delimiter`. This option is used to implement _nested secrets directory_ layout and allows to do even nasty things like `/run/secrets/model/delim/nested1/delim/nested2`.
#### secrets_nested_subdir[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_nested_subdir)
Boolean flag to turn on _nested secrets directory_ mode, `False` by default. If `True`, sets `secrets_nested_delimiter` to `os.sep`. Raises `SettingsError` if `secrets_nested_delimiter` is already specified.
#### secrets_prefix[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets_prefix)
Secret path prefix, similar to `env_prefix`, but works for secrets only. Defaults to `env_prefix` if not specified. Works in both plain and nested directory modes, like `'/run/secrets/prefix_model__nested'` and `'/run/secrets/prefix_model/nested'`.
## AWS Secrets Manager[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#aws-secrets-manager)
You must set one parameter:
  * `secret_id`: The AWS secret id


You must have the same naming convention in the key value in secret as in the field name. For example, if the key in secret is named `SqlServerPassword`, the field name must be the same. You can use an alias too.
In AWS Secrets Manager, nested models are supported with the `--` separator in the key name. For example, `SqlServer--Password`.
Arrays (e.g. `MySecret--0`, `MySecret--1`) are not supported.
```
import os

from pydantic import BaseModel

from pydantic_settings import (
    AWSSecretsManagerSettingsSource,
    BaseSettings,
    PydanticBaseSettingsSource,
)


class SubModel(BaseModel):
    a: str


class AWSSecretsManagerSettings(BaseSettings):
    foo: str
    bar: int
    sub: SubModel

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        aws_secrets_manager_settings = AWSSecretsManagerSettingsSource(
            settings_cls,
            os.environ['AWS_SECRETS_MANAGER_SECRET_ID'],
        )
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            aws_secrets_manager_settings,
        )

```

## Azure Key Vault[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#azure-key-vault)
You must set two parameters:
  * `url`: For example, `https://my-resource.vault.azure.net/`.
  * `credential`: If you use `DefaultAzureCredential`, in local you can execute `az login` to get your identity credentials. The identity must have a role assignment (the recommended one is `Key Vault Secrets User`), so you can access the secrets.


You must have the same naming convention in the field name as in the Key Vault secret name. For example, if the secret is named `SqlServerPassword`, the field name must be the same. You can use an alias too.
In Key Vault, nested models are supported with the `--` separator. For example, `SqlServer--Password`.
Key Vault arrays (e.g. `MySecret--0`, `MySecret--1`) are not supported.
```
import os

from azure.identity import DefaultAzureCredential
from pydantic import BaseModel

from pydantic_settings import (
    AzureKeyVaultSettingsSource,
    BaseSettings,
    PydanticBaseSettingsSource,
)


class SubModel(BaseModel):
    a: str


class AzureKeyVaultSettings(BaseSettings):
    foo: str
    bar: int
    sub: SubModel

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        az_key_vault_settings = AzureKeyVaultSettingsSource(
            settings_cls,
            os.environ['AZURE_KEY_VAULT_URL'],
            DefaultAzureCredential(),
        )
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            az_key_vault_settings,
        )

```

### Snake case conversion[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#snake-case-conversion)
The Azure Key Vault source accepts a `snake_case_convertion` option, disabled by default, to convert Key Vault secret names by mapping them to Python's snake_case field names, without the need to use aliases.
```
import os

from azure.identity import DefaultAzureCredential

from pydantic_settings import (
    AzureKeyVaultSettingsSource,
    BaseSettings,
    PydanticBaseSettingsSource,
)


class AzureKeyVaultSettings(BaseSettings):
    my_setting: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        az_key_vault_settings = AzureKeyVaultSettingsSource(
            settings_cls,
            os.environ['AZURE_KEY_VAULT_URL'],
            DefaultAzureCredential(),
            snake_case_conversion=True,
        )
        return (az_key_vault_settings,)

```

This setup will load Azure Key Vault secrets (e.g., `MySetting`, `mySetting`, `my-secret` or `MY-SECRET`), mapping them to the snake case version (`my_setting` in this case).
### Dash to underscore mapping[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dash-to-underscore-mapping)
The Azure Key Vault source accepts a `dash_to_underscore` option, disabled by default, to support Key Vault kebab-case secret names by mapping them to Python's snake_case field names. When enabled, dashes (`-`) in secret names are mapped to underscores (`_`) in field names during validation.
This mapping applies only to _field names_ , not to aliases.
```
import os

from azure.identity import DefaultAzureCredential
from pydantic import Field

from pydantic_settings import (
    AzureKeyVaultSettingsSource,
    BaseSettings,
    PydanticBaseSettingsSource,
)


class AzureKeyVaultSettings(BaseSettings):
    field_with_underscore: str
    field_with_alias: str = Field(..., alias='Alias-With-Dashes')

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        az_key_vault_settings = AzureKeyVaultSettingsSource(
            settings_cls,
            os.environ['AZURE_KEY_VAULT_URL'],
            DefaultAzureCredential(),
            dash_to_underscore=True,
        )
        return (az_key_vault_settings,)

```

This setup will load Azure Key Vault secrets named `field-with-underscore` and `Alias-With-Dashes`, mapping them to the `field_with_underscore` and `field_with_alias` fields, respectively.
Tip
Alternatively, you can configure an [alias_generator](https://docs.pydantic.dev/latest/concepts/alias/#using-alias-generators) to map PascalCase secrets.
## Google Cloud Secret Manager[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#google-cloud-secret-manager)
Google Cloud Secret Manager allows you to store, manage, and access sensitive information as secrets in Google Cloud Platform. This integration lets you retrieve secrets directly from GCP Secret Manager for use in your Pydantic settings.
### Installation[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#installation_1)
The Google Cloud Secret Manager integration requires additional dependencies:
```
pip install "pydantic-settings[gcp-secret-manager]"

```

### Basic Usage[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#basic-usage)
To use Google Cloud Secret Manager, you need to:
  1. Create a `GoogleSecretManagerSettingsSource`. (See [GCP Authentication](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#gcp-authentication) for authentication options.)
  2. Add this source to your settings customization pipeline


```
from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    GoogleSecretManagerSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class Database(BaseModel):
    password: str
    user: str


class Settings(BaseSettings):
    database: Database

    model_config = SettingsConfigDict(env_nested_delimiter='__')

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        # Create the GCP Secret Manager settings source
        gcp_settings = GoogleSecretManagerSettingsSource(
            settings_cls,
            # If not provided, will use google.auth.default()
            # to get credentials from the environment
            # credentials=your_credentials,
            # If not provided, will use google.auth.default()
            # to get project_id from the environment
            project_id='your-gcp-project-id',
        )

        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            gcp_settings,
        )

```

### GCP Authentication[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#gcp-authentication)
The `GoogleSecretManagerSettingsSource` supports several authentication methods:
  1. **Default credentials** - If you don't provide credentials or project ID, it will use
  2. Service account credentials from `GOOGLE_APPLICATION_CREDENTIALS` environment variable
  3. User credentials from `gcloud auth application-default login`
  4. Compute Engine, GKE, Cloud Run, or Cloud Functions default service accounts
  5. **Explicit credentials** - You can also provide `credentials` directly. e.g. `sa_credentials = google.oauth2.service_account.Credentials.from_service_account_file('path/to/service-account.json')` and then `GoogleSecretManagerSettingsSource(credentials=sa_credentials)`


### Nested Models[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#nested-models)
For nested models, Secret Manager supports the `env_nested_delimiter` setting as long as it complies with the `database__password` and `database__user` in Secret Manager.
### Important Notes[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#important-notes)
  1. **Case Sensitivity** : By default, secret names are case-sensitive.
  2. **Secret Naming** : Create secrets in Google Secret Manager with names that match your field names (including any prefix). According the
  3. **Secret Versions** : The GoogleSecretManagerSettingsSource uses the "latest" version of secrets.


For more details on creating and managing secrets in Google Cloud Secret Manager, see the
## Other settings source[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#other-settings-source)
Other settings sources are available for common configuration files:
  * `JsonConfigSettingsSource` using `json_file` and `json_file_encoding` arguments
  * `PyprojectTomlConfigSettingsSource` using _(optional)_ `pyproject_toml_depth` and _(optional)_ `pyproject_toml_table_header` arguments
  * `TomlConfigSettingsSource` using `toml_file` argument
  * `YamlConfigSettingsSource` using `yaml_file` and yaml_file_encoding arguments


To use them, you can use the same mechanism described [here](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customise-settings-sources).
```
from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class Nested(BaseModel):
    nested_field: str


class Settings(BaseSettings):
    foobar: str
    nested: Nested
    model_config = SettingsConfigDict(toml_file='config.toml')

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)

```

This will be able to read the following "config.toml" file, located in your working directory:
```
foobar = "Hello"
[nested]
nested_field = "world!"

```

You can also provide multiple files by providing a list of paths.
```
from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class Nested(BaseModel):
    foo: int
    bar: int = 0


class Settings(BaseSettings):
    hello: str
    nested: Nested
    model_config = SettingsConfigDict(
        toml_file=['config.default.toml', 'config.custom.toml']
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)

```

The following two configuration files
```
# config.default.toml
hello = "World"

[nested]
foo = 1
bar = 2

```

```
# config.custom.toml
[nested]
foo = 3

```

are equivalent to
```
hello = "world"

[nested]
foo = 3

```

The files are merged shallowly in increasing order of priority. To enable deep merging, set `deep_merge=True` on the source directly.
Warning
The `deep_merge` option is **not available** through the `SettingsConfigDict`.
```
from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class Nested(BaseModel):
    foo: int
    bar: int = 0


class Settings(BaseSettings):
    hello: str
    nested: Nested
    model_config = SettingsConfigDict(
        toml_file=['config.default.toml', 'config.custom.toml']
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls, deep_merge=True),)

```

With deep merge enabled, the following two configuration files
```
# config.default.toml
hello = "World"

[nested]
foo = 1
bar = 2

```

```
# config.custom.toml
[nested]
foo = 3

```

are equivalent to
```
hello = "world"

[nested]
foo = 3
bar = 2

```

### pyproject.toml[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#pyprojecttoml)
"pyproject.toml" is a standardized file for providing configuration values in Python projects. `[tool]` table that can be used to provide arbitrary tool configuration. While encouraged to use the `[tool]` table, `PyprojectTomlConfigSettingsSource` can be used to load variables from any location with in "pyproject.toml" file.
This is controlled by providing `SettingsConfigDict(pyproject_toml_table_header=tuple[str, ...])` where the value is a tuple of header parts. By default, `pyproject_toml_table_header=('tool', 'pydantic-settings')` which will load variables from the `[tool.pydantic-settings]` table.
```
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """Example loading values from the table used by default."""

    field: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (PyprojectTomlConfigSettingsSource(settings_cls),)


class SomeTableSettings(Settings):
    """Example loading values from a user defined table."""

    model_config = SettingsConfigDict(
        pyproject_toml_table_header=('tool', 'some-table')
    )


class RootSettings(Settings):
    """Example loading values from the root of a pyproject.toml file."""

    model_config = SettingsConfigDict(extra='ignore', pyproject_toml_table_header=())

```

This will be able to read the following "pyproject.toml" file, located in your working directory, resulting in `Settings(field='default-table')`, `SomeTableSettings(field='some-table')`, & `RootSettings(field='root')`:
```
field = "root"

[tool.pydantic-settings]
field = "default-table"

[tool.some-table]
field = "some-table"

```

By default, `PyprojectTomlConfigSettingsSource` will only look for a "pyproject.toml" in the your current working directory. However, there are two options to change this behavior.
  * `SettingsConfigDict(pyproject_toml_depth=<int>)` can be provided to check `<int>` number of directories **up** in the directory tree for a "pyproject.toml" if one is not found in the current working directory. By default, no parent directories are checked.
  * An explicit file path can be provided to the source when it is instantiated (e.g. `PyprojectTomlConfigSettingsSource(settings_cls, Path('~/.config').resolve() / 'pyproject.toml')`). If a file path is provided this way, it will be treated as absolute (no other locations are checked).


```
from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
)


class DiscoverSettings(BaseSettings):
    """Example of discovering a pyproject.toml in parent directories in not in `Path.cwd()`."""

    model_config = SettingsConfigDict(pyproject_toml_depth=2)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (PyprojectTomlConfigSettingsSource(settings_cls),)


class ExplicitFilePathSettings(BaseSettings):
    """Example of explicitly providing the path to the file to load."""

    field: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            PyprojectTomlConfigSettingsSource(
                settings_cls, Path('~/.config').resolve() / 'pyproject.toml'
            ),
        )

```

## Field value priority[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#field-value-priority)
In the case where a value is specified for the same `Settings` field in multiple ways, the selected value is determined as follows (in descending order of priority):
  1. If `cli_parse_args` is enabled, arguments passed in at the CLI.
  2. Arguments passed to the `Settings` class initialiser.
  3. Environment variables, e.g. `my_prefix_special_function` as described above.
  4. Variables loaded from a dotenv (`.env`) file.
  5. Variables loaded from the secrets directory.
  6. The default field values for the `Settings` model.


## Customise settings sources[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customise-settings-sources)
If the default order of priority doesn't match your needs, it's possible to change it by overriding the `settings_customise_sources` method of your `Settings` .
`settings_customise_sources` takes four callables as arguments and returns any number of callables as a tuple. In turn these callables are called to build the inputs to the fields of the settings class.
Each callable should take an instance of the settings class as its sole argument and return a `dict`.
### Changing Priority[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#changing-priority)
The order of the returned callables decides the priority of inputs; first item is the highest priority.
```
from pydantic import PostgresDsn

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


class Settings(BaseSettings):
    database_dsn: PostgresDsn

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, init_settings, file_secret_settings


print(Settings(database_dsn='postgres://postgres@localhost:5432/kwargs_db'))
#> database_dsn=PostgresDsn('postgres://postgres@localhost:5432/kwargs_db')

```

By flipping `env_settings` and `init_settings`, environment variables now have precedence over `__init__` kwargs.
### Adding sources[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#adding-sources)
As explained earlier, _pydantic_ ships with multiples built-in settings sources. However, you may occasionally need to add your own custom sources, `settings_customise_sources` makes this very easy:
```
import json
from pathlib import Path
from typing import Any

from pydantic.fields import FieldInfo

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class JsonConfigSettingsSource(PydanticBaseSettingsSource):
    """
    A simple settings source class that loads variables from a JSON file
    at the project's root.

    Here we happen to choose to use the `env_file_encoding` from Config
    when reading `config.json`
    """

    def get_field_value(
        self, field: FieldInfo, field_name: str
    ) -> tuple[Any, str, bool]:
        encoding = self.config.get('env_file_encoding')
        file_content_json = json.loads(
            Path('tests/example_test_config.json').read_text(encoding)
        )
        field_value = file_content_json.get(field_name)
        return field_value, field_name, False

    def prepare_field_value(
        self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
    ) -> Any:
        return value

    def __call__(self) -> dict[str, Any]:
        d: dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(
                field, field_name
            )
            field_value = self.prepare_field_value(
                field_name, field, field_value, value_is_complex
            )
            if field_value is not None:
                d[field_key] = field_value

        return d


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding='utf-8')

    foobar: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            JsonConfigSettingsSource(settings_cls),
            env_settings,
            file_secret_settings,
        )


print(Settings())
#> foobar='test'

```

#### Accessing the result of previous sources[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#accessing-the-result-of-previous-sources)
Each source of settings can access the output of the previous ones.
```
from typing import Any

from pydantic.fields import FieldInfo

from pydantic_settings import PydanticBaseSettingsSource


class MyCustomSource(PydanticBaseSettingsSource):
    def get_field_value(
        self, field: FieldInfo, field_name: str
    ) -> tuple[Any, str, bool]: ...

    def __call__(self) -> dict[str, Any]:
        # Retrieve the aggregated settings from previous sources
        current_state = self.current_state
        current_state.get('some_setting')

        # Retrieve settings from all sources individually
        # self.settings_sources_data["SettingsSourceName"]: dict[str, Any]
        settings_sources_data = self.settings_sources_data
        settings_sources_data['SomeSettingsSource'].get('some_setting')

        # Your code here...

```

### Removing sources[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#removing-sources)
You might also want to disable a source:
```
from pydantic import ValidationError

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


class Settings(BaseSettings):
    my_api_key: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        # here we choose to ignore arguments from init_settings
        return env_settings, file_secret_settings


try:
    Settings(my_api_key='this is ignored')
except ValidationError as exc_info:
    print(exc_info)
    """
    1 validation error for Settings
    my_api_key
      Field required [type=missing, input_value={}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2/v/missing
    """

```

## In-place reloading[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#in-place-reloading)
In case you want to reload in-place an existing setting, you can do it by using its `__init__` method :
```
import os

from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    foo: str = Field('foo')


mutable_settings = Settings()

print(mutable_settings.foo)
#> foo

os.environ['foo'] = 'bar'
print(mutable_settings.foo)
#> foo

mutable_settings.__init__()
print(mutable_settings.foo)
#> bar

os.environ.pop('foo')
mutable_settings.__init__()
print(mutable_settings.foo)
#> foo

```

Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
