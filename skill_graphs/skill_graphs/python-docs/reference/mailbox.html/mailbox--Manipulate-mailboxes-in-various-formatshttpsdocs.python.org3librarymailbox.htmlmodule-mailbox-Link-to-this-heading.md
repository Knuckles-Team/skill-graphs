#  `mailbox` — Manipulate mailboxes in various formats[¶](https://docs.python.org/3/library/mailbox.html#module-mailbox "Link to this heading")
**Source code:**
* * *
This module defines two classes, [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") and [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message"), for accessing and manipulating on-disk mailboxes and the messages they contain. `Mailbox` offers a dictionary-like mapping from keys to messages. `Message` extends the [`email.message`](https://docs.python.org/3/library/email.message.html#module-email.message "email.message: The base class representing email messages.") module’s [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") class with format-specific state and behavior. Supported mailbox formats are Maildir, mbox, MH, Babyl, and MMDF.
See also

Module [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")

Represent and manipulate messages.
