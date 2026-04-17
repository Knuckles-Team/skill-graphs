## Fetching attributes statically[¶](https://docs.python.org/3/library/inspect.html#fetching-attributes-statically "Link to this heading")
Both [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") and [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") can trigger code execution when fetching or checking for the existence of attributes. Descriptors, like properties, will be invoked and [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") and [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") may be called.
For cases where you want passive introspection, like documentation tools, this can be inconvenient. [`getattr_static()`](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "inspect.getattr_static") has the same signature as [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") but avoids executing code when it fetches attributes.

inspect.getattr_static(_obj_ , _attr_ , _default =None_)[¶](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "Link to this definition")

Retrieve attributes without triggering dynamic lookup via the descriptor protocol, [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") or [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__").
Note: this function may not be able to retrieve all attributes that getattr can fetch (like dynamically created attributes) and may find attributes that getattr can’t (like descriptors that raise AttributeError). It can also return descriptors objects instead of instance members.
If the instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") is shadowed by another member (for example a property) then this function will be unable to find instance members.
Added in version 3.2.
[`getattr_static()`](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "inspect.getattr_static") does not resolve descriptors, for example slot descriptors or getset descriptors on objects implemented in C. The descriptor object is returned instead of the underlying attribute.
You can handle these with code like the following. Note that for arbitrary getset descriptors invoking these may trigger code execution:
Copy```
