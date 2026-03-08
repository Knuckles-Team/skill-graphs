[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html)
    * [MADV_* Constants](https://docs.python.org/3/library/mmap.html#madv-constants)
    * [MAP_* Constants](https://docs.python.org/3/library/mmap.html#map-constants)


#### Previous topic
[`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html "previous chapter")
#### Next topic
[Internet Data Handling](https://docs.python.org/3/library/netdata.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=mmap+%E2%80%94+Memory-mapped+file+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmmap.html&pagesource=library%2Fmmap.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/netdata.html "Internet Data Handling") |
  * [previous](https://docs.python.org/3/library/signal.html "signal — Set handlers for asynchronous events") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html)
  * |
  * Theme  Auto Light Dark |


#  `mmap` — Memory-mapped file support[¶](https://docs.python.org/3/library/mmap.html#module-mmap "Link to this heading")
* * *
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
Memory-mapped file objects behave like both [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") and like [file objects](https://docs.python.org/3/glossary.html#term-file-object). You can use mmap objects in most places where `bytearray` are expected; for example, you can use the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") module to search through a memory-mapped file. You can also change a single byte by doing `obj[index] = 97`, or change a subsequence by assigning to a slice: `obj[i1:i2] = b'...'`. You can also read and write data starting at the current file position, and `seek()` through the file to different positions.
A memory-mapped file is created by the [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap") constructor, which is different on Unix and on Windows. In either case you must provide a file descriptor for a file opened for update. If you wish to map an existing Python file object, use its [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method to obtain the correct value for the _fileno_ parameter. Otherwise, you can open the file using the [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") function, which returns a file descriptor directly (the file still needs to be closed when done).
Note
If you want to create a memory-mapping for a writable, buffered file, you should [`flush()`](https://docs.python.org/3/library/io.html#io.IOBase.flush "io.IOBase.flush") the file first. This is necessary to ensure that local modifications to the buffers are actually available to the mapping.
For both the Unix and Windows versions of the constructor, _access_ may be specified as an optional keyword parameter. _access_ accepts one of four values: `ACCESS_READ`, `ACCESS_WRITE`, or `ACCESS_COPY` to specify read-only, write-through or copy-on-write memory respectively, or `ACCESS_DEFAULT` to defer to _prot_. _access_ can be used on both Unix and Windows. If _access_ is not specified, Windows mmap returns a write-through mapping. The initial memory values for all three access types are taken from the specified file. Assignment to an `ACCESS_READ` memory map raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception. Assignment to an `ACCESS_WRITE` memory map affects both memory and the underlying file. Assignment to an `ACCESS_COPY` memory map affects memory but does not update the underlying file.
Changed in version 3.7: Added `ACCESS_DEFAULT` constant.
To map anonymous memory, -1 should be passed as the fileno along with the length.

_class_ mmap.mmap(_fileno_ , _length_ , _tagname =None_, _access =ACCESS_DEFAULT_, _offset =0_)[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap "Link to this definition")

**(Windows version)** Maps _length_ bytes from the file specified by the file handle _fileno_ , and creates a mmap object. If _length_ is larger than the current size of the file, the file is extended to contain _length_ bytes. If _length_ is `0`, the maximum length of the map is the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).
_tagname_ , if specified and not `None`, is a string giving a tag name for the mapping. Windows allows you to have many different mappings against the same file. If you specify the name of an existing tag, that tag is opened, otherwise a new tag of this name is created. If this parameter is omitted or `None`, the mapping is created without a name. Avoiding the use of the _tagname_ parameter will assist in keeping your code portable between Unix and Windows.
_offset_ may be specified as a non-negative integer offset. mmap references will be relative to the offset from the beginning of the file. _offset_ defaults to 0. _offset_ must be a multiple of the `ALLOCATIONGRANULARITY`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `mmap.__new__` with arguments `fileno`, `length`, `access`, `offset`.

_class_ mmap.mmap(_fileno_ , _length_ , _flags =MAP_SHARED_, _prot =PROT_WRITE | PROT_READ_, _access =ACCESS_DEFAULT_, _offset =0_, _*_ , _trackfd =True_)

**(Unix version)** Maps _length_ bytes from the file specified by the file descriptor _fileno_ , and returns a mmap object. If _length_ is `0`, the maximum length of the map will be the current size of the file when [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap") is called.
_flags_ specifies the nature of the mapping. [`MAP_PRIVATE`](https://docs.python.org/3/library/mmap.html#mmap.MAP_PRIVATE "mmap.MAP_PRIVATE") creates a private copy-on-write mapping, so changes to the contents of the mmap object will be private to this process, and [`MAP_SHARED`](https://docs.python.org/3/library/mmap.html#mmap.MAP_SHARED "mmap.MAP_SHARED") creates a mapping that’s shared with all other processes mapping the same areas of the file. The default value is `MAP_SHARED`. Some systems have additional possible flags with the full list specified in [MAP_* constants](https://docs.python.org/3/library/mmap.html#map-constants).
_prot_ , if specified, gives the desired memory protection; the two most useful values are `PROT_READ` and `PROT_WRITE`, to specify that the pages may be read or written. _prot_ defaults to `PROT_READ | PROT_WRITE`.
_access_ may be specified in lieu of _flags_ and _prot_ as an optional keyword parameter. It is an error to specify both _flags_ , _prot_ and _access_. See the description of _access_ above for information on how to use this parameter.
_offset_ may be specified as a non-negative integer offset. mmap references will be relative to the offset from the beginning of the file. _offset_ defaults to 0. _offset_ must be a multiple of `ALLOCATIONGRANULARITY` which is equal to `PAGESIZE` on Unix systems.
If _trackfd_ is `False`, the file descriptor specified by _fileno_ will not be duplicated, and the resulting `mmap` object will not be associated with the map’s underlying file. This means that the [`size()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.size "mmap.mmap.size") and [`resize()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.resize "mmap.mmap.resize") methods will fail. This mode is useful to limit the number of open file descriptors.
To ensure validity of the created memory mapping the file specified by the descriptor _fileno_ is internally automatically synchronized with the physical backing store on macOS.
Changed in version 3.13: The _trackfd_ parameter was added.
This example shows a simple way of using [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap"):
Copy```
import mmap

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(mm[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints b"Hello  world!\n"
    # close the map
    mm.close()

```

[`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap") can also be used as a context manager in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement:
Copy```
import mmap

with mmap.mmap(-1, 13) as mm:
    mm.write(b"Hello world!")

```

Added in version 3.2: Context manager support.
The next example demonstrates how to create an anonymous map and exchange data between the parent and child processes:
Copy```
import mmap
import os

mm = mmap.mmap(-1, 13)
mm.write(b"Hello world!")

pid = os.fork()

if pid == 0:  # In a child process
    mm.seek(0)
    print(mm.readline())

    mm.close()

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `mmap.__new__` with arguments `fileno`, `length`, `access`, `offset`.
Memory-mapped file objects support the following methods:

close()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.close "Link to this definition")

Closes the mmap. Subsequent calls to other methods of the object will result in a ValueError exception being raised. This will not close the open file.

closed[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.closed "Link to this definition")

`True` if the file is closed.
Added in version 3.2.

find(_sub_[, _start_[, _end_]])[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.find "Link to this definition")

Returns the lowest index in the object where the subsequence _sub_ is found, such that _sub_ is contained in the range [_start_ , _end_]. Optional arguments _start_ and _end_ are interpreted as in slice notation. Returns `-1` on failure.
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.

flush()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.flush "Link to this definition")


flush(_offset_ , _size_ , _/_)

Flushes changes made to the in-memory copy of a file back to disk. Without use of this call there is no guarantee that changes are written back before the object is destroyed. If _offset_ and _size_ are specified, only changes to the given range of bytes will be flushed to disk; otherwise, the whole extent of the mapping is flushed. _offset_ must be a multiple of the `PAGESIZE` or `ALLOCATIONGRANULARITY`.
`None` is returned to indicate success. An exception is raised when the call failed.
Changed in version 3.8: Previously, a nonzero value was returned on success; zero was returned on error under Windows. A zero value was returned on success; an exception was raised on error under Unix.

madvise(_option_[, _start_[, _length_]])[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.madvise "Link to this definition")

Send advice _option_ to the kernel about the memory region beginning at _start_ and extending _length_ bytes. _option_ must be one of the [MADV_* constants](https://docs.python.org/3/library/mmap.html#madvise-constants) available on the system. If _start_ and _length_ are omitted, the entire mapping is spanned. On some systems (including Linux), _start_ must be a multiple of the `PAGESIZE`.
Availability: Systems with the `madvise()` system call.
Added in version 3.8.

move(_dest_ , _src_ , _count_)[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.move "Link to this definition")

Copy the _count_ bytes starting at offset _src_ to the destination index _dest_. If the mmap was created with `ACCESS_READ`, then calls to move will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception.

read([_n_])[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.read "Link to this definition")

Return a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") containing up to _n_ bytes starting from the current file position. If the argument is omitted, `None` or negative, return all bytes from the current file position to the end of the mapping. The file position is updated to point after the bytes that were returned.
Changed in version 3.3: Argument can be omitted or `None`.

read_byte()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.read_byte "Link to this definition")

Returns a byte at the current file position as an integer, and advances the file position by 1.

readline()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.readline "Link to this definition")

Returns a single line, starting at the current file position and up to the next newline. The file position is updated to point after the bytes that were returned.

resize(_newsize_)[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.resize "Link to this definition")

Resizes the map and the underlying file, if any.
Resizing a map created with _access_ of `ACCESS_READ` or `ACCESS_COPY`, will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception. Resizing a map created with _trackfd_ set to `False`, will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception.
**On Windows** : Resizing the map will raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if there are other maps against the same named file. Resizing an anonymous map (ie against the pagefile) will silently create a new map with the original data copied over up to the length of the new size.
Changed in version 3.11: Correctly fails if attempting to resize when another map is held Allows resize against an anonymous map on Windows

rfind(_sub_[, _start_[, _end_]])[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.rfind "Link to this definition")

Returns the highest index in the object where the subsequence _sub_ is found, such that _sub_ is contained in the range [_start_ , _end_]. Optional arguments _start_ and _end_ are interpreted as in slice notation. Returns `-1` on failure.
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.

seek(_pos_[, _whence_])[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.seek "Link to this definition")

Set the file’s current position. _whence_ argument is optional and defaults to `os.SEEK_SET` or `0` (absolute file positioning); other values are `os.SEEK_CUR` or `1` (seek relative to the current position) and `os.SEEK_END` or `2` (seek relative to the file’s end).
Changed in version 3.13: Return the new absolute position instead of `None`.

seekable()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.seekable "Link to this definition")

Return whether the file supports seeking, and the return value is always `True`.
Added in version 3.13.

size()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.size "Link to this definition")

Return the length of the file, which can be larger than the size of the memory-mapped area.

tell()[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.tell "Link to this definition")

Returns the current position of the file pointer.

write(_bytes_)[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.write "Link to this definition")

Write the bytes in _bytes_ into memory at the current position of the file pointer and return the number of bytes written (never less than `len(bytes)`, since if the write fails, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised). The file position is updated to point after the bytes that were written. If the mmap was created with `ACCESS_READ`, then writing to it will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception.
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.
Changed in version 3.6: The number of bytes written is now returned.

write_byte(_byte_)[¶](https://docs.python.org/3/library/mmap.html#mmap.mmap.write_byte "Link to this definition")

Write the integer _byte_ into memory at the current position of the file pointer; the file position is advanced by `1`. If the mmap was created with `ACCESS_READ`, then writing to it will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception.
## MADV_* Constants[¶](https://docs.python.org/3/library/mmap.html#madv-constants "Link to this heading")

mmap.MADV_NORMAL[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_NORMAL "Link to this definition")


mmap.MADV_RANDOM[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_RANDOM "Link to this definition")


mmap.MADV_SEQUENTIAL[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_SEQUENTIAL "Link to this definition")


mmap.MADV_WILLNEED[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_WILLNEED "Link to this definition")


mmap.MADV_DONTNEED[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_DONTNEED "Link to this definition")


mmap.MADV_REMOVE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_REMOVE "Link to this definition")


mmap.MADV_DONTFORK[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_DONTFORK "Link to this definition")


mmap.MADV_DOFORK[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_DOFORK "Link to this definition")


mmap.MADV_HWPOISON[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_HWPOISON "Link to this definition")


mmap.MADV_MERGEABLE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_MERGEABLE "Link to this definition")


mmap.MADV_UNMERGEABLE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_UNMERGEABLE "Link to this definition")


mmap.MADV_SOFT_OFFLINE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_SOFT_OFFLINE "Link to this definition")


mmap.MADV_HUGEPAGE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_HUGEPAGE "Link to this definition")


mmap.MADV_NOHUGEPAGE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_NOHUGEPAGE "Link to this definition")


mmap.MADV_DONTDUMP[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_DONTDUMP "Link to this definition")


mmap.MADV_DODUMP[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_DODUMP "Link to this definition")


mmap.MADV_FREE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_FREE "Link to this definition")


mmap.MADV_NOSYNC[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_NOSYNC "Link to this definition")


mmap.MADV_AUTOSYNC[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_AUTOSYNC "Link to this definition")


mmap.MADV_NOCORE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_NOCORE "Link to this definition")


mmap.MADV_CORE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_CORE "Link to this definition")


mmap.MADV_PROTECT[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_PROTECT "Link to this definition")


mmap.MADV_FREE_REUSABLE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_FREE_REUSABLE "Link to this definition")


mmap.MADV_FREE_REUSE[¶](https://docs.python.org/3/library/mmap.html#mmap.MADV_FREE_REUSE "Link to this definition")

These options can be passed to [`mmap.madvise()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.madvise "mmap.mmap.madvise"). Not every option will be present on every system.
Availability: Systems with the madvise() system call.
Added in version 3.8.
## MAP_* Constants[¶](https://docs.python.org/3/library/mmap.html#map-constants "Link to this heading")

mmap.MAP_SHARED[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_SHARED "Link to this definition")


mmap.MAP_PRIVATE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_PRIVATE "Link to this definition")


mmap.MAP_32BIT[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_32BIT "Link to this definition")


mmap.MAP_ALIGNED_SUPER[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_ALIGNED_SUPER "Link to this definition")


mmap.MAP_ANON[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_ANON "Link to this definition")


mmap.MAP_ANONYMOUS[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_ANONYMOUS "Link to this definition")


mmap.MAP_CONCEAL[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_CONCEAL "Link to this definition")


mmap.MAP_DENYWRITE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_DENYWRITE "Link to this definition")


mmap.MAP_EXECUTABLE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_EXECUTABLE "Link to this definition")


mmap.MAP_HASSEMAPHORE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_HASSEMAPHORE "Link to this definition")


mmap.MAP_JIT[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_JIT "Link to this definition")


mmap.MAP_NOCACHE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_NOCACHE "Link to this definition")


mmap.MAP_NOEXTEND[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_NOEXTEND "Link to this definition")


mmap.MAP_NORESERVE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_NORESERVE "Link to this definition")


mmap.MAP_POPULATE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_POPULATE "Link to this definition")


mmap.MAP_RESILIENT_CODESIGN[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_RESILIENT_CODESIGN "Link to this definition")


mmap.MAP_RESILIENT_MEDIA[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_RESILIENT_MEDIA "Link to this definition")


mmap.MAP_STACK[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_STACK "Link to this definition")


mmap.MAP_TPRO[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_TPRO "Link to this definition")


mmap.MAP_TRANSLATED_ALLOW_EXECUTE[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_TRANSLATED_ALLOW_EXECUTE "Link to this definition")


mmap.MAP_UNIX03[¶](https://docs.python.org/3/library/mmap.html#mmap.MAP_UNIX03 "Link to this definition")

These are the various flags that can be passed to [`mmap.mmap()`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap"). `MAP_ALIGNED_SUPER` is only available at FreeBSD and `MAP_CONCEAL` is only available at OpenBSD. Note that some options might not be present on some systems.
Changed in version 3.10: Added `MAP_POPULATE` constant.
Added in version 3.11: Added `MAP_STACK` constant.
Added in version 3.12: Added `MAP_ALIGNED_SUPER` and `MAP_CONCEAL` constants.
Added in version 3.13: Added `MAP_32BIT`, `MAP_HASSEMAPHORE`, `MAP_JIT`, `MAP_NOCACHE`, `MAP_NOEXTEND`, `MAP_NORESERVE`, `MAP_RESILIENT_CODESIGN`, `MAP_RESILIENT_MEDIA`, `MAP_TPRO`, `MAP_TRANSLATED_ALLOW_EXECUTE`, and `MAP_UNIX03` constants.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html)
    * [MADV_* Constants](https://docs.python.org/3/library/mmap.html#madv-constants)
    * [MAP_* Constants](https://docs.python.org/3/library/mmap.html#map-constants)


#### Previous topic
[`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html "previous chapter")
#### Next topic
[Internet Data Handling](https://docs.python.org/3/library/netdata.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=mmap+%E2%80%94+Memory-mapped+file+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmmap.html&pagesource=library%2Fmmap.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/netdata.html "Internet Data Handling") |
  * [previous](https://docs.python.org/3/library/signal.html "signal — Set handlers for asynchronous events") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
