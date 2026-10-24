# fails type checking; an int is not a UserId
user_b = get_user_name(-1)

```

You may still perform all `int` operations on a variable of type `UserId`, but the result will always be of type `int`. This lets you pass in a `UserId` wherever an `int` might be expected, but will prevent you from accidentally creating a `UserId` in an invalid way:
Copy```
# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)

```

Note that these checks are enforced only by the static type checker. At runtime, the statement `Derived = NewType('Derived', Base)` will make `Derived` a callable that immediately returns whatever parameter you pass it. That means the expression `Derived(some_value)` does not create a new class or introduce much overhead beyond that of a regular function call.
More precisely, the expression `some_value is Derived(some_value)` is always true at runtime.
It is invalid to create a subtype of `Derived`:
Copy```
from typing import NewType

UserId = NewType('UserId', int)
