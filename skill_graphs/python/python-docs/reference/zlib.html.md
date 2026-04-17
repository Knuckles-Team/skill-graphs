[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html "previous chapter")
#### Next topic
[`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zlib+%E2%80%94+Compression+compatible+with+gzip&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzlib.html&pagesource=library%2Fzlib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/gzip.html "gzip — Support for gzip files") |
  * [previous](https://docs.python.org/3/library/compression.zstd.html "compression.zstd — Compression compatible with the Zstandard format") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html)
  * |
  * Theme  Auto Light Dark |


#  `zlib` — Compression compatible with **gzip**[¶](https://docs.python.org/3/library/zlib.html#module-zlib "Link to this heading")
* * *
For applications that require data compression, the functions in this module allow compression and decompression, using the
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
zlib’s functions have many options and often need to be used in a particular order. This documentation doesn’t attempt to cover all of the permutations; consult the
For reading and writing `.gz` files see the [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") module.
The available exception and functions in this module are:

_exception_ zlib.error[¶](https://docs.python.org/3/library/zlib.html#zlib.error "Link to this definition")

Exception raised on compression and decompression errors.

zlib.adler32(_data_[, _value_])[¶](https://docs.python.org/3/library/zlib.html#zlib.adler32 "Link to this definition")

Computes an Adler-32 checksum of _data_. (An Adler-32 checksum is almost as reliable as a CRC32 but can be computed much more quickly.) The result is an unsigned 32-bit integer. If _value_ is present, it is used as the starting value of the checksum; otherwise, a default value of 1 is used. Passing in _value_ allows computing a running checksum over the concatenation of several inputs. The algorithm is not cryptographically strong, and should not be used for authentication or digital signatures. Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use as a general hash algorithm.
Changed in version 3.0: The result is always unsigned.

zlib.compress(_data_ , _/_ , _level =Z_DEFAULT_COMPRESSION_, _wbits =MAX_WBITS_)[¶](https://docs.python.org/3/library/zlib.html#zlib.compress "Link to this definition")

Compresses the bytes in _data_ , returning a bytes object containing compressed data. _level_ is an integer from `0` to `9` or `-1` controlling the level of compression; See [`Z_BEST_SPEED`](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_SPEED "zlib.Z_BEST_SPEED") (`1`), [`Z_BEST_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_COMPRESSION "zlib.Z_BEST_COMPRESSION") (`9`), [`Z_NO_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_NO_COMPRESSION "zlib.Z_NO_COMPRESSION") (`0`), and the default, [`Z_DEFAULT_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_DEFAULT_COMPRESSION "zlib.Z_DEFAULT_COMPRESSION") (`-1`) for more information about these values.
The _wbits_ argument controls the size of the history buffer (or the “window size”) used when compressing data, and whether a header and trailer is included in the output. It can take several ranges of values, defaulting to `15` ([`MAX_WBITS`](https://docs.python.org/3/library/zlib.html#zlib.MAX_WBITS "zlib.MAX_WBITS")):
  * +9 to +15: The base-two logarithm of the window size, which therefore ranges between 512 and 32768. Larger values produce better compression at the expense of greater memory usage. The resulting output will include a zlib-specific header and trailer.
  * −9 to −15: Uses the absolute value of _wbits_ as the window size logarithm, while producing a raw output stream with no header or trailing checksum.
  * +25 to +31 = 16 + (9 to 15): Uses the low 4 bits of the value as the window size logarithm, while including a basic **gzip** header and trailing checksum in the output.


Raises the [`error`](https://docs.python.org/3/library/zlib.html#zlib.error "zlib.error") exception if any error occurs.
Changed in version 3.6: _level_ can now be used as a keyword parameter.
Changed in version 3.11: The _wbits_ parameter is now available to set window bits and compression type.

zlib.compressobj(_level=Z_DEFAULT_COMPRESSION_ , _method=DEFLATED_ , _wbits=MAX_WBITS_ , _memLevel=DEF_MEM_LEVEL_ , _strategy=Z_DEFAULT_STRATEGY_[, _zdict_])[¶](https://docs.python.org/3/library/zlib.html#zlib.compressobj "Link to this definition")

Returns a compression object, to be used for compressing data streams that won’t fit into memory at once.
_level_ is the compression level – an integer from `0` to `9` or `-1`. See [`Z_BEST_SPEED`](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_SPEED "zlib.Z_BEST_SPEED") (`1`), [`Z_BEST_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_COMPRESSION "zlib.Z_BEST_COMPRESSION") (`9`), [`Z_NO_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_NO_COMPRESSION "zlib.Z_NO_COMPRESSION") (`0`), and the default, [`Z_DEFAULT_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_DEFAULT_COMPRESSION "zlib.Z_DEFAULT_COMPRESSION") (`-1`) for more information about these values.
_method_ is the compression algorithm. Currently, the only supported value is [`DEFLATED`](https://docs.python.org/3/library/zlib.html#zlib.DEFLATED "zlib.DEFLATED").
The _wbits_ parameter controls the size of the history buffer (or the “window size”), and what header and trailer format will be used. It has the same meaning as [described for compress()](https://docs.python.org/3/library/zlib.html#compress-wbits).
The _memLevel_ argument controls the amount of memory used for the internal compression state. Valid values range from `1` to `9`. Higher values use more memory, but are faster and produce smaller output.
_strategy_ is used to tune the compression algorithm. Possible values are [`Z_DEFAULT_STRATEGY`](https://docs.python.org/3/library/zlib.html#zlib.Z_DEFAULT_STRATEGY "zlib.Z_DEFAULT_STRATEGY"), [`Z_FILTERED`](https://docs.python.org/3/library/zlib.html#zlib.Z_FILTERED "zlib.Z_FILTERED"), [`Z_HUFFMAN_ONLY`](https://docs.python.org/3/library/zlib.html#zlib.Z_HUFFMAN_ONLY "zlib.Z_HUFFMAN_ONLY"), [`Z_RLE`](https://docs.python.org/3/library/zlib.html#zlib.Z_RLE "zlib.Z_RLE") and [`Z_FIXED`](https://docs.python.org/3/library/zlib.html#zlib.Z_FIXED "zlib.Z_FIXED").
_zdict_ is a predefined compression dictionary. This is a sequence of bytes (such as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object) containing subsequences that are expected to occur frequently in the data that is to be compressed. Those subsequences that are expected to be most common should come at the end of the dictionary.
Changed in version 3.3: Added the _zdict_ parameter and keyword argument support.

zlib.crc32(_data_[, _value_])[¶](https://docs.python.org/3/library/zlib.html#zlib.crc32 "Link to this definition")

Computes a CRC (Cyclic Redundancy Check) checksum of _data_. The result is an unsigned 32-bit integer. If _value_ is present, it is used as the starting value of the checksum; otherwise, a default value of 0 is used. Passing in _value_ allows computing a running checksum over the concatenation of several inputs. The algorithm is not cryptographically strong, and should not be used for authentication or digital signatures. Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use as a general hash algorithm.
Changed in version 3.0: The result is always unsigned.

zlib.decompress(_data_ , _/_ , _wbits =MAX_WBITS_, _bufsize =DEF_BUF_SIZE_)[¶](https://docs.python.org/3/library/zlib.html#zlib.decompress "Link to this definition")

Decompresses the bytes in _data_ , returning a bytes object containing the uncompressed data. The _wbits_ parameter depends on the format of _data_ , and is discussed further below. If _bufsize_ is given, it is used as the initial size of the output buffer. Raises the [`error`](https://docs.python.org/3/library/zlib.html#zlib.error "zlib.error") exception if any error occurs.
The _wbits_ parameter controls the size of the history buffer (or “window size”), and what header and trailer format is expected. It is similar to the parameter for [`compressobj()`](https://docs.python.org/3/library/zlib.html#zlib.compressobj "zlib.compressobj"), but accepts more ranges of values:
  * +8 to +15: The base-two logarithm of the window size. The input must include a zlib header and trailer.
  * 0: Automatically determine the window size from the zlib header. Only supported since zlib 1.2.3.5.
  * −8 to −15: Uses the absolute value of _wbits_ as the window size logarithm. The input must be a raw stream with no header or trailer.
  * +24 to +31 = 16 + (8 to 15): Uses the low 4 bits of the value as the window size logarithm. The input must include a gzip header and trailer.
  * +40 to +47 = 32 + (8 to 15): Uses the low 4 bits of the value as the window size logarithm, and automatically accepts either the zlib or gzip format.


When decompressing a stream, the window size must not be smaller than the size originally used to compress the stream; using a too-small value may result in an [`error`](https://docs.python.org/3/library/zlib.html#zlib.error "zlib.error") exception. The default _wbits_ value corresponds to the largest window size and requires a zlib header and trailer to be included.
_bufsize_ is the initial size of the buffer used to hold decompressed data. If more space is required, the buffer size will be increased as needed, so you don’t have to get this value exactly right; tuning it will only save a few calls to `malloc()`.
Changed in version 3.6: _wbits_ and _bufsize_ can be used as keyword arguments.

zlib.decompressobj(_wbits=MAX_WBITS_[, _zdict_])[¶](https://docs.python.org/3/library/zlib.html#zlib.decompressobj "Link to this definition")

Returns a decompression object, to be used for decompressing data streams that won’t fit into memory at once.
The _wbits_ parameter controls the size of the history buffer (or the “window size”), and what header and trailer format is expected. It has the same meaning as [described for decompress()](https://docs.python.org/3/library/zlib.html#decompress-wbits).
The _zdict_ parameter specifies a predefined compression dictionary. If provided, this must be the same dictionary as was used by the compressor that produced the data that is to be decompressed.
Note
If _zdict_ is a mutable object (such as a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray")), you must not modify its contents between the call to `decompressobj()` and the first call to the decompressor’s `decompress()` method.
Changed in version 3.3: Added the _zdict_ parameter.
Compression objects support the following methods:

Compress.compress(_data_)[¶](https://docs.python.org/3/library/zlib.html#zlib.Compress.compress "Link to this definition")

Compress _data_ , returning a bytes object containing compressed data for at least part of the data in _data_. This data should be concatenated to the output produced by any preceding calls to the `compress()` method. Some input may be kept in internal buffers for later processing.

Compress.flush([_mode_])[¶](https://docs.python.org/3/library/zlib.html#zlib.Compress.flush "Link to this definition")

All pending input is processed, and a bytes object containing the remaining compressed output is returned. _mode_ can be selected from the constants [`Z_NO_FLUSH`](https://docs.python.org/3/library/zlib.html#zlib.Z_NO_FLUSH "zlib.Z_NO_FLUSH"), [`Z_PARTIAL_FLUSH`](https://docs.python.org/3/library/zlib.html#zlib.Z_PARTIAL_FLUSH "zlib.Z_PARTIAL_FLUSH"), [`Z_SYNC_FLUSH`](https://docs.python.org/3/library/zlib.html#zlib.Z_SYNC_FLUSH "zlib.Z_SYNC_FLUSH"), [`Z_FULL_FLUSH`](https://docs.python.org/3/library/zlib.html#zlib.Z_FULL_FLUSH "zlib.Z_FULL_FLUSH"), [`Z_BLOCK`](https://docs.python.org/3/library/zlib.html#zlib.Z_BLOCK "zlib.Z_BLOCK"), or [`Z_FINISH`](https://docs.python.org/3/library/zlib.html#zlib.Z_FINISH "zlib.Z_FINISH"), defaulting to `Z_FINISH`. Except `Z_FINISH`, all constants allow compressing further bytestrings of data, while `Z_FINISH` finishes the compressed stream and prevents compressing any more data. After calling `flush()` with _mode_ set to `Z_FINISH`, the [`compress()`](https://docs.python.org/3/library/zlib.html#zlib.compress "zlib.compress") method cannot be called again; the only realistic action is to delete the object.

Compress.copy()[¶](https://docs.python.org/3/library/zlib.html#zlib.Compress.copy "Link to this definition")

Returns a copy of the compression object. This can be used to efficiently compress a set of data that share a common initial prefix.
Changed in version 3.8: Added [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy") and [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy") support to compression objects.
Decompression objects support the following methods and attributes:

Decompress.unused_data[¶](https://docs.python.org/3/library/zlib.html#zlib.Decompress.unused_data "Link to this definition")

A bytes object which contains any bytes past the end of the compressed data. That is, this remains `b""` until the last byte that contains compression data is available. If the whole bytestring turned out to contain compressed data, this is `b""`, an empty bytes object.

Decompress.unconsumed_tail[¶](https://docs.python.org/3/library/zlib.html#zlib.Decompress.unconsumed_tail "Link to this definition")

A bytes object that contains any data that was not consumed by the last [`decompress()`](https://docs.python.org/3/library/zlib.html#zlib.decompress "zlib.decompress") call because it exceeded the limit for the uncompressed data buffer. This data has not yet been seen by the zlib machinery, so you must feed it (possibly with further data concatenated to it) back to a subsequent `decompress()` method call in order to get correct output.

Decompress.eof[¶](https://docs.python.org/3/library/zlib.html#zlib.Decompress.eof "Link to this definition")

A boolean indicating whether the end of the compressed data stream has been reached.
This makes it possible to distinguish between a properly formed compressed stream, and an incomplete or truncated one.
Added in version 3.3.

Decompress.decompress(_data_ , _max_length =0_)[¶](https://docs.python.org/3/library/zlib.html#zlib.Decompress.decompress "Link to this definition")

Decompress _data_ , returning a bytes object containing the uncompressed data corresponding to at least part of the data in _string_. This data should be concatenated to the output produced by any preceding calls to the `decompress()` method. Some of the input data may be preserved in internal buffers for later processing.
If the optional parameter _max_length_ is non-zero then the return value will be no longer than _max_length_. This may mean that not all of the compressed input can be processed; and unconsumed data will be stored in the attribute [`unconsumed_tail`](https://docs.python.org/3/library/zlib.html#zlib.Decompress.unconsumed_tail "zlib.Decompress.unconsumed_tail"). This bytestring must be passed to a subsequent call to `decompress()` if decompression is to continue. If _max_length_ is zero then the whole input is decompressed, and `unconsumed_tail` is empty.
Changed in version 3.6: _max_length_ can be used as a keyword argument.

Decompress.flush([_length_])[¶](https://docs.python.org/3/library/zlib.html#zlib.Decompress.flush "Link to this definition")

All pending input is processed, and a bytes object containing the remaining uncompressed output is returned. After calling `flush()`, the [`decompress()`](https://docs.python.org/3/library/zlib.html#zlib.decompress "zlib.decompress") method cannot be called again; the only realistic action is to delete the object.
The optional parameter _length_ sets the initial size of the output buffer.

Decompress.copy()[¶](https://docs.python.org/3/library/zlib.html#zlib.Decompress.copy "Link to this definition")

Returns a copy of the decompression object. This can be used to save the state of the decompressor midway through the data stream in order to speed up random seeks into the stream at a future point.
Changed in version 3.8: Added [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy") and [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy") support to decompression objects.
The following constants are available to configure compression and decompression behavior:

zlib.DEFLATED[¶](https://docs.python.org/3/library/zlib.html#zlib.DEFLATED "Link to this definition")

The deflate compression method.

zlib.MAX_WBITS[¶](https://docs.python.org/3/library/zlib.html#zlib.MAX_WBITS "Link to this definition")

The maximum window size, expressed as a power of 2. For example, if `MAX_WBITS` is `15` it results in a window size of `32 KiB`.

zlib.DEF_MEM_LEVEL[¶](https://docs.python.org/3/library/zlib.html#zlib.DEF_MEM_LEVEL "Link to this definition")

The default memory level for compression objects.

zlib.DEF_BUF_SIZE[¶](https://docs.python.org/3/library/zlib.html#zlib.DEF_BUF_SIZE "Link to this definition")

The default buffer size for decompression operations.

zlib.Z_NO_COMPRESSION[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_NO_COMPRESSION "Link to this definition")

Compression level `0`; no compression.
Added in version 3.6.

zlib.Z_BEST_SPEED[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_SPEED "Link to this definition")

Compression level `1`; fastest and produces the least compression.

zlib.Z_BEST_COMPRESSION[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_COMPRESSION "Link to this definition")

Compression level `9`; slowest and produces the most compression.

zlib.Z_DEFAULT_COMPRESSION[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_DEFAULT_COMPRESSION "Link to this definition")

Default compression level (`-1`); a compromise between speed and compression. Currently equivalent to compression level `6`.

zlib.Z_DEFAULT_STRATEGY[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_DEFAULT_STRATEGY "Link to this definition")

Default compression strategy, for normal data.

zlib.Z_FILTERED[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_FILTERED "Link to this definition")

Compression strategy for data produced by a filter (or predictor).

zlib.Z_HUFFMAN_ONLY[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_HUFFMAN_ONLY "Link to this definition")

Compression strategy that forces Huffman coding only.

zlib.Z_RLE[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_RLE "Link to this definition")

Compression strategy that limits match distances to one (run-length encoding).
This constant is only available if Python was compiled with zlib 1.2.0.1 or greater.
Added in version 3.6.

zlib.Z_FIXED[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_FIXED "Link to this definition")

Compression strategy that prevents the use of dynamic Huffman codes.
This constant is only available if Python was compiled with zlib 1.2.2.2 or greater.
Added in version 3.6.

zlib.Z_NO_FLUSH[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_NO_FLUSH "Link to this definition")

Flush mode `0`. No special flushing behavior.
Added in version 3.6.

zlib.Z_PARTIAL_FLUSH[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_PARTIAL_FLUSH "Link to this definition")

Flush mode `1`. Flush as much output as possible.

zlib.Z_SYNC_FLUSH[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_SYNC_FLUSH "Link to this definition")

Flush mode `2`. All output is flushed and the output is aligned to a byte boundary.

zlib.Z_FULL_FLUSH[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_FULL_FLUSH "Link to this definition")

Flush mode `3`. All output is flushed and the compression state is reset.

zlib.Z_FINISH[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_FINISH "Link to this definition")

Flush mode `4`. All pending input is processed, no more input is expected.

zlib.Z_BLOCK[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_BLOCK "Link to this definition")

Flush mode `5`. A deflate block is completed and emitted.
This constant is only available if Python was compiled with zlib 1.2.2.2 or greater.
Added in version 3.6.

zlib.Z_TREES[¶](https://docs.python.org/3/library/zlib.html#zlib.Z_TREES "Link to this definition")

Flush mode `6`, for inflate operations. Instructs inflate to return when it gets to the next deflate block boundary.
This constant is only available if Python was compiled with zlib 1.2.3.4 or greater.
Added in version 3.6.
Information about the version of the zlib library in use is available through the following constants:

zlib.ZLIB_VERSION[¶](https://docs.python.org/3/library/zlib.html#zlib.ZLIB_VERSION "Link to this definition")

The version string of the zlib library that was used for building the module. This may be different from the zlib library actually used at runtime, which is available as [`ZLIB_RUNTIME_VERSION`](https://docs.python.org/3/library/zlib.html#zlib.ZLIB_RUNTIME_VERSION "zlib.ZLIB_RUNTIME_VERSION").

zlib.ZLIB_RUNTIME_VERSION[¶](https://docs.python.org/3/library/zlib.html#zlib.ZLIB_RUNTIME_VERSION "Link to this definition")

The version string of the zlib library actually loaded by the interpreter.
Added in version 3.3.

zlib.ZLIBNG_VERSION[¶](https://docs.python.org/3/library/zlib.html#zlib.ZLIBNG_VERSION "Link to this definition")

The version string of the zlib-ng library that was used for building the module if zlib-ng was used. When present, the [`ZLIB_VERSION`](https://docs.python.org/3/library/zlib.html#zlib.ZLIB_VERSION "zlib.ZLIB_VERSION") and [`ZLIB_RUNTIME_VERSION`](https://docs.python.org/3/library/zlib.html#zlib.ZLIB_RUNTIME_VERSION "zlib.ZLIB_RUNTIME_VERSION") constants reflect the version of the zlib API provided by zlib-ng.
If zlib-ng was not used to build the module, this constant will be absent.
Added in version 3.14.
See also

Module [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")

Reading and writing **gzip** -format files.
The zlib library home page.
The zlib manual explains the semantics and usage of the library’s many functions.
In case gzip (de)compression is a bottleneck, the
#### Previous topic
[`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html "previous chapter")
#### Next topic
[`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zlib+%E2%80%94+Compression+compatible+with+gzip&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzlib.html&pagesource=library%2Fzlib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/gzip.html "gzip — Support for gzip files") |
  * [previous](https://docs.python.org/3/library/compression.zstd.html "compression.zstd — Compression compatible with the Zstandard format") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
