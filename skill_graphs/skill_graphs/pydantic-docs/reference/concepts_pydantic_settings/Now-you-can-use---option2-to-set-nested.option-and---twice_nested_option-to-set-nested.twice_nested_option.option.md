# Now you can use --option2 to set nested.option and --twice_nested_option to set nested.twice_nested_option.option

```

If a shortcut collides (is mapped to multiple fields), it will apply to the first matching field in the model.
### Integrating with Existing Parsers[¶](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#integrating-with-existing-parsers)
A CLI settings source can be integrated with existing parsers by overriding the default CLI settings source with a user defined one that specifies the `root_parser` object.
```
import sys
from argparse import ArgumentParser

from pydantic_settings import BaseSettings, CliApp, CliSettingsSource

parser = ArgumentParser()
parser.add_argument('--food', choices=['pear', 'kiwi', 'lime'])


class Settings(BaseSettings):
    name: str = 'Bob'
