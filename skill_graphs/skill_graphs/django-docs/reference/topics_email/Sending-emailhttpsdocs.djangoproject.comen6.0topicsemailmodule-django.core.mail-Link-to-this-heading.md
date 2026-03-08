# Sending email[¶](https://docs.djangoproject.com/en/6.0/topics/email/#module-django.core.mail "Link to this heading")
Although Python provides a mail sending interface via the
The code lives in the `django.core.mail` module.
## Quick examples[¶](https://docs.djangoproject.com/en/6.0/topics/email/#quick-examples "Link to this heading")
Use [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") for straightforward email sending. For example, to send a plain text message:
```
from django.core.mail import send_mail

send_mail(
    "Subject here",
    "Here is the message.",
    "from@example.com",
    ["to@example.com"],
    fail_silently=False,
)

```

When additional email sending functionality is needed, use [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") or [`EmailMultiAlternatives`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives "django.core.mail.EmailMultiAlternatives"). For example, to send a multipart email that includes both HTML and plain text versions with a specific template and custom headers, you can use the following approach:
```
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# First, render the plain text content.
text_content = render_to_string(
    "templates/emails/my_email.txt",
    context={"my_variable": 42},
)

# Secondly, render the HTML content.
html_content = render_to_string(
    "templates/emails/my_email.html",
    context={"my_variable": 42},
)

# Then, create a multipart email instance.
msg = EmailMultiAlternatives(
    subject="Subject here",
    body=text_content,
    from_email="from@example.com",
    to=["to@example.com"],
    headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
)

# Lastly, attach the HTML content to the email instance and send.
msg.attach_alternative(html_content, "text/html")
msg.send()

```

Mail is sent using the SMTP host and port specified in the [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST) and [`EMAIL_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_PORT) settings. The [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_USER) and [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_PASSWORD) settings, if set, are used to authenticate to the SMTP server, and the [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS) and [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL) settings control whether a secure connection is used.
Note
The character set of email sent with `django.core.mail` will be set to the value of your [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting.
##  `send_mail()`[¶](https://docs.djangoproject.com/en/6.0/topics/email/#send-mail "Link to this heading")

send_mail(_subject_ , _message_ , _from_email_ , _recipient_list_ , _*_ , _fail_silently =False_, _auth_user =None_, _auth_password =None_, _connection =None_, _html_message =None_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "Link to this definition")

In most cases, you can send email using `django.core.mail.send_mail()`.
The `subject`, `message`, `from_email` and `recipient_list` parameters are required.
  * `subject`: A string.
  * `message`: A string.
  * `from_email`: A string. If `None`, Django will use the value of the [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_FROM_EMAIL) setting.
  * `recipient_list`: A list of strings, each an email address. Each member of `recipient_list` will see the other recipients in the “To:” field of the email message.


The following parameters are optional, and must be given as keyword arguments if used.
  * `fail_silently`: A boolean. When it’s `False`, `send_mail()` will raise an
  * `auth_user`: The optional username to use to authenticate to the SMTP server. If this isn’t provided, Django will use the value of the [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_USER) setting.
  * `auth_password`: The optional password to use to authenticate to the SMTP server. If this isn’t provided, Django will use the value of the [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_PASSWORD) setting.
  * `connection`: The optional email backend to use to send the mail. If unspecified, an instance of the default backend will be used. See the documentation on [Email backends](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-backends) for more details.
  * `html_message`: If `html_message` is provided, the resulting email will be a _multipart/alternative_ email with `message` as the _text/plain_ content type and `html_message` as the _text/html_ content type.


The return value will be the number of successfully delivered messages (which can be `0` or `1` since it can only send one message).
Deprecated since version 6.0: Passing `fail_silently` and later parameters as positional arguments is deprecated.
##  `send_mass_mail()`[¶](https://docs.djangoproject.com/en/6.0/topics/email/#send-mass-mail "Link to this heading")

send_mass_mail(_datatuple_ , _*_ , _fail_silently =False_, _auth_user =None_, _auth_password =None_, _connection =None_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mass_mail "Link to this definition")

`django.core.mail.send_mass_mail()` is intended to handle mass emailing.
`datatuple` is a tuple in which each element is in this format:
```
(subject, message, from_email, recipient_list)

```

`fail_silently`, `auth_user`, `auth_password` and `connection` have the same functions as in [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail"). They must be given as keyword arguments if used.
Each separate element of `datatuple` results in a separate email message. As in [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail"), recipients in the same `recipient_list` will all see the other addresses in the email messages’ “To:” field.
For example, the following code would send two different messages to two different sets of recipients; however, only one connection to the mail server would be opened:
```
message1 = (
    "Subject here",
    "Here is the message",
    "from@example.com",
    ["first@example.com", "other@example.com"],
)
message2 = (
    "Another Subject",
    "Here is another message",
    "from@example.com",
    ["second@test.com"],
)
send_mass_mail((message1, message2), fail_silently=False)

```

The return value will be the number of successfully delivered messages.
Deprecated since version 6.0: Passing `fail_silently` and later parameters as positional arguments is deprecated.
###  `send_mass_mail()` vs. `send_mail()`[¶](https://docs.djangoproject.com/en/6.0/topics/email/#send-mass-mail-vs-send-mail "Link to this heading")
The main difference between [`send_mass_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mass_mail "django.core.mail.send_mass_mail") and [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") is that [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") opens a connection to the mail server each time it’s executed, while [`send_mass_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mass_mail "django.core.mail.send_mass_mail") uses a single connection for all of its messages. This makes [`send_mass_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mass_mail "django.core.mail.send_mass_mail") slightly more efficient.
##  `mail_admins()`[¶](https://docs.djangoproject.com/en/6.0/topics/email/#mail-admins "Link to this heading")

mail_admins(_subject_ , _message_ , _*_ , _fail_silently =False_, _connection =None_, _html_message =None_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.mail_admins "Link to this definition")

`django.core.mail.mail_admins()` is a shortcut for sending an email to the site admins, as defined in the [`ADMINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ADMINS) setting.
`mail_admins()` prefixes the subject with the value of the [`EMAIL_SUBJECT_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SUBJECT_PREFIX) setting, which is `"[Django] "` by default.
The “From:” header of the email will be the value of the [`SERVER_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SERVER_EMAIL) setting.
This method exists for convenience and readability.
If `html_message` is provided, the resulting email will be a _multipart/alternative_ email with `message` as the _text/plain_ content type and `html_message` as the _text/html_ content type.
Deprecated since version 6.0: Passing `fail_silently` and later parameters as positional arguments is deprecated.
##  `mail_managers()`[¶](https://docs.djangoproject.com/en/6.0/topics/email/#mail-managers "Link to this heading")

mail_managers(_subject_ , _message_ , _*_ , _fail_silently =False_, _connection =None_, _html_message =None_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.mail_managers "Link to this definition")

`django.core.mail.mail_managers()` is just like `mail_admins()`, except it sends an email to the site managers, as defined in the [`MANAGERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MANAGERS) setting.
Deprecated since version 6.0: Passing `fail_silently` and later parameters as positional arguments is deprecated.
## Examples[¶](https://docs.djangoproject.com/en/6.0/topics/email/#examples "Link to this heading")
This sends a single email to
```
send_mail(
    "Subject",
    "Message.",
    "from@example.com",
    ["john@example.com", "jane@example.com"],
)

```

This sends a message to `john@example.com` and `jane@example.com`, with them both receiving a separate email:
```
datatuple = (
    ("Subject", "Message.", "from@example.com", ["john@example.com"]),
    ("Subject", "Message.", "from@example.com", ["jane@example.com"]),
)
send_mass_mail(datatuple)

```

## Preventing header injection[¶](https://docs.djangoproject.com/en/6.0/topics/email/#preventing-header-injection "Link to this heading")
The Django email functions outlined above all protect against header injection by forbidding newlines in header values. If any `subject`, `from_email` or `recipient_list` contains a newline (in either Unix, Windows or Mac style), the email function (e.g. [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail")) will raise
If a `message` contains headers at the start of the string, the headers will be printed as the first bit of the email message.
Here’s an example view that takes a `subject`, `message` and `from_email` from the request’s POST data, sends that to `admin@example.com` and redirects to “/contact/thanks/” when it’s done:
```
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")
    from_email = request.POST.get("from_email", "")
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["admin@example.com"])
        except ValueError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("/contact/thanks/")
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")

```

Changed in Django 6.0:
Older versions raised `django.core.mail.BadHeaderError` for some invalid headers. This has been replaced with `ValueError`.
## The `EmailMessage` class[¶](https://docs.djangoproject.com/en/6.0/topics/email/#the-emailmessage-class "Link to this heading")
Django’s [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") and [`send_mass_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mass_mail "django.core.mail.send_mass_mail") functions are actually thin wrappers that make use of the [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") class.
Not all features of the [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") class are available through the [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") and related wrapper functions. If you wish to use advanced features, such as BCC’ed recipients, file attachments, or multi-part email, you’ll need to create [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") instances directly.
Note
This is a design feature. [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") and related functions were originally the only interface Django provided. However, the list of parameters they accepted was slowly growing over time. It made sense to move to a more object-oriented design for email messages and retain the original functions only for backwards compatibility.
[`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") is responsible for creating the email message itself. The [email backend](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-backends) is then responsible for sending the email.
For convenience, [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") provides a [`send()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.send "django.core.mail.EmailMessage.send") method for sending a single email. If you need to send multiple messages, the email backend API [provides an alternative](https://docs.djangoproject.com/en/6.0/topics/email/#topics-sending-multiple-emails).
###  `EmailMessage` Objects[¶](https://docs.djangoproject.com/en/6.0/topics/email/#emailmessage-objects "Link to this heading")

_class_ EmailMessage[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "Link to this definition")

The `EmailMessage` class is initialized with the following parameters. All parameters are optional and can be set at any time prior to calling the [`send()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.send "django.core.mail.EmailMessage.send") method.
The first four parameters can be passed as positional or keyword arguments, but must be in the given order if positional arguments are used:
  * `subject`: The subject line of the email.
  * `body`: The body text. This should be a plain text message.
  * `from_email`: The sender’s address. Both `fred@example.com` and `"Fred" <fred@example.com>` forms are legal. If omitted, the [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_FROM_EMAIL) setting is used.
  * `to`: A list or tuple of recipient addresses.


The following parameters must be given as keyword arguments if used:
  * `cc`: A list or tuple of recipient addresses used in the “Cc” header when sending the email.
  * `bcc`: A list or tuple of addresses used in the “Bcc” header when sending the email.
  * `reply_to`: A list or tuple of recipient addresses used in the “Reply-To” header when sending the email.
  * `attachments`: A list of attachments to put on the message. Each can be an instance of [`EmailAttachment`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailAttachment "django.core.mail.EmailAttachment"), or a tuple with attributes `(filename, content, mimetype)`.
Changed in Django 5.2:
Support for [`EmailAttachment`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailAttachment "django.core.mail.EmailAttachment") items of `attachments` was added.
Changed in Django 6.0:
Support for `attachments` list was added.
Deprecated since version 6.0: Support for Python’s legacy `attachments` is deprecated. Use
  * `headers`: A dictionary of extra headers to put on the message. The keys are the header name, values are the header values. It’s up to the caller to ensure header names and values are in the correct format for an email message. The corresponding attribute is `extra_headers`.
  * `connection`: An [email backend](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-backends) instance. Use this parameter if you are sending the `EmailMessage` via [`send()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.send "django.core.mail.EmailMessage.send") and you want to use the same connection for multiple messages. If omitted, a new connection is created when [`send()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.send "django.core.mail.EmailMessage.send") is called. This parameter is ignored when using [send_messages()](https://docs.djangoproject.com/en/6.0/topics/email/#topics-sending-multiple-emails).


Deprecated since version 6.0: Passing all except the first four parameters as positional arguments is deprecated.
For example:
```
from django.core.mail import EmailMessage

email = EmailMessage(
    subject="Hello",
    body="Body goes here",
    from_email="from@example.com",
    to=["to1@example.com", "to2@example.com"],
    bcc=["bcc@example.com"],
    reply_to=["another@example.com"],
    headers={"Message-ID": "foo"},
)

```

The class has the following methods:

send(_fail_silently =False_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.send "Link to this definition")

Sends the message. If a connection was specified when the email was constructed, that connection will be used. Otherwise, an instance of the default backend will be instantiated and used. If the keyword argument `fail_silently` is `True`, exceptions raised while sending the message will be quashed. An empty list of recipients will not raise an exception. It will return `1` if the message was sent successfully, otherwise `0`.

message(_policy =email.policy.default_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.message "Link to this definition")

Constructs and returns a Python
The keyword argument `policy` allows specifying the set of rules for updating and serializing the representation of the message. It must be an [`django.core.mail.backends.smtp.EmailBackend`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.backends.smtp.EmailBackend "django.core.mail.backends.smtp.EmailBackend") uses the `\r\n` line endings as required by the SMTP protocol.
If you ever need to extend Django’s [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") class, you’ll probably want to override this method to put the content you want into the Python EmailMessage object.
Changed in Django 6.0:
The `policy` keyword argument was added and the return type was updated to an instance of

recipients()[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.recipients "Link to this definition")

Returns a list of all the recipients of the message, whether they’re recorded in the `to`, `cc` or `bcc` attributes. This is another method you might need to override when subclassing, because the SMTP server needs to be told the full list of recipients when the message is sent. If you add another way to specify recipients in your class, they need to be returned from this method as well.

attach(_filename_ , _content_ , _mimetype_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.attach "Link to this definition")


attach(_mimepart_)

Creates a new attachment and adds it to the message. There are two ways to call `attach()`:
  * You can pass it three arguments: `filename`, `content` and `mimetype`. `filename` is the name of the file attachment as it will appear in the email, `content` is the data that will be contained inside the attachment and `mimetype` is the optional MIME type for the attachment. If you omit `mimetype`, the MIME content type will be guessed from the filename of the attachment.
For example:
```
message.attach("design.png", img_data, "image/png")

```

If you specify a `mimetype` of _message/rfc822_ , `content` can be a [`django.core.mail.EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") or Python’s
For a `mimetype` starting with _text/_ , content is expected to be a string. Binary data will be decoded using UTF-8, and if that fails, the MIME type will be changed to _application/octet-stream_ and the data will be attached unchanged.
  * Or for attachments requiring additional headers or parameters, you can pass `attach()` a single Python _Content-ID_ :
```
import email.utils
from email.message import MIMEPart
from django.core.mail import EmailMultiAlternatives

message = EmailMultiAlternatives(...)
image_data_bytes = ...  # Load image as bytes

# Create a random Content-ID, including angle brackets
cid = email.utils.make_msgid()
inline_image = email.message.MIMEPart()
inline_image.set_content(
    image_data_bytes,
    maintype="image",
    subtype="png",  # or "jpeg", etc. depending on the image type
    disposition="inline",
    cid=cid,
)
message.attach(inline_image)
# Refer to Content-ID in HTML without angle brackets
message.attach_alternative(f'… <img src="cid:{cid[1:-1]}"> …', "text/html")

```

Python’s `MIMEPart.set_content()`.
Changed in Django 6.0:
Support for
Deprecated since version 6.0: Support for



attach_file(_path_ , _mimetype =None_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.attach_file "Link to this definition")

Creates a new attachment using a file from your filesystem. Call it with the path of the file to attach and, optionally, the MIME type to use for the attachment. If the MIME type is omitted, it will be guessed from the filename. You can use it like this:
```
message.attach_file("/images/weather_map.png")

```

For MIME types starting with _text/_ , binary data is handled as in [`attach()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage.attach "django.core.mail.EmailMessage.attach").

_class_ EmailAttachment[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailAttachment "Link to this definition")

New in Django 5.2.
A named tuple to store attachments to an email.
The named tuple has the following indexes:
  * `filename`
  * `content`
  * `mimetype`


### Sending alternative content types[¶](https://docs.djangoproject.com/en/6.0/topics/email/#sending-alternative-content-types "Link to this heading")
#### Sending multiple content versions[¶](https://docs.djangoproject.com/en/6.0/topics/email/#sending-multiple-content-versions "Link to this heading")
It can be useful to include multiple versions of the content in an email; the classic example is to send both text and HTML versions of a message. With Django’s email library, you can do this using the [`EmailMultiAlternatives`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives "django.core.mail.EmailMultiAlternatives") class.

_class_ EmailMultiAlternatives[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives "Link to this definition")

A subclass of [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") that allows additional versions of the message body in the email via the [`attach_alternative()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives.attach_alternative "django.core.mail.EmailMultiAlternatives.attach_alternative") method. This directly inherits all methods (including the class initialization) from [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage").

alternatives[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives.alternatives "Link to this definition")

A list of [`EmailAlternative`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailAlternative "django.core.mail.EmailAlternative") named tuples. This is particularly useful in tests:
```
self.assertEqual(len(msg.alternatives), 1)
self.assertEqual(msg.alternatives[0].content, html_content)
self.assertEqual(msg.alternatives[0].mimetype, "text/html")

```

Alternatives should only be added using the [`attach_alternative()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives.attach_alternative "django.core.mail.EmailMultiAlternatives.attach_alternative") method, or passed to the constructor.
Changed in Django 5.2:
In older versions, `alternatives` was a list of regular tuples, as opposed to [`EmailAlternative`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailAlternative "django.core.mail.EmailAlternative") named tuples.

attach_alternative(_content_ , _mimetype_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives.attach_alternative "Link to this definition")

Attach an alternative representation of the message body in the email.
For example, to send a text and HTML combination, you could write:
```
from django.core.mail import EmailMultiAlternatives

subject = "hello"
from_email = "from@example.com"
to = "to@example.com"
text_content = "This is an important message."
html_content = "<p>This is an <strong>important</strong> message.</p>"
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()

```


body_contains(_text_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMultiAlternatives.body_contains "Link to this definition")

New in Django 5.2.
Returns a boolean indicating whether the provided `text` is contained in the email `body` and in all attached MIME type `text/*` alternatives.
This can be useful when testing emails. For example:
```
def test_contains_email_content(self):
    subject = "Hello World"
    from_email = "from@example.com"
    to = "to@example.com"
    msg = EmailMultiAlternatives(subject, "I am content.", from_email, [to])
    msg.attach_alternative("<p>I am content.</p>", "text/html")

    self.assertIs(msg.body_contains("I am content"), True)
    self.assertIs(msg.body_contains("<p>I am content.</p>"), False)

```


_class_ EmailAlternative[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailAlternative "Link to this definition")

New in Django 5.2.
A named tuple to store alternative versions of email content.
The named tuple has the following indexes:
  * `content`
  * `mimetype`


#### Updating the default content type[¶](https://docs.djangoproject.com/en/6.0/topics/email/#updating-the-default-content-type "Link to this heading")
By default, the MIME type of the `body` parameter in an [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") is `"text/plain"`. It is good practice to leave this alone, because it guarantees that any recipient will be able to read the email, regardless of their mail client. However, if you are confident that your recipients can handle an alternative content type, you can use the `content_subtype` attribute on the [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") class to change the main content type. The major type will always be `"text"`, but you can change the subtype. For example:
```
msg = EmailMessage(subject, html_content, from_email, [to])
msg.content_subtype = "html"  # Main content is now text/html
msg.send()

```

## Email backends[¶](https://docs.djangoproject.com/en/6.0/topics/email/#email-backends "Link to this heading")
The actual sending of an email is handled by the email backend.
The email backend class has the following methods:
  * `open()` instantiates a long-lived email-sending connection.
  * `close()` closes the current email-sending connection.
  * `send_messages(email_messages)` sends a list of [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") objects. If the connection is not open, this call will implicitly open the connection, and close the connection afterward. If the connection is already open, it will be left open after mail has been sent.


It can also be used as a context manager, which will automatically call `open()` and `close()` as needed:
```
from django.core import mail

with mail.get_connection() as connection:
    mail.EmailMessage(
        subject1,
        body1,
        from1,
        [to1],
        connection=connection,
    ).send()
    mail.EmailMessage(
        subject2,
        body2,
        from2,
        [to2],
        connection=connection,
    ).send()

```

### Obtaining an instance of an email backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#obtaining-an-instance-of-an-email-backend "Link to this heading")
The [`get_connection()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.get_connection "django.core.mail.get_connection") function in `django.core.mail` returns an instance of the email backend that you can use.

get_connection(_backend =None_, _*_ , _fail_silently =False_, _** kwargs_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.get_connection "Link to this definition")

By default, a call to `get_connection()` will return an instance of the email backend specified in [`EMAIL_BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_BACKEND). If you specify the `backend` argument, an instance of that backend will be instantiated.
The keyword-only `fail_silently` argument controls how the backend should handle errors. If `fail_silently` is True, exceptions during the email sending process will be silently ignored.
All other keyword arguments are passed directly to the constructor of the email backend.
Django ships with several email sending backends. With the exception of the SMTP backend (which is the default), these backends are only useful during testing and development. If you have special email sending requirements, you can [write your own email backend](https://docs.djangoproject.com/en/6.0/topics/email/#topic-custom-email-backend).
Deprecated since version 6.0: Passing `fail_silently` as positional argument is deprecated.
#### SMTP backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#smtp-backend "Link to this heading")

_class_ backends.smtp.EmailBackend(_host =None_, _port =None_, _username =None_, _password =None_, _use_tls =None_, _fail_silently =False_, _use_ssl =None_, _timeout =None_, _ssl_keyfile =None_, _ssl_certfile =None_, _** kwargs_)[¶](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.backends.smtp.EmailBackend "Link to this definition")

This is the default backend. Email will be sent through a SMTP server.
The value for each argument is retrieved from the matching setting if the argument is `None`:
  * `host`: [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST)
  * `port`: [`EMAIL_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_PORT)
  * `username`: [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_USER)
  * `password`: [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_PASSWORD)
  * `use_tls`: [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS)
  * `use_ssl`: [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL)
  * `timeout`: [`EMAIL_TIMEOUT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_TIMEOUT)
  * `ssl_keyfile`: [`EMAIL_SSL_KEYFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_KEYFILE)
  * `ssl_certfile`: [`EMAIL_SSL_CERTFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_CERTFILE)


The SMTP backend is the default configuration inherited by Django. If you want to specify it explicitly, put the following in your settings:
```
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

```

If unspecified, the default `timeout` will be the one provided by `None` (no timeout).
#### Console backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#console-backend "Link to this heading")
Instead of sending out real emails the console backend just writes the emails that would be sent to the standard output. By default, the console backend writes to `stdout`. You can use a different stream-like object by providing the `stream` keyword argument when constructing the connection.
To specify this backend, put the following in your settings:
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

```

This backend is not intended for use in production – it is provided as a convenience that can be used during development.
#### File backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#file-backend "Link to this heading")
The file backend writes emails to a file. A new file is created for each new session that is opened on this backend. The directory to which the files are written is either taken from the [`EMAIL_FILE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_FILE_PATH) setting or from the `file_path` keyword when creating a connection with [`get_connection()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.get_connection "django.core.mail.get_connection").
To specify this backend, put the following in your settings:
```
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "/tmp/app-messages"  # change this to a proper location

```

This backend is not intended for use in production – it is provided as a convenience that can be used during development.
#### In-memory backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#in-memory-backend "Link to this heading")
The `'locmem'` backend stores messages in a special attribute of the `django.core.mail` module. The `outbox` attribute is created when the first message is sent. It’s a list with an [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") instance for each message that would be sent.
To specify this backend, put the following in your settings:
```
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

```

This backend is not intended for use in production – it is provided as a convenience that can be used during development and testing.
Django’s test runner [automatically uses this backend for testing](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#topics-testing-email).
#### Dummy backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#dummy-backend "Link to this heading")
As the name suggests the dummy backend does nothing with your messages. To specify this backend, put the following in your settings:
```
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

```

This backend is not intended for use in production – it is provided as a convenience that can be used during development.
There are community-maintained solutions too!
Django has a vibrant ecosystem. There are email backends highlighted on the [Community Ecosystem](https://www.djangoproject.com/community/ecosystem/#email-and-notifications) page. The Django Packages
### Defining a custom email backend[¶](https://docs.djangoproject.com/en/6.0/topics/email/#defining-a-custom-email-backend "Link to this heading")
If you need to change how emails are sent you can write your own email backend. The [`EMAIL_BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_BACKEND) setting in your settings file is then the Python import path for your backend class.
Custom email backends should subclass `BaseEmailBackend` that is located in the `django.core.mail.backends.base` module. A custom email backend must implement the `send_messages(email_messages)` method. This method receives a list of [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") instances and returns the number of successfully delivered messages. If your backend has any concept of a persistent session or connection, you should also implement the `open()` and `close()` methods. Refer to `smtp.EmailBackend` for a reference implementation.
### Sending multiple emails[¶](https://docs.djangoproject.com/en/6.0/topics/email/#sending-multiple-emails "Link to this heading")
Establishing and closing an SMTP connection (or any other network connection, for that matter) is an expensive process. If you have a lot of emails to send, it makes sense to reuse an SMTP connection, rather than creating and destroying a connection every time you want to send an email.
There are two ways you tell an email backend to reuse a connection.
Firstly, you can use the `send_messages()` method on a connection. This takes a list of [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") (or subclass) instances, and sends them all using that single connection. As a consequence, any [`connection`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") set on an individual message is ignored.
For example, if you have a function called `get_notification_email()` that returns a list of [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") objects representing some periodic email you wish to send out, you could send these emails using a single call to `send_messages()`:
```
from django.core import mail

connection = mail.get_connection()  # Use default email connection
messages = get_notification_email()
connection.send_messages(messages)

```

In this example, the call to `send_messages()` opens a connection on the backend, sends the list of messages, and then closes the connection again.
The second approach is to use the `open()` and `close()` methods on the email backend to manually control the connection. `send_messages()` will not manually open or close the connection if it is already open, so if you manually open the connection, you can control when it is closed. For example:
```
from django.core import mail

connection = mail.get_connection()

# Manually open the connection
connection.open()

# Construct an email message that uses the connection
email1 = mail.EmailMessage(
    "Hello",
    "Body goes here",
    "from@example.com",
    ["to1@example.com"],
    connection=connection,
)
email1.send()  # Send the email

# Construct two more messages
email2 = mail.EmailMessage(
    "Hello",
    "Body goes here",
    "from@example.com",
    ["to2@example.com"],
)
email3 = mail.EmailMessage(
    "Hello",
    "Body goes here",
    "from@example.com",
    ["to3@example.com"],
)

# Send the two emails in a single call -
connection.send_messages([email2, email3])
# The connection was already open so send_messages() doesn't close it.
# We need to manually close the connection.
connection.close()

```

## Configuring email for development[¶](https://docs.djangoproject.com/en/6.0/topics/email/#configuring-email-for-development "Link to this heading")
There are times when you do not want Django to send emails at all. For example, while developing a website, you probably don’t want to send out thousands of emails – but you may want to validate that emails will be sent to the right people under the right conditions, and that those emails will contain the correct content.
The easiest way to configure email for local development is to use the [console](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-console-backend) email backend. This backend redirects all email to `stdout`, allowing you to inspect the content of mail.
The [file](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-file-backend) email backend can also be useful during development – this backend dumps the contents of every SMTP connection to a file that can be inspected at your leisure.
Another approach is to use a “dumb” SMTP server that receives the emails locally and displays them to the terminal, but does not actually send anything. The
```
python -m pip install "aiosmtpd >= 1.4.5"

python -m aiosmtpd -n -l localhost:8025

```

This command will start a minimal SMTP server listening on port 8025 of localhost. This server prints to standard output all email headers and the email body. You then only need to set the [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST) and [`EMAIL_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_PORT) accordingly. For a more detailed discussion of SMTP server options, see the documentation of the
For information about unit-testing the sending of emails in your application, see the [Email services](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#topics-testing-email) section of the testing documentation.
Previous page and next page
[](https://docs.djangoproject.com/en/6.0/topics/signing/)
[Internationalization and localization ](https://docs.djangoproject.com/en/6.0/topics/i18n/)
[](https://docs.djangoproject.com/en/6.0/topics/email/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Ramana Varanasi donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Sending email](https://docs.djangoproject.com/en/6.0/topics/email/)
    * [Quick examples](https://docs.djangoproject.com/en/6.0/topics/email/#quick-examples)
    * [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#send-mail)
    * [`send_mass_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#send-mass-mail)
      * [`send_mass_mail()` vs. `send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#send-mass-mail-vs-send-mail)
    * [`mail_admins()`](https://docs.djangoproject.com/en/6.0/topics/email/#mail-admins)
    * [`mail_managers()`](https://docs.djangoproject.com/en/6.0/topics/email/#mail-managers)
    * [Examples](https://docs.djangoproject.com/en/6.0/topics/email/#examples)
    * [Preventing header injection](https://docs.djangoproject.com/en/6.0/topics/email/#preventing-header-injection)
    * [The `EmailMessage` class](https://docs.djangoproject.com/en/6.0/topics/email/#the-emailmessage-class)
      * [`EmailMessage` Objects](https://docs.djangoproject.com/en/6.0/topics/email/#emailmessage-objects)
      * [Sending alternative content types](https://docs.djangoproject.com/en/6.0/topics/email/#sending-alternative-content-types)
        * [Sending multiple content versions](https://docs.djangoproject.com/en/6.0/topics/email/#sending-multiple-content-versions)
        * [Updating the default content type](https://docs.djangoproject.com/en/6.0/topics/email/#updating-the-default-content-type)
    * [Email backends](https://docs.djangoproject.com/en/6.0/topics/email/#email-backends)
      * [Obtaining an instance of an email backend](https://docs.djangoproject.com/en/6.0/topics/email/#obtaining-an-instance-of-an-email-backend)
        * [SMTP backend](https://docs.djangoproject.com/en/6.0/topics/email/#smtp-backend)
        * [Console backend](https://docs.djangoproject.com/en/6.0/topics/email/#console-backend)
        * [File backend](https://docs.djangoproject.com/en/6.0/topics/email/#file-backend)
        * [In-memory backend](https://docs.djangoproject.com/en/6.0/topics/email/#in-memory-backend)
        * [Dummy backend](https://docs.djangoproject.com/en/6.0/topics/email/#dummy-backend)
      * [Defining a custom email backend](https://docs.djangoproject.com/en/6.0/topics/email/#defining-a-custom-email-backend)
      * [Sending multiple emails](https://docs.djangoproject.com/en/6.0/topics/email/#sending-multiple-emails)
    * [Configuring email for development](https://docs.djangoproject.com/en/6.0/topics/email/#configuring-email-for-development)


### Browse
  * Prev: [Cryptographic signing](https://docs.djangoproject.com/en/6.0/topics/signing/)
  * Next: [Internationalization and localization](https://docs.djangoproject.com/en/6.0/topics/i18n/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [Using Django](https://docs.djangoproject.com/en/6.0/topics/)
      * Sending email


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
