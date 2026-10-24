If you do have a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use its [`get_info()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_info "mailbox.MaildirMessage.get_info") method instead, because changes made by the message’s [`set_info()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_info "mailbox.MaildirMessage.set_info") method are not reflected here until the mailbox’s [`__setitem__()`](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.__setitem__ "mailbox.Maildir.__setitem__") method is called.
Added in version 3.13.

set_info(_key_ , _info_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.set_info "Link to this definition")

Set the info of the message corresponding to _key_ to _info_. Calling `some_mailbox.set_info(key, flags)` is similar to
Copy```
one_message = some_mailbox.get_message(key)
one_message.set_info(info)
some_mailbox[key] = one_message

```

but faster, because it does not open the message file.
If you do have a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use its [`set_info()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_info "mailbox.MaildirMessage.set_info") method instead, because changes made with this mailbox method will not be visible to the message object’s method, [`get_info()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_info "mailbox.MaildirMessage.get_info").
Added in version 3.13.
Some [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `Maildir` deserve special remarks:

add(_message_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.add "Link to this definition")


__setitem__(_key_ , _message_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.__setitem__ "Link to this definition")


update(_arg_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.update "Link to this definition")

Warning
These methods generate unique file names based upon the current process ID. When using multiple threads, undetected name clashes may occur and cause corruption of the mailbox unless threads are coordinated to avoid using these methods to manipulate the same mailbox simultaneously.

flush()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.flush "Link to this definition")

All changes to Maildir mailboxes are immediately applied, so this method does nothing.

lock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.lock "Link to this definition")


unlock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.unlock "Link to this definition")

Maildir mailboxes do not support (or require) locking, so these methods do nothing.

close()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.close "Link to this definition")

`Maildir` instances do not keep any open files and the underlying mailboxes do not support locking, so this method does nothing.

get_file(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.get_file "Link to this definition")

Depending upon the host platform, it may not be possible to modify or remove the underlying message while the returned file remains open.
See also
A specification of the format. Describes a common extension for supporting folders.
Notes on Maildir by its inventor. Includes an updated name-creation scheme and details on “info” semantics.
###  `mbox` objects[¶](https://docs.python.org/3/library/mailbox.html#mbox-objects "Link to this heading")

_class_ mailbox.mbox(_path_ , _factory =None_, _create =True_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mbox "Link to this definition")

A subclass of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in mbox format. Parameter _factory_ is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If _factory_ is `None`, [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") is used as the default message representation. If _create_ is `True`, the mailbox is created if it does not exist.
The mbox format is the classic format for storing mail on Unix systems. All messages in an mbox mailbox are stored in a single file with the beginning of each message indicated by a line whose first five characters are “From “.
Several variations of the mbox format exist to address perceived shortcomings in the original. In the interest of compatibility, `mbox` implements the original format, which is sometimes referred to as _mboxo_. This means that the _Content-Length_ header, if present, is ignored and that any occurrences of “From “ at the beginning of a line in a message body are transformed to “>From “ when storing the message, although occurrences of “>From “ are not transformed to “From “ when reading the message.
Some [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `mbox` deserve special remarks:

get_bytes(_key_ , _from_ =False_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mbox.get_bytes "Link to this definition")

Note: This method has an extra parameter (_from__) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If _from__ is False, the first line of the file is dropped.

get_file(_key_ , _from_ =False_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mbox.get_file "Link to this definition")

Using the file after calling [`flush()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.flush "mailbox.Mailbox.flush") or [`close()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.close "mailbox.Mailbox.close") on the `mbox` instance may yield unpredictable results or raise an exception.
Note: This method has an extra parameter (_from__) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If _from__ is False, the first line of the file is dropped.

get_string(_key_ , _from_ =False_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mbox.get_string "Link to this definition")

Note: This method has an extra parameter (_from__) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If _from__ is False, the first line of the file is dropped.

lock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mbox.lock "Link to this definition")


unlock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.mbox.unlock "Link to this definition")

Three locking mechanisms are used—dot locking and, if available, the `flock()` and `lockf()` system calls.
See also
A specification of the format, with details on locking.
An argument for using the original mbox format rather than a variation.
A history of mbox variations.
###  `MH` objects[¶](https://docs.python.org/3/library/mailbox.html#mh-objects "Link to this heading")

_class_ mailbox.MH(_path_ , _factory =None_, _create =True_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH "Link to this definition")

A subclass of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in MH format. Parameter _factory_ is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If _factory_ is `None`, [`MHMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MHMessage "mailbox.MHMessage") is used as the default message representation. If _create_ is `True`, the mailbox is created if it does not exist.
MH is a directory-based mailbox format invented for the MH Message Handling System, a mail user agent. Each message in an MH mailbox resides in its own file. An MH mailbox may contain other MH mailboxes (called _folders_) in addition to messages. Folders may be nested indefinitely. MH mailboxes also support _sequences_ , which are named lists used to logically group messages without moving them to sub-folders. Sequences are defined in a file called `.mh_sequences` in each folder.
The `MH` class manipulates MH mailboxes, but it does not attempt to emulate all of **mh** ’s behaviors. In particular, it does not modify and is not affected by the `context` or `.mh_profile` files that are used by **mh** to store its state and configuration.
`MH` instances have all of the methods of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") in addition to the following:
Changed in version 3.13: Supported folders that don’t contain a `.mh_sequences` file.

list_folders()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.list_folders "Link to this definition")

Return a list of the names of all folders.

get_folder(_folder_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.get_folder "Link to this definition")

Return an `MH` instance representing the folder whose name is _folder_. A [`NoSuchMailboxError`](https://docs.python.org/3/library/mailbox.html#mailbox.NoSuchMailboxError "mailbox.NoSuchMailboxError") exception is raised if the folder does not exist.

add_folder(_folder_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.add_folder "Link to this definition")

Create a folder whose name is _folder_ and return an `MH` instance representing it.

remove_folder(_folder_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.remove_folder "Link to this definition")

Delete the folder whose name is _folder_. If the folder contains any messages, a [`NotEmptyError`](https://docs.python.org/3/library/mailbox.html#mailbox.NotEmptyError "mailbox.NotEmptyError") exception will be raised and the folder will not be deleted.

get_sequences()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.get_sequences "Link to this definition")

Return a dictionary of sequence names mapped to key lists. If there are no sequences, the empty dictionary is returned.

set_sequences(_sequences_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.set_sequences "Link to this definition")

Re-define the sequences that exist in the mailbox based upon _sequences_ , a dictionary of names mapped to key lists, like returned by [`get_sequences()`](https://docs.python.org/3/library/mailbox.html#mailbox.MH.get_sequences "mailbox.MH.get_sequences").

pack()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.pack "Link to this definition")

Rename messages in the mailbox as necessary to eliminate gaps in numbering. Entries in the sequences list are updated correspondingly.
Note
Already-issued keys are invalidated by this operation and should not be subsequently used.
Some [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `MH` deserve special remarks:

remove(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.remove "Link to this definition")


__delitem__(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.__delitem__ "Link to this definition")


discard(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.discard "Link to this definition")

These methods immediately delete the message. The MH convention of marking a message for deletion by prepending a comma to its name is not used.

lock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.lock "Link to this definition")


unlock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.unlock "Link to this definition")

Three locking mechanisms are used—dot locking and, if available, the `flock()` and `lockf()` system calls. For MH mailboxes, locking the mailbox means locking the `.mh_sequences` file and, only for the duration of any operations that affect them, locking individual message files.

get_file(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.get_file "Link to this definition")

Depending upon the host platform, it may not be possible to remove the underlying message while the returned file remains open.

flush()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.flush "Link to this definition")

All changes to MH mailboxes are immediately applied, so this method does nothing.

close()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MH.close "Link to this definition")

`MH` instances do not keep any open files, so this method is equivalent to [`unlock()`](https://docs.python.org/3/library/mailbox.html#mailbox.MH.unlock "mailbox.MH.unlock").
See also
Home page of **nmh** , an updated version of the original **mh**.
A GPL-licensed book on **mh** and **nmh** , with some information on the mailbox format.
###  `Babyl` objects[¶](https://docs.python.org/3/library/mailbox.html#babyl-objects "Link to this heading")

_class_ mailbox.Babyl(_path_ , _factory =None_, _create =True_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Babyl "Link to this definition")

A subclass of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in Babyl format. Parameter _factory_ is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If _factory_ is `None`, [`BabylMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.BabylMessage "mailbox.BabylMessage") is used as the default message representation. If _create_ is `True`, the mailbox is created if it does not exist.
Babyl is a single-file mailbox format used by the Rmail mail user agent included with Emacs. The beginning of a message is indicated by a line containing the two characters Control-Underscore (`'\037'`) and Control-L (`'\014'`). The end of a message is indicated by the start of the next message or, in the case of the last message, a line containing a Control-Underscore (`'\037'`) character.
Messages in a Babyl mailbox have two sets of headers, original headers and so-called visible headers. Visible headers are typically a subset of the original headers that have been reformatted or abridged to be more attractive. Each message in a Babyl mailbox also has an accompanying list of _labels_ , or short strings that record extra information about the message, and a list of all user-defined labels found in the mailbox is kept in the Babyl options section.
`Babyl` instances have all of the methods of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") in addition to the following:

get_labels()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Babyl.get_labels "Link to this definition")

Return a list of the names of all user-defined labels used in the mailbox.
Note
The actual messages are inspected to determine which labels exist in the mailbox rather than consulting the list of labels in the Babyl options section, but the Babyl section is updated whenever the mailbox is modified.
Some [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `Babyl` deserve special remarks:

get_file(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Babyl.get_file "Link to this definition")

In Babyl mailboxes, the headers of a message are not stored contiguously with the body of the message. To generate a file-like representation, the headers and body are copied together into an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") instance, which has an API identical to that of a file. As a result, the file-like object is truly independent of the underlying mailbox but does not save memory compared to a string representation.

lock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Babyl.lock "Link to this definition")


unlock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Babyl.unlock "Link to this definition")

Three locking mechanisms are used—dot locking and, if available, the `flock()` and `lockf()` system calls.
See also
A specification of the Babyl format.
The Rmail manual, with some information on Babyl semantics.
###  `MMDF` objects[¶](https://docs.python.org/3/library/mailbox.html#mmdf-objects "Link to this heading")

_class_ mailbox.MMDF(_path_ , _factory =None_, _create =True_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDF "Link to this definition")

A subclass of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in MMDF format. Parameter _factory_ is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If _factory_ is `None`, [`MMDFMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MMDFMessage "mailbox.MMDFMessage") is used as the default message representation. If _create_ is `True`, the mailbox is created if it does not exist.
MMDF is a single-file mailbox format invented for the Multichannel Memorandum Distribution Facility, a mail transfer agent. Each message is in the same form as an mbox message but is bracketed before and after by lines containing four Control-A (`'\001'`) characters. As with the mbox format, the beginning of each message is indicated by a line whose first five characters are “From “, but additional occurrences of “From “ are not transformed to “>From “ when storing messages because the extra message separator lines prevent mistaking such occurrences for the starts of subsequent messages.
Some [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") methods implemented by `MMDF` deserve special remarks:

get_bytes(_key_ , _from_ =False_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDF.get_bytes "Link to this definition")

Note: This method has an extra parameter (_from__) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If _from__ is False, the first line of the file is dropped.

get_file(_key_ , _from_ =False_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDF.get_file "Link to this definition")

Using the file after calling [`flush()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.flush "mailbox.Mailbox.flush") or [`close()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.close "mailbox.Mailbox.close") on the `MMDF` instance may yield unpredictable results or raise an exception.
Note: This method has an extra parameter (_from__) compared with other classes. The first line of an mbox file entry is the Unix “From “ line. If _from__ is False, the first line of the file is dropped.

lock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDF.lock "Link to this definition")


unlock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MMDF.unlock "Link to this definition")

Three locking mechanisms are used—dot locking and, if available, the `flock()` and `lockf()` system calls.
See also
A specification of MMDF format from the documentation of tin, a newsreader.
A Wikipedia article describing the Multichannel Memorandum Distribution Facility.
##  `Message` objects[¶](https://docs.python.org/3/library/mailbox.html#message-objects "Link to this heading")

_class_ mailbox.Message(_message =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Message "Link to this definition")

A subclass of the [`email.message`](https://docs.python.org/3/library/email.message.html#module-email.message "email.message: The base class representing email messages.") module’s [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message"). Subclasses of `mailbox.Message` add mailbox-format-specific state and behavior.
If _message_ is omitted, the new instance is created in a default, empty state. If _message_ is an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") instance, its contents are copied; furthermore, any format-specific information is converted insofar as possible if _message_ is a `Message` instance. If _message_ is a string, a byte string, or a file, it should contain an
The format-specific state and behaviors offered by subclasses vary, but in general it is only the properties that are not specific to a particular mailbox that are supported (although presumably the properties are specific to a particular mailbox format). For example, file offsets for single-file mailbox formats and file names for directory-based mailbox formats are not retained, because they are only applicable to the original mailbox. But state such as whether a message has been read by the user or marked as important is retained, because it applies to the message itself.
There is no requirement that `Message` instances be used to represent messages retrieved using [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") instances. In some situations, the time and memory required to generate `Message` representations might not be acceptable. For such situations, `Mailbox` instances also offer string and file-like representations, and a custom message factory may be specified when a `Mailbox` instance is initialized.
###  `MaildirMessage` objects[¶](https://docs.python.org/3/library/mailbox.html#maildirmessage-objects "Link to this heading")

_class_ mailbox.MaildirMessage(_message =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "Link to this definition")

A message with Maildir-specific behaviors. Parameter _message_ has the same meaning as with the [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") constructor.
Typically, a mail user agent application moves all of the messages in the `new` subdirectory to the `cur` subdirectory after the first time the user opens and closes the mailbox, recording that the messages are old whether or not they’ve actually been read. Each message in `cur` has an “info” section added to its file name to store information about its state. (Some mail readers may also add an “info” section to messages in `new`.) The “info” section may take one of two forms: it may contain “2,” followed by a list of standardized flags (e.g., “2,FR”) or it may contain “1,” followed by so-called experimental information. Standard flags for Maildir messages are as follows:
Flag | Meaning | Explanation
---|---|---
D | Draft | Under composition
F | Flagged | Marked as important
P | Passed | Forwarded, resent, or bounced
R | Replied | Replied to
S | Seen | Read
T | Trashed | Marked for subsequent deletion
`MaildirMessage` instances offer the following methods:

get_subdir()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_subdir "Link to this definition")

Return either “new” (if the message should be stored in the `new` subdirectory) or “cur” (if the message should be stored in the `cur` subdirectory).
Note
A message is typically moved from `new` to `cur` after its mailbox has been accessed, whether or not the message has been read. A message `msg` has been read if `"S" in msg.get_flags()` is `True`.

set_subdir(_subdir_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_subdir "Link to this definition")

Set the subdirectory the message should be stored in. Parameter _subdir_ must be either “new” or “cur”.

get_flags()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_flags "Link to this definition")

Return a string specifying the flags that are currently set. If the message complies with the standard Maildir format, the result is the concatenation in alphabetical order of zero or one occurrence of each of `'D'`, `'F'`, `'P'`, `'R'`, `'S'`, and `'T'`. The empty string is returned if no flags are set or if “info” contains experimental semantics.

set_flags(_flags_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_flags "Link to this definition")

Set the flags specified by _flags_ and unset all others.

add_flag(_flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.add_flag "Link to this definition")

Set the flag(s) specified by _flag_ without changing other flags. To add more than one flag at a time, _flag_ may be a string of more than one character. The current “info” is overwritten whether or not it contains experimental information rather than flags.

remove_flag(_flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.remove_flag "Link to this definition")

Unset the flag(s) specified by _flag_ without changing other flags. To remove more than one flag at a time, _flag_ may be a string of more than one character. If “info” contains experimental information rather than flags, the current “info” is not modified.
