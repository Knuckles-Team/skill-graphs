
get_date()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_date "Link to this definition")

Return the delivery date of the message as a floating-point number representing seconds since the epoch.

set_date(_date_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_date "Link to this definition")

Set the delivery date of the message to _date_ , a floating-point number representing seconds since the epoch.

get_info()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_info "Link to this definition")

Return a string containing the “info” for a message. This is useful for accessing and modifying “info” that is experimental (i.e., not a list of flags).

set_info(_info_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_info "Link to this definition")

Set “info” to _info_ , which should be a string.
When a `MaildirMessage` instance is created based upon an [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the _Status_ and _X-Status_ headers are omitted and the following conversions take place:
Resulting state | [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") state
---|---
“cur” subdirectory | O flag
F flag | F flag
R flag | A flag
S flag | R flag
T flag | D flag
When a `MaildirMessage` instance is created based upon an [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:
Resulting state | [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") state
---|---
“cur” subdirectory | “unseen” sequence
“cur” subdirectory and S flag | no “unseen” sequence
F flag | “flagged” sequence
R flag | “replied” sequence
When a `MaildirMessage` instance is created based upon a [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:
Resulting state | [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") state
---|---
“cur” subdirectory | “unseen” label
“cur” subdirectory and S flag | no “unseen” label
P flag | “forwarded” or “resent” label
R flag | “answered” label
T flag | “deleted” label
###  `mboxMessage` objects[¶](https://docs.python.org/3/library/mailbox.html#mboxmessage-objects "Link to this heading")

_class_ mailbox.mboxMessage(_message =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "Link to this definition")

A message with mbox-specific behaviors. Parameter _message_ has the same meaning as with the [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") constructor.
Messages in an mbox mailbox are stored together in a single file. The sender’s envelope address and the time of delivery are typically stored in a line beginning with “From “ that is used to indicate the start of a message, though there is considerable variation in the exact format of this data among mbox implementations. Flags that indicate the state of the message, such as whether it has been read or marked as important, are typically stored in _Status_ and _X-Status_ headers.
Conventional flags for mbox messages are as follows:
Flag | Meaning | Explanation
---|---|---
R | Read | Read
O | Old | Previously detected by MUA
D | Deleted | Marked for subsequent deletion
F | Flagged | Marked as important
A | Answered | Replied to
The “R” and “O” flags are stored in the _Status_ header, and the “D”, “F”, and “A” flags are stored in the _X-Status_ header. The flags and headers typically appear in the order mentioned.
`mboxMessage` instances offer the following methods:

get_from()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage.get_from "Link to this definition")

Return a string representing the “From “ line that marks the start of the message in an mbox mailbox. The leading “From “ and the trailing newline are excluded.

set_from(_from__ , _time_ =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage.set_from "Link to this definition")

Set the “From “ line to _from__ , which should be specified without a leading “From “ or trailing newline. For convenience, _time__ may be specified and will be formatted appropriately and appended to _from__. If _time__ is specified, it should be a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") instance, a tuple suitable for passing to [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime"), or `True` (to use [`time.gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")).

get_flags()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage.get_flags "Link to this definition")

Return a string specifying the flags that are currently set. If the message complies with the conventional format, the result is the concatenation in the following order of zero or one occurrence of each of `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

set_flags(_flags_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage.set_flags "Link to this definition")

Set the flags specified by _flags_ and unset all others. Parameter _flags_ should be the concatenation in any order of zero or more occurrences of each of `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

add_flag(_flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage.add_flag "Link to this definition")

Set the flag(s) specified by _flag_ without changing other flags. To add more than one flag at a time, _flag_ may be a string of more than one character.

remove_flag(_flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage.remove_flag "Link to this definition")

Unset the flag(s) specified by _flag_ without changing other flags. To remove more than one flag at a time, _flag_ may be a string of more than one character.
When an `mboxMessage` instance is created based upon a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, a “From “ line is generated based upon the `MaildirMessage` instance’s delivery date, and the following conversions take place:
Resulting state | [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") state
---|---
R flag | S flag
O flag | “cur” subdirectory
D flag | T flag
F flag | F flag
A flag | R flag
When an `mboxMessage` instance is created based upon an [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:
Resulting state | [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") state
---|---
R flag and O flag | no “unseen” sequence
O flag | “unseen” sequence
F flag | “flagged” sequence
A flag | “replied” sequence
When an `mboxMessage` instance is created based upon a [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:
Resulting state | [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") state
---|---
R flag and O flag | no “unseen” label
O flag | “unseen” label
D flag | “deleted” label
A flag | “answered” label
When a `mboxMessage` instance is created based upon an [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the “From “ line is copied and all flags directly correspond:
Resulting state | [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") state
---|---
R flag | R flag
O flag | O flag
D flag | D flag
F flag | F flag
A flag | A flag
###  `MHMessage` objects[¶](https://docs.python.org/3/library/mailbox.html#mhmessage-objects "Link to this heading")

_class_ mailbox.MHMessage(_message =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "Link to this definition")

A message with MH-specific behaviors. Parameter _message_ has the same meaning as with the [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") constructor.
MH messages do not support marks or flags in the traditional sense, but they do support sequences, which are logical groupings of arbitrary messages. Some mail reading programs (although not the standard **mh** and **nmh**) use sequences in much the same way flags are used with other formats, as follows:
Sequence | Explanation
---|---
unseen | Not read, but previously detected by MUA
replied | Replied to
flagged | Marked as important
`MHMessage` instances offer the following methods:

get_sequences()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage.get_sequences "Link to this definition")

Return a list of the names of sequences that include this message.

set_sequences(_sequences_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage.set_sequences "Link to this definition")

Set the list of sequences that include this message.

add_sequence(_sequence_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage.add_sequence "Link to this definition")

Add _sequence_ to the list of sequences that include this message.

remove_sequence(_sequence_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage.remove_sequence "Link to this definition")

Remove _sequence_ from the list of sequences that include this message.
When an `MHMessage` instance is created based upon a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, the following conversions take place:
Resulting state | [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") state
---|---
“unseen” sequence | no S flag
“replied” sequence | R flag
“flagged” sequence | F flag
When an `MHMessage` instance is created based upon an [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the _Status_ and _X-Status_ headers are omitted and the following conversions take place:
Resulting state | [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") state
---|---
“unseen” sequence | no R flag
“replied” sequence | A flag
“flagged” sequence | F flag
When an `MHMessage` instance is created based upon a [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:
Resulting state | [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") state
---|---
“unseen” sequence | “unseen” label
“replied” sequence | “answered” label
###  `BabylMessage` objects[¶](https://docs.python.org/3/library/mailbox.html#babylmessage-objects "Link to this heading")

_class_ mailbox.BabylMessage(_message =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "Link to this definition")

A message with Babyl-specific behaviors. Parameter _message_ has the same meaning as with the [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") constructor.
Certain message labels, called _attributes_ , are defined by convention to have special meanings. The attributes are as follows:
Label | Explanation
---|---
unseen | Not read, but previously detected by MUA
deleted | Marked for subsequent deletion
filed | Copied to another file or mailbox
answered | Replied to
forwarded | Forwarded
edited | Modified by the user
resent | Resent
By default, Rmail displays only visible headers. The `BabylMessage` class, though, uses the original headers because they are more complete. Visible headers may be accessed explicitly if desired.
`BabylMessage` instances offer the following methods:

get_labels()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.get_labels "Link to this definition")

Return a list of labels on the message.

set_labels(_labels_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.set_labels "Link to this definition")

Set the list of labels on the message to _labels_.

add_label(_label_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.add_label "Link to this definition")

Add _label_ to the list of labels on the message.

remove_label(_label_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.remove_label "Link to this definition")

Remove _label_ from the list of labels on the message.

get_visible()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.get_visible "Link to this definition")

Return a [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") instance whose headers are the message’s visible headers and whose body is empty.

set_visible(_visible_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.set_visible "Link to this definition")

Set the message’s visible headers to be the same as the headers in _message_. Parameter _visible_ should be a [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") instance, an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") instance, a string, or a file-like object (which should be open in text mode).

update_visible()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage.update_visible "Link to this definition")

When a `BabylMessage` instance’s original headers are modified, the visible headers are not automatically modified to correspond. This method updates the visible headers as follows: each visible header with a corresponding original header is set to the value of the original header, each visible header without a corresponding original header is removed, and any of _Date_ , _From_ , _Reply-To_ , _To_ , _CC_ , and _Subject_ that are present in the original headers but not the visible headers are added to the visible headers.
When a `BabylMessage` instance is created based upon a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, the following conversions take place:
Resulting state | [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") state
---|---
“unseen” label | no S flag
“deleted” label | T flag
“answered” label | R flag
“forwarded” label | P flag
When a `BabylMessage` instance is created based upon an [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") instance, the _Status_ and _X-Status_ headers are omitted and the following conversions take place:
Resulting state | [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") or [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") state
---|---
“unseen” label | no R flag
“deleted” label | D flag
“answered” label | A flag
When a `BabylMessage` instance is created based upon an [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:
Resulting state | [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") state
---|---
“unseen” label | “unseen” sequence
“answered” label | “replied” sequence
###  `MMDFMessage` objects[¶](https://docs.python.org/3/library/mailbox.html#mmdfmessage-objects "Link to this heading")

_class_ mailbox.MMDFMessage(_message =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "Link to this definition")

A message with MMDF-specific behaviors. Parameter _message_ has the same meaning as with the [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") constructor.
As with message in an mbox mailbox, MMDF messages are stored with the sender’s address and the delivery date in an initial line beginning with “From “. Likewise, flags that indicate the state of the message are typically stored in _Status_ and _X-Status_ headers.
Conventional flags for MMDF messages are identical to those of mbox message and are as follows:
Flag | Meaning | Explanation
---|---|---
R | Read | Read
O | Old | Previously detected by MUA
D | Deleted | Marked for subsequent deletion
F | Flagged | Marked as important
A | Answered | Replied to
The “R” and “O” flags are stored in the _Status_ header, and the “D”, “F”, and “A” flags are stored in the _X-Status_ header. The flags and headers typically appear in the order mentioned.
`MMDFMessage` instances offer the following methods, which are identical to those offered by [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage"):

get_from()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage.get_from "Link to this definition")

Return a string representing the “From “ line that marks the start of the message in an mbox mailbox. The leading “From “ and the trailing newline are excluded.

set_from(_from__ , _time_ =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage.set_from "Link to this definition")

Set the “From “ line to _from__ , which should be specified without a leading “From “ or trailing newline. For convenience, _time__ may be specified and will be formatted appropriately and appended to _from__. If _time__ is specified, it should be a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") instance, a tuple suitable for passing to [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime"), or `True` (to use [`time.gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")).

get_flags()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage.get_flags "Link to this definition")

Return a string specifying the flags that are currently set. If the message complies with the conventional format, the result is the concatenation in the following order of zero or one occurrence of each of `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

set_flags(_flags_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage.set_flags "Link to this definition")

Set the flags specified by _flags_ and unset all others. Parameter _flags_ should be the concatenation in any order of zero or more occurrences of each of `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

add_flag(_flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage.add_flag "Link to this definition")

Set the flag(s) specified by _flag_ without changing other flags. To add more than one flag at a time, _flag_ may be a string of more than one character.

remove_flag(_flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage.remove_flag "Link to this definition")

Unset the flag(s) specified by _flag_ without changing other flags. To remove more than one flag at a time, _flag_ may be a string of more than one character.
When an `MMDFMessage` instance is created based upon a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") instance, a “From “ line is generated based upon the `MaildirMessage` instance’s delivery date, and the following conversions take place:
Resulting state | [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") state
---|---
R flag | S flag
O flag | “cur” subdirectory
D flag | T flag
F flag | F flag
A flag | R flag
When an `MMDFMessage` instance is created based upon an [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") instance, the following conversions take place:
Resulting state | [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") state
---|---
R flag and O flag | no “unseen” sequence
O flag | “unseen” sequence
F flag | “flagged” sequence
A flag | “replied” sequence
When an `MMDFMessage` instance is created based upon a [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") instance, the following conversions take place:
Resulting state | [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") state
---|---
R flag and O flag | no “unseen” label
O flag | “unseen” label
D flag | “deleted” label
A flag | “answered” label
When an `MMDFMessage` instance is created based upon an [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") instance, the “From “ line is copied and all flags directly correspond:
Resulting state | [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") state
---|---
R flag | R flag
O flag | O flag
D flag | D flag
F flag | F flag
A flag | A flag
## Exceptions[¶](https://docs.python.org/3/library/mailbox.html#exceptions "Link to this heading")
The following exception classes are defined in the `mailbox` module:

_exception_ mailbox.Error[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Error "Link to this definition")

The base class for all other module-specific exceptions.

_exception_ mailbox.NoSuchMailboxError[¶](https://docs.python.org/3/library/mailbox.html#mailbox.NoSuchMailboxError "Link to this definition")

Raised when a mailbox is expected but is not found, such as when instantiating a [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") subclass with a path that does not exist (and with the _create_ parameter set to `False`), or when opening a folder that does not exist.

_exception_ mailbox.NotEmptyError[¶](https://docs.python.org/3/library/mailbox.html#mailbox.NotEmptyError "Link to this definition")

Raised when a mailbox is not empty but is expected to be, such as when deleting a folder that contains messages.

_exception_ mailbox.ExternalClashError[¶](https://docs.python.org/3/library/mailbox.html#mailbox.ExternalClashError "Link to this definition")

Raised when some mailbox-related condition beyond the control of the program causes it to be unable to proceed, such as when failing to acquire a lock that another program already holds, or when a uniquely generated file name already exists.

_exception_ mailbox.FormatError[¶](https://docs.python.org/3/library/mailbox.html#mailbox.FormatError "Link to this definition")

Raised when the data in a file cannot be parsed, such as when an [`MH`](https://docs.python.org/3/library/mailbox.html#mailbox.MH "mailbox.MH") instance attempts to read a corrupted `.mh_sequences` file.
## Examples[¶](https://docs.python.org/3/library/mailbox.html#examples "Link to this heading")
A simple example of printing the subjects of all messages in a mailbox that seem interesting:
Copy```
import mailbox
for message in mailbox.mbox('~/mbox'):
    subject = message['subject']       # Could possibly be None.
    if subject and 'python' in subject.lower():
        print(subject)

```

To copy all mail from a Babyl mailbox to an MH mailbox, converting all of the format-specific information that can be converted:
Copy```
import mailbox
destination = mailbox.MH('~/Mail')
destination.lock()
for message in mailbox.Babyl('~/RMAIL'):
    destination.add(mailbox.MHMessage(message))
destination.flush()
destination.unlock()

```

This example sorts mail from several mailing lists into different mailboxes, being careful to avoid mail corruption due to concurrent modification by other programs, mail loss due to interruption of the program, or premature termination due to malformed messages in the mailbox:
