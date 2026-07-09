Constant | Description
---|---
`COPYFILE_EXCL` | If present, the copy operation will fail with an error if the destination path already exists.
`COPYFILE_FICLONE` | If present, the copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then a fallback copy mechanism is used.
`COPYFILE_FICLONE_FORCE` | If present, the copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then the operation will fail with an error.
The definitions are also available on Windows.
###### File open constants[#](https://nodejs.org/docs/latest/api/fs.html#file-open-constants)
The following constants are meant for use with `fs.open()`.
Constant | Description
---|---
`O_RDONLY` | Flag indicating to open a file for read-only access.
`O_WRONLY` | Flag indicating to open a file for write-only access.
`O_RDWR` | Flag indicating to open a file for read-write access.
`O_CREAT` | Flag indicating to create the file if it does not already exist.
`O_EXCL` | Flag indicating that opening a file should fail if the `O_CREAT` flag is set and the file already exists.
`O_NOCTTY` | Flag indicating that if path identifies a terminal device, opening the path shall not cause that terminal to become the controlling terminal for the process (if the process does not already have one).
`O_TRUNC` | Flag indicating that if the file exists and is a regular file, and the file is opened successfully for write access, its length shall be truncated to zero.
`O_APPEND` | Flag indicating that data will be appended to the end of the file.
`O_DIRECTORY` | Flag indicating that the open should fail if the path is not a directory.
`O_NOATIME` | Flag indicating reading accesses to the file system will no longer result in an update to the `atime` information associated with the file. This flag is available on Linux operating systems only.
`O_NOFOLLOW` | Flag indicating that the open should fail if the path is a symbolic link.
`O_SYNC` | Flag indicating that the file is opened for synchronized I/O with write operations waiting for file integrity.
`O_DSYNC` | Flag indicating that the file is opened for synchronized I/O with write operations waiting for data integrity.
`O_SYMLINK` | Flag indicating to open the symbolic link itself rather than the resource it is pointing to.
`O_DIRECT` | When set, an attempt will be made to minimize caching effects of file I/O.
`O_NONBLOCK` | Flag indicating to open the file in nonblocking mode when possible.
`UV_FS_O_FILEMAP` | When set, a memory file mapping is used to access the file. This flag is available on Windows operating systems only. On other operating systems, this flag is ignored.
On Windows, only `O_APPEND`, `O_CREAT`, `O_EXCL`, `O_RDONLY`, `O_RDWR`, `O_TRUNC`, `O_WRONLY`, and `UV_FS_O_FILEMAP` are available.
###### File type constants[#](https://nodejs.org/docs/latest/api/fs.html#file-type-constants)
The following constants are meant for use with the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object's `mode` property for determining a file's type.
Constant | Description
---|---
`S_IFMT` | Bit mask used to extract the file type code.
`S_IFREG` | File type constant for a regular file.
`S_IFDIR` | File type constant for a directory.
`S_IFCHR` | File type constant for a character-oriented device file.
`S_IFBLK` | File type constant for a block-oriented device file.
`S_IFIFO` | File type constant for a FIFO/pipe.
`S_IFLNK` | File type constant for a symbolic link.
`S_IFSOCK` | File type constant for a socket.
On Windows, only `S_IFCHR`, `S_IFDIR`, `S_IFLNK`, `S_IFMT`, and `S_IFREG`, are available.
###### File mode constants[#](https://nodejs.org/docs/latest/api/fs.html#file-mode-constants)
The following constants are meant for use with the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object's `mode` property for determining the access permissions for a file.
Constant | Description
---|---
`S_IRWXU` | File mode indicating readable, writable, and executable by owner.
`S_IRUSR` | File mode indicating readable by owner.
`S_IWUSR` | File mode indicating writable by owner.
`S_IXUSR` | File mode indicating executable by owner.
`S_IRWXG` | File mode indicating readable, writable, and executable by group.
`S_IRGRP` | File mode indicating readable by group.
`S_IWGRP` | File mode indicating writable by group.
`S_IXGRP` | File mode indicating executable by group.
`S_IRWXO` | File mode indicating readable, writable, and executable by others.
`S_IROTH` | File mode indicating readable by others.
`S_IWOTH` | File mode indicating writable by others.
`S_IXOTH` | File mode indicating executable by others.
On Windows, only `S_IRUSR` and `S_IWUSR` are available.
### Notes[#](https://nodejs.org/docs/latest/api/fs.html#notes)
#### Ordering of callback and promise-based operations[#](https://nodejs.org/docs/latest/api/fs.html#ordering-of-callback-and-promise-based-operations)
Because they are executed asynchronously by the underlying thread pool, there is no guaranteed ordering when using either the callback or promise-based methods.
For example, the following is prone to error because the `fs.stat()` operation might complete before the `fs.rename()` operation:
```
const fs = require('node:fs');

fs.rename('/tmp/hello', '/tmp/world', (err) => {
  if (err) throw err;
  console.log('renamed complete');
});
fs.stat('/tmp/world', (err, stats) => {
  if (err) throw err;
  console.log(`stats: ${JSON.stringify(stats)}`);
});
copy
```

It is important to correctly order the operations by awaiting the results of one before invoking the other:
```
import { rename, stat } from 'node:fs/promises';

const oldPath = '/tmp/hello';
const newPath = '/tmp/world';

try {
  await rename(oldPath, newPath);
  const stats = await stat(newPath);
  console.log(`stats: ${JSON.stringify(stats)}`);
} catch (error) {
  console.error('there was an error:', error.message);
}
const { rename, stat } = require('node:fs/promises');

(async function(oldPath, newPath) {
  try {
    await rename(oldPath, newPath);
    const stats = await stat(newPath);
    console.log(`stats: ${JSON.stringify(stats)}`);
  } catch (error) {
    console.error('there was an error:', error.message);
  }
})('/tmp/hello', '/tmp/world');
copy
```

Or, when using the callback APIs, move the `fs.stat()` call into the callback of the `fs.rename()` operation:
```
import { rename, stat } from 'node:fs';

rename('/tmp/hello', '/tmp/world', (err) => {
  if (err) throw err;
  stat('/tmp/world', (err, stats) => {
    if (err) throw err;
    console.log(`stats: ${JSON.stringify(stats)}`);
  });
});
const { rename, stat } = require('node:fs/promises');

rename('/tmp/hello', '/tmp/world', (err) => {
  if (err) throw err;
  stat('/tmp/world', (err, stats) => {
    if (err) throw err;
    console.log(`stats: ${JSON.stringify(stats)}`);
  });
});
copy
```

#### File paths[#](https://nodejs.org/docs/latest/api/fs.html#file-paths)
Most `fs` operations accept file paths that may be specified in the form of a string, a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), or a [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object using the `file:` protocol.
##### String paths[#](https://nodejs.org/docs/latest/api/fs.html#string-paths)
String paths are interpreted as UTF-8 character sequences identifying the absolute or relative filename. Relative paths will be resolved relative to the current working directory as determined by calling `process.cwd()`.
Example using an absolute path on POSIX:
```
import { open } from 'node:fs/promises';

let fd;
try {
  fd = await open('/open/some/file.txt', 'r');
  // Do something with the file
} finally {
  await fd?.close();
}
copy
```

Example using a relative path on POSIX (relative to `process.cwd()`):
```
import { open } from 'node:fs/promises';

let fd;
try {
  fd = await open('file.txt', 'r');
  // Do something with the file
} finally {
  await fd?.close();
}
copy
```

##### File URL paths[#](https://nodejs.org/docs/latest/api/fs.html#file-url-paths)
Added in: v7.6.0
For most `node:fs` module functions, the `path` or `filename` argument may be passed as a [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object using the `file:` protocol.
```
import { readFileSync } from 'node:fs';

readFileSync(new URL('file:///tmp/hello'));
copy
```

`file:` URLs are always absolute paths.
###### Platform-specific considerations[#](https://nodejs.org/docs/latest/api/fs.html#platform-specific-considerations)
On Windows, `file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)s with a host name convert to UNC paths, while `file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)s with drive letters convert to local absolute paths. `file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)s with no host name and no drive letter will result in an error:
```
import { readFileSync } from 'node:fs';
// On Windows :

// - WHATWG file URLs with hostname convert to UNC path
// file://hostname/p/a/t/h/file => \\hostname\p\a\t\h\file
readFileSync(new URL('file://hostname/p/a/t/h/file'));

// - WHATWG file URLs with drive letters convert to absolute path
// file:///C:/tmp/hello => C:\tmp\hello
readFileSync(new URL('file:///C:/tmp/hello'));

// - WHATWG file URLs without hostname must have a drive letters
readFileSync(new URL('file:///notdriveletter/p/a/t/h/file'));
readFileSync(new URL('file:///c/p/a/t/h/file'));
// TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must be absolute
copy
```

`file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)s with drive letters must use `:` as a separator just after the drive letter. Using another separator will result in an error.
On all other platforms, `file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)s with a host name are unsupported and will result in an error:
```
import { readFileSync } from 'node:fs';
// On other platforms:

// - WHATWG file URLs with hostname are unsupported
// file://hostname/p/a/t/h/file => throw!
readFileSync(new URL('file://hostname/p/a/t/h/file'));
// TypeError [ERR_INVALID_FILE_URL_PATH]: must be absolute

// - WHATWG file URLs convert to absolute path
// file:///tmp/hello => /tmp/hello
readFileSync(new URL('file:///tmp/hello'));
copy
```

A `file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) having encoded slash characters will result in an error on all platforms:
```
import { readFileSync } from 'node:fs';

// On Windows
readFileSync(new URL('file:///C:/p/a/t/h/%2F'));
readFileSync(new URL('file:///C:/p/a/t/h/%2f'));
/* TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must not include encoded
\ or / characters */

// On POSIX
readFileSync(new URL('file:///p/a/t/h/%2F'));
readFileSync(new URL('file:///p/a/t/h/%2f'));
/* TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must not include encoded
/ characters */
copy
```

On Windows, `file:` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)s having encoded backslash will result in an error:
```
import { readFileSync } from 'node:fs';

// On Windows
readFileSync(new URL('file:///C:/path/%5C'));
readFileSync(new URL('file:///C:/path/%5c'));
/* TypeError [ERR_INVALID_FILE_URL_PATH]: File URL path must not include encoded
\ or / characters */
copy
```

##### Buffer paths[#](https://nodejs.org/docs/latest/api/fs.html#buffer-paths)
Paths specified using a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) are useful primarily on certain POSIX operating systems that treat file paths as opaque byte sequences. On such systems, it is possible for a single file path to contain sub-sequences that use multiple character encodings. As with string paths, [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) paths may be relative or absolute:
Example using an absolute path on POSIX:
```
import { open } from 'node:fs/promises';
import { Buffer } from 'node:buffer';

let fd;
try {
  fd = await open(Buffer.from('/open/some/file.txt'), 'r');
  // Do something with the file
} finally {
  await fd?.close();
}
copy
```

##### Per-drive working directories on Windows[#](https://nodejs.org/docs/latest/api/fs.html#per-drive-working-directories-on-windows)
On Windows, Node.js follows the concept of per-drive working directory. This behavior can be observed when using a drive path without a backslash. For example `fs.readdirSync('C:\\')` can potentially return a different result than `fs.readdirSync('C:')`. For more information, see
#### File descriptors[#](https://nodejs.org/docs/latest/api/fs.html#file-descriptors-1)
On POSIX systems, for every process, the kernel maintains a table of currently open files and resources. Each open file is assigned a simple numeric identifier called a _file descriptor_. At the system-level, all file system operations use these file descriptors to identify and track each specific file. Windows systems use a different but conceptually similar mechanism for tracking resources. To simplify things for users, Node.js abstracts away the differences between operating systems and assigns all open files a numeric file descriptor.
The callback-based `fs.open()`, and synchronous `fs.openSync()` methods open a file and allocate a new file descriptor. Once allocated, the file descriptor may be used to read data from, write data to, or request information about the file.
Operating systems limit the number of file descriptors that may be open at any given time so it is critical to close the descriptor when operations are completed. Failure to do so will result in a memory leak that will eventually cause an application to crash.
```
import { open, close, fstat } from 'node:fs';

function closeFd(fd) {
  close(fd, (err) => {
    if (err) throw err;
  });
}

open('/open/some/file.txt', 'r', (err, fd) => {
  if (err) throw err;
  try {
    fstat(fd, (err, stat) => {
      if (err) {
        closeFd(fd);
        throw err;
      }

      // use stat

      closeFd(fd);
    });
  } catch (err) {
    closeFd(fd);
    throw err;
  }
});
copy
```

The promise-based APIs use a [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) object in place of the numeric file descriptor. These objects are better managed by the system to ensure that resources are not leaked. However, it is still required that they are closed when operations are completed:
```
import { open } from 'node:fs/promises';

let file;
try {
  file = await open('/open/some/file.txt', 'r');
  const stat = await file.stat();
  // use stat
} finally {
  await file.close();
}
copy
```

#### Threadpool usage[#](https://nodejs.org/docs/latest/api/fs.html#threadpool-usage)
All callback and promise-based file system APIs (with the exception of `fs.FSWatcher()`) use libuv's threadpool. This can have surprising and negative performance implications for some applications. See the [`UV_THREADPOOL_SIZE`](https://nodejs.org/docs/latest/api/cli.html#uv_threadpool_sizesize) documentation for more information.
#### File system flags[#](https://nodejs.org/docs/latest/api/fs.html#file-system-flags)
The following flags are available wherever the `flag` option takes a string.
  * `'a'`: Open file for appending. The file is created if it does not exist.
  * `'ax'`: Like `'a'` but fails if the path exists.
  * `'a+'`: Open file for reading and appending. The file is created if it does not exist.
  * `'ax+'`: Like `'a+'` but fails if the path exists.
  * `'as'`: Open file for appending in synchronous mode. The file is created if it does not exist.
  * `'as+'`: Open file for reading and appending in synchronous mode. The file is created if it does not exist.
  * `'r'`: Open file for reading. An exception occurs if the file does not exist.
  * `'rs'`: Open file for reading in synchronous mode. An exception occurs if the file does not exist.
  * `'r+'`: Open file for reading and writing. An exception occurs if the file does not exist.
  * `'rs+'`: Open file for reading and writing in synchronous mode. Instructs the operating system to bypass the local file system cache.
This is primarily useful for opening files on NFS mounts as it allows skipping the potentially stale local cache. It has a very real impact on I/O performance so using this flag is not recommended unless it is needed.
This doesn't turn `fs.open()` or `fsPromises.open()` into a synchronous blocking call. If synchronous operation is desired, something like `fs.openSync()` should be used.
  * `'w'`: Open file for writing. The file is created (if it does not exist) or truncated (if it exists).
  * `'wx'`: Like `'w'` but fails if the path exists.
  * `'w+'`: Open file for reading and writing. The file is created (if it does not exist) or truncated (if it exists).
  * `'wx+'`: Like `'w+'` but fails if the path exists.


`flag` can also be a number as documented by `fs.constants`. On Windows, flags are translated to their equivalent ones where applicable, e.g. `O_WRONLY` to `FILE_GENERIC_WRITE`, or `O_EXCL|O_CREAT` to `CREATE_NEW`, as accepted by `CreateFileW`.
The exclusive flag `'x'` (`O_EXCL` flag in `O_EXCL` returns an error even if the link is to a path that does not exist. The exclusive flag might not work with network file systems.
On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
Modifying a file rather than replacing it may require the `flag` option to be set to `'r+'` rather than the default `'w'`.
The behavior of some flags are platform-specific. As such, opening a directory on macOS and Linux with the `'a+'` flag, as in the example below, will return an error. In contrast, on Windows and FreeBSD, a file descriptor or a `FileHandle` will be returned.
```
// macOS and Linux
fs.open('<directory>', 'a+', (err, fd) => {
  // => [Error: EISDIR: illegal operation on a directory, open <directory>]
});

// Windows and FreeBSD
fs.open('<directory>', 'a+', (err, fd) => {
  // => null, <fd>
});
copy
```

On Windows, opening an existing hidden file using the `'w'` flag (either through `fs.open()`, `fs.writeFile()`, or `fsPromises.open()`) will fail with `EPERM`. Existing hidden files can be opened for writing with the `'r+'` flag.
A call to `fs.ftruncate()` or `filehandle.truncate()` can be used to reset the file contents.
