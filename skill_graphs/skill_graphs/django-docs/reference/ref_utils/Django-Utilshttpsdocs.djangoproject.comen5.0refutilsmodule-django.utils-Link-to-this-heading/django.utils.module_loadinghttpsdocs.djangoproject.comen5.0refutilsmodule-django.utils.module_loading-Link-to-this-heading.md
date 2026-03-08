##  `django.utils.module_loading`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.module_loading "Link to this heading")
Functions for working with Python modules.

import_string(_dotted_path_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/module_loading/#import_string)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.module_loading.import_string "Link to this definition")

Imports a dotted module path and returns the attribute/class designated by the last name in the path. Raises `ImportError` if the import failed. For example:
```
from django.utils.module_loading import import_string

ValidationError = import_string("django.core.exceptions.ValidationError")

```

is equivalent to:
```
from django.core.exceptions import ValidationError

```
