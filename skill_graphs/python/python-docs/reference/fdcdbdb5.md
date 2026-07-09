# Similar outcome as `import json`.
json = import_from_path(module_name, file_path)

```

### Implementing lazy imports[¶](https://docs.python.org/3/library/importlib.html#implementing-lazy-imports "Link to this heading")
The example below shows how to implement lazy imports:
Copy```
>>> import importlib.util
>>> import sys
>>> def lazy_import(name):
...     spec = importlib.util.find_spec(name)
...     loader = importlib.util.LazyLoader(spec.loader)
...     spec.loader = loader
...     module = importlib.util.module_from_spec(spec)
...     sys.modules[name] = module
...     loader.exec_module(module)
...     return module
...
>>> lazy_typing = lazy_import("typing")
>>> #lazy_typing is a real module object,
>>> #but it is not loaded in memory yet.
>>> lazy_typing.TYPE_CHECKING
False

```

### Setting up an importer[¶](https://docs.python.org/3/library/importlib.html#setting-up-an-importer "Link to this heading")
For deep customizations of import, you typically want to implement an [importer](https://docs.python.org/3/glossary.html#term-importer). This means managing both the [finder](https://docs.python.org/3/glossary.html#term-finder) and [loader](https://docs.python.org/3/glossary.html#term-loader) side of things. For finders there are two flavours to choose from depending on your needs: a [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder) or a [path entry finder](https://docs.python.org/3/glossary.html#term-path-entry-finder). The former is what you would put on [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") while the latter is what you create using a [path entry hook](https://docs.python.org/3/glossary.html#term-path-entry-hook) on [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") which works with [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entries to potentially create a finder. This example will show you how to register your own importers so that import will use them (for creating an importer for yourself, read the documentation for the appropriate classes defined within this package):
Copy```
import importlib.machinery
import sys
