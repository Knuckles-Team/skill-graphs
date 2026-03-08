## Management Commands[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#management-commands "Link to this heading")
Management commands can be tested with the [`call_command()`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django.core.management.call_command "django.core.management.call_command") function. The output can be redirected into a `StringIO` instance:
```
from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command("closepoll", poll_ids=[1], stdout=out)
        self.assertIn('Successfully closed poll "1"', out.getvalue())

```
