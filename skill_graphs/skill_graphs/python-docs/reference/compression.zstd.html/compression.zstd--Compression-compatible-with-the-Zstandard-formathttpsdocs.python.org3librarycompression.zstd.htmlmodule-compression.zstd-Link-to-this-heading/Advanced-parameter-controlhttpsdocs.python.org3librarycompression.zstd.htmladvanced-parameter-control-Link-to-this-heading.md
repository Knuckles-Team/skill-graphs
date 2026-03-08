## Advanced parameter control[¶](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control "Link to this heading")

_class_ compression.zstd.CompressionParameter[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") containing the advanced compression parameter keys that can be used when compressing data.
The [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "compression.zstd.CompressionParameter.bounds") method can be used on any attribute to get the valid values for that parameter.
Parameters are optional; any omitted parameter will have it’s value selected automatically.
Example getting the lower and upper bound of [`compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level"):
Copy```
lower, upper = CompressionParameter.compression_level.bounds()

```

Example setting the [`window_log`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "compression.zstd.CompressionParameter.window_log") to the maximum size:
Copy```
_lower, upper = CompressionParameter.window_log.bounds()
options = {CompressionParameter.window_log: upper}
compress(b'venezuelan beaver cheese', options=options)

```


bounds()[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "Link to this definition")

Return the tuple of int bounds, `(lower, upper)`, of a compression parameter. This method should be called on the attribute you wish to retrieve the bounds of. For example, to get the valid values for [`compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level"), one may check the result of `CompressionParameter.compression_level.bounds()`.
Both the lower and upper bounds are inclusive.

compression_level[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "Link to this definition")

A high-level means of setting other compression parameters that affect the speed and ratio of compressing data.
Regular compression levels are greater than `0`. Values greater than `20` are considered “ultra” compression and require more memory than other levels. Negative values can be used to trade off faster compression for worse compression ratios.
Setting the level to zero uses [`COMPRESSION_LEVEL_DEFAULT`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.COMPRESSION_LEVEL_DEFAULT "compression.zstd.COMPRESSION_LEVEL_DEFAULT").

window_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "Link to this definition")

Maximum allowed back-reference distance the compressor can use when compressing data, expressed as power of two, `1 << window_log` bytes. This parameter greatly influences the memory usage of compression. Higher values require more memory but gain better compression values.
A value of zero causes the value to be selected automatically.

hash_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.hash_log "Link to this definition")

Size of the initial probe table, as a power of two. The resulting memory usage is `1 << (hash_log+2)` bytes. Larger tables improve compression ratio of strategies <= [`dfast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "compression.zstd.Strategy.dfast"), and improve compression speed of strategies > `dfast`.
A value of zero causes the value to be selected automatically.

chain_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.chain_log "Link to this definition")

Size of the multi-probe search table, as a power of two. The resulting memory usage is `1 << (chain_log+2)` bytes. Larger tables result in better and slower compression. This parameter has no effect for the [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast") strategy. It’s still useful when using [`dfast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "compression.zstd.Strategy.dfast") strategy, in which case it defines a secondary probe table.
A value of zero causes the value to be selected automatically.

search_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.search_log "Link to this definition")

Number of search attempts, as a power of two. More attempts result in better and slower compression. This parameter is useless for [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast") and [`dfast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "compression.zstd.Strategy.dfast") strategies.
A value of zero causes the value to be selected automatically.

min_match[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.min_match "Link to this definition")

Minimum size of searched matches. Larger values increase compression and decompression speed, but decrease ratio. Note that Zstandard can still find matches of smaller size, it just tweaks its search algorithm to look for this size and larger. For all strategies < [`btopt`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "compression.zstd.Strategy.btopt"), the effective minimum is `4`; for all strategies > [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast"), the effective maximum is `6`.
A value of zero causes the value to be selected automatically.

target_length[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.target_length "Link to this definition")

The impact of this field depends on the selected [`Strategy`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "compression.zstd.Strategy").
For strategies [`btopt`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "compression.zstd.Strategy.btopt"), [`btultra`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra "compression.zstd.Strategy.btultra") and [`btultra2`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra2 "compression.zstd.Strategy.btultra2"), the value is the length of a match considered “good enough” to stop searching. Larger values make compression ratios better, but compresses slower.
For strategy [`fast`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "compression.zstd.Strategy.fast"), it is the distance between match sampling. Larger values make compression faster, but with a worse compression ratio.
A value of zero causes the value to be selected automatically.

strategy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.strategy "Link to this definition")

The higher the value of selected strategy, the more complex the compression technique used by zstd, resulting in higher compression ratios but slower compression.
See also
[`Strategy`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "compression.zstd.Strategy")

enable_long_distance_matching[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.enable_long_distance_matching "Link to this definition")

Long distance matching can be used to improve compression for large inputs by finding large matches at greater distances. It increases memory usage and window size.
`True` or `1` enable long distance matching while `False` or `0` disable it.
Enabling this parameter increases default [`window_log`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "compression.zstd.CompressionParameter.window_log") to 128 MiB except when expressly set to a different value. This setting is enabled by default if `window_log` >= 128 MiB and the compression strategy >= [`btopt`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "compression.zstd.Strategy.btopt") (compression level 16+).

ldm_hash_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_hash_log "Link to this definition")

Size of the table for long distance matching, as a power of two. Larger values increase memory usage and compression ratio, but decrease compression speed.
A value of zero causes the value to be selected automatically.

ldm_min_match[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_min_match "Link to this definition")

Minimum match size for long distance matcher. Larger or too small values can often decrease the compression ratio.
A value of zero causes the value to be selected automatically.

ldm_bucket_size_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_bucket_size_log "Link to this definition")

Log size of each bucket in the long distance matcher hash table for collision resolution. Larger values improve collision resolution but decrease compression speed.
A value of zero causes the value to be selected automatically.

ldm_hash_rate_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.ldm_hash_rate_log "Link to this definition")

Frequency of inserting/looking up entries into the long distance matcher hash table. Larger values improve compression speed. Deviating far from the default value will likely result in a compression ratio decrease.
A value of zero causes the value to be selected automatically.

content_size_flag[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.content_size_flag "Link to this definition")

Write the size of the data to be compressed into the Zstandard frame header when known prior to compressing.
This flag only takes effect under the following scenarios:
  * Calling [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "compression.zstd.compress") for one-shot compression
  * Providing all of the data to be compressed in the frame in a single [`ZstdCompressor.compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress") call, with the [`ZstdCompressor.FLUSH_FRAME`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.FLUSH_FRAME "compression.zstd.ZstdCompressor.FLUSH_FRAME") mode.
  * Calling [`ZstdCompressor.set_pledged_input_size()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.set_pledged_input_size "compression.zstd.ZstdCompressor.set_pledged_input_size") with the exact amount of data that will be provided to the compressor prior to any calls to [`ZstdCompressor.compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor.compress "compression.zstd.ZstdCompressor.compress") for the current frame. `ZstdCompressor.set_pledged_input_size()` must be called for each new frame.


All other compression calls may not write the size information into the frame header.
`True` or `1` enable the content size flag while `False` or `0` disable it.

checksum_flag[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.checksum_flag "Link to this definition")

A four-byte checksum using XXHash64 of the uncompressed content is written at the end of each frame. Zstandard’s decompression code verifies the checksum. If there is a mismatch a [`ZstdError`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdError "compression.zstd.ZstdError") exception is raised.
`True` or `1` enable checksum generation while `False` or `0` disable it.

dict_id_flag[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.dict_id_flag "Link to this definition")

When compressing with a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict"), the dictionary’s ID is written into the frame header.
`True` or `1` enable storing the dictionary ID while `False` or `0` disable it.

nb_workers[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.nb_workers "Link to this definition")

Select how many threads will be spawned to compress in parallel. When `nb_workers` > 0, enables multi-threaded compression, a value of `1` means “one-thread multi-threaded mode”. More workers improve speed, but also increase memory usage and slightly reduce compression ratio.
A value of zero disables multi-threading.

job_size[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.job_size "Link to this definition")

Size of a compression job, in bytes. This value is enforced only when [`nb_workers`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.nb_workers "compression.zstd.CompressionParameter.nb_workers") >= 1. Each compression job is completed in parallel, so this value can indirectly impact the number of active threads.
A value of zero causes the value to be selected automatically.

overlap_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.overlap_log "Link to this definition")

Sets how much data is reloaded from previous jobs (threads) for new jobs to be used by the look behind window during compression. This value is only used when [`nb_workers`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.nb_workers "compression.zstd.CompressionParameter.nb_workers") >= 1. Acceptable values vary from 0 to 9.
>   * 0 means dynamically set the overlap amount
>   * 1 means no overlap
>   * 9 means use a full window size from the previous job
>

Each increment halves/doubles the overlap size. “8” means an overlap of `window_size/2`, “7” means an overlap of `window_size/4`, etc.

_class_ compression.zstd.DecompressionParameter[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") containing the advanced decompression parameter keys that can be used when decompressing data. Parameters are optional; any omitted parameter will have it’s value selected automatically.
The [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.bounds "compression.zstd.DecompressionParameter.bounds") method can be used on any attribute to get the valid values for that parameter.
Example setting the [`window_log_max`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.window_log_max "compression.zstd.DecompressionParameter.window_log_max") to the maximum size:
Copy```
data = compress(b'Some very long buffer of bytes...')

_lower, upper = DecompressionParameter.window_log_max.bounds()

options = {DecompressionParameter.window_log_max: upper}
decompress(data, options=options)

```


bounds()[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.bounds "Link to this definition")

Return the tuple of int bounds, `(lower, upper)`, of a decompression parameter. This method should be called on the attribute you wish to retrieve the bounds of.
Both the lower and upper bounds are inclusive.

window_log_max[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter.window_log_max "Link to this definition")

The base-two logarithm of the maximum size of the window used during decompression. This can be useful to limit the amount of memory used when decompressing data. A larger maximum window size leads to faster decompression.
A value of zero causes the value to be selected automatically.

_class_ compression.zstd.Strategy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "Link to this definition")

An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") containing strategies for compression. Higher-numbered strategies correspond to more complex and slower compression.
Note
The values of attributes of `Strategy` are not necessarily stable across zstd versions. Only the ordering of the attributes may be relied upon. The attributes are listed below in order.
The following strategies are available:

fast[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.fast "Link to this definition")


dfast[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.dfast "Link to this definition")


greedy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.greedy "Link to this definition")


lazy[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.lazy "Link to this definition")


lazy2[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.lazy2 "Link to this definition")


btlazy2[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btlazy2 "Link to this definition")


btopt[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btopt "Link to this definition")


btultra[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra "Link to this definition")


btultra2[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy.btultra2 "Link to this definition")

## Miscellaneous[¶](https://docs.python.org/3/library/compression.zstd.html#miscellaneous "Link to this heading")

compression.zstd.get_frame_info(_frame_buffer_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.get_frame_info "Link to this definition")

Retrieve a [`FrameInfo`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo "compression.zstd.FrameInfo") object containing metadata about a Zstandard frame. Frames contain metadata related to the compressed data they hold.

_class_ compression.zstd.FrameInfo[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo "Link to this definition")

Metadata related to a Zstandard frame.

decompressed_size[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo.decompressed_size "Link to this definition")

The size of the decompressed contents of the frame.

dictionary_id[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo.dictionary_id "Link to this definition")

An integer representing the Zstandard dictionary ID needed for decompressing the frame. `0` means the dictionary ID was not recorded in the frame header. This may mean that a Zstandard dictionary is not needed, or that the ID of a required dictionary was not recorded.

compression.zstd.COMPRESSION_LEVEL_DEFAULT[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.COMPRESSION_LEVEL_DEFAULT "Link to this definition")

The default compression level for Zstandard: `3`.

compression.zstd.zstd_version_info[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.zstd_version_info "Link to this definition")

Version number of the runtime zstd library as a tuple of integers (major, minor, release).
## Examples[¶](https://docs.python.org/3/library/compression.zstd.html#examples "Link to this heading")
Reading in a compressed file:
Copy```
from compression import zstd

with zstd.open("file.zst") as f:
    file_content = f.read()

```

Creating a compressed file:
Copy```
from compression import zstd

data = b"Insert Data Here"
with zstd.open("file.zst", "w") as f:
    f.write(data)

```

Compressing data in memory:
Copy```
from compression import zstd

data_in = b"Insert Data Here"
data_out = zstd.compress(data_in)

```

Incremental compression:
Copy```
from compression import zstd

comp = zstd.ZstdCompressor()
out1 = comp.compress(b"Some data\n")
out2 = comp.compress(b"Another piece of data\n")
out3 = comp.compress(b"Even more data\n")
out4 = comp.flush()
