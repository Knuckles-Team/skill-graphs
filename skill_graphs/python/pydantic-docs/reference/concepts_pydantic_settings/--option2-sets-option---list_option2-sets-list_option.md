# --option2 sets 'option', --list_option2 sets 'list_option'

```

**Nested Example:**
```
from pydantic import BaseModel, Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class TwiceNested(BaseModel):
    option: str = Field(default='foo')


class Nested(BaseModel):
    twice_nested_option: TwiceNested = TwiceNested()
    option: str = Field(default='foo')


class Settings(BaseSettings):
    nested: Nested = Nested()
    model_config = SettingsConfigDict(
        cli_shortcuts={
            'nested.option': 'option2',
            'nested.twice_nested_option.option': 'twice_nested_option',
        }
    )
