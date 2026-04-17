[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html)
    * [Functions](https://docs.python.org/3/library/winreg.html#functions)
    * [Constants](https://docs.python.org/3/library/winreg.html#constants)
      * [HKEY_* Constants](https://docs.python.org/3/library/winreg.html#hkey-constants)
      * [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights)
        * [64-bit Specific](https://docs.python.org/3/library/winreg.html#bit-specific)
      * [Value Types](https://docs.python.org/3/library/winreg.html#value-types)
    * [Registry Handle Objects](https://docs.python.org/3/library/winreg.html#registry-handle-objects)


#### Previous topic
[`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html "previous chapter")
#### Next topic
[`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=winreg+%E2%80%94+Windows+registry+access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwinreg.html&pagesource=library%2Fwinreg.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/winsound.html "winsound — Sound-playing interface for Windows") |
  * [previous](https://docs.python.org/3/library/msvcrt.html "msvcrt — Useful routines from the MS VC++ runtime") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [MS Windows Specific Services](https://docs.python.org/3/library/windows.html) »
  * [`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html)
  * |
  * Theme  Auto Light Dark |


#  `winreg` — Windows registry access[¶](https://docs.python.org/3/library/winreg.html#module-winreg "Link to this heading")
* * *
These functions expose the Windows registry API to Python. Instead of using an integer as the registry handle, a [handle object](https://docs.python.org/3/library/winreg.html#handle-object) is used to ensure that the handles are closed correctly, even if the programmer neglects to explicitly close them.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Changed in version 3.3: Several functions in this module used to raise a [`WindowsError`](https://docs.python.org/3/library/exceptions.html#WindowsError "WindowsError"), which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
## Functions[¶](https://docs.python.org/3/library/winreg.html#functions "Link to this heading")
This module offers the following functions:

winreg.CloseKey(_hkey_)[¶](https://docs.python.org/3/library/winreg.html#winreg.CloseKey "Link to this definition")

Closes a previously opened registry key. The _hkey_ argument specifies a previously opened key.
Note
If _hkey_ is not closed using this method (or via [`hkey.Close()`](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.Close "winreg.PyHKEY.Close")), it is closed when the _hkey_ object is destroyed by Python.

winreg.ConnectRegistry(_computer_name_ , _key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.ConnectRegistry "Link to this definition")

Establishes a connection to a predefined registry handle on another computer, and returns a [handle object](https://docs.python.org/3/library/winreg.html#handle-object).
_computer_name_ is the name of the remote computer, of the form `r"\\computername"`. If `None`, the local computer is used.
_key_ is the predefined handle to connect to.
The return value is the handle of the opened key. If the function fails, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.ConnectRegistry` with arguments `computer_name`, `key`.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.CreateKey(_key_ , _sub_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.CreateKey "Link to this definition")

Creates or opens the specified key, returning a [handle object](https://docs.python.org/3/library/winreg.html#handle-object).
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that names the key this method opens or creates.
If _key_ is one of the predefined keys, _sub_key_ may be `None`. In that case, the handle returned is the same key handle passed in to the function.
If the key already exists, this function opens the existing key.
The return value is the handle of the opened key. If the function fails, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.CreateKey` with arguments `key`, `sub_key`, `access`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.OpenKey/result` with argument `key`.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.CreateKeyEx(_key_ , _sub_key_ , _reserved =0_, _access =KEY_WRITE_)[¶](https://docs.python.org/3/library/winreg.html#winreg.CreateKeyEx "Link to this definition")

Creates or opens the specified key, returning a [handle object](https://docs.python.org/3/library/winreg.html#handle-object).
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that names the key this method opens or creates.
_reserved_ is a reserved integer, and must be zero. The default is zero.
_access_ is an integer that specifies an access mask that describes the desired security access for the key. Default is [`KEY_WRITE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_WRITE "winreg.KEY_WRITE"). See [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights) for other allowed values.
If _key_ is one of the predefined keys, _sub_key_ may be `None`. In that case, the handle returned is the same key handle passed in to the function.
If the key already exists, this function opens the existing key.
The return value is the handle of the opened key. If the function fails, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.CreateKey` with arguments `key`, `sub_key`, `access`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.OpenKey/result` with argument `key`.
Added in version 3.2.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.DeleteKey(_key_ , _sub_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.DeleteKey "Link to this definition")

Deletes the specified key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that must be a subkey of the key identified by the _key_ parameter. This value must not be `None`, and the key may not have subkeys.
_This method can not delete keys with subkeys._
If the method succeeds, the entire key, including all of its values, is removed. If the method fails, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.DeleteKey` with arguments `key`, `sub_key`, `access`.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.DeleteKeyEx(_key_ , _sub_key_ , _access =KEY_WOW64_64KEY_, _reserved =0_)[¶](https://docs.python.org/3/library/winreg.html#winreg.DeleteKeyEx "Link to this definition")

Deletes the specified key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that must be a subkey of the key identified by the _key_ parameter. This value must not be `None`, and the key may not have subkeys.
_reserved_ is a reserved integer, and must be zero. The default is zero.
_access_ is an integer that specifies an access mask that describes the desired security access for the key. Default is [`KEY_WOW64_64KEY`](https://docs.python.org/3/library/winreg.html#winreg.KEY_WOW64_64KEY "winreg.KEY_WOW64_64KEY"). On 32-bit Windows, the WOW64 constants are ignored. See [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights) for other allowed values.
_This method can not delete keys with subkeys._
If the method succeeds, the entire key, including all of its values, is removed. If the method fails, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised.
On unsupported Windows versions, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.DeleteKey` with arguments `key`, `sub_key`, `access`.
Added in version 3.2.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.DeleteValue(_key_ , _value_)[¶](https://docs.python.org/3/library/winreg.html#winreg.DeleteValue "Link to this definition")

Removes a named value from a registry key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_value_ is a string that identifies the value to remove.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.DeleteValue` with arguments `key`, `value`.

winreg.EnumKey(_key_ , _index_)[¶](https://docs.python.org/3/library/winreg.html#winreg.EnumKey "Link to this definition")

Enumerates subkeys of an open registry key, returning a string.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_index_ is an integer that identifies the index of the key to retrieve.
The function retrieves the name of one subkey each time it is called. It is typically called repeatedly until an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised, indicating, no more values are available.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.EnumKey` with arguments `key`, `index`.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.EnumValue(_key_ , _index_)[¶](https://docs.python.org/3/library/winreg.html#winreg.EnumValue "Link to this definition")

Enumerates values of an open registry key, returning a tuple.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_index_ is an integer that identifies the index of the value to retrieve.
The function retrieves the name of one subkey each time it is called. It is typically called repeatedly, until an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception is raised, indicating no more values.
The result is a tuple of 3 items:
Index | Meaning
---|---
`0` | A string that identifies the value name
`1` | An object that holds the value data, and whose type depends on the underlying registry type
`2` | An integer that identifies the type of the value data (see table in docs for [`SetValueEx()`](https://docs.python.org/3/library/winreg.html#winreg.SetValueEx "winreg.SetValueEx"))
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.EnumValue` with arguments `key`, `index`.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.ExpandEnvironmentStrings(_str_)[¶](https://docs.python.org/3/library/winreg.html#winreg.ExpandEnvironmentStrings "Link to this definition")

Expands environment variable placeholders `%NAME%` in strings like [`REG_EXPAND_SZ`](https://docs.python.org/3/library/winreg.html#winreg.REG_EXPAND_SZ "winreg.REG_EXPAND_SZ"):
Copy```
>>> ExpandEnvironmentStrings('%windir%')
'C:\\Windows'

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.ExpandEnvironmentStrings` with argument `str`.

winreg.FlushKey(_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.FlushKey "Link to this definition")

Writes all the attributes of a key to the registry.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
It is not necessary to call `FlushKey()` to change a key. Registry changes are flushed to disk by the registry using its lazy flusher. Registry changes are also flushed to disk at system shutdown. Unlike [`CloseKey()`](https://docs.python.org/3/library/winreg.html#winreg.CloseKey "winreg.CloseKey"), the `FlushKey()` method returns only when all the data has been written to the registry. An application should only call `FlushKey()` if it requires absolute certainty that registry changes are on disk.
Note
If you don’t know whether a `FlushKey()` call is required, it probably isn’t.

winreg.LoadKey(_key_ , _sub_key_ , _file_name_)[¶](https://docs.python.org/3/library/winreg.html#winreg.LoadKey "Link to this definition")

Creates a subkey under the specified key and stores registration information from a specified file into that subkey.
_key_ is a handle returned by [`ConnectRegistry()`](https://docs.python.org/3/library/winreg.html#winreg.ConnectRegistry "winreg.ConnectRegistry") or one of the constants [`HKEY_USERS`](https://docs.python.org/3/library/winreg.html#winreg.HKEY_USERS "winreg.HKEY_USERS") or [`HKEY_LOCAL_MACHINE`](https://docs.python.org/3/library/winreg.html#winreg.HKEY_LOCAL_MACHINE "winreg.HKEY_LOCAL_MACHINE").
_sub_key_ is a string that identifies the subkey to load.
_file_name_ is the name of the file to load registry data from. This file must have been created with the [`SaveKey()`](https://docs.python.org/3/library/winreg.html#winreg.SaveKey "winreg.SaveKey") function. Under the file allocation table (FAT) file system, the filename may not have an extension.
A call to `LoadKey()` fails if the calling process does not have the `SE_RESTORE_PRIVILEGE` privilege. Note that privileges are different from permissions – see the
If _key_ is a handle returned by [`ConnectRegistry()`](https://docs.python.org/3/library/winreg.html#winreg.ConnectRegistry "winreg.ConnectRegistry"), then the path specified in _file_name_ is relative to the remote computer.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.LoadKey` with arguments `key`, `sub_key`, `file_name`.

winreg.OpenKey(_key_ , _sub_key_ , _reserved =0_, _access =KEY_READ_)[¶](https://docs.python.org/3/library/winreg.html#winreg.OpenKey "Link to this definition")


winreg.OpenKeyEx(_key_ , _sub_key_ , _reserved =0_, _access =KEY_READ_)[¶](https://docs.python.org/3/library/winreg.html#winreg.OpenKeyEx "Link to this definition")

Opens the specified key, returning a [handle object](https://docs.python.org/3/library/winreg.html#handle-object).
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that identifies the sub_key to open.
_reserved_ is a reserved integer, and must be zero. The default is zero.
_access_ is an integer that specifies an access mask that describes the desired security access for the key. Default is [`KEY_READ`](https://docs.python.org/3/library/winreg.html#winreg.KEY_READ "winreg.KEY_READ"). See [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights) for other allowed values.
The result is a new handle to the specified key.
If the function fails, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.OpenKey` with arguments `key`, `sub_key`, `access`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.OpenKey/result` with argument `key`.
Changed in version 3.2: Allow the use of named arguments.
Changed in version 3.3: See [above](https://docs.python.org/3/library/winreg.html#exception-changed).

winreg.QueryInfoKey(_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.QueryInfoKey "Link to this definition")

Returns information about a key, as a tuple.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
The result is a tuple of 3 items:
Index | Meaning
---|---
`0` | An integer giving the number of sub keys this key has.
`1` | An integer giving the number of values this key has.
`2` | An integer giving when the key was last modified (if available) as 100’s of nanoseconds since Jan 1, 1601.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.QueryInfoKey` with argument `key`.

winreg.QueryValue(_key_ , _sub_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.QueryValue "Link to this definition")

Retrieves the unnamed value for a key, as a string.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that holds the name of the subkey with which the value is associated. If this parameter is `None` or empty, the function retrieves the value set by the [`SetValue()`](https://docs.python.org/3/library/winreg.html#winreg.SetValue "winreg.SetValue") method for the key identified by _key_.
Values in the registry have name, type, and data components. This method retrieves the data for a key’s first value that has a `NULL` name. But the underlying API call doesn’t return the type, so always use [`QueryValueEx()`](https://docs.python.org/3/library/winreg.html#winreg.QueryValueEx "winreg.QueryValueEx") if possible.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.QueryValue` with arguments `key`, `sub_key`, `value_name`.

winreg.QueryValueEx(_key_ , _value_name_)[¶](https://docs.python.org/3/library/winreg.html#winreg.QueryValueEx "Link to this definition")

Retrieves the type and data for a specified value name associated with an open registry key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_value_name_ is a string indicating the value to query.
The result is a tuple of 2 items:
Index | Meaning
---|---
`0` | The value of the registry item.
`1` | An integer giving the registry type for this value (see table in docs for [`SetValueEx()`](https://docs.python.org/3/library/winreg.html#winreg.SetValueEx "winreg.SetValueEx"))
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.QueryValue` with arguments `key`, `sub_key`, `value_name`.

winreg.SaveKey(_key_ , _file_name_)[¶](https://docs.python.org/3/library/winreg.html#winreg.SaveKey "Link to this definition")

Saves the specified key, and all its subkeys to the specified file.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_file_name_ is the name of the file to save registry data to. This file cannot already exist. If this filename includes an extension, it cannot be used on file allocation table (FAT) file systems by the [`LoadKey()`](https://docs.python.org/3/library/winreg.html#winreg.LoadKey "winreg.LoadKey") method.
If _key_ represents a key on a remote computer, the path described by _file_name_ is relative to the remote computer. The caller of this method must possess the **SeBackupPrivilege** security privilege. Note that privileges are different than permissions – see the
This function passes `NULL` for _security_attributes_ to the API.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.SaveKey` with arguments `key`, `file_name`.

winreg.SetValue(_key_ , _sub_key_ , _type_ , _value_)[¶](https://docs.python.org/3/library/winreg.html#winreg.SetValue "Link to this definition")

Associates a value with a specified key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_sub_key_ is a string that names the subkey with which the value is associated.
_type_ is an integer that specifies the type of the data. Currently this must be [`REG_SZ`](https://docs.python.org/3/library/winreg.html#winreg.REG_SZ "winreg.REG_SZ"), meaning only strings are supported. Use the [`SetValueEx()`](https://docs.python.org/3/library/winreg.html#winreg.SetValueEx "winreg.SetValueEx") function for support for other data types.
_value_ is a string that specifies the new value.
If the key specified by the _sub_key_ parameter does not exist, the SetValue function creates it.
Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.
The key identified by the _key_ parameter must have been opened with [`KEY_SET_VALUE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_SET_VALUE "winreg.KEY_SET_VALUE") access.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.SetValue` with arguments `key`, `sub_key`, `type`, `value`.

winreg.SetValueEx(_key_ , _value_name_ , _reserved_ , _type_ , _value_)[¶](https://docs.python.org/3/library/winreg.html#winreg.SetValueEx "Link to this definition")

Stores data in the value field of an open registry key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
_value_name_ is a string that names the subkey with which the value is associated.
_reserved_ can be anything – zero is always passed to the API.
_type_ is an integer that specifies the type of the data. See [Value Types](https://docs.python.org/3/library/winreg.html#value-types) for the available types.
_value_ is a string that specifies the new value.
This method can also set additional value and type information for the specified key. The key identified by the key parameter must have been opened with [`KEY_SET_VALUE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_SET_VALUE "winreg.KEY_SET_VALUE") access.
To open the key, use the [`CreateKey()`](https://docs.python.org/3/library/winreg.html#winreg.CreateKey "winreg.CreateKey") or [`OpenKey()`](https://docs.python.org/3/library/winreg.html#winreg.OpenKey "winreg.OpenKey") methods.
Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.SetValue` with arguments `key`, `sub_key`, `type`, `value`.

winreg.DisableReflectionKey(_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.DisableReflectionKey "Link to this definition")

Disables registry reflection for 32-bit processes running on a 64-bit operating system.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
Will generally raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if executed on a 32-bit operating system.
If the key is not on the reflection list, the function succeeds but has no effect. Disabling reflection for a key does not affect reflection of any subkeys.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.DisableReflectionKey` with argument `key`.

winreg.EnableReflectionKey(_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.EnableReflectionKey "Link to this definition")

Restores registry reflection for the specified disabled key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
Will generally raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if executed on a 32-bit operating system.
Restoring reflection for a key does not affect reflection of any subkeys.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.EnableReflectionKey` with argument `key`.

winreg.QueryReflectionKey(_key_)[¶](https://docs.python.org/3/library/winreg.html#winreg.QueryReflectionKey "Link to this definition")

Determines the reflection state for the specified key.
_key_ is an already open key, or one of the predefined [HKEY_* constants](https://docs.python.org/3/library/winreg.html#hkey-constants).
Returns `True` if reflection is disabled.
Will generally raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if executed on a 32-bit operating system.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.QueryReflectionKey` with argument `key`.
## Constants[¶](https://docs.python.org/3/library/winreg.html#constants "Link to this heading")
The following constants are defined for use in many `winreg` functions.
### HKEY_* Constants[¶](https://docs.python.org/3/library/winreg.html#hkey-constants "Link to this heading")

winreg.HKEY_CLASSES_ROOT[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_CLASSES_ROOT "Link to this definition")

Registry entries subordinate to this key define types (or classes) of documents and the properties associated with those types. Shell and COM applications use the information stored under this key.

winreg.HKEY_CURRENT_USER[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_CURRENT_USER "Link to this definition")

Registry entries subordinate to this key define the preferences of the current user. These preferences include the settings of environment variables, data about program groups, colors, printers, network connections, and application preferences.

winreg.HKEY_LOCAL_MACHINE[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_LOCAL_MACHINE "Link to this definition")

Registry entries subordinate to this key define the physical state of the computer, including data about the bus type, system memory, and installed hardware and software.

winreg.HKEY_USERS[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_USERS "Link to this definition")

Registry entries subordinate to this key define the default user configuration for new users on the local computer and the user configuration for the current user.

winreg.HKEY_PERFORMANCE_DATA[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_PERFORMANCE_DATA "Link to this definition")

Registry entries subordinate to this key allow you to access performance data. The data is not actually stored in the registry; the registry functions cause the system to collect the data from its source.

winreg.HKEY_CURRENT_CONFIG[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_CURRENT_CONFIG "Link to this definition")

Contains information about the current hardware profile of the local computer system.

winreg.HKEY_DYN_DATA[¶](https://docs.python.org/3/library/winreg.html#winreg.HKEY_DYN_DATA "Link to this definition")

This key is not used in versions of Windows after 98.
### Access Rights[¶](https://docs.python.org/3/library/winreg.html#access-rights "Link to this heading")
For more information, see

winreg.KEY_ALL_ACCESS[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_ALL_ACCESS "Link to this definition")

Combines the STANDARD_RIGHTS_REQUIRED, [`KEY_QUERY_VALUE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_QUERY_VALUE "winreg.KEY_QUERY_VALUE"), [`KEY_SET_VALUE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_SET_VALUE "winreg.KEY_SET_VALUE"), [`KEY_CREATE_SUB_KEY`](https://docs.python.org/3/library/winreg.html#winreg.KEY_CREATE_SUB_KEY "winreg.KEY_CREATE_SUB_KEY"), [`KEY_ENUMERATE_SUB_KEYS`](https://docs.python.org/3/library/winreg.html#winreg.KEY_ENUMERATE_SUB_KEYS "winreg.KEY_ENUMERATE_SUB_KEYS"), [`KEY_NOTIFY`](https://docs.python.org/3/library/winreg.html#winreg.KEY_NOTIFY "winreg.KEY_NOTIFY"), and [`KEY_CREATE_LINK`](https://docs.python.org/3/library/winreg.html#winreg.KEY_CREATE_LINK "winreg.KEY_CREATE_LINK") access rights.

winreg.KEY_WRITE[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_WRITE "Link to this definition")

Combines the STANDARD_RIGHTS_WRITE, [`KEY_SET_VALUE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_SET_VALUE "winreg.KEY_SET_VALUE"), and [`KEY_CREATE_SUB_KEY`](https://docs.python.org/3/library/winreg.html#winreg.KEY_CREATE_SUB_KEY "winreg.KEY_CREATE_SUB_KEY") access rights.

winreg.KEY_READ[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_READ "Link to this definition")

Combines the STANDARD_RIGHTS_READ, [`KEY_QUERY_VALUE`](https://docs.python.org/3/library/winreg.html#winreg.KEY_QUERY_VALUE "winreg.KEY_QUERY_VALUE"), [`KEY_ENUMERATE_SUB_KEYS`](https://docs.python.org/3/library/winreg.html#winreg.KEY_ENUMERATE_SUB_KEYS "winreg.KEY_ENUMERATE_SUB_KEYS"), and [`KEY_NOTIFY`](https://docs.python.org/3/library/winreg.html#winreg.KEY_NOTIFY "winreg.KEY_NOTIFY") values.

winreg.KEY_EXECUTE[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_EXECUTE "Link to this definition")

Equivalent to [`KEY_READ`](https://docs.python.org/3/library/winreg.html#winreg.KEY_READ "winreg.KEY_READ").

winreg.KEY_QUERY_VALUE[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_QUERY_VALUE "Link to this definition")

Required to query the values of a registry key.

winreg.KEY_SET_VALUE[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_SET_VALUE "Link to this definition")

Required to create, delete, or set a registry value.

winreg.KEY_CREATE_SUB_KEY[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_CREATE_SUB_KEY "Link to this definition")

Required to create a subkey of a registry key.

winreg.KEY_ENUMERATE_SUB_KEYS[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_ENUMERATE_SUB_KEYS "Link to this definition")

Required to enumerate the subkeys of a registry key.

winreg.KEY_NOTIFY[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_NOTIFY "Link to this definition")

Required to request change notifications for a registry key or for subkeys of a registry key.

winreg.KEY_CREATE_LINK[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_CREATE_LINK "Link to this definition")

Reserved for system use.
#### 64-bit Specific[¶](https://docs.python.org/3/library/winreg.html#bit-specific "Link to this heading")
For more information, see

winreg.KEY_WOW64_64KEY[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_WOW64_64KEY "Link to this definition")

Indicates that an application on 64-bit Windows should operate on the 64-bit registry view. On 32-bit Windows, this constant is ignored.

winreg.KEY_WOW64_32KEY[¶](https://docs.python.org/3/library/winreg.html#winreg.KEY_WOW64_32KEY "Link to this definition")

Indicates that an application on 64-bit Windows should operate on the 32-bit registry view. On 32-bit Windows, this constant is ignored.
### Value Types[¶](https://docs.python.org/3/library/winreg.html#value-types "Link to this heading")
For more information, see

winreg.REG_BINARY[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_BINARY "Link to this definition")

Binary data in any form.

winreg.REG_DWORD[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_DWORD "Link to this definition")

32-bit number.

winreg.REG_DWORD_LITTLE_ENDIAN[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_DWORD_LITTLE_ENDIAN "Link to this definition")

A 32-bit number in little-endian format. Equivalent to [`REG_DWORD`](https://docs.python.org/3/library/winreg.html#winreg.REG_DWORD "winreg.REG_DWORD").

winreg.REG_DWORD_BIG_ENDIAN[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_DWORD_BIG_ENDIAN "Link to this definition")

A 32-bit number in big-endian format.

winreg.REG_EXPAND_SZ[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_EXPAND_SZ "Link to this definition")

Null-terminated string containing references to environment variables (`%PATH%`).

winreg.REG_LINK[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_LINK "Link to this definition")

A Unicode symbolic link.

winreg.REG_MULTI_SZ[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_MULTI_SZ "Link to this definition")

A sequence of null-terminated strings, terminated by two null characters. (Python handles this termination automatically.)

winreg.REG_NONE[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_NONE "Link to this definition")

No defined value type.

winreg.REG_QWORD[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_QWORD "Link to this definition")

A 64-bit number.
Added in version 3.6.

winreg.REG_QWORD_LITTLE_ENDIAN[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_QWORD_LITTLE_ENDIAN "Link to this definition")

A 64-bit number in little-endian format. Equivalent to [`REG_QWORD`](https://docs.python.org/3/library/winreg.html#winreg.REG_QWORD "winreg.REG_QWORD").
Added in version 3.6.

winreg.REG_RESOURCE_LIST[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_RESOURCE_LIST "Link to this definition")

A device-driver resource list.

winreg.REG_FULL_RESOURCE_DESCRIPTOR[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_FULL_RESOURCE_DESCRIPTOR "Link to this definition")

A hardware setting.

winreg.REG_RESOURCE_REQUIREMENTS_LIST[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_RESOURCE_REQUIREMENTS_LIST "Link to this definition")

A hardware resource list.

winreg.REG_SZ[¶](https://docs.python.org/3/library/winreg.html#winreg.REG_SZ "Link to this definition")

A null-terminated string.
## Registry Handle Objects[¶](https://docs.python.org/3/library/winreg.html#registry-handle-objects "Link to this heading")
This object wraps a Windows HKEY object, automatically closing it when the object is destroyed. To guarantee cleanup, you can call either the [`Close()`](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.Close "winreg.PyHKEY.Close") method on the object, or the [`CloseKey()`](https://docs.python.org/3/library/winreg.html#winreg.CloseKey "winreg.CloseKey") function.
All registry functions in this module return one of these objects.
All registry functions in this module which accept a handle object also accept an integer, however, use of the handle object is encouraged.
Handle objects provide semantics for [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__") – thus
Copy```
if handle:
    print("Yes")

```

will print `Yes` if the handle is currently valid (has not been closed or detached).
Handle objects can be converted to an integer (e.g., using the built-in [`int()`](https://docs.python.org/3/library/functions.html#int "int") function), in which case the underlying Windows handle value is returned. You can also use the [`Detach()`](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.Detach "winreg.PyHKEY.Detach") method to return the integer handle, and also disconnect the Windows handle from the handle object.

PyHKEY.Close()[¶](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.Close "Link to this definition")

Closes the underlying Windows handle.
If the handle is already closed, no error is raised.

PyHKEY.Detach()[¶](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.Detach "Link to this definition")

Detaches the Windows handle from the handle object.
The result is an integer that holds the value of the handle before it is detached. If the handle is already detached or closed, this will return zero.
After calling this function, the handle is effectively invalidated, but the handle is not closed. You would call this function when you need the underlying Win32 handle to exist beyond the lifetime of the handle object.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `winreg.PyHKEY.Detach` with argument `key`.

PyHKEY.__enter__()[¶](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.__enter__ "Link to this definition")


PyHKEY.__exit__(_* exc_info_)[¶](https://docs.python.org/3/library/winreg.html#winreg.PyHKEY.__exit__ "Link to this definition")

The HKEY object implements [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") and thus supports the context protocol for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement:
Copy```
with OpenKey(HKEY_LOCAL_MACHINE, "foo") as key:
    ...  # work with key

```

will automatically close _key_ when control leaves the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) block.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html)
    * [Functions](https://docs.python.org/3/library/winreg.html#functions)
    * [Constants](https://docs.python.org/3/library/winreg.html#constants)
      * [HKEY_* Constants](https://docs.python.org/3/library/winreg.html#hkey-constants)
      * [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights)
        * [64-bit Specific](https://docs.python.org/3/library/winreg.html#bit-specific)
      * [Value Types](https://docs.python.org/3/library/winreg.html#value-types)
    * [Registry Handle Objects](https://docs.python.org/3/library/winreg.html#registry-handle-objects)


#### Previous topic
[`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html "previous chapter")
#### Next topic
[`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=winreg+%E2%80%94+Windows+registry+access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwinreg.html&pagesource=library%2Fwinreg.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/winsound.html "winsound — Sound-playing interface for Windows") |
  * [previous](https://docs.python.org/3/library/msvcrt.html "msvcrt — Useful routines from the MS VC++ runtime") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [MS Windows Specific Services](https://docs.python.org/3/library/windows.html) »
  * [`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
