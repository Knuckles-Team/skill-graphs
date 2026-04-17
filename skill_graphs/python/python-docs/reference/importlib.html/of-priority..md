# of priority.
sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))

```

### Approximating [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module")[¶](https://docs.python.org/3/library/importlib.html#approximating-importlib-import-module "Link to this heading")
Import itself is implemented in Python code, making it possible to expose most of the import machinery through importlib. The following helps illustrate the various APIs that importlib exposes by providing an approximate implementation of [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module"):
Copy```
import importlib.util
import sys

def import_module(name, package=None):
    """An approximate implementation of import."""
    absolute_name = importlib.util.resolve_name(name, package)
    try:
        return sys.modules[absolute_name]
    except KeyError:
        pass

    path = None
    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.__spec__.submodule_search_locations
    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        msg = f'No module named {absolute_name!r}'
        raise ModuleNotFoundError(msg, name=absolute_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[absolute_name] = module
    spec.loader.exec_module(module)
    if path is not None:
        setattr(parent_module, child_name, module)
    return module

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
    * [Introduction](https://docs.python.org/3/library/importlib.html#introduction)
    * [Functions](https://docs.python.org/3/library/importlib.html#functions)
    * [`importlib.abc` – Abstract base classes related to import](https://docs.python.org/3/library/importlib.html#module-importlib.abc)
    * [`importlib.machinery` – Importers and path hooks](https://docs.python.org/3/library/importlib.html#module-importlib.machinery)
    * [`importlib.util` – Utility code for importers](https://docs.python.org/3/library/importlib.html#module-importlib.util)
    * [Examples](https://docs.python.org/3/library/importlib.html#examples)
      * [Importing programmatically](https://docs.python.org/3/library/importlib.html#importing-programmatically)
      * [Checking if a module can be imported](https://docs.python.org/3/library/importlib.html#checking-if-a-module-can-be-imported)
      * [Importing a source file directly](https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly)
      * [Implementing lazy imports](https://docs.python.org/3/library/importlib.html#implementing-lazy-imports)
      * [Setting up an importer](https://docs.python.org/3/library/importlib.html#setting-up-an-importer)
      * [Approximating `importlib.import_module()`](https://docs.python.org/3/library/importlib.html#approximating-importlib-import-module)


#### Previous topic
[`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html "previous chapter")
#### Next topic
[`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib+%E2%80%94+The+implementation+of+import&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.html&pagesource=library%2Fimportlib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.resources.html "importlib.resources – Package resource reading, opening and access") |
  * [previous](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
