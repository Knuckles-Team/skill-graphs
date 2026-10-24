Copy```
import mailbox
import email.errors

list_names = ('python-list', 'python-dev', 'python-bugs')

boxes = {name: mailbox.mbox('~/email/%s' % name) for name in list_names}
inbox = mailbox.Maildir('~/Maildir', factory=None)

for key in inbox.iterkeys():
    try:
        message = inbox[key]
    except email.errors.MessageParseError:
        continue                # The message is malformed. Just leave it.

    for name in list_names:
        list_id = message['list-id']
        if list_id and name in list_id:
            # Get mailbox to use
            box = boxes[name]

            # Write copy to disk before removing original.
            # If there's a crash, you might duplicate a message, but
            # that's better than losing a message completely.
            box.lock()
            box.add(message)
            box.flush()
            box.unlock()

            # Remove original message
            inbox.lock()
            inbox.discard(key)
            inbox.flush()
            inbox.unlock()
            break               # Found destination, so stop looking.

for box in boxes.itervalues():
    box.close()

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3/library/mailbox.html)
    * [`Mailbox` objects](https://docs.python.org/3/library/mailbox.html#mailbox-objects)
      * [`Maildir` objects](https://docs.python.org/3/library/mailbox.html#maildir-objects)
      * [`mbox` objects](https://docs.python.org/3/library/mailbox.html#mbox-objects)
      * [`MH` objects](https://docs.python.org/3/library/mailbox.html#mh-objects)
      * [`Babyl` objects](https://docs.python.org/3/library/mailbox.html#babyl-objects)
      * [`MMDF` objects](https://docs.python.org/3/library/mailbox.html#mmdf-objects)
    * [`Message` objects](https://docs.python.org/3/library/mailbox.html#message-objects)
      * [`MaildirMessage` objects](https://docs.python.org/3/library/mailbox.html#maildirmessage-objects)
      * [`mboxMessage` objects](https://docs.python.org/3/library/mailbox.html#mboxmessage-objects)
      * [`MHMessage` objects](https://docs.python.org/3/library/mailbox.html#mhmessage-objects)
      * [`BabylMessage` objects](https://docs.python.org/3/library/mailbox.html#babylmessage-objects)
      * [`MMDFMessage` objects](https://docs.python.org/3/library/mailbox.html#mmdfmessage-objects)
    * [Exceptions](https://docs.python.org/3/library/mailbox.html#exceptions)
    * [Examples](https://docs.python.org/3/library/mailbox.html#examples)


#### Previous topic
[`json` — JSON encoder and decoder](https://docs.python.org/3/library/json.html "previous chapter")
#### Next topic
[`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=mailbox+%E2%80%94+Manipulate+mailboxes+in+various+formats&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmailbox.html&pagesource=library%2Fmailbox.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/mimetypes.html "mimetypes — Map filenames to MIME types") |
  * [previous](https://docs.python.org/3/library/json.html "json — JSON encoder and decoder") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3/library/mailbox.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
