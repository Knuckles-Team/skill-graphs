## Examples[¶](https://docs.python.org/3/library/importlib.html#examples "Link to this heading")
### Importing programmatically[¶](https://docs.python.org/3/library/importlib.html#importing-programmatically "Link to this heading")
To programmatically import a module, use [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module").
Copy```
import importlib

itertools = importlib.import_module('itertools')

```

### Checking if a module can be imported[¶](https://docs.python.org/3/library/importlib.html#checking-if-a-module-can-be-imported "Link to this heading")
If you need to find out if a module can be imported without actually doing the import, then you should use [`importlib.util.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "importlib.util.find_spec").
Note that if `name` is a submodule (contains a dot), [`importlib.util.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "importlib.util.find_spec") will import the parent module.
Copy```
import importlib.util
import sys

# For illustrative purposes.
name = 'itertools'

if name in sys.modules:
    print(f"{name!r} already in sys.modules")
elif (spec := importlib.util.find_spec(name)) is not None:
    # If you chose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    print(f"{name!r} has been imported")
else:
    print(f"can't find the {name!r} module")

```

### Importing a source file directly[¶](https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly "Link to this heading")
This recipe should be used with caution: it is an approximation of an import statement where the file path is specified directly, rather than [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") being searched. Alternatives should first be considered first, such as modifying `sys.path` when a proper module is required, or using [`runpy.run_path()`](https://docs.python.org/3/library/runpy.html#runpy.run_path "runpy.run_path") when the global namespace resulting from running a Python file is appropriate.
To import a Python source file directly from a path, use the following recipe:
Copy```
import importlib.util
import sys


def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
