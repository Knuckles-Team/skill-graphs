#### Class: `fs.ReadStream`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream)
Added in: v0.1.93
  * Extends: [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)


Instances of [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream) are created and returned using the [`fs.createReadStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatereadstreampath-options) function.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/fs.html#event-close-2)
Added in: v0.1.93
Emitted when the [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream)'s underlying file descriptor has been closed.
##### Event: `'open'`[#](https://nodejs.org/docs/latest/api/fs.html#event-open)
Added in: v0.1.93
  * `fd` [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream).


Emitted when the [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream)'s file descriptor has been opened.
##### Event: `'ready'`[#](https://nodejs.org/docs/latest/api/fs.html#event-ready)
Added in: v9.11.0
Emitted when the [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream) is ready to be used.
Fires immediately after `'open'`.
#####  `readStream.bytesRead`[#](https://nodejs.org/docs/latest/api/fs.html#readstreambytesread)
Added in: v6.4.0
  * Type:


The number of bytes that have been read so far.
#####  `readStream.path`[#](https://nodejs.org/docs/latest/api/fs.html#readstreampath)
Added in: v0.1.93
  * Type: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


The path to the file the stream is reading from as specified in the first argument to `fs.createReadStream()`. If `path` is passed as a string, then `readStream.path` will be a string. If `path` is passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), then `readStream.path` will be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer). If `fd` is specified, then `readStream.path` will be `undefined`.
#####  `readStream.pending`[#](https://nodejs.org/docs/latest/api/fs.html#readstreampending)
Added in: v11.2.0, v10.16.0
  * Type:


This property is `true` if the underlying file has not been opened yet, i.e. before the `'ready'` event is emitted.
#### Class: `fs.Stats`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)
Added in: v0.1.21History Version | Changes
---|---
v22.0.0, v20.13.0 | Public constructor is deprecated.
v8.1.0 | Added times as numbers.
A [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object provides information about a file.
Objects returned from [`fs.stat()`](https://nodejs.org/docs/latest/api/fs.html#fsstatpath-options-callback), [`fs.lstat()`](https://nodejs.org/docs/latest/api/fs.html#fslstatpath-options-callback), [`fs.fstat()`](https://nodejs.org/docs/latest/api/fs.html#fsfstatfd-options-callback), and their synchronous counterparts are of this type. If `bigint` in the `options` passed to those methods is true, the numeric values will be `bigint` instead of `number`, and the object will contain additional nanosecond-precision properties suffixed with `Ns`. `Stat` objects are not to be created directly using the `new` keyword.
```
Stats {
  dev: 2114,
  ino: 48064969,
  mode: 33188,
  nlink: 1,
  uid: 85,
  gid: 100,
  rdev: 0,
  size: 527,
  blksize: 4096,
  blocks: 8,
  atimeMs: 1318289051000.1,
  mtimeMs: 1318289051000.1,
  ctimeMs: 1318289051000.1,
  birthtimeMs: 1318289051000.1,
  atime: Mon, 10 Oct 2011 23:24:11 GMT,
  mtime: Mon, 10 Oct 2011 23:24:11 GMT,
  ctime: Mon, 10 Oct 2011 23:24:11 GMT,
  birthtime: Mon, 10 Oct 2011 23:24:11 GMT }
copy
```

`bigint` version:
```
BigIntStats {
  dev: 2114n,
  ino: 48064969n,
  mode: 33188n,
  nlink: 1n,
  uid: 85n,
  gid: 100n,
  rdev: 0n,
  size: 527n,
  blksize: 4096n,
  blocks: 8n,
  atimeMs: 1318289051000n,
  mtimeMs: 1318289051000n,
  ctimeMs: 1318289051000n,
  birthtimeMs: 1318289051000n,
  atimeNs: 1318289051000000000n,
  mtimeNs: 1318289051000000000n,
  ctimeNs: 1318289051000000000n,
  birthtimeNs: 1318289051000000000n,
  atime: Mon, 10 Oct 2011 23:24:11 GMT,
  mtime: Mon, 10 Oct 2011 23:24:11 GMT,
  ctime: Mon, 10 Oct 2011 23:24:11 GMT,
  birthtime: Mon, 10 Oct 2011 23:24:11 GMT }
copy
```

#####  `stats.isBlockDevice()`[#](https://nodejs.org/docs/latest/api/fs.html#statsisblockdevice)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a block device.
#####  `stats.isCharacterDevice()`[#](https://nodejs.org/docs/latest/api/fs.html#statsischaracterdevice)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a character device.
#####  `stats.isDirectory()`[#](https://nodejs.org/docs/latest/api/fs.html#statsisdirectory)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a file system directory.
If the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object was obtained from calling [`fs.lstat()`](https://nodejs.org/docs/latest/api/fs.html#fslstatpath-options-callback) on a symbolic link which resolves to a directory, this method will return `false`. This is because [`fs.lstat()`](https://nodejs.org/docs/latest/api/fs.html#fslstatpath-options-callback) returns information about a symbolic link itself and not the path it resolves to.
#####  `stats.isFIFO()`[#](https://nodejs.org/docs/latest/api/fs.html#statsisfifo)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a first-in-first-out (FIFO) pipe.
#####  `stats.isFile()`[#](https://nodejs.org/docs/latest/api/fs.html#statsisfile)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a regular file.
#####  `stats.isSocket()`[#](https://nodejs.org/docs/latest/api/fs.html#statsissocket)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a socket.
#####  `stats.isSymbolicLink()`[#](https://nodejs.org/docs/latest/api/fs.html#statsissymboliclink)
Added in: v0.1.10
  * Returns:


Returns `true` if the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object describes a symbolic link.
This method is only valid when using [`fs.lstat()`](https://nodejs.org/docs/latest/api/fs.html#fslstatpath-options-callback).
#####  `stats.dev`[#](https://nodejs.org/docs/latest/api/fs.html#statsdev)
  * Type:


The numeric identifier of the device containing the file.
#####  `stats.ino`[#](https://nodejs.org/docs/latest/api/fs.html#statsino)
  * Type:


The file system specific "Inode" number for the file.
#####  `stats.mode`[#](https://nodejs.org/docs/latest/api/fs.html#statsmode)
  * Type:


A bit-field describing the file type and mode.
#####  `stats.nlink`[#](https://nodejs.org/docs/latest/api/fs.html#statsnlink)
  * Type:


The number of hard-links that exist for the file.
#####  `stats.uid`[#](https://nodejs.org/docs/latest/api/fs.html#statsuid)
  * Type:


The numeric user identifier of the user that owns the file (POSIX).
#####  `stats.gid`[#](https://nodejs.org/docs/latest/api/fs.html#statsgid)
  * Type:


The numeric group identifier of the group that owns the file (POSIX).
#####  `stats.rdev`[#](https://nodejs.org/docs/latest/api/fs.html#statsrdev)
  * Type:


A numeric device identifier if the file represents a device.
#####  `stats.size`[#](https://nodejs.org/docs/latest/api/fs.html#statssize)
  * Type:


The size of the file in bytes.
If the underlying file system does not support getting the size of the file, this will be `0`.
#####  `stats.blksize`[#](https://nodejs.org/docs/latest/api/fs.html#statsblksize)
  * Type:


The file system block size for i/o operations.
#####  `stats.blocks`[#](https://nodejs.org/docs/latest/api/fs.html#statsblocks)
  * Type:


The number of blocks allocated for this file.
#####  `stats.atimeMs`[#](https://nodejs.org/docs/latest/api/fs.html#statsatimems)
Added in: v8.1.0
  * Type:


The timestamp indicating the last time this file was accessed expressed in milliseconds since the POSIX Epoch.
#####  `stats.mtimeMs`[#](https://nodejs.org/docs/latest/api/fs.html#statsmtimems)
Added in: v8.1.0
  * Type:


The timestamp indicating the last time this file was modified expressed in milliseconds since the POSIX Epoch.
#####  `stats.ctimeMs`[#](https://nodejs.org/docs/latest/api/fs.html#statsctimems)
Added in: v8.1.0
  * Type:


The timestamp indicating the last time the file status was changed expressed in milliseconds since the POSIX Epoch.
#####  `stats.birthtimeMs`[#](https://nodejs.org/docs/latest/api/fs.html#statsbirthtimems)
Added in: v8.1.0
  * Type:


The timestamp indicating the creation time of this file expressed in milliseconds since the POSIX Epoch.
#####  `stats.atimeNs`[#](https://nodejs.org/docs/latest/api/fs.html#statsatimens)
Added in: v12.10.0
  * Type:


Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the last time this file was accessed expressed in nanoseconds since the POSIX Epoch.
#####  `stats.mtimeNs`[#](https://nodejs.org/docs/latest/api/fs.html#statsmtimens)
Added in: v12.10.0
  * Type:


Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the last time this file was modified expressed in nanoseconds since the POSIX Epoch.
#####  `stats.ctimeNs`[#](https://nodejs.org/docs/latest/api/fs.html#statsctimens)
Added in: v12.10.0
  * Type:


Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the last time the file status was changed expressed in nanoseconds since the POSIX Epoch.
#####  `stats.birthtimeNs`[#](https://nodejs.org/docs/latest/api/fs.html#statsbirthtimens)
Added in: v12.10.0
  * Type:


Only present when `bigint: true` is passed into the method that generates the object. The timestamp indicating the creation time of this file expressed in nanoseconds since the POSIX Epoch.
#####  `stats.atime`[#](https://nodejs.org/docs/latest/api/fs.html#statsatime)
Added in: v0.11.13
  * Type:


The timestamp indicating the last time this file was accessed.
#####  `stats.mtime`[#](https://nodejs.org/docs/latest/api/fs.html#statsmtime)
Added in: v0.11.13
  * Type:


The timestamp indicating the last time this file was modified.
#####  `stats.ctime`[#](https://nodejs.org/docs/latest/api/fs.html#statsctime)
Added in: v0.11.13
  * Type:


The timestamp indicating the last time the file status was changed.
#####  `stats.birthtime`[#](https://nodejs.org/docs/latest/api/fs.html#statsbirthtime)
Added in: v0.11.13
  * Type:


The timestamp indicating the creation time of this file.
##### Stat time values[#](https://nodejs.org/docs/latest/api/fs.html#stat-time-values)
The `atimeMs`, `mtimeMs`, `ctimeMs`, `birthtimeMs` properties are numeric values that hold the corresponding times in milliseconds. Their precision is platform specific. When `bigint: true` is passed into the method that generates the object, the properties will be
The `atimeNs`, `mtimeNs`, `ctimeNs`, `birthtimeNs` properties are `bigint: true` is passed into the method that generates the object. Their precision is platform specific.
`atime`, `mtime`, `ctime`, and `birthtime` are `Date` and number values are not connected. Assigning a new number value, or mutating the `Date` value, will not be reflected in the corresponding alternate representation.
The times in the stat object have the following semantics:
  * `atime` "Access Time": Time when file data last accessed. Changed by the
  * `mtime` "Modified Time": Time when file data last modified. Changed by the
  * `ctime` "Change Time": Time when file status was last changed (inode data modification). Changed by the
  * `birthtime` "Birth Time": Time of file creation. Set once when the file is created. On file systems where birthtime is not available, this field may instead hold either the `ctime` or `1970-01-01T00:00Z` (ie, Unix epoch timestamp `0`). This value may be greater than `atime` or `mtime` in this case. On Darwin and other FreeBSD variants, also set if the `atime` is explicitly set to an earlier value than the current `birthtime` using the


Prior to Node.js 0.12, the `ctime` held the `birthtime` on Windows systems. As of 0.12, `ctime` is not "creation time", and on Unix systems, it never was.
#### Class: `fs.StatFs`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs)
Added in: v19.6.0, v18.15.0
Provides information about a mounted file system.
Objects returned from [`fs.statfs()`](https://nodejs.org/docs/latest/api/fs.html#fsstatfspath-options-callback) and its synchronous counterpart are of this type. If `bigint` in the `options` passed to those methods is `true`, the numeric values will be `bigint` instead of `number`.
```
StatFs {
  type: 1397114950,
  bsize: 4096,
  blocks: 121938943,
  bfree: 61058895,
  bavail: 61058895,
  files: 999,
  ffree: 1000000
}
copy
```

`bigint` version:
```
StatFs {
  type: 1397114950n,
  bsize: 4096n,
  blocks: 121938943n,
  bfree: 61058895n,
  bavail: 61058895n,
  files: 999n,
  ffree: 1000000n
}
copy
```

#####  `statfs.bavail`[#](https://nodejs.org/docs/latest/api/fs.html#statfsbavail)
Added in: v19.6.0, v18.15.0
  * Type:


Free blocks available to unprivileged users.
#####  `statfs.bfree`[#](https://nodejs.org/docs/latest/api/fs.html#statfsbfree)
Added in: v19.6.0, v18.15.0
  * Type:


Free blocks in file system.
#####  `statfs.blocks`[#](https://nodejs.org/docs/latest/api/fs.html#statfsblocks)
Added in: v19.6.0, v18.15.0
  * Type:


Total data blocks in file system.
#####  `statfs.bsize`[#](https://nodejs.org/docs/latest/api/fs.html#statfsbsize)
Added in: v19.6.0, v18.15.0
  * Type:


Optimal transfer block size.
#####  `statfs.ffree`[#](https://nodejs.org/docs/latest/api/fs.html#statfsffree)
Added in: v19.6.0, v18.15.0
  * Type:


Free file nodes in file system.
#####  `statfs.files`[#](https://nodejs.org/docs/latest/api/fs.html#statfsfiles)
Added in: v19.6.0, v18.15.0
  * Type:


Total file nodes in file system.
#####  `statfs.type`[#](https://nodejs.org/docs/latest/api/fs.html#statfstype)
Added in: v19.6.0, v18.15.0
  * Type:


Type of file system.
#### Class: `fs.Utf8Stream`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsutf8stream)
Added in: v24.6.0
Stability: 1 - Experimental
An optimized UTF-8 stream writer that allows for flushing all the internal buffering on demand. It handles `EAGAIN` errors correctly, allowing for customization, for example, by dropping content if the disk is busy.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/fs.html#event-close-3)
The `'close'` event is emitted when the stream is fully closed.
##### Event: `'drain'`[#](https://nodejs.org/docs/latest/api/fs.html#event-drain)
The `'drain'` event is emitted when the internal buffer has drained sufficiently to allow continued writing.
##### Event: `'drop'`[#](https://nodejs.org/docs/latest/api/fs.html#event-drop)
The `'drop'` event is emitted when the maximal length is reached and that data will not be written. The data that was dropped is passed as the first argument to the event handler.
##### Event: `'error'`[#](https://nodejs.org/docs/latest/api/fs.html#event-error-1)
The `'error'` event is emitted when an error occurs.
##### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/fs.html#event-finish)
The `'finish'` event is emitted when the stream has been ended and all data has been flushed to the underlying file.
##### Event: `'ready'`[#](https://nodejs.org/docs/latest/api/fs.html#event-ready-1)
The `'ready'` event is emitted when the stream is ready to accept writes.
##### Event: `'write'`[#](https://nodejs.org/docs/latest/api/fs.html#event-write)
The `'write'` event is emitted when a write operation has completed. The number of bytes written is passed as the first argument to the event handler.
#####  `new fs.Utf8Stream([options])`[#](https://nodejs.org/docs/latest/api/fs.html#new-fsutf8streamoptions)
  * `options`
    * `append`: **Default** : `true`.
    * `contentMode`: `'utf8'` or `'buffer'`. **Default** : `'utf8'`.
    * `dest`:
    * `fd`: `fs.open()` or `fs.openSync()`.
    * `fs`: `fs` module, useful for mocking, testing, or customizing the behavior of the stream.
    * `fsync`: `fs.fsyncSync()` every time a write is completed.
    * `maxLength`: `maxLength`, the data written is dropped and a drop event is emitted with the dropped data
    * `maxWrite`: **Default** : `16384`
    * `minLength`:
    * `mkdir`: `dest` file exists when true. **Default** : `false`.
    * `mode`: `fs.open()`).
    * `periodicFlush`: `periodicFlush` milliseconds.
    * `retryEAGAIN` `write()`, `writeSync()`, or `flushSync()` encounters an `EAGAIN` or `EBUSY` error. If the return value is `true` the operation will be retried, otherwise it will bubble the error. The `err` is the error that caused this function to be called, `writeBufferLen` is the length of the buffer that was written, and `remainingBufferLen` is the length of the remaining buffer that the stream did not try to write.
      * `err` `null`.
      * `writeBufferLen`
      * `remainingBufferLen`:
    * `sync`:


#####  `utf8Stream.append`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamappend)
#####  `utf8Stream.contentMode`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamcontentmode)
  * `'utf8'` or `'buffer'`. **Default** : `'utf8'`.


#####  `utf8Stream.destroy()`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamdestroy)
Close the stream immediately, without flushing the internal buffer.
#####  `utf8Stream.end()`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamend)
Close the stream gracefully, flushing the internal buffer before closing.
#####  `utf8Stream.fd`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamfd)
#####  `utf8Stream.file`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamfile)
#####  `utf8Stream.flush(callback)`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamflushcallback)
  * `callback`
    * `err` `null`.


Writes the current buffer to the file if a write was not in progress. Do nothing if `minLength` is zero or if it is already writing.
#####  `utf8Stream.flushSync()`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamflushsync)
Flushes the buffered data synchronously. This is a costly operation.
#####  `utf8Stream.fsync`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamfsync)
  * `fs.fsyncSync()` after every write operation.


#####  `utf8Stream.maxLength`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streammaxlength)
  * `maxLength`, the data written is dropped and a drop event is emitted with the dropped data.


#####  `utf8Stream.minLength`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamminlength)
#####  `utf8Stream.mkdir`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streammkdir)
  * `dest` file exists. If `true`, it will create the directory if it does not exist. **Default** : `false`.


#####  `utf8Stream.mode`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streammode)
#####  `utf8Stream.periodicFlush`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamperiodicflush)
  * `0`, no periodic flushes will be performed.


#####  `utf8Stream.reopen(file)`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamreopenfile)
  * `file`: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) A path to a file to be written to (mode controlled by the append option).


Reopen the file in place, useful for log rotation.
#####  `utf8Stream.sync`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamsync)
#####  `utf8Stream.write(data)`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamwritedata)
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The data to write.
  * Returns


When the `options.contentMode` is set to `'utf8'` when the stream is created, the `data` argument must be a string. If the `contentMode` is set to `'buffer'`, the `data` argument must be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
#####  `utf8Stream.writing`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamwriting)
#####  `utf8Stream[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/fs.html#utf8streamsymboldispose)
Calls `utf8Stream.destroy()`.
#### Class: `fs.WriteStream`[#](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream)
Added in: v0.1.93
  * Extends [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)


Instances of [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream) are created and returned using the [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options) function.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/fs.html#event-close-4)
Added in: v0.1.93
Emitted when the [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream)'s underlying file descriptor has been closed.
##### Event: `'open'`[#](https://nodejs.org/docs/latest/api/fs.html#event-open-1)
Added in: v0.1.93
  * `fd` [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream).


Emitted when the [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream)'s file is opened.
##### Event: `'ready'`[#](https://nodejs.org/docs/latest/api/fs.html#event-ready-2)
Added in: v9.11.0
Emitted when the [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream) is ready to be used.
Fires immediately after `'open'`.
#####  `writeStream.bytesWritten`[#](https://nodejs.org/docs/latest/api/fs.html#writestreambyteswritten)
Added in: v0.4.7
The number of bytes written so far. Does not include data that is still queued for writing.
#####  `writeStream.close([callback])`[#](https://nodejs.org/docs/latest/api/fs.html#writestreamclosecallback)
Added in: v0.9.4
  * `callback`
    * `err`


Closes `writeStream`. Optionally accepts a callback that will be executed once the `writeStream` is closed.
#####  `writeStream.path`[#](https://nodejs.org/docs/latest/api/fs.html#writestreampath)
Added in: v0.1.93
The path to the file the stream is writing to as specified in the first argument to [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options). If `path` is passed as a string, then `writeStream.path` will be a string. If `path` is passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), then `writeStream.path` will be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
#####  `writeStream.pending`[#](https://nodejs.org/docs/latest/api/fs.html#writestreampending)
Added in: v11.2.0
  * Type:


This property is `true` if the underlying file has not been opened yet, i.e. before the `'ready'` event is emitted.
####  `fs.constants`[#](https://nodejs.org/docs/latest/api/fs.html#fsconstants)
  * Type:


Returns an object containing commonly used constants for file system operations.
##### FS constants[#](https://nodejs.org/docs/latest/api/fs.html#fs-constants)
The following constants are exported by `fs.constants` and `fsPromises.constants`.
Not every constant will be available on every operating system; this is especially important for Windows, where many of the POSIX specific definitions are not available. For portable applications it is recommended to check for their presence before use.
To use more than one constant, use the bitwise OR `|` operator.
Example:
```
import { open, constants } from 'node:fs';

const {
  O_RDWR,
  O_CREAT,
  O_EXCL,
} = constants;

open('/path/to/my/file', O_RDWR | O_CREAT | O_EXCL, (err, fd) => {
  // ...
});
copy
```

###### File access constants[#](https://nodejs.org/docs/latest/api/fs.html#file-access-constants)
The following constants are meant for use as the `mode` parameter passed to [`fsPromises.access()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesaccesspath-mode), [`fs.access()`](https://nodejs.org/docs/latest/api/fs.html#fsaccesspath-mode-callback), and [`fs.accessSync()`](https://nodejs.org/docs/latest/api/fs.html#fsaccesssyncpath-mode).
Constant | Description
---|---
`F_OK` | Flag indicating that the file is visible to the calling process. This is useful for determining if a file exists, but says nothing about `rwx` permissions. Default if no mode is specified.
`R_OK` | Flag indicating that the file can be read by the calling process.
`W_OK` | Flag indicating that the file can be written by the calling process.
`X_OK` | Flag indicating that the file can be executed by the calling process. This has no effect on Windows (will behave like `fs.constants.F_OK`).
The definitions are also available on Windows.
###### File copy constants[#](https://nodejs.org/docs/latest/api/fs.html#file-copy-constants)
The following constants are meant for use with [`fs.copyFile()`](https://nodejs.org/docs/latest/api/fs.html#fscopyfilesrc-dest-mode-callback).
