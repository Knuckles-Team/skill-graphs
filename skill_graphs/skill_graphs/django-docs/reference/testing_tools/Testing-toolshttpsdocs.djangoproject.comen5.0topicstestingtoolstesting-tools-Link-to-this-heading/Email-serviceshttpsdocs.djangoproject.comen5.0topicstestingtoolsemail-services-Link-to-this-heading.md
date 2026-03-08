## Email services[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#email-services "Link to this heading")
If any of your Django views send email using [Django’s email functionality](https://docs.djangoproject.com/en/5.0/topics/email/), you probably don’t want to send email each time you run a test using that view. For this reason, Django’s test runner automatically redirects all Django-sent email to a dummy outbox. This lets you test every aspect of sending email – from the number of messages sent to the contents of each message – without actually sending the messages.
The test runner accomplishes this by transparently replacing the normal email backend with a testing backend. (Don’t worry – this has no effect on any other email senders outside of Django, such as your machine’s mail server, if you’re running one.)

django.core.mail.outbox[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.core.mail.django.core.mail.outbox "Link to this definition")

During test running, each outgoing email is saved in `django.core.mail.outbox`. This is a list of all [`EmailMessage`](https://docs.djangoproject.com/en/5.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") instances that have been sent. The `outbox` attribute is a special attribute that is created _only_ when the `locmem` email backend is used. It doesn’t normally exist as part of the [`django.core.mail`](https://docs.djangoproject.com/en/5.0/topics/email/#module-django.core.mail "django.core.mail: Helpers to easily send email.") module and you can’t import it directly. The code below shows how to access this attribute correctly.
Here’s an example test that examines `django.core.mail.outbox` for length and contents:
```
from django.core import mail
from django.test import TestCase


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, "Subject here")

```

As noted [previously](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#emptying-test-outbox), the test outbox is emptied at the start of every test in a Django `*TestCase`. To empty the outbox manually, assign the empty list to `mail.outbox`:
```
from django.core import mail

# Empty the test outbox
mail.outbox = []

```
