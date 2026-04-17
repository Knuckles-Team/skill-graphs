##  `Mailbox` objects[¶](https://docs.python.org/3/library/mailbox.html#mailbox-objects "Link to this heading")

_class_ mailbox.Mailbox[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "Link to this definition")

A mailbox, which may be inspected and modified.
The `Mailbox` class defines an interface and is not intended to be instantiated. Instead, format-specific subclasses should inherit from `Mailbox` and your code should instantiate a particular subclass.
The `Mailbox` interface is dictionary-like, with small keys corresponding to messages. Keys are issued by the `Mailbox` instance with which they will be used and are only meaningful to that `Mailbox` instance. A key continues to identify a message even if the corresponding message is modified, such as by replacing it with another message.
Messages may be added to a `Mailbox` instance using the set-like method [`add()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.add "mailbox.Mailbox.add") and removed using a `del` statement or the set-like methods [`remove()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.remove "mailbox.Mailbox.remove") and [`discard()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.discard "mailbox.Mailbox.discard").
`Mailbox` interface semantics differ from dictionary semantics in some noteworthy ways. Each time a message is requested, a new representation (typically a [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") instance) is generated based upon the current state of the mailbox. Similarly, when a message is added to a `Mailbox` instance, the provided message representation’s contents are copied. In neither case is a reference to the message representation kept by the `Mailbox` instance.
The default `Mailbox` [iterator](https://docs.python.org/3/glossary.html#term-iterator) iterates over message representations, not keys as the default [`dictionary`](https://docs.python.org/3/library/stdtypes.html#dict "dict") iterator does. Moreover, modification of a mailbox during iteration is safe and well-defined. Messages added to the mailbox after an iterator is created will not be seen by the iterator. Messages removed from the mailbox before the iterator yields them will be silently skipped, though using a key from an iterator may result in a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception if the corresponding message is subsequently removed.
Warning
Be very cautious when modifying mailboxes that might be simultaneously changed by some other process. The safest mailbox format to use for such tasks is [`Maildir`](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir "mailbox.Maildir"); try to avoid using single-file formats such as [`mbox`](https://docs.python.org/3/library/mailbox.html#mailbox.mbox "mailbox.mbox") for concurrent writing. If you’re modifying a mailbox, you _must_ lock it by calling the [`lock()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.lock "mailbox.Mailbox.lock") and [`unlock()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.unlock "mailbox.Mailbox.unlock") methods _before_ reading any messages in the file or making any changes by adding or deleting a message. Failing to lock the mailbox runs the risk of losing messages or corrupting the entire mailbox.
`Mailbox` instances have the following methods:

add(_message_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.add "Link to this definition")

Add _message_ to the mailbox and return the key that has been assigned to it.
Parameter _message_ may be a [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") instance, an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") instance, a string, a byte string, or a file-like object (which should be open in binary mode). If _message_ is an instance of the appropriate format-specific `Message` subclass (e.g., if it’s an [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") instance and this is an [`mbox`](https://docs.python.org/3/library/mailbox.html#mailbox.mbox "mailbox.mbox") instance), its format-specific information is used. Otherwise, reasonable defaults for format-specific information are used.
Changed in version 3.2: Support for binary input was added.

remove(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.remove "Link to this definition")


__delitem__(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__delitem__ "Link to this definition")


discard(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.discard "Link to this definition")

Delete the message corresponding to _key_ from the mailbox.
If no such message exists, a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception is raised if the method was called as `remove()` or `__delitem__()` but no exception is raised if the method was called as `discard()`. The behavior of `discard()` may be preferred if the underlying mailbox format supports concurrent modification by other processes.

__setitem__(_key_ , _message_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__setitem__ "Link to this definition")

Replace the message corresponding to _key_ with _message_. Raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception if no message already corresponds to _key_.
As with [`add()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.add "mailbox.Mailbox.add"), parameter _message_ may be a [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") instance, an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") instance, a string, a byte string, or a file-like object (which should be open in binary mode). If _message_ is an instance of the appropriate format-specific `Message` subclass (e.g., if it’s an [`mboxMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage "mailbox.mboxMessage") instance and this is an [`mbox`](https://docs.python.org/3/library/mailbox.html#mailbox.mbox "mailbox.mbox") instance), its format-specific information is used. Otherwise, the format-specific information of the message that currently corresponds to _key_ is left unchanged.

iterkeys()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.iterkeys "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) over all keys

keys()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.keys "Link to this definition")

The same as [`iterkeys()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.iterkeys "mailbox.Mailbox.iterkeys"), except that a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") is returned rather than an [iterator](https://docs.python.org/3/glossary.html#term-iterator)

itervalues()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.itervalues "Link to this definition")


__iter__()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__iter__ "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) over representations of all messages. The messages are represented as instances of the appropriate format-specific [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified when the `Mailbox` instance was initialized.
Note
The behavior of `__iter__()` is unlike that of dictionaries, which iterate over keys.

values()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.values "Link to this definition")

The same as [`itervalues()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.itervalues "mailbox.Mailbox.itervalues"), except that a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") is returned rather than an [iterator](https://docs.python.org/3/glossary.html#term-iterator)

iteritems()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.iteritems "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) over (_key_ , _message_) pairs, where _key_ is a key and _message_ is a message representation. The messages are represented as instances of the appropriate format-specific [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified when the `Mailbox` instance was initialized.

items()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.items "Link to this definition")

The same as [`iteritems()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.iteritems "mailbox.Mailbox.iteritems"), except that a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of pairs is returned rather than an [iterator](https://docs.python.org/3/glossary.html#term-iterator) of pairs.

get(_key_ , _default =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get "Link to this definition")


__getitem__(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__getitem__ "Link to this definition")

Return a representation of the message corresponding to _key_. If no such message exists, _default_ is returned if the method was called as `get()` and a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception is raised if the method was called as `__getitem__()`. The message is represented as an instance of the appropriate format-specific [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified when the `Mailbox` instance was initialized.

get_message(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_message "Link to this definition")

Return a representation of the message corresponding to _key_ as an instance of the appropriate format-specific [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") subclass, or raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception if no such message exists.

get_bytes(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_bytes "Link to this definition")

Return a byte representation of the message corresponding to _key_ , or raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception if no such message exists.
Added in version 3.2.

get_string(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_string "Link to this definition")

Return a string representation of the message corresponding to _key_ , or raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception if no such message exists. The message is processed through [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") to convert it to a 7bit clean representation.

get_file(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_file "Link to this definition")

Return a [file-like](https://docs.python.org/3/glossary.html#term-file-like-object) representation of the message corresponding to _key_ , or raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception if no such message exists. The file-like object behaves as if open in binary mode. This file should be closed once it is no longer needed.
Changed in version 3.2: The file object really is a [binary file](https://docs.python.org/3/glossary.html#term-binary-file); previously it was incorrectly returned in text mode. Also, the [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) now supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol: you can use a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement to automatically close it.
Note
Unlike other representations of messages, [file-like](https://docs.python.org/3/glossary.html#term-file-like-object) representations are not necessarily independent of the `Mailbox` instance that created them or of the underlying mailbox. More specific documentation is provided by each subclass.

__contains__(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__contains__ "Link to this definition")

Return `True` if _key_ corresponds to a message, `False` otherwise.

__len__()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__len__ "Link to this definition")

Return a count of messages in the mailbox.

clear()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.clear "Link to this definition")

Delete all messages from the mailbox.

pop(_key_ , _default =None_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.pop "Link to this definition")

Return a representation of the message corresponding to _key_ and delete the message. If no such message exists, return _default_. The message is represented as an instance of the appropriate format-specific [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified when the `Mailbox` instance was initialized.

popitem()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.popitem "Link to this definition")

Return an arbitrary (_key_ , _message_) pair, where _key_ is a key and _message_ is a message representation, and delete the corresponding message. If the mailbox is empty, raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception. The message is represented as an instance of the appropriate format-specific [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message") subclass unless a custom message factory was specified when the `Mailbox` instance was initialized.

update(_arg_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.update "Link to this definition")

Parameter _arg_ should be a _key_ -to-_message_ mapping or an iterable of (_key_ , _message_) pairs. Updates the mailbox so that, for each given _key_ and _message_ , the message corresponding to _key_ is set to _message_ as if by using [`__setitem__()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.__setitem__ "mailbox.Mailbox.__setitem__"). As with `__setitem__()`, each _key_ must already correspond to a message in the mailbox or else a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception will be raised, so in general it is incorrect for _arg_ to be a `Mailbox` instance.
Note
Unlike with dictionaries, keyword arguments are not supported.

flush()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.flush "Link to this definition")

Write any pending changes to the filesystem. For some `Mailbox` subclasses, changes are always written immediately and `flush()` does nothing, but you should still make a habit of calling this method.

lock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.lock "Link to this definition")

Acquire an exclusive advisory lock on the mailbox so that other processes know not to modify it. An [`ExternalClashError`](https://docs.python.org/3/library/mailbox.html#mailbox.ExternalClashError "mailbox.ExternalClashError") is raised if the lock is not available. The particular locking mechanisms used depend upon the mailbox format. You should _always_ lock the mailbox before making any modifications to its contents.

unlock()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.unlock "Link to this definition")

Release the lock on the mailbox, if any.

close()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.close "Link to this definition")

Flush the mailbox, unlock it if necessary, and close any open files. For some `Mailbox` subclasses, this method does nothing.
###  `Maildir` objects[¶](https://docs.python.org/3/library/mailbox.html#maildir-objects "Link to this heading")

_class_ mailbox.Maildir(_dirname_ , _factory =None_, _create =True_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir "Link to this definition")

A subclass of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") for mailboxes in Maildir format. Parameter _factory_ is a callable object that accepts a file-like message representation (which behaves as if opened in binary mode) and returns a custom representation. If _factory_ is `None`, [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") is used as the default message representation. If _create_ is `True`, the mailbox is created if it does not exist.
If _create_ is `True` and the _dirname_ path exists, it will be treated as an existing maildir without attempting to verify its directory layout.
It is for historical reasons that _dirname_ is named as such rather than _path_.
Maildir is a directory-based mailbox format invented for the qmail mail transfer agent and now widely supported by other programs. Messages in a Maildir mailbox are stored in separate files within a common directory structure. This design allows Maildir mailboxes to be accessed and modified by multiple unrelated programs without data corruption, so file locking is unnecessary.
Maildir mailboxes contain three subdirectories, namely: `tmp`, `new`, and `cur`. Messages are created momentarily in the `tmp` subdirectory and then moved to the `new` subdirectory to finalize delivery. A mail user agent may subsequently move the message to the `cur` subdirectory and store information about the state of the message in a special “info” section appended to its file name.
Folders of the style introduced by the Courier mail transfer agent are also supported. Any subdirectory of the main mailbox is considered a folder if `'.'` is the first character in its name. Folder names are represented by `Maildir` without the leading `'.'`. Each folder is itself a Maildir mailbox but should not contain other folders. Instead, a logical nesting is indicated using `'.'` to delimit levels, e.g., “Archived.2005.07”.

colon[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.colon "Link to this definition")

The Maildir specification requires the use of a colon (`':'`) in certain message file names. However, some operating systems do not permit this character in file names, If you wish to use a Maildir-like format on such an operating system, you should specify another character to use instead. The exclamation point (`'!'`) is a popular choice. For example:
Copy```
import mailbox
mailbox.Maildir.colon = '!'

```

The `colon` attribute may also be set on a per-instance basis.
Changed in version 3.13: `Maildir` now ignores files with a leading dot.
`Maildir` instances have all of the methods of [`Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox") in addition to the following:

list_folders()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.list_folders "Link to this definition")

Return a list of the names of all folders.

get_folder(_folder_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.get_folder "Link to this definition")

Return a `Maildir` instance representing the folder whose name is _folder_. A [`NoSuchMailboxError`](https://docs.python.org/3/library/mailbox.html#mailbox.NoSuchMailboxError "mailbox.NoSuchMailboxError") exception is raised if the folder does not exist.

add_folder(_folder_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.add_folder "Link to this definition")

Create a folder whose name is _folder_ and return a `Maildir` instance representing it.

remove_folder(_folder_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.remove_folder "Link to this definition")

Delete the folder whose name is _folder_. If the folder contains any messages, a [`NotEmptyError`](https://docs.python.org/3/library/mailbox.html#mailbox.NotEmptyError "mailbox.NotEmptyError") exception will be raised and the folder will not be deleted.

clean()[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.clean "Link to this definition")

Delete temporary files from the mailbox that have not been accessed in the last 36 hours. The Maildir specification says that mail-reading programs should do this occasionally.

get_flags(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.get_flags "Link to this definition")

Return as a string the flags that are set on the message corresponding to _key_. This is the same as `get_message(key).get_flags()` but much faster, because it does not open the message file. Use this method when iterating over the keys to determine which messages are interesting to get.
If you do have a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use its [`get_flags()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_flags "mailbox.MaildirMessage.get_flags") method instead, because changes made by the message’s [`set_flags()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_flags "mailbox.MaildirMessage.set_flags"), [`add_flag()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.add_flag "mailbox.MaildirMessage.add_flag") and [`remove_flag()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.remove_flag "mailbox.MaildirMessage.remove_flag") methods are not reflected here until the mailbox’s [`__setitem__()`](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.__setitem__ "mailbox.Maildir.__setitem__") method is called.
Added in version 3.13.

set_flags(_key_ , _flags_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.set_flags "Link to this definition")

On the message corresponding to _key_ , set the flags specified by _flags_ and unset all others. Calling `some_mailbox.set_flags(key, flags)` is similar to
Copy```
one_message = some_mailbox.get_message(key)
one_message.set_flags(flags)
some_mailbox[key] = one_message

```

but faster, because it does not open the message file.
If you do have a [`MaildirMessage`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage "mailbox.MaildirMessage") object, use its [`set_flags()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.set_flags "mailbox.MaildirMessage.set_flags") method instead, because changes made with this mailbox method will not be visible to the message object’s method, [`get_flags()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.get_flags "mailbox.MaildirMessage.get_flags").
Added in version 3.13.

add_flag(_key_ , _flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.add_flag "Link to this definition")

On the message corresponding to _key_ , set the flags specified by _flag_ without changing other flags. To add more than one flag at a time, _flag_ may be a string of more than one character.
Considerations for using this method versus the message object’s [`add_flag()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.add_flag "mailbox.MaildirMessage.add_flag") method are similar to those for [`set_flags()`](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.set_flags "mailbox.Maildir.set_flags"); see the discussion there.
Added in version 3.13.

remove_flag(_key_ , _flag_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.remove_flag "Link to this definition")

On the message corresponding to _key_ , unset the flags specified by _flag_ without changing other flags. To remove more than one flag at a time, _flag_ may be a string of more than one character.
Considerations for using this method versus the message object’s [`remove_flag()`](https://docs.python.org/3/library/mailbox.html#mailbox.MaildirMessage.remove_flag "mailbox.MaildirMessage.remove_flag") method are similar to those for [`set_flags()`](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.set_flags "mailbox.Maildir.set_flags"); see the discussion there.
Added in version 3.13.

get_info(_key_)[¶](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir.get_info "Link to this definition")

Return a string containing the info for the message corresponding to _key_. This is the same as `get_message(key).get_info()` but much faster, because it does not open the message file. Use this method when iterating over the keys to determine which messages are interesting to get.
