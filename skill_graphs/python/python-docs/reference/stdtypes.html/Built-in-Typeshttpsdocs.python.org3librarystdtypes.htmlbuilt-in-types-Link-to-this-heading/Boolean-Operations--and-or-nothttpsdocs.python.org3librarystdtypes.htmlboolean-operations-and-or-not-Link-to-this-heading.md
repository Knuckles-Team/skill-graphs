## Boolean Operations — `and`, `or`, `not`[¶](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not "Link to this heading")
These are the Boolean operations, ordered by ascending priority:
Operation | Result | Notes
---|---|---
`x or y` | if _x_ is true, then _x_ , else _y_ | (1)
`x and y` | if _x_ is false, then _x_ , else _y_ | (2)
`not x` | if _x_ is false, then `True`, else `False` | (3)
Notes:
  1. This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
  2. This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
  3. `not` has a lower priority than non-Boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `a == not b` is a syntax error.
