[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`os.path` — Common pathname manipulations](https://docs.python.org/3/library/os.path.html "previous chapter")
#### Next topic
[`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=stat+%E2%80%94+Interpreting+stat%28%29+results&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstat.html&pagesource=library%2Fstat.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/filecmp.html "filecmp — File and Directory Comparisons") |
  * [previous](https://docs.python.org/3/library/os.path.html "os.path — Common pathname manipulations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html)
  * |
  * Theme  Auto Light Dark |


#  `stat` — Interpreting [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") results[¶](https://docs.python.org/3/library/stat.html#module-stat "Link to this heading")
**Source code:**
* * *
The `stat` module defines constants and functions for interpreting the results of [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"), [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat") and [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat") (if they exist). For complete details about the `stat()`, `fstat()` and `lstat()` calls, consult the documentation for your system.
Changed in version 3.4: The stat module is backed by a C implementation.
The `stat` module defines the following functions to test for specific file types:

stat.S_ISDIR(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISDIR "Link to this definition")

Return non-zero if the mode is from a directory.

stat.S_ISCHR(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISCHR "Link to this definition")

Return non-zero if the mode is from a character special device file.

stat.S_ISBLK(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISBLK "Link to this definition")

Return non-zero if the mode is from a block special device file.

stat.S_ISREG(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISREG "Link to this definition")

Return non-zero if the mode is from a regular file.

stat.S_ISFIFO(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISFIFO "Link to this definition")

Return non-zero if the mode is from a FIFO (named pipe).

stat.S_ISLNK(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISLNK "Link to this definition")

Return non-zero if the mode is from a symbolic link.

stat.S_ISSOCK(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISSOCK "Link to this definition")

Return non-zero if the mode is from a socket.

stat.S_ISDOOR(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISDOOR "Link to this definition")

Return non-zero if the mode is from a door.
Added in version 3.4.

stat.S_ISPORT(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISPORT "Link to this definition")

Return non-zero if the mode is from an event port.
Added in version 3.4.

stat.S_ISWHT(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_ISWHT "Link to this definition")

Return non-zero if the mode is from a whiteout.
Added in version 3.4.
Two additional functions are defined for more general manipulation of the file’s mode:

stat.S_IMODE(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_IMODE "Link to this definition")

Return the portion of the file’s mode that can be set by [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")—that is, the file’s permission bits, plus the sticky bit, set-group-id, and set-user-id bits (on systems that support them).

stat.S_IFMT(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.S_IFMT "Link to this definition")

Return the portion of the file’s mode that describes the file type (used by the `S_IS*()` functions above).
Normally, you would use the `os.path.is*()` functions for testing the type of a file; the functions here are useful when you are doing multiple tests of the same file and wish to avoid the overhead of the `stat()` system call for each test. These are also useful when checking for information about a file that isn’t handled by [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames."), like the tests for block and character devices.
Example:
Copy```
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)

```

An additional utility function is provided to convert a file’s mode in a human readable string:

stat.filemode(_mode_)[¶](https://docs.python.org/3/library/stat.html#stat.filemode "Link to this definition")

Convert a file’s mode to a string of the form ‘-rwxrwxrwx’.
Added in version 3.3.
Changed in version 3.4: The function supports [`S_IFDOOR`](https://docs.python.org/3/library/stat.html#stat.S_IFDOOR "stat.S_IFDOOR"), [`S_IFPORT`](https://docs.python.org/3/library/stat.html#stat.S_IFPORT "stat.S_IFPORT") and [`S_IFWHT`](https://docs.python.org/3/library/stat.html#stat.S_IFWHT "stat.S_IFWHT").
All the variables below are simply symbolic indexes into the 10-tuple returned by [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"), [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat") or [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat").

stat.ST_MODE[¶](https://docs.python.org/3/library/stat.html#stat.ST_MODE "Link to this definition")

Inode protection mode.

stat.ST_INO[¶](https://docs.python.org/3/library/stat.html#stat.ST_INO "Link to this definition")

Inode number.

stat.ST_DEV[¶](https://docs.python.org/3/library/stat.html#stat.ST_DEV "Link to this definition")

Device inode resides on.

stat.ST_NLINK[¶](https://docs.python.org/3/library/stat.html#stat.ST_NLINK "Link to this definition")

Number of links to the inode.

stat.ST_UID[¶](https://docs.python.org/3/library/stat.html#stat.ST_UID "Link to this definition")

User id of the owner.

stat.ST_GID[¶](https://docs.python.org/3/library/stat.html#stat.ST_GID "Link to this definition")

Group id of the owner.

stat.ST_SIZE[¶](https://docs.python.org/3/library/stat.html#stat.ST_SIZE "Link to this definition")

Size in bytes of a plain file; amount of data waiting on some special files.

stat.ST_ATIME[¶](https://docs.python.org/3/library/stat.html#stat.ST_ATIME "Link to this definition")

Time of last access.

stat.ST_MTIME[¶](https://docs.python.org/3/library/stat.html#stat.ST_MTIME "Link to this definition")

Time of last modification.

stat.ST_CTIME[¶](https://docs.python.org/3/library/stat.html#stat.ST_CTIME "Link to this definition")

The “ctime” as reported by the operating system. On some systems (like Unix) is the time of the last metadata change, and, on others (like Windows), is the creation time (see platform documentation for details).
The interpretation of “file size” changes according to the file type. For plain files this is the size of the file in bytes. For FIFOs and sockets under most flavors of Unix (including Linux in particular), the “size” is the number of bytes waiting to be read at the time of the call to [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"), [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat"), or [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat"); this can sometimes be useful, especially for polling one of these special files after a non-blocking open. The meaning of the size field for other character and block devices varies more, depending on the implementation of the underlying system call.
The variables below define the flags used in the [`ST_MODE`](https://docs.python.org/3/library/stat.html#stat.ST_MODE "stat.ST_MODE") field.
Use of the functions above is more portable than use of the first set of flags:

stat.S_IFSOCK[¶](https://docs.python.org/3/library/stat.html#stat.S_IFSOCK "Link to this definition")

Socket.

stat.S_IFLNK[¶](https://docs.python.org/3/library/stat.html#stat.S_IFLNK "Link to this definition")

Symbolic link.

stat.S_IFREG[¶](https://docs.python.org/3/library/stat.html#stat.S_IFREG "Link to this definition")

Regular file.

stat.S_IFBLK[¶](https://docs.python.org/3/library/stat.html#stat.S_IFBLK "Link to this definition")

Block device.

stat.S_IFDIR[¶](https://docs.python.org/3/library/stat.html#stat.S_IFDIR "Link to this definition")

Directory.

stat.S_IFCHR[¶](https://docs.python.org/3/library/stat.html#stat.S_IFCHR "Link to this definition")

Character device.

stat.S_IFIFO[¶](https://docs.python.org/3/library/stat.html#stat.S_IFIFO "Link to this definition")

FIFO.

stat.S_IFDOOR[¶](https://docs.python.org/3/library/stat.html#stat.S_IFDOOR "Link to this definition")

Door.
Added in version 3.4.

stat.S_IFPORT[¶](https://docs.python.org/3/library/stat.html#stat.S_IFPORT "Link to this definition")

Event port.
Added in version 3.4.

stat.S_IFWHT[¶](https://docs.python.org/3/library/stat.html#stat.S_IFWHT "Link to this definition")

Whiteout.
Added in version 3.4.
Note
[`S_IFDOOR`](https://docs.python.org/3/library/stat.html#stat.S_IFDOOR "stat.S_IFDOOR"), [`S_IFPORT`](https://docs.python.org/3/library/stat.html#stat.S_IFPORT "stat.S_IFPORT") or [`S_IFWHT`](https://docs.python.org/3/library/stat.html#stat.S_IFWHT "stat.S_IFWHT") are defined as 0 when the platform does not have support for the file types.
The following flags can also be used in the _mode_ argument of [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod"):

stat.S_ISUID[¶](https://docs.python.org/3/library/stat.html#stat.S_ISUID "Link to this definition")

Set UID bit.

stat.S_ISGID[¶](https://docs.python.org/3/library/stat.html#stat.S_ISGID "Link to this definition")

Set-group-ID bit. This bit has several special uses. For a directory it indicates that BSD semantics is to be used for that directory: files created there inherit their group ID from the directory, not from the effective group ID of the creating process, and directories created there will also get the `S_ISGID` bit set. For a file that does not have the group execution bit ([`S_IXGRP`](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "stat.S_IXGRP")) set, the set-group-ID bit indicates mandatory file/record locking (see also [`S_ENFMT`](https://docs.python.org/3/library/stat.html#stat.S_ENFMT "stat.S_ENFMT")).

stat.S_ISVTX[¶](https://docs.python.org/3/library/stat.html#stat.S_ISVTX "Link to this definition")

Sticky bit. When this bit is set on a directory it means that a file in that directory can be renamed or deleted only by the owner of the file, by the owner of the directory, or by a privileged process.

stat.S_IRWXU[¶](https://docs.python.org/3/library/stat.html#stat.S_IRWXU "Link to this definition")

Mask for file owner permissions.

stat.S_IRUSR[¶](https://docs.python.org/3/library/stat.html#stat.S_IRUSR "Link to this definition")

Owner has read permission.

stat.S_IWUSR[¶](https://docs.python.org/3/library/stat.html#stat.S_IWUSR "Link to this definition")

Owner has write permission.

stat.S_IXUSR[¶](https://docs.python.org/3/library/stat.html#stat.S_IXUSR "Link to this definition")

Owner has execute permission.

stat.S_IRWXG[¶](https://docs.python.org/3/library/stat.html#stat.S_IRWXG "Link to this definition")

Mask for group permissions.

stat.S_IRGRP[¶](https://docs.python.org/3/library/stat.html#stat.S_IRGRP "Link to this definition")

Group has read permission.

stat.S_IWGRP[¶](https://docs.python.org/3/library/stat.html#stat.S_IWGRP "Link to this definition")

Group has write permission.

stat.S_IXGRP[¶](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "Link to this definition")

Group has execute permission.

stat.S_IRWXO[¶](https://docs.python.org/3/library/stat.html#stat.S_IRWXO "Link to this definition")

Mask for permissions for others (not in group).

stat.S_IROTH[¶](https://docs.python.org/3/library/stat.html#stat.S_IROTH "Link to this definition")

Others have read permission.

stat.S_IWOTH[¶](https://docs.python.org/3/library/stat.html#stat.S_IWOTH "Link to this definition")

Others have write permission.

stat.S_IXOTH[¶](https://docs.python.org/3/library/stat.html#stat.S_IXOTH "Link to this definition")

Others have execute permission.

stat.S_ENFMT[¶](https://docs.python.org/3/library/stat.html#stat.S_ENFMT "Link to this definition")

System V file locking enforcement. This flag is shared with [`S_ISGID`](https://docs.python.org/3/library/stat.html#stat.S_ISGID "stat.S_ISGID"): file/record locking is enforced on files that do not have the group execution bit ([`S_IXGRP`](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "stat.S_IXGRP")) set.

stat.S_IREAD[¶](https://docs.python.org/3/library/stat.html#stat.S_IREAD "Link to this definition")

Unix V7 synonym for [`S_IRUSR`](https://docs.python.org/3/library/stat.html#stat.S_IRUSR "stat.S_IRUSR").

stat.S_IWRITE[¶](https://docs.python.org/3/library/stat.html#stat.S_IWRITE "Link to this definition")

Unix V7 synonym for [`S_IWUSR`](https://docs.python.org/3/library/stat.html#stat.S_IWUSR "stat.S_IWUSR").

stat.S_IEXEC[¶](https://docs.python.org/3/library/stat.html#stat.S_IEXEC "Link to this definition")

Unix V7 synonym for [`S_IXUSR`](https://docs.python.org/3/library/stat.html#stat.S_IXUSR "stat.S_IXUSR").
The following flags can be used in the _flags_ argument of [`os.chflags()`](https://docs.python.org/3/library/os.html#os.chflags "os.chflags"):

stat.UF_SETTABLE[¶](https://docs.python.org/3/library/stat.html#stat.UF_SETTABLE "Link to this definition")

All user settable flags.
Added in version 3.13.

stat.UF_NODUMP[¶](https://docs.python.org/3/library/stat.html#stat.UF_NODUMP "Link to this definition")

Do not dump the file.

stat.UF_IMMUTABLE[¶](https://docs.python.org/3/library/stat.html#stat.UF_IMMUTABLE "Link to this definition")

The file may not be changed.

stat.UF_APPEND[¶](https://docs.python.org/3/library/stat.html#stat.UF_APPEND "Link to this definition")

The file may only be appended to.

stat.UF_OPAQUE[¶](https://docs.python.org/3/library/stat.html#stat.UF_OPAQUE "Link to this definition")

The directory is opaque when viewed through a union stack.

stat.UF_NOUNLINK[¶](https://docs.python.org/3/library/stat.html#stat.UF_NOUNLINK "Link to this definition")

The file may not be renamed or deleted.

stat.UF_COMPRESSED[¶](https://docs.python.org/3/library/stat.html#stat.UF_COMPRESSED "Link to this definition")

The file is stored compressed (macOS 10.6+).

stat.UF_TRACKED[¶](https://docs.python.org/3/library/stat.html#stat.UF_TRACKED "Link to this definition")

Used for handling document IDs (macOS)
Added in version 3.13.

stat.UF_DATAVAULT[¶](https://docs.python.org/3/library/stat.html#stat.UF_DATAVAULT "Link to this definition")

The file needs an entitlement for reading or writing (macOS 10.13+)
Added in version 3.13.

stat.UF_HIDDEN[¶](https://docs.python.org/3/library/stat.html#stat.UF_HIDDEN "Link to this definition")

The file should not be displayed in a GUI (macOS 10.5+).

stat.SF_SETTABLE[¶](https://docs.python.org/3/library/stat.html#stat.SF_SETTABLE "Link to this definition")

All super-user changeable flags
Added in version 3.13.

stat.SF_SUPPORTED[¶](https://docs.python.org/3/library/stat.html#stat.SF_SUPPORTED "Link to this definition")

All super-user supported flags
[Availability](https://docs.python.org/3/library/intro.html#availability): macOS
Added in version 3.13.

stat.SF_SYNTHETIC[¶](https://docs.python.org/3/library/stat.html#stat.SF_SYNTHETIC "Link to this definition")

All super-user read-only synthetic flags
[Availability](https://docs.python.org/3/library/intro.html#availability): macOS
Added in version 3.13.

stat.SF_ARCHIVED[¶](https://docs.python.org/3/library/stat.html#stat.SF_ARCHIVED "Link to this definition")

The file may be archived.

stat.SF_IMMUTABLE[¶](https://docs.python.org/3/library/stat.html#stat.SF_IMMUTABLE "Link to this definition")

The file may not be changed.

stat.SF_APPEND[¶](https://docs.python.org/3/library/stat.html#stat.SF_APPEND "Link to this definition")

The file may only be appended to.

stat.SF_RESTRICTED[¶](https://docs.python.org/3/library/stat.html#stat.SF_RESTRICTED "Link to this definition")

The file needs an entitlement to write to (macOS 10.13+)
Added in version 3.13.

stat.SF_NOUNLINK[¶](https://docs.python.org/3/library/stat.html#stat.SF_NOUNLINK "Link to this definition")

The file may not be renamed or deleted.

stat.SF_SNAPSHOT[¶](https://docs.python.org/3/library/stat.html#stat.SF_SNAPSHOT "Link to this definition")

The file is a snapshot file.

stat.SF_FIRMLINK[¶](https://docs.python.org/3/library/stat.html#stat.SF_FIRMLINK "Link to this definition")

The file is a firmlink (macOS 10.15+)
Added in version 3.13.

stat.SF_DATALESS[¶](https://docs.python.org/3/library/stat.html#stat.SF_DATALESS "Link to this definition")

The file is a dataless object (macOS 10.15+)
Added in version 3.13.
See the *BSD or macOS systems man page
On Windows, the following file attribute constants are available for use when testing bits in the `st_file_attributes` member returned by [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"). See the

stat.FILE_ATTRIBUTE_ARCHIVE[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_ARCHIVE "Link to this definition")


stat.FILE_ATTRIBUTE_COMPRESSED[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_COMPRESSED "Link to this definition")


stat.FILE_ATTRIBUTE_DEVICE[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_DEVICE "Link to this definition")


stat.FILE_ATTRIBUTE_DIRECTORY[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_DIRECTORY "Link to this definition")


stat.FILE_ATTRIBUTE_ENCRYPTED[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_ENCRYPTED "Link to this definition")


stat.FILE_ATTRIBUTE_HIDDEN[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_HIDDEN "Link to this definition")


stat.FILE_ATTRIBUTE_INTEGRITY_STREAM[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_INTEGRITY_STREAM "Link to this definition")


stat.FILE_ATTRIBUTE_NORMAL[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_NORMAL "Link to this definition")


stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED "Link to this definition")


stat.FILE_ATTRIBUTE_NO_SCRUB_DATA[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_NO_SCRUB_DATA "Link to this definition")


stat.FILE_ATTRIBUTE_OFFLINE[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_OFFLINE "Link to this definition")


stat.FILE_ATTRIBUTE_READONLY[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_READONLY "Link to this definition")


stat.FILE_ATTRIBUTE_REPARSE_POINT[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_REPARSE_POINT "Link to this definition")


stat.FILE_ATTRIBUTE_SPARSE_FILE[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_SPARSE_FILE "Link to this definition")


stat.FILE_ATTRIBUTE_SYSTEM[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_SYSTEM "Link to this definition")


stat.FILE_ATTRIBUTE_TEMPORARY[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_TEMPORARY "Link to this definition")


stat.FILE_ATTRIBUTE_VIRTUAL[¶](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_VIRTUAL "Link to this definition")

Added in version 3.5.
On Windows, the following constants are available for comparing against the `st_reparse_tag` member returned by [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat"). These are well-known constants, but are not an exhaustive list.

stat.IO_REPARSE_TAG_SYMLINK[¶](https://docs.python.org/3/library/stat.html#stat.IO_REPARSE_TAG_SYMLINK "Link to this definition")


stat.IO_REPARSE_TAG_MOUNT_POINT[¶](https://docs.python.org/3/library/stat.html#stat.IO_REPARSE_TAG_MOUNT_POINT "Link to this definition")


stat.IO_REPARSE_TAG_APPEXECLINK[¶](https://docs.python.org/3/library/stat.html#stat.IO_REPARSE_TAG_APPEXECLINK "Link to this definition")

Added in version 3.8.
#### Previous topic
[`os.path` — Common pathname manipulations](https://docs.python.org/3/library/os.path.html "previous chapter")
#### Next topic
[`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=stat+%E2%80%94+Interpreting+stat%28%29+results&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstat.html&pagesource=library%2Fstat.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/filecmp.html "filecmp — File and Directory Comparisons") |
  * [previous](https://docs.python.org/3/library/os.path.html "os.path — Common pathname manipulations") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
