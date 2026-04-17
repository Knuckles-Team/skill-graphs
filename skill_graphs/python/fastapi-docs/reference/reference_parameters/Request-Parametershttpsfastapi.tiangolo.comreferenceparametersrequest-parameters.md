# Request Parameters[¶](https://fastapi.tiangolo.com/reference/parameters/#request-parameters)
Here's the reference information for the request parameters.
These are the special functions that you can put in _path operation function_ parameters or dependency functions with `Annotated` to get data from the request.
It includes:
  * `Query()`
  * `Path()`
  * `Body()`
  * `Cookie()`
  * `Header()`
  * `Form()`
  * `File()`


You can import them all directly from `fastapi`:
```
from fastapi import Body, Cookie, File, Form, Header, Path, Query

```
