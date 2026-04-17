## Attribute copies[¶](https://docs.pydantic.dev/latest/concepts/models/#attribute-copies)
In many cases, arguments passed to the constructor will be copied in order to perform validation and, where necessary, coercion.
In this example, note that the ID of the list changes after the class is constructed because it has been copied during validation:
```
from pydantic import BaseModel


class C1:
    arr = []

    def __init__(self, in_arr):
        self.arr = in_arr


class C2(BaseModel):
    arr: list[int]


arr_orig = [1, 9, 10, 3]


c1 = C1(arr_orig)
c2 = C2(arr=arr_orig)
print(f'{id(c1.arr) == id(c2.arr)=}')
#> id(c1.arr) == id(c2.arr)=False

```

Note
There are some situations where Pydantic does not copy attributes, such as when passing models — we use the model as is. You can override this behaviour by setting [`model_config['revalidate_instances'] = 'always'`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict).
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
