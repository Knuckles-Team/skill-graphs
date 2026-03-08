## Organizing models in a package[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#organizing-models-in-a-package "Link to this heading")
The [`manage.py startapp`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startapp) command creates an application structure that includes a `models.py` file. If you have many models, organizing them in separate files may be useful.
To do so, create a `models` package. Remove `models.py` and create a `myapp/models/` directory with an `__init__.py` file and the files to store your models. You must import the models in the `__init__.py` file.
For example, if you had `organic.py` and `synthetic.py` in the `models` directory:
`myapp/models/__init__.py`[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#id11 "Link to this code")
```
from .organic import Person
from .synthetic import Robot

```

Explicitly importing each model rather than using `from .models import *` has the advantages of not cluttering the namespace, making code more readable, and keeping code analysis tools useful.
See also

[The Models Reference](https://docs.djangoproject.com/en/5.0/ref/models/)

Covers all the model related APIs including model fields, related objects, and `QuerySet`.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/db/)
[Making queries ](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
[](https://docs.djangoproject.com/en/5.0/topics/db/models/#top)
