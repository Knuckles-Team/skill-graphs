## Zstandard dictionaries[¶](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries "Link to this heading")

compression.zstd.train_dict(_samples_ , _dict_size_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "Link to this definition")

Train a Zstandard dictionary, returning a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") instance. Zstandard dictionaries enable more efficient compression of smaller sizes of data, which is traditionally difficult to compress due to less repetition. If you are compressing multiple similar groups of data (such as similar files), Zstandard dictionaries can improve compression ratios and speed significantly.
The _samples_ argument (an iterable of [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects), is the population of samples used to train the Zstandard dictionary.
The _dict_size_ argument, an integer, is the maximum size (in bytes) the Zstandard dictionary should be. The Zstandard documentation suggests an absolute maximum of no more than 100 KB, but the maximum can often be smaller depending on the data. Larger dictionaries generally slow down compression, but improve compression ratios. Smaller dictionaries lead to faster compression, but reduce the compression ratio.

compression.zstd.finalize_dict(_zstd_dict_ , _/_ , _samples_ , _dict_size_ , _level_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.finalize_dict "Link to this definition")

An advanced function for converting a “raw content” Zstandard dictionary into a regular Zstandard dictionary. “Raw content” dictionaries are a sequence of bytes that do not need to follow the structure of a normal Zstandard dictionary.
The _zstd_dict_ argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") instance with the [`dict_content`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_content "compression.zstd.ZstdDict.dict_content") containing the raw dictionary contents.
The _samples_ argument (an iterable of [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects), contains sample data for generating the Zstandard dictionary.
The _dict_size_ argument, an integer, is the maximum size (in bytes) the Zstandard dictionary should be. See [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") for suggestions on the maximum dictionary size.
The _level_ argument (an integer) is the compression level expected to be passed to the compressors using this dictionary. The dictionary information varies for each compression level, so tuning for the proper compression level can make compression more efficient.

_class_ compression.zstd.ZstdDict(_dict_content_ , _/_ , _*_ , _is_raw =False_)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "Link to this definition")

A wrapper around Zstandard dictionaries. Dictionaries can be used to improve the compression of many small chunks of data. Use [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") if you need to train a new dictionary from sample data.
The _dict_content_ argument (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)), is the already trained dictionary information.
The _is_raw_ argument, a boolean, is an advanced parameter controlling the meaning of _dict_content_. `True` means _dict_content_ is a “raw content” dictionary, without any format restrictions. `False` means _dict_content_ is an ordinary Zstandard dictionary, created from Zstandard functions, for example, [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") or the external **zstd** CLI.
When passing a `ZstdDict` to a function, the `as_digested_dict` and `as_undigested_dict` attributes can control how the dictionary is loaded by passing them as the `zstd_dict` argument, for example, `compress(data, zstd_dict=zd.as_digested_dict)`. Digesting a dictionary is a costly operation that occurs when loading a Zstandard dictionary. When making multiple calls to compression or decompression, passing a digested dictionary will reduce the overhead of loading the dictionary.
> Difference for compression[¶](https://docs.python.org/3/library/compression.zstd.html#id1 "Link to this table") | Digested dictionary | Undigested dictionary
> ---|---|---
> Advanced parameters of the compressor which may be overridden by the dictionary’s parameters | `window_log`, `hash_log`, `chain_log`, `search_log`, `min_match`, `target_length`, `strategy`, `enable_long_distance_matching`, `ldm_hash_log`, `ldm_min_match`, `ldm_bucket_size_log`, `ldm_hash_rate_log`, and some non-public parameters. | None
> `ZstdDict` internally caches the dictionary | Yes. It’s faster when loading a digested dictionary again with the same compression level. | No. If you wish to load an undigested dictionary multiple times, consider reusing a compressor object.
If passing a `ZstdDict` without any attribute, an undigested dictionary is passed by default when compressing and a digested dictionary is generated if necessary and passed by default when decompressing.
>

dict_content[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_content "Link to this definition")

> The content of the Zstandard dictionary, a `bytes` object. It’s the same as the _dict_content_ argument in the `__init__` method. It can be used with other programs, such as the `zstd` CLI program.

dict_id[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_id "Link to this definition")

> Identifier of the Zstandard dictionary, a non-negative int value.
> Non-zero means the dictionary is ordinary, created by Zstandard functions and following the Zstandard format.
> `0` means a “raw content” dictionary, free of any format restriction, used for advanced users.
> Note
> The meaning of `0` for `ZstdDict.dict_id` is different from the `dictionary_id` attribute to the [`get_frame_info()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.get_frame_info "compression.zstd.get_frame_info") function.

as_digested_dict[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.as_digested_dict "Link to this definition")

> Load as a digested dictionary.

as_undigested_dict[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.as_undigested_dict "Link to this definition")

> Load as an undigested dictionary.
